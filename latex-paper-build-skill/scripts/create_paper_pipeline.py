#!/usr/bin/env python3
"""Create a complete research-paper pipeline workspace."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path


STAGE_DIRS = (
    "00_research_logic",
    "01_experiment_design",
    "02_training_code",
    "03_results",
    "04_reports",
    "05_manuscript",
    "06_submission",
)


def slugify(text: str) -> str:
    tokens = re.findall(r"[A-Za-z0-9]+", text.lower())
    return "-".join(tokens[:8]) if tokens else "paper-project"


def write_text(path: Path, text: str, force: bool) -> None:
    if path.exists() and not force:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def copy_template(skill_dir: Path, manuscript_dir: Path, title: str, force: bool) -> None:
    template_dir = skill_dir / "assets" / "revtex-qwct-template"
    if not template_dir.exists():
        return

    for source in template_dir.rglob("*"):
        relative = source.relative_to(template_dir)
        destination = manuscript_dir / relative
        if source.is_dir():
            destination.mkdir(parents=True, exist_ok=True)
            continue
        if destination.exists() and not force:
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)

    frontmatter = manuscript_dir / "frontmatter.tex"
    if frontmatter.exists():
        text = frontmatter.read_text(encoding="utf-8")
        text = re.sub(r"\\title\{[^}]*\}", lambda _m: f"\\title{{{title}}}", text, count=1)
        frontmatter.write_text(text, encoding="utf-8")


def run_latex_scaffold(
    skill_dir: Path,
    latex_source: Path,
    bib: Path | None,
    manuscript_dir: Path,
    copy_figures: bool,
    force: bool,
) -> None:
    script = skill_dir / "scripts" / "scaffold_latex_paper.py"
    command = [
        sys.executable,
        str(script),
        "--source",
        str(latex_source),
        "--out",
        str(manuscript_dir),
    ]
    if bib:
        command.extend(["--bib", str(bib)])
    if copy_figures:
        command.append("--copy-figures")
    if force:
        command.append("--force")
    subprocess.run(command, check=True)


def pipeline_context(title: str, project_key: str, latex_source: Path | None) -> str:
    source_line = f"- LaTeX source: `{latex_source}`" if latex_source else "- LaTeX source: TODO"
    return f"""
# Paper Pipeline Context

- Title: {title}
- Project key: {project_key}
- Created: {date.today().isoformat()}
{source_line}

## Stage Map

| Stage | Folder | Sibling skill | Status |
|---|---|---|---|
| Intake and inventory | `00_research_logic/` | this skill | TODO |
| Research logic | `00_research_logic/research_logic.md` | `research-logic` | TODO |
| Experiment design | `01_experiment_design/experiment_plan.md` | `experiment-design` | TODO |
| Training code/results | `02_training_code/`, `03_results/` | `training-code-architecture` | TODO |
| HTML research report | `04_reports/` | `research-html-report` | TODO |
| LaTeX manuscript | `05_manuscript/` | `latex-paper-build-skill` | TODO |
| Build/submission audit | `06_submission/` | `latex-paper-build-skill` | TODO |

## Next Step

Start at the first TODO stage whose artifact is missing or too weak to support the later stages.
"""


def intake_template(title: str) -> str:
    return f"""
# Intake

- Paper title: {title}
- One-sentence identity: TODO
- Target venue: TODO
- Language: TODO
- Page limit: TODO
- Blind-review constraints: TODO

## Existing Assets

- Manuscript: TODO
- Bibliography: TODO
- Figures: TODO
- Experiment code: TODO
- Result files: TODO
- Reports/notes: TODO

## Missing Decisions

- TODO
"""


def research_logic_template() -> str:
    return """
# Research Logic

Use `research-logic` for this stage.

## Central Mechanism

TODO

## Native Functions

TODO

## Direct Connection

TODO

## Mechanism-Level Reconstruction

TODO

## Claim Discipline

TODO
"""


def experiment_plan_template() -> str:
    return """
# Experiment Plan

Use `experiment-design` for this stage.

## Central Claim

TODO

## Research Questions

TODO

## Datasets and Tasks

TODO

## Baselines

TODO

## Ablations

TODO

## Mechanism Checks

TODO

## Metrics and Tables

TODO

## Claim Boundaries

TODO
"""


def build_report_template() -> str:
    return """
# Build and Submission Report

## Build Command

```powershell
latexmk -xelatex -bibtex -interaction=nonstopmode -file-line-error -outdir=build main.tex
```

## Checks

| Check | Status | Notes |
|---|---|---|
| PDF builds | TODO | |
| Undefined references | TODO | |
| Undefined citations | TODO | |
| Missing figures | TODO | |
| Bibliography drift | TODO | |
| Page count | TODO | |
| Anonymization | TODO | |
"""


def create_pipeline(args: argparse.Namespace) -> None:
    skill_dir = Path(__file__).resolve().parents[1]
    project = Path(args.project).resolve()
    title = args.title
    project_key = args.project_key or slugify(title)
    latex_source = Path(args.latex_source).resolve() if args.latex_source else None
    bib = Path(args.bib).resolve() if args.bib else None

    project.mkdir(parents=True, exist_ok=True)
    for stage in STAGE_DIRS:
        (project / stage).mkdir(parents=True, exist_ok=True)

    write_text(project / "pipeline_context.md", pipeline_context(title, project_key, latex_source), args.force)
    write_text(project / "00_research_logic" / "intake.md", intake_template(title), args.force)
    write_text(project / "00_research_logic" / "research_logic.md", research_logic_template(), args.force)
    write_text(project / "01_experiment_design" / "experiment_plan.md", experiment_plan_template(), args.force)
    write_text(project / "06_submission" / "build_report.md", build_report_template(), args.force)

    manuscript_dir = project / "05_manuscript"
    if latex_source:
        run_latex_scaffold(skill_dir, latex_source, bib, manuscript_dir, args.copy_figures, args.force)
    elif not args.no_template:
        copy_template(skill_dir, manuscript_dir, title, args.force)

    print(f"Created paper pipeline: {project}")
    print(f"Pipeline context: {project / 'pipeline_context.md'}")
    print(f"Manuscript folder: {manuscript_dir}")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, help="Output project/pipeline directory.")
    parser.add_argument("--title", required=True, help="Paper title used in generated context and template.")
    parser.add_argument("--project-key", help="Stable short key for reports and artifacts.")
    parser.add_argument("--latex-source", help="Existing .tex file to scaffold into 05_manuscript/.")
    parser.add_argument("--bib", help="Bibliography file to use when --latex-source is provided.")
    parser.add_argument("--copy-figures", action="store_true", help="Copy referenced figures when scaffolding LaTeX.")
    parser.add_argument("--no-template", action="store_true", help="Do not copy the default LaTeX template when no source is provided.")
    parser.add_argument("--force", action="store_true", help="Overwrite generated files.")
    return parser.parse_args(argv)


if __name__ == "__main__":
    try:
        create_pipeline(parse_args(sys.argv[1:]))
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
