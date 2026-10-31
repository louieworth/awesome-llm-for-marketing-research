#!/usr/bin/env python3
"""Look up bibliographic records for one candidate (used by the citation-verifier agent).

Queries Crossref by title (structured authors, journal, volume/issue/pages,
online dates) and the arXiv API by ID, and prints compact JSON.

  python3 scripts/lookup.py --cid C003
  python3 scripts/lookup.py --title "Some paper title"
  python3 scripts/lookup.py --arxiv 2510.12345
  python3 scripts/lookup.py --doi 10.1287/mksc.2024.0990
"""

import argparse
import json
import sys
import xml.etree.ElementTree as ET

from common import WORK_DIR, http_get, http_json, normalize_title, titles_match

ATOM = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}


def _date(d):
    p = (d or {}).get("date-parts", [[None]])[0]
    return "-".join(f"{x:02d}" if i else str(x) for i, x in enumerate(p) if x) if p and p[0] else None


def crossref_record(it):
    return {
        "doi": it.get("DOI"),
        "type": it.get("type"),
        "title": " ".join(" ".join(it.get("title") or []).split()),
        "authors": [{"given": a.get("given", ""), "family": a.get("family") or a.get("name", "")}
                    for a in it.get("author", [])],
        "container": " ".join(it.get("container-title") or []),
        "volume": it.get("volume"), "issue": it.get("issue"), "page": it.get("page"),
        "published_online": _date(it.get("published-online")),
        "published_print": _date(it.get("published-print")),
        "posted": _date(it.get("posted")),
        "created": _date(it.get("created")),
        "relation": {k: [r.get("id") for r in v] for k, v in (it.get("relation") or {}).items()},
    }


def crossref_by_title(title, rows=8):
    msg = http_json("https://api.crossref.org/works", {"query.bibliographic": title, "rows": rows})["message"]
    nt = normalize_title(title)
    return [crossref_record(it) for it in msg["items"]
            if titles_match(nt, normalize_title(" ".join(it.get("title") or [""])))]


def crossref_by_doi(doi):
    return crossref_record(http_json(f"https://api.crossref.org/works/{doi}")["message"])


def arxiv_by_id(arxiv_id):
    root = ET.fromstring(http_get("https://export.arxiv.org/api/query", {"id_list": arxiv_id}))
    e = root.find("a:entry", ATOM)
    if e is None:
        return None
    return {
        "id": arxiv_id,
        "title": " ".join(e.findtext("a:title", "", ATOM).split()),
        "authors": [a.findtext("a:name", "", ATOM) for a in e.findall("a:author", ATOM)],
        "first_posted": e.findtext("a:published", "", ATOM)[:10],
        "updated": e.findtext("a:updated", "", ATOM)[:10],
        "journal_ref": e.findtext("arxiv:journal_ref", None, ATOM),
        "doi": e.findtext("arxiv:doi", None, ATOM),
        "comment": e.findtext("arxiv:comment", None, ATOM),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cid")
    ap.add_argument("--candidates", default=str(WORK_DIR / "candidates.json"))
    ap.add_argument("--title")
    ap.add_argument("--arxiv")
    ap.add_argument("--doi")
    args = ap.parse_args()

    title, arxiv_ids, dois = args.title, [args.arxiv] if args.arxiv else [], [args.doi] if args.doi else []
    if args.cid:
        cand = next(c for c in json.load(open(args.candidates))["candidates"] if c["cid"] == args.cid)
        title = title or cand["title"]
        arxiv_ids += [i[6:] for i in cand["ids"] if i.startswith("arxiv:")]
        dois += [i[4:] for i in cand["ids"] if i.startswith("doi:")]

    out = {"query_title": title, "crossref_title_matches": [], "crossref_doi": [], "arxiv": []}
    errors = []
    if title:
        try:
            out["crossref_title_matches"] = crossref_by_title(title)
        except Exception as e:
            errors.append(f"crossref title: {e}")
    for d in dict.fromkeys(dois):
        try:
            out["crossref_doi"].append(crossref_by_doi(d))
        except Exception as e:
            errors.append(f"crossref doi {d}: {e}")
    for a in dict.fromkeys(arxiv_ids):
        try:
            rec = arxiv_by_id(a)
            if rec:
                out["arxiv"].append(rec)
        except Exception as e:
            errors.append(f"arxiv {a}: {e}")
    if errors:
        out["errors"] = errors
    json.dump(out, sys.stdout, ensure_ascii=False, indent=1)
    print()


if __name__ == "__main__":
    main()
