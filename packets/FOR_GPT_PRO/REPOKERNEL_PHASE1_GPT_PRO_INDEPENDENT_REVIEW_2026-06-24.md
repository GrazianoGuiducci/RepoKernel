# RepoKernel Phase 1 — Independent GPT Pro Review

Date: 2026-06-24
Reviewed repository: `GrazianoGuiducci/RepoKernel`
Latest reviewed state: commit `e64d7df` (one commit after the reported `a726549`)
Verdict: **architecture direction accepted; Phase 1 implementation not yet acceptable for collaborator or public testing**

---

## Executive verdict

RepoKernel has converged on a coherent architecture:

```text
SourceManifest
-> ProjectModel
-> reviewed SeedSpec
-> deterministic GenerationPlan
-> reviewed application
-> ActivationReport
```

The separation between `repokernel-core`, cognition, cycle and runtime is correct. Deferring executable L3, automatic writes, network services and Seed promotion is also correct.

The current Phase 1 code is a **useful prototype skeleton**, not yet a contract-safe compiler. The main problems are:

1. governance state is inconsistent: Phase 1 was implemented while the active packet still says `Phase 0 only`;
2. the public quickstart invokes legacy scripts that write immediately and emit the obsolete root-first layout;
3. schemas and Python validators are much weaker than the architecture they claim to encode;
4. the planner is not deterministic across dates and does not implement the canonical `.repokernel/` layout or safe retrofit snapshots;
5. the audit result `L2 ready` does not validate Phase 1 code, schemas or tests;
6. guide privacy and authority controls are insufficient;
7. there is no CLI, installer workflow, package-data strategy or hosted CI;
8. A1 remains a plan, not a proof.

Do not proceed to a real external repository test until the P0 corrections below pass.

---

## 1. Architecture findings

### Correct

- One host-neutral compiler, not separate template and generator systems.
- Reference Seeds as precompiled SeedSpecs.
- Retrofit as an application mode.
- `.repokernel/` as canonical installed control plane.
- Root and host surfaces as adapters.
- L0–L2 first; L3 contract-only.
- Cognition, cycle and runtime optional and dependency-separated.
- No automatic target writes in the new Phase 1 package.

### Critical drift

The accepted architecture says `.repokernel/` is canonical, but the Phase 1 planner emits:

```text
AGENTS.md
CURRENT_STATE.md
process/FIRST_PACKET.md
README.md
sources/bootstrap/
skills/
repokernel.json
registry/
```

The current public quickstart still invokes `scripts/scaffold_repokernel_project.py`, which writes these root-first files directly.

### Missing canonical contracts

The final architecture required richer contracts than the current schemas provide.

Missing or materially incomplete:

```text
SourceManifest:
  instruction_handling
  allowed_uses
  authority/privacy/freshness enums
  content hash constraints
  unique source IDs

ProjectModel:
  evidence-bearing assertions
  per-assertion source references
  verified/inferred/conflict/unknown status
  constraints, terminology, capabilities, workflows, validation

SeedSpec:
  version
  source_manifest_hash
  project_model_hash
  canonical_namespace
  review.status
  selected_capabilities
  boundaries
  adapters
  runtime_route
  file_plan_policy
  validation_plan
  compiler_compatibility

GenerationPlan:
  plan_id
  compiler_version
  target_root
  target_snapshot_hash
  before_hash / after_hash
  patch or content reference
  apply policy
  rollback manifest
  stale-plan protection

ActivationReport:
  selected level
  required check structure
  applied plan hash
  post-apply snapshot
  unresolved items
  limitations
```

### GuideSet inconsistency

`GuideSet` is classified as `core_required`, but there is no GuideSet schema or stable provenance/drift contract. The implementation is a helper returning five Markdown strings.

---

## 2. Governance and configuration findings

### Critical — active gate contradiction

Current repository surfaces disagree:

```text
CURRENT_STATE:
  active_surface = Phase 1 canonical core, planner and guides

FIRST_PACKET:
  status = authorized_phase_0_only
  needs_confirmation = Phase 1

FORGE_R_PHASE1_CONVERGED_RESULTANT:
  status = proposed_for_operator_acceptance

PHASE1_PACKET_AMENDMENT_PROPOSAL:
  authority = do_not_modify_authoritative_packet_until_operator_acceptance
```

No Phase 1 acceptance decision is recorded in `process/DECISION_LOG.md`.

This violates the repository’s own recovery rule requiring `CURRENT_STATE` and `FIRST_PACKET` to agree before work continues.

### Required correction

Choose one of two truthful routes:

```text
A. Operator confirms that Phase 1 was accepted:
   - record dated acceptance in DECISION_LOG;
   - close/supersede Phase 0 packet;
   - create Phase 1 review packet as the active packet;
   - update CURRENT_STATE, ROADMAP, Source Atlas and recovery state.

B. Operator did not accept Phase 1:
   - preserve current work on a review branch;
   - restore main to the accepted Phase 0 baseline;
   - review and reapply Phase 1 after acceptance.
```

Given the operator’s statement that all material was given to Codex, route A is probably intended, but it must be recorded explicitly.

### High — stale generated evidence

- `phase0-validation-summary.md` reports 113 files.
- The external review request reports 113 files.
- Commit `a726549` moved the count to 114.
- Current state includes 115 files after commit `e64d7df`.
- `link-check.json` checked only two Markdown links.
- The Source Atlas still labels `FIRST_PACKET` as the Phase 0 gate.

Generated evidence must include a `generated_from_commit` field and be regenerated atomically.

---

## 3. Safety and authority review

### High — extension authority validation is bypassable

The current blacklist recognizes only a small number of exact keys such as:

```text
authority
authority_mode
autonomy
autonomy_level
action
action_class
```

These pass without error:

```json
{"vendor.policy": {"write_files": true}}
{"vendor.policy": {"permissions": ["project_write"]}}
```

Do not expand the blacklist indefinitely. Use this rule instead:

```text
extensions are opaque data;
core planner never reads extension semantics;
every extension has authority_effect = none;
only a separately registered adapter may interpret an extension;
adapter capabilities are declared outside the extension payload.
```

### High — path validation is incomplete

Current path normalization accepts an empty string as `"."`.

Add rejection for:

```text
empty path
"."
Windows drive prefixes
UNC forms
NUL/control characters
reserved platform names where relevant
symlink escape at apply time
case-collision on case-insensitive targets
```

Planning must be lexical; application must resolve the actual parent and verify it remains under the selected target.

### High — privacy leakage in guide projection

The guide helper:

- excludes only `private` and `withheld`;
- includes `mixed`, unknown or arbitrary privacy values;
- ignores `used_for`;
- exposes `path_or_origin`;
- always emits project intent and product;
- does not apply a disclosure profile;
- does not escape Markdown/control content.

Public output should be deny-by-default:

```text
include only privacy == public
and "public_guide" in allowed_uses
and no withheld_reason
and public label explicitly supplied
```

Never expose raw absolute paths or source IDs by default.

### High — source-as-data boundary is not encoded

The architecture requires source document instructions to remain data unless authorized. The schema does not have `instruction_handling`, and tests do not cover prompt-injection-like source content.

### Medium — no self-approval is documented but not enforced

There is no accepted/reviewed SeedSpec state, evaluator identity, role separation, or immutable review artifact in the implemented contracts.

---

## 4. Core code findings

### `canonical.py`

**High**

- `json.dumps` permits `NaN` and infinities, which are not canonical JSON.
- No Unicode normalization policy.
- No explicit non-semantic-field hashing policy.
- Namespace validation accepts weak forms such as `.x` or `x.`.
- Authority protection is a bypassable key blacklist.

**Required**

```python
json.dumps(..., allow_nan=False)
```

Define and test:

```text
UTF-8
NFC normalization policy
newline policy
string-key-only mappings
semantic vs non-semantic fields
extension round-trip rules
```

### `models.py`

**Critical contract weakness**

Examples currently accepted without errors:

```text
ProjectModel with mission=None, source_refs="oops", boundaries=[]
SeedSpec with no seed_id
GenerationPlan item with no path and external authority on a conflict item
ActivationReport state=active with no successful checks
SkillRegistry entries with arbitrary state, risk and evidence
```

Validators must validate types, enums, required fields, non-empty values, identifier patterns, relations and conditional constraints.

### JSON Schemas

**High**

The tests only verify that schema files parse as JSON. They do not execute JSON Schema validation.

Current schemas permit:

```text
empty SourceManifest sources
arbitrary privacy/authority strings
empty IDs
arbitrary SkillRegistry states
active ActivationReport with empty checks
GenerationPlan without target snapshot or path constraints
```

Add Draft 2020-12 validation tests and parity tests between JSON Schemas and Python validators.

### `planner.py`

**Critical before external test**

- `date.today()` is embedded in planned content and plan metadata, so plans differ across dates.
- The test compares only `items` generated during the same run/day.
- Emits obsolete root-first layout, not canonical `.repokernel/`.
- Does not require `SeedSpec.review.status == accepted`.
- Does not validate source/model hashes.
- Ignores target mode except for a manually supplied list of paths.
- Has no target snapshot or before-hash.
- Cannot detect `leave_unchanged` from identical content.
- `propose_update` contains replacement content, not a reviewable patch.
- `blocked` ignores `propose_update`.
- L3 produces no L3 contract files and is effectively L2.
- Slug generation can yield invalid/empty identifiers.
- Raw intent/product values are inserted into Markdown without a data boundary.

### `dry_run_apply_plan`

The function does not validate the plan, inspect the target, calculate a snapshot, or verify path safety. It only returns paths whose action is `create`. It is a report helper, not an apply preflight.

### `guide_model.py`

**High**

- No contract validation.
- No disclosure profile.
- Mixed/unknown sources may be exposed.
- `used_for` is ignored.
- Raw origin paths can leak.
- SeedSpec intent/product are always public.
- No provenance/hash/drift metadata.
- No escaping of Markdown or instruction-like content.

---

## 5. Test findings

The eight tests likely pass, but they are insufficient.

Current coverage:

```text
2 canonical tests
3 planner tests
2 schema/validator tests
1 guide test
```

Missing P0 negative tests:

```text
canonical NaN/Infinity rejection
Unicode/hash policy
extension alias bypasses
empty, drive, UNC and traversal paths
schema validation with jsonschema
schema/Python-validator parity
duplicate source IDs
invalid privacy/authority/freshness
evidence-bearing ProjectModel conflicts
SeedSpec without accepted review
same plan across different dates
canonical .repokernel output
existing identical file -> leave_unchanged
README remains unchanged by default
stale target snapshot
before/after hash
private/mixed/withheld guide disclosure
Markdown injection/data boundary
active ActivationReport with failed/empty checks
candidate registry entry without evidence
L3 contract-only handling
```

There are no GitHub Actions workflow runs or status checks for the reviewed commit. Local validation is not repository-hosted evidence.

---

## 6. Audit/readiness findings

`repokernel-source ready=true / L2` does **not** validate Phase 1 quality.

The audit checks mainly:

```text
required files/directories exist
state and packet contain keywords
skill frontmatter/path/description
Source Atlas paths exist
registry paths/states/evidence paths exist
```

It does not:

```text
run unit tests
validate JSON Schemas
compare schemas with Python validators
test planner determinism
inspect guide privacy
verify CURRENT_STATE/FIRST_PACKET semantic agreement
verify evidence freshness or relevance
verify the current commit
verify Reference Seed reproducibility
```

`LOCAL_VALIDATION.md` describes an older v0.3 overlay with nine tests, not the current Phase 1 package.

Rename the current audit result:

```text
repository_structure_ready
```

Do not call it Phase 1 L2 readiness until code, schema, guide and integration checks are included.

---

## 7. Installer / CLI / usage review

### Current state

- `pyproject.toml` can package Python modules.
- No console entry point.
- No `__main__.py`.
- No package-data strategy for schemas or guides.
- No CLI.
- Public docs call legacy scripts that immediately write files.
- Legacy scripts do not implement dry-run-first planning.

### Minimum next interface

```bash
repokernel validate-spec seed.json
repokernel plan --spec seed.json --target ./project --output plan.json
repokernel inspect --target ./existing --output snapshot.json
repokernel guides --spec seed.json --manifest sources.json --output ./staging
repokernel audit --target ./project
```

Do not ship `apply` yet. First ship a staging/materialization command that writes only to a new explicitly selected staging directory.

Later:

```bash
repokernel apply \
  --plan plan.json \
  --target ./project \
  --approve-plan <hash>
```

Only after target snapshot, rollback and atomic application are implemented.

### Packaging

Add:

```toml
[project.scripts]
repokernel = "repokernel.cli:main"
```

Move or package schemas under `src/repokernel/resources/` and access them with `importlib.resources`. Ensure wheels contain schemas and guide templates.

Legacy scaffold scripts should:

```text
print deprecation warning
default to dry-run
refuse non-empty targets without an explicit reviewed plan
delegate to the package
```

Until then, remove them from the public quickstart.

---

## 8. Guide review

### Good

- Clear high-level mode names.
- Clear approval list.
- Public-safe language.
- Explicit deferral of runtime and multi-repo operation.

### Missing

The guide-system decision requires much more than the current files provide.

The minimal example lacks:

```text
SourceManifest
ProjectModel with source references/conflicts
reviewed SeedSpec status
full GenerationPlan
guide output
ActivationReport
failure path
retrofit example
privacy example
```

The user guide has no installation or executable workflow. The coder guide has no API signatures, contract tables, error semantics or package layout. The architecture guide states capabilities not yet implemented.

### Public claim corrections

Replace:

```text
"RepoKernel assimilates ... then compiles ..."
```

with:

```text
"RepoKernel is being built to compile..."
"Phase 1 currently validates minimal contracts and produces a prototype dry-run plan from a hand-prepared SeedSpec."
```

Remove or replace the stale README “Current Gate” section.

First page:

```text
external user -> docs/guides/user-guide.md
coder -> docs/guides/coder-guide.md
reviewer/architect -> docs/guides/architecture.md
```

But README must link them with actual Markdown links, not plain code-block paths.

---

## 9. A1 observe-and-propose review

The current document is a good proof **plan**, not evidence.

To reduce self-evaluation bias:

1. Precommit evaluator criteria and expected failure cases before generating Resultants.
2. Use a separate evaluator role or independent model/session.
3. Hash the evaluator fixture before observation.
4. Include adversarial and ambiguous examples.
5. Include at least one human-labeled reference.
6. Measure false positive and false negative triggers.
7. Run against a read-only snapshot of a real external-style repo.
8. Hash the tree before and after and assert equality.
9. Exclude `.git`, secrets, large binary files and ignored paths.
10. Require cited evidence for every material claim.

Independent evaluator checks:

```text
source citation coverage
conflicts preserved
unknowns not invented
authority unchanged
no file/network side effects
deduplication
resultant relevance
counterexample handling
operator usefulness
scope discipline
```

A1 should not be called proven until fixtures and an independent evaluation report exist.

---

## 10. External-use readiness

| Use mode | Status | Minimum blocker |
| --- | --- | --- |
| Private internal architecture/prototype work | **Ready with restrictions** | Use hand-built fixtures only; no target writes; do not trust L2 audit as quality evidence |
| Trusted collaborator review | **Not ready as a tool** | Fix state/gate, schemas, planner determinism, safe public entrypoint and tests |
| Public experimental use | **Not ready** | CLI/staging workflow, packaged resources, CI, real examples, disclosure controls |
| Production use | **Not ready** | Safe apply transaction, snapshots, rollback, integration evidence, security model and release process |

---

## 11. Prioritized improvement plan

### P0 — before the next external-style test

1. **Repair governance state**
   - Files: `CURRENT_STATE.md`, `process/FIRST_PACKET.md`, `process/DECISION_LOG.md`, `process/ROADMAP.md`, Source Atlas.
   - Record whether Phase 1 was explicitly accepted.
   - Acceptance: recovery validation reports no gate conflict.

2. **Remove unsafe legacy public path**
   - Files: `README.md`, `docs/quickstart.md`, scaffold scripts.
   - Remove direct-write commands or make them fail-safe/dry-run.
   - Acceptance: following README performs no target write.

3. **Make schemas and validators real**
   - Execute Draft 2020-12 validation.
   - Add schema/Python parity fixtures.
   - Acceptance: all adversarial invalid fixtures fail both.

4. **Fix canonical serialization**
   - Reject NaN/Infinity; define Unicode and semantic-hash policy.
   - Acceptance: cross-process fixture hashes stable.

5. **Fix path safety**
   - Reject empty, drive, UNC, control and traversal paths.
   - Acceptance: adversarial path matrix passes.

6. **Fix planner determinism and layout**
   - No live date in semantic plan.
   - Emit `.repokernel/`.
   - Require accepted SeedSpec.
   - Separate new and retrofit planning.
   - Acceptance: same spec and snapshot produce byte-identical plan across dates.

7. **Fix guide disclosure**
   - Public-only whitelist and allowed-use check.
   - No raw source path or private intent/product.
   - Acceptance: privacy fixture has zero leakage.

8. **Correct readiness claim**
   - Rename structural audit result or extend audit to run current tests/schema checks.
   - Acceptance: L2 cannot pass with malformed schema or failing unit test.

### P1 — before trusted collaborator use

- Build CLI with validate/inspect/plan/guides/audit.
- Package schemas/templates.
- Add CI.
- Add complete new-project and retrofit fixtures.
- Add target snapshot and before-hash.
- Add ActivationReport generator.
- Add review status and source/model hashes to SeedSpec.
- Add independent A1 fixtures and evaluator report.

### P2 — before public experimental use

- Staging materialization.
- Signed/reproducible Reference Seed proof.
- Cross-platform path/case tests.
- Public/private disclosure profiles.
- Error taxonomy and troubleshooting.
- Version compatibility and migration policy.
- Security review and threat model.
- Two external pilot reports.

### P3 — later

- Reviewed apply transaction with rollback.
- ContextSnapshot/TensionReport cycle package.
- Departmental extensions.
- Runtime adapters.
- L3 reference runtime.
- Seed promotion.
- Multi-repo constellation.

---

## 12. Patch-ready design changes

### Validators

Prefer typed validation helpers plus JSON Schema parity. Every validator should return structured errors:

```python
{
    "path": "sources[0].privacy",
    "code": "invalid_enum",
    "message": "...",
}
```

Add:

```text
validate_source_entry
validate_assertion
validate_review_block
validate_plan_item
validate_activation_check
validate_registry_entry
```

### Planner signature

```python
build_generation_plan(
    seed_spec,
    *,
    target_snapshot,
    compiler_version,
    generated_at=None,
)
```

`generated_at` is metadata excluded from semantic plan hashing.

### Guide projection

```python
build_guides(
    seed_spec,
    source_manifest,
    *,
    disclosure_profile="public",
)
```

Only explicit public fields enter public guides.

### CLI

```text
validate-spec
inspect
plan
guides
audit
verify-dist
```

No `apply` in the next release.

---

## 13. Questions for the operator

1. Was the converged Phase 1 scope explicitly accepted before commit `8942874`?
2. Should `.repokernel/` become canonical immediately, or is one root-first compatibility release required?
3. Is the first usable product:
   - a planner API,
   - a CLI for Direct Start,
   - or read-only retrofit inspection?
4. May public guides expose project intent/product by default?
5. Is adding `jsonschema` as a locked dependency acceptable?
6. Should Phase 1 reject L3 SeedSpecs entirely or permit only `runtime_route=contract-only`?
7. Should legacy scaffold scripts be disabled now or retained behind an explicit `--legacy-write` flag?

---

## Final recommendation

Keep the Phase 1 work. Do not revert the architecture or discard the code.

Treat commit `8942874` as a prototype implementation branch now present on main. Repair governance and safety first, then harden schemas, planner and tests before any real external-repository pilot.

The next Codex task should be a bounded **Phase 1 P0 hardening packet**, not Phase 2.
