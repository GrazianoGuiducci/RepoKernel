"""Stage GenerationPlan content into an explicit review directory."""
from __future__ import annotations

from pathlib import Path
from typing import Any

from .models import validate_generation_plan
from .paths import normalize_relative_path


STAGEABLE_ACTIONS = {"create", "propose_update"}


def stage_generation_plan(plan: dict[str, Any], output_dir: Path) -> dict[str, Any]:
    """Write stageable plan content to an empty review directory.

    This is not an apply operation. It never inspects or writes the target
    repository named by the plan; it only renders proposed files for review.
    """
    errors = validate_generation_plan(plan)
    if errors:
        raise ValueError("; ".join(errors))

    output_dir = output_dir.expanduser().resolve()
    if output_dir.exists() and any(output_dir.iterdir()):
        raise ValueError(f"output directory must be empty: {output_dir}")
    output_dir.mkdir(parents=True, exist_ok=True)

    staged: list[str] = []
    skipped: list[dict[str, str]] = []
    for item in plan.get("items", []):
        action = item.get("action")
        rel = normalize_relative_path(item.get("path", ""))
        if action not in STAGEABLE_ACTIONS:
            skipped.append({"path": rel, "action": str(action)})
            continue
        content = item.get("content")
        if not isinstance(content, str):
            skipped.append({"path": rel, "action": str(action), "reason": "no content"})
            continue
        destination = (output_dir / rel).resolve()
        try:
            destination.relative_to(output_dir)
        except ValueError as exc:
            raise ValueError(f"staged path escapes output directory: {rel}") from exc
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(content, encoding="utf-8", newline="\n")
        staged.append(rel)

    return {
        "schema": "repokernel.stage-report.v1",
        "output_dir": str(output_dir),
        "writes_performed": staged,
        "target_writes_performed": [],
        "skipped": skipped,
        "boundary": "staging_only_not_apply",
    }
