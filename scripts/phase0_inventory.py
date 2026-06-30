#!/usr/bin/env python3
"""Generate RepoKernel Phase 0 inventory, classification and link reports."""
from __future__ import annotations

import json
import re
import subprocess
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "process" / "reports"


def git_ls_files() -> list[str]:
    result = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files"],
        check=True,
        capture_output=True,
        text=True,
    )
    return sorted(path.replace("\\", "/") for path in result.stdout.splitlines() if path.strip())


def text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return ""


def group_for(path: str) -> str:
    if "/" not in path:
        return "root"
    return path.split("/", 1)[0]


def action_for(path: str) -> tuple[str, str, str]:
    if path in {".gitignore", "LICENSE"}:
        return ("keep", "stable_support", "Stable repository support file.")
    if path.startswith(".github/workflows/"):
        return ("keep_ci_template", "ci", "Hosted CI workflow support; activation state is governed separately.")
    if path.startswith(".github/ISSUE_TEMPLATE/"):
        return ("keep_feedback_template", "feedback_template", "Public-safe GitHub issue template.")
    if path == "MANIFEST.in":
        return ("keep_phase1_package_metadata", "phase1_package", "Package manifest for source distribution contents.")
    if path in {"CHANGELOG.md", "CAPABILITIES.md"}:
        return ("keep_update_signal", "update_signal", "Coder-readable update and capability adoption signal.")
    if path in {"README.md", "AGENTS.md", "CURRENT_STATE.md", "repokernel.json"}:
        return ("migrate_later", "compatibility_adapter", "Root file remains active until .repokernel/ self-host migration.")
    if path == "pyproject.toml":
        return ("keep_phase1_package_metadata", "phase1_package", "Phase 1 package metadata for the core library.")
    if path.startswith("specs/reference/"):
        return ("keep_reference_seed", "reference_seed", "Reviewed SeedSpec used for reproducible reference distribution.")
    if path.startswith("dist/reference/"):
        return ("keep_reference_distribution", "reference_distribution", "Compiler-verifiable generated reference distribution.")
    if path == "process/FIRST_PACKET.md":
        return ("keep_current_gate", "active_phase0_gate", "Active Phase 0 packet.")
    if path == "registry/skills.json":
        return ("correct_and_migrate_later", "registry", "Registry remains active; final schema migration is Phase 1+.")
    if path.startswith("docs/"):
        if path.startswith("docs/guides/"):
            return ("keep_phase1_guide", "guide", "Phase 1 guide surface; explains contracts without authority.")
        if path in {"docs/context-surface.md", "docs/quickstart.md", "docs/codex-operating-guide.md", "docs/concept.md"}:
            return ("replace_or_reduce", "documentation_cleanup", "Current docs require final-architecture alignment before stable release.")
        if path in {"docs/internal-runtime-architecture.md", "docs/recursive-distillation-plane.md", "docs/autopoietic-cycle-gap-analysis.md", "docs/departmental-autonomy-spectral-analysis.md", "docs/possibility-horizon.md"}:
            return ("keep_as_optional_reference", "optional_architecture", "Optional plane or future constraint; not current implementation authority.")
        return ("keep_and_normalize", "documentation", "Architecture or policy doc remains source material for convergence.")
    if path.startswith("templates/"):
        return ("migrate_to_compiler_templates", "template", "Template remains source material until compiler template layout exists.")
    if path.startswith("examples/"):
        return ("replace_with_generated_fixture", "example", "Example must be regenerated from compiler once Phase 1+ supports it.")
    if path.startswith("skills/"):
        return ("keep_registered_skill", "skill", "Skill is governed by registry state and evidence.")
    if path.startswith("scripts/"):
        if path == "scripts/phase0_inventory.py":
            return ("keep_phase0_tool", "phase0_tool", "Generates reproducible Phase 0 reports.")
        return ("keep_prototype_or_wrapper", "script", "Prototype/wrapper remains until package refactor has parity tests.")
    if path.startswith("src/repokernel/"):
        return ("keep_phase1_core", "phase1_core", "Phase 1 core package surface.")
    if path.startswith("schemas/"):
        return ("keep_phase1_schema", "phase1_schema", "Phase 1 canonical contract schema.")
    if path.startswith("tests/"):
        return ("keep_phase1_test", "phase1_test", "Phase 1 regression or contract test.")
    if path.startswith("process/reports/"):
        return ("keep_phase0_evidence", "phase0_report", "Generated Phase 0 evidence.")
    if path.startswith("process/agentic-feedback/"):
        return ("keep_agentic_feedback", "agentic_feedback", "Public-safe structured agent/runtime feedback evidence.")
    if path.startswith("process/evidence/"):
        return ("keep_evidence", "evidence", "Validation evidence remains source for readiness decisions.")
    if path.startswith("process/deltas/"):
        return ("keep_historical_delta", "delta", "Durable accepted delta.")
    if path.startswith("process/"):
        return ("keep_process_record", "process", "Process state, roadmap or decision record.")
    if path.startswith("sources/bootstrap/"):
        return ("keep_until_self_host_migration", "bootstrap", "Bootstrap remains active until .repokernel/sources migration.")
    if path.startswith("packets/archive/"):
        return ("keep_archive_index", "archive", "Archive index for superseded packet lineage.")
    if path.startswith("packets/FOR_CODEX/V03_") or path.startswith("packets/FOR_CODEX/V04_"):
        return ("superseded_keep_until_archive_move", "superseded_packet", "Superseded by final architecture; retained in place for provenance.")
    if path.startswith("packets/FOR_CODEX/POST_PHASE0_"):
        return ("keep_post_phase0_gate", "post_phase0_gate", "Gate material only after Phase 0 acceptance.")
    if path.startswith("packets/FOR_CODEX/GPT_PRO_") or path.startswith("packets/FOR_CODEX/REPOKERNEL_FINAL_"):
        return ("keep_authoritative_packet", "authoritative_packet", "Final architecture or implementation gate.")
    if path.startswith("packets/FOR_CODEX/REPO_OBSERVER_"):
        return ("keep_classification_note", "phase0_classification", "Phase 0 ownership correction; no implementation authority.")
    if path.startswith("packets/FOR_CODEX/"):
        return ("classify_before_phase1", "packet", "Packet must be reviewed during convergence before Phase 1.")
    if path.startswith("packets/FOR_GPT_PRO/"):
        return ("archive_after_acceptance", "source_packet", "Source packet lineage; not direct implementation authority.")
    if path.startswith("packets/FOR_SEED_PROMOTION/"):
        return ("keep_draft_no_promotion", "seed_candidate_draft", "Seed promotion is blocked until stable L0-L2 evidence.")
    return ("manual_review", "unclassified", "No Phase 0 rule matched this path.")


def build_reports(paths: list[str]) -> tuple[dict, dict]:
    tree_items = []
    class_items = []
    for path in paths:
        file_path = ROOT / path
        action, category, reason = action_for(path)
        tree_items.append({
            "path": path,
            "group": group_for(path),
            "kind": "file",
            "suffix": file_path.suffix,
        })
        class_items.append({
            "path": path,
            "action": action,
            "category": category,
            "reason": reason,
        })
    unclassified = [item["path"] for item in class_items if item["category"] == "unclassified"]
    current_tree = {
        "schema": "repokernel.phase0.current-tree.v1",
        "generated_on": date.today().isoformat(),
        "tracked_file_count": len(paths),
        "groups": sorted({group_for(path) for path in paths}),
        "files": tree_items,
    }
    classification = {
        "schema": "repokernel.phase0.migration-classification.v1",
        "generated_on": date.today().isoformat(),
        "tracked_file_count": len(paths),
        "unclassified_count": len(unclassified),
        "unclassified": unclassified,
        "actions": sorted({item["action"] for item in class_items}),
        "categories": sorted({item["category"] for item in class_items}),
        "files": class_items,
    }
    return current_tree, classification


LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)#][^)]+)\)")


def check_links(paths: list[str]) -> dict:
    results = []
    for path in paths:
        if not path.endswith(".md"):
            continue
        content = text(ROOT / path)
        for raw in LINK_RE.findall(content):
            target = raw.split("#", 1)[0].strip()
            if not target or re.match(r"^[a-z]+://", target) or target.startswith("mailto:"):
                continue
            target_path = (ROOT / path).parent.joinpath(target).resolve()
            try:
                target_path.relative_to(ROOT)
            except ValueError:
                ok = False
            else:
                ok = target_path.exists()
            results.append({
                "source": path,
                "target": target,
                "ok": ok,
            })
    broken = [item for item in results if not item["ok"]]
    return {
        "schema": "repokernel.phase0.link-check.v1",
        "generated_on": date.today().isoformat(),
        "checked_links": len(results),
        "broken_count": len(broken),
        "broken": broken,
        "links": results,
    }


def main() -> int:
    paths = git_ls_files()
    current_tree, classification = build_reports(paths)
    link_report = check_links(paths)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    (REPORT_DIR / "current-tree.json").write_text(json.dumps(current_tree, indent=2) + "\n", encoding="utf-8")
    (REPORT_DIR / "migration-classification.json").write_text(json.dumps(classification, indent=2) + "\n", encoding="utf-8")
    (REPORT_DIR / "link-check.json").write_text(json.dumps(link_report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "tracked_file_count": len(paths),
        "unclassified_count": classification["unclassified_count"],
        "broken_links": link_report["broken_count"],
        "reports": [
            "process/reports/current-tree.json",
            "process/reports/migration-classification.json",
            "process/reports/link-check.json",
        ],
    }, indent=2))
    return 1 if classification["unclassified_count"] or link_report["broken_count"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
