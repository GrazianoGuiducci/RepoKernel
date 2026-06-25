# Evolution, Versioning And Review Loop

Status: Phase 1 governance contract  
Audience: operator, GPT Pro reviewer, Codex implementer, maintainers and pilot reviewers

## Purpose

RepoKernel improves through repeated interaction, but improvement must remain
traceable. This protocol separates product version, contract version, source
revision and review-cycle state so that evidence does not silently become stale.

## Four Version Coordinates

### Package Version

Use semantic versioning with pre-release labels:

```text
0.3.0.dev0   development surface
0.3.0a1      first installable alpha
0.3.0b1      pilot-qualified beta
0.3.0rc1     release candidate
0.3.0        stable release
```

A package-version change identifies a product distribution change. It does not
by itself change contract meaning.

### Contract Version

Each machine contract has an independent identifier:

```text
repokernel.source-manifest.v1
repokernel.project-model.v1
repokernel.seed-spec.v1
repokernel.generation-plan.v1
repokernel.activation-report.v1
```

Rules:

- breaking semantic changes require a new contract major version;
- additions must remain backward compatible or stay under namespaced extensions;
- a contract ID is not declared stable merely because it says `v1`;
- stability is declared in the compatibility matrix and release notes;
- validators and schemas must agree on every frozen contract.

### Source Revision

Every proof, staged bundle and pilot run records the exact Git commit SHA.

```text
repo_kernel_source_revision: <40-character SHA>
```

A branch name such as `main` is not a reproducible version lock.

### Review Cycle

Every GPT Pro–Codex–operator cycle receives an ID:

```text
RK-RVW-YYYYMMDD-NN
```

Example:

```text
RK-RVW-20260625-01
```

The cycle ID links request, review, triage, implementation, validation and final
operator decision.

## Artifact Provenance Block

Every durable generated or reviewed artifact should carry, where applicable:

```yaml
artifact_schema: repokernel.<artifact>.v1
repo_kernel_package_version: 0.3.0.dev0
repo_kernel_source_revision: <commit-sha>
contract_versions:
  seed_spec: repokernel.seed-spec.v1
  generation_plan: repokernel.generation-plan.v1
seed_spec_hash: <sha256-or-null>
target_snapshot_hash: <sha256-or-null>
review_cycle: RK-RVW-YYYYMMDD-NN
created_at: <ISO-8601>
created_by_role: operator | gpt_pro | codex | evaluator
review_status: draft | proposed | accepted | implemented | verified | superseded
supersedes: []
```

Timestamps and human-readable labels may be excluded from semantic hashes only
through an explicit hashing policy.

## Review Lifecycle

```text
draft_request
-> ready_for_gpt_pro
-> reviewed
-> triaged
-> accepted_for_codex
-> implemented
-> independently_verified
-> operator_accepted
-> archived_or_superseded
```

### Operator

The operator owns:

```text
intent;
target selection;
source authorization;
authority boundary;
acceptance criteria;
final acceptance, deferment or stop decision.
```

### GPT Pro

GPT Pro performs independent review:

```text
inspect evidence;
expand hidden possibilities;
contract to concrete findings;
classify severity;
propose tests and falsifiers;
identify assumptions and unknowns.
```

GPT Pro does not authorize implementation or external action.

### Triage

Every review finding receives exactly one disposition:

```text
accept
adapt
defer
reject
needs_verification
```

A triage record includes rationale, owner, target version and acceptance test.

### Codex

Codex implements only `accept` and `adapt` items that belong to the active gate.

Codex returns:

```text
files changed;
commit SHA;
tests and commands;
actual results;
remaining blockers;
deviations from packet;
new risks discovered.
```

Codex does not mark its own implementation independently verified.

### GPT Pro Readback

GPT Pro compares the implementation against the accepted triage:

```text
implemented as accepted;
implemented with justified adaptation;
not implemented;
regressed;
new issue;
needs operator decision.
```

### Operator Closure

The operator chooses:

```text
accept cycle;
request correction;
open a new review cycle;
defer remaining items;
stop.
```

## Review Ledger

Maintain a compact ledger in:

```text
process/reviews/REVIEW_LEDGER.md
```

Recommended row:

| Cycle | Source revision | Scope | GPT Pro result | Codex commit | Verification | Operator decision | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |

The ledger points to artifacts; it does not duplicate their full content.

## Temporary Packet Policy

Files under `packets/FOR_CODEX/` and `packets/FOR_GPT_PRO/` may be temporary.

After cycle closure:

- delete or move superseded operational packets to `packets/archive/`;
- preserve the review result if it remains architectural evidence;
- preserve accepted decisions in `process/DECISION_LOG.md`;
- preserve implementation evidence in `process/evidence/`;
- preserve durable rule changes in `process/deltas/`;
- keep only the current active packet in the primary reentry path.

## Compatibility Matrix

Maintain:

```text
docs/compatibility-matrix.md
```

It should map:

```text
package version;
source revision or release tag;
contract versions;
Python versions;
CLI commands;
Reference Seed versions;
pilot evidence;
known limitations;
migration notes.
```

## Evidence Invalidation

Evidence becomes stale when any relevant coordinate changes:

```text
compiler logic;
contract semantics;
planner output policy;
path-safety policy;
guide disclosure policy;
audit implementation;
pilot target snapshot.
```

A change does not always require repeating every test. Each evidence record must
state which checks are invalidated and which remain applicable.

## Release Gates

### Development

```text
unit tests pass;
no-write boundary preserved;
known blockers explicit.
```

### Alpha

```text
clean-environment install proof;
schema/validator parity;
minimal deterministic product path;
versioned CLI documentation.
```

### Private Pilot

```text
core conformance passes;
pilot locked to exact version;
no-write target proof;
independent reviewer feedback;
operator acceptance.
```

### Public Experimental

```text
hosted CI;
Reference Seed reproducibility;
privacy/disclosure proof;
two neutral pilot reports;
accurate public claims;
versioned migration policy.
```

### Stable

```text
reviewed apply transaction or explicitly no-apply product definition;
rollback and stale-target controls;
security review;
compatibility commitment;
release notes and signed/tagged artifacts.
```

## Governing Rule

```text
No evidence without a version lock.
No implementation without an accepted review disposition.
No cycle closure without independent readback or explicit operator waiver.
No public readiness claim without evidence produced against the claimed version.
```
