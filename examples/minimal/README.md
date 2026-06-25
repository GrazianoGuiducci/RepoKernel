# Minimal RepoKernel Example

This is a synthetic example showing the smallest useful continuity layer.

It contains:

```text
AGENTS.md
CURRENT_STATE.md
process/FIRST_PACKET.md
seed-spec.json
source-manifest.json
```

The point is not bureaucracy. The point is that the next AI session can see the active state, boundary and first safe action.

Use the JSON fixtures with the Phase 1 CLI:

```bash
PYTHONPATH=src python -m repokernel.cli validate-spec --kind seed-spec --input examples/minimal/seed-spec.json
PYTHONPATH=src python -m repokernel.cli validate-bundle --source-manifest examples/minimal/source-manifest.json --project-model examples/minimal/project-model.json --seed-spec examples/minimal/seed-spec.json
PYTHONPATH=src python -m repokernel.cli plan --seed-spec examples/minimal/seed-spec.json --source-manifest examples/minimal/source-manifest.json --project-model examples/minimal/project-model.json > plan.json
PYTHONPATH=src python -m repokernel.cli guides --seed-spec examples/minimal/seed-spec.json --source-manifest examples/minimal/source-manifest.json
```

To inspect proposed files without touching a target repository, save a plan and
stage it into a separate empty review directory:

```bash
PYTHONPATH=src python -m repokernel.cli stage --plan plan.json --output-dir ./repokernel-staging
```
