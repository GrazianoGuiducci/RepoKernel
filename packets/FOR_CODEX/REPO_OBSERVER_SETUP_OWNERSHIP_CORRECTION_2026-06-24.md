# Repo Observer Setup Ownership Correction

date: 2026-06-24
status: Phase 0 classification note
authority: documentation/classification only

## Correction

`dnd-repo-observer-setup` is not canonically a Business Manager function.

Its operational nucleus belongs to RepoKernel:

```text
external repo or project evidence
  -> read-only observation
  -> ProjectModel-like understanding
  -> L0/L1/L2 setup proposal
  -> review gate
  -> no writes unless separately authorized
```

This matches RepoKernel A1 `observe_and_propose` and the retrofit path more
closely than it matches outreach, contact management or offer framing.

## Correct Ownership

```text
canonical_owner: RepoKernel A1 observe_and_propose / retrofit adapter
business_owner: Business Manager only for relationship, call, offer and follow-up routing
seed_owner: none yet; future candidate only after stable L0-L2 evidence
```

Business Manager may keep an adapter copy because first contacts, clients,
partners and creators are often the entry channel. That copy must not imply
that Business Manager contains full RepoKernel functionality.

## RepoKernel Function

RepoKernel is a compiler/generator for project-specific kernels, not merely a
folder scaffold.

Current architecture:

```text
intent + documents + repository state + constraints
  -> source intake
  -> ProjectModel
  -> reviewed SeedSpec
  -> file plan / retrofit overlay
  -> validated Project Kernel
```

The target output is not another clone of the RepoKernel source repository. It
is a local project control plane: reentry, state, source atlas, semantic kernel,
evidence, review gates, memory deltas and optional runtime contract.

## Autological And Combinator Mapping

Autological elements:

```text
the system observes its own operation;
friction/correction becomes explicit evidence;
evidence becomes a bounded proposal;
accepted deltas update the local kernel without self-approving promotion.
```

Combinator elements:

```text
sources + state + skills + tools + faculties + gates + target authority
  -> selected capability assembly
  -> ResultantPacket or setup capsule
  -> reviewed action boundary
```

This means `dnd-repo-observer-setup` should remain an observer/proposer until
RepoKernel proves the A1 cycle, then can be evaluated as a RepoKernel adapter
or Reference Seed candidate.

## Boundaries

Do not:

```text
move this directly into d-nd-seed;
claim RepoKernel is already integrated into Business Manager;
write to third-party repositories from a contact note;
promote the adapter before Phase 0 and post-Phase-0 convergence gates;
let one process observe, propose, implement, evaluate and promote itself.
```

## First Safe Use

Use Denis Craciun's public repositories only as a consensual pilot candidate:

```text
ask him to choose one repo/use case;
observe direct repo evidence;
produce a setup capsule;
propose the smallest useful L0/L1/L2 overlay;
stop before writes, PRs, Seed install or product claims.
```

