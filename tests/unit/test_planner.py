import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from repokernel.canonical import canonical_hash
from repokernel.planner import build_generation_plan, dry_run_apply_plan


def seed():
    return {
        "schema": "repokernel.seed-spec.v1",
        "seed_id": "demo-seed",
        "project": {
            "name": "Demo Project",
            "intent": "Preserve continuity",
            "product": "A test project kernel",
        },
        "target": {"mode": "new_repository", "path": "demo"},
        "readiness_level": "L2",
        "authority_mode": "propose",
        "extensions": {"dnd.trace": {"value": "kept"}},
    }


class PlannerTests(unittest.TestCase):
    def test_same_seed_same_plan(self):
        first = build_generation_plan(seed())
        second = build_generation_plan(seed())
        self.assertEqual(canonical_hash(first["items"]), canonical_hash(second["items"]))

    def test_existing_agents_is_propose_update_not_overwrite(self):
        plan = build_generation_plan(seed(), existing_paths=["AGENTS.md"])
        agents = [item for item in plan["items"] if item["path"] == "AGENTS.md"][0]
        self.assertEqual(agents["action"], "propose_update")
        self.assertTrue(agents["approval_needed"])

    def test_dry_run_writes_nothing(self):
        plan = build_generation_plan(seed())
        with tempfile.TemporaryDirectory() as tmp:
            report = dry_run_apply_plan(plan, Path(tmp))
            self.assertEqual(report["writes_performed"], [])
            self.assertTrue(report["dry_run"])
            self.assertFalse(any(Path(tmp).iterdir()))


if __name__ == "__main__":
    unittest.main()
