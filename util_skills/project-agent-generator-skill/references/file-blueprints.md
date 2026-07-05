# File Blueprints

Use these blueprints when reviewing or manually improving generated `.agents/` files.

## `README.md`

Purpose: index for future agents.

Must include:

- project root path;
- generated file list;
- recommended reading order;
- warning that files are agent context, not chat history.

## `AGENTS.md`

Purpose: stable operational rules for AI coding agents.

Must include:

- runtime/tooling constraints;
- safe editing rules;
- test/build expectations;
- generated output or data directories to avoid touching;
- project-specific naming or architecture rules;
- "do not fabricate" reminder for unknown project facts;
- credential safety rule: do not open, print, copy, summarize, upload, or modify suspected key/password/token/credential files.

## `PROJECT_CONTEXT.md`

Purpose: concise project background.

Must include:

- project name;
- detected stack;
- README-derived purpose when available;
- important docs and entry points;
- explicit TODOs for goals that cannot be verified from files.

## `ARCHITECTURE.md`

Purpose: code structure and boundaries.

Must include:

- top-level directory map;
- likely source/test/docs/config directories;
- entry points;
- package/module boundaries;
- generated/cache/vendor directories.

## `CONFIG_SPEC.md`

Purpose: configuration surfaces.

Must include:

- config files found;
- environment files found, without secrets;
- build/tool config files;
- user-editable config fields if detectable;
- TODOs for config semantics that require project owner input;
- explicit reminder that credential files must not be opened, printed, copied, summarized, uploaded, or modified.

## `RUNBOOK.md`

Purpose: commands a future agent should run or avoid.

Must include:

- setup/install commands;
- run/dev commands;
- test/lint/build commands;
- deployment or release commands only if verified;
- notes about long-running or destructive commands requiring approval;
- credential-file safety rule before any troubleshooting workflow.

## `DECISIONS.md`

Purpose: durable architecture/product decisions.

Must include:

- existing ADR/decision files found;
- decisions visible from repo structure;
- unresolved questions;
- dated additions only when the agent/user confirms the decision.

## Credential Safety

All generated agent files must preserve this rule:

- Do not open, print, copy, summarize, upload, or modify any suspected key, password, token, or credential file.
- Treat filenames or paths containing `.env`, `secret`, `credential`, `credentials`, `token`, `password`, `passwd`, `apikey`, `api_key`, `private_key`, `id_rsa`, `.pem`, `.p12`, `.pfx`, `cookie`, or `session` as sensitive unless the project owner explicitly says otherwise.
- Record at most the filename/path and state that contents were not inspected.
- Never add secret values to `.agents`, generated reports, README files, logs, or final responses.
