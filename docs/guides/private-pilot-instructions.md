# Private Pilot Instructions

Use this for one controlled technical reviewer before any broad public tester
request.

## Scope

RepoKernel Phase 1 P0 is a read-only planner and review surface.

The pilot may test:

```text
validate-spec
plan
stage
guides
audit
```

The pilot must not test:

```text
apply
automatic repository modification
production runtime behavior
Seed, THIA or Lab integration
confidential/client repositories without permission
```

## First Smoke Test

Run from the RepoKernel checkout:

```bash
PYTHONPATH=src python -m repokernel.cli validate-spec --kind seed-spec --input examples/minimal/seed-spec.json
PYTHONPATH=src python -m repokernel.cli validate-bundle --source-manifest examples/minimal/source-manifest.json --project-model examples/minimal/project-model.json --seed-spec examples/minimal/seed-spec.json
PYTHONPATH=src python -m repokernel.cli plan --seed-spec examples/minimal/seed-spec.json --source-manifest examples/minimal/source-manifest.json --project-model examples/minimal/project-model.json > plan.json
PYTHONPATH=src python -m repokernel.cli stage --plan plan.json --output-dir ./repokernel-staging
PYTHONPATH=src python -m repokernel.cli guides --seed-spec examples/minimal/seed-spec.json --source-manifest examples/minimal/source-manifest.json
```

Expected:

```text
SeedSpec is valid.
GenerationPlan is written to plan.json.
Proposed files are staged under ./repokernel-staging.
No files are written to the target path named by the SeedSpec.
```

## Optional Repository Observation

Only use a public or non-sensitive repository.

Before running:

```text
confirm repository owner;
confirm permission to inspect;
exclude secrets, logs, .env files and private source material;
use observe-and-propose only.
```

Run:

```bash
PYTHONPATH=src python -m repokernel.cli inspect --path /path/to/project
```

Do not write proposed files into the target repository.

## Feedback Requested

Use `docs/feedback.md`.

Most useful feedback:

```text
what command was unclear;
whether staging felt safe;
whether the proposed files were understandable;
whether the no-write boundary was obvious;
what example would make the next test easier.
```

Do not share:

```text
credentials
tokens
private logs
client material
.env files
full repository dumps
anything you do not have permission to disclose
```

## Stop Rule

Stop the pilot if:

```text
the target repository contains sensitive material;
the command appears to write outside the explicit staging directory;
the reviewer expects an installer or apply command;
the feedback would require exposing private project details.
```
