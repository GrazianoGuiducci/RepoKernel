# Retrofit Model

RepoKernel integrates into an existing repository by mapping and adapting its current structure. It does not clone itself over the project.

```text
read-only inventory -> authority map -> SeedSpec -> overlay plan -> review -> apply -> audit -> activation
```

Existing project files remain authoritative until an explicit reviewed change replaces them.

## Namespace And Adapters

For retrofits, the host-neutral state should default to:

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

Root files and host-specific directories are adapters. They are created or changed only when the selected host requires them and after conflicts are reviewed.

## Existing Entry Gates

When `AGENTS.md` or another agent instruction file already exists:

- preserve it as the active gate;
- classify its scope and authority;
- propose a minimal RepoKernel block or pointer;
- provide a diff-ready update rather than replacing the file;
- stop when existing canon and the proposed kernel contradict each other.

When no suitable entry gate exists, create the canonical gate under `.repokernel/` and optionally propose a short root adapter.

## Existing State

Do not create competing sources of truth.

If the project already has an authoritative state file, register it in the SeedSpec and manifest. If no suitable state exists, create `.repokernel/state/CURRENT_STATE.md`.

`README.md` remains a public or product surface. It may be used as an identity source, but it is not automatically rewritten for operational integration.

## Overlay Actions

Every path is classified as:

```text
create
leave_unchanged
propose_update
conflict
withhold
```

A `propose_update` item contains a rationale and reviewable patch. A `conflict` blocks application until resolved. `withhold` keeps material outside the emitted seed.

## Activation

The local Project Kernel becomes active only when:

- one authoritative state surface is registered;
- the selected host can read the entry gate or adapter;
- source references resolve;
- planned conflicts are resolved;
- approved changes match the target state;
- the selected readiness audit passes.

Activation does not imply publication, deployment, remote creation or stronger runtime authority.

## Resultant

```text
RepoKernel discovers the structure already present and compiles the smallest compatible kernel around it.
```
