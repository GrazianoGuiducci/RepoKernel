# Active Packet — Track A Readback Corrections

date: 2026-06-25
status: correction_implemented_pending_final_readback
review_cycle: RK-RVW-20260625-01
track_b_status: blocked

## Objective

```text
objective: close the remaining Track A contract, snapshot, planning, audit and reproducibility gaps before locking a version for the private pilot
```

## Authoritative Sources

```text
CURRENT_STATE.md
process/reviews/RK-RVW-20260625-01/CODEX_RETURN.md
process/reviews/RK-RVW-20260625-01/GPT_PRO_READBACK.md
packets/FOR_CODEX/TRACK_A_READBACK_CORRECTIONS_2026-06-25.md
docs/guides/evolution-versioning-and-review-loop.md
docs/compatibility-matrix.md
process/reviews/REVIEW_LEDGER.md
sources/bootstrap/SOURCE_ATLAS_v1.0.md
```

## Correction Scope

```text
complete schema/Python parity;
evidence-bearing ProjectModel;
SourceManifest/ProjectModel/SeedSpec bundle verification;
TargetSnapshot integrity and exclusion policy;
fully target-bound GenerationPlan;
compiler-regenerated Reference Seed;
canonical .repokernel project audit;
uniform CLI validation and provenance;
package/evidence cleanup.
```

## Boundary

```text
allowed after operator acceptance:
  RepoKernel core contracts, validators, snapshot, planner, Reference Seed,
  audit, CLI, tests, packaging, docs and review records.

blocked:
  denis-repokernel-pilot changes or execution;
  Track B;
  target apply or writes;
  network and credential use;
  runtime/L3;
  public tester request;
  Seed/THIA/Lab promotion;
  unrelated repository changes.
```

## First Safe Action

```text
first_safe_action: push the correction commit and request final GPT Pro Track A readback; Codex does not run the pilot before that decision
```

## Required Codex Return

```text
process/reviews/RK-RVW-20260625-01/CODEX_RETURN_CORRECTION.md

exact correction commit;
package version;
files changed;
contract fixture/parity summary;
commands and actual outputs;
clean-install evidence;
remaining blockers and deviations;
confirmation that Track B and the pilot were not executed;
request for final GPT Pro Track A readback.
```

## Acceptance Gate

```text
GPT Pro correction readback: accepted_for_private_pilot
operator version-lock decision
pilot execution SHA recorded
```

Only after all three may Track B start.

## Memory Delta

```text
preserve:
  accepted corrections;
  adversarial tests;
  versioned evidence;
  clarified contract and audit semantics;
  final Track A compatibility state.

do_not_preserve:
  raw reasoning;
  unverified local claims;
  staged proposal trees;
  pilot-specific or private relationship material.
```
