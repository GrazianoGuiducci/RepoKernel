# RepoKernel Current State

updated: 2026-06-25
status: dual core-and-pilot completion gate prepared; implementation pending operator acceptance
repository: GrazianoGuiducci/RepoKernel
visibility: public
license: MIT
branch: main

## Active Surface

```text
active_surface: complete Phase 1 core conformance and qualify one version-locked private no-write pilot
current_next: operator accepts RK-RVW-20260625-01, then Codex executes REPOKERNEL_CORE_AND_PILOT_COMPLETION_PACKET_2026-06-25.md
```

## Accepted Architecture

```text
RepoKernel Source / Compiler
  -> authorized sources and ProjectModel
  -> reviewed SeedSpec
  -> deterministic, target-bound GenerationPlan
  -> staging/review
  -> later separately authorized apply gate
  -> validated Project Kernel under .repokernel/
```

```text
Reference Seed = precompiled reproducible SeedSpec
Synthesized ProjectSeed = custom reviewed SeedSpec
Retrofit Overlay = existing-target application mode
Root/host files = adapters or existing authority
L0-L2 = first stable scope
L3 = contract only
```

Optional layers remain separate:

```text
repokernel-core
repokernel-cognition
repokernel-cycle
repokernel-runtime
```

Independent coordinates remain:

```text
readiness: L0-L3
autonomy: A0-A4
authority: none | read | propose | project_write | external_action
cognitive_depth: D0-D3
```

No coordinate implies another.

## Current Gate

Review cycle:

```text
RK-RVW-20260625-01
```

Authoritative packet:

```text
packets/FOR_CODEX/REPOKERNEL_CORE_AND_PILOT_COMPLETION_PACKET_2026-06-25.md
```

Independent review:

```text
process/reports/REPOKERNEL_FULL_SURFACE_AND_PILOT_REVIEW_2026-06-25.md
```

Versioning/review protocol:

```text
docs/guides/evolution-versioning-and-review-loop.md
docs/compatibility-matrix.md
process/reviews/REVIEW_LEDGER.md
```

Pilot:

```text
GrazianoGuiducci/denis-repokernel-pilot
run: RK-PILOT-20260625-01
mode: existing_repository_retrofit / A1 observe-and-propose
```

## Verified

```text
final compiler/SeedSpec architecture accepted;
.repokernernel canonical control plane accepted;
Phase 1 package and console entry point exist;
CLI commands exist: validate-spec, inspect, plan, stage, guides, audit;
staging is separate from target apply;
planner emits .repokernel-oriented proposal files;
public source labels use deny-by-default filtering;
18 repository-contained local unit tests reported passing;
minimal validate -> plan -> stage -> guides flow reported passing;
local synthetic A1 no-write proof exists;
private pilot repository exists with proposal-first policy;
full-surface review and dual completion packet committed;
versioning protocol, compatibility matrix and review ledger committed;
pilot protocol and version-lock template committed.
```

## Not Yet Verified

```text
Draft 2020-12 schema execution and Python-validator parity;
review.status and source/model hashes required by SeedSpec;
content-hashed TargetSnapshot and stale-plan protection;
content-aware leave_unchanged/propose_update/conflict planning;
canonical .repokernel project audit profile;
audit evidence independent of self-attested Markdown phrases;
clean-environment wheel/sdist and installed CLI proof;
hosted CI tied to a commit;
Reference Seed byte-for-byte reproducibility;
version-locked private pilot execution;
independent pilot evaluation;
trusted collaborator or public experimental readiness;
apply transaction, runtime, Seed promotion and external automation.
```

## Boundary

```text
can_change:
  - RepoKernel schemas, validators, planner, inspect/snapshot, audit, CLI, tests,
    package resources, guides, governance and versioning records;
  - private pilot technical protocol and sanitized test evidence.

needs_confirmation:
  - execute RK-RVW-20260625-01 implementation;
  - run the private pilot after core conformance;
  - any external repository observation or write;
  - public tester request;
  - apply command, runtime/L3, Seed promotion or downstream mutation.

must_not_touch:
  - credentials and .env;
  - private relationship/contact material;
  - Denis-owned external repositories;
  - unrelated repositories;
  - target project files before a later reviewed apply gate.
```

## Separation Of Duties

```text
operator: intent, sources, authority and final acceptance
GPT Pro: independent review and readback
Codex: accepted implementation and evidence
independent evaluator: pilot/result evaluation
```

The same unreviewed process may not define intent, implement, evaluate and
promote its own result.

## First Safe Action

```text
1. Operator accepts the dual completion packet.
2. Codex runs Track A core conformance.
3. GPT Pro performs readback on the exact Codex commit.
4. Operator accepts the execution version.
5. Codex runs Track B against the private pilot with zero target writes.
6. Independent evaluation and operator decision close the cycle.
```

## Residue Not To Follow

```text
legacy scaffold scripts as the primary product path;
self-attested L2 readiness;
hand-edited generated distributions;
branch names used as version locks;
pilot evidence without source revision and target hash;
person-specific logic entering neutral core;
automatic apply, runtime, network or Seed promotion;
public readiness claims before dual conformance passes.
```
