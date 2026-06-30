# RepoKernel User Guide

Use RepoKernel when a project needs continuity across AI sessions, coders,
documents, tools or repositories.

## If You Are Asking An Assistant

If you are asking a coding assistant what RepoKernel is useful for, ask for a
read-only explanation first. The assistant should explain the value, current
limits and likely first safe step before cloning, inspecting or staging
anything.

Useful first request:

```text
Read the RepoKernel docs and tell me whether it is useful for my project.
Stay read-only and ask before cloning or running diagnostics.
```

Assistant-facing guidance lives in
[`external-assistant-playbook.md`](external-assistant-playbook.md).

## Choose A Mode

Direct Start creates a new kernel. Synthesis compiles from intent and sources.
Retrofit observes an existing repository and proposes compatible additions.
A1 observe-and-propose inspects without writes.

Phase 1 can also stage a reviewed `GenerationPlan` into a separate empty
directory so you can inspect proposed files without touching the target
repository.

## What You Get

```text
L0: entry gate, current state, first packet
L1: semantic kernel and source atlas
L2: evidence, deltas, registry and governed improvement
L3: runtime contract only, not executable by default
```

The project kernel lives primarily in `.repokernel/`. Root files are only
adapters or ordinary project files when the host needs them.

## What Requires Approval

```text
writing to a target repo
overwriting or modifying existing files
publishing
deploying
using network or credentials
promoting to Seed
enabling runtime behavior
```

## Feedback

After trying RepoKernel, please consider leaving a short privacy-safe note using
`docs/feedback.md`. The most useful feedback says what the kernel helped with,
where the guide or installer was unclear and what would make the next use
safer or easier.
