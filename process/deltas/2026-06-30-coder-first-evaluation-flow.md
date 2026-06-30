# Delta: Coder-First Evaluation Flow

date: 2026-06-30
status: active

## Trigger

The operator clarified that RepoKernel speaks more to the coder/agent than to
the end user. A coder may arrive only to evaluate the repository, may not yet
understand it and may need to produce the best explanation and next steps for
the user across Codex, Claude Code, OpenCode or another agentic system.

## Decision

Add a coder-first evaluation flow that orients the assistant runtime before it
speaks or acts.

## Change

```text
added:
  docs/guides/coder-first-evaluation-flow.md

updated:
  README.md
  docs/guides/README.md
  docs/guides/user-guide.md
  docs/guides/use-cases.md
  docs/guides/external-assistant-playbook.md
  sources/bootstrap/SOURCE_ATLAS_v1.0.md
  process/DECISION_LOG.md
  CURRENT_STATE.md
```

## Preserved Rule

```text
RepoKernel first contact is a dual-audience event:
  user needs a clear value explanation;
  coder needs runtime, authority, fit mode and next safe action.
```

## Boundary

The new guide does not authorize clone, private folder reading, diagnostics,
staging, writes, apply behavior, automation, public claims or installation.
Each stronger action still requires explicit user consent and a runtime
capability check.

## Next Safe Action

Use `docs/guides/coder-first-evaluation-flow.md` before the external assistant
playbook when the assistant/coder is not already familiar with RepoKernel or is
only evaluating it for a user.
