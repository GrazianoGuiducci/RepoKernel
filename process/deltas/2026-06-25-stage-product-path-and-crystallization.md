# Delta - Stage Product Path And Crystallization Rule

date: 2026-06-25
status: active_delta

## What Changed

RepoKernel moved from a planner-only Phase 1 P0 surface toward a tester-safe
product path:

```text
validate-spec -> inspect -> plan -> stage -> guides -> audit
```

The new `stage` command renders a GenerationPlan into an explicit empty review
directory. It is not `apply` and does not write to the target repository.

The operator also corrected the operating method:

```text
crystallize whenever a work unit closes, an important assertion changes the
state of facts, or a compact/interruption is approaching.
```

## Why It Matters

RepoKernel is being built as the system that preserves project awareness while
the workspace is also using awareness to build it. That creates a recursion
risk: if state changes are not crystallized at each closure point, the next
session can confuse product work, business routing, Seed/THIA promotion and
local boot memory.

## Evidence

Verified locally after reentry:

```text
python -m pytest
  18 passed

PYTHONPATH=src python -m repokernel.cli audit --path . --profile repokernel-source
  ready: true

python scripts\phase0_inventory.py --root . --out process\reports
  tracked_file_count: 129
  unclassified_count: 0
  broken_links: 0

git diff --check
  no errors
```

Relevant changed surfaces:

```text
src/repokernel/staging.py
src/repokernel/cli.py
tests/unit/test_cli.py
examples/minimal/seed-spec.json
examples/minimal/source-manifest.json
README.md
docs/guides/*
process/evidence/LOCAL_VALIDATION.md
CURRENT_STATE.md
```

## Boundary

Allowed now:

```text
continue Phase 1 P0 productization;
verify the staged review-bundle path;
refine README/guides/tester instructions;
produce readiness verdict.
```

Not authorized by this delta:

```text
LinkedIn publication;
external tester request;
third-party repo writes;
apply command;
Seed/THIA/Lab promotion;
runtime/L3 execution;
commit/push without explicit operator gate.
```

## Residue Not To Follow

```text
Business Manager target-list route;
public product claims before readiness gate;
full D-ND theory as public explanation;
Seed/THIA/Lab integration as if already selected.
```

## First Safe Next Action

Finish the current RepoKernel productization loop in this order:

```text
1. keep the staged review path as the product center;
2. inspect README/guides for overclaim and missing tester commands;
3. produce publish | hold | private_pilot_first readiness verdict;
4. only then decide whether to refine the LinkedIn tester draft.
```
