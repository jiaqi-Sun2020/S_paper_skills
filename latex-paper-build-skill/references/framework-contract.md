# LaTeX Framework Contract

Use this contract when generating or reviewing a managed LaTeX paper framework.

## Target Tree

```text
paper_latex_framework/
  main.tex
  preamble.tex
  frontmatter.tex
  backmatter.tex
  latexmkrc
  sections/
    01_introduction.tex
    02_background.tex
    ...
  figures/
    referenced-figure-files
  references/
    paper.bib
  notes/
    paper_context.md
```

## File Responsibilities

- `main.tex`: orchestration only. It should contain `\input{preamble}`, `\begin{document}`, `\input{frontmatter}`, section inputs, `\input{backmatter}`, and `\end{document}`.
- `preamble.tex`: document class, numbering policy, packages, theorem definitions, and macros.
- `frontmatter.tex`: title, authors, affiliations, date, abstract, and `\maketitle`.
- `sections/*.tex`: one top-level section per file. Preserve labels and internal subsection structure.
- `backmatter.tex`: bibliography style, bibliography command, acknowledgments, appendices, and any final material.
- `figures/`: only figures referenced by the generated framework unless the user asks for archival copy.
- `references/`: BibTeX or BibLaTeX databases used by the paper.
- `notes/paper_context.md`: generated structure report and known mechanical issues.

## Generation Rules

- Generate into a new directory by default.
- Write UTF-8 text files.
- Keep source prose unchanged when splitting.
- Keep labels unchanged unless fixing duplicates with explicit user approval.
- Keep citation keys unchanged.
- Rewrite bibliography paths only when the generated file layout requires it.
- Rewrite figure paths only when the corresponding figure file has been copied.
- Prefer short, stable slugs: `01_introduction.tex`, `02_background.tex`, `03_model.tex`, `04_experiments.tex`, `05_conclusion.tex`.

## Build Rules

- Use `latexmk -xelatex -bibtex -interaction=nonstopmode -file-line-error -outdir=build main.tex` for `ctex` or `fontspec` papers.
- Use `latexmk -pdf` only when the paper has no Unicode/fontspec dependency.
- Keep build artifacts out of manuscript source folders.
- After compilation, inspect `.log` warnings for undefined references, missing citations, missing figures, overfull boxes, and font warnings.
