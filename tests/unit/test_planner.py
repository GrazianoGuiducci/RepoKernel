import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from repokernel.canonical import canonical_hash
from repokernel.planner import build_generation_plan, dry_run_apply_plan
from repokernel.snapshot import build_target_snapshot


def seed():
    return {
        "schema": "repokernel.seed-spec.v1",
        "version": "repokernel.seed-spec.v1",
        "seed_id": "demo-seed",
        "source_manifest_hash": "0" * 64,
        "project_model_hash": "0" * 64,
        "canonical_namespace": ".repokernel",
        "project": {
            "name": "Demo Project",
            "intent": "Preserve continuity",
            "product": "A test project kernel",
        },
        "target": {"mode": "new_repository", "path": "demo"},
        "readiness_level": "L2",
        "authority_mode": "propose",
        "review": {
            "status": "accepted",
            "accepted_by_role": "operator",
            "accepted_at": "2026-06-25",
            "review_cycle": "RK-RVW-20260625-01",
        },
        "compiler_compatibility": {"package_version": "0.3.0.dev0"},
        "file_plan_policy": "stage_only",
        "validation_plan": ["validate-spec", "plan", "stage"],
        "extensions": {"dnd.trace": {"value": "kept"}},
    }


class PlannerTests(unittest.TestCase):
    def test_same_seed_same_plan(self):
        first = build_generation_plan(seed())
        second = build_generation_plan(seed())
        self.assertEqual(first["generated_on"], "undated")
        self.assertEqual(canonical_hash(first["items"]), canonical_hash(second["items"]))

    def test_plan_uses_repokernel_control_plane(self):
        plan = build_generation_plan(seed())
        paths = {item["path"] for item in plan["items"]}
        self.assertIn("AGENTS.md", paths)
        self.assertIn(".repokernel/state/CURRENT_STATE.md", paths)
        self.assertIn(".repokernel/packets/FIRST_PACKET.md", paths)
        self.assertIn(".repokernel/manifest.json", paths)

    def test_existing_agents_is_propose_update_not_overwrite(self):
        plan = build_generation_plan(seed(), existing_paths=["AGENTS.md"])
        agents = [item for item in plan["items"] if item["path"] == "AGENTS.md"][0]
        self.assertEqual(agents["action"], "propose_update")
        self.assertTrue(agents["approval_needed"])

    def test_existing_retrofit_without_snapshot_is_blocked(self):
        spec = seed()
        spec["target"]["mode"] = "existing_repository_retrofit"
        plan = build_generation_plan(spec)
        self.assertTrue(plan["blocked"])
        self.assertTrue(all(item["action"] == "withhold" for item in plan["items"]))

    def test_snapshot_identical_content_is_leave_unchanged(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            spec = seed()
            plan = build_generation_plan(spec)
            agents = next(item for item in plan["items"] if item["path"] == "AGENTS.md")
            (root / "AGENTS.md").write_text(agents["content"], encoding="utf-8")
            snapshot = build_target_snapshot(root)
            spec["target"]["mode"] = "existing_repository_retrofit"
            plan = build_generation_plan(spec, target_snapshot=snapshot)
            agents = next(item for item in plan["items"] if item["path"] == "AGENTS.md")
            self.assertEqual(agents["action"], "leave_unchanged")

    def test_unknown_extensions_do_not_change_plan_items(self):
        baseline = seed()
        adversarial = seed()
        adversarial["extensions"] = {
            "x.write_files": {"authority_mode": "project_write", "requested_actions": ["deploy"]},
        }
        self.assertEqual(
            canonical_hash(build_generation_plan(baseline)["items"]),
            canonical_hash(build_generation_plan(adversarial)["items"]),
        )

    def test_unsafe_existing_path_is_rejected(self):
        with self.assertRaises(ValueError):
            build_generation_plan(seed(), existing_paths=["C:\\tmp\\bad"])

    def test_dry_run_writes_nothing(self):
        plan = build_generation_plan(seed())
        with tempfile.TemporaryDirectory() as tmp:
            report = dry_run_apply_plan(plan, Path(tmp))
            self.assertEqual(report["writes_performed"], [])
            self.assertTrue(report["dry_run"])
            self.assertFalse(any(Path(tmp).iterdir()))


if __name__ == "__main__":
    unittest.main()
