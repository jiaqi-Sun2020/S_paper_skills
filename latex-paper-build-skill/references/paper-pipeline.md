# Paper Pipeline Contract

Use this reference when the user asks for a complete paper pipeline, or when `latex-paper-build-skill` is installed inside a bundle such as `S_paper_skills`.

## Pipeline Stages

```text
0. Intake and project inventory
1. Research logic
2. Experiment design
3. Training code and result contract
4. Research HTML report
5. LaTeX manuscript architecture
6. Build, audit, and submission checks
```

Each stage should produce a durable artifact. Avoid treating chat-only reasoning as complete unless the user explicitly wants a discussion rather than a managed project.

## Stage 0: Intake and Inventory

Goal: identify what already exists and what is missing.

Inspect:

- paper idea or current manuscript;
- available `.tex`, `.bib`, figures, PDFs, logs;
- experiment code, configs, outputs, metrics CSVs;
- reports or planning notes;
- target venue, language, page limit, anonymity status.

Recommended artifact:

```text
00_research_logic/intake.md
```

Minimum contents:

- one-sentence project identity;
- current source assets;
- missing decisions;
- target pipeline stage.

## Stage 1: Research Logic

Sibling skill: `../research-logic-skill/SKILL.md`

Use when the contribution, mechanism, or method combination is unclear.

Artifact:

```text
00_research_logic/research_logic.md
```

It should contain:

- native function of each method;
- direct connection point;
- shallow integration baseline;
- mechanism-level reconstruction;
- claim discipline and boundaries.

Exit gate:

- central mechanism is stated as a state, operator, update rule, or assumption change;
- claims avoid generic "we improve performance" phrasing;
- open theory gaps are explicit.

## Stage 2: Experiment Design

Sibling skill: `../experiment-design-skill/SKILL.md`

Use after the central claim is known, before running or rewriting experiments.

Artifact:

```text
01_experiment_design/experiment_plan.md
```

It should contain:

- central claim;
- research questions;
- datasets and tasks;
- baselines;
- ablations;
- mechanism checks;
- metrics and tables;
- failure cases;
- claim boundaries;
- minimum viable experiment plan.

Exit gate:

- every claim maps to an experiment or TODO;
- every table/figure in the future paper has a purpose;
- baselines include strong and mechanism-neighbor alternatives.

## Stage 3: Training Code and Results

Sibling skill: `../training-code-architecture-skill/SKILL.md`

Use when creating or standardizing experiment code.

Artifacts:

```text
02_training_code/
03_results/
```

Expected result contract:

```text
outputs/runs/{run_name}/
  config.json
  checkpoints/best.pt
  logs/train.log
  results/train_history.csv
  results/final_metrics.csv
  results/ablation_ready_metrics.csv
```

Exit gate:

- training entrypoint is reproducible;
- configs are copied into run folders;
- final metrics can feed paper tables;
- result files include model, variant, dataset, seed, metric, split, and checkpoint path.

## Stage 4: Research HTML Report

Sibling skill: `../research-html-report/SKILL.md`

Use when the user wants a shareable research brief, a paper-planning dashboard, or a printable pre-paper report.

Artifact:

```text
04_reports/<project-key>.html
```

Exit gate:

- report states the exact claim;
- mechanism, experiment plan, evidence matrix, risks, and TODOs are visible;
- missing evidence is marked as TODO rather than implied as complete.

## Stage 5: LaTeX Manuscript Architecture

This skill owns this stage.

Artifacts:

```text
05_manuscript/
  main.tex
  preamble.tex
  frontmatter.tex
  sections/
  figures/
  references/
  notes/paper_context.md
```

Use `scripts/scaffold_latex_paper.py` for existing monolithic papers. Use `assets/revtex-qwct-template/` for new REVTeX/QWCT-style manuscripts.

Exit gate:

- source manuscript is modular;
- original source remains untouched unless explicitly requested;
- figure and bibliography paths resolve;
- labels and citation keys are preserved.

## Stage 6: Build, Audit, and Submission

Use after the manuscript exists.

Required checks:

- compile with `latexmk -xelatex -bibtex -interaction=nonstopmode -file-line-error -outdir=build main.tex` when `ctex` or `fontspec` is used;
- check undefined references and citations;
- check missing figures;
- check bibliography drift;
- check figure formats and raster/vector suitability;
- check page count and venue constraints if known;
- check anonymity if double blind.

Artifact:

```text
06_submission/build_report.md
```

Exit gate:

- PDF builds;
- unresolved references are listed or fixed;
- warnings that affect submission are separated from harmless typography warnings.

## Default Project Tree

```text
paper_pipeline/
  00_research_logic/
    intake.md
    research_logic.md
  01_experiment_design/
    experiment_plan.md
  02_training_code/
  03_results/
  04_reports/
  05_manuscript/
  06_submission/
    build_report.md
  pipeline_context.md
```

## Routing Rules

- If the user asks "is this idea a paper?", start at Stage 1.
- If the idea is clear but evidence is weak, start at Stage 2.
- If the experiments exist but code/results are messy, start at Stage 3.
- If the user wants a visual plan or shareable summary, start at Stage 4.
- If the user has a `.tex` manuscript or asks for paper architecture, start at Stage 5.
- If the user has a manuscript and wants readiness, start at Stage 6.

Do not require all stages for small edits. A pipeline exists to preserve continuity, not to create ceremony.
