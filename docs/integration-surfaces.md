# Integration Surfaces

status: active_guidance

RepoKernel can enter a project through several surfaces. Do not assume one
host, one IDE, one language, one installer or one automation model.

## First Rule

Integration is selected by the target context.

```text
RepoKernel does not activate itself.
RepoKernel does not grant hooks, skills, writes or runtime authority.
RepoKernel provides contracts, diagnostics, plans and staged review output.
```

## Possible Integration Surfaces

| Surface | Use when | Boundary |
| --- | --- | --- |
| Human read | The user only wants to understand the method | No commands, no project inspection |
| Coder guide | Codex, Claude Code, OpenCode, Cursor or another coder needs orientation | Read docs first; no target write |
| Repository instructions | The target accepts AGENTS/CLAUDE/IDE instruction files | Merge by review; preserve existing authority |
| Project-local skill | The target runtime supports skills or capability folders | Skill describes behavior; it does not grant tools |
| CLI diagnostic | The user allows no-write inspect/audit/plan | Read-only or external staging only |
| Staged preview | The project may benefit from generated continuity files | Output goes outside target; read `REVIEW_ME_FIRST` |
| Hook or automation | A mature host wants pre-action or post-action gates | Contract only until explicitly implemented and tested |
| Non-development workflow | Business, research, editorial or operations work needs continuity | Use state, sources, decisions, evidence and next action; no code assumption |
| Agentic system | A custom runtime wants to adopt the pattern | Map read/propose/stage/write/publish authorities first |

## Activation Ladder

Use the lowest useful activation:

```text
A0 explain only
A1 read-only assessment
A2 no-write diagnostic
A3 external staged preview
A4 reviewed target integration
A5 host-specific hooks or runtime automation
```

Current RepoKernel is designed for A0-A3. A4 requires explicit project review.
A5 is future work and must be host-specific.

## Skill Or Hook?

Use a skill when the host needs reusable reasoning instructions:

```text
read current state;
respect source authority;
classify unclear files;
propose memory deltas only when useful;
stop before target writes.
```

Use a hook only when the host has a stable, explicit lifecycle event:

```text
before action;
before write;
after command;
before commit;
before publish;
session close/reentry.
```

Hooks are not the default. A weak hook adds noise and can create false
authority. Start with docs, staged output and receipts.

## Non-Development Use

RepoKernel is not only for software. The same kernel shape can support:

```text
business decisions;
research notes;
editorial workflows;
model/data assumptions;
monitoring and prediction notes;
opportunity discovery;
operational folders;
agentic workspaces.
```

For non-development contexts, translate code terms into functional terms:

```text
source files -> authoritative sources
tests -> validation checks
commits -> accepted decisions
issues -> open questions or tasks
skills -> reusable procedures
hooks -> workflow checkpoints
```

## Integration Receipt

Every integration should preserve:

```text
target:
runtime:
mode:
sources_read:
authority:
files_or_surfaces_proposed:
what_remains_untouched:
review_gate:
next_safe_action:
feedback_path:
```

## Boundary

This guide does not authorize apply behavior, background automation, target
writes, hook activation, public claims, credential handling, provider calls,
deployment or cross-repository mutation.
