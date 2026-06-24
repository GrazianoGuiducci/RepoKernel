# RepoKernel Coder Guide

Phase 1 implementation lives in:

```text
src/repokernel/
schemas/
tests/unit/
```

Core modules:

```text
audit.py
canonical.py
cli.py
guide_model.py
models.py
paths.py
planner.py
```

Rules:

```text
use Python standard library first
preserve deterministic output
do not write during compile or plan
never silently overwrite existing target files
keep unknown namespaced extensions
do not let extensions affect authority
keep guides explanatory, not authoritative
```

Generated Project Kernel files belong under `.repokernel/` unless the file is a
host adapter such as root `AGENTS.md` or a project-native file such as
`README.md`. Existing root authority must become `propose_update`, not
overwrite.

Public guide projections are deny-by-default: include a source only when it is
`privacy: public` and its `used_for` list contains `public_guide`.

CLI contract:

```text
validate-spec: validate one canonical JSON contract
inspect: inspect a repository without writing
plan: emit GenerationPlan JSON without writing
guides: emit guide JSON without writing target files
audit: run read-only RepoKernel audit
apply: intentionally absent in Phase 1 P0
```

Test commands:

```powershell
$env:PYTHONPATH="src"
python -m unittest discover -s tests/unit -v
python scripts/phase0_inventory.py
python scripts/audit_repokernel_project.py --path . --profile repokernel-source --json
$env:PYTHONPATH="src"
python -m repokernel.cli audit --path . --profile repokernel-source
git diff --check
```

## Feedback Hook

If you build installer or CLI flows, include a non-blocking feedback prompt
that points to `docs/feedback.md`.

The prompt must be optional and privacy-safe. Do not ask for tokens, logs,
private files, `.env` contents, client material or repository dumps.
