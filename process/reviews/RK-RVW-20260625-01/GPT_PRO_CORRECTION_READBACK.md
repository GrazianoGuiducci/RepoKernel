# RepoKernel Track A Correction - Final GPT Pro Readback

Date: 2026-06-25
Review cycle: `RK-RVW-20260625-01`
Reviewed implementation: `43902309fb41a9574bddf1ffa13b07238fd6488a`
Pointer commit: `f26471fbb2f8e346db69cd5a5c02335a753697bd`
Package: `0.3.0.dev0`

## Verdict

```text
Track A architecture: accepted
Track A implementation: accepted for a controlled neutral no-write diagnostic pilot
Alpha/public readiness: not accepted
Apply/runtime/network/Seed promotion: blocked
Former private pilot fixture: remains frozen unless explicitly reauthorized
```

Codex closed the central Track A corrections:

- linked SourceManifest/ProjectModel/SeedSpec bundle validation;
- evidence-bearing ProjectModel assertions;
- TargetSnapshot integrity checks and exclusion policy;
- target/snapshot/compiler/bundle-bound GenerationPlan identity;
- blocked-plan staging rejection;
- compiler-regenerated Reference Seed comparison with extra-file detection;
- canonical `.repokernel/` audit path;
- SPDX license and clean local package proof.

The 45-test and clean-environment results remain Codex-produced local evidence.
They were not independently re-executed by GPT Pro because the review container
could not resolve GitHub.

## Residual Debt

These items do not prevent a read-only diagnostic fixture, but they block alpha,
public testing or a claim of complete self-conformance.

### 1. Live SkillRegistry does not match its own new contract

The checked-in registry still uses risk values such as `safe` and `writes_files`,
plus fields not admitted by the current schema. Add a test validating the actual
`registry/skills.json`, then migrate either the schema or the data deliberately.

### 2. Generated Starter L1 does not pass its own project-kernel audit

The generated current-state file lacks `boundary` and `first_safe_action`.
The generated first packet lacks `source`, `boundary`, `first_safe_action` and
`memory delta`.

Add one invariant test:

```text
generate starter-l1
-> audit generated directory with profile project-kernel
-> ready must be true
```

### 3. TargetSnapshot remains limited

- raw `root` can expose a workstation path;
- `target_identity` is not recomputed from `root`;
- unsupported/binary file content is represented with `content_hash = null`, so
  some content changes do not alter the tree hash;
- a missing target warning is not clearly treated as blocking;
- the default exclusion policy is not yet operator-configurable.

A diagnostic pilot must therefore be text-oriented, use a fresh snapshot
generated in the same run, and commit only sanitized reports.

### 4. Snapshot validation in `plan` is not fully uniform

Planning uses Python TargetSnapshot validation and integrity checking, but does
not explicitly execute the JSON Schema validator on the supplied snapshot.
This is acceptable for the controlled diagnostic path, not for a conformance
claim.

### 5. Provenance needs the exact source revision

Artifacts record package and contract information but not an immutable source
revision. The pilot must carry the exact commit in its external version lock.

## Controlled Diagnostic Pilot Gate

A neutral pilot may run only if the operator explicitly selects or reauthorizes
the fixture.

Version lock:

```text
RepoKernel source revision:
43902309fb41a9574bddf1ffa13b07238fd6488a

pointer:
f26471fbb2f8e346db69cd5a5c02335a753697bd

package:
0.3.0.dev0
```

Required controls:

```text
A1 observe-and-propose only
read-only target
fresh inspect and plan in the same run
do not edit the TargetSnapshot manually
stage outside the target
before target hash == after target hash
no network, credentials, apply, runtime or remote mutation
do not commit raw absolute workstation paths
treat audit results as diagnostic, not activation proof
independent evaluator and operator decision required
```

The former private pilot fixture remains frozen under the current repository
decision. It is not selected by this readback.

## Codex Instruction

```text
Track A is accepted for a controlled neutral no-write diagnostic pilot, with the
residual debt recorded in this readback.

Do not modify or execute the former private pilot fixture unless the operator
explicitly reauthorizes it as a neutral technical fixture.

Before any selected pilot:
1. record RepoKernel commit 43902309fb41a9574bddf1ffa13b07238fd6488a;
2. record package 0.3.0.dev0 and all contract versions;
3. use a fresh same-run TargetSnapshot;
4. stage outside the target;
5. prove before/after target equality;
6. sanitize absolute local paths from committed evidence;
7. obtain independent evaluation;
8. return residual findings without weakening contracts.

Do not start public distribution, apply, runtime, network automation or Seed
promotion.
```

## Next Development Debt

After the diagnostic pilot, consolidate the findings with:

```text
actual registry self-validation
generated starter audit invariant
full-file snapshot hashing or explicit unhashed-file blocking
target identity verification/redaction
uniform contract validation
source-revision provenance
hosted CI
```
