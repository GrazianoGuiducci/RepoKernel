# Interrupted Session Reentry

Date: 2026-06-26
Status: accepted documentation delta

## Trigger

A live operator workflow exposed a continuity gap: an AI session may stop
abruptly after reading or partially acting on a prior packet, review response
or runtime surface. The next session needs a neutral way to recover without
trusting chat memory or repeating side effects.

## Rule

Previous-instance transcripts, compaction snapshots and handoff notes are
reentry inputs. They are not current authority until reconciled with:

```text
CURRENT_STATE
FIRST_PACKET or active packet
SOURCE_ATLAS or source manifest
git branch and head
dirty or untracked work
the real external target surface, when a side effect is claimed
```

If these sources disagree, produce a recovery report and stop before
implementation.

## Secret Boundary

Scheduler, service, environment and log output can leak credentials even when
the command is read-only. Any such stream copied into chat, packets or reports
must be filtered or summarized so raw secrets and tokens are not exposed.

This redaction rule does not authorize reading secrets. It only limits leakage
when a specific operation already requires inspecting sensitive-adjacent output.

## Updated Surfaces

```text
docs/recovery-procedure.md
docs/context-surface.md
docs/codex-operating-guide.md
```
