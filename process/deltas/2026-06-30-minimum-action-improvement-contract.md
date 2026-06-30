# Minimum-Action Improvement Contract Delta

date: 2026-06-30
status: accepted documentation/governance delta

## Trigger

The operator clarified that all experiences should be usable for improving the
larger system, but that improvement must follow a minimum-action logic: reduce
entropy and noise, increase clarity and avoid file accumulation.

## Change

Added a neutral RepoKernel governance contract:

```text
docs/minimum-action-improvement-contract.md
```

Updated:

```text
docs/guides/operational-procedure.md
docs/guides/evolution-versioning-and-review-loop.md
docs/repokernel-promotion-rules.md
sources/bootstrap/SOURCE_ATLAS_v1.0.md
process/DECISION_LOG.md
```

## Resultant

Experience-driven improvement now has an explicit A1 gate:

```text
experience
-> source and authority classification
-> surface and owner classification
-> tension report
-> expected improvement
-> minimum useful artifact
-> review gate
-> receipt
```

If no next action changes, the correct result is `no_cycle`.

## Boundary

This delta does not enable:

```text
apply;
runtime;
background hooks;
Seed/THIA/Lab promotion;
downstream mutation;
external writes;
public readiness claims.
```

Downstream-system lessons may become RepoKernel rules only after neutralization
and owner-boundary classification.

## Validation

```text
repokernel-source audit must remain ready;
Markdown references must resolve through the Source Atlas;
no code/runtime behavior changed.
```
