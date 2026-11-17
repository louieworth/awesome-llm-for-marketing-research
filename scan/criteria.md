# Scan inclusion criteria

This file sets the standard for papers the automatic scan proposes. It is **narrower** than CONTRIBUTING.md, and both apply; placement and citation format follow CONTRIBUTING.md. Changes here take effect on the next scan.

In this file, LLM includes transformer models, such as customer-journey or consumption-sequence transformers trained on marketing data.

## Scope: the marketing gate, or the human-simulation bar

Propose a paper only if it passes the **marketing gate** (tracks A and C), or if it is human-simulation research that clears the **bar** under track B.

### The marketing gate (tracks A and C)

A **marketing setting** must be part of the paper's research question, its data or its evaluation. A marketing setting means at least one of:

- consumers or customers choosing, buying, rating or reacting to products, brands or services;
- preferences, choice, conjoint, willingness to pay, pricing or demand;
- advertising, promotions, marketing content or persuasion aimed at customers;
- market research: consumer surveys, concept or product tests, customer interviews, perceptual maps, segmentation;
- recommendation, personalization, search or customer data in a commercial setting.

These do **not** pass the gate on their own:

- general social-science, political, psychological or economic-game simulation, such as public opinion polls, GSS, ANES, WVS or Pew items, values, moral judgments, norms, well-being, ultimatum or 11–20 games (these can still qualify under track B);
- general LLM methods, persona collections or agents with no marketing task and no simulation of people;
- naming marketing as one possible application;
- the venue: a UTD 24 journal does not make a paper a marketing paper.

If the abstract shows neither a marketing setting nor LLM simulation of people, **exclude** the paper. Do not mark it uncertain.

### The human-simulation bar (track B)

Papers in which LLMs simulate people without a marketing setting are treated as digital-twin research and are in scope, but only if they clear a bar. The paper must:

- be published in a peer-reviewed venue: a journal, or the main proceedings or Findings of a major conference (workshops, companion proceedings and proceedings series do not count), **or**
- be highly cited: at least 100 citations, or at least 50 a year (`influence` in `scripts/scan_config.json`).

Unpublished preprints and working papers below the citation bar are excluded, however relevant they look. `scripts/build_proposals.py` applies the bar after citation verification, using the verified venue and the citation count. The bar replaces the business-school author tiers for track B; the length rule still applies.

## Length

An arXiv preprint needs at least **20 pages** in its full PDF, references and appendices included (`min_pages` in `scripts/scan_config.json`). `scripts/page_count.py` counts the pages after screening, and arXiv papers below the minimum are excluded automatically. Published journal articles and SSRN working papers are exempt.

## Journals

Review capacity is limited, so a published journal article must also clear a venue rule, whatever its track or tier. It passes if the journal is:

- a UTD 24 journal (`journal_sets.utd24` in `scripts/scan_config.json`);
- a marketing journal: marketing, consumer research, advertising, retailing or services, such as IJRM, JAMS, JCP, Journal of Retailing, JRCS, Journal of Advertising, JAR, JIM, Psychology & Marketing, JSR, QME, Marketing Letters or EJM;
- a flagship multidisciplinary journal: Nature, Science, PNAS, PNAS Nexus, or a Nature-branded research journal such as Nature Human Behaviour, Nature Computational Science or Nature Machine Intelligence. npj, Communications and Scientific Reports journals do not count.

An article in any other journal needs at least 100 citations or 50 a year (`influence` in `scan_config.json`); otherwise it is excluded, even with a business-school author. General business journals such as the Journal of Business Research are marked uncertain and decided case by case. The maintainer may keep a clearly important exception. `scripts/build_proposals.py` applies this rule after citation verification (`journal_rule` in `scan_config.json`). Conference papers, SSRN working papers and arXiv preprints are not affected.

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

### B. `human_simulation`: LLM simulation of people outside marketing → category 1, with the bar

LLMs simulate people, and the paper compares the simulation with human data or examines whether it is valid. No marketing setting is needed, but the bar above is. For example:

- survey and opinion-poll responses, such as GSS, ANES, WVS, Pew, OpinionQA or census items;
- psychology, social-science and economic-game experiments, and their replication;
- cultural or moral values, norms, well-being and personality, measured against human data;
- general human-behavior simulation benchmarks, and digital twins of individuals.

Not track B: value-alignment papers whose aim is to align or steer the model itself rather than to stand in for people, general machine-learning papers such as model collapse or training on synthetic data, statistics methods that do not simulate people, persona collections built only as training data, and papers that study LLMs as a market or product.

## Tiers: where the paper comes from and who wrote it

Tiers apply to tracks A and C, and every tier requires the marketing gate. Track B uses the bar above instead of the tiers.

- **Tier 1, UTD 24 journals** (listed under `journal_sets.utd24` in `scripts/scan_config.json`): propose regardless of author affiliation.
- **Tier 2, other sources** (arXiv, SSRN, conferences, other journals): at least one author must be from a business school.
  - Confirmed business-school author: propose.
  - Confirmed none: go to tier 3.
  - Cannot tell: mark uncertain and list the affiliations found.
- **Tier 3, no business-school author** (often CS or NLP work): propose only if the paper has at least 100 citations or at least 50 a year (set under `influence` in `scan_config.json`), or the screener flags it as exceptionally valuable and says why.

## Decisions

- `include`: clearly passes the marketing gate and fits track A or C, or clearly fits track B (the bar is applied later, by script).
- `uncertain`: in scope, but the abstract leaves the LLM's role or the track unclear. Never use uncertain because the marketing setting is unclear: a paper without one is track B if it simulates people, and excluded otherwise.
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
