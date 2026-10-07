# Contributing

Help improve Awesome LLMs for Marketing Research by suggesting relevant papers or correcting citations.

## Adding a paper

1. Choose the category and subsection by the paper's main contribution, using this order and structure: 1. Consumer Simulation; 2. Generative Targeting; 3. Model and Algorithm Augmentation. Consumer Simulation has 1.1 Capabilities and Opportunities, 1.2 Validity and Limitations, and 1.3 Methods and Improvements. Place demonstrations and use cases in 1.1; behavioral, group, statistical, and causal validity studies and validity-centered reviews in 1.2; and grounding, calibration, supervised fine-tuning, validation, and human-data integration methods in 1.3. Generative Targeting has 2.1 Market Effects and Limitations for advertising, persuasion, and market-outcome evidence or boundary conditions, and 2.2 Methods and Improvements for personalized generation, feedback alignment, creative optimization, and information design. Model and Algorithm Augmentation has 3.1 Performance and Limitations for algorithm evaluations, reproducibility, and synthetic-training risks, and 3.2 Methods and Improvements for choice-design, pricing, demand, online-learning, recommendation, customer-text, and prediction or measurement methods. Classify computer-science papers by their contribution rather than their venue. Preserve the three, two, and two subsections. Include relevant LLM methods, datasets, and limitation research, plus the selected visual generative-AI marketing studies described below.
2. Verify the title, author order, venue or source identifier, date, and paper link against primary sources.
3. Add a reference as a Markdown unordered list item using the format below. Quote the title and place the paper link at the end with the label [link]. Use the verified journal or workshop name, or the arXiv/SSRN identifier; omit the venue when none is established.
4. Include each paper once in the main collection and update the category counts. Use a unique, stable title-based paper anchor for internal links; keep existing anchors unchanged when adding papers. Selected Foundational Papers may repeat a citation and link its title to the main entry.

```markdown
<a id="paper-descriptive-title-slug"></a>

- Author, First name, et al. "Full paper title." Venue or arXiv/SSRN identifier (YYYY-MM). [[link]](https://primary-paper-url)
```

Use YYYY-MM dates: the first online journal publication month when available; otherwise the conference/proceedings publication month, the listed preprint's first posting month, or the date on the author-hosted draft. If a month cannot be verified, flag it for verification rather than inventing a date. Use author names and title from the linked version. Identify a workshop by its full name rather than its parent conference alone. Keep entries limited to citation details and an external paper link.

## Adding a benchmark or dataset

1. Place standalone resources under 1.4 Benchmarks and Datasets, 2.3 Benchmarks and Datasets, or 3.3 Benchmarks and Datasets according to their research use. These resource sections supplement the existing three, two, and two paper subsections. Dataset entries do not increase the paper counts.
2. Link to the official data source, an actionable download location, and the provider's license or access terms. Distinguish data licensing from a repository or package license. State login, contact-sharing, noncommercial, research-use, or permission requirements, and identify an unspecified data license explicitly.
3. Describe what observations or labels are supplied and the research task they support. Identify human observations, synthetic profiles or responses, and creative annotations separately. Do not equate persuasion ratings or strategy labels with causal marketing effects; respect documented training/test splits and leakage risks.
4. Use a unique `dataset-` anchor and keep existing paper anchors unchanged. Cross-link a resource used across categories rather than duplicating it. Verify the release or version against its official documentation; keep raw dataset files outside the repository.

## Corrections

Include a primary source supporting a corrected title, author list, venue, date, or link. Link to papers externally rather than adding their full text to the repository.

## Scope and evidence

Keep the README as a clean reference list. Support scope decisions and corrections with primary sources, and distinguish inspected full text from abstract-only evidence. A general generative-AI label or a text encoder alone does not establish substantive LLM use. Retain research on LLM limitations and mixed-model methods when the LLM component is verified. Flag unresolved cases for verification. Merge preprint and published versions of the same work; match effect claims to the inspected version.

Marketing relevance and inclusion are separate decisions. Recommendation, ratings, product preferences, pricing, customer text, and advertising establish relevant marketing applications when supported by the paper. Selected cross-disciplinary capability, validity, and method studies may remain without a direct marketing task. Record a background exception or unresolved scope in the audit; do not infer LLM use from a generative-AI label or infer marketing relevance from a venue or a prior inclusion decision. Preserve existing citations and stable anchors during category migrations.

Selected visual generative-AI studies of advertising effectiveness and marketing outcomes are included in Generative Targeting, even when their creative-generation component uses diffusion models. Classify these studies by their marketing contribution, and state their model type accurately in supporting audits.
