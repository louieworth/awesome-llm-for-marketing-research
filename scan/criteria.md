# 自动扫描的收录规则

本文件定义每周自动扫描推荐论文的标准。它比 CONTRIBUTING.md 的收录范围**更窄**，两者同时适用。分类和引用格式仍以 CONTRIBUTING.md 为准。修改本文件后，下一次扫描立即生效。

## 三条推荐路径（track）

### A. `consumer_simulation`：消费者 digital twin / 消费者模拟 → 第 1 类

用 LLM 模拟消费者或顾客（包括 digital twin、synthetic respondents、silicon samples、personas），并且用在营销情境里，例如：

- 偏好、选择、conjoint、支付意愿（WTP）
- 购买意向、产品或概念评价、品牌认知
- 对广告或价格的反应
- 市场调研问卷、顾客访谈

模拟方法、效度检验、局限性研究都算。**作者单位不限**，用私有数据（如电商平台日志）也照常收录。

### B. `public_data_simulation`：用公开人类回答数据做的 LLM 人类模拟 → 第 1 类

不要求营销场景。论文必须用公开的人类回答数据集，构建或评估 LLM 对人的模拟（个体或群体层面的回答分布）。例如：

- OpinionQA、Twin-2K-500
- GSS、ANES、World Values Survey、Pew American Trends Panel、European Social Survey
- Many Labs 等公开实验复现数据

**作者单位不限。** 只是把 LLM 当作经济或社会主体放进博弈、辩论、多智能体互动里，没有和公开人类数据对比的，不属于这条路径。

### C. `marketing_method`：营销内容生成或算法增强 → 第 2、3 类

满足 CONTRIBUTING.md 对第 2 类（内容生成与个性化）或第 3 类（模型与算法增强）的要求，同时**至少一位作者来自商学院**。按以下方式处理：

- 确认有商学院作者：推荐。
- 确认没有：排除。
- 无法确认：列为待定，并写明查到的单位。

**什么算商学院**：business school、school of management，以及商学院内的 marketing、operations、information systems、strategy 等系。例如 Wharton、Booth、Kellogg、HBS、Stern、Columbia Business School、MIT Sloan、Rotman、Ivey、INSEAD、LBS、HKUST Business School、CKGSB、北大光华、清华经管。

经济系、计算机系、统计系、心理系，以及企业研究院（如 Google、Meta、阿里、快手），都**不算**。

## 一律排除

- 只是把 LLM 当作被研究的产品或市场（例如 LLM 平台的定价理论），没有用 LLM 模拟消费者，也不是营销方法里的组件。
- 通用的 agent、工具调用、RL、推荐系统工程论文，而且没有商学院作者。
- 只贴了 "generative AI" 标签，没有实质使用 LLM。
