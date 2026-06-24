---
name: latex-paper-build-skill
description: Build, restructure, and maintain complete research-paper delivery pipelines centered on LaTeX manuscripts. Use when Codex needs to inspect an existing .tex paper, generate a project-specific LaTeX scaffold, split a monolithic manuscript into modular files, preserve revtex/ctex/fontspec/BibTeX conventions, check figure and bibliography paths, choose XeLaTeX/latexmk build commands, or orchestrate a full paper workflow from research logic, experiment design, training-code outputs, HTML research reports, manuscript architecture, compilation, and submission checks.
---

# LaTeX Paper Build Skill

## Overview

Use this skill to turn a research idea or LaTeX paper directory into a maintainable paper-delivery pipeline without overwriting the original source. The default target is a scientific manuscript with research notes, experiment plans, training outputs, reports, `main.tex`, `preamble.tex`, `frontmatter.tex`, modular `sections/`, `figures/`, `references/`, `notes/`, and a reproducible build path.

## Workflow

1. Discover the paper context before editing.
   - Find the main `.tex`, `.bib`, figure directories, compiled PDFs/logs, and venue class.
   - Prefer `rg --files`, then inspect `\documentclass`, packages, `\title`, `\section`, `\includegraphics`, `\bibliographystyle`, and `\bibliography`.
   - If the project is the QWCT/QWTA paper under `2026_06_17`, read `references/qwct-paper-profile.md`.
   - If creating or reorganizing a framework, read `references/framework-contract.md`.

2. Choose the operation.
   - Full paper pipeline: read `references/paper-pipeline.md` and use the sibling skills listed there when available.
   - Existing monolithic paper: run `scripts/scaffold_latex_paper.py` with `--source`.
   - Pipeline workspace: run `scripts/create_paper_pipeline.py`.
   - New paper with similar conventions: copy or adapt `assets/revtex-qwct-template/`.
   - Compile/debug request: preserve the current file layout, then run the build command and fix only the failing surface.
   - Writing-only request: defer to the user's writing skill or local paper-writing rules; this skill owns architecture, paths, and build mechanics.

3. Generate the framework non-destructively.
   - Never overwrite the original manuscript unless the user explicitly asks.
   - Create a new output directory such as `<paper>_latex_framework`.
   - Keep one source of truth for packages in `preamble.tex`.
   - Keep title/authors/abstract in `frontmatter.tex`.
   - Keep each top-level section in `sections/NN_slug.tex`.
   - Move/copy cited bibliography files into `references/` and update `\bibliography{references/<stem>}`.
   - Copy only referenced figures unless the user asks for the whole asset tree.

4. Validate the result.
   - Run `python -m py_compile scripts/scaffold_latex_paper.py` after script edits.
   - Run the skill validator after skill edits:
     `python C:\Users\SSS\.codex\skills\.system\skill-creator\scripts\quick_validate.py <skill-dir>`
   - For generated LaTeX frameworks, prefer:
     `latexmk -xelatex -bibtex -interaction=nonstopmode -file-line-error -outdir=build main.tex`
   - If `latexmk` is unavailable, use `xelatex`, `bibtex`, `xelatex`, `xelatex`.

## Script Entry Point

Create a complete pipeline workspace:

```powershell
python scripts\create_paper_pipeline.py --project path\to\paper_pipeline --title "Paper Title"
```

Attach an existing LaTeX manuscript to that pipeline:

```powershell
python scripts\create_paper_pipeline.py --project path\to\paper_pipeline --title "Paper Title" --latex-source path\to\paper.tex --bib path\to\refs.bib --copy-figures
```

Generate only the LaTeX framework:

Use:

```powershell
python scripts\scaffold_latex_paper.py --source path\to\paper.tex --bib path\to\refs.bib --out path\to\paper_latex_framework --copy-figures
```

Useful options:

- `--inspect-only`: print a Markdown structure report without writing a framework.
- `--force`: allow overwriting files inside the output directory.
- `--copy-figures`: copy referenced figure files into `figures/` and rewrite include paths.
- `--paper-key`: override the generated project key used in reports.

## Build Rules

- Use XeLaTeX when the paper loads `ctex` or `fontspec`.
- Preserve `revtex4-2` options unless the user asks for a venue change.
- Preserve labels, citations, equations, algorithms, captions, and section content verbatim during scaffolding.
- Treat bibliography drift as a build issue. For example, if the source says `\bibliography{QWTA_cite}` but the available file is `QWCT_cite.bib`, rewrite the generated framework to the available `.bib` and report the drift.
- Do not silently convert Chinese text encodings. Read as UTF-8 first, then fall back to `gb18030`/`cp936`; write generated framework files as UTF-8.

## Pipeline Integration

When this skill lives inside a skill bundle such as `S_paper_skills`, treat sibling skills as pipeline stages rather than duplicated content. Read only the sibling `SKILL.md` needed for the active stage:

- `../research-logic-skill/SKILL.md` for contribution logic and mechanism-level claims.
- `../experiment-design-skill/SKILL.md` for paper-grade validation plans.
- `../training-code-architecture-skill/SKILL.md` for reusable experiment code architecture and result contracts.
- `../research-html-report/SKILL.md` for shareable research briefs and publication-style HTML reports.
- `../skill-audit-refactor/SKILL.md` when the pipeline skill itself needs pruning or restructuring.

Do not copy all sibling skill instructions into context by default. Use `references/paper-pipeline.md` as the routing contract.

## Extensibility

Add new paper or venue behavior by adding one focused reference file under `references/` and, only when deterministic automation is needed, a script under `scripts/`. Keep `SKILL.md` as the routing layer rather than a large manual.
