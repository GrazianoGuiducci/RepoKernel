# Integration Surfaces And Agentic Feedback

date: 2026-06-30
status: applied_locally_pending_validation

## Trigger

Operator asked whether RepoKernel now explains how to integrate in many
different contexts and whether agentic systems can leave useful feedback.
TM3/TM7-vps proposed a structured public-safe agentic feedback channel from a
clean contribution lane.

## Change

```text
docs/integration-surfaces.md:
  maps human read, coder guide, repo instructions, skills, CLI diagnostics,
  staged preview, hooks, non-development workflows and custom agentic systems.

docs/agentic-feedback.md:
  defines public-safe structured feedback from AI coding assistants and
  agentic systems.

.github/ISSUE_TEMPLATE/agentic-system-feedback.md:
  provides a GitHub issue template for feedback triage.

process/agentic-feedback/2026-06-30-tm9-codex.md:
  records local TM9 Codex feedback from the integration/cold-run experience.
```

## Boundary

No hook, runtime, apply command, target write, publication, provider call,
credential handling, downstream project mutation or public readiness claim is
activated by this change.
