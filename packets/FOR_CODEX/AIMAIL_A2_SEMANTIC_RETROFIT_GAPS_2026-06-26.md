# AIMAIL A2 Semantic Retrofit Gaps

date: 2026-06-26
status: accepted_for_track_a_patch_scope
source: AIMAIL A2 no-write diagnostic

## Purpose

Use the AIMAIL A2 no-write diagnostic to improve RepoKernel without expanding
authority.

RepoKernel passed the safety proof:

```text
contract validation: passed
bundle validation: passed
fresh snapshot planning: passed
stage outside target: passed
target_writes_performed: []
before/after tracked target hash: equal
```

It did not yet pass the usefulness bar for semantic retrofit:

```text
planner output was still too generic;
ProjectModel assertions did not materially shape generated state/source files;
root AGENTS.md and README.md proposals looked like replacement templates;
inspect artifacts became noisy when a target contained local node_modules;
snapshot root path is useful locally but too raw for review/public packets.
```

## Authorized Patch Scope

Allowed:

```text
planner semantic content quality;
ProjectModel-aware generated .repokernel files;
more conservative root adapter proposals;
compact exclusion summaries in TargetSnapshot;
tests using an AIMAIL-like fixture;
docs/state updates for this patch.
```

Blocked:

```text
apply command;
target writes;
runtime/daemon;
network service;
external automation;
provider/email/TTS/local model work;
public readiness claims;
Seed promotion.
```

## Acceptance Criteria

```text
1. CLI plan passes ProjectModel into the planner.
2. Generated .repokernel/state/CURRENT_STATE.md includes mission/product,
   verified/inferred assertions, boundaries and unknowns from ProjectModel.
3. Generated .repokernel/sources/SOURCE_ATLAS.md includes source references
   from ProjectModel instead of only generic README/current-state rows.
4. Root AGENTS.md and README.md proposed updates are explicitly review-only
   adapter deltas, not authoritative replacement copy.
5. Snapshot excludes vendor/build trees compactly enough that node_modules does
   not produce hundreds of excluded path entries.
6. Tests prove an AIMAIL-like ProjectModel changes semantic output without
   granting write authority.
7. Existing no-write/stage behavior remains unchanged.
```

## Next Review

After implementation, run the unit suite and optionally repeat the AIMAIL A2
diagnostic to confirm that the staged output is materially better while still
not writing to AIMAIL.
