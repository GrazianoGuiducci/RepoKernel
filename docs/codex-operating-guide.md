# Codex Operating Guide

When working in a RepoKernel project:

1. Read `AGENTS.md`.
2. Read `CURRENT_STATE.md`.
3. Read the relevant `skills/*/SKILL.md`.
4. Verify the target file or repository state before editing.
5. Make the smallest useful change.
6. Run the relevant audit or tests.
7. Update current state only when the active surface, boundary, source of truth or next action changes.

If resuming after an interrupted session, run the recovery procedure before
continuing any action described by the previous session. A previous response,
transcript or packet is evidence to reconcile with current files and git state,
not proof that the side effect happened.

## Output Discipline

Report:

```text
what changed:
where:
verification:
boundary:
next safe action:
```

Do not report private secrets, raw tokens or unrelated local state.

## Sensitive Streams

Operational output can leak secrets even when the command itself is read-only.
Before copying scheduler, service, environment, log or credential-adjacent
output into a chat, packet or report, pass it through a redaction filter and
report only the fields needed for the decision.

The filter does not authorize reading secrets. It only reduces leakage when a
specific operation already requires inspecting a sensitive-adjacent surface.
