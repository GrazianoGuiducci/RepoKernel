# Package Boundaries V1

date: 2026-06-24
status: convergence_gate_output

## Packages

```text
repokernel-core
  schemas
  canonical serialization
  source manifest
  project model
  SeedSpec
  deterministic GenerationPlan
  dry-run application
  retrofit observation and conflict classification
  ActivationReport
  SkillRegistry
  GuideSet model and maintained guide surfaces

repokernel-cognition
  recursive distillation
  cognitive profiles
  ResultantPacket
  branch scoring
  possibility expansion

repokernel-cycle
  ContextSnapshot
  TensionReport
  AutonomyPolicy
  FitnessContract
  ResultantEvaluation
  LearningDelta
  event deduplication fixtures

repokernel-runtime
  optional execution body
  sessions
  event lifecycle
  tool adapters
  extension loading
  action preflight
```

## Allowed Dependencies

```text
core -> Python standard library
cognition -> core
cycle -> core, cognition
runtime -> core, cycle
departmental extensions -> core, optionally cycle
```

Forbidden:

```text
core -> cognition
core -> cycle
core -> runtime
core -> departments
core -> network-dependent services
```

## Guide Boundary

Guides are part of `repokernel-core` because they are necessary for external
and internal use. They are not a separate authority plane.

```text
canonical contracts
  -> guide model
  -> user guide
  -> coder guide
  -> architecture guide
  -> use-case guide
  -> examples
```

A guide may explain, project, summarize or exemplify. It may not redefine:

```text
authority
source validity
SeedSpec semantics
planner behavior
promotion rules
runtime permission
```

## Departmental Boundary

Future department contracts depend on core contracts:

```text
DepartmentContract -> SeedSpec, SourceManifest, ActivationReport, SkillRegistry
SynapticEvent -> SourceManifest references, authority_mode, lifecycle
```

Core does not depend on departments. Direct Start, Synthesis and Retrofit must
work when no departmental extension exists.

## Runtime Boundary

Runtime is deferred. Phase 1 can reserve:

```text
runtime_route: "no-runtime" | "contract-only"
extensions: {}
```

No event daemon, scheduler, tool execution, network transport or model loop is
implemented in Phase 1.

## Import Rule For Phase 1

```text
src/repokernel/models.py
src/repokernel/canonical.py
src/repokernel/paths.py
src/repokernel/planner.py
src/repokernel/guide_model.py
```

These modules may not import future cognition, cycle, runtime or departmental
modules.

## Acceptance

The boundary is valid when:

```text
unit tests import core without optional packages;
schemas validate without runtime fields;
unknown namespaced extensions are preserved but ignored by planning authority;
guides can be produced from core fields without changing core decisions.
```
