# RepoKernel Core And Pilot Completion Packet

Date: 2026-06-25  
Review cycle: `RK-RVW-20260625-01`  
Status: ready for operator acceptance, then Codex implementation  
Temporary packet: archive or delete after cycle closure

## Objective

Close the current dual task without expanding scope:

```text
A. make the Phase 1 core contract-safe, installable and honestly auditable;
B. qualify the private pilot as a version-locked, no-write existing-repository test.
```

Do not begin Phase 2, apply, runtime, Seed promotion, external network automation
or public tester distribution.

## Read Order

```text
CURRENT_STATE.md
process/FIRST_PACKET.md
process/reports/REPOKERNEL_FULL_SURFACE_AND_PILOT_REVIEW_2026-06-25.md
docs/guides/evolution-versioning-and-review-loop.md
docs/compatibility-matrix.md
process/reviews/REVIEW_LEDGER.md
packets/FOR_CODEX/PHASE1_P0_HARDENING_PACKET_2026-06-24.md
src/repokernel/
schemas/
tests/unit/
Former private pilot fixture:
  README.md
  AGENTS.md
  .repokernel/state/CURRENT_STATE.md
  .repokernel/sources/SOURCE_ATLAS.md
  .repokernel/review/REVIEW_POLICY.md
```

## Global Rules

```text
no target apply command;
no external repository write;
no network automation;
no credential access;
no D-ND-specific semantics in neutral core;
no person-specific material copied into RepoKernel;
no readiness claim without a version-pinned report;
no self-approval of implementation and verification.
```

## Track A — Core Conformance

### A0. Normalize Governance

Modify:

```text
CURRENT_STATE.md
process/FIRST_PACKET.md
process/DECISION_LOG.md
process/ROADMAP.md
sources/bootstrap/SOURCE_ATLAS_v1.0.md
process/reviews/REVIEW_LEDGER.md
```

Requirements:

- remove stale “after Phase 0” instructions;
- remove already-resolved items from `not_yet_verified`;
- set active objective to this dual completion packet;
- record operator acceptance of `RK-RVW-20260625-01` before code changes;
- distinguish local validation from hosted CI;
- record package/source/contract versions.

Acceptance:

```text
recovery procedure finds no contradiction among state, packet, decision log and atlas.
```

### A1. Execute JSON Schemas And Enforce Parity

Create or modify:

```text
src/repokernel/schema_validation.py
src/repokernel/models.py
schemas/*.schema.json
tests/fixtures/contracts/**
tests/unit/test_schema_validation.py
tests/unit/test_schema_validator_parity.py
pyproject.toml
```

Requirements:

- use a real Draft 2020-12 validator;
- select and pin a reviewed `jsonschema` 4.x dependency;
- validate formats/patterns explicitly where relied upon;
- produce structured errors with path, code and message;
- run identical valid/invalid fixtures through JSON Schema and Python validation;
- fail parity when acceptance differs;
- reject duplicate source IDs;
- add authority/privacy/freshness/instruction-handling enums;
- ensure source documents default to `data_only`;
- constrain skill states, risk and evidence shape;
- prohibit `active` ActivationReport when required checks fail or are absent.

Acceptance:

```text
all positive and negative fixtures agree across both validator surfaces.
```

### A2. Make SeedSpec Reviewable And Version-Bound

Extend `SeedSpec` with required fields:

```text
version
source_manifest_hash
project_model_hash
canonical_namespace: .repokernel
review:
  status: accepted
  accepted_by_role
  accepted_at
  review_cycle
compiler_compatibility
file_plan_policy
validation_plan
```

Rules:

- planner rejects any SeedSpec whose review status is not accepted;
- review metadata is provenance, not authority escalation;
- `authority_mode` remains no higher than `propose` in this line;
- semantic hash policy explicitly includes/excludes fields.

Update examples and guides.

### A3. Add TargetSnapshot And Content-Aware Retrofit Planning

Create:

```text
schemas/target-snapshot.schema.json
src/repokernel/snapshot.py
```

Extend `inspect` to emit:

```text
target_snapshot_id
tree_hash
path
kind
content_hash for eligible text files
authority_role when known
excluded reason
case-collision warnings
symlink warnings
```

Extend GenerationPlan with:

```text
plan_id
compiler_version
target_snapshot_hash
before_hash
after_hash
patch_or_content_ref
apply_policy
rollback_manifest placeholder
```

Planner behavior:

```text
same path + same content -> leave_unchanged
existing root/project authority -> propose_update
existing canonical .repokernel surface -> leave_unchanged or propose_update based on content
unsafe/unclassified collision -> conflict
stale or missing snapshot for retrofit -> blocked
```

The planner must distinguish `new_repository` from
`existing_repository_retrofit`.

### A4. Replace Extension Blacklist With Opaque Extension Policy

Core planner and validators must not infer capabilities from extension payloads.

Requirements:

```text
extension key is a valid namespace;
extension data round-trips;
authority_effect is always none;
core planner output is identical with or without semantically unknown extension data;
known adapter interpretation requires a separate registered adapter declaration.
```

Add adversarial tests for aliases such as:

```text
write_files
permissions
requested_actions
tool_policy
publish_request
```

### A5. Add Disclosure Profiles

Create a minimal disclosure contract:

```text
public
internal
private
```

Public guide projection includes only explicitly permitted fields.

Control:

```text
project name
intent
product
source labels
domain
users
paths
examples
```

Default public profile is deny-by-default.

### A6. Canonical Project Audit

Add a canonical profile for `.repokernel/` projects.

Separate results:

```text
repository_structure_ready
contract_conformant
planner_conformant
project_kernel_ready
distribution_ready
```

Remove phrase-based validation evidence. Audit must not pass because a Markdown
file contains “validation passed”.

The source-repository conformance command may invoke:

```text
unit tests;
schema parity suite;
minimal product path;
package install smoke test;
Reference Seed verification when available.
```

Keep ordinary target audits read-only and bounded.

### A7. Package And CLI Proof

Requirements:

```text
build wheel and sdist;
install into clean virtual environment;
run repokernel --help;
run validate-spec -> inspect -> plan -> stage -> guides -> audit;
verify schemas/templates/resources are included;
verify no target writes;
uninstall cleanly.
```

Add `.github/workflows/ci.yml` or document why hosted CI is unavailable. If CI
is added, run supported Python versions and publish no secrets.

### A8. Reference Seed Reproducibility

Create one normative L1 Reference Seed spec and generated distribution.

```text
specs/reference/starter-l1.seed.json
dist/reference/starter-l1/
```

Add `verify-dist`:

```text
regenerate to temp;
normalize non-semantic metadata;
compare every path and hash;
fail on drift.
```

Do not hand-edit `dist/`.

## Track B — Private Pilot Conformance

Repository:

```text
former private pilot fixture
```

The pilot is a private test workspace. It is not evidence that RepoKernel is
installed in a formerly selected external project.

### B0. Portability And Version Lock

Replace workstation paths in the pilot Source Atlas with repository identifiers
and immutable revisions.

Create:

```text
.repokernel/review/REPOKERNEL_VERSION_LOCK.md
docs/REPOKERNEL_PRODUCT_TEST_PROTOCOL.md
packets/FOR_CODEX/DENIS_PILOT_TEST_EXECUTION_PACKET_2026-06-25.md
```

Version lock records:

```text
RepoKernel source revision used for the test;
package version;
contract versions;
review cycle;
pilot run ID;
authority: read/propose only;
expected target tree hash before execution.
```

Private Business Manager context is referenced only by a private source ID, not
a workstation path.

### B1. Create Pilot Inputs

Under a versioned test-run directory, create:

```text
test-runs/RK-PILOT-20260625-01/source-manifest.json
test-runs/RK-PILOT-20260625-01/project-model.json
test-runs/RK-PILOT-20260625-01/seed-spec.json
```

Rules:

- target mode is `existing_repository_retrofit`;
- canonical namespace is `.repokernel`;
- authority is `propose`;
- SeedSpec review is accepted by operator before plan;
- private relationship context is withheld;
- direct RepoKernel public docs are technical sources;
- pilot-local files remain target authority.

### B2. Execute Read-Only And Stage Outside Target

Run the installed, pinned RepoKernel build:

```text
inspect pilot;
validate all inputs;
plan against TargetSnapshot;
stage to a temporary sibling directory outside the pilot;
generate guides with internal disclosure profile;
audit the pilot before and after;
```

Capture:

```text
before tree hash
after tree hash
inspect report
GenerationPlan
stage report
guide report
audit report
stdout/stderr summary
```

Required invariant:

```text
before tree hash == after tree hash
```

Do not commit the staged proposed tree to the pilot target. Commit only sanitized
reports and selected plan excerpts after review.

### B3. Pilot Assertions

The run must test:

```text
existing AGENTS.md preserved;
existing README.md preserved;
existing .repokernel/state recognized;
existing .repokernel/sources recognized;
review policy remains authoritative;
local paths are not leaked;
private source IDs do not enter public outputs;
canonical files are leave_unchanged or propose_update, not blind conflict;
missing packet/manifest surfaces are proposed explicitly;
no target write;
no external action.
```

### B4. Independent Evaluation

Create:

```text
test-runs/RK-PILOT-20260625-01/PILOT_EVALUATION.md
```

Evaluator checks:

```text
reentry quality;
plan correctness;
conflict quality;
false positives/negatives;
guide usefulness;
privacy;
no-write proof;
version provenance;
remaining operator burden;
what should become a core test.
```

The implementer does not mark the pilot independently passed.

## Interaction Artifacts

For `RK-RVW-20260625-01`, create:

```text
process/reviews/RK-RVW-20260625-01/TRIAGE.md
process/reviews/RK-RVW-20260625-01/CODEX_RETURN.md
process/reviews/RK-RVW-20260625-01/GPT_PRO_READBACK.md
process/reviews/RK-RVW-20260625-01/OPERATOR_DECISION.md
```

Triage every review finding as:

```text
accept | adapt | defer | reject | needs_verification
```

## Final Acceptance Gate

The cycle passes only when:

```text
core conformance is tied to a commit/package version;
pilot conformance uses the same version lock;
all target writes remain zero;
independent readback passes or lists explicit blockers;
operator records final acceptance;
compatibility matrix and review ledger are updated;
temporary packets are archived or deleted;
CURRENT_STATE and FIRST_PACKET point to the next true gate.
```

## Required Codex Return

```text
exact commits in both repositories;
files changed;
version lock;
commands and actual outputs;
core conformance report;
pilot conformance report;
remaining blockers;
deviations from this packet;
items requiring operator decision.
```
