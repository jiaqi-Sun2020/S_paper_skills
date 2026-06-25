---
name: project-agent-generator-skill
description: Generate or update a project-local .agents or .agent context folder for unfamiliar codebases, including AGENTS.md, PROJECT_CONTEXT.md, ARCHITECTURE.md, CONFIG_SPEC.md, RUNBOOK.md, DECISIONS.md, and README.md. Use when Codex is asked to onboard an AI agent to a project, preserve project architecture for future sessions, create agent context files, document an unfamiliar repository for AI coding agents, or refresh project handoff documentation.
---

# Project Agent Generator

Create a project-local agent context bundle that lets future Codex/AI-agent sessions resume work from repository facts instead of chat history.

Default output:

```text
.agents/
|-- AGENTS.md
|-- PROJECT_CONTEXT.md
|-- ARCHITECTURE.md
|-- CONFIG_SPEC.md
|-- RUNBOOK.md
|-- DECISIONS.md
`-- README.md
```

Use `--out-dir .agent` only when the user explicitly asks for singular `.agent`.

## Workflow

1. Inspect the target project before generating.
   - Read root README, existing AGENTS/CLAUDE/GEMINI/Copilot instruction files, package/build configs, CI files, and obvious source directories.
   - Do not infer project goals from chat history unless the user explicitly asks to include them.
   - Treat generated files as handoff documentation for agents, not human marketing docs.

2. Run the generator when a first pass is enough.

```powershell
python path\to\project-agent-generator-skill\scripts\generate_project_agents.py D:\path\to\project
```

Common options:

```powershell
python path\to\project-agent-generator-skill\scripts\generate_project_agents.py D:\path\to\project --out-dir .agents --force
python path\to\project-agent-generator-skill\scripts\generate_project_agents.py D:\path\to\project --out-dir .agent --force
python path\to\project-agent-generator-skill\scripts\generate_project_agents.py D:\path\to\project --dry-run
```

3. Read and edit the generated files.
   - Replace `TODO(agent)` markers only with verified information or user-confirmed intent.
   - Keep instructions short, operational, and repository-specific.
   - Prefer pointers to source files over duplicating long explanations.

4. Verify before final response.
   - Confirm every referenced command/path exists or mark it as inferred.
   - Run lightweight syntax/test commands only when safe.
   - Report generated files and any TODOs left for the user.

## Generation Rules

- Use structured sections and tables where they make scanning easier.
- Never fabricate commands, architecture, configs, or decisions.
- Separate facts from inferences.
- Keep long-lived project rules in `AGENTS.md`.
- Keep current project purpose and user-facing context in `PROJECT_CONTEXT.md`.
- Keep module boundaries and file map in `ARCHITECTURE.md`.
- Keep config surfaces, environment variables, and schema notes in `CONFIG_SPEC.md`.
- Keep setup, run, test, build, and deploy commands in `RUNBOOK.md`.
- Keep durable design choices and unresolved questions in `DECISIONS.md`.
- Keep `.agents/README.md` as the index and reading order.

## Reference Routing

- Read `references/file-blueprints.md` when manually revising the seven generated files.
- Read `references/project-detection.md` when adapting the generator for a project type it does not recognize.
- Use `scripts/generate_project_agents.py` for deterministic first-pass generation.

