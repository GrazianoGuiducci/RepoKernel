# Codex Operating Guide

When working in a RepoKernel project:

1. Read `AGENTS.md`.
2. Read `CURRENT_STATE.md`.
3. Read the relevant `skills/*/SKILL.md`.
4. Verify the target file or repository state before editing.
5. Make the smallest useful change.
6. Run the relevant audit or tests.
7. Update current state only when the active surface, boundary, source of truth or next action changes.

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

