# RepoKernel Coder Guide

Phase 1 implementation lives in:

```text
src/repokernel/
schemas/
tests/unit/
```

Core modules:

```text
canonical.py
models.py
paths.py
planner.py
guide_model.py
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

Test commands:

```powershell
$env:PYTHONPATH="src"
python -m unittest discover -s tests/unit -v
python scripts/phase0_inventory.py
python scripts/audit_repokernel_project.py --path . --profile repokernel-source --json
git diff --check
```
