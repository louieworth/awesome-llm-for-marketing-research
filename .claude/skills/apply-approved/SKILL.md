---
name: apply-approved
description: Apply the papers ticked in a paper-scan review PR to README.md and push the change to that PR for final review. Use when a scan PR gets the `apply` label, or when asked to apply approved papers (optionally with a PR number, e.g. `/apply-approved 12`). Never merges.
---

# Apply approved papers

The maintainer has ticked papers in a `paper-scan` PR's body, possibly edited section numbers, and added the `apply` label. This skill writes the approved entries into README.md on the PR's branch. **Never merge the PR, and never push to `main`.**

## 1. Find the PR

- If a PR number was given (`$ARGUMENTS`), use it.
- Otherwise run `python3 scripts/gh_rest.py labeled --label apply`. It returns open PRs carrying the label, with their head branch. If none, report that and stop. If several, process them one at a time.

## 2. Check out its branch

```bash
git fetch origin "<head>"
git checkout -B "<head>" "origin/<head>"
```

The tree must be clean first. In a local session, stop and tell the user if it is not.

## 3. Apply

```bash
python3 scripts/apply_proposals.py --pr <N>
```

The script prints a summary JSON:

- `added`: cid, section, title, anchor;
- `rejected`: unticked cids, now recorded so they are never proposed again;
- `warnings`;
- `badge_increments`;
- possibly `new_ordering_problems`.

## 4. Inspect the diff

Run `git diff README.md`. It must contain only:

- the new entry blocks: anchor line(s), a blank line, the entry;
- the category badge count changes.

Check each new entry against `CONTRIBUTING.md`:

- citation format;
- position: published before unpublished, then by date;
- a unique anchor.

If `new_ordering_problems` is present, or an entry landed in the wrong place, move the block by hand. Then re-run `python3 scripts/apply_proposals.py --check` and confirm it lists nothing beyond the problems that were already there before this run.

Do not change any other part of README.md.

## 5. Commit and push to the PR branch

```bash
git add README.md scan/proposals/<date>.json
git commit -m "Add <n> papers from paper scan <date>"
git push origin "<head>"
```

If nothing was ticked, there is no README change: commit only the proposals JSON (the rejections) with message `Record paper scan <date> review: none approved`.

## 6. Report on the PR

Write `scan/work/apply_summary.md` in 简体中文:

- 已写入 README 的论文（cid · 小节 · 标题）;
- 拒绝数量;
- 每条 warning，以及需要手动处理的事项，例如缺少数据集链接;
- 最后一句：请在 Files changed 中检查 diff，确认后 merge。

Then:

```bash
python3 scripts/gh_rest.py comment <N> --body-file scan/work/apply_summary.md
python3 scripts/gh_rest.py remove-label <N> apply
```

Reply with the same summary and the PR URL.
