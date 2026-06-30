# 2026-06-30 - External Assistant First Contact

status: accepted local implementation

## Trigger

The operator proposed a scenario where an external user asks a coding assistant
what is useful in RepoKernel. The assistant should read prepared material,
explain possibilities clearly, give examples and ask for approval before clone
or setup work begins.

## Decision

Add an assistant-facing first-contact playbook.

## Change

```text
docs/guides/external-assistant-playbook.md:
  plain-language explanation, current useful capabilities, examples by project
  type, response template, consent gate and first setup report shape.

docs/guides/user-guide.md:
  points users to ask for a read-only explanation before clone or diagnostics.

docs/guides/use-cases.md:
  adds assistant-guided first contact as a use case.

README.md and Source Atlas:
  link and index the guide.
```

## Boundary

No public tester solicitation, publication, external cloning, private repository
inspection, target write, apply behavior, runtime activation or credential
handling is authorized by this guide.

## Next Safe Action

Use the playbook as the basis for the external RepoKernel narrative and later
convert the best parts into approved public copy or an onboarding page.
