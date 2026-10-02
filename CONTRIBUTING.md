# Contributing

Help improve Awesome LLMs for Marketing Research by suggesting relevant papers or correcting citations.

## Adding a paper

1. Choose the best-fitting category and subsection: Consumer Simulation, Model and Algorithm Augmentation, or Generative Targeting. Place work that uses digital twins or simulated consumer responses for downstream inference, experiments, or decisions in 1.4 Simulated Experiments and Decision Support, including work with statistical or algorithmic contributions. General LLM training-data augmentation alone does not meet this criterion. Include substantive uses of language or multimodal language models, relevant datasets, or research and reviews on LLM methods and limitations. For mixed-model methods, verify the LLM component against a primary source.
2. Verify the title, author order, venue or source identifier, date, and paper link against primary sources.
3. Add a reference using the format below. Bold the bracketed number, quote the title, and place the paper link at the end with the label [pdf]. Use the verified journal or workshop name, or the arXiv/SSRN identifier; omit the venue when none is established.
4. Keep numbering continuous across all three categories, include each paper once, and update the category counts, paper anchors, and all affected reference links.

```markdown
<a id="paper-N"></a>

**[N]** Author, First name, et al. "Full paper title." Venue or arXiv/SSRN identifier (YYYY-MM). [[pdf]](https://primary-paper-url)
```

Use YYYY-MM dates: the first online journal publication month when available; otherwise the conference/proceedings publication month, the listed preprint's first posting month, or the date on the author-hosted draft. If a month cannot be verified, flag it for verification rather than inventing a date. Use author names and title from the linked version. Identify a workshop by its full name rather than its parent conference alone. Keep entries limited to citation details and an external paper link.

## Corrections

Include a primary source supporting a corrected title, author list, venue, date, or link. Link to papers externally rather than adding their full text to the repository.

## Scope and evidence

Keep the README as a clean reference list. Support scope decisions and corrections with primary sources, and distinguish inspected full text from abstract-only evidence. A general generative-AI label or a text encoder alone does not establish substantive LLM use. Retain research on LLM limitations and mixed-model methods when the LLM component is verified. Flag unresolved cases for verification. Merge preprint and published versions of the same work; match effect claims to the inspected version.
