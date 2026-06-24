# RepoKernel Phase 1 External Review Request For GPT Pro

date: 2026-06-24
status: ready_to_send_to_gpt_pro
target_repo: https://github.com/GrazianoGuiducci/RepoKernel
current_commit: 8942874

## Copy/Paste Request

You are acting as an independent external reviewer for RepoKernel.

Please inspect the public repository:

```text
https://github.com/GrazianoGuiducci/RepoKernel
```

Focus on the current Phase 1 state around commit:

```text
8942874 feat: add phase 1 core planner and guides
```

RepoKernel is intended to become a host-neutral Project Kernel compiler:

```text
authorized sources + project intent
-> SourceManifest
-> ProjectModel
-> reviewed SeedSpec
-> deterministic GenerationPlan
-> dry-run / reviewed application
-> ActivationReport
```

It must support both internal D-ND use and external users. The external user
should not need to understand the whole D-ND system to use RepoKernel safely.

## Current Scope

Phase 1 has intentionally implemented only the core:

```text
src/repokernel/
schemas/
docs/guides/
tests/unit/
```

The current core includes:

```text
canonical JSON serialization and hashing;
minimal contract validators;
path safety;
SeedSpec -> GenerationPlan planner;
dry-run apply report;
guide projection helper;
JSON schema surfaces;
user/coder/architecture/use-case guides;
unit tests.
```

Current local validation:

```text
8 unit tests pass.
phase0_inventory reports 113 tracked files, 0 unclassified, 0 broken links.
repokernel-source audit returns ready true / readiness L2.
git diff --check passed before commit.
```

## Non-Negotiable Boundaries

Do not recommend turning Phase 1 into:

```text
runtime implementation;
autonomous agent loop;
network service;
Seed promotion;
multi-repo orchestrator;
domain pack marketplace;
automatic writes to target repositories;
automatic PR/issue creation;
credential or secret handling;
public claims that RepoKernel is production-ready before evidence.
```

You may propose those as future/deferred layers only if you keep them clearly
outside the Phase 1 core.

## Review Goals

Please produce a rigorous review in these sections.

### 1. Architecture Review

Evaluate whether the current architecture is coherent:

```text
SourceManifest
ProjectModel
SeedSpec
GenerationPlan
ActivationReport
SkillRegistry
GuideSet
```

Check whether these are enough for:

```text
Direct Start;
Synthesis from intent/documents;
Existing Repository Retrofit;
A1 observe-and-propose;
future Reference Seed reproducibility.
```

Identify missing contracts, over-specified parts, naming problems and
misleading abstractions.

### 2. Safety And Authority Review

Evaluate whether the repo protects:

```text
no silent overwrite;
source documents as data, not instruction authority;
unknown namespaced extensions cannot raise authority;
private/withheld sources do not leak to public guides;
dry-run before application;
no self-approval;
clear separation between readiness, autonomy, authority and cognitive depth.
```

Suggest tests or schema constraints that would catch violations.

### 3. Core Code Review

Inspect:

```text
src/repokernel/canonical.py
src/repokernel/models.py
src/repokernel/paths.py
src/repokernel/planner.py
src/repokernel/guide_model.py
tests/unit/
schemas/
```

Look for:

```text
bugs;
weak validators;
missing negative tests;
non-determinism;
bad path handling;
planner behavior that could become unsafe;
places where schemas and Python validators diverge;
places where GuideSet can duplicate or distort authority.
```

### 4. Installer / CLI / Usage Modus Review

Design the next practical usage layer.

We need a clear flow for both users and coders. Please propose:

```text
recommended CLI commands;
minimum installer or package approach;
dry-run-first workflow;
how to inspect an existing repo;
how to produce a SeedSpec;
how to produce a GenerationPlan;
how to apply only after review;
how to generate/maintain guides;
how to run validation;
how to keep compatibility with current scripts until replacement.
```

Please distinguish:

```text
must build next;
should build later;
should not build yet.
```

### 5. Guide Review

Inspect:

```text
docs/guides/README.md
docs/guides/architecture.md
docs/guides/user-guide.md
docs/guides/coder-guide.md
docs/guides/use-cases.md
docs/guides/application-types.md
docs/guides/examples/minimal-project.md
README.md
docs/quickstart.md
```

The guides must serve both:

```text
external user: wants to understand what to do and when approval is needed;
coder: needs exact architecture, contracts, files, tests and boundaries.
```

Please recommend:

```text
missing guide sections;
better examples;
better diagrams or text flows;
better installation/use wording;
public-safe positioning;
which guide should be the first page for users;
which guide should be the first page for coders.
```

### 6. A1 Observe-And-Propose Review

Review:

```text
packets/FOR_CODEX/A1_OBSERVE_AND_PROPOSE_PROOF_PLAN.md
packets/FOR_CODEX/REPO_OBSERVER_SETUP_OWNERSHIP_CORRECTION_2026-06-24.md
```

Question:

```text
Is the A1 proof enough to reduce self-evaluation bias?
What fixture or external-style test would you add?
How should we evaluate RepoKernel on a real repo without writing to it?
What should the independent evaluator check?
```

### 7. External Use Readiness

Assess whether RepoKernel is ready for:

```text
private internal use;
trusted collaborator use;
public experimental use;
production use.
```

For each, state:

```text
ready / not ready;
why;
minimum blocker;
first safe improvement.
```

### 8. Concrete Improvement Plan

Please return a prioritized plan:

```text
P0: must fix before next test;
P1: must fix before external collaborator;
P2: should fix before public experimental use;
P3: later/future.
```

Each item should include:

```text
file(s);
problem;
proposed change;
test or acceptance criterion;
risk if ignored.
```

### 9. Optional Patch Suggestions

If you can propose direct improvements, provide patch-ready suggestions for:

```text
models.py validators;
planner.py;
guide_model.py;
schema files;
tests;
guide structure;
CLI/installer plan;
README/quickstart wording.
```

Do not provide broad rewrites without explaining the reason.

## Expected Output Format

Please answer with:

```text
executive verdict
architecture findings
safety/authority findings
core code findings
guide findings
installer/CLI recommendation
A1 proof improvements
external readiness table
prioritized P0/P1/P2/P3 plan
patch-ready suggestions
questions for the operator
```

Use clear severity labels:

```text
critical
high
medium
low
suggestion
```

## Important Evaluation Rule

Do not judge only whether the code passes its current tests. Judge whether the
tests are strong enough to prevent a weak generator, unsafe retrofit,
misleading guides or premature public claims.
