"""Shared helpers for the paper-scan pipeline. Standard library only."""

import difflib
import json
import re
import subprocess
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
INDEXED_DOCS = [
    README,
    ROOT / "docs" / "consumer-simulation-method-supplement.md",
    ROOT / "docs" / "consumer-simulation-review.md",
]
CONFIG_PATH = Path(__file__).resolve().parent / "scan_config.json"
SCAN_DIR = ROOT / "scan"
WORK_DIR = SCAN_DIR / "work"
PROPOSALS_DIR = SCAN_DIR / "proposals"

SECTIONS = {
    "1.1": "Capabilities and Opportunities",
    "1.2": "Validity and Limitations",
    "1.3": "Methods and Improvements",
    "1.4": "Benchmarks and Datasets",
    "2.1": "Market Effects and Limitations",
    "2.2": "Methods and Improvements",
    "2.3": "Benchmarks and Datasets",
    "3.1": "Performance and Limitations",
    "3.2": "Methods and Improvements",
    "3.3": "Benchmarks and Datasets",
}
DATASET_SECTIONS = {"1.4", "2.3", "3.3"}
CATEGORY_BADGES = {
    "1": "Consumer_Simulation",
    "2": "Content_Generation_and_Personalization",
    "3": "Model_%26_Algorithm_Augmentation",
}
MAX_FULL_AUTHORS = 4
USER_AGENT = "awesome-llm-for-marketing-research paper-scan (+https://github.com/louieworth/awesome-llm-for-marketing-research)"


def load_config():
    return json.loads(CONFIG_PATH.read_text())


# ---------- text normalization ----------

TITLE_PREFIXES = ("frontiers:", "database report:", "research note:", "commentary:")


def normalize_title(title):
    t = re.sub(r"[‐-―]", "-", title)
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower().strip()
    for p in TITLE_PREFIXES:
        if t.startswith(p):
            t = t[len(p):]
    return re.sub(r"[^a-z0-9]+", " ", t).strip()


def make_anchor(title, prefix="paper-"):
    t = re.sub(r"[‐-―]", "-", title)
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    t = re.sub(r"['’‘]", "", t)
    return prefix + re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def titles_match(a, b):
    """a, b are normalized titles."""
    if a == b:
        return True
    if min(len(a), len(b)) < 20:
        return False
    sm = difflib.SequenceMatcher(None, a, b)
    return sm.quick_ratio() > 0.92 and sm.ratio() > 0.92


# ---------- identifiers ----------

def ids_from_doi(doi):
    doi = doi.lower().strip().rstrip(".")
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi)
    out = {f"doi:{doi}"}
    m = re.match(r"10\.2139/ssrn\.(\d+)", doi)
    if m:
        out.add(f"ssrn:{m.group(1)}")
    m = re.match(r"10\.48550/arxiv\.(\d{4}\.\d{4,5})", doi)
    if m:
        out.add(f"arxiv:{m.group(1)}")
    return out


def ids_from_text(text):
    ids = set()
    ids |= {f"arxiv:{m}" for m in re.findall(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})", text)}
    ids |= {f"arxiv:{m}" for m in re.findall(r"arXiv[: ](\d{4}\.\d{4,5})", text)}
    ids |= {f"ssrn:{m}" for m in re.findall(r"abstract_id=(\d+)", text)}
    ids |= {f"ssrn:{m}" for m in re.findall(r"SSRN (\d{6,8})", text)}
    for m in re.findall(r"doi\.org/(10\.[^\s)\]>\"]+)", text):
        ids |= ids_from_doi(m)
    return ids


QUOTED_TITLE = re.compile(r'"\[?([^"\[\]]{12,}?)\]?(?:\([^)]*\))?\.?"')


def collection_index():
    """IDs and normalized titles of every paper already in the collection or its audits."""
    ids, titles = set(), set()
    for path in INDEXED_DOCS:
        if not path.exists():
            continue
        text = path.read_text()
        ids |= ids_from_text(text)
        titles |= {normalize_title(m) for m in QUOTED_TITLE.findall(text)}
    anchors = set(re.findall(r'<a id="([^"]+)"', README.read_text()))
    return {"ids": ids, "titles": titles, "anchors": anchors}


def _git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True)


def scan_history(fetch_remote=True):
    """Every proposals file on this checkout and on remote scan/* branches (open review PRs)."""
    if fetch_remote:
        _git("fetch", "--quiet", "origin", "+refs/heads/scan/*:refs/remotes/origin/scan/*")
    docs = {}
    for p in sorted(PROPOSALS_DIR.glob("*.json")):
        docs[p.name] = json.loads(p.read_text())
    refs = _git("for-each-ref", "--format=%(refname)", "refs/remotes/origin/scan/").stdout.split()
    for ref in refs:
        names = _git("ls-tree", "--name-only", ref, "scan/proposals/").stdout.split()
        for name in names:
            if not name.endswith(".json"):
                continue
            base = Path(name).name
            if base in docs:
                continue
            shown = _git("show", f"{ref}:{name}")
            if shown.returncode == 0:
                docs[base] = json.loads(shown.stdout)
    return docs


def history_index(docs):
    ids, titles, last_scan = set(), set(), None
    for doc in docs.values():
        last_scan = max(last_scan or doc["scan_date"], doc["scan_date"])
        for item in doc["items"]:
            ids |= set(item.get("ids", []))
            titles.add(item["norm_title"])
    return {"ids": ids, "titles": titles, "last_scan": last_scan}


def is_known(candidate_ids, norm_title, *indexes):
    for idx in indexes:
        if set(candidate_ids) & idx["ids"]:
            return True
        if norm_title in idx["titles"]:
            return True
    for idx in indexes:
        if any(titles_match(norm_title, t) for t in idx["titles"]):
            return True
    return False


# ---------- citation formatting ----------

def format_authors(authors):
    """authors: list of {"given": ..., "family": ...}, in paper order."""
    def inverted(a):
        return f"{a['family']}, {a['given']}" if a.get("given") else a["family"]

    def natural(a):
        return f"{a.get('given', '')} {a['family']}".strip()

    if not authors:
        return ""
    if len(authors) == 1:
        s = inverted(authors[0])
    elif len(authors) > MAX_FULL_AUTHORS:
        s = f"{inverted(authors[0])}, et al"
    elif len(authors) == 2:
        s = f"{inverted(authors[0])}, and {natural(authors[1])}"
    else:
        mid = ", ".join(natural(a) for a in authors[1:-1])
        s = f"{inverted(authors[0])}, {mid}, and {natural(authors[-1])}"
    return s if s.endswith(".") else s + "."


def quoted_title(title, link=None):
    ends = title.rstrip()[-1:] in "?!."
    if link:
        return f'"[{title}]({link})"' if ends else f'"[{title}]({link})."'
    return f'"{title}"' if ends else f'"{title}."'


def format_entry(meta, link_title_to=None, dataset=None):
    parts = [f"- {format_authors(meta['authors'])}", quoted_title(meta["title"], link_title_to)]
    if meta.get("venue"):
        parts.append(meta["venue"])
    line = " ".join(parts) + f" ({meta['date']}). [[link]]({meta['url']})"
    if dataset and dataset.get("description") and dataset.get("url"):
        desc = dataset["description"].strip()
        desc = desc if desc.endswith(".") else desc + "."
        line += f". {desc} [[data]]({dataset['url']})"
    return line


# ---------- HTTP ----------

def http_get(url, params=None, headers=None, retries=3, timeout=60):
    if params:
        url = f"{url}?{urllib.parse.urlencode(params, quote_via=urllib.parse.quote)}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, **(headers or {})})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and attempt < retries - 1:
                time.sleep(5 * (attempt + 1))
                continue
            raise
        except urllib.error.URLError:
            if attempt < retries - 1:
                time.sleep(5 * (attempt + 1))
                continue
            raise


def http_json(url, params=None, **kw):
    return json.loads(http_get(url, params, **kw))
