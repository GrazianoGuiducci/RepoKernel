# Metaskill Propagation Contract

Status: candidate propagation contract for generated Project Kernels

## Purpose

A metaskill is a reusable invariant that may emerge inside one surface but
should not remain trapped there if it can improve other projects.

This contract explains how RepoKernel handles such invariants without turning
them into bulk copy, hidden authority or runtime mutation.

## Core Distinction

```text
invariant:
  reusable rule or method that can guide many projects.

incarnation:
  local expression of that invariant inside one project, skill, adapter, UI,
  workflow, generated Project Kernel or runtime contract.
```

Do not copy an incarnation as if it were the invariant.

## Intake

When a metaskill-like signal appears, classify:

```text
origin_surface:
local_failure_corrected:
invariant:
verified_local_incarnation:
candidate_owner:
candidate_surfaces:
first_safe_propagation_path:
```

If the invariant cannot be stated without private paths, runtime assumptions,
client context, secrets or local identity, it is not ready for public
RepoKernel propagation.

## Propagation Gate

Before an invariant reaches a Project Kernel, require:

```text
owner:
source:
gate:
validation:
receipt:
do_not_apply_globally:
```

Valid outputs:

```text
no_cycle:
  signal does not change future action.

update_candidate:
  propose local adoption, no mutation.

project_kernel_rule:
  add a project-local rule in generated/staged Project Kernel content.

skill_candidate:
  propose a project-local skill only when repeated use justifies it.

capability_manifest:
  propose a project-local manifest when skill-like behavior may be consumed by
  an autonomous runtime, product workbench, agent loop or service surface.

receipt_reducer:
  propose a deterministic reducer or validator when a receipt class is stable
  enough to map to a finite state and next legal action without model
  reinterpretation.

promotion_packet:
  neutral transfer packet for another source lane.
```

## Generated Project Kernel Rule

When applicable, the generated Project Kernel should receive a local rule that
asks future coders to:

```text
distinguish invariant from incarnation;
avoid copying the rule everywhere;
check owner, source, gate, validation and receipt;
adopt only when it improves this project;
record why the local incarnation is useful here;
```

If the local incarnation is autonomous or semi-autonomous capability use, the
generated Project Kernel should also ask future coders to define:

```text
capability manifest;
allowed and blocked actions;
side-effect class;
receipt schema;
reducer or validator when the receipt is stable;
human gate trigger;
stop condition;
next legal action.
```

The rule belongs inside the staged project object. A RepoKernel-only document is
not enough for product behavior.

## Prohibited Propagation

Do not use this contract to justify:

```text
bulk patching all skills or repos;
hidden hooks;
runtime authority;
target writes;
cleanup campaigns;
public publication;
secret or log reads;
cross-node state cloning;
```

## Receipt Shape

```text
metaskill_name:
origin_surface:
invariant:
local_incarnation:
target_project:
minimum_artifact:
owner:
gate:
validation:
receipt:
next_action:
```

For autonomous capability candidates, add:

```text
capability_id:
allowed_actions:
blocked_actions:
side_effect_class:
receipt_schema:
reducer_or_validator:
human_gate_required_when:
stop_condition:
```
