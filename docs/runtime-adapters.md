# Runtime Adapters

RepoKernel is host-neutral. Each environment maps the same project contract to the surfaces it actually supports.

## Adapter Contract

```text
runtime
native surfaces
adapted surfaces
documented-only behavior
unsupported behavior
entry gate
state location
model interface
tool interface
session interface
verification rule
```

## Current Targets

| Environment | Typical role |
| --- | --- |
| Codex | Repository work, shell and supported skills |
| Claude Code | Repository instructions, skills and host lifecycle features |
| OpenCode | Repository files and supported tools or instructions |
| ChatGPT project | Reentry through selected repository sources |
| Generic agent | Documented protocol over the access exposed by its host |
| Internal reference runtime | Optional L3 body generated inside a project seed |
| Pi adapter candidate | Optional future mapping to Pi resources, events, sessions and SDK/RPC |

Compatibility is classified as `native`, `adapted`, `documented`, `unsupported` or `unknown`.

“Works with” does not imply that every host automatically loads instructions, skills, extensions or memory.

```text
portable kernel -> environment adapter -> runtime state -> verified delta
```

The runtime is replaceable. Project meaning remains in the kernel plane.
