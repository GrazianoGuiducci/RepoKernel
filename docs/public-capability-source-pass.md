# Public Capability Source Pass

status: active_design_candidate
updated: 2026-06-30

## Purpose

RepoKernel can optionally inspect public, neutral capability repositories after
the target project audit and before generating or regenerating a Project
Kernel.

The pass answers one question:

```text
Which public capabilities are relevant to this project, and how should they be
made visible without installing or copying them automatically?
```

## Position In The Flow

```text
target project request
-> consent and source boundary
-> read-only target audit
-> optional public capability source pass
-> capability fit report
-> reviewed GenerationPlan
-> external staging
-> human review gate
```

This pass does not replace target audit. It runs only after the project need,
domain, source authority and read boundary are clear.

## Allowed Sources

Initial public source allowlist:

| Source | Public role | Use when |
| --- | --- | --- |
| `GrazianoGuiducci/d-nd-ux-ai-seed` | Agentic UX Seed | The target needs workspace shells, panels, modals, navigation, assistant UI, dense dashboards or agent-readable interface orientation. |
| `GrazianoGuiducci/d-nd-seed` | Portable AI coder operating substrate | The target needs boot/reentry discipline, runtime profiles, hooks, guardrails, skill routing or governed self-improvement rules. |
| `GrazianoGuiducci/D-ND_LAB` | Research/lab cycle reference | The target needs domain research cycles, evidence reports, falsifiers, repeatable experiments or lab-style orchestration. |
| `GrazianoGuiducci/KPhi1-EN` | Legacy cognitive kernel reference | The target needs historical architecture ideas, skill categories, axioms or cognitive-kernel patterns, but not current runtime authority. |

Each source must be treated as public documentation and capability evidence,
not as automatic install authority.

## Output Object

The pass should produce a target-specific capability fit report:

```text
target_project:
target_domain:
target_need:
sources_read:
capability_candidates:
  - capability:
    source_repo:
    source_ref:
    why_relevant:
    maturity:
    suggested_use:
    required_gate:
    install_or_copy:
    risk_or_boundary:
rejected_or_deferred:
  - source_or_capability:
    reason:
recommended_next_step:
```

## Capability Decisions

Use one of these decisions for each candidate:

```text
include_as_reference:
  mention the capability in the Project Kernel as a useful source to read.

stage_adapter:
  stage local instructions or adapter notes outside the target for review.

defer:
  useful later, but not needed for the first Project Kernel.

reject:
  not relevant, too broad, too immature or too risky for this target.
```

Do not use:

```text
auto_install
auto_copy
auto_mutate_target
auto_enable_hooks
auto_publish
```

## Source Handling Rules

```text
pin source:
  record repository URL and commit/ref when used for a staged recommendation.

separate public from private:
  use public repo content only unless the operator explicitly authorizes a
  local/private source.

preserve target authority:
  the target project remains source of truth for its own domain and constraints.

smallest useful capability:
  recommend only what helps the target's next action.

no THIA state transfer:
  public THIA-derived capabilities may be referenced; private THIA runtime
  state, secrets, local memory and unpublished internal logic must not travel.
```

## Example Mapping

```text
If the target is an AI workbench UI:
  d-nd-ux-ai-seed may provide workspace shell and assistant surface patterns.

If the target is a coding-agent environment:
  d-nd-seed may provide runtime profile, boot and guardrail patterns.

If the target is a domain research project:
  D-ND_LAB may provide cycle structure and report/falsifier patterns.

If the target needs cognitive architecture references:
  KPhi1-EN may provide legacy kernel/skill taxonomy inspiration only.
```

## Boundary

This pass is read-only and recommendation-only. It does not grant RepoKernel
authority to clone private repositories, install Seed, copy UX components,
run Lab cycles, activate hooks, mutate the target project or publish external
claims.

## First Implementation Shape

The first implementation should be documentation and staged reports only:

```text
docs/public-capability-source-pass.md
optional capability-fit-report fixture
future schema only after repeated use proves the object shape
future CLI option only after report semantics stabilize
```
