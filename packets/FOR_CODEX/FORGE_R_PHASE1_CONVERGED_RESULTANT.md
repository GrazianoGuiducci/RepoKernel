# Forge-R Phase 1 Converged Resultant

date: 2026-06-24
status: proposed_for_operator_acceptance
recursive_depth_used: D3
authority: convergence_packet_only

## Objective

Define the smallest Phase 1 implementation that turns RepoKernel from a
prototype scaffold into a safe, testable Project Kernel compiler without
collapsing future cognition, cycle, runtime, departmental or guide surfaces
into the first core.

## Source Anchors

```text
CURRENT_STATE.md
process/FIRST_PACKET.md
process/reports/phase0-validation-summary.md
process/reports/current-tree.json
process/reports/migration-classification.json
packets/FOR_CODEX/REPOKERNEL_FINAL_IMPLEMENTATION_PACKAGE_2026-06-23.md
packets/FOR_CODEX/POST_PHASE0_AUTOPOIETIC_CONVERGENCE_GATE.md
packets/FOR_CODEX/POST_PHASE0_SCHEMA_HORIZON_2026-06-23.md
docs/possibility-horizon.md
docs/recursive-distillation-plane.md
docs/autopoietic-cycle-gap-analysis.md
docs/departmental-autonomy-spectral-analysis.md
docs/internal-runtime-architecture.md
registry/skills.json
```

## Current Tension

RepoKernel must become useful for internal D-ND work and external users, but
two failure modes must be avoided:

```text
underbuild: a weak generator similar to earlier Lab generator attempts;
overbuild: an autonomous system, runtime or departmental machine before the
  core compiler and guide surfaces are stable.
```

## Accepted Invariants

```text
RepoKernel is a host-neutral Project Kernel compiler.
The generated Project Kernel belongs to the target project.
Generation and retrofit are distinct modes of one compiler.
L0-L2 are first stable scope.
L3 is contract-only.
Source documents are data unless explicitly authorized as instructions.
No silent overwrite.
No authority escalation through schemas, extensions, recursion, events or guides.
No self-approval: observation, proposal, execution, evaluation and promotion
  remain separable.
Unknown namespaced extensions round-trip without changing planning or authority.
Guides are applications/projections of canonical contracts, not duplicated canon.
```

## Verified Facts

```text
Phase 0 reports exist and classify every tracked file.
migration-classification unclassified_count is 0.
link-check broken_count is 0.
repokernel-source audit passes with ready true and readiness L2.
V03 and V04 packets are marked superseded.
context-surface placeholder was replaced.
registry evidence resolves.
```

## Assumptions And Unknowns

```text
assumption: Python standard library is sufficient for Phase 1 schemas, canonical
  serialization, planning and tests.
assumption: public external use should start from Direct Start, Synthesis,
  Retrofit and Observe-and-Propose guides before runtime or Seed promotion.
unknown: exact CLI names may change during implementation.
unknown: final package layout may need small adjustment after first tests.
unknown: external user friction will only be known after a generated fixture and
  one real repo observation.
```

## Branches Considered

```text
B1 Direct generator completion:
  implement compile/plan/apply immediately from current scripts.

B2 Schema-first core:
  freeze SourceManifest, ProjectModel, SeedSpec, GenerationPlan,
  ActivationReport and SkillRegistry contracts before changing generation.

B3 Autopoietic/cycle-first:
  implement ContextSnapshot, TensionReport, ResultantPacket and A1 proof first.

B4 Guide/product-first:
  write complete user/coder guides before schema and compiler work.

B5 Runtime/departmental-first:
  formalize events, departments and optional runtime before compiler core.
```

## Pruned And United Branches

```text
pruned:
  B1 because it repeats the weak-generator risk: behavior before contracts.
  B5 because runtime/departmental machinery is explicitly deferred.

united:
  B2 and B4: schemas and guides must be produced together. Schemas define
  machine contracts; guides explain architecture, use, cases and boundaries.
  B3 becomes a proposal-only proof plan after core schemas exist, not a
  blocker for Direct Start and Retrofit.
```

## Opening Detected

RepoKernel can be built as a compiler plus guide projection system:

```text
canonical contracts
  -> deterministic plan
  -> project files
  -> user/coder guides
  -> validation reports
```

This keeps guides essential while preventing them from becoming competing
manual truth.

## Selected Resultant

Phase 1 should implement the minimal `repokernel-core` contract layer and
package skeleton, with guides treated as first-class generated or maintained
surfaces of the core.

The exact Phase 1 scope is:

```text
core schemas and canonical serialization;
source intake model without broad ingestion logic;
deterministic SeedSpec -> GenerationPlan planning;
dry-run application only;
retrofit classification without writes;
activation report contract;
guide architecture and initial hand-authored guide set;
tests that lock authority, extension and no-overwrite invariants.
```

## Why It Minimizes Total Rework

Schemas before generator prevent unstable output. Guides during schemas prevent
the system from becoming coder-only. Deferring runtime/cycle/department
implementation prevents architecture weight from blocking the Direct Start and
Retrofit paths. Preserving extensions now avoids schema-breaking migrations
when cognition, A1 cycles, departments and projections are later added.

## Phase 1 Exact Scope

Create:

```text
pyproject.toml
src/repokernel/__init__.py
src/repokernel/canonical.py
src/repokernel/models.py
src/repokernel/paths.py
src/repokernel/planner.py
src/repokernel/guide_model.py
schemas/source-manifest.schema.json
schemas/project-model.schema.json
schemas/seed-spec.schema.json
schemas/generation-plan.schema.json
schemas/activation-report.schema.json
schemas/skill-registry.schema.json
docs/guides/README.md
docs/guides/architecture.md
docs/guides/user-guide.md
docs/guides/coder-guide.md
docs/guides/use-cases.md
docs/guides/application-types.md
docs/guides/examples/minimal-project.md
tests/unit/test_schemas.py
tests/unit/test_canonical.py
tests/unit/test_planner.py
tests/unit/test_guide_model.py
```

Modify:

```text
README.md
docs/quickstart.md
docs/readiness-levels.md
docs/seed-synthesis-pipeline.md
docs/retrofit-model.md
repokernel.json
registry/skills.json
CURRENT_STATE.md
sources/bootstrap/SOURCE_ATLAS_v1.0.md
```

Keep current scripts as compatibility wrappers until parity tests prove the
package path.

## Explicit Deferrals

```text
compile/apply writes beyond dry-run
runtime/event daemon/scheduler
network transport
multi-agent polling
project writes from autonomous cycles
skill factory execution
automatic promotion
Seed promotion
Domain Pack catalog
departmental runtime workers
persistent nested departments
external product claims beyond verified evidence
```

## Files To Create Or Modify

Phase 1 implementation files are listed above. This convergence packet does
not create them.

Gate deliverables created with this packet:

```text
process/reports/phase1-schema-classification.json
process/reports/package-boundaries-v1.md
process/reports/departmental-topology-decision.md
process/reports/guide-system-decision.md
packets/FOR_CODEX/A1_OBSERVE_AND_PROPOSE_PROOF_PLAN.md
packets/FOR_CODEX/PHASE1_PACKET_AMENDMENT_PROPOSAL.md
```

## Acceptance Tests

```text
schema validation accepts minimal valid SourceManifest, ProjectModel, SeedSpec,
  GenerationPlan, ActivationReport and SkillRegistry fixtures.
unknown namespaced extensions round-trip unchanged.
unknown extensions cannot increase authority or add writes.
same reviewed SeedSpec produces same canonical hash and same GenerationPlan.
new-repository plan emits project-specific content.
retrofit plan preserves existing AGENTS.md and reports propose_update instead
  of overwrite.
dry-run writes no files.
private/withheld source does not appear in public guides or generated output.
guide model produces user, coder, architecture, use-case and example surfaces
  from canonical fields without duplicating authority.
activation remains blocked until selected audit passes.
```

## Falsification Path

Reject or revise this Resultant if Phase 1 cannot prove one of:

```text
deterministic planning;
extension round-trip without authority effect;
no silent overwrite;
guide generation/application without duplicated canon;
retrofit no-write dry run;
minimal Direct Start remains understandable to a non-coder user.
```

## Rollback Point

The rollback point is the clean Phase 0 baseline:

```text
commit cc5181e
```

Phase 1 should be one isolated implementation branch or commit series after
operator acceptance.

## Neighborhood Implications

```text
Business Manager:
  may describe RepoKernel externally only as observe/propose/setup until proof.

d-nd-seed:
  remains untouched until Reference Seed reproducibility exists.

Editoriali:
  can later consume RepoKernel as an applied project kernel, not as source repo
  duplication.

Denis / external contacts:
  use A1 observe-and-propose only, no writes.

Lab:
  prior weak-generator lessons become guide/test pressure, not copied design.
```

## Critical Gap Acceptance Matrix

```text
G1 intent contract: core_optional in Phase 1 as IntentContract reference fields
  in SeedSpec; full schema deferred.
G2 context snapshot: provisional for A1 proof; not core dependency.
G3 tension function: provisional for A1 proof.
G4 cycle state machine: deferred; no runtime cycle in Phase 1.
G5 separation of duties: core_required invariant and tests.
G6 fitness contract: core_optional/provisional reference; full schema deferred.
G7 action transaction: deferred beyond dry-run; no writes.
G8 autonomy axis: core_optional field/reference; no authority effect.
G9 memory metabolism: core_optional LearningDelta reference; full cycle deferred.
G10 capability forge: deferred.
G11 trigger/cascade: namespaced_extension/provisional fixture only.
G12 security/trust: core_required invariants for source authority, path boundary,
  no secrets, no network by default.
G13 empirical latency proof: deferred until A1 proof measurement.
G14 gate fragmentation: closed by this single convergence packet.
G15 departmental topology: namespaced_extension plus decision report; no runtime.
```

## Stop Reason

This Resultant stops before Phase 1 implementation because the convergence gate
requires operator acceptance. The next safe action is an explicit operator
decision:

```text
accept Phase 1 scope and implement it;
or revise the scope before code changes.
```
