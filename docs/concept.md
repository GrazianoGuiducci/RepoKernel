# RepoKernel Concept

RepoKernel is a repository pattern for making projects readable, continuable
and improvable by AI systems over time.

It can be applied to new or existing projects as a project-local learning
structure. The project keeps its own current state, source atlas, process
packets, rules, skills, evidence, memory deltas and reentry points, so useful
interactions can sediment into continuity instead of remaining scattered in chat
history.

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

RepoKernel is therefore a generator of intelligent project environments in a
bounded sense: it gives projects the structure to remember, route, review and
improve AI-assisted work. It is not a claim that the project becomes autonomous
or that RepoKernel may write to the target without a later reviewed gate.
