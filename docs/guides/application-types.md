# RepoKernel Application Types

## New Repository

RepoKernel can generate the first project kernel.

## Existing Repository

RepoKernel observes first. Existing files remain authoritative. Proposed
changes are classified as:

```text
create
leave_unchanged
propose_update
conflict
withhold
```

## Knowledge Workspace

RepoKernel can organize documents, research, source atlases, memory deltas and
guide projections even when the target is not mainly code.

## Multi-Repo System

Deferred. Future constellations should reference local Project Kernels rather
than merge them into one global state.

## Public/Private Split

RepoKernel can support guides or projections that include only public-safe
sources. A source must be marked `privacy: public` and explicitly include
`public_guide` in `used_for` before it can appear in a public guide. Private,
internal or withheld sources must not leak into public guides.
