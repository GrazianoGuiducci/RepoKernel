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
validate-bundle
inspect
plan
stage
guides
audit
verify-dist
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
target-snapshot
```

## inspect

Inspect a repository without writing:

```bash
PYTHONPATH=src python -m repokernel.cli inspect --path /path/to/project
```

This reports whether the path has root adapters, legacy project-kernel files or
the canonical `.repokernel/` control plane. It also emits a read-only
TargetSnapshot with path kinds, content hashes for eligible text files and
warnings for symlinks or path collisions.

Snapshotting applies the default exclusion policy for repository metadata,
credential/environment files, private keys, virtualenvs, vendor trees and build
artifacts. Sensitive excluded paths are redacted in the report. Excluded
directory trees are summarized compactly under
`extensions.repokernel.excluded_summary` so local vendor folders do not dominate
review artifacts.

## plan

Build a deterministic `GenerationPlan` from a reviewed and linked bundle:

```bash
PYTHONPATH=src python -m repokernel.cli plan \
  --seed-spec seed.json \
  --source-manifest sources.json \
  --project-model project-model.json \
  > plan.json
```

Optional existing paths can be supplied as one relative path per line:

```bash
PYTHONPATH=src python -m repokernel.cli plan \
  --seed-spec seed.json \
  --source-manifest sources.json \
  --project-model project-model.json \
  --existing-paths-file paths.txt \
  > plan.json
```

For existing repository retrofit, provide a fresh TargetSnapshot:

```bash
PYTHONPATH=src python -m repokernel.cli inspect --path /path/to/project > inspect.json
PYTHONPATH=src python -m repokernel.cli plan \
  --seed-spec seed.json \
  --source-manifest sources.json \
  --project-model project-model.json \
  --target-snapshot inspect.json \
  > plan.json
```

The command validates the SourceManifest, ProjectModel, SeedSpec and supplied
TargetSnapshot before planning. It emits JSON to stdout and does not write
generated files.

## validate-bundle

Validate SourceManifest, ProjectModel and SeedSpec linkage:

```bash
PYTHONPATH=src python -m repokernel.cli validate-bundle \
  --source-manifest sources.json \
  --project-model project-model.json \
  --seed-spec seed.json
```

This recomputes canonical source/model hashes, checks SeedSpec linkage,
validates ProjectModel source references and checks compiler package
compatibility.

## stage

Render a `GenerationPlan` into an explicit empty staging directory:

```bash
PYTHONPATH=src python -m repokernel.cli stage --plan plan.json --output-dir ./repokernel-staging
```

This is for review only. It writes proposed files under the staging directory
and never writes to the target repository named by the plan. Blocked plans are
rejected explicitly.

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

## verify-dist

Verify a Reference Seed distribution by regenerating the expected files through
the compiler and comparing the normalized path set and content hashes:

```bash
PYTHONPATH=src python -m repokernel.cli verify-dist --seed-spec specs/reference/starter-l1.seed.json --dist-dir dist/reference/starter-l1
```

## Boundary

The CLI does not grant repository write authority, network use, deployment,
Seed promotion or runtime activation. Those require later reviewed gates.
