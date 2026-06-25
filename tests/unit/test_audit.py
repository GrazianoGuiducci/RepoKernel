import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from repokernel.audit import audit


ROOT = Path(__file__).resolve().parents[2]


class AuditTests(unittest.TestCase):
    def test_source_audit_reports_separate_readiness_axes(self):
        result = audit(ROOT, "repokernel-source")
        readiness = result["readiness"]
        self.assertIn("repository_structure_ready", readiness)
        self.assertIn("contract_conformant", readiness)
        self.assertIn("planner_conformant", readiness)
        self.assertIn("project_kernel_ready", readiness)
        self.assertIn("distribution_ready", readiness)

    def test_project_kernel_profile_accepts_repokernel_only_surface(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / ".repokernel/state").mkdir(parents=True)
            (root / ".repokernel/packets").mkdir(parents=True)
            (root / ".repokernel/sources").mkdir(parents=True)
            (root / ".repokernel/skills/demo-skill").mkdir(parents=True)
            (root / ".repokernel/state/CURRENT_STATE.md").write_text(
                "active_surface: demo\ncurrent_next: test\nboundary: none\nfirst_safe_action: audit\n",
                encoding="utf-8",
            )
            (root / ".repokernel/packets/FIRST_PACKET.md").write_text(
                "objective: demo\nsource: test\nboundary: none\nfirst_safe_action: audit\nmemory delta: none\n",
                encoding="utf-8",
            )
            (root / ".repokernel/sources/SOURCE_ATLAS.md").write_text(
                "| Path | Role |\n| --- | --- |\n| `.repokernel/state/CURRENT_STATE.md` | state |\n",
                encoding="utf-8",
            )
            (root / ".repokernel/skills/demo-skill/SKILL.md").write_text(
                "---\nname: demo-skill\ndescription: Demo skill for project-kernel audit.\n---\n",
                encoding="utf-8",
            )
            result = audit(root, "project-kernel")
            self.assertTrue(result["ready"], result["failed"])

    def test_source_audit_fails_when_contract_conformance_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for rel in [
                "docs",
                "skills/demo-skill",
                "scripts",
                "process/deltas",
                "process/evidence",
                "registry",
                "examples/minimal",
            ]:
                (root / rel).mkdir(parents=True, exist_ok=True)
            for rel in [
                "README.md",
                "AGENTS.md",
                "CURRENT_STATE.md",
                "repokernel.json",
                "registry/skills.json",
                "docs/readiness-levels.md",
                "docs/runtime-adapters.md",
                "process/FIRST_PACKET.md",
                "process/deltas/README.md",
                "process/evidence/README.md",
                "process/evidence/LOCAL_VALIDATION.md",
            ]:
                (root / rel).write_text("active_surface current_next boundary first_safe_action objective source memory delta {}", encoding="utf-8")
            (root / "registry/skills.json").write_text('{"schema":"repokernel.skill-registry.v1","skills":[]}', encoding="utf-8")
            (root / "examples/minimal/source-manifest.json").write_text("{}", encoding="utf-8")
            result = audit(root, "repokernel-source")
            self.assertFalse(result["ready"])
            self.assertFalse(result["readiness"]["contract_conformant"])


if __name__ == "__main__":
    unittest.main()
