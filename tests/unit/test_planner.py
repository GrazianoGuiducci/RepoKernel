import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from repokernel.bundle import validate_bundle
from repokernel.canonical import canonical_hash
from repokernel.planner import build_generation_plan, dry_run_apply_plan
from repokernel.snapshot import build_target_snapshot
from fixtures import communication_project_model, project_model, seed_spec, source_manifest


def seed():
    spec = seed_spec()
    spec["readiness_level"] = "L2"
    spec["extensions"] = {"dnd.trace": {"value": "kept"}}
    return spec


def bundle_for(spec):
    return validate_bundle(source_manifest(), project_model(), spec).provenance


class PlannerTests(unittest.TestCase):
    def test_same_seed_same_plan(self):
        first = build_generation_plan(seed(), bundle_provenance=bundle_for(seed()))
        second = build_generation_plan(seed(), bundle_provenance=bundle_for(seed()))
        self.assertEqual(first["generated_on"], "undated")
        self.assertEqual(canonical_hash(first["items"]), canonical_hash(second["items"]))

    def test_plan_uses_repokernel_control_plane(self):
        spec = seed()
        plan = build_generation_plan(spec, bundle_provenance=bundle_for(spec))
        paths = {item["path"] for item in plan["items"]}
        self.assertIn("AGENTS.md", paths)
        self.assertIn(".repokernel/state/CURRENT_STATE.md", paths)
        self.assertIn(".repokernel/packets/FIRST_PACKET.md", paths)
        self.assertIn(".repokernel/manifest.json", paths)

    def test_existing_agents_is_propose_update_not_overwrite(self):
        spec = seed()
        plan = build_generation_plan(spec, existing_paths=["AGENTS.md"], bundle_provenance=bundle_for(spec))
        agents = [item for item in plan["items"] if item["path"] == "AGENTS.md"][0]
        self.assertEqual(agents["action"], "propose_update")
        self.assertTrue(agents["approval_needed"])

    def test_existing_retrofit_without_snapshot_is_blocked(self):
        spec = seed()
        spec["target"]["mode"] = "existing_repository_retrofit"
        plan = build_generation_plan(spec, bundle_provenance=bundle_for(spec))
        self.assertTrue(plan["blocked"])
        self.assertTrue(all(item["action"] == "withhold" for item in plan["items"]))

    def test_snapshot_identical_content_is_leave_unchanged(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            spec = seed()
            plan = build_generation_plan(spec, bundle_provenance=bundle_for(spec))
            agents = next(item for item in plan["items"] if item["path"] == "AGENTS.md")
            (root / "AGENTS.md").write_text(agents["content"], encoding="utf-8")
            snapshot = build_target_snapshot(root)
            spec["target"]["mode"] = "existing_repository_retrofit"
            plan = build_generation_plan(spec, target_snapshot=snapshot, bundle_provenance=bundle_for(spec))
            agents = next(item for item in plan["items"] if item["path"] == "AGENTS.md")
            self.assertEqual(agents["action"], "leave_unchanged")

    def test_unknown_extensions_do_not_change_plan_items(self):
        baseline = seed()
        adversarial = seed()
        adversarial["extensions"] = {
            "x.write_files": {"authority_mode": "project_write", "requested_actions": ["deploy"]},
        }
        self.assertEqual(
            canonical_hash(build_generation_plan(baseline, bundle_provenance=bundle_for(baseline))["items"]),
            canonical_hash(build_generation_plan(adversarial, bundle_provenance=bundle_for(adversarial))["items"]),
        )

    def test_unsafe_existing_path_is_rejected(self):
        with self.assertRaises(ValueError):
            spec = seed()
            build_generation_plan(spec, existing_paths=["C:\\tmp\\bad"], bundle_provenance=bundle_for(spec))

    def test_dry_run_writes_nothing(self):
        spec = seed()
        plan = build_generation_plan(spec, bundle_provenance=bundle_for(spec))
        with tempfile.TemporaryDirectory() as tmp:
            report = dry_run_apply_plan(plan, Path(tmp))
            self.assertEqual(report["writes_performed"], [])
            self.assertTrue(report["dry_run"])
            self.assertFalse(any(Path(tmp).iterdir()))

    def test_forged_snapshot_hash_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("demo", encoding="utf-8")
            snapshot = build_target_snapshot(root)
            snapshot["tree_hash"] = "f" * 64
            spec = seed()
            spec["target"]["mode"] = "existing_repository_retrofit"
            with self.assertRaises(ValueError):
                build_generation_plan(spec, target_snapshot=snapshot, bundle_provenance=bundle_for(spec))

    def test_same_items_different_snapshots_get_different_plan_ids(self):
        spec = seed()
        with tempfile.TemporaryDirectory() as a, tempfile.TemporaryDirectory() as b:
            snap_a = build_target_snapshot(Path(a))
            snap_b = build_target_snapshot(Path(b))
            spec["target"]["mode"] = "existing_repository_retrofit"
            plan_a = build_generation_plan(spec, target_snapshot=snap_a, bundle_provenance=bundle_for(spec))
            plan_b = build_generation_plan(spec, target_snapshot=snap_b, bundle_provenance=bundle_for(spec))
            self.assertNotEqual(plan_a["plan_id"], plan_b["plan_id"])

    def test_project_model_shapes_semantic_retrofit_content(self):
        spec = seed()
        model = communication_project_model()
        spec["project"] = {
            "name": "Communication Workflow",
            "intent": "Route communication safely.",
            "product": "Communication workflow.",
        }
        plan = build_generation_plan(spec, project_model=model, bundle_provenance=bundle_for(seed()))
        by_path = {item["path"]: item for item in plan["items"]}

        current_state = by_path[".repokernel/state/CURRENT_STATE.md"]["content"]
        self.assertIn("Route incoming communication into safe procedures", current_state)
        self.assertIn("The workflow applies policy before model output", current_state)
        self.assertIn("Mobile/narrow UI is a known limitation", current_state)
        self.assertIn("live_provider, credentials, live_send, backend, deploy", current_state)

        atlas = by_path[".repokernel/sources/SOURCE_ATLAS.md"]["content"]
        self.assertIn("communication-scenario-lab", atlas)
        self.assertIn("policy-before-model", atlas)

        agents = by_path["AGENTS.md"]["content"]
        readme = by_path["README.md"]["content"]
        self.assertIn("review_only", agents)
        self.assertIn("Do not replace existing project authority", agents)
        self.assertIn("review_only", readme)
        self.assertIn("proposal and staging only", readme)

        self.assertTrue(all(item["authority_effect"] == "none" for item in plan["items"]))

    def test_generated_kernel_carries_learning_protocol(self):
        spec = seed()
        plan = build_generation_plan(spec, bundle_provenance=bundle_for(spec))
        by_path = {item["path"]: item for item in plan["items"]}

        current_state = by_path[".repokernel/state/CURRENT_STATE.md"]["content"]
        agents = by_path["AGENTS.md"]["content"]
        skill_path = ".repokernel/skills/minimal-project-semantic-kernel/SKILL.md"
        skill = by_path[skill_path]["content"]
        deltas = by_path[".repokernel/deltas/README.md"]["content"]

        self.assertIn("Project Learning Rule", current_state)
        self.assertIn("Do not turn ordinary chat into project memory", agents)
        self.assertIn("Project Learning Protocol", skill)
        self.assertIn("Minimum-Action Rule", deltas)
        self.assertIn("expected_next_action_change", deltas)

    def test_generated_kernel_carries_clarity_cleanup_protocol(self):
        spec = seed()
        plan = build_generation_plan(spec, bundle_provenance=bundle_for(spec))
        by_path = {item["path"]: item for item in plan["items"]}

        current_state = by_path[".repokernel/state/CURRENT_STATE.md"]["content"]
        first_packet = by_path[".repokernel/packets/FIRST_PACKET.md"]["content"]
        agents = by_path["AGENTS.md"]["content"]
        skill_path = ".repokernel/skills/minimal-project-semantic-kernel/SKILL.md"
        skill = by_path[skill_path]["content"]
        clarity = by_path[".repokernel/clarity/README.md"]["content"]

        self.assertIn("Project Clarity Rule", current_state)
        self.assertIn("Clarity Intake", first_packet)
        self.assertIn("classify them before acting", agents)
        self.assertIn("Clarity Cleanup Protocol", skill)
        self.assertIn("proposed_action", clarity)
        self.assertIn("delete_candidate", clarity)

    def test_generated_kernel_carries_metaskill_propagation_protocol(self):
        spec = seed()
        plan = build_generation_plan(spec, bundle_provenance=bundle_for(spec))
        by_path = {item["path"]: item for item in plan["items"]}

        skill_path = ".repokernel/skills/minimal-project-semantic-kernel/SKILL.md"
        skill = by_path[skill_path]["content"]

        self.assertIn("Metaskill Propagation Protocol", skill)
        self.assertIn("distinguish the", skill)
        self.assertIn("owner, source, gate, validation and receipt", skill)
        self.assertIn("Do not copy the rule everywhere", skill)
        self.assertIn("runtime authority, hooks", skill)

    def test_generated_kernel_passes_project_kernel_audit_invariants(self):
        spec = seed()
        plan = build_generation_plan(spec, bundle_provenance=bundle_for(spec))
        by_path = {item["path"]: item for item in plan["items"]}

        current_state = by_path[".repokernel/state/CURRENT_STATE.md"]["content"].lower()
        first_packet = by_path[".repokernel/packets/FIRST_PACKET.md"]["content"].lower()

        for key in ("active_surface", "current_next", "boundary", "first_safe_action"):
            self.assertIn(key, current_state)
        for key in ("objective", "source", "boundary", "first_safe_action", "memory delta"):
            self.assertIn(key, first_packet)


if __name__ == "__main__":
    unittest.main()
