# Quickstart

## Choose The Mode

```text
new_repository
existing_repository_retrofit
A1 observe-and-propose
```

Use A1 when you are looking at another person's repository or a project where
you do not yet have write authority.

## Prepare Contracts

RepoKernel uses three linked inputs:

```text
SourceManifest -> ProjectModel -> SeedSpec
```

For a first run, use the included minimal fixtures instead of hand-writing a
partial SeedSpec:

```text
examples/minimal/source-manifest.json
examples/minimal/project-model.json
examples/minimal/seed-spec.json
```

A valid SeedSpec now includes source/model hashes, review metadata, compiler
compatibility and a file plan policy. A partial object like the older examples
below is not enough:

```json
{
  "schema": "repokernel.seed-spec.v1",
  "version": "repokernel.seed-spec.v1",
  "seed_id": "demo-seed",
  "source_manifest_hash": "<sha256 of canonical SourceManifest>",
  "project_model_hash": "<sha256 of canonical ProjectModel>",
  "canonical_namespace": ".repokernel",
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
  "authority_mode": "propose",
  "review": {
    "status": "accepted",
    "accepted_by_role": "operator",
    "accepted_at": "2026-06-26",
    "review_cycle": "local-review"
  },
  "compiler_compatibility": {
    "package_version": "0.3.0.dev0"
  },
  "file_plan_policy": "stage_only",
  "validation_plan": ["validate-spec", "validate-bundle", "plan", "stage"]
}
```

## Plan Before Writing

Phase 1 core creates a deterministic `GenerationPlan`. Existing repository
files are not overwritten silently.

For existing repositories, run `inspect` first and pass the same-run snapshot
to `plan`:

```bash
PYTHONPATH=src python -m repokernel.cli inspect --path /path/to/project > inspect.json
PYTHONPATH=src python -m repokernel.cli plan \
  --seed-spec seed.json \
  --source-manifest sources.json \
  --project-model project-model.json \
  --target-snapshot inspect.json > plan.json
```

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

Phase 1 is currently an experimental no-apply diagnostic path. Treat generated
plans as proposals, not as installer output.

## CLI

Run from the RepoKernel checkout:

```bash
PYTHONPATH=src python -m repokernel.cli validate-spec --kind seed-spec --input seed.json
PYTHONPATH=src python -m repokernel.cli inspect --path /path/to/project
PYTHONPATH=src python -m repokernel.cli validate-bundle --source-manifest sources.json --project-model project-model.json --seed-spec seed.json
PYTHONPATH=src python -m repokernel.cli plan --seed-spec seed.json --source-manifest sources.json --project-model project-model.json > plan.json
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
PYTHONPATH=src python -m repokernel.cli validate-bundle --source-manifest examples/minimal/source-manifest.json --project-model examples/minimal/project-model.json --seed-spec examples/minimal/seed-spec.json
PYTHONPATH=src python -m repokernel.cli plan --seed-spec examples/minimal/seed-spec.json --source-manifest examples/minimal/source-manifest.json --project-model examples/minimal/project-model.json > plan.json
PYTHONPATH=src python -m repokernel.cli stage --plan plan.json --output-dir ./repokernel-staging
PYTHONPATH=src python -m repokernel.cli guides --seed-spec examples/minimal/seed-spec.json --source-manifest examples/minimal/source-manifest.json
```

This smoke test writes only `plan.json` and the explicit staging directory in
your checkout. It does not write to the target path named by the SeedSpec.

After staging, inspect `stage-report.json` or command output and confirm:

```text
target_writes_performed: []
boundary: staging_only_not_apply
```

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
