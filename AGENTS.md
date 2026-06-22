# RepoKernel Agent Gate

This repository defines the RepoKernel pattern: AI-readable repositories for long-running projects.

Before editing, read:

```text
CURRENT_STATE.md
docs/claim-boundaries.md
docs/skill-repo-lifecycle.md
skills/repokernel-semantic-kernel/SKILL.md
```

## Operating Rule

Work from current state and explicit sources, not from chat memory alone.

Use these labels when reasoning:

```text
source
accepted rule
inference
hypothesis
verified external fact
to verify
residue
```

## Allowed Work

You may:

- improve public-safe docs and templates;
- create candidate scripts and examples;
- propose skill lifecycle rules;
- prepare packets for review;
- update `CURRENT_STATE.md` when the active state, boundary or next action changes.

## Confirmation Needed

Ask before:

- publishing or pushing to a new remote;
- changing license or external claims;
- adding private project material;
- promoting anything to another repository or package;
- deleting source files or examples.

## Memory Delta

Preserve only useful deltas: durable decisions, accepted corrections, source promotions, boundaries, residue not to follow and first safe next actions. Do not store raw chat, credentials, private logs or temporary speculation.

