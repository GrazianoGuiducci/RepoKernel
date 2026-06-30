# First Contact Preview And Hook Clarity

date: 2026-06-30
status: active_delta

## Trigger

Operator clarified that RepoKernel must not imply hooks are unavailable or only
future in every system. RepoKernel does not activate hooks by default, but an
external host may use hooks, skills or runtime adapters if that host owns the
lifecycle and authority model.

The operator also noted that users may need a safe local preview before they
trust RepoKernel near real work.

## Change

Added:

```text
docs/first-contact-preview.md
```

Updated:

```text
docs/integration-surfaces.md
docs/guides/coder-first-evaluation-flow.md
docs/guides/external-assistant-playbook.md
docs/agentic-feedback.md
README.md
```

## Rule

RepoKernel provides contracts and staged evidence. Host systems decide how to
activate it. Coder-facing onboarding should offer a safe preview path before
integration when the user needs trust or understanding.

## Boundary

No hook, runtime, background automation, target write, public claim, adjacent
repo import or feedback submission is authorized by this delta.
