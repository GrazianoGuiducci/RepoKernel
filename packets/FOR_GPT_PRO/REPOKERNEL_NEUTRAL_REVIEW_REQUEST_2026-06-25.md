# RepoKernel Neutral GPT Pro Review Request

date: 2026-06-25
status: draft_ready_for_operator_review
target: RepoKernel neutral architecture / product readiness
review_reference: latest pushed `main` commit containing this packet
prepared_from_local_head: 7ac6937 docs: add neutral GPT Pro review request
important_note: if the public GitHub repository does not show this packet or
the latest neutral commits, ask for the pasted source bundle instead.

## Purpose

Use GPT Pro as an independent high-capacity reviewer for RepoKernel while
keeping RepoKernel neutral, general and usable by anyone.

RepoKernel must not become specific to AIMAIL, D-ND internal operations, one
contact, one client, one repository, or one local workflow.

## Source Mode

Choose one before sending:

```text
A. Push current RepoKernel state, then give GPT Pro the GitHub URL and commit.
B. Do not push; paste the source bundle below into GPT Pro.
C. Hybrid: give public URL plus paste the changed/current files that are ahead
   of origin.
```

Recommended for now:

```text
A after the current documentation is pushed.
C only if the public repository is not yet updated.
```

## Copy/Paste Request

You are acting as an independent external reviewer for RepoKernel.

RepoKernel is intended to be a neutral project/kernel compiler and continuity
system for AI-assisted development. It should help a human or AI coder turn
authorized project sources into a reviewable project kernel without silently
overwriting target repositories.

Current intended flow:

```text
authorized sources + project intent
-> SourceManifest
-> reviewed SeedSpec
-> deterministic GenerationPlan
-> stage proposed files into an explicit review directory
-> generate public-safe guides
-> audit
-> human/operator gate before any future write-capable step
```

Current reference to review:

```text
Use the latest pushed `main` commit that contains:
- this packet;
- docs: add neutral GPT Pro review request;
- docs: remove contact-specific RepoKernel materials;
- feat: add staging review path.
```

If you inspect the GitHub repository and this commit is not visible, ask me for
the current local files or review the pasted source bundle instead.

## Non-Negotiable Boundaries

Do not recommend making RepoKernel:

```text
specific to AIMAIL or any single product;
specific to one contact/client/repository;
a runtime agent loop;
a network service;
a credential handler;
a background automation daemon;
a tool that opens PRs/issues automatically;
a system that writes to target repositories before a reviewed apply gate;
publicly production-ready before evidence supports it.
```

You may propose these as future layers only if clearly deferred.

## Review Through This Frame

Use a dual/non-dual review movement:

```text
1. Expand: identify hidden possibilities, architectural inversions, missing
   axes, safety gaps and product opportunities.
2. Contract: reduce them to concrete contracts, files, tests, CLI commands,
   guides and gates.
3. Resultant: produce the smallest coherent next plan.
4. Autological integration: state what RepoKernel should learn from this
   review and what durable rule/test/packet should exist afterward.
```

Keep this as an internal reasoning structure. The final output should be
concrete engineering/product review, not philosophical language.

## Source Bundle To Review

Core state and procedure:

```text
CURRENT_STATE.md
README.md
docs/quickstart.md
docs/guides/operational-procedure.md
docs/guides/cli-reference.md
docs/guides/private-review-brief.md
docs/guides/private-pilot-instructions.md
process/reports/distribution-readiness-2026-06-25.md
```

Core implementation:

```text
src/repokernel/
schemas/
tests/unit/
examples/minimal/seed-spec.json
examples/minimal/source-manifest.json
```

Existing prior GPT Pro review:

```text
packets/FOR_GPT_PRO/REPOKERNEL_PHASE1_GPT_PRO_INDEPENDENT_REVIEW_2026-06-24.md
```

## Review Goals

### 1. Neutrality And Generality

Evaluate whether RepoKernel is general enough for many projects and users.
Identify any remaining coupling to D-ND internals, AIMAIL, local TM9 workflow,
or private assumptions.

### 2. Architecture

Review whether these concepts are coherent and sufficient:

```text
SourceManifest
SeedSpec
GenerationPlan
ActivationReport
SkillRegistry
GuideSet
.repokernel/ control plane
```

Check whether the current architecture supports:

```text
new repository bootstrap;
existing repository retrofit;
A1 observe-and-propose;
future reviewed apply gate;
external user/coder usage without D-ND knowledge.
```

### 3. Safety And Authority

Evaluate:

```text
no silent overwrite;
no target writes during stage;
private/withheld source protection;
extension fields cannot raise authority;
root adapters vs .repokernel authority;
separation of readiness, autonomy, authority and cognitive depth;
one process cannot self-approve intent, action, evaluation and promotion.
```

### 4. CLI / Installer / Usage Path

Design the next practical user/coder path:

```text
install package;
validate source manifest;
validate seed spec;
inspect repo;
plan;
stage;
review;
guides;
audit;
future apply gate.
```

Classify:

```text
must build next;
should build later;
should not build yet.
```

### 5. Tests And Evidence

Identify missing tests and evidence for:

```text
path safety;
schema-validator consistency;
staging no-write behavior;
guide source leakage;
existing root file conflict handling;
repeatable minimal example;
external-style A1 proof without unsafe target writes;
public-readiness claims.
```

### 6. Public/Private Readiness

Assess readiness for:

```text
private internal use;
trusted collaborator review;
public experimental tester request;
production use.
```

For each, state:

```text
ready / not ready;
why;
minimum blocker;
first safe improvement.
```

## Expected Output Format

Return:

```text
executive verdict
neutrality findings
architecture findings
safety/authority findings
CLI/installer recommendation
guide and onboarding findings
test/evidence findings
external readiness table
prioritized P0/P1/P2/P3 plan
patch-ready suggestions
operator questions
```

Use severity labels:

```text
critical
high
medium
low
suggestion
```

Each P0/P1/P2/P3 item must include:

```text
file(s):
problem:
proposed change:
test or acceptance criterion:
risk if ignored:
```

## Evaluation Rule

Do not judge only whether current tests pass. Judge whether the tests and
guides prevent a weak generator, unsafe retrofit, misleading public claim or
premature apply/autonomy path.
