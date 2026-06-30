# Update And Adoption Guide

Status: coder-facing update path

## Purpose

This guide tells a coder or external agent how to discover new RepoKernel
capabilities and decide whether a local installation or Project Kernel should
receive an update.

RepoKernel does not assume a universal updater. The base model is:

```text
coder enters repository
-> reads update signals
-> compares local state
-> proposes adoption only when useful
-> waits for owner gate before mutation
```

## Read Order

Use this order when checking for updates:

```text
README.md
CHANGELOG.md
CAPABILITIES.md
CURRENT_STATE.md
docs/compatibility-matrix.md
selected capability documentation
```

## Room-Start Update Awareness

When a coder, coding assistant or agentic system starts a new room/session
inside a project that uses RepoKernel, a generated Project Kernel or a D-ND
skill/repository, it should perform a short update-awareness check before
planning work.

This is a memory and orientation step, not an automatic update mechanism:

```text
new room/session starts
-> identify installed RepoKernel/skill source and local revision if available
-> read CHANGELOG.md, CAPABILITIES.md or the skill source-authority section
-> decide whether new upstream capability matters for the current project
-> choose ignore, explain, propose, stage or adopt
-> ask for owner gate before mutation
```

If the local system supports hooks, boot scripts or skill-load callbacks, it
may use them to remind the coder to perform this check. RepoKernel does not
assume those mechanisms exist and does not require a universal hook runtime.

For generated Project Kernels, also read:

```text
.repokernel/state/CURRENT_STATE.md
.repokernel/sources/SOURCE_ATLAS.md
.repokernel/deltas/README.md
.repokernel/skills/<project>-semantic-kernel/SKILL.md
```

## Compare Installed State

Record:

```text
installed_source_revision:
installed_package_version:
installed_capabilities:
local_project_kernel_version:
local_modifications:
target_owner:
authority_mode:
```

If the local installation cannot identify its version or source revision, do
not patch blindly. Propose a version-discovery or re-staging step first.

## Adoption Decisions

Use one of these outcomes:

```text
ignore:
  capability is irrelevant or too costly for the local project.

explain:
  describe the update to the user without changing files.

propose:
  prepare an UpdateCandidate with owner, source, gate and validation.

stage:
  render a preview in an external review directory.

adopt:
  only after explicit owner gate, validation and receipt.
```

## UpdateCandidate Shape

```text
capability_id:
source_revision:
local_revision:
target_project:
why_relevant:
minimum_artifact:
owner:
gate:
validation:
receipt:
do_not_do:
```

## Boundaries

Do not:

```text
auto-pull and apply changes;
overwrite local Project Kernel files;
copy all RepoKernel skills into a target;
install hooks because a capability mentions hooks;
activate runtime behavior;
publish public claims;
read secrets, logs or private source material to check versions;
```

RepoKernel updates are meaningful only when they improve a next action,
prevent a repeated error or clarify a boundary for the selected project.
