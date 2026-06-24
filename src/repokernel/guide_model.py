"""Guide projection helpers for RepoKernel."""
from __future__ import annotations

from typing import Any


GUIDE_FILES = {
    "architecture": "docs/guides/architecture.md",
    "user": "docs/guides/user-guide.md",
    "coder": "docs/guides/coder-guide.md",
    "use_cases": "docs/guides/use-cases.md",
    "application_types": "docs/guides/application-types.md",
}


def public_source_titles(source_manifest: dict[str, Any]) -> list[str]:
    """Return source labels allowed for public guide surfaces."""
    titles: list[str] = []
    for source in source_manifest.get("sources", []):
        if source.get("privacy") != "public":
            continue
        if source.get("withheld_reason"):
            continue
        used_for = source.get("used_for", [])
        if not isinstance(used_for, list) or "public_guide" not in used_for:
            continue
        titles.append(source.get("public_label") or source.get("source_id", "source"))
    return titles


def build_guides(seed_spec: dict[str, Any], source_manifest: dict[str, Any]) -> dict[str, str]:
    """Build concise guide surfaces from canonical fields."""
    project = seed_spec["project"]
    public_sources = public_source_titles(source_manifest)
    name = project["name"]
    intent = project["intent"]
    product = project["product"]
    common_boundary = (
        "Guides explain RepoKernel contracts. They do not redefine authority, "
        "grant writes, install Seed or enable runtime operation."
    )
    return {
        GUIDE_FILES["architecture"]: f"# Architecture\n\n{name} uses RepoKernel as a Project Kernel compiler.\n\nIntent: {intent}\n\nProduct: {product}\n\nBoundary: {common_boundary}\n",
        GUIDE_FILES["user"]: f"# User Guide\n\nUse RepoKernel to choose Direct Start, Synthesis, Retrofit or Observe-and-Propose.\n\nApproval is required before writes, publication, Seed promotion or runtime use.\n\nPublic sources: {', '.join(public_sources) or 'none declared'}.\n",
        GUIDE_FILES["coder"]: "# Coder Guide\n\nImplement against SourceManifest, ProjectModel, SeedSpec, GenerationPlan, ActivationReport and SkillRegistry.\n\nRun tests before changing generator behavior. Preserve dry-run/no-overwrite behavior.\n",
        GUIDE_FILES["use_cases"]: "# Use Cases\n\n- software repository\n- AI/RAG project\n- editorial project\n- business operating function\n- research lab\n- creator portfolio\n",
        GUIDE_FILES["application_types"]: "# Application Types\n\nDirect Start creates a new kernel. Synthesis compiles from sources. Retrofit proposes a compatible overlay. A1 observe-and-propose inspects without writes.\n",
    }
