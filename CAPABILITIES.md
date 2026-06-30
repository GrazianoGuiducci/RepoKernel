# RepoKernel Capabilities

This file is the first place a coder or external agent should check to see
which RepoKernel capabilities exist and whether a local installation or Project
Kernel should consider an update.

Capabilities are proposals until the local owner accepts them.

## Active Capability Index

| Capability | Status | Added | Use when | Adoption |
| --- | --- | --- | --- | --- |
| Project Kernel staging | active | 0.3.0.dev0 | a project needs current state, source atlas, packets, local skill, evidence, deltas and review gates | staged preview only |
| Minimum-action improvement contract | active | 0.3.0.dev0 | a correction or signal may become durable project memory | propose delta/rule/skill candidate |
| Clarity cleanup cycle | active | 0.3.0.dev0 | dirty or unclear files reduce action clarity | classify first, no destructive cleanup |
| Coder-first evaluation flow | active | 0.3.0.dev0 | a coder is evaluating RepoKernel for a user | explain/read/diagnose/stage before write |
| Public capability source pass | candidate | 0.3.0.dev0 | a target project may benefit from public neutral sources after audit | recommendation only |
| Agentic feedback channel | candidate | 0.3.0.dev0 | external AI systems can report installation or evaluation friction | public-safe feedback only |
| Metaskill propagation contract | candidate | 0.3.0.dev0 | a reusable invariant emerges in one surface and may need project-local adoption | owner/source/gate/validation/receipt required |

## Update Reading Rule

When a coder enters RepoKernel to update or evaluate an installation:

```text
README.md
-> CHANGELOG.md
-> CAPABILITIES.md
-> docs/update-and-adoption.md
-> selected capability doc
```

When a coder or agentic system starts a new room/session in a project that
uses RepoKernel, a generated Project Kernel or one of the related D-ND
skills/repositories, it should first check whether the source has newer
capabilities relevant to the current project. This check may be triggered by a
manual boot habit, a local skill rule, a project boot file or a hook in systems
that support hooks. It is still only an awareness step until the owner approves
an adoption.

Then produce one of:

```text
ignore:
  update is irrelevant to the local project.

explain:
  tell the user what changed and why it matters.

propose:
  prepare an UpdateCandidate; do not mutate.

stage:
  generate a reviewable staged preview outside the target.

adopt:
  only after owner gate, validation and receipt.
```

## Boundary

Do not infer auto-update authority from this file. A new capability is not a
request to patch every project, adapter, hook or runtime.
