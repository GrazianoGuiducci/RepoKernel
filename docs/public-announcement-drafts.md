# RepoKernel Public Announcement Drafts

status: draft_not_published
updated: 2026-06-26
scope: public-safe copy for LinkedIn, GitHub and short outreach

## Claim Boundary

Use RepoKernel publicly only as:

```text
an experimental no-apply Project Kernel compiler that validates authorized
sources, builds target-bound generation plans, stages proposed files outside
the target repository and preserves review gates before any future write-capable
step.
```

Do not claim:

```text
production-ready;
installer-ready;
safe for arbitrary repositories;
autonomous repo modification;
apply support;
runtime/daemon support;
public alpha for non-technical users;
trusted security boundary for secrets or private repositories.
```

## Current Link Set

```text
repository: https://github.com/GrazianoGuiducci/RepoKernel
overview: https://github.com/GrazianoGuiducci/RepoKernel/blob/main/docs/overview.html
quickstart: https://github.com/GrazianoGuiducci/RepoKernel/blob/main/docs/quickstart.md
pre-public checklist: https://github.com/GrazianoGuiducci/RepoKernel/blob/main/docs/pre-public-checklist.md
latest CI evidence: https://github.com/GrazianoGuiducci/RepoKernel/actions/runs/28249042426
```

## LinkedIn Draft - Italian

```text
Sto lavorando a RepoKernel: un compilatore sperimentale per creare Project
Kernel revisionabili nei progetti sviluppati con AI.

L'idea nasce da un problema pratico: quando si usa un assistant per sviluppare
software, serve un modo stabile per conservare intento, fonti autorizzate,
stato, confini, decisioni e prossime mosse senza trasformare subito l'AI in un
sistema che modifica repository in autonomia.

RepoKernel oggi fa una cosa precisa:

fonti autorizzate + modello del progetto
-> SeedSpec revisionato
-> GenerationPlan legato al target
-> staging dei file proposti fuori dal repository
-> revisione umana prima di qualsiasi futuro passo con scrittura

Non e' ancora un installer, non e' production-ready e non ha un comando apply.
E' una base diagnostica no-write: utile per osservare, pianificare e rendere
revisionabile il modo in cui un progetto puo' acquisire un proprio kernel
operativo.

Per ora il valore non e' "l'AI scrive codice o email da sola".
Il valore e':

- continuita' del progetto;
- fonti e decisioni ispezionabili;
- no-write staging;
- policy prima del modello;
- promozione solo dopo revisione.

Repository:
https://github.com/GrazianoGuiducci/RepoKernel
```

## LinkedIn Draft - Shorter Italian

```text
Ho pubblicato RepoKernel, un esperimento open source per rendere piu'
revisionabili i progetti sviluppati con AI.

RepoKernel prende fonti autorizzate e intento di progetto, valida i contratti,
crea un piano legato al target e mette i file proposti in staging fuori dal
repository. Nessun apply, nessuna scrittura automatica, nessun runtime.

Il punto e' semplice: prima di far agire un sistema AI su un progetto, voglio
che il progetto abbia stato, confini, fonti, evidenze e review gate leggibili.

Stato attuale: sperimentale, no-write, diagnostico. Non production-ready.

Repo:
https://github.com/GrazianoGuiducci/RepoKernel
```

## LinkedIn Draft - English

```text
I am working on RepoKernel: an experimental no-apply compiler for reviewable
Project Kernels in AI-assisted development.

The problem is practical. When an AI assistant helps develop a project, the
project needs a stable way to preserve intent, authorized sources, state,
boundaries, decisions and next actions without immediately becoming an
autonomous repository modifier.

Current flow:

authorized sources + project model
-> reviewed SeedSpec
-> target-bound GenerationPlan
-> staged proposed files outside the target repository
-> human review before any future write-capable step

RepoKernel is not production-ready, not an installer and has no apply command.
It is a no-write diagnostic base for making AI-assisted project setup more
inspectable.

Repository:
https://github.com/GrazianoGuiducci/RepoKernel
```

## GitHub Repository Short Description

```text
Experimental no-apply compiler for reviewable Project Kernels in AI-assisted development.
```

## GitHub About / Pinned Card Copy

```text
RepoKernel validates authorized project sources, builds target-bound generation
plans and stages proposed project-kernel files outside the target repository.
It is currently an experimental diagnostic compiler: no apply command, no
runtime, no credential handling and no autonomous repository writes.
```

## First Comment / Clarification If Asked

```text
The important boundary is that RepoKernel does not install itself into a target
repository today. It proposes and stages files for review. Any future
write-capable apply gate must be separately designed, reviewed and authorized.
```

## Before Posting

```text
1. Verify repository is public and clean.
2. Verify latest hosted CI run is success.
3. Verify README, quickstart, overview and checklist remain aligned.
4. Do not include private paths, tokens, client material or local-only reports.
5. Link only RepoKernel public-safe surfaces.
6. Operator approves exact text before publishing.
```
