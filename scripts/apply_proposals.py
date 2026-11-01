#!/usr/bin/env python3
"""Apply the papers ticked in a review PR to README.md.

Reads the PR body (checkboxes and possibly edited section numbers), inserts
each approved entry into its subsection following CONTRIBUTING.md ordering
(published first, then unpublished; each by YYYY-MM, equal dates keep order),
bumps the category badge counts, and records approved/rejected status in the
proposals file so rejected papers are never proposed again.

  python3 scripts/apply_proposals.py --pr 12
  python3 scripts/apply_proposals.py --body-file scan/work/pr_body.md --dry-run
  python3 scripts/apply_proposals.py --check      # validate README ordering only
"""

import argparse
import json
import re
import sys

from common import (
    CATEGORY_BADGES, DATASET_SECTIONS, PROPOSALS_DIR, README, SECTIONS, collection_index,
    format_entry, is_known,
)

CHECKBOX = re.compile(r"^- \[([ xX])\] \*\*(C\d{3,4})\*\* · `?(\d\.\d|\?\.\?)`?[^\n]*?(?:· \+(\d\.\d))?\s*$", re.M)
MARKER = re.compile(r"<!-- paper-scan:(\d{4}-\d{2}-\d{2}) -->")
DATE = re.compile(r"\((\d{4})(?:-(\d{2}))?(?:,[^)]*)?\)")
UNPUBLISHED = re.compile(
    r"arXiv|SSRN|[Ww]orking [Pp]aper|research record|[Pp]reprint|Research Square|PsyArXiv|SocArXiv|OSF|NBER|"
    r"[Ff]orthcoming|[Mm]imeo|[Dd]raft|[Tt]echnical [Rr]eport|[Rr]esearch [Pp]aper|[Uu]npublished")


def entry_key(line):
    """(published, (year, month)) for a README list entry; month 13 when unverified."""
    head = line.split("[[link]]", 1)[0]
    quotes = [m.start() for m in re.finditer('"', head)]
    venue_part = head[quotes[1] + 1:] if len(quotes) >= 2 else head
    dates = DATE.findall(venue_part)
    year, month = (int(dates[-1][0]), int(dates[-1][1] or 13)) if dates else (9999, 13)
    venue = DATE.split(venue_part)[0].strip(" .")
    published = bool(venue) and not UNPUBLISHED.search(venue)
    return published, (year, month)


def section_span(lines, sec):
    head = next((i for i, l in enumerate(lines) if l.startswith(f"### {sec} ")), None)
    if head is None:
        raise KeyError(f"README has no '### {sec}' heading")
    end = next((i for i in range(head + 1, len(lines))
                if lines[i].startswith(("### ", "## ", "---"))), len(lines))
    return head, end


def section_entries(lines, sec):
    head, end = section_span(lines, sec)
    out, first = [], None
    for i in range(head + 1, end):
        if lines[i].startswith("<a id="):
            first = i if first is None else first
        elif lines[i].startswith("- "):
            out.append({"first": first if first is not None else i, "line": i, "key": entry_key(lines[i])})
            first = None
    return head, end, out


def insert_entry(lines, sec, anchors, entry):
    head, end, entries = section_entries(lines, sec)
    published, date = entry_key(entry)
    block = [f'<a id="{a}"></a>' for a in anchors] + ["", entry]
    group = [e for e in entries if e["key"][0] == published]
    earlier = [e for e in group if e["key"][1] <= date]
    if earlier:
        at = earlier[-1]["line"] + 1
        lines[at:at] = [""] + block
    elif group:
        at = group[0]["first"]
        lines[at:at] = block + [""]
    elif published and entries:  # first published entry goes before all unpublished ones
        at = entries[0]["first"]
        lines[at:at] = block + [""]
    elif entries:
        at = entries[-1]["line"] + 1
        lines[at:at] = [""] + block
    else:
        at = head + 2
        lines[at:at] = block + [""]


def bump_badges(text, added):
    for cat, n in added.items():
        if n:
            name = re.escape(CATEGORY_BADGES[cat])
            text = re.sub(rf"(badge/{name}-)(\d+)(-)", lambda m: f"{m.group(1)}{int(m.group(2)) + n}{m.group(3)}", text)
    return text


def check_readme():
    lines = README.read_text().split("\n")
    problems = []
    for sec in SECTIONS:
        _, _, entries = section_entries(lines, sec)
        keys = [e["key"] for e in entries]
        seen_unpub = False
        for (pub, date), e in zip(keys, entries):
            if not pub:
                seen_unpub = True
            elif seen_unpub:
                problems.append(f"{sec}: published entry after unpublished ones at line {e['line'] + 1}")
        for pub in (True, False):
            dates = [(d, e) for (p, d), e in zip(keys, entries) if p == pub]
            for (d0, _), (d1, e1) in zip(dates, dates[1:]):
                if d1 < d0:
                    problems.append(f"{sec}: {d1} after {d0} ({'published' if pub else 'unpublished'}) at line {e1['line'] + 1}")
    anchors = re.findall(r'<a id="([^"]+)"', "\n".join(lines))
    dupes = sorted({a for a in anchors if anchors.count(a) > 1})
    problems += [f"duplicate anchor: {a}" for a in dupes]
    return problems


def parse_review(body):
    marker = MARKER.search(body)
    if not marker:
        sys.exit("PR body has no <!-- paper-scan:DATE --> marker")
    ticks = {}
    for m in CHECKBOX.finditer(body):
        checked, cid, sec, ds = m.groups()
        ticks[cid] = {"checked": checked in "xX", "section": sec, "dataset_section": ds}
    return marker.group(1), ticks


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--pr", type=int)
    src.add_argument("--body-file")
    src.add_argument("--check", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if args.check:
        problems = check_readme()
        print("\n".join(problems) or "README ordering OK")
        sys.exit(1 if problems else 0)

    if args.pr:
        from gh_rest import get_pr
        body = get_pr(args.pr)["body"] or ""
    else:
        body = open(args.body_file).read()
    scan_date, ticks = parse_review(body)
    path = PROPOSALS_DIR / f"{scan_date}.json"
    doc = json.loads(path.read_text())

    baseline = {p.split(" at line")[0] for p in check_readme()}
    text = README.read_text()
    lines = text.split("\n")
    collection = collection_index()
    added, rejected, warnings = [], [], []
    per_cat = {"1": 0, "2": 0, "3": 0}

    for item in doc["items"]:
        if item["status"] not in ("proposed", "approved", "rejected") or item["decision"] == "exclude":
            continue
        tick = ticks.get(item["cid"])
        if tick is None:
            warnings.append(f"{item['cid']}: checkbox line not found in PR body; left unchanged")
            continue
        if not tick["checked"]:
            if item["status"] == "approved":
                warnings.append(f"{item['cid']}: unticked after being applied; remove it from README by hand if intended")
            else:
                item["status"] = "rejected"
                rejected.append(item["cid"])
            continue
        sec, ds = tick["section"], tick["dataset_section"]
        if sec not in SECTIONS:
            warnings.append(f"{item['cid']}: no valid section ('{sec}'); skipped")
            continue
        if item["anchor"] in collection["anchors"] or is_known(item["ids"], item["norm_title"], collection):
            if item["status"] != "approved":
                warnings.append(f"{item['cid']}: already in README; skipped")
            item["status"] = "approved"
            continue

        meta, dataset = item["meta"], item.get("dataset")
        anchors = [item["anchor"]]
        if sec in DATASET_SECTIONS:
            anchors.append(item.get("dataset_anchor") or item["anchor"].replace("paper-", "dataset-", 1))
            if not dataset:
                warnings.append(f"{item['cid']}: placed in dataset section {sec} without data description/link")
        insert_entry(lines, sec, anchors, format_entry(meta, dataset=dataset if sec in DATASET_SECTIONS else None))
        per_cat[sec[0]] += 1
        if ds and ds in DATASET_SECTIONS and ds != sec:
            if dataset:
                insert_entry(lines, ds, [item.get("dataset_anchor") or item["anchor"].replace("paper-", "dataset-", 1)],
                             format_entry(meta, link_title_to=f"#{item['anchor']}", dataset=dataset))
            else:
                warnings.append(f"{item['cid']}: +{ds} requested but no dataset description/link; add it by hand")
        item.update(status="approved", final_section=sec, final_dataset_section=ds)
        added.append({"cid": item["cid"], "section": sec, "title": meta["title"], "anchor": item["anchor"]})

    new_text = bump_badges("\n".join(lines), per_cat)
    summary = {"scan_date": scan_date, "added": added, "rejected": rejected, "warnings": warnings,
               "badge_increments": per_cat}
    if not args.dry_run:
        README.write_text(new_text)
        path.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n")
        new_problems = [p for p in check_readme() if p.split(" at line")[0] not in baseline]
        if new_problems:
            summary["new_ordering_problems"] = new_problems
    json.dump(summary, sys.stdout, ensure_ascii=False, indent=1)
    print()


if __name__ == "__main__":
    main()
