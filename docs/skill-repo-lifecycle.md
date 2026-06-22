# Skill Repository Lifecycle

RepoKernel can create and evaluate repository-shaped skills.

## Lifecycle States

```text
draft
candidate
accepted
promoted
private
residue
```

## Draft

A capability idea exists, but it has not been tested.

Required evidence:

- problem statement;
- intended user or agent;
- first example;
- boundary.

## Candidate

The skill has a repository or folder structure and can be tested.

Required evidence:

- `AGENTS.md`;
- `CURRENT_STATE.md`;
- `skills/<name>/SKILL.md`;
- first packet or test case;
- memory-delta rule.

## Accepted

The skill has worked at least once in a real or synthetic task and its boundary is clear.

Required evidence:

- test or readback;
- clear source authority;
- current limitations;
- next safe improvement.

## Promoted

The skill is ready to move to a broader package, registry or seed.

Required evidence:

- normalized brief;
- what must not travel;
- proof of usefulness;
- rollback or deprecation path;
- owner approval.

## Private

The skill is useful but contains private context, client material, credentials, internal process or sensitive source assumptions.

## Residue

The idea should not be followed now. Keep only the reason if it prevents future confusion.

