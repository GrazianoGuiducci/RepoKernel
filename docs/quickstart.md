# Quickstart

## Choose The Mode

```text
new_repository
existing_repository_retrofit
A1 observe-and-propose
```

Use A1 when you are looking at another person's repository or a project where
you do not yet have write authority.

## Prepare A SeedSpec

Minimal example:

```json
{
  "schema": "repokernel.seed-spec.v1",
  "seed_id": "demo-seed",
  "project": {
    "name": "Demo Project",
    "intent": "Preserve continuity",
    "product": "A project kernel"
  },
  "target": {
    "mode": "new_repository",
    "path": "DemoProject"
  },
  "readiness_level": "L1",
  "authority_mode": "propose"
}
```

## Plan Before Writing

Phase 1 core creates a deterministic `GenerationPlan`. Existing repository
files are not overwritten silently.

## Audit An Existing Repository

```bash
python scripts/audit_repokernel_project.py --path /path/to/repo
```

Read the missing layers and add only what improves reentry.

## Current Safe Flow

```text
prepare SeedSpec
validate contracts
create GenerationPlan
review proposed files and operations
optionally stage proposed files into a separate review directory
apply only after a later explicit apply gate exists
```

Phase 1 is currently P0-hardening. Treat generated plans as proposals, not as
installer output.

## CLI

Run from the RepoKernel checkout:

```bash
PYTHONPATH=src python -m repokernel.cli validate-spec --kind seed-spec --input seed.json
PYTHONPATH=src python -m repokernel.cli inspect --path /path/to/project
PYTHONPATH=src python -m repokernel.cli plan --seed-spec seed.json > plan.json
PYTHONPATH=src python -m repokernel.cli stage --plan plan.json --output-dir ./repokernel-staging
PYTHONPATH=src python -m repokernel.cli guides --seed-spec seed.json --source-manifest sources.json
PYTHONPATH=src python -m repokernel.cli audit --path . --profile repokernel-source
```

The CLI is read-only with respect to target repositories. It can emit JSON
plans, stage proposed files in a separate review directory and emit guide
content, but it does not apply generated files to the target repository.

For a first local smoke test, use the included minimal fixtures:

```bash
PYTHONPATH=src python -m repokernel.cli validate-spec --kind seed-spec --input examples/minimal/seed-spec.json
PYTHONPATH=src python -m repokernel.cli plan --seed-spec examples/minimal/seed-spec.json > plan.json
PYTHONPATH=src python -m repokernel.cli stage --plan plan.json --output-dir ./repokernel-staging
PYTHONPATH=src python -m repokernel.cli guides --seed-spec examples/minimal/seed-spec.json --source-manifest examples/minimal/source-manifest.json
```

This smoke test writes only `plan.json` and the explicit staging directory in
your checkout. It does not write to the target path named by the SeedSpec.

See `docs/guides/cli-reference.md` for command details and
`docs/guides/operational-procedure.md` for the full repo-intake procedure.

## Legacy Scaffold Scripts

The old scaffold scripts are compatibility prototypes, not the canonical Phase
1 installer path:

```text
scripts/scaffold_repokernel_project.py
scripts/scaffold_skill_repo.py
```

Use them only for internal comparison while the Phase 1 planner, schemas and
future CLI converge.
