# Runtime Adapters

RepoKernel is host-neutral. Each environment maps the same logical contract to its available project surfaces.

Every adapter declares:

```text
runtime
native surfaces
adapted surfaces
documented-only behavior
unsupported behavior
entry gate
state location
verification rule
```

Current targets include Codex, Claude Code, OpenCode, ChatGPT projects with repository access and generic file-reading agents.

Compatibility is classified as `native`, `adapted`, `documented`, `unsupported` or `unknown`. A compatibility claim does not imply that every host loads instructions, skills or memory automatically.

The invariant flow is:

```text
portable logic -> host adapter -> project state
```
