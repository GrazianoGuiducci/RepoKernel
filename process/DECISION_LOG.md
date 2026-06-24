# Decision Log

## 2026-06-22 - RepoKernel As Primary Container

Decision: create `RepoKernel` rather than `d-nd-skill-lab`.

Reason: RepoKernel is broader than a skill lab. It contains the pattern that allows repositories to become readable, continuable and progressively improvable by AI systems.

Boundary: first-level public material must stay practical and public-safe.

## 2026-06-24 - Phase 0 Before Generator Completion

Decision: complete Phase 0 inventory and cleanup before implementing the final
compiler/generator.

Reason: RepoKernel is architecturally a Project Kernel compiler, but the
current generator is still a prototype. External or Seed-facing use requires a
clean baseline, zero unclassified tracked files, resolved evidence, link checks
and an accepted post-Phase-0 convergence resultant.

Boundary: no Phase 1 schemas, package skeleton, Seed promotion, runtime or
downstream repository mutation during this step.

## 2026-06-24 - Repo Observer Adapter Ownership

Decision: classify repo-observer setup as RepoKernel A1 observe-and-propose /
retrofit logic, with Business Manager acting only as relationship and offer
wrapper.

Reason: the method observes repository evidence, infers a project-kernel setup
need, proposes L0/L1/L2 overlays and stops before writes.

Boundary: no third-party writes, no Seed install and no claim that Business
Manager owns the compiler/generator logic.

## 2026-06-24 - Phase 1 Accepted For P0 Hardening Only

Decision: keep the Phase 1 package skeleton, schemas, planner and guides as the
active implementation surface, but block collaborator/public testing until P0
hardening is complete.

Reason: the independent GPT Pro review accepted the architectural direction and
identified concrete blockers: stale governance state, unsafe legacy quickstart
paths, weak schemas and validators, planner determinism gaps, path-safety gaps,
guide disclosure risks, audit overclaiming and missing CLI/installer strategy.

Boundary: GPT Pro review is treated as external evidence, not authority. Phase 1
continues under `packets/FOR_CODEX/PHASE1_P0_HARDENING_PACKET_2026-06-24.md`.
No external repository pilot, Seed promotion, runtime/L3 execution or public
installer claim is allowed before this gate passes.
