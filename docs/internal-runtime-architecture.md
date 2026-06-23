# Internal Runtime Architecture

RepoKernel may generate an optional internal runtime candidate for a project that needs stronger independence from a specific AI host.

The runtime is a replaceable body around the project kernel. It is not the identity of the seed.

## Planes

### Kernel Plane

```text
identity
state
source authority
boundaries
skills
registry
evidence
```

### Runtime Plane

```text
context compiler
model adapter
event lifecycle
tool registry
action preflight
result gate
session store
extension loader
```

### Improvement Plane

```text
observation -> proposal -> isolated test -> evidence -> review -> accepted change
```

### Bridge Plane

```text
GitHub
local workspace
agent host
chat project
document store
database or event stream
local or remote model provider
```

## Reference Events

```text
runtime_start
cycle_start
context_ready
model_request
model_response
action_preflight
action_start
action_end
cycle_end
runtime_end
```

Every event carries stable run, cycle and lineage identifiers.

## Sessions

Sessions use append-only records with a stable identifier and optional parent identifier. Branches preserve prior history. Context summaries remain distinct from source events and accepted project memory.

## Trust

Project-local executable extensions stay disabled until the project is explicitly trusted and their source has been reviewed. Prompts and skills do not grant tool or publication authority.

## Authority Modes

```text
none
proposal_only
project_write
operator_granted
```

The generated default is `proposal_only`.
