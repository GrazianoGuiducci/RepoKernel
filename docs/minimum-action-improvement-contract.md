# Minimum-Action Improvement Contract

Status: governance contract candidate for A1 observe-and-propose

## Purpose

Every observed experience can improve RepoKernel, but not every observation
deserves a new file, rule, hook or feature.

This contract defines how an external lesson, project run, reviewer comment,
operator correction, target-repository friction or downstream system signal can
be converted into a durable RepoKernel improvement without increasing noise.

## Core Rule

```text
An improvement is valid only when it removes more operational complexity than
it adds.
```

An accepted improvement should reduce at least one of:

```text
wrong-surface action;
reentry ambiguity;
review latency;
operator burden;
duplicate artifacts;
source confusion;
unsafe authority escalation;
unverified public claims;
future rework.
```

If the expected reduction is not clear, the correct result is `no_cycle`.

## Experience Intake

Use this sequence before turning an experience into a durable change:

```text
experience
-> source and authority classification
-> surface and owner classification
-> tension report
-> expected improvement
-> minimum useful artifact
-> review gate
-> receipt
```

### Source And Authority Classification

Classify the source before using it:

```text
operator correction;
local validation output;
independent review;
target-repository evidence;
downstream-system signal;
public external source;
private or withheld source.
```

Private, withheld or downstream-system material may influence internal
reasoning, but it must be neutralized before entering public RepoKernel docs,
fixtures, examples or public claims.

### Surface And Owner Classification

Classify where the improvement belongs:

```text
RepoKernel core contract;
RepoKernel documentation;
RepoKernel test or fixture;
process delta;
review packet;
portable promotion candidate;
downstream private system;
residue.
```

Do not patch RepoKernel when the lesson belongs to a downstream private system.
Do not patch a downstream system when the lesson belongs to RepoKernel core.

## Minimum Useful Artifact

Choose the smallest artifact that preserves the learning:

```text
none / no_cycle:
  the signal does not change a future action.

process delta:
  the signal changes project memory or review state.

documentation patch:
  the signal clarifies procedure, boundaries or user-facing behavior.

contract patch:
  the signal changes machine-checked semantics or safety rules.

test or fixture:
  the signal exposes a repeatable failure or acceptance condition.

promotion packet:
  the signal may travel to another system, but only after neutralization.
```

Never create a new artifact when an existing current state, decision log,
delta, contract or test can carry the same instruction more clearly.

## A1 Boundary

In A1 observe-and-propose mode, experience intake may:

```text
observe;
classify;
produce a tension report;
propose a patch;
record a process delta;
prepare a promotion packet;
stop for review.
```

It may not:

```text
write to a target repository;
install hooks;
schedule background work;
activate runtime behavior;
promote to Seed, THIA, Lab or any downstream system;
claim public readiness;
increase authority mode.
```

## Fitness Check

Before accepting a patch, record the expected fitness gain:

```text
what confusion is reduced?
what next action becomes easier?
what repeated error is prevented?
what source boundary becomes clearer?
what additional complexity is introduced?
what validation proves the change stayed bounded?
```

Reject or defer the change if the added structure is heavier than the improved
decision.

## Downstream And Public Promotion

RepoKernel may learn from downstream systems and external experiences, but the
public core must stay neutral.

For a downstream system such as Seed, THIA, Lab, a client repository, a private
assistant or an internal node:

```text
1. capture the lesson as a RepoKernel-neutral rule when possible;
2. remove private paths, runtime assumptions and product-specific claims;
3. keep promotion blocked until a dedicated promotion packet exists;
4. make the receiving system choose adoption under its own gate.
```

RepoKernel improvement does not equal downstream activation.

## Receipt Shape

Every accepted experience-driven improvement should preserve:

```text
trigger:
source:
surface_owner:
tension:
minimum_artifact:
expected_fitness_gain:
boundary:
validation:
next_gate:
```

This receipt may live in a process delta, decision log entry, review packet or
implementation return.

## Governing Stop Rule

```text
If a lesson does not improve the next action, prevent a repeated error or
clarify a boundary, do not crystallize it.
```
