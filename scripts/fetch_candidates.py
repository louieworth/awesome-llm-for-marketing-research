#!/usr/bin/env python3
"""Fetch new candidate papers from arXiv and Crossref (SSRN + marketing journals).

Drops papers already in the collection or screened in an earlier scan, merges
versions of the same paper, ranks by keyword relevance, and writes
scan/work/candidates.json for the screening agents.
"""

import argparse
import datetime as dt
import hashlib
import html
import json
import re
import sys
import time
import xml.etree.ElementTree as ET

from common import (
    WORK_DIR, collection_index, history_index, http_get, http_json, ids_from_doi,
    is_known, load_config, normalize_title, scan_history,
)

ATOM = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom",
        "os": "http://a9.com/-/spec/opensearch/1.1/"}


def _term(field, t):
    return f'{field}:"{t}"' if re.search(r"[\s\-/]", t) else f"{field}:{t}"


def fetch_arxiv(cfg, terms, since, until, chunk_days=45):
    """arXiv API deep paging fails with HTTP 500 on large result sets, so query in date slices."""
    out, lo = [], since
    while lo <= until:
        hi = min(lo + dt.timedelta(days=chunk_days - 1), until)
        out += _fetch_arxiv_slice(cfg, terms, lo, hi)
        lo = hi + dt.timedelta(days=1)
    return out


def _fetch_arxiv_slice(cfg, terms, since, until):
    """One date slice; slices that ended before today are cached under scan/work/cache/."""
    key = hashlib.md5(json.dumps([cfg["categories"], terms["llm_terms"], terms["domain_terms"]]).encode()).hexdigest()[:8]
    cache = WORK_DIR / "cache" / f"arxiv_{since}_{until}_{key}.json"
    if cache.exists():
        return json.loads(cache.read_text())
    out = _query_arxiv_slice(cfg, terms, since, until)
    if until < dt.date.today():
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_text(json.dumps(out))
    return out


def _query_arxiv_slice(cfg, terms, since, until):
    cats = " OR ".join(f"cat:{c}" for c in cfg["categories"])
    llm = " OR ".join(_term("abs", t) for t in terms["llm_terms"])
    dom = " OR ".join(_term("abs", t) for t in terms["domain_terms"])
    query = (f"({cats}) AND ({llm}) AND ({dom}) AND "
             f"submittedDate:[{since:%Y%m%d}0000 TO {until:%Y%m%d}2359]")
    out, start, page = [], 0, 200
    while True:
        xml = http_get("https://export.arxiv.org/api/query", {
            "search_query": query, "start": start, "max_results": page,
            "sortBy": "submittedDate", "sortOrder": "descending"}, retries=6)
        root = ET.fromstring(xml)
        entries = root.findall("a:entry", ATOM)
        total = int(root.findtext("os:totalResults", "0", ATOM))
        for e in entries:
            arxiv_id = re.sub(r"v\d+$", "", e.findtext("a:id", "", ATOM).rsplit("/abs/", 1)[-1])
            ids = {f"arxiv:{arxiv_id}"}
            doi = e.findtext("arxiv:doi", None, ATOM)
            if doi:
                ids |= ids_from_doi(doi)
            out.append({
                "source": "arxiv",
                "title": " ".join(e.findtext("a:title", "", ATOM).split()),
                "authors": [a.findtext("a:name", "", ATOM) for a in e.findall("a:author", ATOM)],
                "date": e.findtext("a:published", "", ATOM)[:10],
                "venue": f"arXiv:{arxiv_id}",
                "journal_ref": e.findtext("arxiv:journal_ref", None, ATOM),
                "url": f"https://arxiv.org/abs/{arxiv_id}",
                "abstract": " ".join(e.findtext("a:summary", "", ATOM).split()),
                "categories": [c.get("term") for c in e.findall("a:category", ATOM)],
                "ids": sorted(ids),
            })
        start += len(entries)
        if not entries or start >= total:
            break
        time.sleep(3)  # arXiv API etiquette
    return out


def _date(*candidates):
    """Most precise Crossref date among candidates, as YYYY[-MM[-DD]]."""
    best = []
    for d in candidates:
        p = [x for x in (d or {}).get("date-parts", [[None]])[0] if x]
        if len(p) > len(best):
            best = p
    return "-".join(f"{x:02d}" if i else str(x) for i, x in enumerate(best))


def _strip_jats(s):
    s = html.unescape(html.unescape(s or ""))  # SSRN abstracts are often entity-escaped HTML
    return " ".join(re.sub(r"<[^>]+>", " ", s).split())


def fetch_crossref(cfg, filters, since, until, query=None, limit=None):
    """Crossref works matching filters whose DOI was created in [since, until].

    With `query`, results come in relevance order and stop after `limit`.
    """
    out, cursor = [], "*"
    params = {"mailto": cfg["mailto"]} if cfg.get("mailto") else {}
    if query:
        params["query.bibliographic"] = query
    limit = limit or cfg["max_records"]
    filt = ",".join(filters + [f"from-created-date:{since}", f"until-created-date:{until}"])
    select = "DOI,title,abstract,author,created,posted,published-online,published-print,container-title,volume,issue,page,type"
    while cursor and len(out) < limit:
        msg = http_json("https://api.crossref.org/works", {
            "filter": filt, "rows": min(1000, limit), "cursor": cursor, "select": select, **params})["message"]
        items = msg["items"]
        for it in items:
            title = " ".join(" ".join(it.get("title") or []).split())
            if not title:
                continue
            ids = ids_from_doi(it["DOI"])
            ssrn = next((i for i in ids if i.startswith("ssrn:")), None)
            journal = " ".join(it.get("container-title") or [])
            out.append({
                "source": "ssrn" if ssrn else "journal",
                "title": _strip_jats(title),
                "authors": [" ".join(filter(None, [a.get("given"), a.get("family")])) or a.get("name", "")
                            for a in it.get("author", [])],
                "date": _date(it.get("posted"), it.get("published-online"), it.get("created")),
                "venue": f"SSRN {ssrn[5:]}" if ssrn else journal,
                "url": (f"https://papers.ssrn.com/sol3/papers.cfm?abstract_id={ssrn[5:]}" if ssrn
                        else f"https://doi.org/{it['DOI']}"),
                "abstract": _strip_jats(it.get("abstract")),
                "ids": sorted(ids),
            })
        if not items:
            break
        cursor = msg.get("next-cursor")
    return out


def fill_abstracts(cands, cfg):
    """Fill missing journal abstracts from OpenAlex (Crossref lacks them for some publishers)."""
    wanted = [n.lower() for n in cfg["crossref"]["abstract_fill_journals"]]
    todo = [c for c in cands if c["source"] == "journal" and not c["abstract"]
            and any(w in c["venue"].lower() for w in wanted)]
    by_doi = {next(i[4:] for i in c["ids"] if i.startswith("doi:")): c for c in todo}
    dois, filled = list(by_doi), 0
    for k in range(0, len(dois), 50):
        batch = dois[k:k + 50]
        try:
            data = http_json("https://api.openalex.org/works", {
                "filter": "doi:" + "|".join(batch), "per-page": 50, "select": "doi,abstract_inverted_index"})
        except Exception as e:
            print(f"openalex abstract fill stopped: {e}", file=sys.stderr)
            break
        for w in data["results"]:
            c = by_doi.get((w.get("doi") or "").lower().removeprefix("https://doi.org/"))
            if c and w.get("abstract_inverted_index"):
                words = sorted((p, t) for t, ps in w["abstract_inverted_index"].items() for p in ps)
                c["abstract"] = " ".join(t for _, t in words)
                filled += 1
        time.sleep(1.5)
    return len(todo), filled


def in_focus(c, focus):
    """Backfill-only topical gate (scan/criteria.md tracks), applied before agent screening."""
    title, text = c["title"], f"{c['title']} {c['abstract']}"
    if focus["public_data"].search(text):
        return True
    if focus["human_sim"].search(text) and focus["consumer"].search(text):
        return True
    if focus["marketing_core"].search(title):
        return True
    return len({m.lower() for m in focus["marketing_core"].findall(c["abstract"])}) >= 2


def score(c, cfg, llm_re):
    title, abstract = c["title"].lower(), c["abstract"].lower()
    s = 0
    for t in cfg["domain_terms"]:
        pat = r"\b" + re.escape(t.lower()) + r"\b"
        if re.search(pat, title):
            s += 3
        elif re.search(pat, abstract):
            s += 1
    s += sum(2 for t in cfg["strong_terms"] if t.lower() in title or t.lower() in abstract)
    if c["source"] == "journal":
        s += 5
    if llm_re.search(c["title"]):
        s += 2
    return s


def merge_versions(cands):
    """Collapse arXiv / SSRN / journal records of the same paper; keep the published one first."""
    rank = {"journal": 0, "ssrn": 1, "arxiv": 2}
    groups = {}
    for c in sorted(cands, key=lambda c: rank[c["source"]]):
        key = normalize_title(c["title"])
        if key in groups:
            g = groups[key]
            g["ids"] = sorted(set(g["ids"]) | set(c["ids"]))
            g["versions"].append({k: c[k] for k in ("source", "venue", "url", "date")})
            if not g["abstract"] and c["abstract"]:
                g["abstract"] = c["abstract"]
        else:
            c["versions"] = [{k: c[k] for k in ("source", "venue", "url", "date")}]
            groups[key] = c
    return list(groups.values())


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--until", type=dt.date.fromisoformat, default=dt.date.today())
    ap.add_argument("--since", type=dt.date.fromisoformat)
    ap.add_argument("--max-screen", type=int)
    ap.add_argument("--skip", action="append", default=[], choices=["arxiv", "ssrn", "journals"])
    ap.add_argument("--no-git-fetch", action="store_true", help="do not fetch remote scan/* branches")
    ap.add_argument("--out", default=str(WORK_DIR / "candidates.json"))
    args = ap.parse_args()

    cfg = load_config()
    llm_re = re.compile(cfg["llm_regex"], re.I)
    collection = collection_index()
    history = history_index(scan_history(fetch_remote=not args.no_git_fetch))

    until = args.until
    if args.since:
        since = args.since
    else:
        since = until - dt.timedelta(days=cfg["lookback_days"])
        if history["last_scan"]:
            since = min(since, dt.date.fromisoformat(history["last_scan"]) - dt.timedelta(days=2))
        since = max(since, until - dt.timedelta(days=cfg["max_lookback_days"]))

    backfill = (until - since).days > cfg["backfill"]["min_window_days"]
    raw, stats = [], {"mode": "backfill" if backfill else "weekly"}
    if "arxiv" not in args.skip:
        got = fetch_arxiv(cfg["arxiv"], cfg, since, until)
        stats["fetched_arxiv"] = len(got)
        raw += got
    if "ssrn" not in args.skip:
        if backfill:  # all SSRN DOIs over years is ~10^5 records; use targeted relevance queries
            got = []
            for q in cfg["backfill"]["ssrn_queries"]:
                got += fetch_crossref(cfg["crossref"], ["prefix:10.2139"], since, until,
                                      query=q, limit=cfg["backfill"]["ssrn_top_per_query"])
                time.sleep(1)
            got = list({c["ids"][0]: c for c in got}.values())
        else:
            got = fetch_crossref(cfg["crossref"], ["prefix:10.2139"], since, until)
        stats["fetched_ssrn"] = len(got)
        raw += got
    if "journals" not in args.skip:
        issns = [f"issn:{i}" for i in cfg["crossref"]["journals"].values()]
        got = fetch_crossref(cfg["crossref"], issns, since, until)
        stats["fetched_journals"] = len(got)
        stats["abstracts_missing"], stats["abstracts_filled"] = fill_abstracts(got, cfg)
        raw += got

    # Literal LLM mention everywhere; a marketing/behavior term too outside marketing journals.
    dom_res = [re.compile(r"\b" + re.escape(t) + r"\b", re.I) for t in cfg["domain_terms"]]
    filtered = []
    for c in raw:
        text = f"{c['title']} {c['abstract']}"
        if not llm_re.search(text):
            continue
        if c["source"] != "journal" and not any(r.search(text) for r in dom_res):
            continue
        filtered.append(c)
    stats["keyword_match"] = len(filtered)
    if backfill:
        focus = {k: re.compile(v, re.I) for k, v in cfg["backfill"]["focus"].items()}
        filtered = [c for c in filtered if c["source"] == "journal" or in_focus(c, focus)]
        stats["focus_match"] = len(filtered)

    merged = merge_versions(filtered)
    fresh = []
    stats["already_in_collection"] = stats["already_screened"] = 0
    for c in merged:
        nt = normalize_title(c["title"])
        if is_known(c["ids"], nt, collection):
            stats["already_in_collection"] += 1
        elif is_known(c["ids"], nt, history):
            stats["already_screened"] += 1
        else:
            c["norm_title"] = nt
            fresh.append(c)
    stats["new"] = len(fresh)

    for c in fresh:
        c["prefilter_score"] = score(c, cfg, llm_re)
    fresh.sort(key=lambda c: (-c["prefilter_score"], c["date"]))
    cap = args.max_screen or cfg["max_screen"]
    screened, skipped = fresh[:cap], fresh[cap:]
    for i, c in enumerate(screened, 1):
        c["cid"] = f"C{i:03d}"
    stats["to_screen"] = len(screened)
    stats["over_cap"] = len(skipped)

    out = {
        "scan_date": until.isoformat(),
        "window": [since.isoformat(), until.isoformat()],
        "stats": stats,
        "candidates": screened,
        "over_cap": [{"title": c["title"], "url": c["url"], "prefilter_score": c["prefilter_score"]} for c in skipped],
    }
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    json.dump({"out": args.out, "window": out["window"], **stats}, sys.stdout, indent=1)
    print()


if __name__ == "__main__":
    main()
