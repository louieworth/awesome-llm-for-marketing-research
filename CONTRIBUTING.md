# Contributing

Help improve the collection by suggesting relevant papers or correcting citations.

## Adding a paper

1. Choose the best-fitting category and subsection: Consumer Simulation, Model and Algorithm Augmentation, or Generative Targeting. Distinguish core synthetic-data mechanisms from adjacent foundations or applications.
2. Verify the title, author order, venue or source identifier, date, and paper link against primary sources.
3. Add a reference using the format below. Bold the bracketed number, quote the title, and place the paper link at the end with the label [pdf]. Use the verified journal or workshop name, or the arXiv/SSRN identifier; omit the venue when none is established.
4. Keep numbering continuous across all three categories, include each paper once, and update the category counts, paper anchors, and all affected survey references.

```markdown
<a id="paper-N"></a>

**[N]** Author, First name, et al. "Full paper title." Venue or arXiv/SSRN identifier (YYYY-MM). [[pdf]](https://primary-paper-url)
```

Use YYYY-MM dates: the first online journal publication month when available; otherwise the conference/proceedings publication month, the listed preprint's first posting month, or the date on the author-hosted draft. If a month cannot be verified, keep the candidate in the survey's source gaps rather than inventing a date. Use author names and title from the linked version. Identify a workshop by its full name rather than its parent conference alone. Keep entries limited to citation details and an external paper link.

## Corrections

Include a primary source supporting a corrected title, author list, venue, date, or link. Link to papers externally rather than adding their full text to the repository.

## Survey evidence

Keep the README as a clean reference list. Put comparisons and source limitations in SURVEY.md, with numbered links to the matching README paper anchors supporting substantive claims. Retain primary-source links when they identify the inspected version or a correction. Distinguish inspected full text from abstract-only evidence, and distinguish predicted outcomes from observed behavior. Merge preprint and published versions of the same work; match effect claims to the inspected version.
