#!/usr/bin/env python3
"""Exhaustive sweep of selected journals (default: UTD 24) for LLM / generative-AI papers.

Unlike fetch_candidates.py, this pulls every article the journals registered
in the window. It fills missing abstracts from OpenAlex, then Semantic
Scholar, matches a broader generative-AI pattern, and attaches citation
counts. Writes a candidates file compatible with build_proposals.py.

  python3 scripts/journal_sweep.py --since 2022-12-01 --until 2026-10-31
"""

import argparse
import datetime as dt
import json
import re
import sys
import time
import urllib.error

from common import (
    WORK_DIR, collection_index, history_index, http_json, is_known, load_config, normalize_title, scan_history,
)
from fetch_candidates import doi_of, fetch_crossref, s2_fill


def openalex_fill(cands):
    """Abstracts and citation counts from OpenAlex, 50 DOIs per request."""
    by = {doi_of(c): c for c in cands}
    dois = list(by)
    for k in range(0, len(dois), 50):
        batch = dois[k:k + 50]
        for attempt in range(5):
            try:
                data = http_json("https://api.openalex.org/works", {
                    "filter": "doi:" + "|".join(batch), "per-page": 50,
                    "select": "doi,cited_by_count,abstract_inverted_index"}, retries=1)
                break
            except urllib.error.HTTPError as e:
                if e.code != 429:
                    raise
                time.sleep(10 * (attempt + 1))
        else:
            print("openalex: giving up after repeated 429s", file=sys.stderr)
            return
        for w in data["results"]:
            c = by.get((w.get("doi") or "").lower().removeprefix("https://doi.org/"))
            if not c:
                continue
            c["citations"] = w.get("cited_by_count")
            inv = w.get("abstract_inverted_index")
            if inv and not c["abstract"]:
                c["abstract"] = " ".join(t for _, t in sorted((p, t) for t, ps in inv.items() for p in ps))
        time.sleep(1.2)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--since", type=dt.date.fromisoformat, required=True)
    ap.add_argument("--until", type=dt.date.fromisoformat, default=dt.date.today())
    ap.add_argument("--journals", default="utd24", help="key under scan_config 'journal_sets'")
    ap.add_argument("--out", default=str(WORK_DIR / "candidates_utd.json"))
    args = ap.parse_args()

    cfg = load_config()
    issns = cfg["journal_sets"][args.journals]
    raw = fetch_crossref(cfg["crossref"], [f"issn:{i}" for i in issns.values()], args.since, args.until)
    raw = [c for c in raw if c["source"] == "journal"]
    stats = {"fetched": len(raw), "abstract_missing_crossref": sum(not c["abstract"] for c in raw)}

    genai = re.compile(cfg["genai_regex"], re.I)
    need = [c for c in raw if not c["abstract"]]
    openalex_fill(need)
    s2_fill([c for c in need if not c["abstract"]])
    stats["abstract_missing_after_fill"] = sum(not c["abstract"] for c in raw)

    hits = [c for c in raw if genai.search(f"{c['title']} {c['abstract']}")]
    stats["genai_match"] = len(hits)
    missing_cites = [c for c in hits if c.get("citations") is None]
    openalex_fill(missing_cites)
    s2_fill([c for c in missing_cites if c.get("citations") is None])

    collection = collection_index()
    history = history_index(scan_history(fetch_remote=False))
    out = []
    for c in hits:
        nt = normalize_title(c["title"])
        c["norm_title"] = nt
        c["in_collection"] = is_known(c["ids"], nt, collection)
        c["previously_screened"] = is_known(c["ids"], nt, history)
        c["versions"] = [{k: c[k] for k in ("source", "venue", "url", "date")}]
        out.append(c)
    out.sort(key=lambda c: (c["in_collection"], c["venue"], c["date"]))
    for i, c in enumerate(out, 1):
        c["cid"] = f"U{i:03d}"
    stats["already_in_collection"] = sum(c["in_collection"] for c in out)
    stats["previously_screened"] = sum(c["previously_screened"] and not c["in_collection"] for c in out)
    doc = {"scan_date": args.until.isoformat(), "window": [args.since.isoformat(), args.until.isoformat()],
           "stats": stats, "candidates": [c for c in out if not c["in_collection"]],
           "in_collection": [{"title": c["title"], "venue": c["venue"]} for c in out if c["in_collection"]]}
    with open(args.out, "w") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    print(json.dumps({"out": args.out, **stats, "new_candidates": len(doc["candidates"])}))


if __name__ == "__main__":
    main()
