# RepoKernel

RepoKernel is a developing host-neutral compiler for reviewable Project Kernels.

It is being built to turn authorized project intent and sources into a validated
`SeedSpec`, a deterministic `GenerationPlan` and a project-local control plane
under `.repokernel/` without silently overwriting target repositories.

Current status: `0.3.0.dev0`, experimental diagnostic compiler, no apply
command.

In practical terms, RepoKernel is a generator for AI-readable project
continuity structures. It helps new or existing projects preserve current
state, source lineage, process packets, rules, skills, evidence, memory deltas
and reentry points so that future AI-assisted work can continue from reviewed
project memory instead of scattered chat context.

The generated Project Kernel carries its own learning protocol. It tells the
target project how useful interactions may become reviewed memory deltas,
accepted rules or project-local skill candidates, while ordinary chat and
unverified speculation stay out of durable project memory.

## One Compiler, Two Distribution Forms

```text
RepoKernel Source / Compiler
        -> reviewed SeedSpec
        -> Project Kernel
```

A future user may consume RepoKernel through:

- **Reference Seed** — a reproducible precompiled SeedSpec;
- **Synthesized ProjectSeed** — a custom reviewed SeedSpec compiled from
  authorized project sources.

Reference Seeds and custom seeds must use the same contracts and planner.

## Application Modes

```text
new_repository
existing_repository_retrofit
A1 observe-and-propose
```

Retrofit is not a blind installation. Existing project files remain authoritative
until a reviewed plan says otherwise.

## Intended Pipeline

```text
authorized sources + project intent
-> SourceManifest
-> ProjectModel
-> reviewed SeedSpec
-> target-bound GenerationPlan
-> staging and human review
-> future separately authorized apply gate
-> ActivationReport
```

The current Phase 1 line implements the no-apply validation/planning path.
Apply and runtime remain deferred.

Public interpretation:

```text
safe to inspect as an experimental/research repository;
safe to run locally on non-sensitive targets for no-write diagnostics;
not production-ready;
not an installer;
not an autonomous repo modifier.
```

## Readiness Levels

| Level | Purpose | Current status |
| --- | --- | --- |
| **L0** | Reentry core | planned/generated surface |
| **L1** | Semantic kernel and sources | planned/generated surface |
| **L2** | Evidence, deltas and governed improvement | first stable scope, incomplete |
| **L3** | Optional runtime contract | contract only; executable runtime deferred |

Readiness does not imply autonomy or authority.

## Current Safe CLI Path

Use RepoKernel from a checkout or installed development environment:

```bash
repokernel validate-spec --kind seed-spec --input seed.json
repokernel validate-bundle --source-manifest sources.json --project-model project-model.json --seed-spec seed.json
repokernel inspect --path /path/to/project
repokernel plan --seed-spec seed.json --source-manifest sources.json --project-model project-model.json > plan.json
repokernel stage --plan plan.json --output-dir /empty/review-directory
repokernel guides --seed-spec seed.json --source-manifest sources.json
repokernel audit --path . --profile repokernel-source
```

Equivalent development command:

```bash
PYTHONPATH=src python -m repokernel.cli <command>
```

`stage` renders proposals into an explicit empty review directory. It is not an
apply operation and must not modify the target repository.

There is intentionally no `apply` command in the current line.

## Minimal Local Smoke Path

```bash
repokernel validate-spec --kind seed-spec --input examples/minimal/seed-spec.json
repokernel validate-bundle --source-manifest examples/minimal/source-manifest.json \
  --project-model examples/minimal/project-model.json \
  --seed-spec examples/minimal/seed-spec.json
repokernel plan --seed-spec examples/minimal/seed-spec.json \
  --source-manifest examples/minimal/source-manifest.json \
  --project-model examples/minimal/project-model.json > plan.json
repokernel stage --plan plan.json --output-dir ./repokernel-staging
repokernel guides --seed-spec examples/minimal/seed-spec.json \
  --source-manifest examples/minimal/source-manifest.json
```

Remove disposable local artifacts after review.

## How This Relates To Your Workflow

To try RepoKernel in your own workflow, start with the included minimal
fixtures, then replace them with your own authorized project inputs:

```text
your SourceManifest
your ProjectModel
your reviewed SeedSpec
your target snapshot
```

RepoKernel does not require any D-ND project, private fixture or specific
application. Use your own authorized inputs and keep staging outside the target
repository.

The intended value is not raw file generation. The value is giving a project a
reviewable learning structure: useful interactions can become deltas, accepted
corrections can become rules, repeated procedures can become project-local
skills, and the next session can reenter through explicit state and evidence.

This learning structure is staged into the project object itself. RepoKernel
documentation is not enough; the target project must receive the rule that
explains how to keep improving without accumulating noise.

Dirty or unclear file state is handled the same way: classify before cleanup.
Generated L2 Project Kernels include a `.repokernel/clarity/` ledger and local
rules for reviewing ambiguous files before delete, move, ignore or bulk
normalization actions are considered.

## Guides

- [Single-page overview](docs/overview.html)
- [User guide](docs/guides/user-guide.md)
- [Coder guide](docs/guides/coder-guide.md)
- [External assistant playbook](docs/guides/external-assistant-playbook.md)
- [Architecture guide](docs/guides/architecture.md)
- [CLI reference](docs/guides/cli-reference.md)
- [Operational procedure](docs/guides/operational-procedure.md)
- [Clarity cleanup cycle](docs/clarity-cleanup-cycle.md)
- [Meta-skill integration map](docs/meta-skill-integration-map.md)
- [Evolution, versioning and review loop](docs/guides/evolution-versioning-and-review-loop.md)
- [Compatibility matrix](docs/compatibility-matrix.md)
- [Pre-public checklist](docs/pre-public-checklist.md)

CI template:

```text
docs/ci/github-actions-ci.yml
```

Activating it under `.github/workflows/` requires a GitHub token or user action
with workflow scope.

## Current Status

RepoKernel has completed its first controlled no-write diagnostic loops. The
current result:

```text
mechanical no-write safety: passed
semantic retrofit usefulness: improved after A2 patch
apply/runtime/public production readiness: blocked
```

Current review and implementation sources:

- [Full surface and pilot review](process/reports/REPOKERNEL_FULL_SURFACE_AND_PILOT_REVIEW_2026-06-25.md)
- [Core and pilot completion packet](packets/FOR_CODEX/REPOKERNEL_CORE_AND_PILOT_COMPLETION_PACKET_2026-06-25.md)
- [Review ledger](process/reviews/REVIEW_LEDGER.md)

The diagnostic evidence is not proof of production installation in a
third-party repository.

## Evidence Rule

```text
files present != semantics valid
local tests passed != hosted CI
CI configured != CI has passed on your fork
structure ready != contract conformant
runtime present != authority granted
pilot procedure ready != pilot passed
```

Evidence is valid only for the package, source revision, contract versions and
target snapshot it records.

## Current Boundaries

Blocked until later reviewed gates:

```text
apply to target repositories;
automatic overwrite;
network or credential handling;
PR/issue creation;
public production claims;
Seed/THIA/Lab promotion;
executable L3 runtime;
autonomous project writes.
```

## Feedback

Privacy-safe feedback is described in [docs/feedback.md](docs/feedback.md).
Do not share credentials, private source documents, client material or full
repository dumps.

## What RepoKernel Is Not

RepoKernel is not unrestricted autonomous modification, a guarantee of correct
AI behavior or a replacement for project ownership and review.

## License

MIT. See [LICENSE](LICENSE).
