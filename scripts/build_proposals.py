#!/usr/bin/env python3
"""Merge agent outputs into scan/proposals/<date>.json and render the review PR body.

Reads scan/work/candidates.json plus the agents' screen-*.json,
classify-*.json and verify-*.json files.
"""

import argparse
import json
import sys

from common import (
    PROPOSALS_DIR, SECTIONS, WORK_DIR, collection_index, format_entry, make_anchor,
)

CONFIDENCE_ZH = {"high": "高", "medium": "中", "low": "低"}


def load_agent_files(pattern):
    merged = {}
    for p in sorted(WORK_DIR.glob(pattern)):
        for row in json.loads(p.read_text()):
            merged[row["cid"]] = row
    return merged


def fallback_meta(c):
    """Unverified citation fields from the raw candidate record."""
    def split(name):
        parts = name.split()
        return {"given": " ".join(parts[:-1]), "family": parts[-1]} if parts else {"given": "", "family": name}
    return {"title": c["title"], "authors": [split(a) for a in c["authors"]], "venue": c["venue"],
            "date": c["date"][:7], "url": c["url"]}


def build(candidates_doc):
    screen = load_agent_files("screen-*.json")
    classify = load_agent_files("classify-*.json")
    verify = load_agent_files("verify-*.json")
    used = set(collection_index()["anchors"])
    items, missing = [], []

    for c in candidates_doc["candidates"]:
        cid = c["cid"]
        s = screen.get(cid)
        if not s:
            missing.append(cid)
            continue
        item = {
            "cid": cid, "title": c["title"], "ids": c["ids"], "norm_title": c["norm_title"],
            "source": c["source"], "url": c["url"], "date": c["date"],
            "decision": s["decision"], "reason": s.get("reason", ""),
            "llm_use": s.get("llm_use", ""), "evidence": s.get("evidence", "abstract-only"),
        }
        if s["decision"] == "exclude":
            item["status"] = "excluded"
            items.append(item)
            continue

        item["status"] = "proposed"
        cl = classify.get(cid, {})
        item["section"] = cl.get("section")
        item["dataset_section"] = cl.get("dataset_section")
        item["classification"] = cl.get("rationale", "")
        item["confidence"] = cl.get("confidence", "low")

        v = verify.get(cid)
        meta = ({k: v[k] for k in ("title", "authors", "venue", "date", "url")} if v else fallback_meta(c))
        item["verified"] = bool(v)
        item["published"] = bool(v and v.get("published"))
        item["verification"] = v.get("checks", "") if v else "未核验：引用信息来自抓取的原始记录"
        item["issues"] = v.get("issues", []) if v else ["未经 citation-verifier 核验"]
        if v and v.get("evidence"):
            item["evidence"] = v["evidence"]
        item["meta"] = meta
        item["dataset"] = v.get("dataset") if v else None

        anchor = make_anchor(meta["title"])
        base, n = anchor, 2
        while anchor in used:
            anchor, n = f"{base}-{n}", n + 1
        used.add(anchor)
        item["anchor"] = anchor
        if item["dataset_section"] or (item["section"] in ("1.4", "2.3", "3.3")):
            item["dataset_anchor"] = make_anchor(meta["title"], "dataset-")
        items.append(item)

    return items, missing


def render_entry(item):
    in_dataset = item.get("section") in ("1.4", "2.3", "3.3")
    return format_entry(item["meta"], dataset=item.get("dataset") if in_dataset else None)


def section_label(sec):
    return f"{sec} {SECTIONS[sec]}" if sec in SECTIONS else "?.? 未分类（请填写位置）"


def render_item(item):
    head = f"- [ ] **{item['cid']}** · {section_label(item.get('section'))}"
    if item.get("dataset_section"):
        head += f" · +{item['dataset_section']}"
    lines = [head, f"  - 条目：{render_entry(item).removeprefix('- ')}", f"  - 理由：{item['reason']}"]
    if item.get("classification"):
        lines.append(f"  - 分类：{item['classification']}（置信度：{CONFIDENCE_ZH.get(item['confidence'], item['confidence'])}）")
    lines.append(f"  - 核验：{item['verification']} · 证据：{item['evidence']}")
    if item.get("issues"):
        lines.append(f"  - ⚠️ 待确认：{'；'.join(i.rstrip('。；. ') for i in item['issues'])}")
    return "\n".join(lines)


def render_body(doc, over_cap):
    items = doc["items"]
    inc = [i for i in items if i["decision"] == "include"]
    unc = [i for i in items if i["decision"] == "uncertain"]
    exc = [i for i in items if i["decision"] == "exclude"]
    order = lambda i: (i.get("section") or "9", i["cid"])
    st = doc["stats"]
    fetched = " · ".join(f"{k.removeprefix('fetched_')} {v}" for k, v in st.items() if k.startswith("fetched_"))
    out = [
        f"<!-- paper-scan:{doc['scan_date']} -->",
        f"## 📚 论文扫描 {doc['scan_date']}",
        "",
        f"窗口 {doc['window'][0]} → {doc['window'][1]} · 抓取 {fetched} · 关键词命中 {st.get('keyword_match', 0)}"
        f" · 已收录 {st.get('already_in_collection', 0)} · 已审过 {st.get('already_screened', 0)}"
        f" · agent 筛选 {st.get('to_screen', 0)}（超上限未筛 {st.get('over_cap', 0)}）",
        "",
        f"**建议收录 {len(inc)} · 待定 {len(unc)} · 排除 {len(exc)}**",
        "",
        "**审核方法**：勾选要收录的论文；要换位置就把 `1.2` 这类编号改掉（`+1.4` 表示同时列入数据集小节，删掉即不列）；"
        "审完给这个 PR 加 `apply` 标签。apply 会把勾选条目写进 README 并 push 到本 PR，你在 Files changed 看 diff 后 merge。"
        "未勾选的记为拒绝，以后不再推荐。即使一篇都不收，也请 merge（保留审核记录），不要直接关掉。",
        "",
    ]
    if inc:
        out += [f"### ✅ 建议收录（{len(inc)}）", ""] + [render_item(i) + "\n" for i in sorted(inc, key=order)]
    if unc:
        out += [f"### ❓ 待定（{len(unc)}）", ""] + [render_item(i) + "\n" for i in sorted(unc, key=order)]
    if exc:
        out += [f"<details><summary>❌ 排除（{len(exc)}）</summary>", ""]
        out += [f"- {i['cid']} [{i['title']}]({i['url']}) — {i['reason']}" for i in exc]
        out += ["", "</details>", ""]
    if over_cap:
        out += [f"<details><summary>⏭️ 超出筛选上限、未交给 agent（{len(over_cap)}）</summary>", ""]
        out += [f"- [{c['title']}]({c['url']})" for c in over_cap]
        out += ["", "</details>", ""]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--candidates", default=str(WORK_DIR / "candidates.json"))
    ap.add_argument("--body-out", default=str(WORK_DIR / "pr_body.md"))
    ap.add_argument("--list-passed", action="store_true",
                    help="print IDs screened include/uncertain (for classify and verify batches) and exit")
    args = ap.parse_args()

    if args.list_passed:
        screen = load_agent_files("screen-*.json")
        print(" ".join(sorted(c for c, s in screen.items() if s["decision"] != "exclude")))
        return

    cand = json.load(open(args.candidates))
    items, missing = build(cand)
    if missing:
        sys.exit(f"screening output missing for: {', '.join(missing)}")
    doc = {"scan_date": cand["scan_date"], "window": cand["window"], "stats": cand["stats"], "items": items}
    PROPOSALS_DIR.mkdir(parents=True, exist_ok=True)
    path = PROPOSALS_DIR / f"{cand['scan_date']}.json"
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n")
    body = render_body(doc, cand.get("over_cap", []))
    if len(body) > 60000:  # GitHub caps PR bodies at 65,536 characters
        body = render_body(doc, [])[:60000] + "\n\n…（列表过长已截断，完整记录见 proposals JSON）\n"
    open(args.body_out, "w").write(body)
    n = {d: sum(i["decision"] == d for i in items) for d in ("include", "uncertain", "exclude")}
    print(json.dumps({"proposals": str(path), "pr_body": args.body_out, "body_chars": len(body), **n}))


if __name__ == "__main__":
    main()
