# Awesome Synthetic Data for Marketing

A curated paper collection on how synthetic data supports marketing research, with an emphasis on LLM-based methods. The collection follows three research pathways: simulating consumers, augmenting existing models and algorithms, and training generators of marketing content.

**8 unique papers · 3 categories · Metadata checked: 2026-10-02**

## Scope and organization

The initial selection comes exclusively from sections **3, 4, and 5** of *Synthetic_Data_for_Marketing_Research_Outline.md*. The original section numbers and subsection assignments are preserved below. Papers used in multiple subsections have one main entry and cross-references.

| Category | Generated object or research role | Unique papers |
| --- | --- | ---: |
| [3. Consumer Simulation](#3-consumer-simulation) | Consumer responses or behavior, including population simulations, segment personas, and individual twins | 4 |
| [4. Model and Algorithm Augmentation](#4-model-and-algorithm-augmentation) | Auxiliary response signals or pseudo-observations for an existing estimator or decision algorithm | 2 |
| [5. Generative Targeting](#5-generative-targeting) | Synthetic content demonstrations for learning a consumer-conditioned marketing generator | 2 |

Entries include the outline's supporting and boundary references. **Benchmark** denotes real grounding or validation data; **Adjacent** denotes a related method outside the core synthetic-data mechanism; **Methodological reference** denotes a relevant training mechanism without an established consumer-personalization contribution; **Pending scope verification** denotes an application whose synthetic-demonstration workflow still needs confirmation.

Years refer to first arXiv submission or SSRN posting, or the dated author-hosted draft. An arXiv or SSRN listing does not establish journal publication or peer-review status.

## Contents

- [3. Consumer Simulation](#3-consumer-simulation)
  - [3.1 Construction, Grounding, and Benchmarks](#31-construction-grounding-and-benchmarks)
  - [3.2 Predictive and Behavioral Fidelity](#32-predictive-and-behavioral-fidelity)
  - [3.3 Market Parameter Estimation and Statistical Inference](#33-market-parameter-estimation-and-statistical-inference)
  - [3.4 Decision Support and Simulated Experimentation](#34-decision-support-and-simulated-experimentation)
- [4. Model and Algorithm Augmentation](#4-model-and-algorithm-augmentation)
  - [4.1 Synthetic Response Signals and Pseudo-Observations](#41-synthetic-response-signals-and-pseudo-observations)
  - [4.2 Integration with Estimation and Online Learning](#42-integration-with-estimation-and-online-learning)
  - [4.3 Boundary with Direct Parameter Prediction](#43-boundary-with-direct-parameter-prediction)
- [5. Generative Targeting](#5-generative-targeting)
  - [5.1 Constructing Synthetic Content Demonstrations](#51-constructing-synthetic-content-demonstrations)
  - [5.2 Learning Consumer-Conditioned Content Generation](#52-learning-consumer-conditioned-content-generation)
  - [5.3 Outcome Alignment and Validation of Generative Targeting](#53-outcome-alignment-and-validation-of-generative-targeting)
- [Curation notes](#curation-notes)
- [Contributing](#contributing)

## 3. Consumer Simulation

Synthetic consumers generate responses or behavior that can be assessed against people, used to estimate market quantities, or applied to simulated experiments. Studies that estimate preferences from generated consumer responses remain in this category.

### 3.1 Construction, Grounding, and Benchmarks

- **[Twin-2K-500: A dataset for building digital twins of over 2,000 people based on their answers to over 500 questions](https://arxiv.org/abs/2505.17479)** <br>
  Olivier Toubia, George Z. Gui, Tianyi Peng, Daniel J. Merlau, Ang Li, and Haozhe Chen. **2025 · arXiv preprint · Benchmark.** <br>
  Provides individual survey records and a repeated-measure baseline for constructing and evaluating digital twins. The participant records are real observations; the synthetic objects are the twins' generated responses. **Outline: §3.1.**

### 3.2 Predictive and Behavioral Fidelity

- **[Digital Twins as Funhouse Mirrors: Five Key Distortions](https://arxiv.org/abs/2509.19088)** <br>
  Tianyi Peng et al. **2025 · arXiv preprint.** <br>
  Compares individuals with their corresponding LLM twins across preregistered studies, examining prediction accuracy and systematic distortions in simulated responses. A reference for assessing whether individual differences survive consumer simulation. **Outline: §3.2.**

### 3.3 Market Parameter Estimation and Statistical Inference

- **[Large Language Models for Market Research: A Data-augmentation Approach](https://arxiv.org/abs/2412.19363)** <br>
  Mengxin Wang, Dennis J. Zhang, and Heng Zhang. **2024 · arXiv preprint.** <br>
  Develops a statistical approach to combine LLM-generated consumer responses with real survey data in conjoint analysis, addressing estimation error and bias from substituting synthetic responses for human data. **Outline: §3.3.**

### 3.4 Decision Support and Simulated Experimentation

- **[SimGym: Traffic-Grounded Browser Agents for Offline A/B Testing in E-Commerce](https://arxiv.org/abs/2602.01443)** <br>
  Alberto Castelo et al. **2026 · arXiv preprint.** <br>
  Uses synthetic buyers grounded in traffic data to navigate storefronts and compare interface variants offline. Connects simulated shopping behavior with validation against outcomes from real buyers. **Outline: §3.4.**

## 4. Model and Algorithm Augmentation

Generated information serves as auxiliary input to an existing estimator or decision algorithm. The defining distinction is the role of that information in the learning procedure.

### 4.1 Synthetic Response Signals and Pseudo-Observations

- **[LOLA: LLM-Assisted Online Learning Algorithm for Content Experiments](https://arxiv.org/abs/2406.02611)** <br>
  Zikun Ye, Hema Yoganarasimhan, and Yufeng Zheng. **2024 · arXiv preprint.** <br>
  Incorporates LLM predictions of headline click-through rates into adaptive content experiments through a pseudo-sample representation. Tunes the auxiliary sample size using historical data to control the predictions' influence alongside real feedback. **Outline: §§4.1–4.2.** [Method text, v3](https://arxiv.org/html/2406.02611v3).

### 4.2 Integration with Estimation and Online Learning

See **[LOLA](#41-synthetic-response-signals-and-pseudo-observations)** above for the integration of auxiliary predictions with online feedback. This cross-reference preserves the outline's second use of the paper without counting it twice.

### 4.3 Boundary with Direct Parameter Prediction

- **[Generative Brand Choice](https://leekevin.io/jmp.pdf)** <br>
  Kevin Lee. **2025 · author-hosted working paper · Adjacent.** <br>
  Learns a mapping from brand and consumer descriptions to preferences estimated by a structural demand model, allowing predictions for unseen brands. These predicted utilities do not, by themselves, constitute synthetic consumer observations or a synthetic dataset. **Outline: §4.3.** [Author's paper listing](https://leekevin.io/).

## 5. Generative Targeting

The core pathway uses synthetic content examples paired with consumer or segment information to train a marketing content generator. Synthetic scores and preference comparisons can support example selection and alignment. Inclusion as a core method requires evidence that synthetic demonstrations contribute substantively to learning the generator.

### 5.1 Constructing Synthetic Content Demonstrations

- **[Balancing Engagement and Polarization: Multi-Objective Alignment of News Content Using LLMs](https://arxiv.org/abs/2504.13444)** <br>
  Mengjie Cheng, Elie Ofek, and Hema Yoganarasimhan. **2025 · arXiv preprint · Methodological reference.** <br>
  Uses generated article rewrites as supervised demonstrations and comparison data to align a content model with engagement and polarization objectives. It supplies a content-training example; consumer-level personalization requires separate evidence. **Outline: §§5.1 and 5.3.** [Training workflow, v2](https://arxiv.org/html/2504.13444v2).

### 5.2 Learning Consumer-Conditioned Content Generation

- **[Generative Personalization with Textual and Non-textual Data](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5329729)** <br>
  M. Yin, R. Gao, and Z. Cong, as listed on the coauthor's publication page. **2025 · SSRN listing · Pending scope verification.** <br>
  An application reference for personalization using textual and non-textual information. The former title, *Personalizing Language Models for Generative Targeting*, is confirmed by the [coauthor's publication page](https://ruijiang81.github.io/publications/). Its specific use of synthetic demonstrations in model training remains unverified. **Outline: §5.2.**

### 5.3 Outcome Alignment and Validation of Generative Targeting

See **[Balancing Engagement and Polarization](#51-constructing-synthetic-content-demonstrations)** above for generated demonstrations, synthetic evaluations, and multi-objective alignment. Evidence of content alignment should be distinguished from evidence of personalization gains or real consumer outcomes.

## Curation notes

- **Provenance:** all eight entries are from outline §§3–5. No additional papers were added. The original outline is maintained separately and is not reproduced in this repository.
- **Metadata:** the six arXiv records were checked for title, authors, and initial submission year. The author-hosted *Generative Brand Choice* listing and indexed draft identify Kevin Lee and a May 2025 draft. Descriptions are brief original summaries, not copied abstracts.
- **Targeting candidate:** the coauthor's publication page verifies the current title, former title, and author initials for *Generative Personalization*. The indexed SSRN record lists an initial posting on 2025-06-30 and a revision on 2026-09-06. Direct SSRN access returned HTTP 403 during checking; this is an access restriction, not evidence of a dead link. Full author-name expansion and the synthetic-demonstration training workflow remain to be checked against the full text.
- **Scope:** Twin-2K-500 is a grounding benchmark; *Generative Brand Choice* is adjacent; *Balancing Engagement and Polarization* is a methodological reference; *Generative Personalization* is a candidate pending scope verification. The category totals count these references and do not imply eight verified core synthetic-data methods.
- **Format references:** organization draws on [Awesome LLM-based Human Simulation](https://github.com/Persdre/awesome-llm-human-simulation), [Awesome-LLM-Synthetic-Data](https://github.com/wasiahmad/Awesome-LLM-Synthetic-Data), and [LLM Agents Papers](https://github.com/zjunlp/LLMAgentPapers): a concise scope, linked contents, thematic paper entries, and contribution guidance. Their broader topic lists and paper descriptions are not copied here.

## Contributing

Suggest an in-scope paper or a metadata correction through an issue or pull request. Include a primary paper link, author names, year, the relevant outline subsection, and a brief explanation of the synthetic-data role. See [CONTRIBUTING.md](CONTRIBUTING.md) for the entry format.
