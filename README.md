<div align="center">

<img src="assets/banner.png" alt="Synthetic consumers and data networks" width="800">

![Consumer Simulation](https://img.shields.io/badge/Consumer_Simulation-66-4C70C8?style=for-the-badge)
![Model and Algorithm Augmentation](https://img.shields.io/badge/Model_%26_Algorithm_Augmentation-11-9865C6?style=for-the-badge)
![Generative Targeting](https://img.shields.io/badge/Generative_Targeting-28-D98757?style=for-the-badge)

</div>

# Awesome LLMs for Marketing Research

A curated list of **papers on large language models (LLMs) for marketing**, organized around consumer simulation, model and algorithm augmentation, and generative targeting.

The collection prioritizes marketing and business-school research, with selected computer-science and social-science methods, validation studies, and reviews. It covers substantive uses of language and multimodal language models, including mixed-model methods, datasets for LLM-based simulation, and research on LLM limitations. Evidence on simulated consumers, downstream learning, and marketing outcomes is grouped by research direction; inclusion does not establish that LLM-generated data are valid substitutes for human observations.

Browse by research direction:

- 🧑 **[1. Consumer Simulation](#consumer-simulation)** — consumer responses, behavioral fidelity, and market insights.
- 🔬 **[2. Model and Algorithm Augmentation](#model-and-algorithm-augmentation)** — calibrated inference, synthetic training signals, and adaptive learning.
- ✨ **[3. Generative Targeting](#generative-targeting)** — synthetic preferences, outcome alignment, and personalized marketing content.

Suggestions and corrections are welcome; see [Contributing](#contributing).

## Contents

- [Awesome LLMs for Marketing Research](#awesome-llms-for-marketing-research)
  - [Contents](#contents)
  - [Selected Foundational Papers](#selected-foundational-papers)
  - [🧑 1. Consumer Simulation](#-1-consumer-simulation)
    - [1.1 Grounding, Construction, and Calibration](#11-grounding-construction-and-calibration)
    - [1.2 Behavioral Fidelity, Heterogeneity, and Statistical Validity](#12-behavioral-fidelity-heterogeneity-and-statistical-validity)
    - [1.3 Preference Measurement and Market Research](#13-preference-measurement-and-market-research)
    - [1.4 Simulated Experiments and Decision Support](#14-simulated-experiments-and-decision-support)
    - [1.5 Reviews and Research Design](#15-reviews-and-research-design)
  - [🔬 2. Model and Algorithm Augmentation](#-2-model-and-algorithm-augmentation)
    - [2.1 Choice Design and Online Learning](#21-choice-design-and-online-learning)
    - [2.2 Recommendation and Customer Text Training](#22-recommendation-and-customer-text-training)
    - [2.3 Training Limits and Direct Prediction](#23-training-limits-and-direct-prediction)
  - [✨ 3. Generative Targeting](#-3-generative-targeting)
    - [3.1 Synthetic Preferences and Demonstration Learning](#31-synthetic-preferences-and-demonstration-learning)
    - [3.2 Human Feedback and Personalized Generation](#32-human-feedback-and-personalized-generation)
    - [3.3 Marketing Field Evidence and Creative Production](#33-marketing-field-evidence-and-creative-production)
    - [3.4 Persuasion, Transparency, and Strategic Boundaries](#34-persuasion-transparency-and-strategic-boundaries)
  - [🤝 Contributing](#-contributing)

## Selected Foundational Papers

A starting set of early studies and selected published or forthcoming work on LLM-based consumer simulation, human cognition, market research, and persuasion. Entries are ordered by reference number and reuse the reference numbers in the full collection.

**[[1]](#paper-1)** Toubia, Olivier, et al. "Database Report: Twin-2K-500: A Data Set for Building Digital Twins of over 2,000 People Based on Their Answers to over 500 Questions." Marketing Science 44(6): 1446–1455 (2025-08). [[pdf]](https://doi.org/10.1287/mksc.2025.0262)

**[[8]](#paper-8)** Leng, Yan, Yunxin Sang, and Ashish Agarwal. "Reducing Disparity Between LLMs and Humans: Optimal LLM Sample Calibration." Marketing Science, forthcoming. [[pdf]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4802019)

**[[9]](#paper-9)** Goli, Ali, and Amandeep Singh. "Frontiers: Can Large Language Models Capture Human Preferences?" Marketing Science 43(4): 709–722 (2024-04). [[pdf]](https://doi.org/10.1287/mksc.2023.0306)

**[[31]](#paper-31)** Ashokkumar, Ashwini, et al. "Large language models can predict the results of social science experiments." Nature 656: 115–122 (2026-07). [[pdf]](https://doi.org/10.1038/s41586-026-10742-x)

**[[35]](#paper-35)** Binz, Marcel, et al. "A foundation model to predict and capture human cognition." Nature 644: 1002–1009 (2025-07). [[pdf]](https://doi.org/10.1038/s41586-025-09215-4)

**[[37]](#paper-37)** Aher, Gati V., Rosa I. Arriaga, and Adam Tauman Kalai. "Using Large Language Models to Simulate Multiple Humans and Replicate Human Subject Studies." ICML 2023, PMLR 202: 337–371 (2023-07). [[pdf]](https://proceedings.mlr.press/v202/aher23a.html)

**[[47]](#paper-47)** Wang, Mengxin, Dennis J. Zhang, and Heng Zhang. "Large Language Models for Market Research: A Data-Augmentation Approach." Marketing Science 45(4): 728–751 (2026-03). [[pdf]](https://doi.org/10.1287/mksc.2025.0009)

---

<a id="consumer-simulation"></a>

## 🧑 1. Consumer Simulation

### 1.1 Grounding, Construction, and Calibration

LLM-based consumer and population models grounded in surveys, interviews, interaction histories, or explicit calibration; selected social-science and NLP benchmarks provide methodological foundations.

<a id="paper-1"></a>

**[1]** Toubia, Olivier, et al. "Database Report: Twin-2K-500: A Data Set for Building Digital Twins of over 2,000 People Based on Their Answers to over 500 Questions." Marketing Science 44(6): 1446–1455 (2025-08). [[pdf]](https://doi.org/10.1287/mksc.2025.0262)

<a id="paper-2"></a>

**[2]** Park, Joon Sung, et al. "LLM Agents Grounded in Self-Reports Enable General-Purpose Simulation of Individuals." arXiv:2411.10109 (2024-11). [[pdf]](https://arxiv.org/abs/2411.10109)

<a id="paper-3"></a>

**[3]** Argyle, Lisa P., et al. "Out of One, Many: Using Language Models to Simulate Human Samples." Political Analysis 31(3): 337–351 (2023-02). [[pdf]](https://doi.org/10.1017/pan.2023.2)


<a id="paper-4"></a>

**[4]** Deng, Yuting, et al. "AI-Moderated Interviews for Market Research and Digital Twins Calibration." arXiv:2609.29143 (2026-09). [[pdf]](https://arxiv.org/abs/2609.29143)

<a id="paper-5"></a>

**[5]** Kinzinger, Leonard, and Jochen Hartmann. "Synthetic Personalities: How Well Can LLMs Mimic Individual Respondents Using Socio-Economic Microdata?" arXiv:2606.04592 (2026-06). [[pdf]](https://arxiv.org/abs/2606.04592)

<a id="paper-6"></a>

**[6]** Fan, Grace Jiarui, et al. "SYN-DIGITS: A Synthetic Control Framework for Calibrated Digital Twin Simulation." arXiv:2604.07513 (2026-04). [[pdf]](https://arxiv.org/abs/2604.07513)

<a id="paper-7"></a>

**[7]** Kolluri, Akaash, et al. "Finetuning LLMs for Human Behavior Prediction in Social Science Experiments." EMNLP 2025 (2025-11). [[pdf]](https://aclanthology.org/2025.emnlp-main.1530/)

<a id="paper-8"></a>

**[8]** Leng, Yan, Yunxin Sang, and Ashish Agarwal. "Reducing Disparity Between LLMs and Humans: Optimal LLM Sample Calibration." Marketing Science, forthcoming. [[pdf]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4802019)

### 1.2 Behavioral Fidelity, Heterogeneity, and Statistical Validity

Evidence on individual responses, population distributions, subgroup representation, causal effects, and artifacts induced by prompts or model design.

<a id="paper-9"></a>

**[9]** Goli, Ali, and Amandeep Singh. "Frontiers: Can Large Language Models Capture Human Preferences?" Marketing Science 43(4): 709–722 (2024-04). [[pdf]](https://doi.org/10.1287/mksc.2023.0306)

<a id="paper-10"></a>

**[10]** Peng, Tianyi, et al. "Digital twins are funhouse mirrors: Five systematic distortions." Science Advances 12(36): eaeh8260 (2026-09). [[pdf]](https://doi.org/10.1126/sciadv.aeh8260)

<a id="paper-11"></a>

**[11]** Xie, Yueqi, et al. "Evaluating the statistical realism of LLM-generated social science data." PNAS 123(19): e2538145123 (2026-05). [[pdf]](https://doi.org/10.1073/pnas.2538145123)

<a id="paper-12"></a>

**[12]** Gao, Yuan, et al. "Take caution in using LLMs as human surrogates." PNAS 122(24): e2501660122 (2025-06). [[pdf]](https://doi.org/10.1073/pnas.2501660122)

<a id="paper-13"></a>

**[13]** Bisbee, James, et al. "Synthetic Replacements for Human Survey Data? The Perils of Large Language Models." Political Analysis 32(4): 401–416 (2024-05). [[pdf]](https://doi.org/10.1017/pan.2024.5)

<a id="paper-14"></a>

**[14]** Wang, Angelina, Jamie Morgenstern, and John P. Dickerson. "Large language models that replace human participants can harmfully misportray and flatten identity groups." Nature Machine Intelligence 7: 400–411 (2025-02). [[pdf]](https://doi.org/10.1038/s42256-025-00986-z)

<a id="paper-15"></a>

**[15]** Santurkar, Shibani, et al. "Whose Opinions Do Language Models Reflect?" ICML 2023, PMLR 202: 29971–30004 (2023-07). [[pdf]](https://proceedings.mlr.press/v202/santurkar23a.html)

<a id="paper-16"></a>

**[16]** Dominguez-Olmedo, Ricardo, Moritz Hardt, and Celestine Mendler-Dünner. "Questioning the Survey Responses of Large Language Models." NeurIPS 2024 (2024-12). [[pdf]](https://proceedings.neurips.cc/paper_files/paper/2024/hash/515c62809e0a29729d7eec26e2916fc0-Abstract-Conference.html)

<a id="paper-17"></a>

**[17]** Durmus, Esin, et al. "Towards Measuring the Representation of Subjective Global Opinions in Language Models." COLM 2024 (2024-10). [[pdf]](https://openreview.net/forum?id=zl16jLb91v)

<a id="paper-18"></a>

**[18]** Tao, Yan, et al. "Cultural bias and cultural alignment of large language models." PNAS Nexus 3(9): pgae346 (2024-09). [[pdf]](https://doi.org/10.1093/pnasnexus/pgae346)

<a id="paper-19"></a>

**[19]** Salecha, Aadesh, et al. "Large language models display human-like social desirability biases in Big Five personality surveys." PNAS Nexus 3(12): pgae533 (2024-12). [[pdf]](https://doi.org/10.1093/pnasnexus/pgae533)

<a id="paper-20"></a>

**[20]** Zewail, Aliah, et al. "Moral stereotyping in large language models." PNAS 123(10): e2519941123 (2026-03). [[pdf]](https://doi.org/10.1073/pnas.2519941123)

<a id="paper-21"></a>

**[21]** Pataranutaporn, Pat, et al. "Simulating human well-being with large language models: Systematic validation and misestimation across 64,000 individuals from 64 countries." PNAS 122(48): e2519394122 (2025-11). [[pdf]](https://doi.org/10.1073/pnas.2519394122)

<a id="paper-22"></a>

**[22]** Boelaert, Julien, et al. "Machine Bias. How Do Generative Language Models Answer Opinion Polls?" Sociological Methods & Research 54(3): 1156–1196 (2025-04). [[pdf]](https://doi.org/10.1177/00491241251330582)

<a id="paper-23"></a>

**[23]** Brucks, Melanie, and Olivier Toubia. "Prompt architecture induces methodological artifacts in large language models." PLOS ONE 20(4): e0319159 (2025-04). [[pdf]](https://doi.org/10.1371/journal.pone.0319159)


<a id="paper-24"></a>

**[24]** Liu, Ryan, et al. "Large Language Models Assume People are More Rational than We Really are." ICLR 2025 (2025-04). [[pdf]](https://proceedings.iclr.cc/paper_files/paper/2025/hash/7cdb411d07bdf6cd43ddf1254fae98cd-Abstract-Conference.html)

<a id="paper-25"></a>

**[25]** Hu, Tiancheng, et al. "SimBench: Benchmarking the Ability of Large Language Models to Simulate Human Behaviors." ICLR 2026 (2026-04). [[pdf]](https://proceedings.iclr.cc/paper_files/paper/2026/hash/2fc4d6a6400addda7493b9db258c34e0-Abstract-Conference.html)


<a id="paper-26"></a>

**[26]** Kuric, Eduard, Peter Demcak, and Matus Krajcovic. "Distorted Perspectives of LLM-Simulated Preferences: Can AI Mislead Design?" arXiv:2605.18311 (2026-05). [[pdf]](https://arxiv.org/abs/2605.18311)


<a id="paper-27"></a>

**[27]** Xie, Yu, and Yueqi Xie. "Variance reduction in output from generative AI." arXiv:2503.01033 (2025-03). [[pdf]](https://arxiv.org/abs/2503.01033)

<a id="paper-28"></a>

**[28]** Yin, Haonan, Shai Vardi, and Vidyanand Choudhary. "Fragile preferences: A deep dive into order effects in large language models." PNAS Nexus 5(8): pgag246 (2026-08). [[pdf]](https://doi.org/10.1093/pnasnexus/pgag246)

### 1.3 Preference Measurement and Market Research

Measurement and validation of synthetic purchase intent and willingness to pay.


<a id="paper-29"></a>

**[29]** Maier, Benjamin F., et al. "LLMs Reproduce Human Purchase Intent via Semantic Similarity Elicitation of Likert Ratings." arXiv:2510.08338 (2025-10). [[pdf]](https://arxiv.org/abs/2510.08338)

<a id="paper-30"></a>

**[30]** Oetzel, Sebastian, and Tobias Maiberger. "How price sensitive is AI? Benchmarking LLM-generated willingness to pay in pricing analytics." Journal of Marketing Analytics (2026-09). [[pdf]](https://doi.org/10.1057/s41270-026-00542-7)


### 1.4 Simulated Experiments and Decision Support

Digital twins and simulated consumers support downstream inference, experiments, and decisions, including statistical calibration, human sample allocation, preference estimation, and adaptive learning. Related behavioral and cognition studies assess the opportunities and limits of simulation-based decision support.

<a id="paper-31"></a>

**[31]** Ashokkumar, Ashwini, et al. "Large language models can predict the results of social science experiments." Nature 656: 115–122 (2026-07). [[pdf]](https://doi.org/10.1038/s41586-026-10742-x)

<a id="paper-32"></a>

**[32]** Horton, John J., Apostolos Filippas, and Benjamin S. Manning. "Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?" arXiv:2301.07543 (2023-01). [[pdf]](https://arxiv.org/abs/2301.07543)

<a id="paper-33"></a>

**[33]** Li, Han, et al. "SimGym: A Framework for A/B Test Simulation in E-Commerce with Traffic-Grounded VLM Agents." arXiv:2605.19219 (2026-05). [[pdf]](https://arxiv.org/abs/2605.19219)

<a id="paper-34"></a>

**[34]** France, Stephen L., and Pia A. Albinsson. "Synthetic Consumer Insight Generation with Large Language Models." arXiv:2607.05761 (2026-07). [[pdf]](https://arxiv.org/abs/2607.05761)

<a id="paper-35"></a>

**[35]** Binz, Marcel, et al. "A foundation model to predict and capture human cognition." Nature 644: 1002–1009 (2025-07). [[pdf]](https://doi.org/10.1038/s41586-025-09215-4)

<a id="paper-36"></a>

**[36]** Eriksson, Kimmo, et al. "Large language models outperform humans at estimating society’s everyday norms." Communications AI & Computing 1: 15 (2026-09). [[pdf]](https://doi.org/10.1038/s44488-026-00018-8)

<a id="paper-37"></a>

**[37]** Aher, Gati V., Rosa I. Arriaga, and Adam Tauman Kalai. "Using Large Language Models to Simulate Multiple Humans and Replicate Human Subject Studies." ICML 2023, PMLR 202: 337–371 (2023-07). [[pdf]](https://proceedings.mlr.press/v202/aher23a.html)

<a id="paper-38"></a>

**[38]** Arora, Neeraj, Ishita Chakraborty, and Yohei Nishimura. "AI–Human Hybrids for Marketing Research: Leveraging Large Language Models (LLMs) as Collaborators." Journal of Marketing 89(2): 43–70 (2024-08). [[pdf]](https://doi.org/10.1177/00222429241276529)

<a id="paper-39"></a>

**[39]** Gui, George, and Olivier Toubia. "The Challenge of Using LLMs to Simulate Human Behavior: A Causal Inference Perspective." SSRN 4650172 (2023-12). [[pdf]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4650172)

<a id="paper-40"></a>

**[40]** Hullman, Jessica, et al. "This human study did not involve human subjects: Validating LLM simulations as behavioral evidence." arXiv:2602.15785 (2026-02). [[pdf]](https://arxiv.org/abs/2602.15785)

<a id="paper-41"></a>

**[41]** Li, Zonghan, and Feng Ji. "Statistical realism is not evidence that LLMs can estimate treatment effects in social science experiments." arXiv:2604.02458 (2026-04). [[pdf]](https://arxiv.org/abs/2604.02458)

<a id="paper-42"></a>

**[42]** Chen, Zihan, Di Zhu, and Lei Nico Zheng. "When Synthetic Users Fail: A Cross-Domain Benchmark of LLM-Simulated Human Survey Responses." arXiv:2607.26348 (2026-07). [[pdf]](https://arxiv.org/abs/2607.26348)

<a id="paper-43"></a>

**[43]** Kuric, Eduard, Peter Demcak, and Matus Krajcovic. "What Would GPT Click: Practical Effects of Human-AI Behavioral Misalignment and the Cost of Synthetic Participants in User Experience." arXiv:2605.18302 (2026-05). [[pdf]](https://arxiv.org/abs/2605.18302)

<a id="paper-44"></a>

**[44]** Brand, James, Ayelet Israeli, and Donald Ngwe. "Using LLMs for Market Research." SSRN 4395751 (2023-03). [[pdf]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4395751)

<a id="paper-45"></a>

**[45]** Li, Peiyao, et al. "Frontiers: Determining the Validity of Large Language Models for Automated Perceptual Analysis." Marketing Science 43(2): 254–266 (2024-01). [[pdf]](https://doi.org/10.1287/mksc.2023.0454)

<a id="paper-46"></a>

**[46]** Netzer, Oded, and Rajan Sambandam. "Synthetic Data in Marketing Research: How to Evaluate and When to Trust." arXiv:2609.13995 (2026-09). [[pdf]](https://arxiv.org/abs/2609.13995)

<a id="paper-47"></a>

**[47]** Wang, Mengxin, Dennis J. Zhang, and Heng Zhang. "Large Language Models for Market Research: A Data-Augmentation Approach." Marketing Science 45(4): 728–751 (2026-03). [[pdf]](https://doi.org/10.1287/mksc.2025.0009)

<a id="paper-48"></a>

**[48]** Lu, Cheng, et al. "Generative Augmented Inference." ICML 2026, PMLR 306: 81730–81751 (2026-07). [[pdf]](https://proceedings.mlr.press/v306/lu26am.html)

<a id="paper-49"></a>

**[49]** Ye, Zikun, and Hema Yoganarasimhan. "Rectification Difficulty and Optimal Sample Allocation in LLM-Augmented Surveys." arXiv:2604.17267 (2026-04). [[pdf]](https://arxiv.org/abs/2604.17267)

<a id="paper-50"></a>

**[50]** Ye, Zikun, Jiameng Lyu, and Rui Tao. "Allocating Human Oversight in AI-Enabled Analytics." arXiv:2604.12497 (2026-04). [[pdf]](https://arxiv.org/abs/2604.12497)

<a id="paper-51"></a>

**[51]** Liu, Tianming, et al. "Distributionally Robust LLM Augmentation of Discrete Choice Models." SSRN 7500939 (2026-09). [[pdf]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7500939)

<a id="paper-52"></a>

**[52]** Krsteski, Stefan, et al. "Valid Survey Simulations with Limited Human Data: The Roles of Prompting, Fine-Tuning, and Rectification." ACL 2026, Long Papers: 10887–10906 (2026-07). [[pdf]](https://aclanthology.org/2026.acl-long.498/)

<a id="paper-53"></a>

**[53]** Baek, Jackie, et al. "LLM-SAA: LLM-persona Generated Distributions for Decision-making." arXiv:2602.06357 (2026-02). [[pdf]](https://arxiv.org/abs/2602.06357)

<a id="paper-54"></a>

**[54]** Huang, Chengpiao, and Kaizheng Wang. "LLM-Powered Virtual Population for Demand Simulation and Pricing." arXiv:2606.16183 (2026-06). [[pdf]](https://arxiv.org/abs/2606.16183)

<a id="paper-55"></a>

**[55]** Alamdari, Parand A., Yanshuai Cao, and Kevin H. Wilson. "Jump Starting Bandits with LLM-Generated Prior Knowledge." EMNLP 2024: 19821–19833 (2024-11). [[pdf]](https://aclanthology.org/2024.emnlp-main.1107/)

<a id="paper-56"></a>

**[56]** Bayley, Adam, et al. "Jump Start or False Start? A Theoretical and Empirical Evaluation of LLM-initialized Bandits." arXiv:2604.02527 (2026-04). [[pdf]](https://arxiv.org/abs/2604.02527)

<a id="paper-57"></a>

**[57]** Casero, Emilio, et al. "Customer Digital Twins in the Field: Cross-Sell Micro-Personalization at Scale." Columbia Business School research record (2026-09). [[pdf]](https://business.columbia.edu/faculty/research/customer-digital-twins-field-cross-sell-micro-personalization-scale)


### 1.5 Reviews and Research Design

Reviews, perspectives, and methodological guidance on using simulated participants as research evidence.

<a id="paper-58"></a>

**[58]** Toubia, Olivier. "Synthetic Data and Digital Twins: The Hype, The Facts, the Promise." SSRN 7065919 (2026-07). [[pdf]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7065919)

<a id="paper-59"></a>

**[59]** Abdurahman, Suhaib, et al. "Perils and opportunities in using large language models in psychological research." PNAS Nexus 3(7): pgae245 (2024-07). [[pdf]](https://doi.org/10.1093/pnasnexus/pgae245)

<a id="paper-60"></a>

**[60]** Dillion, Danica, et al. "Can AI language models replace human participants?" Trends in Cognitive Sciences 27(7): 597–600 (2023-05). [[pdf]](https://doi.org/10.1016/j.tics.2023.04.008)

<a id="paper-61"></a>

**[61]** Agnew, William, et al. "The Illusion of Artificial Inclusion." CHI 2024 (2024-05). [[pdf]](https://doi.org/10.1145/3613904.3642703)

<a id="paper-62"></a>

**[62]** Lin, Zhicheng. "Six Fallacies in Substituting Large Language Models for Human Participants." Advances in Methods and Practices in Psychological Science (2025-08). [[pdf]](https://doi.org/10.1177/25152459251357566)

<a id="paper-63"></a>

**[63]** Lin, Zhicheng. "Large Language Models as Psychological Simulators: A Methodological Guide." Advances in Methods and Practices in Psychological Science 9(1) (2026-02). [[pdf]](https://doi.org/10.1177/25152459251410153)

<a id="paper-64"></a>

**[64]** Karetnikov, Nikita, Iyad Rahwan, and Davor Svetinovic. "Large language models as human proxies." Nature Computational Science (2026-09). [[pdf]](https://doi.org/10.1038/s43588-026-01060-3)

<a id="paper-65"></a>

**[65]** Kuric, Eduard, Peter Demcak, and Matus Krajcovic. "Synthetic Participants Generated by Large Language Models: A Systematic Literature Review." Research Square (2026-03). [[pdf]](https://doi.org/10.21203/rs.3.rs-9057643/v1)

<a id="paper-66"></a>

**[66]** Zeng, Yongchao, Calum Brown, and Mark Rounsevell. "Too human to model: the uncanny valley of large language models in simulating human systems." npj Complexity 3: 13 (2026-03). [[pdf]](https://doi.org/10.1038/s44260-026-00075-1)

---

<a id="model-and-algorithm-augmentation"></a>

## 🔬 2. Model and Algorithm Augmentation

### 2.1 Choice Design and Online Learning

LLM-based priors inform human experiment design, while direct content predictions support adaptive experimentation.

<a id="paper-67"></a>

**[67]** Eggers, Felix, and Marco Vriens. "Using LLM-Based Priors to Optimize Choice Designs in Conjoint Experiments." SSRN 6719681 (2026-05). [[pdf]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6719681)


<a id="paper-68"></a>

**[68]** Ye, Zikun, Hema Yoganarasimhan, and Yufeng Zheng. "LOLA: LLM-Assisted Online Learning Algorithm for Content Experiments." Marketing Science 44(5): 995–1016 (2025-03). [[pdf]](https://pubsonline.informs.org/doi/10.1287/mksc.2024.0990)


### 2.2 Recommendation and Customer Text Training

Selected CS and product-research bridges where generated requests, profiles, graph edges, or labeled texts train downstream models.

<a id="paper-69"></a>

**[69]** Mysore, Sheshera, Andrew McCallum, and Hamed Zamani. "Large Language Model Augmented Narrative Driven Recommendations." RecSys 2023: 777–783 (2023-09). [[pdf]](https://doi.org/10.1145/3604915.3608829)

<a id="paper-70"></a>

**[70]** Wei, Wei, et al. "LLMRec: Large Language Models with Graph Augmentation for Recommendation." WSDM 2024 (2024-03). [[pdf]](https://doi.org/10.1145/3616855.3635853)

<a id="paper-71"></a>

**[71]** Fioretti, Maria Lucia, et al. "How Powerful are LLMs to Support Multimodal Recommendation? A Reproducibility Study of LLMRec." RecSys 2025: 774–782 (2025-09). [[pdf]](https://doi.org/10.1145/3705328.3748154)

<a id="paper-72"></a>

**[72]** Liu, Qijiong, et al. "ONCE: Boosting Content-based Recommendation with Both Open- and Closed-source Large Language Models." WSDM 2024: 452–461 (2024-03). [[pdf]](https://doi.org/10.1145/3616855.3635845)

<a id="paper-73"></a>

**[73]** Luo, Sichun, et al. "Integrating Large Language Models Into Recommendation via Mutual Augmentation and Adaptive Aggregation." IEEE Journal of Selected Topics in Signal Processing 20(1): 77–89 (2026-01). [[pdf]](https://doi.org/10.1109/JSTSP.2026.3653160)

<a id="paper-74"></a>

**[74]** Huang, Shaoqin, Hu Qin, and Yue Wang. "Mining novel customer needs for product design from user-generated content through large language model-enabled data augmentation and ensemble learning." International Journal of Production Research (2026-02). [[pdf]](https://doi.org/10.1080/00207543.2026.2625971)

<a id="paper-75"></a>

**[75]** Li, Zhuoyan, et al. "Synthetic Data Generation with Large Language Models for Text Classification: Potential and Limitations." EMNLP 2023: 10443–10461 (2023-12). [[pdf]](https://aclanthology.org/2023.emnlp-main.647/)

### 2.3 Training Limits and Direct Prediction

Adjacent boundary evidence: recursive model training and direct utility prediction, rather than a new synthetic consumer sample.

<a id="paper-76"></a>

**[76]** Zhang, Jinghui, et al. "Regurgitative Training: The Value of Real Data in Training Large Language Models." Management Science (2026-05). [[pdf]](https://doi.org/10.1287/mnsc.2024.07005)

<a id="paper-77"></a>

**[77]** Lee, Kevin. "Generative Brand Choice." (2025-05). [[pdf]](https://leekevin.io/jmp.pdf)

---

<a id="generative-targeting"></a>

## ✨ 3. Generative Targeting

### 3.1 Synthetic Preferences and Demonstration Learning

Generated preference pairs, model-rated examples, or synthetic labels help train and align content generation. Some evidence remains restricted to synthetic or offline evaluation.

<a id="paper-78"></a>

**[78]** Cheng, Mengjie, Elie Ofek, and Hema Yoganarasimhan. "Balancing Engagement and Polarization: Multi-Objective Alignment of News Content Using LLMs." arXiv:2504.13444 (2025-04). [[pdf]](https://arxiv.org/abs/2504.13444)

<a id="paper-79"></a>

**[79]** Dey, Priyanka, et al. "GRAVITY: A Framework for Personalized Text Generation via Profile-Grounded Synthetic Preferences." EACL 2026, Long Papers: 7416–7436 (2026-03). [[pdf]](https://aclanthology.org/2026.eacl-long.348/)

<a id="paper-80"></a>

**[80]** Singh, Anikait, et al. "FSPO: Few-Shot Optimization of Synthetic Preferences Personalizes to Real Users." ICLR 2026 (2026-04). [[pdf]](https://proceedings.iclr.cc/paper_files/paper/2026/file/b2118ec72f6396c7e7bb2407e2d05eb4-Paper-Conference.pdf)

<a id="paper-81"></a>

**[81]** Challapalli, Vedasamhitha, et al. "SLM4Offer: Personalized Marketing Offer Generation Using Contrastive Learning Based Fine-Tuning." arXiv:2508.15471 (2025-08). [[pdf]](https://arxiv.org/abs/2508.15471)

<a id="paper-82"></a>

**[82]** Si, Harini, et al. "Long-Term Ad Memorability: Understanding & Generating Memorable Ads." WACV 2025 (2025-02). [[pdf]](https://openaccess.thecvf.com/content/WACV2025/html/Si_Long-Term_Ad_Memorability_Understanding__Generating_Memorable_Ads_WACV_2025_paper.html)

### 3.2 Human Feedback and Personalized Generation

Related generation methods grounded in real interactions, experiments, or estimated outcomes; synthetic demonstrations are not the main training input in every paper.

<a id="paper-83"></a>

**[83]** Yin, Mingzhang, Ruijiang Gao, and Ziwei Cong. "Generative Personalization with Textual and Non-textual Data." SSRN 5329729 (2025-06). [[pdf]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5329729)

<a id="paper-84"></a>

**[84]** Angelopoulos, Panagiotis, Kevin Lee, and Sanjog Misra. "Causal Alignment: Augmenting Language Models with A/B Tests." SSRN 4781850 (2024-04). [[pdf]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4781850)


<a id="paper-85"></a>

**[85]** Lee, Kevin, et al. "Offline-to-Online Creative Optimization with Generative Models and Adaptive Testing." arXiv:2607.23696 (2026-07). [[pdf]](https://arxiv.org/abs/2607.23696)

<a id="paper-86"></a>

**[86]** Ellickson, Paul B., et al. "Evaluating Novel Unstructured Treatments with Generative AI: A Causal Prediction Framework." Journal of Marketing Research (2026-08). [[pdf]](https://doi.org/10.1177/00222437261476639)

<a id="paper-87"></a>

**[87]** Xu, Yexing, et al. "Design Your Ad: Personalized Advertising Image and Text Generation with Unified Autoregressive Models." CVPR 2026 (2026-06). [[pdf]](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Design_Your_Ad_Personalized_Advertising_Image_and_Text_Generation_with_CVPR_2026_paper.pdf)

### 3.3 Marketing Field Evidence and Creative Production

Adjacent commercial applications test generated creatives and personalized delivery. Producing content alone does not establish synthetic training-data quality or incremental personalization value.

<a id="paper-88"></a>

**[88]** Kapoor, Anuj, and Madhav Kumar. "Frontiers: Generative AI and Personalized Video Advertisements." Marketing Science 44(4): 733–747 (2025-05). [[pdf]](https://doi.org/10.1287/mksc.2023.0494)

<a id="paper-89"></a>

**[89]** Reisenbichler, Martin, Thomas Reutterer, and David A. Schweidel. "Applying Large Language Models to Sponsored Search Advertising." Marketing Science 45(1): 123–141 (2025-11). [[pdf]](https://doi.org/10.1287/mksc.2023.0611)

<a id="paper-90"></a>

**[90]** Reisenbichler, Martin, et al. "Frontiers: Supporting Content Marketing with Natural Language Generation." Marketing Science 41(3): 441–452 (2022-02). [[pdf]](https://doi.org/10.1287/mksc.2022.1354)

<a id="paper-91"></a>

**[91]** Exner, Yannick, et al. "AI in Disguise—Quasi-Experimental Analysis of a Large-Scale Deployment of AI-Generated Ads." SSRN 5096969 (2025-03). [[pdf]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5096969)

<a id="paper-92"></a>

**[92]** Lee, Hyesoo, et al. "The Impact of Visual Generative AI on Advertising Effectiveness." SSRN 5638311 (2025-11). [[pdf]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5638311)

<a id="paper-93"></a>

**[93]** Dubé, Jean-Pierre, and Ariel Xu. "Large Language Models and Creative Content Design: a case study of email marketing at Wine Access." Quantitative Marketing and Economics 24: Article 1 (2026-01). [[pdf]](https://doi.org/10.1007/s11129-025-09303-9)

<a id="paper-94"></a>

**[94]** Gu, Wenying, et al. "When Machines Persuade Better Than Humans: Generative AI, Cognitive Constraints, and Promotional Effectiveness." SSRN 6294798 (2026-02). [[pdf]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6294798)

<a id="paper-95"></a>

**[95]** Fang, Lu, et al. "Generative AI and Sales Productivity: Field Experiments in Online Retail." arXiv:2510.12049 (2025-10). [[pdf]](https://arxiv.org/abs/2510.12049)


### 3.4 Persuasion, Transparency, and Strategic Boundaries

Selected behavioral studies, transparency research, and economic models clarify the effects and limits of personalized generation. Political persuasion is adjacent evidence; strategic models and conceptual reviews are context rather than synthetic-data validation.

<a id="paper-96"></a>

**[96]** Matz, Sandra C., et al. "The potential of generative AI for personalized persuasion at scale." Scientific Reports 14: 4692 (2024-02). [[pdf]](https://doi.org/10.1038/s41598-024-53755-0)

<a id="paper-97"></a>

**[97]** Teeny, Jacob D., et al. "The Promise of Generative AI for Personalized Persuasion." Current Directions in Psychological Science (2026-05). [[pdf]](https://doi.org/10.1177/09637214261424859)

<a id="paper-98"></a>

**[98]** Teeny, Jacob D., and Sandra C. Matz. "We need to understand “when” not “if” generative AI can enhance personalized persuasion." PNAS 121(43): e2418005121 (2024-10). [[pdf]](https://doi.org/10.1073/pnas.2418005121)

<a id="paper-99"></a>

**[99]** Hackenburg, Kobi, and Helen Margetts. "Evaluating the persuasive influence of political microtargeting with large language models." PNAS 121(24): e2403116121 (2024-06). [[pdf]](https://doi.org/10.1073/pnas.2403116121)

<a id="paper-100"></a>

**[100]** Simchon, Almog, Matthew Edwards, and Stephan Lewandowsky. "The persuasive effects of political microtargeting in the age of generative artificial intelligence." PNAS Nexus 3(2): pgae035 (2024-01). [[pdf]](https://doi.org/10.1093/pnasnexus/pgae035)

<a id="paper-101"></a>

**[101]** Salvi, Francesco, et al. "On the conversational persuasiveness of GPT-4." Nature Human Behaviour 9: 1645–1653 (2025-05). [[pdf]](https://doi.org/10.1038/s41562-025-02194-6)

<a id="paper-102"></a>

**[102]** Meguellati, Elyas, et al. "LLM-Generated Ads: From Personalization Parity to Persuasion Superiority." arXiv:2512.03373 (2025-12). [[pdf]](https://arxiv.org/abs/2512.03373)

<a id="paper-103"></a>

**[103]** Tang, Brian Jay, et al. "Ads that Talk Back: Implications and Perceptions of Injecting Personalized Advertising into LLM Chatbots." Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies 9(4): Article 213 (2025-12). [[pdf]](https://doi.org/10.1145/3770640)

<a id="paper-104"></a>

**[104]** Fainmesser, Itay P., Dominique Olie Lauga, and Elie Ofek. "Will it Click? Advertising Strategy with Generative AI." SSRN 6517138 (2026-04). [[pdf]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6517138)

<a id="paper-105"></a>

**[105]** Hu, Lin, Xueyan Yin, and Juan Feng. "Knowing Me, Telling Me: Information Design in Gen-AI Enabled Communication in Digital Marketing." SSRN 5229032 (2025-05). [[pdf]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5229032)


<a id="contributing"></a>

## 🤝 Contributing

Paper suggestions and citation corrections are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for the reference format.
