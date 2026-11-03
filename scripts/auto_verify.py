#!/usr/bin/env python3
"""Script-only citation verification for large scans (backfill).

For each candidate ID, finds the canonical version via Crossref and the arXiv
API and writes README citation fields in the same shape as the
citation-verifier agent: a published journal or proceedings version when one
exists, otherwise the arXiv or SSRN preprint. Author affiliations are not
covered; those come from the affiliation agents (affil-*.json).

  python3 scripts/auto_verify.py --candidates scan/work/candidates_backfill.json --cids C001 C007 ...
  python3 scripts/auto_verify.py --candidates ... --passed      # every include/uncertain in screen-*.json
"""

import argparse
import html
import json
import re
import sys
import time
import xml.etree.ElementTree as ET

from common import WORK_DIR, http_get, normalize_title, titles_match
from lookup import ATOM, crossref_by_doi, crossref_by_title

PARTICLES = {"van", "von", "de", "der", "den", "da", "di", "del", "della", "le", "la", "du", "dos", "das", "ten", "ter"}
PUBLISHED_TYPES = ("journal-article", "proceedings-article", "book-chapter")


def split_name(name):
    parts = name.split()
    if len(parts) < 2:
        return {"given": "", "family": name}
    i = len(parts) - 1
    while i > 1 and parts[i - 1].lower() in PARTICLES:
        i -= 1
    return {"given": " ".join(parts[:i]), "family": " ".join(parts[i:])}


def arxiv_batch(ids):
    out = {}
    for k in range(0, len(ids), 100):
        root = ET.fromstring(http_get("https://export.arxiv.org/api/query",
                                      {"id_list": ",".join(ids[k:k + 100]), "max_results": 100}, retries=6))
        for e in root.findall("a:entry", ATOM):
            aid = re.sub(r"v\d+$", "", e.findtext("a:id", "", ATOM).rsplit("/abs/", 1)[-1])
            out[aid] = {
                "title": " ".join(e.findtext("a:title", "", ATOM).split()),
                "authors": [a.findtext("a:name", "", ATOM) for a in e.findall("a:author", ATOM)],
                "first_posted": e.findtext("a:published", "", ATOM)[:10],
                "journal_ref": e.findtext("arxiv:journal_ref", None, ATOM),
                "doi": e.findtext("arxiv:doi", None, ATOM),
            }
        time.sleep(3)
    return out


def venue_of(rec):
    v = rec["container"]
    if rec.get("volume"):
        v += f" {rec['volume']}"
        if rec.get("issue"):
            v += f"({rec['issue']})"
    if rec.get("page"):
        v += f": {rec['page'].replace('-', '–')}"
    return v.strip()


def clean(s):
    return " ".join(re.sub(r"<[^>]+>", " ", html.unescape(html.unescape(s or ""))).split())


def from_crossref(rec, published):
    dates = [rec.get(k) for k in ("published_online", "published_print", "posted", "created") if rec.get(k)]
    date = next((d for d in dates if len(d) >= 7), dates[0] if dates else "")
    # Crossref often lacks published-online for journals (e.g. INFORMS, Elsevier); the DOI
    # registration date then tracks the first online posting better than the print issue.
    created = rec.get("created") or ""
    if rec.get("type") == "journal-article" and not rec.get("published_online") and len(created) >= 7:
        date = min(date[:7], created[:7]) if len(date) >= 7 else created
    doi = rec["doi"]
    ssrn = re.match(r"10\.2139/ssrn\.(\d+)", doi or "", re.I)
    return {
        "title": clean(rec["title"]),
        "authors": [{"given": a["given"], "family": a["family"]} for a in rec["authors"]],
        "venue": f"SSRN {ssrn.group(1)}" if ssrn else venue_of(rec),
        "date": date[:7],
        "url": (f"https://papers.ssrn.com/sol3/papers.cfm?abstract_id={ssrn.group(1)}" if ssrn
                else f"https://doi.org/{doi}"),
        "published": published,
        "affiliations": [{"author": f"{a['given']} {a['family']}".strip(), "affiliation": "; ".join(a["affiliation"])}
                         for a in rec["authors"] if a.get("affiliation")],
    }


def verify(c, arxiv_rec):
    issues, checks = [], []
    published = None
    for doi in [i[4:] for i in c["ids"] if i.startswith("doi:") and "10.2139/" not in i and "10.48550/" not in i]:
        rec = crossref_by_doi(doi)
        if rec["type"] in PUBLISHED_TYPES:
            published = rec
            checks.append(f"Crossref DOI {doi}")
            break
    if not published:
        nt = normalize_title(c["title"])
        for rec in crossref_by_title(c["title"]):
            if rec["type"] in PUBLISHED_TYPES and titles_match(nt, normalize_title(rec["title"])):
                published = rec
                checks.append(f"Crossref 标题匹配到已发表版本 {rec['doi']}")
                break
        time.sleep(1)
    if published:
        out = from_crossref(published, True)
        if not out["date"]:
            issues.append("发表月份缺失")
    elif arxiv_rec:
        aid = c["venue"].removeprefix("arXiv:")
        out = {
            "title": arxiv_rec["title"],
            "authors": [split_name(a) for a in arxiv_rec["authors"]],
            "venue": f"arXiv:{aid}", "date": arxiv_rec["first_posted"][:7],
            "url": f"https://arxiv.org/abs/{aid}", "published": False, "affiliations": [],
        }
        checks.append("arXiv API（首次提交月）")
        issues.append("作者姓/名由 arXiv 全名自动拆分")
        if arxiv_rec.get("journal_ref"):
            issues.append(f"arXiv 标注已发表但未找到 DOI：{arxiv_rec['journal_ref']}")
    else:
        ssrn = next((i[4:] for i in c["ids"] if i.startswith("doi:10.2139/")), None)
        out = from_crossref(crossref_by_doi(ssrn), False) if ssrn else None
        if out:
            checks.append(f"Crossref SSRN DOI {ssrn}")
        else:
            return None
    out.update(cid=c["cid"], other_versions=[v["url"] for v in c.get("versions", []) if v["url"] != out["url"]],
               dataset=None, business_school=None,
               checks="自动核验：" + "；".join(checks), issues=issues, evidence="abstract-only")
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--candidates", required=True)
    ap.add_argument("--cids", nargs="*", default=[])
    ap.add_argument("--passed", action="store_true")
    ap.add_argument("--out", default=str(WORK_DIR / "verify-auto.json"))
    args = ap.parse_args()

    cands = {c["cid"]: c for c in json.load(open(args.candidates))["candidates"]}
    cids = list(args.cids)
    if args.passed:
        for p in sorted(WORK_DIR.glob("screen-*.json")):
            cids += [r["cid"] for r in json.loads(p.read_text()) if r["decision"] != "exclude"]
    cids = list(dict.fromkeys(cids))
    arx = arxiv_batch([cands[c]["venue"].removeprefix("arXiv:") for c in cids if cands[c]["source"] == "arxiv"])

    out, failed = [], []
    for cid in cids:
        c = cands[cid]
        try:
            v = verify(c, arx.get(c["venue"].removeprefix("arXiv:")) if c["source"] == "arxiv" else None)
        except Exception as e:
            print(f"{cid}: {e}", file=sys.stderr)
            v = None
        if v:
            out.append(v)
        else:
            failed.append(cid)
    json.dump(out, open(args.out, "w"), ensure_ascii=False, indent=1)
    print(json.dumps({"verified": len(out), "published": sum(v["published"] for v in out), "failed": failed}))


if __name__ == "__main__":
    main()
