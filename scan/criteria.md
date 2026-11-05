# 自动扫描的收录规则

本文件定义自动扫描推荐论文的标准。它比 CONTRIBUTING.md 的收录范围**更窄**，两者同时适用；分类和引用格式以 CONTRIBUTING.md 为准。修改本文件后，下一次扫描立即生效。

本文件中的 LLM 包括 transformer 模型，例如在营销数据上训练的顾客旅程或消费序列 transformer。

## 第一层：UTD 24 期刊，基本都收

论文发表在 UTD 24 期刊上（列表见 `scripts/scan_config.json` 的 `journal_sets.utd24`），并且 LLM 或生成式 AI 是它的研究工具、研究对象或方法组件，就推荐。这一层**不限下面的三条路径，也不限作者单位**，按 CONTRIBUTING.md 分类即可。

以下情况不算：

- 只在文中顺带提到 AI；
- 研究的是 LLM 出现之前的规则型 chatbot 或传统机器学习（transformer 模型不算传统机器学习）。

## 第二层：其他来源，要求商学院作者

适用于 arXiv、SSRN、会议论文和非 UTD 期刊。论文必须同时满足：

- 属于下面三条路径之一（A、B、C）；
- **至少一位作者来自商学院。**

作者单位的处理：

- 确认有商学院作者：推荐。
- 确认没有：转入第三层判断。
- 无法确认：列为待定，并写明查到的单位。

## 第三层：没有商学院作者（多为 CS / NLP 社区），只收有影响力的工作

属于 A、B、C 路径，但没有商学院作者的论文，只在以下任一情况下推荐：

- 引用数 ≥ 100，或年均引用 ≥ 50。阈值在 `scan_config.json` 的 `influence` 中设置。
- agent 判断它特别有价值，并写明理由。例如：被营销或社会科学研究广泛使用的数据集、基准或方法。

LLM 文化或价值观对齐研究，例如用 WVS、Pew 测模型的文化立场或做价值观对齐，**只能通过第三层进入**。

## 三条推荐路径（track）

### A. `consumer_simulation`：消费者 digital twin / 消费者模拟 → 第 1 类

用 LLM 模拟消费者或顾客，用在营销情境里，例如：

- 偏好、选择、conjoint、支付意愿（WTP）；
- 购买意向、产品或概念评价、品牌认知；
- 对广告或价格的反应；
- 市场调研问卷、顾客访谈。

形式包括 digital twin、synthetic respondents、silicon samples、personas。模拟方法、效度检验、局限性研究都算，私有数据也算。

### B. `public_data_simulation`：用公开人类回答数据做的 LLM 人类模拟 → 第 1 类

不要求营销场景。论文必须用公开的人类回答数据集，构建或评估 LLM 对人的模拟，也就是看模拟出的个体或群体回答分布与真人是否一致。常见数据集有：

- OpinionQA、Twin-2K-500；
- GSS、ANES、World Values Survey、Pew American Trends Panel、European Social Survey；
- Many Labs 等公开实验复现数据。

**以下不属于 B**，只能走第三层：

- 只用这些数据集测量或对齐模型本身的价值观，比如做文化对齐、价值观对齐、文化偏差测评；
- 把 LLM 当作博弈或多智能体中的主体，但没有与公开人类数据对比。

### C. `marketing_method`：营销内容生成或算法增强 → 第 2、3 类

满足 CONTRIBUTING.md 对第 2 类（内容生成与个性化）或第 3 类（模型与算法增强）的要求。

## 什么算商学院

**算商学院的：**

- business school、school of management；
- 商学院内的 marketing、operations、information systems、strategy、finance、accounting 等系；
- 例如 Wharton、Booth、Kellogg、HBS、Stern、Columbia Business School、MIT Sloan、Rotman、Ivey、INSEAD、LBS、HKUST Business School、CKGSB、北大光华、清华经管。

**不算的：**

- 经济系、计算机系、统计系、心理系；
- 企业研究院，例如 Google、Meta、阿里、快手。

## 一律排除（第一层 UTD 期刊除外）

- 只把 LLM 当作被研究的产品或市场的论文。例如 LLM 平台定价理论、品牌在 LLM 回答中的曝光审计。这类论文既没有用 LLM 模拟消费者，LLM 也不是营销方法的组件。
- 通用的 agent、工具调用、RL、推荐系统工程论文。
- 只贴了 "generative AI" 标签，没有实质使用 LLM 的论文。
