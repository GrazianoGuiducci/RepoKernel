# GPT Pro Readback — RK-RVW-20260625-01

Date: 2026-06-25  
Reviewed implementation: `db6a761216d914530a8ee6c53956a5106434c535`  
Pointer commit: `e42064fc3a98d05a18a0703ba5c18792a7673432`  
Status: `pass_with_required_corrections`  
Track B: blocked pending correction readback and operator decision

## Review Method

This readback inspected the pushed implementation, schemas, tests, CLI, audit,
planner, snapshot logic, package metadata and `CODEX_RETURN` against the accepted
Track A triage.

The reviewer environment could not resolve `github.com` from the local container,
so the 32-test and clean-venv results were not independently re-executed in this
session. They remain Codex-produced, repository-contained evidence. Static
readback was performed against the exact pushed files.

## Executive Verdict

Track A made substantial and valid progress:

```text
Draft 2020-12 validation exists;
SeedSpec now requires accepted review metadata and input hashes;
TargetSnapshot and content-aware planning exist;
unknown extensions are opaque to core planning;
guide disclosure is deny-by-default for project fields;
.repokernernel project profile exists;
CLI includes validate, inspect, plan, stage, guides, audit and verify-dist;
package metadata includes jsonschema and packaged schemas;
no apply command exists;
Track B was correctly not executed.
```

Track A cannot yet be marked conformant complete. Several accepted criteria are
implemented only partially or are satisfied by presence checks rather than by
the promised invariant. These gaps directly affect the private pilot, especially
TargetSnapshot trust, canonical audit and Reference Seed reproducibility.

## Accepted As Implemented

### A. Governance And Scope

- Track A acceptance is recorded.
- Track B, apply, runtime, public distribution and Seed promotion remain blocked.
- `CODEX_RETURN` records exact commits, deviations and local evidence.

### B. Canonical JSON And Extension Direction

- Non-finite numbers are rejected.
- Extension keys are namespaced.
- Core planning does not inspect extension payload semantics.

### C. SeedSpec Review Gate

- `review.status` is constrained to `accepted`.
- source/model hash fields, canonical namespace, compiler compatibility,
  file-plan policy and validation plan are required.

### D. Basic Snapshot And Retrofit Behavior

- snapshots hash eligible text content;
- `.git/` is excluded;
- case collisions and symlinks are surfaced as warnings;
- identical planned content can become `leave_unchanged`;
- retrofit without a snapshot is blocked/withheld.

### E. Disclosure And No-Write Surface

- public project fields are withheld unless explicitly enabled;
- source labels require `privacy=public` and `used_for=public_guide`;
- staging writes only to an explicit empty review directory;
- no target apply command exists.

### F. Package Surface

- console entry point is declared;
- `jsonschema` is declared;
- packaged schema resources are configured;
- Codex reports a clean-wheel CLI proof.

## Required Corrections Before Track B

### R1 — Schema/Validator Parity Is Not Yet Complete

Severity: high

The parity suite covers a small positive/negative set for SeedSpec and
SourceManifest, plus positive TargetSnapshot cases. It does not establish
acceptance parity for all contracts.

Examples:

```text
ProjectModel Python validation checks mostly field presence;
SkillRegistry Python and JSON Schema validation do not constrain state/risk/evidence sufficiently;
ActivationReport conditional active-state behavior exists only in Python;
TargetSnapshot Python validation does not enforce path safety or hash shape;
SourceManifest duplicate source IDs are rejected only by Python;
GenerationPlan parity is not exercised through a negative matrix.
```

Required outcome:

```text
valid and invalid fixture matrix for every contract;
explicit documented exceptions where JSON Schema cannot express a semantic rule;
parity test fails on any unexplained acceptance difference;
SkillRegistry state/risk/evidence constraints enforced;
ProjectModel types and evidence-bearing source references enforced.
```

### R2 — TargetSnapshot Is Accepted Without Integrity Validation

Severity: critical for Track B

`repokernel plan` reads a supplied TargetSnapshot but does not run its Python or
JSON Schema validators. The planner does not recompute or verify that
`tree_hash` matches `entries`, and it trusts the supplied content hashes.

Additional snapshot gaps:

```text
only .git is excluded;
secret/sensitive/ignored path policy is absent;
non-UTF-8 files with eligible suffixes may abort inspection;
symlink and case-collision warnings do not automatically block unsafe planning;
duplicate entry paths are not rejected.
```

Required outcome:

```text
plan validates snapshot through both validator surfaces;
recompute and verify snapshot/tree identity before use;
bind snapshot to target identity;
reject duplicate/unsafe entries;
apply explicit exclusion policy for secrets, ignored paths, build/venv/vendor trees;
handle unreadable/non-UTF-8 files as excluded/warnings rather than crashing;
block or require operator review for symlink/case-collision conditions.
```

### R3 — GenerationPlan Is Not Fully Target-Bound

Severity: high

`plan_id` is currently the hash of `items` only. The same items can produce the
same plan ID for different SeedSpecs or targets. `after_hash` is a synthetic
hash of the prior hash and item hash, not a defined projected tree hash.

Required outcome:

```text
plan_id hashes seed hash, actual compiler version, target identity,
target snapshot hash, policy and items;
compiler version comes from the running package, not only from SeedSpec claims;
plan records a clear predicted-after-tree or renames the field to avoid
misrepresenting a synthetic hash;
retrofit plans reject missing or invalid snapshot identity.
```

### R4 — SeedSpec Hash Linkage Is Syntactic, Not Verified

Severity: high

SeedSpec requires `source_manifest_hash` and `project_model_hash`, but no command
verifies that they match the actual SourceManifest and ProjectModel used for the
run. Zero hashes can satisfy validation. Compiler compatibility is also copied
from the spec into the plan without checking the installed package.

Required outcome:

```text
add validate-bundle or equivalent;
recompute canonical SourceManifest and ProjectModel hashes;
verify SeedSpec linkage;
verify package/contract compatibility against the running implementation;
block planning when linkage fails.
```

### R5 — ProjectModel Is Not Yet Evidence-Bearing

Severity: high for synthesis and pilot evidence

The current model has one global `source_refs` list. The accepted architecture
and pilot protocol require source references for each material assertion and
explicit `verified/inferred/conflict/unknown` status.

Required outcome:

```text
introduce assertion objects or another explicit evidence map;
preserve conflicts and unknowns structurally;
validate source references against SourceManifest IDs;
add positive, conflicting and unsupported-assertion fixtures.
```

### R6 — Canonical Project Audit Is Functionally Incorrect

Severity: critical for Track B

The `project-kernel` profile requires `.repokernel/...` files, but the shared
audit flow still reads root `CURRENT_STATE.md`, root `process/FIRST_PACKET.md`,
root `skills/` and root `sources/bootstrap/SOURCE_ATLAS_v1.0.md` for non-reentry
profiles. A valid project that stores canonical state only under `.repokernel/`
can therefore fail for legacy-root reasons.

The source audit’s `contract_conformant` and `planner_conformant` checks are also
presence/token checks. They are appended after `evolution_ready` is calculated,
so `ready=true` may remain true independently of those conformance axes.

Required outcome:

```text
profile-specific state, packet, atlas and skill paths;
project-kernel profile audits only canonical project surfaces and registered adapters;
source readiness does not become true when contract/planner conformance is false;
conformance commands execute or consume version-pinned evidence rather than
checking module/token presence;
rename legacy profiles clearly where retained.
```

### R7 — `verify-dist` Verifies A Manifest, Not Reproducibility

Severity: critical to the accepted Reference Seed criterion

Current `verify-dist` checks listed file hashes against committed files. It does
not regenerate the distribution from the compiler, detect unexpected extra
files, or prove that the same accepted specification produces the distribution.

The current `starter-l1` manifest lists only `AGENTS.md` and current state; it is
not the complete L1 surface described by the architecture.

Required outcome:

```text
a normative Reference Seed input accepted by the compiler;
regenerate into a temporary directory;
compare exact normalized path set and hashes;
fail on missing and extra files;
include the full declared L1 surface or rename the artifact to its actual level;
never hand-edit generated dist output.
```

### R8 — CLI Commands Do Not Uniformly Validate Inputs

Severity: medium/high

```text
plan validates SeedSpec only through the Python validator and does not validate
TargetSnapshot;
guides does not validate SeedSpec or SourceManifest before projection;
stage validates GenerationPlan but does not explicitly refuse a blocked plan;
commands do not consistently record package/source provenance in reports.
```

Required outcome:

```text
shared contract-loading/validation path;
plan, guides and stage reject invalid contracts consistently;
stage policy for blocked plans is explicit and tested;
reports include package version, source revision or build identifier,
contract versions, review cycle and relevant hashes.
```

### R9 — Snapshot Exclusion And Privacy Policy Needs A Core Contract

Severity: high before general repository pilots

Snapshotting currently inventories nearly every path outside `.git/`. Even when
content is not emitted, path names and hashes can disclose sensitive structure
or cause unnecessary processing.

Required outcome:

```text
explicit default exclusions for credentials, .env, private keys, virtualenvs,
node_modules, build artifacts and user-declared withheld paths;
respect a reviewed ignore/exclusion policy;
record excluded reason without exposing secret content;
add fixture proving no secret path/content leakage.
```

### R10 — Hosted CI And License Warning

Severity: non-blocking for private pilot after all critical corrections

The missing workflow is a documented token-scope limitation. Local evidence may
be used for a controlled private pilot if labeled accurately. Before public
experimental distribution, add hosted CI through a token or UI with workflow
permission.

Replace the deprecated TOML license table with an SPDX string during the
correction pass.

## Track A Disposition

```text
architecture_direction: accepted
implementation_progress: substantial
core_conformance: not_yet_accepted
readback_result: pass_with_required_corrections
track_b_authority: blocked
public_distribution: blocked
```

## Minimal Correction Gate

Track B may start only after:

1. R1, R2, R3, R4, R6 and R7 are implemented and independently read back.
2. R5 is implemented or the pilot is explicitly narrowed to a non-synthesis
   fixture with a documented temporary model limitation; preferred decision is
   to implement it now.
3. R8 and R9 have passing safety tests.
4. Codex reruns package, contract, planner, audit and verify-dist proofs and ties
   them to one exact commit.
5. GPT Pro readback marks the correction commit `accepted_for_private_pilot`.
6. Operator explicitly authorizes Track B against that exact version lock.

## Readback Evidence Status

```text
Codex local tests: acknowledged, not independently rerun in this session
static source readback: completed
hosted CI: absent
pilot execution: not run
independent pilot evaluation: not run
```

## Next Safe Action

Codex executes the bounded Track A readback correction packet. It must not touch
the private pilot or begin Track B.
