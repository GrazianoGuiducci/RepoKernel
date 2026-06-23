# Retrofit Model

RepoKernel integrates into an existing repository by mapping and adapting its current structure. It does not clone itself over the project.

```text
read-only inventory -> authority map -> SeedSpec -> overlay plan -> review -> apply -> audit -> activation
```

Existing project files remain authoritative until an explicit reviewed change replaces them.
