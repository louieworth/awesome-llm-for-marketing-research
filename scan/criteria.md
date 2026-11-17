# Scan inclusion criteria

This file sets the standard for papers the automatic scan proposes. It is **narrower** than CONTRIBUTING.md, and both apply; placement and citation format follow CONTRIBUTING.md. Changes here take effect on the next scan.

In this file, LLM includes transformer models, such as customer-journey or consumption-sequence transformers trained on marketing data.

## The marketing gate (every paper, every tier)

Propose a paper only if a **marketing setting** is part of its research question, its data or its evaluation. A marketing setting means at least one of:

- consumers or customers choosing, buying, rating or reacting to products, brands or services;
- preferences, choice, conjoint, willingness to pay, pricing or demand;
- advertising, promotions, marketing content or persuasion aimed at customers;
- market research: consumer surveys, concept or product tests, customer interviews, perceptual maps, segmentation;
- recommendation, personalization, search or customer data in a commercial setting.

These do **not** pass the gate on their own:

- general social-science, political, psychological or economic-game simulation, such as public opinion polls, GSS, ANES, WVS or Pew items, values, moral judgments, norms, well-being, ultimatum or 11–20 games;
- general LLM methods, benchmarks, persona collections or agents with no marketing task;
- naming marketing as one possible application;
- the venue: a UTD 24 journal does not make a paper a marketing paper.

If the abstract does not show a marketing setting, **exclude** the paper. Do not mark it uncertain.

## Length

An arXiv preprint needs at least **20 pages** in its full PDF, references and appendices included (`min_pages` in `scripts/scan_config.json`). `scripts/page_count.py` counts the pages after screening, and arXiv papers below the minimum are excluded automatically. Published journal articles and SSRN working papers are exempt.

## Tracks

### A. `consumer_simulation`: consumer digital twins and consumer simulation → category 1

LLMs simulate consumers or customers in a marketing setting, for example:

- preferences, choice, conjoint, willingness to pay;
- purchase intent, product or concept evaluation, brand perception;
- responses to advertising or prices;
- market research surveys and customer interviews.

Forms include digital twins, synthetic respondents, silicon samples and personas. Simulation methods, validity tests and limitation studies all count, with public or private data. A public human-response dataset counts only when the simulated outcomes are consumer or marketing outcomes, such as the pricing and product questions in Twin-2K-500.

### C. `marketing_method`: marketing content generation or algorithm augmentation → categories 2 and 3

Meets the CONTRIBUTING.md requirements for category 2 (content generation and personalization) or category 3 (model and algorithm augmentation), with a marketing task in the data or the evaluation.

The former track B, LLM simulation of people from public survey data without a marketing setting, is retired.

## Tiers: where the paper comes from and who wrote it

Every tier requires the marketing gate and track A or C.

- **Tier 1, UTD 24 journals** (listed under `journal_sets.utd24` in `scripts/scan_config.json`): propose regardless of author affiliation.
- **Tier 2, other sources** (arXiv, SSRN, conferences, other journals): at least one author must be from a business school.
  - Confirmed business-school author: propose.
  - Confirmed none: go to tier 3.
  - Cannot tell: mark uncertain and list the affiliations found.
- **Tier 3, no business-school author** (often CS or NLP work): propose only if the paper has at least 100 citations or at least 50 a year (set under `influence` in `scan_config.json`), or the screener flags it as exceptionally valuable and says why.

## Decisions

- `include`: clearly passes the gate and fits track A or C.
- `uncertain`: passes the gate, but the abstract leaves the LLM's role or the track unclear. Never use uncertain because the marketing setting is unclear.
- `exclude`: everything else.

Expect a handful of proposals a week at most. A week with none is normal.

## What counts as a business school

**Counts:**

- business schools and schools of management;
- marketing, operations, information systems, strategy, finance and accounting departments inside a business school;
- for example Wharton, Booth, Kellogg, HBS, Stern, Columbia Business School, MIT Sloan, Rotman, Ivey, INSEAD, LBS, HKUST Business School, CKGSB, Peking University Guanghua and Tsinghua SEM.

**Does not count:**

- economics, computer science, statistics and psychology departments;
- corporate research labs, such as Google, Meta, Alibaba and Kuaishou.

## Always exclude (all tiers, including UTD 24)

- Papers that treat an LLM only as the product or market being studied, such as pricing theory for LLM platforms or audits of brand exposure in LLM answers. These neither simulate consumers with an LLM nor use one as part of a marketing method.
- General agent, tool-use, RL or recommender-system engineering papers without commercial data or a marketing outcome.
- Papers that only carry a "generative AI" label without substantive LLM use, mention AI in passing, or study pre-LLM rule-based chatbots or classic machine learning.
