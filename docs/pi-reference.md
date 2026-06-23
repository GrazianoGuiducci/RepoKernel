# Pi Agent Harness Reference

Source reviewed: <https://github.com/earendil-works/pi/tree/main>

This is an architectural reference only. RepoKernel does not copy Pi code and does not require Pi as a dependency.

## Patterns Retained

- separate model, agent-runtime and user-interface layers;
- context preparation before a model request;
- pre-action and post-action hooks;
- explicit runtime events;
- append-only session trees with stable identifiers;
- separate skills, prompts and executable extensions;
- project trust before loading local executable resources;
- SDK or process interfaces for alternate hosts;
- a small core with optional extensions.

## RepoKernel Translation

```text
Pi model API        -> model/provider adapter
Pi agent core       -> optional runtime plane
Pi tool hooks       -> action and result gates
Pi session tree     -> append-only lineage
Pi local resources  -> seed-local skills, prompts and extensions
Pi project trust    -> explicit executable-resource trust gate
Pi packages         -> optional portable seed bundles
```

## Deliberate Differences

RepoKernel does not adopt Pi as a mandatory runtime, implicit trust, automatic third-party execution, or direct runtime output as accepted project state.

A future Pi adapter may map a RepoKernel L3 seed to Pi resources, sessions, events and programmatic interfaces. That adapter remains optional and version-pinned.
