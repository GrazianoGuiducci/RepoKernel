# Minimum-Action Improvement Contract

Status: generated Project Kernel learning contract and RepoKernel governance rule

## Purpose

Every observed experience can improve a RepoKernel-shaped project, but not
every observation deserves a new file, rule, hook or feature.

This contract defines how an external lesson, project run, reviewer comment,
operator correction, target-repository friction or downstream system signal can
be converted into durable project memory without increasing noise.

RepoKernel must use this contract in two places:

```text
1. inside RepoKernel itself, when improving the compiler, docs, tests or
   promotion rules;
2. inside generated Project Kernels, so the final project knows how to turn
   useful interactions into deltas, rules, skill candidates and reentry state.
```

The second point is the primary product behavior. RepoKernel is a metatool: its
improvement logic is useful only when it is transferred to the project object
that RepoKernel stages or generates.

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
generated Project Kernel current state;
generated Project Kernel process delta;
generated Project Kernel semantic skill;
RepoKernel core contract;
RepoKernel documentation or test;
review packet;
portable promotion candidate;
downstream private system;
residue.
```

Do not patch RepoKernel when the lesson belongs to a generated or downstream
project. Do not patch a downstream system when the lesson belongs to RepoKernel
core. When the lesson is generic, neutralize it first and then transfer it into
the generated Project Kernel pattern.

## Minimum Useful Artifact

Choose the smallest artifact that preserves the learning:

```text
none / no_cycle:
  the signal does not change a future action.

process delta:
  the signal changes project memory or review state.

semantic skill note:
  the signal changes how the project-specific AI assistant should work.

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
record or stage a process delta;
stage a project-local learning rule;
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

RepoKernel improvement does not equal downstream activation. Generated Project
Kernel learning rules remain proposal-only until the target owner accepts them.

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
