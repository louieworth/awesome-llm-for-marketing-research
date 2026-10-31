# 论文自动扫描

每周自动扫描 arXiv、SSRN 和主要营销期刊，找出可能适合本列表的新论文，开一个审核 PR。你在 PR 里勾选，确认后才会写进 README。

```
每周 routine：/scan-papers
  fetch_candidates.py ── arXiv API + Crossref（SSRN 前缀 10.2139 + 营销期刊 ISSN）
     │                   去重：README、docs、以往扫描记录（main 和所有 origin/scan/* 分支）
     ▼
  paper-screener ×N    并行，判断收录 / 待定 / 排除，附中文理由
  paper-classifier     分到 1.1–3.3，必要时加 +1.4/2.3/3.3
  citation-verifier    对照 Crossref / arXiv / 落地页核验作者、标题、venue、日期
     ▼
  build_proposals.py ── scan/proposals/<date>.json + PR 描述（勾选清单）
     ▼
  PR「论文扫描 <date>」  ⏸ 你审核：勾选、改小节编号、加 apply 标签
     ▼
GitHub 触发 routine：/apply-approved
  apply_proposals.py ── 按 CONTRIBUTING 排序插入 README，更新 badge 计数
     ▼
  push 到同一个 PR      ⏸ 你看 Files changed，然后 merge
```

## 一次性设置

### 1. 云端环境网络白名单

默认的 Trusted 网络访问不允许下面这些域名。设置路径：

1. 打开 claude.ai/code/routines，进入 routine，在名称旁的菜单里点 Edit。
2. 进入 Advanced settings → Cloud environment，点环境名旁的设置图标。
3. 把 Network access 改成 **Custom**，在 Allowed domains 里每行填一个：

```
export.arxiv.org
arxiv.org
api.crossref.org
doi.org
papers.ssrn.com
```

4. 勾选 **Also include default list of common package managers**，然后保存。两个 routine 用同一个环境即可。

如果 citation-verifier 需要打开出版社页面（例如 pubsonline.informs.org、journals.sagepub.com），会返回 403。这不影响结果：核验主要靠 Crossref，打不开的页面它会写进 `issues`。需要的话可以把这些出版社域名也加进白名单。

### 2. 安装 Claude GitHub App

GitHub 触发器需要在本仓库安装 Claude GitHub App。

### 3. 创建两个 routine

| Routine | 触发 | Prompt |
|---|---|---|
| paper-scan | Schedule：每周一 09:07 | `/scan-papers` |
| paper-apply | GitHub：Pull request → labeled，Labels 过滤 `apply` | `/apply-approved` |

两个都选本仓库，并使用第 1 步配置好的环境。也可以在 Claude Code 里用 `/schedule` 创建。

## 每周审核流程

1. 收到 PR「论文扫描 YYYY-MM-DD」。PR 描述里每篇候选包含：拟加入的条目、收录理由、分类依据、核验情况。
2. **勾选**要收录的论文，手机上点 checkbox 就行。
3. 要换小节，就编辑 PR 描述，把 `· 1.2` 改成别的编号。`· +1.4` 表示同时列入数据集小节，删掉就只放在主小节。
4. 给 PR 加 **`apply`** 标签。paper-apply 会把勾选的条目写进 README，push 到这个 PR，并留一条中文总结评论。
5. 在 **Files changed** 里检查 diff，没问题就 **merge**。

注意：

- **一篇都不收，也请 merge**，不要直接关掉 PR，也不要删分支。扫描历史来自 main 和 `origin/scan/*` 上的 `scan/proposals/*.json`，记录丢了会导致同一批论文被重新推荐。
- 没勾选的论文会记为拒绝，以后不再推荐。想重新推荐某篇，就从对应的 proposals JSON 里删掉它的记录。
- 改完 README 后如果还想调整，可以直接在 PR 分支上改，也可以取消勾选后重新加 `apply`。注意：已经写入 README 的条目不会被自动删除。

## 本地使用

```bash
claude "/scan-papers"
```

```bash
claude "/apply-approved 12"
```

单独调试脚本：

```bash
python3 scripts/fetch_candidates.py --since 2026-10-01 --max-screen 20
```

```bash
python3 scripts/lookup.py --title "Using LLMs for Market Research"
```

```bash
python3 scripts/apply_proposals.py --check
```

## 调参

`scripts/scan_config.json` 里可以调：

- `llm_terms` / `domain_terms` / `llm_regex`：关键词预筛。
- `strong_terms`：排序加权。
- `max_screen`：每周最多交给 agent 筛选的篇数，超出的列在 PR 末尾。
- `crossref.journals`：期刊 ISSN 列表。
- `lookback_days`：扫描窗口。下一次运行会自动从上次扫描日期往前 2 天开始，最长 `max_lookback_days`。

收录和分类标准以 `CONTRIBUTING.md` 为准，agent 每次运行都会读它，所以只需改 CONTRIBUTING，不用改 agent。
