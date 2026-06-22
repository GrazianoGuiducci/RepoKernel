# RepoKernel Concept

RepoKernel is a repository pattern for making projects readable, continuable and improvable by AI systems over time.

The central loop is:

```text
entry gate -> current state -> source bootstrap -> semantic kernel
-> process packet -> action -> memory delta -> next reentry
```

The goal is practical continuity. A future AI session should be able to enter the repository and answer:

- what is this project;
- what is active now;
- which sources govern the work;
- what changed recently;
- what should not be followed;
- what can be changed freely;
- what needs confirmation;
- what is the next safe move.

## Autological Loop

In RepoKernel, "autological" does not mean that a project changes itself without supervision.

It means the project records how it was understood, which correction mattered, which rule held, which delta should be preserved, and how the next session should reenter.

## Autoevolutive Loop

In RepoKernel, "autoevolutive" means that repeated useful procedures can become:

- templates;
- scripts;
- skills;
- audit checks;
- promotion packets;
- reusable project rules.

The loop is:

```text
observation -> packet -> action -> delta -> rule -> template/skill -> next repository or promotion
```

