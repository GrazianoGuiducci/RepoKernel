# Active Packet — v0.3 Integration

date: 2026-06-23
status: active

## Objective

```text
objective: connect the shared L0-L3 generator core to commands, audits and repository-hosted validation
```

## Sources

```text
CURRENT_STATE.md
README.md
scripts/repokernel_core.py
docs/readiness-levels.md
docs/runtime-adapters.md
docs/internal-runtime-architecture.md
docs/pi-reference.md
packets/FOR_CODEX/V03_INTEGRATION.md
```

## Boundary

```text
allowed: public-safe integration, documentation and synthetic validation
needs_confirmation: downstream promotion and stronger execution modes
out_of_scope: private material and mandatory dependency on one external agent framework
```

## First Move

```text
first_safe_action: integrate the command and regression files described in the v0.3 packet
validation: run the regression suite and the source-repository audit
```

## Memory Delta

```text
preserve: generator contract, readiness model, adapter decisions, validation result and next action
do_not_preserve: temporary implementation failures and unrelated host state
```
