# AIMAIL A2 Semantic Retrofit Patch

date: 2026-06-26
status: local_validation_passed
packet: packets/FOR_CODEX/AIMAIL_A2_SEMANTIC_RETROFIT_GAPS_2026-06-26.md

## Purpose

Patch RepoKernel after the AIMAIL A2 no-write diagnostic proved safety but
exposed weak semantic retrofit quality.

## Changes

```text
planner:
  - CLI passes ProjectModel into build_generation_plan.
  - .repokernel/state/CURRENT_STATE.md now includes ProjectModel mission,
    product_or_result, assertions, boundaries and unknowns.
  - .repokernel/sources/SOURCE_ATLAS.md now includes ProjectModel source_refs
    and assertion lineage.
  - staged root AGENTS.md and README.md are explicit review-only adapter deltas,
    not replacement-oriented templates.

snapshot:
  - excluded directory trees such as node_modules are compacted.
  - excluded_summary is stored under extensions.repokernel.excluded_summary.
```

## Local Tests

```text
command: PYTHONPATH=src python -m pytest tests/unit -q
result: 47 passed
```

The Reference Seed distribution was regenerated through the compiler after
planner output changed.

## AIMAIL A2 Replay

Replay directory:

```text
C:\PVSC\ANTI_G\_repokernel_runs\aimail-a2-p21-20260626
```

No-write proof:

```text
before_hash: 98ff0a2ca39c831875a97fd517c2c5637d540ccf8866bf1b967a524b18aa1d97
after_hash:  98ff0a2ca39c831875a97fd517c2c5637d540ccf8866bf1b967a524b18aa1d97
equal: true
target_writes_performed: []
```

Semantic improvement observed:

```text
.repokernel/state/CURRENT_STATE.md includes AIMAIL mission, product,
policy/procedure assertions, Local Privacy Mode signal boundary, blocked
provider/send/backend/runtime actions and unknowns.

.repokernel/sources/SOURCE_ATLAS.md includes AIMAIL source refs and assertion
lineage.
```

Inspect compaction observed:

```text
excluded entries: 3
excluded_summary:
  build_artifact: 5
  repository_metadata: 587
  vendor_tree: 1814
```

## Remaining Limits

```text
This is still proposal/stage only.
No apply command was added.
No target repository write authority was added.
No public/alpha readiness claim is made.
Root adapter deltas still need human review before any future apply gate.
```

## Next Gate

Repeat the controlled AIMAIL A2 diagnostic only if the operator wants a fresh
record in AIMAIL. Otherwise, use this patch as evidence that RepoKernel moved
from mechanical no-write safety toward useful semantic retrofit.
