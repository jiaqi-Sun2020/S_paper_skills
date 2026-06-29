# Chinese-To-English Translation Workflow

Do not translate Chinese scientific prose clause by clause. First recover the argument, then write English prose that serves the target venue.

## Pass 1: Proposition Extraction

For each paragraph, identify:

- the core claim;
- the evidence or equation supporting it;
- the contrast with prior work or baseline;
- the boundary, limitation, or TODO;
- terms that must enter the terminology ledger.

## Pass 2: Logic Reconstruction

Chinese academic drafts often leave links implicit. Rebuild only the links that are already supported by the source:

- contrast: however, by contrast, whereas;
- cause or mechanism: because, this reflects, this arises from;
- consequence: therefore, as a result, this enables;
- boundary: under this condition, within this parameter regime, for the tested cases.

Do not add a new premise to make a paragraph sound smoother.

## Pass 3: Venue Rewrite

- For Nature, broaden the opening frame and reduce specialist density.
- For PRL, compress toward one result and one evidence chain.
- For PRA, keep the mathematical and procedural details needed for trust.

## Pass 4: Sentence Polish

- Use direct subject-verb sentences where possible.
- Split comma-linked chains into smaller sentences.
- Keep technical terms stable rather than using synonyms.
- Match hedge strength to evidence strength.
- Avoid rhetorical flourishes that are not supported by the results.