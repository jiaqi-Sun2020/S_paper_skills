#!/usr/bin/env python3
"""Generate a project-local .agents context folder for AI coding agents."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


SKIP_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".idea",
    ".vscode",
    ".venv",
    "venv",
    "env",
    "node_modules",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "dist",
    "build",
    "target",
    ".next",
    ".turbo",
}

OUTPUT_LIKE_DIRS = {
    "data",
    "datasets",
    "results",
    "outputs",
    "runs",
    "experiments",
    "checkpoints",
    "figures",
    "logs",
}


@dataclass
class ProjectFacts:
    root: Path
    project_name: str
    generated_at: str
    git_branch: str | None = None
    git_remote: str | None = None
    readme_summary: str | None = None
    detected_stacks: list[str] = field(default_factory=list)
    top_dirs: list[str] = field(default_factory=list)
    top_files: list[str] = field(default_factory=list)
    tree_lines: list[str] = field(default_factory=list)
    docs: list[str] = field(default_factory=list)
    existing_agent_files: list[str] = field(default_factory=list)
    config_files: list[str] = field(default_factory=list)
    env_files: list[str] = field(default_factory=list)
    ci_files: list[str] = field(default_factory=list)
    entry_points: list[str] = field(default_factory=list)
    test_paths: list[str] = field(default_factory=list)
    output_dirs: list[str] = field(default_factory=list)
    commands: list[tuple[str, str, str]] = field(default_factory=list)
    decisions: list[str] = field(default_factory=list)


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def safe_read_text(path: Path, limit: int = 12000) -> str:
    try:
        with path.open("r", encoding="utf-8", errors="replace") as fh:
            return fh.read(limit)
    except OSError:
        return ""


def run_git(root: Path, args: list[str]) -> str | None:
    try:
        proc = subprocess.run(
            ["git", "-C", str(root), *args],
            check=False,
            capture_output=True,
            text=True,
            timeout=5,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    if proc.returncode != 0:
        return None
    out = proc.stdout.strip()
    return out or None


def iter_files(root: Path, max_files: int = 5000) -> Iterable[Path]:
    count = 0
    for current, dirnames, filenames in os.walk(root):
        current_path = Path(current)
        dirnames[:] = [
            d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".git")
        ]
        for name in filenames:
            if count >= max_files:
                return
            path = current_path / name
            if path.is_file():
                count += 1
                yield path


def first_readme_summary(root: Path) -> str | None:
    candidates = [
        root / "README.md",
        root / "readme.md",
        root / "README.rst",
        root / "README.txt",
    ]
    for path in candidates:
        if not path.exists():
            continue
        text = safe_read_text(path, 8000)
        lines = []
        for raw in text.splitlines():
            line = raw.strip()
            if not line:
                if lines:
                    break
                continue
            if line.startswith(("#", "=", "-", "```", "![", "[!")):
                cleaned = re.sub(r"^#+\s*", "", line).strip()
                if cleaned and not cleaned.startswith(("=", "-", "```", "![")):
                    lines.append(cleaned)
                continue
            lines.append(line)
            if len(" ".join(lines)) > 420:
                break
        summary = " ".join(lines).strip()
        return summary[:600] if summary else None
    return None


def top_level(root: Path) -> tuple[list[str], list[str]]:
    dirs: list[str] = []
    files: list[str] = []
    for child in sorted(root.iterdir(), key=lambda p: p.name.lower()):
        if child.name in SKIP_DIRS:
            continue
        if child.is_dir():
            dirs.append(child.name + "/")
        elif child.is_file():
            files.append(child.name)
    return dirs[:80], files[:80]


def small_tree(root: Path, max_depth: int = 2, max_entries: int = 120) -> list[str]:
    lines: list[str] = [root.name + "/"]
    count = 0

    def walk(path: Path, prefix: str, depth: int) -> None:
        nonlocal count
        if depth > max_depth or count >= max_entries:
            return
        children = [
            p
            for p in sorted(path.iterdir(), key=lambda x: x.name.lower())
            if p.name not in SKIP_DIRS
        ]
        for idx, child in enumerate(children):
            if count >= max_entries:
                return
            connector = "`-- " if idx == len(children) - 1 else "|-- "
            suffix = "/" if child.is_dir() else ""
            lines.append(prefix + connector + child.name + suffix)
            count += 1
            if child.is_dir() and depth < max_depth:
                next_prefix = prefix + ("    " if idx == len(children) - 1 else "|   ")
                walk(child, next_prefix, depth + 1)

    walk(root, "", 1)
    if count >= max_entries:
        lines.append("... truncated ...")
    return lines


def detect_stacks(root: Path, files: list[Path]) -> list[str]:
    names = {rel(p, root) for p in files}
    basenames = {p.name for p in files}
    stacks: list[str] = []
    if {"pyproject.toml", "setup.py", "requirements.txt", "environment.yml"} & basenames or any(
        p.suffix == ".py" for p in files
    ):
        stacks.append("Python")
    if "package.json" in basenames:
        stacks.append("Node/JavaScript")
    if "tsconfig.json" in basenames or any(p.suffix in {".ts", ".tsx"} for p in files):
        stacks.append("TypeScript")
    if "go.mod" in basenames:
        stacks.append("Go")
    if "Cargo.toml" in basenames:
        stacks.append("Rust")
    if {"pom.xml", "build.gradle", "settings.gradle"} & basenames:
        stacks.append("Java/JVM")
    if "composer.json" in basenames:
        stacks.append("PHP")
    if any(name.endswith(".sln") or name.endswith(".csproj") for name in names):
        stacks.append(".NET")
    if any(part in names for part in {"train.py", "train_generic.py"}) or any(
        top in names or top + "/" in names for top in ("experiments", "notebooks", "configs")
    ):
        stacks.append("Research/ML")
    return list(dict.fromkeys(stacks)) or ["unknown"]


def collect_paths(root: Path, files: list[Path]) -> tuple[list[str], list[str], list[str], list[str], list[str]]:
    docs: list[str] = []
    configs: list[str] = []
    envs: list[str] = []
    ci: list[str] = []
    agents: list[str] = []
    config_names = {
        "pyproject.toml",
        "setup.cfg",
        "tox.ini",
        "pytest.ini",
        "requirements.txt",
        "environment.yml",
        "package.json",
        "tsconfig.json",
        "vite.config.js",
        "vite.config.ts",
        "next.config.js",
        "go.mod",
        "Cargo.toml",
        "composer.json",
        "Makefile",
        "Dockerfile",
        "docker-compose.yml",
    }
    for path in files:
        r = rel(path, root)
        lower = r.lower()
        name = path.name
        if lower.startswith((".github/workflows/", ".gitlab-ci")) or name in {
            ".github",
            ".gitlab-ci.yml",
            "azure-pipelines.yml",
        }:
            ci.append(r)
        if name in config_names or name.endswith((".ini", ".toml", ".yaml", ".yml", ".json")) and (
            "config" in lower or lower.startswith(("configs/", "config/"))
        ):
            configs.append(r)
        if name.startswith(".env"):
            envs.append(r)
        if name.lower().startswith(("readme", "contributing", "security", "license", "changelog")) or lower.startswith(
            ("docs/", "doc/")
        ):
            docs.append(r)
        if name in {"AGENTS.md", "CLAUDE.md", "GEMINI.md"} or lower.endswith(
            ("/copilot-instructions.md", "/agent.md", "/agents.md")
        ):
            agents.append(r)
    return sorted(docs), sorted(configs), sorted(envs), sorted(ci), sorted(agents)


def collect_entry_points(root: Path, files: list[Path]) -> list[str]:
    candidates: list[str] = []
    names = {rel(p, root): p for p in files}
    for preferred in [
        "main.py",
        "app.py",
        "train.py",
        "train_generic.py",
        "server.py",
        "src/main.py",
        "src/index.ts",
        "src/index.js",
        "index.ts",
        "index.js",
        "main.go",
        "cmd",
    ]:
        if preferred in names or (root / preferred).exists():
            candidates.append(preferred)
    for path in files:
        r = rel(path, root)
        if r.startswith(("scripts/", "automation/")) and path.suffix in {".py", ".sh", ".ps1", ".js", ".ts"}:
            candidates.append(r)
    return sorted(dict.fromkeys(candidates))[:40]


def collect_tests(root: Path, files: list[Path]) -> list[str]:
    tests: set[str] = set()
    for path in files:
        r = rel(path, root)
        parts = r.split("/")
        if parts[0] in {"tests", "test", "__tests__", "spec"}:
            tests.add(parts[0] + ("/" if path.parent.name != parts[0] else ""))
        if path.name.startswith("test_") or path.name.endswith(("_test.py", ".test.ts", ".spec.ts", "_test.go")):
            tests.add(r)
    return sorted(tests)[:40]


def collect_output_dirs(root: Path) -> list[str]:
    found = []
    for child in sorted(root.iterdir(), key=lambda p: p.name.lower()):
        if child.is_dir() and child.name.lower() in OUTPUT_LIKE_DIRS:
            found.append(child.name + "/")
    return found


def collect_decisions(root: Path, files: list[Path]) -> list[str]:
    decisions = []
    for path in files:
        r = rel(path, root)
        lower = r.lower()
        if "adr" in lower or "decision" in lower or lower.startswith(("docs/adr", "docs/decisions")):
            decisions.append(r)
    return sorted(decisions)[:40]


def extract_commands(root: Path) -> list[tuple[str, str, str]]:
    commands: list[tuple[str, str, str]] = []
    package_json = root / "package.json"
    if package_json.exists():
        try:
            data = json.loads(safe_read_text(package_json, 20000))
            scripts = data.get("scripts", {})
            package_manager = "npm"
            if (root / "pnpm-lock.yaml").exists():
                package_manager = "pnpm"
            elif (root / "yarn.lock").exists():
                package_manager = "yarn"
            for name in sorted(scripts):
                commands.append((f"{package_manager} run {name}", "package.json", "fact"))
        except json.JSONDecodeError:
            pass
    makefile = root / "Makefile"
    if makefile.exists():
        text = safe_read_text(makefile, 20000)
        for line in text.splitlines():
            if line.startswith("\t") or ":" not in line:
                continue
            target = line.split(":", 1)[0].strip()
            if target and re.match(r"^[A-Za-z0-9_.-]+$", target) and not target.startswith("."):
                commands.append((f"make {target}", "Makefile", "fact"))
    if (root / "pyproject.toml").exists() or (root / "pytest.ini").exists() or (root / "tests").exists():
        commands.append(("python -m pytest", "Python project markers", "inference"))
    if (root / "requirements.txt").exists():
        commands.append(("python -m pip install -r requirements.txt", "requirements.txt", "inference"))
    if (root / "environment.yml").exists():
        commands.append(("conda env update -f environment.yml", "environment.yml", "inference"))
    if (root / "go.mod").exists():
        commands.extend([
            ("go test ./...", "go.mod", "inference"),
            ("go build ./...", "go.mod", "inference"),
        ])
    if (root / "Cargo.toml").exists():
        commands.extend([
            ("cargo test", "Cargo.toml", "inference"),
            ("cargo build", "Cargo.toml", "inference"),
        ])
    return list(dict.fromkeys(commands))[:80]


def analyze_project(root: Path) -> ProjectFacts:
    files = list(iter_files(root))
    project_name = root.name
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    top_dirs, top_files = top_level(root)
    docs, configs, envs, ci, agents = collect_paths(root, files)
    return ProjectFacts(
        root=root,
        project_name=project_name,
        generated_at=generated_at,
        git_branch=run_git(root, ["branch", "--show-current"]),
        git_remote=run_git(root, ["remote", "get-url", "origin"]),
        readme_summary=first_readme_summary(root),
        detected_stacks=detect_stacks(root, files),
        top_dirs=top_dirs,
        top_files=top_files,
        tree_lines=small_tree(root),
        docs=docs,
        existing_agent_files=agents,
        config_files=configs,
        env_files=envs,
        ci_files=ci,
        entry_points=collect_entry_points(root, files),
        test_paths=collect_tests(root, files),
        output_dirs=collect_output_dirs(root),
        commands=extract_commands(root),
        decisions=collect_decisions(root, files),
    )


def bullet(items: list[str], empty: str = "- TODO(agent): fill after inspection.") -> str:
    if not items:
        return empty
    return "\n".join(f"- `{item}`" for item in items)


def command_table(commands: list[tuple[str, str, str]]) -> str:
    if not commands:
        return "| Command | Source | Status |\n|---|---|---|\n| TODO(agent): add verified commands | - | unknown |"
    rows = ["| Command | Source | Status |", "|---|---|---|"]
    for cmd, source, status in commands:
        rows.append(f"| `{cmd}` | `{source}` | {status} |")
    return "\n".join(rows)


def header(facts: ProjectFacts, title: str) -> str:
    return (
        f"# {title}\n\n"
        "<!-- Generated by project-agent-generator-skill. Edit after verifying project facts. -->\n\n"
        f"- Project root: `{facts.root}`\n"
        f"- Generated: {facts.generated_at}\n"
        "- Rule: facts are recorded from repository files; uncertain items are marked `TODO(agent)` or `inference`.\n\n"
    )


def render_readme(f: ProjectFacts) -> str:
    return header(f, "Agent Context Index") + f"""This directory contains agent-facing context for `{f.project_name}`.

Recommended reading order:

1. `AGENTS.md`
2. `PROJECT_CONTEXT.md`
3. `ARCHITECTURE.md`
4. `CONFIG_SPEC.md`
5. `RUNBOOK.md`
6. `DECISIONS.md`

Files:

| File | Purpose |
|---|---|
| `AGENTS.md` | Operational rules and safety constraints for AI coding agents. |
| `PROJECT_CONTEXT.md` | Project purpose, stack, docs, and verified context. |
| `ARCHITECTURE.md` | Directory map, module boundaries, entry points, and generated-output areas. |
| `CONFIG_SPEC.md` | Config files, environment surfaces, and editable settings. |
| `RUNBOOK.md` | Setup, run, test, build, and approval-gated commands. |
| `DECISIONS.md` | Durable decisions, ADRs, and unresolved project questions. |

Do not treat these files as a transcript. They should summarize stable project facts and owner-confirmed rules only.
"""


def render_agents(f: ProjectFacts) -> str:
    return header(f, "Agent Instructions") + f"""## Scope

These instructions apply to the project rooted at:

```text
{f.root}
```

## Detected Stack

{bullet(f.detected_stacks)}

## Repository

- Git branch: `{f.git_branch or "unknown"}`
- Git remote: `{f.git_remote or "unknown"}`

## Operating Rules

- Read `.agents/README.md` first when joining a fresh session.
- Prefer repository files over chat memory.
- Do not invent project goals, commands, APIs, metrics, or config semantics.
- Before changing generated outputs or large experiment/data folders, ask the user.
- Keep edits scoped to the requested task.
- Verify commands before documenting them as facts.

## Likely Generated Or Large Output Directories

{bullet(f.output_dirs, "- None detected at top level.")}

## Commands

{command_table(f.commands)}

## Existing Agent/AI Instruction Files

{bullet(f.existing_agent_files, "- None detected.")}

## TODO For Project Owner

- TODO(agent): add project-specific do-not-touch paths if any.
- TODO(agent): add required Python/Node/Go/etc. runtime versions if not already documented.
- TODO(agent): add approval rules for long-running, destructive, network, deployment, or training commands.
"""


def render_context(f: ProjectFacts) -> str:
    summary = f.readme_summary or "TODO(agent): summarize project purpose after reading project docs or asking the owner."
    return header(f, "Project Context") + f"""## Project Summary

{summary}

## Detected Stack

{bullet(f.detected_stacks)}

## Important Documentation

{bullet(f.docs, "- No documentation files detected.")}

## Entry Points

{bullet(f.entry_points, "- TODO(agent): identify entry points.")}

## Current Unknowns

- TODO(agent): confirm the main user-facing goal of this project.
- TODO(agent): confirm what outputs are source-of-truth versus generated artifacts.
- TODO(agent): confirm any domain-specific naming rules.
"""


def render_architecture(f: ProjectFacts) -> str:
    tree = "\n".join(f.tree_lines)
    return header(f, "Architecture") + f"""## Top-Level Map

```text
{tree}
```

## Top-Level Directories

{bullet(f.top_dirs, "- No top-level directories detected.")}

## Top-Level Files

{bullet(f.top_files, "- No top-level files detected.")}

## Entry Points

{bullet(f.entry_points, "- TODO(agent): identify entry points.")}

## Tests

{bullet(f.test_paths, "- No test paths detected.")}

## Generated / Output Areas

{bullet(f.output_dirs, "- None detected at top level.")}

## Boundary Notes

- TODO(agent): document module ownership and import boundaries after inspecting source code.
- TODO(agent): document which directories are safe to regenerate.
"""


def render_config(f: ProjectFacts) -> str:
    return header(f, "Config Spec") + f"""## Config Files

{bullet(f.config_files, "- No config files detected.")}

## Environment Files

Only filenames are listed. Do not copy secret values.

{bullet(f.env_files, "- No environment files detected.")}

## CI / Automation Files

{bullet(f.ci_files, "- No CI files detected.")}

## Command Sources

{command_table(f.commands)}

## Config Semantics To Confirm

- TODO(agent): identify user-editable config fields and their valid values.
- TODO(agent): document required environment variables without exposing secrets.
- TODO(agent): mark generated config files separately from source config files.
"""


def render_runbook(f: ProjectFacts) -> str:
    return header(f, "Runbook") + f"""## Setup / Run / Test Commands

{command_table(f.commands)}

## Suggested Verification Flow

1. Read `AGENTS.md` and this runbook.
2. Check the working tree before editing.
3. Run the smallest relevant syntax or unit-test command first.
4. Escalate to full builds, training, migrations, deployment, or network calls only with user approval.

## Long-Running Or Risky Commands

- TODO(agent): list training, deployment, database migration, destructive cleanup, or expensive commands.

## Troubleshooting

- If a command fails, record the exact command and source file that suggested it.
- If a command was inferred, verify it before treating it as part of the official workflow.
"""


def render_decisions(f: ProjectFacts) -> str:
    return header(f, "Decisions") + f"""## Existing Decision Records

{bullet(f.decisions, "- No ADR/decision files detected.")}

## Repository-Implied Decisions

- Detected stack: {", ".join(f.detected_stacks)}
- TODO(agent): add owner-confirmed architecture, naming, data, or workflow decisions.

## Open Questions

- TODO(agent): what files or generated outputs should never be overwritten?
- TODO(agent): what commands are required before a change is considered complete?
- TODO(agent): what architectural constraints should future agents preserve?
"""


RENDERERS = {
    "README.md": render_readme,
    "AGENTS.md": render_agents,
    "PROJECT_CONTEXT.md": render_context,
    "ARCHITECTURE.md": render_architecture,
    "CONFIG_SPEC.md": render_config,
    "RUNBOOK.md": render_runbook,
    "DECISIONS.md": render_decisions,
}


def write_outputs(facts: ProjectFacts, out_dir: Path, force: bool, dry_run: bool) -> list[Path]:
    outputs: list[Path] = []
    if dry_run:
        return [out_dir / name for name in RENDERERS]
    out_dir.mkdir(parents=True, exist_ok=True)
    for name, renderer in RENDERERS.items():
        path = out_dir / name
        if path.exists() and not force:
            raise FileExistsError(f"{path} exists; pass --force to overwrite")
        with path.open("w", encoding="utf-8", newline="\n") as fh:
            fh.write(renderer(facts))
        outputs.append(path)
    return outputs


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", help="Project root to inspect")
    parser.add_argument("--out-dir", default=".agents", help="Output directory name/path, default: .agents")
    parser.add_argument("--force", action="store_true", help="Overwrite existing generated files")
    parser.add_argument("--dry-run", action="store_true", help="Show target files without writing")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    root = Path(args.project).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        print(f"error: project root does not exist or is not a directory: {root}", file=sys.stderr)
        return 2
    out_dir = Path(args.out_dir)
    if not out_dir.is_absolute():
        out_dir = root / out_dir
    facts = analyze_project(root)
    try:
        outputs = write_outputs(facts, out_dir, args.force, args.dry_run)
    except FileExistsError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 3
    action = "Would write" if args.dry_run else "Wrote"
    print(f"{action} {len(outputs)} files:")
    for path in outputs:
        print(f"- {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

