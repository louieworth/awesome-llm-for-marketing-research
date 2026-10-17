# Consumer Simulation: 1.3 严格方法贡献审查记录

更新日期：2026-10-14。用户最终澄清：仅缩减 1.3，1.1 和 1.2 的原有论文全部保留。此前的整节筛选方案已撤回；本记录仅说明 1.3 的方法标准与条目迁移。

后续调整（2026-10-17）：README 的 1.3 当前标题为 Methods and Improvements。各论文小节先列已发表论文，再列未发表论文，两组内分别按引用月份从早到晚排序。以下保留 2026-10-14 的审查记录及当时计数，当前条目与数量以 README 为准。

## 审查时的范围与计数

| 小节 | 原有条目保留情况 | 当前论文数 |
| --- | --- | ---: |
| 1.1 Capabilities and Opportunities | 恢复原有全部 13 篇 | 13 |
| 1.2 Validity and Limitations | 恢复原有全部 35 篇，并保留从 1.3 迁入的 50、51、58、60 | 39 |
| 1.3 Methodological Innovations | 严格方法清单 | 10 |
| 1.4 Benchmarks and Datasets | 恢复原有 3 篇，并保留 SimGym（56） | 4 |
| 主节合计 | 论文引用计数，不含数据资源表 | 66 |
| 方法补充列表 | 保留其余原 1.3 条目 | 8 |
| 原始 Consumer Simulation 引用总数 | 全部保留在主节或补充列表 | 74 |

全部原有数据资源均恢复至 1.4。论文仍按引用月份从新到旧排序，未核实月份的引用放在所在列表末尾。审查序号沿用初始 74 篇清单的编号，便于对应先前讨论。

## 1.3 的严格标准

论文的核心贡献应是可复用、明确可操作的方法对象，例如估计量、校准目标、算法、概率模型、正式回答测量程序，或有计算刻画的决策评估方法。比较访谈形式、数据深度、模型或提示变体，以及综合工作流的应用展示，不自动构成这里要求的方法创新。

## 1.3 保留的 10 篇

| 审查序号 | 论文 | 明确的核心方法贡献 | 核验来源 |
| ---: | --- | --- | --- |
| 65 | [Distributionally Robust LLM Augmentation of Discrete Choice Models](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7500939) | **Wasserstein 稳健两阶段校准估计**。在校准分布不确定性下优化真人和 LLM 的关系，给出有限维优化形式、特定线性情形的凸锥表示与误差保证。 | [作者原始摘要，索引可读](https://papers.ssrn.com/sol3/Delivery.cfm/7500939.pdf?abstractid=7500939&mirid=1) |
| 62 | [Generative Augmented Inference](https://proceedings.mlr.press/v306/lu26am.html) | **GAI 正交矩估计**。把 AI 输出作为辅助特征，用灵活的非参数关系及正交矩构造估计量，建立渐近推断与效率比较。 | [会议摘要与作者稿](https://arxiv.org/abs/2604.14575) |
| 67 | [LLM-Powered Virtual Population for Demand Simulation and Pricing](https://arxiv.org/abs/2606.16183) | **人设混合的概率需求模型及拟合程序**。定义人设购买概率混合及 Binomial 需求分布，估计混合权重与曝光量，并考虑需求截断和概率尺度校准。核心是模型、目标函数及估计算法。 | [第 2 节，式 2.1-2.4 及 Algorithm 1](https://arxiv.org/pdf/2606.16183) |
| 52 | [SYN-DIGITS: A Synthetic Control Framework for Calibrated Digital Twin Simulation](https://arxiv.org/abs/2604.07513) | **潜因子视角下的数字孪生校准框架**。通过模拟回答与真人回答的潜空间对齐，构造 fit-and-transfer 校准；给出对齐条件和误差分析。十种被比较的方法不都应称为新算法。 | [第 3 节、校准条件与实验](https://arxiv.org/pdf/2604.07513) |
| 63 | [Rectification Difficulty and Optimal Sample Allocation in LLM-Augmented Surveys](https://arxiv.org/abs/2604.17267) | **纠偏难度驱动的最优样本配置**。刻画题目级 rectification difficulty，推导固定预算下的最优配置，再用历史任务预测新任务的难度。Neyman 配置本身是既有原理，方法创新在 LLM 问卷中的刻画与配置框架。 | [配置推导与任务迁移程序](https://arxiv.org/pdf/2604.17267) |
| 64 | [Allocating Human Oversight in AI-Enabled Analytics](https://arxiv.org/abs/2604.12497) | **UCB 真人验证预算配置算法**。在线学习未知纠偏难度，通过置信界配置真人验证预算，并给出相对 oracle 配置的理论效率损失分析。 | [Algorithm 1 与 regret analysis](https://arxiv.org/pdf/2604.12497) |
| 61 | [Large Language Models for Market Research: A Data-Augmentation Approach](https://doi.org/10.1287/mksc.2025.0009) | **真人与合成消费者数据的联合估计**。构造数据增广估计程序，并给出一致性、渐近正态性与有限样本误差界。方法对象是消费偏好参数的统计估计。 | [出版社原始摘要](https://doi.org/10.1287/mksc.2025.0009) |
| 70 | [LLM-SAA: LLM-persona Generated Distributions for Decision-making](https://arxiv.org/abs/2602.06357) | **决策质量的最坏 competitive-ratio 计算方法**。定义给定真人与合成分布时的最坏决策损失，并推导产品组合、定价和 newsvendor 情形下的计算方法。技术贡献是新的评估优化问题及计算刻画，不将套用 SAA 本身视为创新。 | [贡献段与第 4-6 节定理、计算程序](https://arxiv.org/pdf/2602.06357) |
| 55 | [LLMs Reproduce Human Purchase Intent via Semantic Similarity Elicitation of Likert Ratings](https://arxiv.org/abs/2510.08338) | **SSR 回答测量程序**。将自由文本购买意愿、量表锚点的 embedding 相似度转为 Likert 回答概率。核心对象是明确的文本到概率分布映射，属于 elicitation/measurement 方法。 | [第 3 节与附录 C.1](https://arxiv.org/pdf/2510.08338) |
| 54 | [Reducing Disparity Between LLMs and Humans: Optimal LLM Sample Calibration](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4802019) | **HuMCal 校准权重优化**。用真人聚合基准学习多个 elicitation variants 的可信度权重，定义可求解的校准目标及校准样本上的 baseline-safe 性质。 | [作者原始摘要，索引可读](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4802019) |

## 原 1.3 全部 23 条的去向

| 原审查序号 | 论文 | 当前位置 | 分类依据 |
| ---: | --- | --- | --- |
| 50 | [AI-Moderated Interviews for Market Research and Digital Twins Calibration.](../README.md#paper-ai-moderated-interviews-for-market-research-and-digital-twins-calibration) | 1.2 | 访谈及孪生有效性比较。 |
| 60 | [Synthetic Data in Marketing Research: How to Evaluate and When to Trust.](../README.md#paper-synthetic-data-in-marketing-research-how-to-evaluate-and-when-to-trust) | 1.2 | 准确性测量与随机森林 OOB 诊断。 |
| 65 | [Distributionally Robust LLM Augmentation of Discrete Choice Models.](../README.md#paper-distributionally-robust-llm-augmentation-of-discrete-choice-models) | 1.3 | 已确认的严格方法清单，具体方法对象见上表。 |
| 62 | [Generative Augmented Inference.](../README.md#paper-generative-augmented-inference) | 1.3 | 已确认的严格方法清单，具体方法对象见上表。 |
| 66 | [Valid Survey Simulations with Limited Human Data: The Roles of Prompting, Fine-Tuning, and Rectification.](consumer-simulation-method-supplement.md#paper-valid-survey-simulations-with-limited-human-data-the-roles-of-prompting-fine-tuning-and-rectification) | 方法补充列表 | A general panel-survey study, retained as supporting methodology outside the confirmed ten-paper list. |
| 51 | [Synthetic Personalities: How Well Can LLMs Mimic Individual Respondents Using Socio-Economic Microdata?](../README.md#paper-synthetic-personalities-how-well-can-llms-mimic-individual-respondents-using-socio-economic-microdata) | 1.2 | 构建条件及数据深度的经验比较。 |
| 67 | [LLM-Powered Virtual Population for Demand Simulation and Pricing.](../README.md#paper-llm-powered-virtual-population-for-demand-simulation-and-pricing) | 1.3 | 已确认的严格方法清单，具体方法对象见上表。 |
| 56 | [SimGym: A Framework for A/B Test Simulation in E-Commerce with Traffic-Grounded VLM Agents.](../README.md#paper-simgym-a-framework-for-a-b-test-simulation-in-e-commerce-with-traffic-grounded-vlm-agents) | 1.4 | 按用户指定归入 benchmark 与测试框架。 |
| 52 | [SYN-DIGITS: A Synthetic Control Framework for Calibrated Digital Twin Simulation.](../README.md#paper-syn-digits-a-synthetic-control-framework-for-calibrated-digital-twin-simulation) | 1.3 | 已确认的严格方法清单，具体方法对象见上表。 |
| 63 | [Rectification Difficulty and Optimal Sample Allocation in LLM-Augmented Surveys.](../README.md#paper-rectification-difficulty-and-optimal-sample-allocation-in-llm-augmented-surveys) | 1.3 | 已确认的严格方法清单，具体方法对象见上表。 |
| 64 | [Allocating Human Oversight in AI-Enabled Analytics.](../README.md#paper-allocating-human-oversight-in-ai-enabled-analytics) | 1.3 | 已确认的严格方法清单，具体方法对象见上表。 |
| 61 | [Large Language Models for Market Research: A Data-Augmentation Approach.](../README.md#paper-large-language-models-for-market-research-a-data-augmentation-approach) | 1.3 | 已确认的严格方法清单，具体方法对象见上表。 |
| 69 | [Large Language Models as Psychological Simulators: A Methodological Guide.](consumer-simulation-method-supplement.md#paper-large-language-models-as-psychological-simulators-a-methodological-guide) | 方法补充列表 | A general guide to psychological personas, validation, and cognitive modeling. |
| 70 | [LLM-SAA: LLM-persona Generated Distributions for Decision-making.](../README.md#paper-llm-saa-llm-persona-generated-distributions-for-decision-making) | 1.3 | 已确认的严格方法清单，具体方法对象见上表。 |
| 53 | [Finetuning LLMs for Human Behavior Prediction in Social Science Experiments.](consumer-simulation-method-supplement.md#paper-finetuning-llms-for-human-behavior-prediction-in-social-science-experiments) | 方法补充列表 | A general social-science fine-tuning study, outside the confirmed ten-paper method list. |
| 55 | [LLMs Reproduce Human Purchase Intent via Semantic Similarity Elicitation of Likert Ratings.](../README.md#paper-llms-reproduce-human-purchase-intent-via-semantic-similarity-elicitation-of-likert-ratings) | 1.3 | 已确认的严格方法清单，具体方法对象见上表。 |
| 68 | [New Tools, New Rules: A Practical Guide to Effective and Responsible Generative AI Use for Surveys and Experiments in Research.](consumer-simulation-method-supplement.md#paper-new-tools-new-rules-a-practical-guide-to-effective-and-responsible-generative-ai-use-for-surveys-and-experiments-in-research) | 方法补充列表 | A practical guide covering survey design, administration, coding, and interpretation. |
| 71 | [Variance reduction in output from generative AI.](consumer-simulation-method-supplement.md#paper-variance-reduction-in-output-from-generative-ai) | 方法补充列表 | A perspective on reduced output variance, retained as background rather than a method innovation. |
| 57 | [AI-Human Hybrids for Marketing Research: Leveraging Large Language Models (LLMs) as Collaborators.](consumer-simulation-method-supplement.md#paper-ai-human-hybrids-for-marketing-research-leveraging-large-language-models-llms-as-collaborators) | 方法补充列表 | A human-AI collaboration framework and empirical application, outside the strict method list. |
| 54 | [Reducing Disparity Between LLMs and Humans: Optimal LLM Sample Calibration.](../README.md#paper-reducing-disparity-between-llms-and-humans-optimal-llm-sample-calibration) | 1.3 | 已确认的严格方法清单，具体方法对象见上表。 |
| 58 | [The Challenge of Using LLMs to Simulate Human Behavior: A Causal Inference Perspective.](../README.md#paper-the-challenge-of-using-llms-to-simulate-human-behavior-a-causal-inference-perspective) | 1.2 | 提示歧义、因果有效性与 unblinding 设计原则。 |
| 59 | [Using LLMs for Market Research.](consumer-simulation-method-supplement.md#paper-using-llms-for-market-research) | 方法补充列表 | A foundational market-research study retained here while the original 1.1 membership is restored. |
| 49 | [Twinface: Generating synthetic faces for multimodal consumer digital twins.](consumer-simulation-method-supplement.md#paper-twinface-generating-synthetic-faces-for-multimodal-consumer-digital-twins) | 方法补充列表 | The original manuscript is unavailable; the existing citation points to a secondary review. Its relation to The Face of Digital Twins remains unverified. |

## 58、60 的方法贡献

58 形式化提示歧义，并给出 unblinding 提示协议；本次分类重心为模拟实验的识别和设计有效性。60 给出随机森林 out-of-bag $R^2$ 的问题可回答性诊断；本次分类重心为准确性测量和经验筛查。两篇均保留在 1.2。

核验来源：[58 正文第 4、5 节及附录 F](https://arxiv.org/pdf/2312.15524)，[60 第 4.2 节及验证](https://arxiv.org/pdf/2609.13995)。其余方法证据见上表的原始来源；本记录不宣称已独立验证所有理论结果。

## 引用时间依据

HuMCal 的期刊出版月份尚不明确，保留原有 forthcoming 标记，按 [SSRN 首次发布月份 2024-04](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4802019)排序并注明日期性质。Toubia 综述保留 [SSRN 首次发布月份 2026-07](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7065919)。
