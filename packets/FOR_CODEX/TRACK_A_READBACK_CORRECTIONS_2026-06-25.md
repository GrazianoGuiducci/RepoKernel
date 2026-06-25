# Track A Readback Corrections

Date: 2026-06-25
Review cycle: `RK-RVW-20260625-01`
Status: waiting for operator acceptance
Source implementation: `db6a761216d914530a8ee6c53956a5106434c535`
Source readback: `process/reviews/RK-RVW-20260625-01/GPT_PRO_READBACK.md`
Track B: blocked

## Objective

Complete the remaining Track A invariants and return one exact commit for final
GPT Pro readback. Do not execute the private pilot in this packet.

## Scope

### 1. Contract parity

- Add positive and negative fixtures for every current contract.
- Run both Draft 2020-12 and Python validation on each fixture.
- Fail unexplained acceptance differences.
- Constrain SkillRegistry states, risk, identifiers and evidence.
- Make ProjectModel evidence-bearing and preserve conflict/unknown status.
- Validate safe and unique TargetSnapshot paths.

### 2. Bundle linkage

Add `validate-bundle` or equivalent for SourceManifest, ProjectModel and
SeedSpec.

It must:

```text
validate all contracts;
validate source references;
recompute source/model canonical hashes;
compare SeedSpec hashes;
verify accepted review;
verify running package compatibility;
return structured errors and provenance.
```

Planning must require a valid bundle artifact or equivalent proof.

### 3. Snapshot integrity

- Validate a supplied TargetSnapshot before planning.
- Recompute and verify snapshot/tree identity.
- Reject duplicate and unsafe entries.
- Define target identity binding.
- Handle unreadable files through bounded exclusions/warnings.
- Add a reviewed default exclusion policy for non-project and sensitive paths.
- Block unsafe symlink and case-collision conditions according to policy.

### 4. Target-bound plans

- Bind `plan_id` to compiler version, bundle/SeedSpec hash, target identity,
  snapshot hash, policy and items.
- Use the running package version, not only a value asserted by the SeedSpec.
- Define the exact meaning of the projected-after-state hash.
- Require a valid fresh snapshot for retrofit.
- Test identical item lists against different targets/snapshots.

### 5. Reference Seed reproducibility

Current `verify-dist` checks recorded hashes; it does not regenerate output.

Implement:

```text
normative compiler input;
temporary regeneration through the normal emitter;
exact normalized path and content comparison;
missing and extra file detection;
full declared L1 surface or honest level/name correction;
generated-only dist policy.
```

### 6. Canonical project audit

- Make audit paths profile-specific.
- `project-kernel` must read canonical `.repokernel/` state, packet, atlas and
  skill surfaces without requiring legacy root equivalents.
- Source readiness must fail when required contract/planner conformance fails.
- Replace module/token presence checks with bounded actual checks or pinned
  evidence.
- Add passing and failing canonical fixtures.

### 7. Uniform CLI validation

- `plan` validates the bundle and TargetSnapshot.
- `guides` validates SeedSpec and SourceManifest.
- `stage` has an explicit tested policy for blocked plans.
- Reports include package, contract, review, SeedSpec and snapshot provenance.
- No command writes to the target.

### 8. Snapshot privacy and scope

- Add a reviewed exclusion policy for repository metadata, generated/vendor
  trees, environment-specific files and operator-withheld paths.
- Record safe exclusion reasons without reading or exposing excluded content.
- Add no-leak fixtures.

### 9. Evidence and packaging

- Replace the deprecated license table with an SPDX string.
- Rerun wheel/sdist and clean-environment CLI proof.
- Label evidence as repository-contained local until hosted CI exists.
- Record exact commit/package versions and invalidated prior evidence.

## Required Tests

At minimum:

```text
forged snapshot hash;
duplicate snapshot path;
symlink and case collision;
excluded-path handling;
unreadable text candidate;
unbound SeedSpec hashes;
wrong compiler compatibility;
ProjectModel source reference not present in SourceManifest;
blocked plan staging;
different target snapshots with identical plan items;
extra Reference Seed output;
valid .repokernel-only project audit;
source audit with failing contract conformance.
```

## Required Return

Create:

```text
process/reviews/RK-RVW-20260625-01/CODEX_RETURN_CORRECTION.md
```

Include:

```text
exact commit and package version;
files changed;
fixture/parity summary;
commands and actual outputs;
clean-install evidence;
remaining deviations;
confirmation that Track B and the pilot were not executed;
request for final GPT Pro Track A readback.
```

## Exit Gate

Track B remains blocked until:

```text
critical corrections pass;
GPT Pro marks the correction commit accepted_for_private_pilot;
operator authorizes Track B against that exact version;
pilot version lock is updated.
```
