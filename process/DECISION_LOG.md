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
