# RepoKernel Final Implementation Package

Date: 2026-06-23  
Status: authoritative package for Codex

Read in this order:

1. `GPT_PRO_REPOKERNEL_FINAL_ARCHITECTURE_AND_CODEX_PACKET_2026-06-23.md`
2. `GPT_PRO_REPOKERNEL_FINAL_ARCHITECTURE_APPENDIX_2026-06-23.md`

Together these files constitute the final GPT Pro architecture report and phased Codex implementation packet.

## Final Decisions

```text
RepoKernel = one host-neutral Project Kernel compiler
SeedSpec = canonical reviewed build contract
Reference Seed = precompiled reproducible SeedSpec
Synthesized ProjectSeed = custom SeedSpec
Retrofit Overlay = application mode against an existing target
Project Kernel = validated local materialization under .repokernel/
Root and host files = adapters or registered existing authorities
L0-L2 = first stable release scope
L3 = contract and roadmap only
```

## Execution Gate

Codex must execute **Phase 0 only**.

Phase 0 ends when:

- every tracked file is inventoried and classified;
- registry and evidence paths resolve;
- incomplete or superseded surfaces are identified;
- internal links are checked;
- the worktree is clean after one isolated commit;
- no Phase 1 implementation has started.

Codex must return the Phase 0 inventory, changes, validation output and blockers for review before continuing.

## Post-Phase-0 Horizon Gate

After Phase 0 is explicitly accepted, but before Phase 1 schemas are frozen, read:

```text
../../docs/possibility-horizon.md
POST_PHASE0_SCHEMA_HORIZON_2026-06-23.md
```

This second gate does not authorize implementation of future capabilities. It only decides the minimum lineage, lifecycle, authority and namespaced-extension fields needed to avoid blocking later evolution.
