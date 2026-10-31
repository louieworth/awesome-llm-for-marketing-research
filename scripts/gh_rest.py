#!/usr/bin/env python3
"""Minimal GitHub REST helpers over `gh api`.

Cloud sessions route GitHub through a proxy that rejects GraphQL, so
`gh pr` / `gh issue` fail there; everything here uses REST endpoints only.

  python3 scripts/gh_rest.py open-pr --head scan/2026-11-02 --title "..." --body-file scan/work/pr_body.md --label paper-scan
  python3 scripts/gh_rest.py pr-body 12
  python3 scripts/gh_rest.py labeled --label apply
  python3 scripts/gh_rest.py remove-label 12 apply
  python3 scripts/gh_rest.py comment 12 --body-file scan/work/apply_summary.md
"""

import argparse
import json
import re
import subprocess
import sys

from common import ROOT


def repo_slug():
    url = subprocess.run(["git", "-C", str(ROOT), "remote", "get-url", "origin"],
                         capture_output=True, text=True, check=True).stdout.strip()
    m = re.search(r"([^/:]+)/([^/]+?)(?:\.git)?/?$", url)
    return f"{m.group(1)}/{m.group(2)}"


def api(method, path, payload=None):
    cmd = ["gh", "api", "-X", method, "-H", "Accept: application/vnd.github+json", path]
    if payload is not None:
        cmd += ["--input", "-"]
    r = subprocess.run(cmd, input=json.dumps(payload) if payload is not None else None,
                       capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"gh api {method} {path} failed: {r.stderr.strip() or r.stdout.strip()}")
    return json.loads(r.stdout) if r.stdout.strip() else None


def default_branch():
    return api("GET", f"repos/{repo_slug()}")["default_branch"]


def open_pr(head, title, body, labels=(), base=None, draft=False):
    repo = repo_slug()
    pr = api("POST", f"repos/{repo}/pulls", {
        "title": title, "head": head, "base": base or default_branch(), "body": body, "draft": draft})
    if labels:
        api("POST", f"repos/{repo}/issues/{pr['number']}/labels", {"labels": list(labels)})
    return pr


def get_pr(number):
    return api("GET", f"repos/{repo_slug()}/pulls/{number}")


def labeled_prs(label):
    issues = api("GET", f"repos/{repo_slug()}/issues?state=open&labels={label}&per_page=50")
    out = []
    for it in issues:
        if "pull_request" in it:
            pr = get_pr(it["number"])
            out.append({"number": pr["number"], "head": pr["head"]["ref"], "title": pr["title"], "url": pr["html_url"]})
    return out


def remove_label(number, label):
    api("DELETE", f"repos/{repo_slug()}/issues/{number}/labels/{label}")


def comment(number, body):
    return api("POST", f"repos/{repo_slug()}/issues/{number}/comments", {"body": body})


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("open-pr")
    p.add_argument("--head", required=True)
    p.add_argument("--title", required=True)
    p.add_argument("--body-file", required=True)
    p.add_argument("--label", action="append", default=[])
    p.add_argument("--base")
    p.add_argument("--draft", action="store_true")
    p = sub.add_parser("pr-body")
    p.add_argument("number", type=int)
    p = sub.add_parser("labeled")
    p.add_argument("--label", required=True)
    p = sub.add_parser("remove-label")
    p.add_argument("number", type=int)
    p.add_argument("label")
    p = sub.add_parser("comment")
    p.add_argument("number", type=int)
    p.add_argument("--body-file", required=True)
    args = ap.parse_args()

    if args.cmd == "open-pr":
        pr = open_pr(args.head, args.title, open(args.body_file).read(), args.label, args.base, args.draft)
        print(json.dumps({"number": pr["number"], "url": pr["html_url"]}))
    elif args.cmd == "pr-body":
        print(get_pr(args.number)["body"] or "")
    elif args.cmd == "labeled":
        print(json.dumps(labeled_prs(args.label), indent=1))
    elif args.cmd == "remove-label":
        remove_label(args.number, args.label)
    elif args.cmd == "comment":
        print(comment(args.number, open(args.body_file).read())["html_url"])


if __name__ == "__main__":
    main()
