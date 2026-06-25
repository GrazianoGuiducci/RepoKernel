# RepoKernel Current State

updated: 2026-06-25
status: Track A readback corrections pushed; final GPT Pro/operator readback pending; former private pilot fixture frozen
repository: GrazianoGuiducci/RepoKernel
visibility: public
license: MIT
branch: main

## Active Surface

```text
active_surface: close the remaining Track A conformance gaps identified by GPT Pro readback
current_next: wait for final GPT Pro Track A readback on pushed correction commit; do not reactivate the former private pilot fixture
first_safe_action: keep Track B blocked and keep denis-repokernel-pilot out of active context
```

## Accepted Architecture

```text
RepoKernel Source / Compiler
  -> authorized SourceManifest and evidence-bearing ProjectModel
  -> reviewed and input-bound SeedSpec
  -> validated TargetSnapshot
  -> deterministic target-bound GenerationPlan
  -> external staging and review
  -> later separately authorized apply gate
  -> validated Project Kernel under .repokernel/
```

```text
Reference Seed = compiler-regenerated distribution
Synthesized ProjectSeed = custom reviewed and input-bound SeedSpec
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

Track A implementation:

```text
db6a761216d914530a8ee6c53956a5106434c535
pointer: e42064fc3a98d05a18a0703ba5c18792a7673432
```

GPT Pro readback:

```text
process/reviews/RK-RVW-20260625-01/GPT_PRO_READBACK.md
result: pass_with_required_corrections
```

Correction packet:

```text
packets/FOR_CODEX/TRACK_A_READBACK_CORRECTIONS_2026-06-25.md
status: accepted and implemented locally; final readback pending
```

Former Private Pilot Fixture:

```text
GrazianoGuiducci/denis-repokernel-pilot
run: RK-PILOT-20260625-01
status: frozen; not an active context; not a Denis/person context
boundary: do not read, pull, execute, mutate, stage against, or cite as active
unless the operator explicitly reauthorizes a neutral technical fixture later.
```

## Verified

```text
final compiler/SeedSpec architecture accepted;
.repokernel canonical control plane accepted;
Phase 1 package and console entry point exist;
CLI commands exist: validate-spec, validate-bundle, inspect, plan, stage, guides, audit, verify-dist;
staging remains separate from target apply;
planner emits .repokernel-oriented proposals;
public guide project fields and source labels are deny-by-default;
SeedSpec requires accepted review metadata and source/model hash fields;
basic TargetSnapshot and content-aware leave_unchanged behavior exist;
unknown namespaced extensions remain opaque to core planning;
32 repository-contained local unit tests reported passing by Codex;
clean-environment local wheel/CLI proof reported by Codex;
Track B was correctly not executed;
static GPT Pro readback of pushed Track A files completed.
complete schema/Python parity across every contract;
evidence-bearing ProjectModel with per-assertion source references;
actual SourceManifest/ProjectModel hash linkage to SeedSpec;
TargetSnapshot validation, integrity recomputation and safe exclusion policy;
plan ID fully bound to compiler, SeedSpec, target and snapshot;
canonical project-kernel audit without legacy root dependencies;
source ready status dependent on real contract/planner conformance;
Reference Seed compiler regeneration and extra-file detection;
uniform CLI validation and provenance;
local 45-test correction suite passing;
clean-environment local wheel/CLI correction proof passing;
license SPDX string replacing deprecated TOML table;
```

## Not Yet Verified Or Not Yet Conformant

```text
independent re-execution of the 45-test correction suite in GPT Pro environment;
hosted CI tied to a commit;
replacement neutral pilot or fixture decision;
version-locked pilot execution if explicitly reauthorized later;
independent pilot evaluation;
trusted collaborator or public experimental readiness;
apply transaction, runtime, Seed promotion and external automation.
```

## Boundary

```text
can_change after operator acceptance:
  - RepoKernel contracts, validators, bundle validation, snapshot, planner,
    Reference Seed generation, audit, CLI, tests, packaging and governance.

needs_confirmation:
  - execute the correction packet;
  - choose any future neutral pilot/fixture after final readback;
  - any external repository observation or write;
  - public tester request;
  - apply command, runtime/L3, Seed promotion or downstream mutation.

must_not_touch:
  - denis-repokernel-pilot as active context or default Track B target;
  - credentials, environment files and private relationship/contact material;
  - person/contact-specific repositories or context;
  - unrelated repositories;
  - target project files before a later reviewed apply gate.
```

## Separation Of Duties

```text
operator: intent, scope, dependency decision and final acceptance
GPT Pro: independent review and readback
Codex: accepted implementation and evidence
independent evaluator: later pilot/result evaluation
```

Codex does not independently close Track A or authorize Track B.

## First Safe Action

```text
1. GPT Pro performs final Track A readback on the pushed correction commit.
2. Operator decides whether Track A is accepted.
3. If a pilot is still useful, operator selects a neutral fixture explicitly.
4. Codex keeps denis-repokernel-pilot frozen unless separately reauthorized.
```

## Residue Not To Follow

```text
calling manifest hash checking Reference Seed reproducibility;
using a supplied snapshot without integrity verification;
root legacy paths inside canonical project-kernel audit;
self-attested L2 readiness;
branch names used as evidence version locks;
using denis-repokernel-pilot as active context or as a Denis/person context;
pilot execution against an unaccepted correction state;
automatic apply, runtime, network or Seed promotion;
public readiness claims before core and pilot conformance pass.
```
