# Project Detection Notes

The generator uses conservative heuristics. Extend them only when a new marker is stable and easy to verify.

## Common Markers

| Stack | Markers |
|---|---|
| Python | `pyproject.toml`, `setup.py`, `requirements.txt`, `environment.yml`, `*.py` |
| Node/TypeScript | `package.json`, `pnpm-lock.yaml`, `yarn.lock`, `tsconfig.json`, `vite.config.*`, `next.config.*` |
| Go | `go.mod`, `go.sum`, `cmd/`, `internal/` |
| Rust | `Cargo.toml`, `Cargo.lock`, `src/main.rs`, `src/lib.rs` |
| Java/JVM | `pom.xml`, `build.gradle`, `settings.gradle` |
| PHP | `composer.json`, `artisan`, `symfony.lock` |
| .NET | `*.sln`, `*.csproj`, `Directory.Build.props` |
| Research/ML | `notebooks/`, `experiments/`, `configs/`, `data/`, `results/`, `figures/`, `train*.py` |

## Safety Heuristics

- Mark `data/`, `datasets/`, `results/`, `outputs/`, `experiments/`, `checkpoints/`, and `runs/` as likely generated or large-output directories unless README says otherwise.
- Never open or copy `.env` values. Record the filename only.
- Treat commands from package/build files as facts; treat commands inferred from filenames as inferences.
- If a command may train models, migrate data, deploy, delete, or overwrite results, put it behind an approval note in `RUNBOOK.md`.

