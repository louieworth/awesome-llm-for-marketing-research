<div align="center">

<img src="assets/banner.png" alt="Synthetic consumers and data networks" width="800">

![Consumer Simulation](https://img.shields.io/badge/Consumer_Simulation-74-4C70C8?style=for-the-badge)
![Generative Targeting](https://img.shields.io/badge/Generative_Targeting-28-D98757?style=for-the-badge)
![Model and Algorithm Augmentation](https://img.shields.io/badge/Model_%26_Algorithm_Augmentation-14-9865C6?style=for-the-badge)

</div>

# Awesome LLMs for Marketing Research

A curated list of **papers on large language models (LLMs) for marketing**, organized around consumer simulation, generative targeting, and model and algorithm augmentation.

The collection prioritizes marketing and business-school research, with selected computer-science and social-science methods, validation studies, and reviews. It covers substantive uses of language and multimodal language models, including mixed-model methods, datasets for LLM-based simulation, and research on LLM limitations. Selected visual generative-AI studies of advertising effectiveness and marketing outcomes are also included. Evidence on simulated consumers, downstream learning, and marketing outcomes is grouped by research direction; inclusion does not establish that LLM-generated data are valid substitutes for human observations.

Browse by research direction:

- 🧑 **[1. Consumer Simulation](#consumer-simulation)** — consumer responses, behavioral fidelity, and market insights.
- ✨ **[2. Generative Targeting](#generative-targeting)** — personalized content, advertising effects, and marketing outcomes.
- 🔬 **[3. Model and Algorithm Augmentation](#model-and-algorithm-augmentation)** — algorithm performance, synthetic training signals, and improved learning methods.

Suggestions and corrections are welcome; see [Contributing](#contributing).

## Contents

- [Awesome LLMs for Marketing Research](#awesome-llms-for-marketing-research)
  - [Contents](#contents)
  - [Selected Foundational Papers](#selected-foundational-papers)
  - [🧑 1. Consumer Simulation](#-1-consumer-simulation)
    - [1.1 Capabilities and Opportunities](#11-capabilities-and-opportunities)
    - [1.2 Validity and Limitations](#12-validity-and-limitations)
    - [1.3 Methods and Improvements](#13-methods-and-improvements)
  - [✨ 2. Generative Targeting](#-2-generative-targeting)
    - [2.1 Market Effects and Limitations](#21-market-effects-and-limitations)
    - [2.2 Methods and Improvements](#22-methods-and-improvements)
  - [🔬 3. Model and Algorithm Augmentation](#-3-model-and-algorithm-augmentation)
    - [3.1 Performance and Limitations](#31-performance-and-limitations)
    - [3.2 Methods and Improvements](#32-methods-and-improvements)
  - [🤝 Contributing](#-contributing)

## Selected Foundational Papers

A starting set across consumer simulation, generative targeting, and model and algorithm augmentation: four consumer-simulation papers and one paper from each subsection of the other two directions. Brand et al.'s working paper is included as an exception for its foundational framing of LLM-based market research. Entries are ordered from earliest to latest by the dates shown. Title links point to the corresponding entries in the full collection.

- Brand, James, Ayelet Israeli, and Donald Ngwe. "[Using LLMs for Market Research](#paper-using-llms-for-market-research)." SSRN 4395751 (2023-03). [[link]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4395751)

- Santurkar, Shibani, et al. "Whose Opinions Do Language Models Reflect?" ICML 2023, PMLR 202: 29971–30004 (2023-07). [[link]](https://proceedings.mlr.press/v202/santurkar23a.html)

- Matz, Sandra C., et al. "[The potential of generative AI for personalized persuasion at scale](#paper-the-potential-of-generative-ai-for-personalized-persuasion-at-scale)." Scientific Reports 14: 4692 (2024-02). [[link]](https://doi.org/10.1038/s41598-024-53755-0)

- Goli, Ali, and Amandeep Singh. "[Frontiers: Can Large Language Models Capture Human Preferences?](#paper-frontiers-can-large-language-models-capture-human-preferences)" Marketing Science 43(4): 709–722 (2024-04). [[link]](https://doi.org/10.1287/mksc.2023.0306)

- Arora, Neeraj, Ishita Chakraborty, and Yohei Nishimura. "[AI–Human Hybrids for Marketing Research: Leveraging Large Language Models (LLMs) as Collaborators](#paper-ai-human-hybrids-for-marketing-research-leveraging-large-language-models-llms-as-collaborators)." Journal of Marketing 89(2): 43–70 (2024-08). [[link]](https://doi.org/10.1177/00222429241276529)

- Ye, Zikun, Hema Yoganarasimhan, and Yufeng Zheng. "[LOLA: LLM-Assisted Online Learning Algorithm for Content Experiments](#paper-lola-llm-assisted-online-learning-algorithm-for-content-experiments)." Marketing Science 44(5): 995–1016 (2025-03). [[link]](https://pubsonline.informs.org/doi/10.1287/mksc.2024.0990)


---

<a id="consumer-simulation"></a>

## 🧑 1. Consumer Simulation

### 1.1 Capabilities and Opportunities

Demonstrations and research opportunities for LLM-based consumer and human simulation, including preference measurement, experimental prediction, and digital-twin applications. Selected cross-disciplinary studies establish capabilities and use cases.

<a id="paper-llm-agents-grounded-in-self-reports-enable-general-purpose-simulation-of-individuals"></a>

- Park, Joon Sung, et al. "LLM Agents Grounded in Self-Reports Enable General-Purpose Simulation of Individuals." arXiv:2411.10109 (2024-11). [[link]](https://arxiv.org/abs/2411.10109)

<a id="paper-out-of-one-many-using-language-models-to-simulate-human-samples"></a>

- Argyle, Lisa P., et al. "Out of One, Many: Using Language Models to Simulate Human Samples." Political Analysis 31(3): 337–351 (2023-02). [[link]](https://doi.org/10.1017/pan.2023.2)

<a id="paper-synthetic-contact-with-ai-reduces-cross-partisan-animosity"></a>

- Lira, Benjamin, Noah Castelo, Stefano Puntoni, and Olivier Toubia. "Synthetic Contact with AI Reduces Cross-Partisan Animosity." arXiv:2607.02181 (2026-07). [[link]](https://arxiv.org/abs/2607.02181)

<a id="paper-large-language-models-can-predict-the-results-of-social-science-experiments"></a>

- Ashokkumar, Ashwini, et al. "Large language models can predict the results of social science experiments." Nature 656: 115–122 (2026-07). [[link]](https://doi.org/10.1038/s41586-026-10742-x)

<a id="paper-large-language-models-as-simulated-economic-agents-what-can-we-learn-from-homo-silicus"></a>

- Horton, John J., Apostolos Filippas, and Benjamin S. Manning. "Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?" arXiv:2301.07543 (2023-01). [[link]](https://arxiv.org/abs/2301.07543)

<a id="paper-synthetic-consumer-insight-generation-with-large-language-models"></a>

- France, Stephen L., and Pia A. Albinsson. "Synthetic Consumer Insight Generation with Large Language Models." arXiv:2607.05761 (2026-07). [[link]](https://arxiv.org/abs/2607.05761)

<a id="paper-a-foundation-model-to-predict-and-capture-human-cognition"></a>

- Binz, Marcel, et al. "A foundation model to predict and capture human cognition." Nature 644: 1002–1009 (2025-07). [[link]](https://doi.org/10.1038/s41586-025-09215-4)

<a id="paper-large-language-models-outperform-humans-at-estimating-societys-everyday-norms"></a>

- Eriksson, Kimmo, et al. "Large language models outperform humans at estimating society’s everyday norms." Communications AI & Computing 1: 15 (2026-09). [[link]](https://doi.org/10.1038/s44488-026-00018-8)

<a id="paper-using-large-language-models-to-simulate-multiple-humans-and-replicate-human-subject-studies"></a>

- Aher, Gati V., Rosa I. Arriaga, and Adam Tauman Kalai. "Using Large Language Models to Simulate Multiple Humans and Replicate Human Subject Studies." ICML 2023, PMLR 202: 337–371 (2023-07). [[link]](https://proceedings.mlr.press/v202/aher23a.html)

<a id="paper-frontiers-determining-the-validity-of-large-language-models-for-automated-perceptual-analysis"></a>

- Li, Peiyao, et al. "Frontiers: Determining the Validity of Large Language Models for Automated Perceptual Analysis." Marketing Science 43(2): 254–266 (2024-01). [[link]](https://doi.org/10.1287/mksc.2023.0454)

<a id="paper-customer-digital-twins-in-the-field-cross-sell-micro-personalization-at-scale"></a>

- Casero, Emilio, et al. "Customer Digital Twins in the Field: Cross-Sell Micro-Personalization at Scale." Columbia Business School research record (2026-09). [[link]](https://business.columbia.edu/faculty/research/customer-digital-twins-field-cross-sell-micro-personalization-scale)

<a id="paper-the-case-for-synthetic-data"></a>

- Sambandam, Rajan, and Oded Netzer. "The Case for Synthetic Data." Quirk's Marketing Research Review (2025-11). [[link]](https://business.columbia.edu/faculty/research/case-synthetic-data)

<a id="paper-can-ai-language-models-replace-human-participants"></a>

- Dillion, Danica, et al. "Can AI language models replace human participants?" Trends in Cognitive Sciences 27(7): 597–600 (2023-05). [[link]](https://doi.org/10.1016/j.tics.2023.04.008)

### 1.2 Validity and Limitations

Evidence on behavioral fidelity, heterogeneity, representation, statistical and causal validity, and the limits of replacing human observations. Reviews and conceptual critiques are grouped here when validity is their main contribution.

<a id="paper-a-large-scale-replication-of-scenario-based-experiments-in-psychology-and-management-using-large-language-models"></a>

- Cui, Ziyan, Ning Li, and Huaikang Zhou. "A large-scale replication of scenario-based experiments in psychology and management using large language models." Nature Computational Science 5(8): 627–634 (2025-07). [[link]](https://doi.org/10.1038/s43588-025-00840-7)

<a id="paper-measuring-the-digital-twin-separating-individuation-from-population-regularity-in-llm-survey-twins"></a>

- Miller, Moses. "Measuring the Digital Twin: Separating Individuation from Population Regularity in LLM Survey Twins." Working paper, Reichman University (2026; month unverified), cited in Netzer and Sambandam, arXiv:2609.13995, p. 31; original manuscript unavailable. [[link]](https://arxiv.org/pdf/2609.13995#page=31)

<a id="paper-llm-generated-persona-is-a-promise-with-a-catch"></a>

- Li, Ang, Haozhe Chen, Hongseok Namkoong, and Tianyi Peng. "LLM Generated Persona is a Promise with a Catch." NeurIPS 2025, Position Paper Track, Advances in Neural Information Processing Systems 38 (2025-12). [[link]](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5fc150b75e8b509735564de16bc3527b-Abstract-Position_Paper_Track.html)

<a id="paper-on-the-reliability-of-individual-economic-rationality-measurements"></a>

- Nitsch, Felix J., Luca M. Lüpken, Nils Lüschow, and Tobias Kalenscher. "On the reliability of individual economic rationality measurements." PNAS 119(31): e2202070119 (2022-07), consumer-choice measurement background. [[link]](https://doi.org/10.1073/pnas.2202070119)

<a id="paper-whats-in-a-name-auditing-large-language-models-for-race-and-gender-bias"></a>

- Salinas, Alejandro, Amit Haim, and Julian Nyarko. "What's in a Name? Auditing Large Language Models for Race and Gender Bias." arXiv:2402.14875 (2024-02). [[link]](https://arxiv.org/abs/2402.14875)

<a id="paper-frontiers-can-large-language-models-capture-human-preferences"></a>

- Goli, Ali, and Amandeep Singh. "Frontiers: Can Large Language Models Capture Human Preferences?" Marketing Science 43(4): 709–722 (2024-04). [[link]](https://doi.org/10.1287/mksc.2023.0306)

<a id="paper-digital-twins-are-funhouse-mirrors-five-systematic-distortions"></a>

- Peng, Tianyi, et al. "Digital twins are funhouse mirrors: Five systematic distortions." Science Advances 12(36): eaeh8260 (2026-09). [[link]](https://doi.org/10.1126/sciadv.aeh8260)

<a id="paper-evaluating-the-statistical-realism-of-llm-generated-social-science-data"></a>

- Xie, Yueqi, et al. "Evaluating the statistical realism of LLM-generated social science data." PNAS 123(19): e2538145123 (2026-05). [[link]](https://doi.org/10.1073/pnas.2538145123)

<a id="paper-take-caution-in-using-llms-as-human-surrogates"></a>

- Gao, Yuan, et al. "Take caution in using LLMs as human surrogates." PNAS 122(24): e2501660122 (2025-06). [[link]](https://doi.org/10.1073/pnas.2501660122)

<a id="paper-synthetic-replacements-for-human-survey-data-the-perils-of-large-language-models"></a>

- Bisbee, James, et al. "Synthetic Replacements for Human Survey Data? The Perils of Large Language Models." Political Analysis 32(4): 401–416 (2024-05). [[link]](https://doi.org/10.1017/pan.2024.5)

<a id="paper-large-language-models-that-replace-human-participants-can-harmfully-misportray-and-flatten-identity-groups"></a>

- Wang, Angelina, Jamie Morgenstern, and John P. Dickerson. "Large language models that replace human participants can harmfully misportray and flatten identity groups." Nature Machine Intelligence 7: 400–411 (2025-02). [[link]](https://doi.org/10.1038/s42256-025-00986-z)

<a id="paper-whose-opinions-do-language-models-reflect"></a>

- Santurkar, Shibani, et al. "Whose Opinions Do Language Models Reflect?" ICML 2023, PMLR 202: 29971–30004 (2023-07). [[link]](https://proceedings.mlr.press/v202/santurkar23a.html)

<a id="paper-questioning-the-survey-responses-of-large-language-models"></a>

- Dominguez-Olmedo, Ricardo, Moritz Hardt, and Celestine Mendler-Dünner. "Questioning the Survey Responses of Large Language Models." NeurIPS 2024 (2024-12). [[link]](https://proceedings.neurips.cc/paper_files/paper/2024/hash/515c62809e0a29729d7eec26e2916fc0-Abstract-Conference.html)

<a id="paper-towards-measuring-the-representation-of-subjective-global-opinions-in-language-models"></a>

- Durmus, Esin, et al. "Towards Measuring the Representation of Subjective Global Opinions in Language Models." COLM 2024 (2024-10). [[link]](https://openreview.net/forum?id=zl16jLb91v)

<a id="paper-cultural-bias-and-cultural-alignment-of-large-language-models"></a>

- Tao, Yan, et al. "Cultural bias and cultural alignment of large language models." PNAS Nexus 3(9): pgae346 (2024-09). [[link]](https://doi.org/10.1093/pnasnexus/pgae346)

<a id="paper-large-language-models-display-human-like-social-desirability-biases-in-big-five-personality-surveys"></a>

- Salecha, Aadesh, et al. "Large language models display human-like social desirability biases in Big Five personality surveys." PNAS Nexus 3(12): pgae533 (2024-12). [[link]](https://doi.org/10.1093/pnasnexus/pgae533)

<a id="paper-moral-stereotyping-in-large-language-models"></a>

- Zewail, Aliah, et al. "Moral stereotyping in large language models." PNAS 123(10): e2519941123 (2026-03). [[link]](https://doi.org/10.1073/pnas.2519941123)

<a id="paper-simulating-human-well-being-with-large-language-models-systematic-validation-and-misestimation-across-64-000-individuals-from-64-countries"></a>

- Pataranutaporn, Pat, et al. "Simulating human well-being with large language models: Systematic validation and misestimation across 64,000 individuals from 64 countries." PNAS 122(48): e2519394122 (2025-11). [[link]](https://doi.org/10.1073/pnas.2519394122)

<a id="paper-machine-bias-how-do-generative-language-models-answer-opinion-polls"></a>

- Boelaert, Julien, et al. "Machine Bias. How Do Generative Language Models Answer Opinion Polls?" Sociological Methods & Research 54(3): 1156–1196 (2025-04). [[link]](https://doi.org/10.1177/00491241251330582)

<a id="paper-prompt-architecture-induces-methodological-artifacts-in-large-language-models"></a>

- Brucks, Melanie, and Olivier Toubia. "Prompt architecture induces methodological artifacts in large language models." PLOS ONE 20(4): e0319159 (2025-04). [[link]](https://doi.org/10.1371/journal.pone.0319159)

<a id="paper-large-language-models-assume-people-are-more-rational-than-we-really-are"></a>

- Liu, Ryan, et al. "Large Language Models Assume People are More Rational than We Really are." ICLR 2025 (2025-04). [[link]](https://proceedings.iclr.cc/paper_files/paper/2025/hash/7cdb411d07bdf6cd43ddf1254fae98cd-Abstract-Conference.html)

<a id="paper-simbench-benchmarking-the-ability-of-large-language-models-to-simulate-human-behaviors"></a>

- Hu, Tiancheng, et al. "SimBench: Benchmarking the Ability of Large Language Models to Simulate Human Behaviors." ICLR 2026 (2026-04). [[link]](https://proceedings.iclr.cc/paper_files/paper/2026/hash/2fc4d6a6400addda7493b9db258c34e0-Abstract-Conference.html)

<a id="paper-distorted-perspectives-of-llm-simulated-preferences-can-ai-mislead-design"></a>

- Kuric, Eduard, Peter Demcak, and Matus Krajcovic. "Distorted Perspectives of LLM-Simulated Preferences: Can AI Mislead Design?" arXiv:2605.18311 (2026-05). [[link]](https://arxiv.org/abs/2605.18311)

<a id="paper-variance-reduction-in-output-from-generative-ai"></a>

- Xie, Yu, and Yueqi Xie. "Variance reduction in output from generative AI." arXiv:2503.01033 (2025-03). [[link]](https://arxiv.org/abs/2503.01033)

<a id="paper-fragile-preferences-a-deep-dive-into-order-effects-in-large-language-models"></a>

- Yin, Haonan, Shai Vardi, and Vidyanand Choudhary. "Fragile preferences: A deep dive into order effects in large language models." PNAS Nexus 5(8): pgag246 (2026-08). [[link]](https://doi.org/10.1093/pnasnexus/pgag246)

<a id="paper-how-price-sensitive-is-ai-benchmarking-llm-generated-willingness-to-pay-in-pricing-analytics"></a>

- Oetzel, Sebastian, and Tobias Maiberger. "How price sensitive is AI? Benchmarking LLM-generated willingness to pay in pricing analytics." Journal of Marketing Analytics (2026-09). [[link]](https://doi.org/10.1057/s41270-026-00542-7)

<a id="paper-statistical-realism-is-not-evidence-that-llms-can-estimate-treatment-effects-in-social-science-experiments"></a>

- Li, Zonghan, and Feng Ji. "Statistical realism is not evidence that LLMs can estimate treatment effects in social science experiments." arXiv:2604.02458 (2026-04). [[link]](https://arxiv.org/abs/2604.02458)

<a id="paper-when-synthetic-users-fail-a-cross-domain-benchmark-of-llm-simulated-human-survey-responses"></a>

- Chen, Zihan, Di Zhu, and Lei Nico Zheng. "When Synthetic Users Fail: A Cross-Domain Benchmark of LLM-Simulated Human Survey Responses." arXiv:2607.26348 (2026-07). [[link]](https://arxiv.org/abs/2607.26348)

<a id="paper-what-would-gpt-click-practical-effects-of-human-ai-behavioral-misalignment-and-the-cost-of-synthetic-participants-in-user-experience"></a>

- Kuric, Eduard, Peter Demcak, and Matus Krajcovic. "What Would GPT Click: Practical Effects of Human-AI Behavioral Misalignment and the Cost of Synthetic Participants in User Experience." arXiv:2605.18302 (2026-05). [[link]](https://arxiv.org/abs/2605.18302)

<a id="paper-synthetic-data-and-digital-twins-the-hype-the-facts-the-promise"></a>

- Toubia, Olivier. "Synthetic Data and Digital Twins: The Hype, The Facts, the Promise." SSRN 7065919 (2026-07). [[link]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7065919)

<a id="paper-perils-and-opportunities-in-using-large-language-models-in-psychological-research"></a>

- Abdurahman, Suhaib, et al. "Perils and opportunities in using large language models in psychological research." PNAS Nexus 3(7): pgae245 (2024-07). [[link]](https://doi.org/10.1093/pnasnexus/pgae245)

<a id="paper-the-illusion-of-artificial-inclusion"></a>

- Agnew, William, et al. "The Illusion of Artificial Inclusion." CHI 2024 (2024-05). [[link]](https://doi.org/10.1145/3613904.3642703)

<a id="paper-six-fallacies-in-substituting-large-language-models-for-human-participants"></a>

- Lin, Zhicheng. "Six Fallacies in Substituting Large Language Models for Human Participants." Advances in Methods and Practices in Psychological Science (2025-08). [[link]](https://doi.org/10.1177/25152459251357566)

<a id="paper-large-language-models-as-human-proxies"></a>

- Karetnikov, Nikita, Iyad Rahwan, and Davor Svetinovic. "Large language models as human proxies." Nature Computational Science (2026-09). [[link]](https://doi.org/10.1038/s43588-026-01060-3)

<a id="paper-synthetic-participants-generated-by-large-language-models-a-systematic-literature-review"></a>

- Kuric, Eduard, Peter Demcak, and Matus Krajcovic. "Synthetic Participants Generated by Large Language Models: A Systematic Literature Review." Research Square (2026-03). [[link]](https://doi.org/10.21203/rs.3.rs-9057643/v1)

<a id="paper-too-human-to-model-the-uncanny-valley-of-large-language-models-in-simulating-human-systems"></a>

- Zeng, Yongchao, Calum Brown, and Mark Rounsevell. "Too human to model: the uncanny valley of large language models in simulating human systems." npj Complexity 3: 13 (2026-03). [[link]](https://doi.org/10.1038/s44260-026-00075-1)

### 1.3 Methods and Improvements

Methods that construct, ground, calibrate, fine-tune, validate, or improve simulated responses and research workflows. This includes human-data integration, supervised fine-tuning, inference correction, and selected transferable computer-science methods.

<a id="paper-database-report-twin-2k-500-a-data-set-for-building-digital-twins-of-over-2-000-people-based-on-their-answers-to-over-500-questions"></a>

- Toubia, Olivier, et al. "Database Report: Twin-2K-500: A Data Set for Building Digital Twins of over 2,000 People Based on Their Answers to over 500 Questions." Marketing Science 44(6): 1446–1455 (2025-08). [[link]](https://doi.org/10.1287/mksc.2025.0262)

<a id="paper-twinface-generating-synthetic-faces-for-multimodal-consumer-digital-twins"></a>

- Sherwin, R., M. Miller, Y. Zwebner, and J. Goldenberg. "Twinface: Generating synthetic faces for multimodal consumer digital twins." Working paper (2026; month unverified), cited in Toubia, SSRN 7065919; original manuscript unavailable and correspondence to "The Face of Digital Twins" unverified. [[link]](https://business.columbia.edu/faculty/research/synthetic-data-and-digital-twins-hype-facts-promise)

<a id="paper-ai-moderated-interviews-for-market-research-and-digital-twins-calibration"></a>

- Deng, Yuting, et al. "AI-Moderated Interviews for Market Research and Digital Twins Calibration." arXiv:2609.29143 (2026-09). [[link]](https://arxiv.org/abs/2609.29143)

<a id="paper-synthetic-personalities-how-well-can-llms-mimic-individual-respondents-using-socio-economic-microdata"></a>

- Kinzinger, Leonard, and Jochen Hartmann. "Synthetic Personalities: How Well Can LLMs Mimic Individual Respondents Using Socio-Economic Microdata?" arXiv:2606.04592 (2026-06). [[link]](https://arxiv.org/abs/2606.04592)

<a id="paper-syn-digits-a-synthetic-control-framework-for-calibrated-digital-twin-simulation"></a>

- Fan, Grace Jiarui, et al. "SYN-DIGITS: A Synthetic Control Framework for Calibrated Digital Twin Simulation." arXiv:2604.07513 (2026-04). [[link]](https://arxiv.org/abs/2604.07513)

<a id="paper-finetuning-llms-for-human-behavior-prediction-in-social-science-experiments"></a>

- Kolluri, Akaash, et al. "Finetuning LLMs for Human Behavior Prediction in Social Science Experiments." EMNLP 2025 (2025-11). [[link]](https://aclanthology.org/2025.emnlp-main.1530/)

<a id="paper-reducing-disparity-between-llms-and-humans-optimal-llm-sample-calibration"></a>

- Leng, Yan, Yunxin Sang, and Ashish Agarwal. "Reducing Disparity Between LLMs and Humans: Optimal LLM Sample Calibration." Marketing Science, forthcoming. [[link]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4802019)

<a id="paper-how-ai-helps-scale-qualitative-customer-research"></a>

- Korst, Jeremy, Stefano Puntoni, and Olivier Toubia. "How AI Helps Scale Qualitative Customer Research." Harvard Business Review (2026-04). [[link]](https://hbr.org/2026/04/how-ai-helps-scale-qualitative-customer-research)

<a id="paper-llms-reproduce-human-purchase-intent-via-semantic-similarity-elicitation-of-likert-ratings"></a>

- Maier, Benjamin F., et al. "LLMs Reproduce Human Purchase Intent via Semantic Similarity Elicitation of Likert Ratings." arXiv:2510.08338 (2025-10). [[link]](https://arxiv.org/abs/2510.08338)

<a id="paper-simgym-a-framework-for-a-b-test-simulation-in-e-commerce-with-traffic-grounded-vlm-agents"></a>

- Li, Han, et al. "SimGym: A Framework for A/B Test Simulation in E-Commerce with Traffic-Grounded VLM Agents." arXiv:2605.19219 (2026-05). [[link]](https://arxiv.org/abs/2605.19219)

<a id="paper-ai-human-hybrids-for-marketing-research-leveraging-large-language-models-llms-as-collaborators"></a>

- Arora, Neeraj, Ishita Chakraborty, and Yohei Nishimura. "AI–Human Hybrids for Marketing Research: Leveraging Large Language Models (LLMs) as Collaborators." Journal of Marketing 89(2): 43–70 (2024-08). [[link]](https://doi.org/10.1177/00222429241276529)

<a id="paper-the-challenge-of-using-llms-to-simulate-human-behavior-a-causal-inference-perspective"></a>

- Gui, George, and Olivier Toubia. "The Challenge of Using LLMs to Simulate Human Behavior: A Causal Inference Perspective." SSRN 4650172 (2023-12). [[link]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4650172)

<a id="paper-this-human-study-did-not-involve-human-subjects-validating-llm-simulations-as-behavioral-evidence"></a>

- Hullman, Jessica, et al. "This human study did not involve human subjects: Validating LLM simulations as behavioral evidence." arXiv:2602.15785 (2026-02). [[link]](https://arxiv.org/abs/2602.15785)

<a id="paper-using-llms-for-market-research"></a>

- Brand, James, Ayelet Israeli, and Donald Ngwe. "Using LLMs for Market Research." SSRN 4395751 (2023-03). [[link]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4395751)

<a id="paper-synthetic-data-in-marketing-research-how-to-evaluate-and-when-to-trust"></a>

- Netzer, Oded, and Rajan Sambandam. "Synthetic Data in Marketing Research: How to Evaluate and When to Trust." arXiv:2609.13995 (2026-09). [[link]](https://arxiv.org/abs/2609.13995)

<a id="paper-large-language-models-for-market-research-a-data-augmentation-approach"></a>

- Wang, Mengxin, Dennis J. Zhang, and Heng Zhang. "Large Language Models for Market Research: A Data-Augmentation Approach." Marketing Science 45(4): 728–751 (2026-03). [[link]](https://doi.org/10.1287/mksc.2025.0009)

<a id="paper-generative-augmented-inference"></a>

- Lu, Cheng, et al. "Generative Augmented Inference." ICML 2026, PMLR 306: 81730–81751 (2026-07). [[link]](https://proceedings.mlr.press/v306/lu26am.html)

<a id="paper-rectification-difficulty-and-optimal-sample-allocation-in-llm-augmented-surveys"></a>

- Ye, Zikun, and Hema Yoganarasimhan. "Rectification Difficulty and Optimal Sample Allocation in LLM-Augmented Surveys." arXiv:2604.17267 (2026-04). [[link]](https://arxiv.org/abs/2604.17267)

<a id="paper-allocating-human-oversight-in-ai-enabled-analytics"></a>

- Ye, Zikun, Jiameng Lyu, and Rui Tao. "Allocating Human Oversight in AI-Enabled Analytics." arXiv:2604.12497 (2026-04). [[link]](https://arxiv.org/abs/2604.12497)

<a id="paper-distributionally-robust-llm-augmentation-of-discrete-choice-models"></a>

- Liu, Tianming, et al. "Distributionally Robust LLM Augmentation of Discrete Choice Models." SSRN 7500939 (2026-09). [[link]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7500939)

<a id="paper-valid-survey-simulations-with-limited-human-data-the-roles-of-prompting-fine-tuning-and-rectification"></a>

- Krsteski, Stefan, et al. "Valid Survey Simulations with Limited Human Data: The Roles of Prompting, Fine-Tuning, and Rectification." ACL 2026, Long Papers: 10887–10906 (2026-07). [[link]](https://aclanthology.org/2026.acl-long.498/)

<a id="paper-llm-powered-virtual-population-for-demand-simulation-and-pricing"></a>

- Huang, Chengpiao, and Kaizheng Wang. "LLM-Powered Virtual Population for Demand Simulation and Pricing." arXiv:2606.16183 (2026-06). [[link]](https://arxiv.org/abs/2606.16183)

<a id="paper-new-tools-new-rules-a-practical-guide-to-effective-and-responsible-generative-ai-use-for-surveys-and-experiments-in-research"></a>

- Blanchard, Simon J., Nofar Duani, Aaron M. Garvey, Oded Netzer, and Travis Tae Oh. "New Tools, New Rules: A Practical Guide to Effective and Responsible Generative AI Use for Surveys and Experiments in Research." Journal of Marketing 89(6): 119–139 (2025-06). [[link]](https://doi.org/10.1177/00222429251349882)

<a id="paper-large-language-models-as-psychological-simulators-a-methodological-guide"></a>

- Lin, Zhicheng. "Large Language Models as Psychological Simulators: A Methodological Guide." Advances in Methods and Practices in Psychological Science 9(1) (2026-02). [[link]](https://doi.org/10.1177/25152459251410153)

<a id="paper-llm-saa-llm-persona-generated-distributions-for-decision-making"></a>

- Baek, Jackie, et al. "LLM-SAA: LLM-persona Generated Distributions for Decision-making." arXiv:2602.06357 (2026-02). [[link]](https://arxiv.org/abs/2602.06357)

---

<a id="generative-targeting"></a>

## ✨ 2. Generative Targeting

### 2.1 Market Effects and Limitations

Empirical and theoretical evidence on advertising, content, persuasion, and market outcomes, including visual generative AI. Selected cross-disciplinary persuasion studies inform effectiveness and boundary conditions without establishing consumer-market validity.

<a id="paper-frontiers-generative-ai-and-personalized-video-advertisements"></a>

- Kapoor, Anuj, and Madhav Kumar. "Frontiers: Generative AI and Personalized Video Advertisements." Marketing Science 44(4): 733–747 (2025-05). [[link]](https://doi.org/10.1287/mksc.2023.0494)

<a id="paper-ai-in-disguise-quasi-experimental-analysis-of-a-large-scale-deployment-of-ai-generated-ads"></a>

- Exner, Yannick, et al. "AI in Disguise—Quasi-Experimental Analysis of a Large-Scale Deployment of AI-Generated Ads." SSRN 5096969 (2025-03). [[link]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5096969)

<a id="paper-the-impact-of-visual-generative-ai-on-advertising-effectiveness"></a>

- Lee, Hyesoo, et al. "The Impact of Visual Generative AI on Advertising Effectiveness." SSRN 5638311 (2025-11). [[link]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5638311)

<a id="paper-large-language-models-and-creative-content-design-a-case-study-of-email-marketing-at-wine-access"></a>

- Dubé, Jean-Pierre, and Ariel Xu. "Large Language Models and Creative Content Design: a case study of email marketing at Wine Access." Quantitative Marketing and Economics 24: Article 1 (2026-01). [[link]](https://doi.org/10.1007/s11129-025-09303-9)

<a id="paper-when-machines-persuade-better-than-humans-generative-ai-cognitive-constraints-and-promotional-effectiveness"></a>

- Gu, Wenying, et al. "When Machines Persuade Better Than Humans: Generative AI, Cognitive Constraints, and Promotional Effectiveness." SSRN 6294798 (2026-02). [[link]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6294798)

<a id="paper-generative-ai-and-sales-productivity-field-experiments-in-online-retail"></a>

- Fang, Lu, et al. "Generative AI and Sales Productivity: Field Experiments in Online Retail." arXiv:2510.12049 (2025-10). [[link]](https://arxiv.org/abs/2510.12049)

<a id="paper-the-potential-of-generative-ai-for-personalized-persuasion-at-scale"></a>

- Matz, Sandra C., et al. "The potential of generative AI for personalized persuasion at scale." Scientific Reports 14: 4692 (2024-02). [[link]](https://doi.org/10.1038/s41598-024-53755-0)

<a id="paper-we-need-to-understand-when-not-if-generative-ai-can-enhance-personalized-persuasion"></a>

- Teeny, Jacob D., and Sandra C. Matz. "We need to understand “when” not “if” generative AI can enhance personalized persuasion." PNAS 121(43): e2418005121 (2024-10). [[link]](https://doi.org/10.1073/pnas.2418005121)

<a id="paper-evaluating-the-persuasive-influence-of-political-microtargeting-with-large-language-models"></a>

- Hackenburg, Kobi, and Helen Margetts. "Evaluating the persuasive influence of political microtargeting with large language models." PNAS 121(24): e2403116121 (2024-06). [[link]](https://doi.org/10.1073/pnas.2403116121)

<a id="paper-the-persuasive-effects-of-political-microtargeting-in-the-age-of-generative-artificial-intelligence"></a>

- Simchon, Almog, Matthew Edwards, and Stephan Lewandowsky. "The persuasive effects of political microtargeting in the age of generative artificial intelligence." PNAS Nexus 3(2): pgae035 (2024-01). [[link]](https://doi.org/10.1093/pnasnexus/pgae035)

<a id="paper-on-the-conversational-persuasiveness-of-gpt-4"></a>

- Salvi, Francesco, et al. "On the conversational persuasiveness of GPT-4." Nature Human Behaviour 9: 1645–1653 (2025-05). [[link]](https://doi.org/10.1038/s41562-025-02194-6)

<a id="paper-llm-generated-ads-from-personalization-parity-to-persuasion-superiority"></a>

- Meguellati, Elyas, et al. "LLM-Generated Ads: From Personalization Parity to Persuasion Superiority." arXiv:2512.03373 (2025-12). [[link]](https://arxiv.org/abs/2512.03373)

<a id="paper-ads-that-talk-back-implications-and-perceptions-of-injecting-personalized-advertising-into-llm-chatbots"></a>

- Tang, Brian Jay, et al. "Ads that Talk Back: Implications and Perceptions of Injecting Personalized Advertising into LLM Chatbots." Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies 9(4): Article 213 (2025-12). [[link]](https://doi.org/10.1145/3770640)

<a id="paper-will-it-click-advertising-strategy-with-generative-ai"></a>

- Fainmesser, Itay P., Dominique Olie Lauga, and Elie Ofek. "Will it Click? Advertising Strategy with Generative AI." SSRN 6517138 (2026-04). [[link]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6517138)

### 2.2 Methods and Improvements

Methods for personalized content generation, preference modeling, feedback alignment, experimental optimization, and information design. This includes human-AI creative workflows and text or multimodal advertising generation.

<a id="paper-balancing-engagement-and-polarization-multi-objective-alignment-of-news-content-using-llms"></a>

- Cheng, Mengjie, Elie Ofek, and Hema Yoganarasimhan. "Balancing Engagement and Polarization: Multi-Objective Alignment of News Content Using LLMs." arXiv:2504.13444 (2025-04). [[link]](https://arxiv.org/abs/2504.13444)

<a id="paper-gravity-a-framework-for-personalized-text-generation-via-profile-grounded-synthetic-preferences"></a>

- Dey, Priyanka, et al. "GRAVITY: A Framework for Personalized Text Generation via Profile-Grounded Synthetic Preferences." EACL 2026, Long Papers: 7416–7436 (2026-03). [[link]](https://aclanthology.org/2026.eacl-long.348/)

<a id="paper-fspo-few-shot-optimization-of-synthetic-preferences-personalizes-to-real-users"></a>

- Singh, Anikait, et al. "FSPO: Few-Shot Optimization of Synthetic Preferences Personalizes to Real Users." ICLR 2026 (2026-04). [[link]](https://proceedings.iclr.cc/paper_files/paper/2026/file/b2118ec72f6396c7e7bb2407e2d05eb4-Paper-Conference.pdf)

<a id="paper-slm4offer-personalized-marketing-offer-generation-using-contrastive-learning-based-fine-tuning"></a>

- Challapalli, Vedasamhitha, et al. "SLM4Offer: Personalized Marketing Offer Generation Using Contrastive Learning Based Fine-Tuning." arXiv:2508.15471 (2025-08). [[link]](https://arxiv.org/abs/2508.15471)

<a id="paper-long-term-ad-memorability-understanding-generating-memorable-ads"></a>

- Si, Harini, et al. "Long-Term Ad Memorability: Understanding & Generating Memorable Ads." WACV 2025 (2025-02). [[link]](https://openaccess.thecvf.com/content/WACV2025/html/Si_Long-Term_Ad_Memorability_Understanding__Generating_Memorable_Ads_WACV_2025_paper.html)

<a id="paper-generative-personalization-with-textual-and-non-textual-data"></a>

- Yin, Mingzhang, Ruijiang Gao, and Ziwei Cong. "Generative Personalization with Textual and Non-textual Data." SSRN 5329729 (2025-06). [[link]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5329729)

<a id="paper-causal-alignment-augmenting-language-models-with-a-b-tests"></a>

- Angelopoulos, Panagiotis, Kevin Lee, and Sanjog Misra. "Causal Alignment: Augmenting Language Models with A/B Tests." SSRN 4781850 (2024-04). [[link]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4781850)

<a id="paper-offline-to-online-creative-optimization-with-generative-models-and-adaptive-testing"></a>

- Lee, Kevin, et al. "Offline-to-Online Creative Optimization with Generative Models and Adaptive Testing." arXiv:2607.23696 (2026-07). [[link]](https://arxiv.org/abs/2607.23696)

<a id="paper-evaluating-novel-unstructured-treatments-with-generative-ai-a-causal-prediction-framework"></a>

- Ellickson, Paul B., et al. "Evaluating Novel Unstructured Treatments with Generative AI: A Causal Prediction Framework." Journal of Marketing Research (2026-08). [[link]](https://doi.org/10.1177/00222437261476639)

<a id="paper-design-your-ad-personalized-advertising-image-and-text-generation-with-unified-autoregressive-models"></a>

- Xu, Yexing, et al. "Design Your Ad: Personalized Advertising Image and Text Generation with Unified Autoregressive Models." CVPR 2026 (2026-06). [[link]](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Design_Your_Ad_Personalized_Advertising_Image_and_Text_Generation_with_CVPR_2026_paper.pdf)

<a id="paper-applying-large-language-models-to-sponsored-search-advertising"></a>

- Reisenbichler, Martin, Thomas Reutterer, and David A. Schweidel. "Applying Large Language Models to Sponsored Search Advertising." Marketing Science 45(1): 123–141 (2025-11). [[link]](https://doi.org/10.1287/mksc.2023.0611)

<a id="paper-frontiers-supporting-content-marketing-with-natural-language-generation"></a>

- Reisenbichler, Martin, et al. "Frontiers: Supporting Content Marketing with Natural Language Generation." Marketing Science 41(3): 441–452 (2022-02). [[link]](https://doi.org/10.1287/mksc.2022.1354)

<a id="paper-the-promise-of-generative-ai-for-personalized-persuasion"></a>

- Teeny, Jacob D., et al. "The Promise of Generative AI for Personalized Persuasion." Current Directions in Psychological Science (2026-05). [[link]](https://doi.org/10.1177/09637214261424859)

<a id="paper-knowing-me-telling-me-information-design-in-gen-ai-enabled-communication-in-digital-marketing"></a>

- Hu, Lin, Xueyan Yin, and Juan Feng. "Knowing Me, Telling Me: Information Design in Gen-AI Enabled Communication in Digital Marketing." SSRN 5229032 (2025-05). [[link]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5229032)

---

<a id="model-and-algorithm-augmentation"></a>

## 🔬 3. Model and Algorithm Augmentation

### 3.1 Performance and Limitations

Evidence on the performance, reproducibility, and limitations of LLM-augmented algorithms and synthetic training data, including online-learning mismatch and repeated synthetic training.

<a id="paper-jump-start-or-false-start-a-theoretical-and-empirical-evaluation-of-llm-initialized-bandits"></a>

- Bayley, Adam, et al. "Jump Start or False Start? A Theoretical and Empirical Evaluation of LLM-initialized Bandits." arXiv:2604.02527 (2026-04). [[link]](https://arxiv.org/abs/2604.02527)

<a id="paper-how-powerful-are-llms-to-support-multimodal-recommendation-a-reproducibility-study-of-llmrec"></a>

- Fioretti, Maria Lucia, et al. "How Powerful are LLMs to Support Multimodal Recommendation? A Reproducibility Study of LLMRec." RecSys 2025: 774–782 (2025-09). [[link]](https://doi.org/10.1145/3705328.3748154)

<a id="paper-regurgitative-training-the-value-of-real-data-in-training-large-language-models"></a>

- Zhang, Jinghui, et al. "Regurgitative Training: The Value of Real Data in Training Large Language Models." Management Science (2026-05). [[link]](https://doi.org/10.1287/mnsc.2024.07005)

### 3.2 Methods and Improvements

Methods that use LLM information or synthetic signals to improve choice designs, pricing and demand models, online learning, recommendation, customer-text models, and corrected prediction or measurement.

<a id="paper-jump-starting-bandits-with-llm-generated-prior-knowledge"></a>

- Alamdari, Parand A., Yanshuai Cao, and Kevin H. Wilson. "Jump Starting Bandits with LLM-Generated Prior Knowledge." EMNLP 2024: 19821–19833 (2024-11). [[link]](https://aclanthology.org/2024.emnlp-main.1107/)

<a id="paper-large-language-models-an-applied-econometric-framework"></a>

- Ludwig, Jens, Sendhil Mullainathan, and Ashesh Rambachan. "Large Language Models: An Applied Econometric Framework." Annual Review of Economics 18: 283–316 (2026-04). [[link]](https://doi.org/10.1146/annurev-economics-120925-105620)

<a id="paper-automating-the-b2b-salesperson-pricing-decisions-a-human-machine-hybrid-approach"></a>

- Karlinsky-Shichor, Yael, and Oded Netzer. "Automating the B2B Salesperson Pricing Decisions: A Human-Machine Hybrid Approach." Marketing Science 43(1): 138–157 (2023-06), pricing-automation background. [[link]](https://doi.org/10.1287/mksc.2023.1449)

<a id="paper-using-llm-based-priors-to-optimize-choice-designs-in-conjoint-experiments"></a>

- Eggers, Felix, and Marco Vriens. "Using LLM-Based Priors to Optimize Choice Designs in Conjoint Experiments." SSRN 6719681 (2026-05). [[link]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6719681)

<a id="paper-lola-llm-assisted-online-learning-algorithm-for-content-experiments"></a>

- Ye, Zikun, Hema Yoganarasimhan, and Yufeng Zheng. "LOLA: LLM-Assisted Online Learning Algorithm for Content Experiments." Marketing Science 44(5): 995–1016 (2025-03). [[link]](https://pubsonline.informs.org/doi/10.1287/mksc.2024.0990)

<a id="paper-generative-brand-choice"></a>

- Lee, Kevin. "Generative Brand Choice." (2025-05). [[link]](https://leekevin.io/jmp.pdf)

<a id="paper-large-language-model-augmented-narrative-driven-recommendations"></a>

- Mysore, Sheshera, Andrew McCallum, and Hamed Zamani. "Large Language Model Augmented Narrative Driven Recommendations." RecSys 2023: 777–783 (2023-09). [[link]](https://doi.org/10.1145/3604915.3608829)

<a id="paper-llmrec-large-language-models-with-graph-augmentation-for-recommendation"></a>

- Wei, Wei, et al. "LLMRec: Large Language Models with Graph Augmentation for Recommendation." WSDM 2024 (2024-03). [[link]](https://doi.org/10.1145/3616855.3635853)

<a id="paper-once-boosting-content-based-recommendation-with-both-open-and-closed-source-large-language-models"></a>

- Liu, Qijiong, et al. "ONCE: Boosting Content-based Recommendation with Both Open- and Closed-source Large Language Models." WSDM 2024: 452–461 (2024-03). [[link]](https://doi.org/10.1145/3616855.3635845)

<a id="paper-integrating-large-language-models-into-recommendation-via-mutual-augmentation-and-adaptive-aggregation"></a>

- Luo, Sichun, et al. "Integrating Large Language Models Into Recommendation via Mutual Augmentation and Adaptive Aggregation." IEEE Journal of Selected Topics in Signal Processing 20(1): 77–89 (2026-01). [[link]](https://doi.org/10.1109/JSTSP.2026.3653160)

<a id="paper-mining-novel-customer-needs-for-product-design-from-user-generated-content-through-large-language-model-enabled-data-augmentation-and-ensemble-learning"></a>

- Huang, Shaoqin, Hu Qin, and Yue Wang. "Mining novel customer needs for product design from user-generated content through large language model-enabled data augmentation and ensemble learning." International Journal of Production Research (2026-02). [[link]](https://doi.org/10.1080/00207543.2026.2625971)

---

<a id="contributing"></a>

## 🤝 Contributing

Paper suggestions and citation corrections are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for the reference format.
