# RepoKernel Full-Surface And Pilot Review

Date: 2026-06-25  
Reviewer role: GPT Pro independent architecture/product review  
RepoKernel reference: `b5f7958c877314adba75e5c104342dd6c7024c45`  
Pilot repository: `GrazianoGuiducci/denis-repokernel-pilot`  
Verdict: architecture coherent; product path partially proven; dual completion gate required

## Executive Verdict

RepoKernel has moved beyond the earlier prototype skeleton. It now has:

```text
package metadata and CLI entry point;
contract validators;
canonical hashing;
path guards;
.repokernernel-oriented deterministic planning;
staging-only rendering;
public-safe guide filtering;
read-only inspection and audit;
18 local unit tests;
minimal product-path evidence;
A1 no-write proof documents;
a private pilot workspace.
```

The architecture should be preserved. The next step is not Phase 2, runtime,
Seed promotion or broad public distribution. The next step is to close one
**dual conformance cycle**:

```text
Track A — RepoKernel Core Conformance
  contracts -> planner -> stage -> audit -> packaged CLI -> reproducible evidence

Track B — Pilot Conformance
  pinned RepoKernel version -> inspect existing workspace -> plan -> stage outside
  target -> review -> independent evaluation -> feedback -> no-write proof
```

The two tracks share one version lock and one review ledger. The pilot may
produce evidence and transferable findings, but it must not introduce
person-specific logic into RepoKernel core.

## What Is Correct

### Architecture

- One compiler and one SeedSpec lineage.
- `.repokernel/` is the canonical control plane.
- Root files are adapters or existing project authority.
- New repository and retrofit remain modes of one planner.
- L0-L2 remain the first stable scope.
- L3, runtime, network automation and automatic apply remain deferred.
- Cognition, cycle and departmental ideas remain optional layers.

### Product Safety

- No `apply` command exists.
- `stage` writes only to an explicitly selected empty review directory.
- Private and withheld source labels are excluded from public guide source lists.
- Existing root `AGENTS.md` and `README.md` become review proposals rather than silent overwrites.
- The public procedure states that external repositories remain read-only.

### Governance Progress

- Phase 1 direction and P0 hardening are recorded.
- The independent review is stored in the repository.
- The active packet now describes Phase 1 P0 rather than Phase 0 only.
- The pilot keeps private relationship context out of RepoKernel core.

## Remaining Critical Gaps

### C1 — Schema Files Are Not Executed As Schemas

`tests/unit/test_schemas.py` confirms that schema files parse as JSON, but does
not run Draft 2020-12 validation. Python validators and JSON Schemas may drift.

Required:

```text
execute every schema against valid and invalid fixtures;
run parity tests against Python validators;
fail when one accepts an object that the other rejects;
pin and document the JSON Schema validator dependency or implement an explicit
minimal subset with a declared limitation.
```

### C2 — SeedSpec Is Not Yet A Reviewed Build Contract

The architecture requires a reviewed SeedSpec, but the current contract does
not require:

```text
review.status = accepted;
reviewer or acceptance authority;
source_manifest_hash;
project_model_hash;
compiler compatibility;
canonical namespace;
validation plan;
file-plan policy.
```

The planner currently accepts an unreviewed minimal SeedSpec.

### C3 — Retrofit Planning Is Path-Aware, Not State-Aware

The current planner receives an `existing_paths` list. It does not receive:

```text
target snapshot hash;
existing content hashes;
known authoritative file roles;
content equality;
case-collision information;
symlink boundary;
before hashes;
patch/diff references.
```

It therefore cannot distinguish:

```text
identical existing content -> leave_unchanged;
reviewable canonical update -> propose_update;
stale target -> block;
unsafe collision -> conflict.
```

The private pilot is especially useful here because it already contains root
adapters and a partial `.repokernel/` control plane. The current planner will
likely classify existing canonical `.repokernel/state` and source files as
conflicts rather than performing a semantic reconciliation.

### C4 — Audit Is Still Root-First And Self-Attested

The current `project` audit profile expects legacy root surfaces, while the
accepted installed architecture places canonical state under `.repokernel/`.

The source audit also considers validation passed when a phrase exists in
`LOCAL_VALIDATION.md`. It does not directly execute tests, schemas, package
installation, CLI smoke tests or artifact checks.

Required distinction:

```text
repository_structure_ready
contract_conformant
planner_conformant
pilot_conformant
distribution_ready
```

Do not compress these into one `L2 ready` result.

### C5 — Extension Safety Is Still A Blacklist

Extensions are preserved, but current validation searches for a limited set of
field names. Equivalent fields can bypass the blacklist.

Core rule should be:

```text
extensions are opaque data;
core planning never interprets extension semantics;
all extension blocks have authority_effect = none;
only a separately registered adapter may interpret a known namespace;
adapter capabilities are declared outside the payload.
```

### C6 — Guide Disclosure Is Better But Not Complete

Public source labels are deny-by-default, which is correct. Project `intent` and
`product` are still always emitted into generated guides. A private project may
need field-level disclosure controls.

Add a disclosure profile that controls:

```text
project name;
intent;
product;
source labels;
domain;
users;
paths;
examples.
```

### C7 — Packaging Is Not Yet Proven

`pyproject.toml` exposes a `repokernel` command, but there is no committed wheel
or clean-environment installation proof. Schemas and guide resources are stored
outside the package and may not be available after installation.

Required proof:

```text
build wheel and sdist;
install into a clean virtual environment;
run repokernel --help;
run minimal validate -> plan -> stage -> guides flow;
verify package resources are present;
uninstall cleanly.
```

### C8 — No Hosted CI Evidence

The repository contains local validation text, but no tracked `.github/`
workflow in the current inventory. “Repository-hosted validation” should not mean
that a result was written into the repository.

Use:

```text
repository-contained local validation
```

until a hosted CI run exists and is linked by commit.

### C9 — Current State Contains Historical Residue As Active Unknowns

`CURRENT_STATE.md` still lists Phase 0 classification and registry cleanup as
not verified while later reports and the 129-file inventory exist. It also
retains an “After explicit Phase 0 acceptance” block although the convergence
and Phase 1 work already occurred.

Normalize current state to the active P0/pilot gate and move historical sequence
to decision/delta records.

## Pilot Review

## Pilot Strengths

The private pilot correctly:

- remains a neutral workspace;
- uses `.repokernel/` state;
- separates technical method from private relationship context;
- blocks external writes;
- requires path selection and review before configuration;
- defines explicit stop/no-fit options;
- avoids claiming installation into an external repository.

## Pilot Gaps

### P1 — Not Version-Pinned

The pilot refers to local Windows filesystem paths for RepoKernel sources. This
is not portable and does not prove which compiler revision produced an artifact.

Replace with:

```text
RepoKernel repository URL;
source commit SHA;
package version;
contract versions;
pilot protocol version.
```

Private Business Manager sources should be referenced by a private source ID,
not a workstation path.

### P2 — It Is A Decision Scaffold, Not Yet A Product Test

The pilot has not yet produced:

```text
machine-readable SourceManifest;
reviewed SeedSpec;
read-only inspect report;
target snapshot;
GenerationPlan;
staging report;
guide output;
contract/audit result;
reviewer evaluation;
versioned feedback.
```

### P3 — Existing Canonical Surface Is A Valuable Adversarial Fixture

The pilot already contains:

```text
root AGENTS.md;
README.md;
.repokernel/state/CURRENT_STATE.md;
.repokernel/sources/SOURCE_ATLAS.md;
.repokernel/review/REVIEW_POLICY.md.
```

This makes it a better test than an empty repository. The expected planner
result is not to recreate these files blindly. It should classify existing
canonical surfaces using content and authority:

```text
leave_unchanged
propose_update
conflict with reason
```

The test should expose planner limitations without altering the pilot.

### P4 — Pilot Outcome Must Remain Neutral

Only generic findings may flow back to RepoKernel:

```text
contract gaps;
planner behaviors;
CLI friction;
guide ambiguity;
privacy failures;
reentry quality;
versioning needs.
```

Person-specific context, relationship notes and selected business follow-up
remain outside RepoKernel.

## Dual Completion Model

### Track A — Core Conformance

Exit conditions:

1. JSON Schemas execute and match Python validators.
2. Accepted review block and source/model hashes are required by SeedSpec.
3. Plan is bound to compiler version and target snapshot.
4. Existing content can produce `leave_unchanged`.
5. `.repokernel/` project audit profile exists.
6. Audit does not trust a validation phrase as proof.
7. Clean-environment package/CLI test passes.
8. Hosted CI or explicitly labeled local-only evidence is available.
9. Reference Seed reproducibility proof passes.

### Track B — Pilot Conformance

Exit conditions:

1. Pilot locks RepoKernel commit and contract versions.
2. Inspect is run read-only.
3. SourceManifest and accepted SeedSpec validate.
4. Existing-file inventory includes hashes and authority roles.
5. Plan is produced without target writes.
6. Staging occurs outside the pilot target or in an explicitly disposable review
   directory excluded from canonical state.
7. Before/after target tree hashes are equal.
8. Independent reviewer evaluates usefulness, safety and omissions.
9. Feedback is classified and returned through the review loop.
10. No person-specific material flows into RepoKernel core.

## Shared Completion Gate

RepoKernel may move from `private_pilot_first` toward trusted collaborator use
only when both tracks pass on the same pinned version.

```text
CoreConformanceReport.version_lock
  == PilotConformanceReport.version_lock
```

A later code change invalidates only the affected checks, but the distribution
verdict must show which evidence was produced against which version.

## Versioning Decision

Use four independent versions:

```text
1. package_version
   SemVer/pre-release, e.g. 0.3.0.dev0

2. contract_version
   schema IDs such as repokernel.seed-spec.v1

3. source_revision
   exact Git commit SHA

4. review_cycle
   RK-RVW-YYYYMMDD-NN
```

Every generated or reviewed artifact should record:

```text
artifact_schema;
repo_kernel_package_version;
repo_kernel_source_revision;
contract_versions;
seed_spec_hash;
target_snapshot_hash when relevant;
review_cycle;
created_at;
created_by_role;
review_status;
supersedes;
```

## GPT Pro — Codex — Operator Loop

```text
operator
  -> states intent, target, boundary and acceptance authority

GPT Pro
  -> performs independent expansion/contraction review
  -> returns findings with evidence and severity

triage
  -> accept | adapt | defer | reject | needs_verification

Codex
  -> implements only accepted/adapted items
  -> records exact files, commit and validation evidence

GPT Pro readback
  -> verifies implementation against accepted findings
  -> identifies regressions and remaining uncertainty

operator
  -> accepts, requests another cycle or stops

archive
  -> temporary packets are removed or archived;
     durable decisions, tests and deltas remain
```

No role self-closes the whole cycle.

## Readiness Verdict

```text
internal prototype use: ready with version lock and no-write boundary
private technical pilot: ready after protocol/version files are added
trusted collaborator tool use: not yet ready
public experimental tester request: not yet ready
production: not ready
```

## Immediate Resultant

Do not expand scope. Complete:

```text
schema/validator parity;
reviewed SeedSpec;
target snapshot planning;
canonical audit;
package installation proof;
version-locked private pilot;
independent pilot evaluation;
review-cycle ledger.
```

Then reassess distribution readiness.
