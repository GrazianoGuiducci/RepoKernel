# RepoKernel CLI Reference

The Phase 1 CLI is a read-only control surface for contracts and plans.

Run from the repository checkout:

```bash
PYTHONPATH=src python -m repokernel.cli <command>
```

After installation, the package exposes:

```bash
repokernel <command>
```

## Commands

```text
validate-spec
inspect
plan
stage
guides
audit
```

There is no `apply` command in Phase 1 P0.

## validate-spec

Validate a canonical JSON contract:

```bash
PYTHONPATH=src python -m repokernel.cli validate-spec --kind seed-spec --input seed.json
```

Supported kinds:

```text
activation-report
generation-plan
project-model
seed-spec
skill-registry
source-manifest
```

## inspect

Inspect a repository without writing:

```bash
PYTHONPATH=src python -m repokernel.cli inspect --path /path/to/project
```

This reports whether the path has root adapters, legacy project-kernel files or
the canonical `.repokernel/` control plane.

## plan

Build a deterministic `GenerationPlan` from a reviewed `SeedSpec`:

```bash
PYTHONPATH=src python -m repokernel.cli plan --seed-spec seed.json > plan.json
```

Optional existing paths can be supplied as one relative path per line:

```bash
PYTHONPATH=src python -m repokernel.cli plan --seed-spec seed.json --existing-paths-file paths.txt > plan.json
```

The command emits JSON to stdout. It does not write generated files.

## stage

Render a `GenerationPlan` into an explicit empty staging directory:

```bash
PYTHONPATH=src python -m repokernel.cli stage --plan plan.json --output-dir ./repokernel-staging
```

This is for review only. It writes proposed files under the staging directory
and never writes to the target repository named by the plan.

## guides

Project guide text from a `SeedSpec` and `SourceManifest`:

```bash
PYTHONPATH=src python -m repokernel.cli guides --seed-spec seed.json --source-manifest sources.json
```

Public guide output includes only sources marked `privacy: public` and
`used_for: ["public_guide"]`.

## audit

Run the package audit:

```bash
PYTHONPATH=src python -m repokernel.cli audit --path . --profile repokernel-source
```

The compatibility script calls the same package audit:

```bash
python scripts/audit_repokernel_project.py --path . --profile repokernel-source --json
```

## Boundary

The CLI does not grant repository write authority, network use, deployment,
Seed promotion or runtime activation. Those require later reviewed gates.
