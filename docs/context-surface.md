# Context Surface

Status: replaced during Phase 0 cleanup.

RepoKernel does not treat context as a vague memory dump. A context surface is
the smallest project-readable layer that lets a future AI/operator session know
where it is, which sources matter and what action is allowed next.

## Minimal Surface

```text
entry gate
current state
source atlas or source manifest
active packet
boundary
evidence
memory delta
```

For the current source repository, the root files remain compatibility
adapters until the self-hosted `.repokernel/` plane is introduced in a later
accepted phase.

## Reentry Inputs

Crash transcripts, compaction snapshots, previous-instance files and operator
handoff notes can help reconstruct position. They are reentry inputs, not
standalone authority.

Before acting from a reentry input, compare it with:

```text
current state
source atlas or manifest
active packet
git branch and head
dirty or untracked work
relevant external surface, if any side effect is claimed
```

If these disagree, the next action is a recovery report, not implementation.

## New Repository

A new project kernel may receive root-level adapters such as `AGENTS.md` and
`CURRENT_STATE.md` when that host expects them. The generated kernel must still
preserve source authority, boundaries and validation criteria.

## Existing Repository Retrofit

An existing repository keeps its own structure first. RepoKernel observes it,
maps authority, proposes the smallest compatible overlay and stops before
conflicting writes.

Default retrofit namespace:

```text
.repokernel/
  manifest.json
  state/
  sources/
  packets/
  evidence/
  deltas/
  skills/
  plans/
  reports/
```

Root files are adapters, not competing truth, unless the target repository
explicitly accepts them.

## Boundary

Context surfaces do not grant autonomy, publication, deployment, network,
secret access or cross-repository authority. They only make the next action
legible and reviewable.
