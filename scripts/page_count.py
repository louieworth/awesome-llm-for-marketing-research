#!/usr/bin/env python3
"""Count the pages of arXiv preprints that passed screening (scan/criteria.md, "Length").

Only papers whose verified version is an arXiv preprint are counted; journal
articles and SSRN working papers are exempt. Pages are counted on the full
arXiv PDF, references and appendices included.

  python3 scripts/page_count.py            # writes scan/work/pages.json  {cid: pages or null}
"""

import json
import re
import sys
import time
import zlib

from common import WORK_DIR, http_get


def _stdlib_count(data):
    """Page count from the page tree: the largest /Count of a /Type /Pages node.

    Looks in the raw file and in every Flate-compressed stream, which covers
    PDFs that keep the page tree in compressed object streams.
    """
    chunks = [data]
    for m in re.finditer(rb"stream\r?\n", data):
        start = m.end()
        try:
            chunks.append(zlib.decompressobj().decompress(data[start:start + 4_000_000]))
        except zlib.error:
            continue
    best = 0
    for chunk in chunks:
        for m in re.finditer(rb"/Type\s*/Pages\b", chunk):
            # the page-tree dictionary holding this /Type (page-tree nodes have no nested dictionaries)
            start, end = chunk.rfind(b"<<", 0, m.start()), chunk.find(b">>", m.end())
            if start < 0 or end < 0:
                continue
            for n in re.findall(rb"/Count\s+(\d+)", chunk[start:end]):
                best = max(best, int(n))
    return best or None


def pdf_page_count(data):
    if not data.startswith(b"%PDF"):
        return None
    try:
        import io
        import pypdf  # optional; the stdlib parser is the fallback
        return len(pypdf.PdfReader(io.BytesIO(data)).pages)
    except Exception:
        return _stdlib_count(data)


def arxiv_pages(aid):
    data = http_get(f"https://arxiv.org/pdf/{aid}", retries=4, timeout=120)
    return pdf_page_count(data)


def main():
    screen, verify = {}, {}
    for p in sorted(WORK_DIR.glob("screen-*.json")):
        screen.update({r["cid"]: r for r in json.loads(p.read_text())})
    for p in sorted(WORK_DIR.glob("verify-*.json")):
        verify.update({r["cid"]: r for r in json.loads(p.read_text())})
    cands = {c["cid"]: c for c in json.loads((WORK_DIR / "candidates.json").read_text())["candidates"]}
    out = {}
    for cid, s in screen.items():
        if s["decision"] == "exclude" or cid not in cands:
            continue
        venue = (verify.get(cid) or {}).get("venue") or cands[cid]["venue"]
        if not venue.startswith("arXiv:"):
            continue
        aid = re.sub(r"v\d+$", "", venue.removeprefix("arXiv:"))
        try:
            out[cid] = arxiv_pages(aid)
        except Exception as e:
            print(f"{cid} arXiv:{aid}: {e}", file=sys.stderr)
            out[cid] = None
        time.sleep(3)
    (WORK_DIR / "pages.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps({"counted": sum(v is not None for v in out.values()), "failed": [c for c, v in out.items() if v is None],
                      "short": sorted(c for c, v in out.items() if v is not None and v < 20)}))


if __name__ == "__main__":
    main()
