# Changelog

RepoKernel changes are recorded for coders and agentic systems that enter the
repository later and need to decide whether an installed copy or a local
Project Kernel should be updated.

This changelog is evidence for review. It is not automatic update authority.

## 0.3.0.dev0 - 2026-06-30

### Added

- Coder-readable capability update path:
  - `CAPABILITIES.md`
  - `docs/update-and-adoption.md`
- Metaskill propagation contract:
  - `docs/metaskill-propagation-contract.md`
- Generated Project Kernels now carry a project-local metaskill propagation
  protocol in staged semantic skills.

### Boundary

- No auto-update, hook activation, runtime authority, target write, bulk copy
  or public readiness claim is implied.
- A coder may read these files, compare local state and propose an update
  candidate with owner, source, gate, validation and receipt.
