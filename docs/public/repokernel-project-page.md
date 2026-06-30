# RepoKernel Project Page Draft

status: draft_not_published
updated: 2026-06-30
surface: d-nd.com project page draft
publication_gate: operator_approval_required

## Page Frame

RepoKernel is an experimental no-apply generator for reviewable AI-readable
Project Kernels.

It exists to give new or existing projects a project-local continuity
structure: current state, source atlas, process packets, rules, skills,
evidence, memory deltas and reentry points. Instead of silently modifying a
target repository, RepoKernel validates authorized inputs, builds a
target-bound plan, stages proposed files outside the target and keeps human
review as the gate.

## What It Does

```text
authorized sources + project model
-> reviewed SeedSpec
-> validated TargetSnapshot
-> target-bound GenerationPlan
-> external staging directory
-> human review gate
```

Current capabilities:

```text
validate source and seed contracts;
inspect a target repository without writing to it;
build a deterministic generation plan tied to the target snapshot;
stage proposed project-kernel files outside the target repository;
generate public-safe guides;
describe project-local rules, skills and memory deltas;
run diagnostic audits;
verify the reference distribution.
```

## Why It Matters

AI-assisted development needs more than generated files. A project also needs a
visible record of:

```text
authorized sources;
project intent;
current state;
target evidence;
decision boundaries;
review gates;
project-local rules and skills;
memory deltas and reentry points;
blocked claims and future authority.
```

RepoKernel is a controlled experiment in making those elements explicit, so
useful interactions can become reviewed project memory before stronger
authority is granted to any automation.

## Current Status

```text
visibility: public repository
license: MIT
status: experimental diagnostic compiler
write authority: none
apply command: not present
runtime/daemon: not present
credential handling: not present
production readiness: blocked
public tester request: blocked
```

## Safe Evaluation Path

Use RepoKernel as a local experimental/research tool only:

```text
1. install in a development environment;
2. validate the example source manifest and seed spec;
3. inspect a non-sensitive target;
4. generate a plan;
5. stage proposed files outside the target repository;
6. review outputs manually;
7. keep any write-capable operation outside the current authority.
```

## What RepoKernel Is Not

RepoKernel is not currently:

```text
a production installer;
a runtime agent;
a daemon;
a credential manager;
a security boundary for private repositories;
an autonomous repository modifier;
autonomous project intelligence;
a public alpha for non-technical users;
a guarantee that a target project is safe or complete.
```

## Optional Public Capability Source Pass

After a read-only target audit, RepoKernel can optionally inspect public,
neutral capability sources and recommend which ones are useful for the target
domain.

Current candidate sources:

```text
GrazianoGuiducci/d-nd-ux-ai-seed:
  agentic UX workspace and assistant-interface patterns.

GrazianoGuiducci/d-nd-seed:
  portable AI coder substrate, boot/reentry rules, profiles and guarded
  capability routing.

GrazianoGuiducci/D-ND_LAB:
  domain research cycle, evidence report and falsifier patterns.

GrazianoGuiducci/KPhi1-EN:
  legacy cognitive-kernel architecture reference.
```

This pass is recommendation-only. It does not install, copy, activate hooks,
run Lab cycles or mutate the target project.

## Links

```text
GitHub repository:
https://github.com/GrazianoGuiducci/RepoKernel

Quickstart:
https://github.com/GrazianoGuiducci/RepoKernel/blob/main/docs/quickstart.md

Current limits:
https://github.com/GrazianoGuiducci/RepoKernel/blob/main/docs/pre-public-checklist.md

HTML overview:
https://github.com/GrazianoGuiducci/RepoKernel/blob/main/docs/overview.html
```

## Publication Rule

This draft is a source asset for later site work. It is not approval to publish,
deploy, create a subdomain, ask for public testers, or describe RepoKernel as
production-ready.
