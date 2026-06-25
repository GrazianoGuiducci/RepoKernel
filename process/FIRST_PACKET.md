# Active Packet — Core And Pilot Completion

date: 2026-06-25
status: accepted_for_codex_track_a_implemented_pending_readback
review_cycle: RK-RVW-20260625-01

## Objective

```text
objective: complete Phase 1 core conformance and qualify one version-locked private no-write pilot without starting Phase 2, apply, runtime or Seed promotion
```

## Authoritative Sources

```text
CURRENT_STATE.md
process/reports/REPOKERNEL_FULL_SURFACE_AND_PILOT_REVIEW_2026-06-25.md
packets/FOR_CODEX/REPOKERNEL_CORE_AND_PILOT_COMPLETION_PACKET_2026-06-25.md
docs/guides/evolution-versioning-and-review-loop.md
docs/compatibility-matrix.md
process/reviews/REVIEW_LEDGER.md
sources/bootstrap/SOURCE_ATLAS_v1.0.md
```

Pilot sources:

```text
GrazianoGuiducci/denis-repokernel-pilot
.repokernel/review/REPOKERNEL_VERSION_LOCK.md
docs/REPOKERNEL_PRODUCT_TEST_PROTOCOL.md
packets/FOR_CODEX/DENIS_PILOT_TEST_EXECUTION_PACKET_2026-06-25.md
```

## Scope

```text
Track A:
  schema-validator parity;
  reviewed/version-bound SeedSpec;
  TargetSnapshot and content-aware planning;
  opaque extension policy;
  disclosure profiles;
  canonical audit;
  clean package/CLI proof;
  Reference Seed reproducibility.

Track B:
  pilot version lock;
  read-only inspect;
  accepted pilot SeedSpec;
  target-bound plan;
  external staging;
  before/after tree equality;
  independent evaluation;
  operator decision.
```

## Boundary

```text
allowed after operator acceptance:
  RepoKernel core/docs/tests/governance;
  private pilot technical protocol and sanitized test-run evidence.

blocked:
  apply to target;
  external repository writes;
  network automation;
  credentials or private relationship context;
  public tester request;
  runtime/L3;
  Seed/THIA/Lab promotion;
  downstream repository mutation.
```

## First Safe Action

```text
first_safe_action: push Track A core conformance and return exact commit/test evidence; do not execute Track B before GPT Pro readback and operator decision
```

## Required Codex Return

```text
commits in both repositories;
files changed;
version lock;
commands and actual outputs;
core conformance report;
pilot conformance report;
remaining blockers;
deviations;
operator decisions required.
```

## Memory Delta

```text
preserve:
  accepted review dispositions;
  versioned evidence;
  durable contract and safety rules;
  pilot findings transferable to neutral core;
  compatibility and readiness changes.

do_not_preserve:
  private contact context;
  temporary internal reasoning;
  staged target proposals after review;
  obsolete Codex/GPT Pro packets after cycle closure.
```
