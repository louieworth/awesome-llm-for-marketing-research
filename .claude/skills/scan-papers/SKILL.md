---
name: scan-papers
description: Scan arXiv, SSRN and marketing journals for new LLM-for-marketing papers, screen/classify/verify them with subagents, and open a review PR whose body is the approval checklist. Use when asked to scan for new papers, or when the weekly paper-scan routine fires. Never edits README.md.
---

# Scan for new papers

Produces one review PR per run. The maintainer approves papers in the PR; `/apply-approved` writes them into README.md later. This skill **never edits README.md, CONTRIBUTING.md or docs/**.

## 0. Preconditions

- Run `git status --porcelain` and `git rev-parse --abbrev-ref HEAD`. The working tree must be clean and on the default branch (`main`), up to date with `origin`. In a local session, stop and tell the user if it is not. In a cloud run the clone is already clean.
- `DATE=$(date -u +%F)`. This is the scan date.
- Remove stale agent output: `rm -f scan/work/screen-*.json scan/work/classify-*.json scan/work/verify-*.json`.

## 1. Fetch candidates

```bash
python3 scripts/fetch_candidates.py --until "$DATE"
```

The script prints a stats JSON. If `to_screen` is 0, report the stats and stop: no branch, no PR. If the request fails with HTTP 403 `host_not_allowed`, the cloud environment's network allowlist is missing a host (see `scan/README.md`). Report that and stop.

## 2. Screen (parallel)

Read `scan/work/candidates.json` and list the `cid`s in order. Split them into batches of at most 12, numbered 01, 02, …. In **one message**, launch one `paper-screener` agent per batch:

> Screen candidates C001–C012 (C001, C002, …, C012). Output: scan/work/screen-01.json

When all agents are done, check that every cid appears in some `screen-*.json`. Re-run a screener for any missing cids.

## 3. Classify and verify (parallel)

```bash
python3 scripts/build_proposals.py --list-passed
```

This prints the cids screened `include` or `uncertain`. If there are none, skip to step 4. Otherwise, in **one message**, launch:

- `paper-classifier` agents, batches of at most 10 → `scan/work/classify-NN.json`
- `citation-verifier` agents, batches of at most 4 → `scan/work/verify-NN.json`

Both read the candidates file themselves. Pass only the cids and the output path.

## 4. Build the review sheet

```bash
python3 scripts/build_proposals.py
```

This writes `scan/proposals/$DATE.json` (the permanent record, including excluded papers so they are never re-screened) and `scan/work/pr_body.md`.

Spot-check `scan/work/pr_body.md`:

- Each proposed entry looks like the README format: `Author, First, et al. "Title." Venue (YYYY-MM). [[link]](url)`.
- Sections are valid (1.1–3.3).
- Reasons are concrete.

If an entry is clearly malformed because of a verifier mistake, fix that cid's fields in `scan/work/verify-NN.json` and rebuild. Do not hand-edit the generated files.

## 5. Branch, commit, PR

```bash
BRANCH="scan/$DATE"
git ls-remote --exit-code --heads origin "$BRANCH" >/dev/null && BRANCH="scan/$DATE-2"
git checkout -b "$BRANCH"
git add scan/proposals/$DATE.*   # .json, plus .md when the sheet was too long for a PR body
git commit -m "Paper scan $DATE: <N> proposed, <M> excluded"
git push -u origin "$BRANCH"
python3 scripts/gh_rest.py open-pr --head "$BRANCH" \
  --title "论文扫描 $DATE：建议收录 <N> 篇" \
  --body-file scan/work/pr_body.md --label paper-scan
```

- `<N>` is include + uncertain.
- Commit **only** the proposals JSON.
- Open the PR even when N is 0: the PR is the history record that stops the same papers being re-screened.
- Use `gh_rest.py`, not `gh pr`. The cloud GitHub proxy rejects GraphQL.

## 6. Report

Reply with:

- the PR URL;
- the counts (fetched per source, screened, include / uncertain / exclude);
- one line per proposed paper: cid, section, title;
- anything the agents flagged as unresolved.
