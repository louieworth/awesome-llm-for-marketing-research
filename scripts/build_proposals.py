#!/usr/bin/env python3
"""Merge agent outputs into scan/proposals/<date>.json and render the review PR body.

Reads scan/work/candidates.json plus the agents' screen-*.json,
classify-*.json and verify-*.json files.
"""

import argparse
import datetime as dt
import html
import json
import re
import sys

from common import (
    PROPOSALS_DIR, SECTIONS, WORK_DIR, collection_index, format_entry, ids_from_text, is_known, load_config,
    make_anchor, normalize_title,
)

TRACK_LABEL = {"consumer_simulation": "A consumer simulation", "human_simulation": "B human simulation (digital twin)",
               "public_data_simulation": "B public-data human simulation",
               "marketing_method": "C marketing method", "utd": "UTD journal"}
TIER_LABEL = {1: "tier 1 UTD journal", 2: "tier 2 business-school author", 3: "tier 3 high impact",
              "B-published": "bar: peer-reviewed", "B-cited": "bar: highly cited"}


def load_agent_files(pattern):
    merged = {}
    for p in sorted(WORK_DIR.glob(pattern)):
        for row in json.loads(p.read_text()):
            merged[row["cid"]] = row
    return merged


def fallback_meta(c):
    """Unverified citation fields from the raw candidate record."""
    def split(name):
        parts = name.split()
        return {"given": " ".join(parts[:-1]), "family": parts[-1]} if parts else {"given": "", "family": name}
    return {"title": c["title"], "authors": [split(a) for a in c["authors"]], "venue": c["venue"],
            "date": c["date"][:7], "url": c["url"]}


def is_utd(venue, cfg):
    """Journal name is the venue text before its volume number, e.g. 'Management Science 72(3): 1–20'."""
    name = re.split(r"\s+\d", html.unescape(venue))[0].strip().lower().removeprefix("the ")
    return name in {n.lower().removeprefix("the ") for n in cfg["journal_sets"]["utd24"]}


def influential(item, cfg):
    cites = item.get("citations") or 0
    try:
        years = max(0.5, (dt.date.today() - dt.date.fromisoformat(item["date"][:10].ljust(10, "-")[:7] + "-01")).days / 365)
    except ValueError:
        years = 1.0
    inf = cfg["influence"]
    return cites >= inf["min_citations"] or cites / years >= inf["min_citations_per_year"]


MINOR_VENUE = re.compile(r"\b(workshops?|companion|lecture notes|extended abstracts?|doctoral consortium)\b", re.I)


def apply_human_sim_bar(item, cfg):
    """scan/criteria.md track B: human simulation without a marketing setting. Returns True when excluded.

    The paper must be published in a peer-reviewed venue (verified; workshops, companion proceedings and
    proceedings series do not count) or be influential (citations). The bar replaces the business-school
    author tiers for this track.
    """
    if item["published"] and not MINOR_VENUE.search(item["meta"]["venue"]):
        item["tier"] = "B-published"
        return False
    if influential(item, cfg):
        item["tier"] = "B-cited"
        return False
    inf = cfg["influence"]
    item.update(status="excluded", decision="exclude",
                reason=f"Human simulation without a marketing setting needs a peer-reviewed venue or at least "
                       f"{inf['min_citations']} citations ({inf['min_citations_per_year']} a year); this is unpublished "
                       f"with {item.get('citations') or 0} citations. {item['reason']}")
    return True


def apply_tier_rules(item, cfg):
    """scan/criteria.md tiers (tracks A and C; track B uses apply_human_sim_bar). Returns True when excluded.

    Tier 1: UTD 24 journal papers pass regardless of affiliation.
    Tier 2: other papers need a business-school author.
    Tier 3: without one, only influential (citations) or screener-flagged notable papers pass.
    """
    if item.get("track") == "human_simulation":
        return apply_human_sim_bar(item, cfg)
    item["tier"] = 1 if is_utd(item["meta"]["venue"], cfg) else 2
    if item["tier"] == 1 or item["business_school"] is True:
        return False
    if influential(item, cfg) or item.get("notable"):
        item["tier"] = 3
        why = f"{item.get('citations') or 0} citations" if influential(item, cfg) else f"notable: {item.get('notable_reason', '')}"
        item["issues"] = item["issues"] + [f"No business-school author; included under tier 3 ({why})"]
        return False
    if item["business_school"] is False:
        item.update(status="excluded", decision="exclude",
                    reason=f"No business-school author and limited impact ({item.get('citations') or 0} citations); "
                           f"affiliations: {affiliation_summary(item) or 'unknown'}. {item['reason']}")
        return True
    item["decision"] = "uncertain"
    item["issues"] = item["issues"] + ["Business-school authorship not confirmed"]
    return False


def apply_length_rule(item, pages, cfg):
    """scan/criteria.md "Length": arXiv preprints need a minimum page count. Returns True when excluded.

    Journal articles and SSRN working papers are exempt. `pages` comes from scripts/page_count.py.
    """
    if not item["meta"]["venue"].startswith("arXiv:"):
        return False
    need = cfg["min_pages"]["arxiv"]
    item["pages"] = pages
    if pages is None:
        item["issues"] = item["issues"] + [f"Page count not checked (arXiv papers need at least {need} pages)"]
        return False
    if pages < need:
        item.update(status="excluded", decision="exclude",
                    reason=f"Only {pages} pages in the arXiv PDF, references and appendices included; "
                           f"arXiv papers need at least {need}. {item['reason']}")
        return True
    return False


def affiliation_summary(item, limit=4):
    seen = list(dict.fromkeys(a.get("affiliation") or "?" for a in item.get("affiliations", [])))
    return "; ".join(seen[:limit]) + ("…" if len(seen) > limit else "")


def build(candidates_doc):
    screen = load_agent_files("screen-*.json")
    classify = load_agent_files("classify-*.json")
    verify = load_agent_files("verify-*.json")
    affil = load_agent_files("affil-*.json")
    cites_file = WORK_DIR / "citations.json"
    cites = json.loads(cites_file.read_text()) if cites_file.exists() else {}
    pages_file = WORK_DIR / "pages.json"
    pages = json.loads(pages_file.read_text()) if pages_file.exists() else {}
    cfg = load_config()
    collection = collection_index()
    used = set(collection["anchors"])
    items, missing = [], []

    for c in candidates_doc["candidates"]:
        cid = c["cid"]
        s = screen.get(cid)
        if not s:
            missing.append(cid)
            continue
        item = {
            "cid": cid, "title": c["title"], "ids": c["ids"], "norm_title": c["norm_title"],
            "source": c["source"], "url": c["url"], "date": c["date"],
            "decision": s["decision"], "reason": s.get("reason", ""), "track": s.get("track", ""),
            "llm_use": s.get("llm_use", ""), "human_data": s.get("human_data", ""),
            "evidence": s.get("evidence", "abstract-only"),
            "citations": cites.get(cid, c.get("citations")),
            "notable": s.get("notable", False), "notable_reason": s.get("notable_reason", ""),
        }
        if s["decision"] == "exclude":
            item["status"] = "excluded"
            items.append(item)
            continue

        item["status"] = "proposed"
        cl = classify.get(cid) or s  # backfill screeners classify in the same pass
        item["section"] = cl.get("section")
        item["dataset_section"] = cl.get("dataset_section")
        item["classification"] = cl.get("rationale", "")
        item["confidence"] = cl.get("confidence", "low")

        v = verify.get(cid)
        meta = ({k: v[k] for k in ("title", "authors", "venue", "date", "url")} if v else fallback_meta(c))
        item["verified"] = bool(v)
        item["published"] = bool(v and v.get("published"))
        item["verification"] = v.get("checks", "") if v else "Not verified: citation details come from the raw fetched record"
        item["issues"] = v.get("issues", []) if v else ["Not checked by citation-verifier"]
        if v and v.get("evidence"):
            item["evidence"] = v["evidence"]
        item["meta"] = meta
        item["dataset"] = v.get("dataset") if v else None
        item["affiliations"] = v.get("affiliations", []) if v else []
        item["business_school"] = v.get("business_school") if v else None
        if cid in affil:  # backfill: affiliations checked separately from script-only verification
            item["affiliations"] = affil[cid].get("affiliations", [])
            item["business_school"] = affil[cid].get("business_school")
        if is_known(set(c["ids"]) | ids_from_text(meta["url"]), normalize_title(meta["title"]), collection):
            item.update(status="excluded", decision="exclude",
                        reason=f"Already in the README (verified match: {meta['venue'] or meta['url']}). {item['reason']}")
            items.append(item)
            continue
        if apply_length_rule(item, pages.get(cid), cfg) or apply_tier_rules(item, cfg):
            items.append(item)
            continue

        anchor = make_anchor(meta["title"])
        base, n = anchor, 2
        while anchor in used:
            anchor, n = f"{base}-{n}", n + 1
        used.add(anchor)
        item["anchor"] = anchor
        if item["dataset_section"] or (item["section"] in ("1.4", "2.3", "3.3")):
            item["dataset_anchor"] = make_anchor(meta["title"], "dataset-")
        items.append(item)

    return items, missing


def render_entry(item):
    in_dataset = item.get("section") in ("1.4", "2.3", "3.3")
    return format_entry(item["meta"], dataset=item.get("dataset") if in_dataset else None)


def section_label(sec):
    return f"{sec} {SECTIONS[sec]}" if sec in SECTIONS else "?.? unclassified (fill in a section)"


def render_item(item):
    head = f"- [ ] **{item['cid']}** · {section_label(item.get('section'))}"
    if item.get("dataset_section"):
        head += f" · +{item['dataset_section']}"
    lines = [head, f"  - Entry: {render_entry(item).removeprefix('- ')}", f"  - Reason: {item['reason']}"]
    bs = {True: "business-school author ✓", False: "no business-school author",
          None: "business-school author unconfirmed"}[item.get("business_school")]
    track = TRACK_LABEL.get(item.get("track"), "")
    tier = TIER_LABEL.get(item.get("tier"), "")
    cites = item.get("citations")
    pages = f" · {item['pages']} pages" if item.get("pages") else ""
    lines.append(f"  - Route: {track} · {tier} · citations {cites if cites is not None else '?'}{pages}"
                 f" · affiliations: {affiliation_summary(item) or 'unknown'} ({bs})")
    if item.get("classification"):
        lines.append(f"  - Classification: {item['classification']} (confidence: {item['confidence']})")
    lines.append(f"  - Verification: {item['verification']} · evidence: {item['evidence']}")
    if item.get("issues"):
        lines.append(f"  - ⚠️ To confirm: {'; '.join(i.rstrip('。；;. ') for i in item['issues'])}")
    return "\n".join(lines)


def render_body(doc, over_cap):
    items = doc["items"]
    inc = [i for i in items if i["decision"] == "include"]
    unc = [i for i in items if i["decision"] == "uncertain"]
    exc = [i for i in items if i["decision"] == "exclude"]
    order = lambda i: (i.get("section") or "9", i["cid"])
    st = doc["stats"]
    fetched = " · ".join(f"{k.removeprefix('fetched_')} {v}" for k, v in st.items() if k.startswith("fetched_"))
    out = [
        f"<!-- paper-scan:{doc['scan_date']} -->",
        f"## 📚 Paper scan {doc['scan_date']}",
        "",
        f"Window {doc['window'][0]} → {doc['window'][1]} · fetched {fetched} · keyword matches {st.get('keyword_match', 0)}"
        f" · already listed {st.get('already_in_collection', 0)} · already screened {st.get('already_screened', 0)}"
        f" · screened by agents {st.get('to_screen', 0)} ({st.get('over_cap', 0)} over the cap, not screened)",
        "",
        f"**Proposed {len(inc)} · uncertain {len(unc)} · excluded {len(exc)}**",
        "",
        "**How to review**: tick the papers to include. To move a paper, edit its section number such as `1.2` "
        "(`+1.4` also lists it in the dataset subsection; delete that to skip it). When done, add the `apply` label to "
        "this PR. Apply writes the ticked entries into the README and pushes them to this PR; check the diff under "
        "Files changed, then merge. Unticked papers are recorded as rejected and will not be proposed again. Merge the "
        "PR even if nothing is included, so the review stays on record; do not just close it.",
        "",
    ]
    if inc:
        out += [f"### ✅ Proposed ({len(inc)})", ""] + [render_item(i) + "\n" for i in sorted(inc, key=order)]
    if unc:
        out += [f"### ❓ Uncertain ({len(unc)})", ""] + [render_item(i) + "\n" for i in sorted(unc, key=order)]
    if exc:
        out += [f"<details><summary>❌ Excluded ({len(exc)})</summary>", ""]
        out += [f"- {i['cid']} [{i['title']}]({i['url']}) — {i['reason']}" for i in exc]
        out += ["", "</details>", ""]
    if over_cap:
        out += [f"<details><summary>⏭️ Over the screening cap, not sent to agents ({len(over_cap)})</summary>", ""]
        out += [f"- [{c['title']}]({c['url']})" for c in over_cap]
        out += ["", "</details>", ""]
    return "\n".join(out)


def render_compact(doc, details_url, reason_chars=60):
    """One checkbox line per paper, grouped by section, for scans too large for a PR body."""
    items = [i for i in doc["items"] if i["decision"] != "exclude"]
    n_exc = sum(i["decision"] == "exclude" for i in doc["items"])
    full = render_body(doc, []).split("**How to review**", 1)
    out = [full[0].rstrip(), "",
           f"Full reasons, affiliations, verification details and the {n_exc} excluded papers are in "
           f"[{doc['scan_date']}.md]({details_url}). The second line under each paper is a shortened reason; "
           "⚠️ marks items to confirm and 🏫 marks a business-school author.", "",
           "**How to review**" + full[1].split("\n", 1)[0], ""]
    for label, dec in (("✅ Proposed", "include"), ("❓ Uncertain", "uncertain")):
        group = sorted((i for i in items if i["decision"] == dec), key=lambda i: (i.get("section") or "9", i["cid"]))
        if not group:
            continue
        out += [f"### {label} ({len(group)})", ""]
        current = None
        for i in group:
            if i.get("section") != current:
                current = i.get("section")
                out += [f"#### {section_label(current)}", ""]
            meta = i["meta"]
            flags = ("⚠️" if i.get("issues") else "") + ("🏫" if i.get("business_school") else "")
            line = (f"- [ ] **{i['cid']}** · {i.get('section') or '?.?'} · [{meta['title']}]({meta['url']})"
                    f" · {meta['venue'][:32]} {meta['date']} {flags}".rstrip())
            if i.get("dataset_section"):
                line += f" · +{i['dataset_section']}"
            out.append(line)
            if reason_chars:
                r = i["reason"]
                out.append(f"  {r[:reason_chars]}{'…' if len(r) > reason_chars else ''}")
        out.append("")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--candidates", default=str(WORK_DIR / "candidates.json"))
    ap.add_argument("--body-out", default=str(WORK_DIR / "pr_body.md"))
    ap.add_argument("--branch", help="review branch name, for the details link (default scan/<date>)")
    ap.add_argument("--list-passed", action="store_true",
                    help="print IDs screened include/uncertain (for classify and verify batches) and exit")
    args = ap.parse_args()

    if args.list_passed:
        screen = load_agent_files("screen-*.json")
        print(" ".join(sorted(c for c, s in screen.items() if s["decision"] != "exclude")))
        return

    cand = json.load(open(args.candidates))
    items, missing = build(cand)
    if missing:
        sys.exit(f"screening output missing for: {', '.join(missing)}")
    doc = {"scan_date": cand["scan_date"], "window": cand["window"], "stats": cand["stats"], "items": items}
    PROPOSALS_DIR.mkdir(parents=True, exist_ok=True)
    path = PROPOSALS_DIR / f"{cand['scan_date']}.json"
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n")
    body = render_body(doc, cand.get("over_cap", []))
    if len(body) > 60000:  # GitHub caps PR bodies at 65,536 characters
        details = PROPOSALS_DIR / f"{cand['scan_date']}.md"
        details.write_text(body + "\n")
        from gh_rest import repo_slug
        url = f"https://github.com/{repo_slug()}/blob/{args.branch or 'scan/' + cand['scan_date']}/scan/proposals/{details.name}"
        for chars in (60, 30, 0):
            body = render_compact(doc, url, chars)
            if len(body) <= 60000:
                break
    open(args.body_out, "w").write(body)
    n = {d: sum(i["decision"] == d for i in items) for d in ("include", "uncertain", "exclude")}
    print(json.dumps({"proposals": str(path), "pr_body": args.body_out, "body_chars": len(body), **n}))


if __name__ == "__main__":
    main()
