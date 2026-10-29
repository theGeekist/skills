"""Exercise the optional adapter as an actual subprocess receiving a Stop event."""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
ADAPTER = ROOT / "adapters/codex/stop-language.py"


class StopHookTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.registry = self.root / "terms.json"
        self.value = {
            "version": 1,
            "contexts": [{"id": "content", "name": "Content", "definition": "Writing project content."}],
            "concepts": [{
                "id": "content.confidence", "context": "content",
                "preferred_term": "Confidence", "definition": "Strength of supporting evidence.",
                "status": "accepted", "aliases": ["certainty"],
                "distinct_from": [], "labels": {"dashboard": "Evidence strength"},
                "sources": [{"path": "docs/assessment.md", "revision": "abc123"}],
            }],
        }
        self.save()

    def tearDown(self):
        self.temporary.cleanup()

    def save(self):
        self.registry.write_text(json.dumps(self.value), encoding="utf-8")

    def invoke(self, payload, *args, raw=False):
        result = subprocess.run(
            [sys.executable, str(ADAPTER), "--registry", str(self.registry), "--context", "content", *args],
            input=payload if raw else json.dumps(payload), capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        return json.loads(result.stdout)

    def event(self, message="Confidence is growing.", **extra):
        return {"hook_event_name": "Stop", "last_assistant_message": message, **extra}

    def test_clean_message_returns_empty_object(self):
        self.assertEqual(self.invoke(self.event()), {})

    def test_alias_requests_contextual_revision(self):
        result = self.invoke(self.event("certainty is growing."))
        self.assertEqual(result["decision"], "block")
        self.assertIn("certainty → Confidence", result["reason"])
        self.assertIn("Validate the context", result["reason"])
        self.assertIn("preserving meaning", result["reason"])

    def test_audience_label_is_used(self):
        result = self.invoke(self.event("certainty"), "--audience", "dashboard")
        self.assertIn("certainty → Evidence strength", result["reason"])

    def test_active_loop_guard_prevents_second_block(self):
        self.assertEqual(self.invoke(self.event("certainty", stop_hook_active=True)), {})

    def test_missing_null_or_empty_message_is_noop(self):
        for payload in ({"hook_event_name": "Stop"}, self.event(None), self.event("")):
            with self.subTest(payload=payload):
                self.assertEqual(self.invoke(payload), {})

    def test_wrong_event_fails_open(self):
        result = self.invoke({"hook_event_name": "SessionStart", "last_assistant_message": "certainty"})
        self.assertIn("systemMessage", result)
        self.assertNotIn("decision", result)

    def test_malformed_json_fails_open_without_echo(self):
        result = self.invoke('{"private-payload":', raw=True)
        self.assertIn("systemMessage", result)
        self.assertNotIn("private-payload", json.dumps(result))

    def test_malformed_payload_types_fail_open(self):
        for payload in ([], None, self.event(["certainty"]), self.event("certainty", stop_hook_active="true")):
            with self.subTest(payload=payload):
                result = self.invoke(payload)
                self.assertIn("systemMessage", result)
                self.assertNotIn("decision", result)

    def test_invalid_registry_fails_open_without_path_leak(self):
        self.registry.write_text("not JSON", encoding="utf-8")
        result = self.invoke(self.event("certainty"))
        self.assertIn("systemMessage", result)
        self.assertNotIn(str(self.root), json.dumps(result))

    def test_unknown_context_fails_open(self):
        result = self.invoke(self.event("certainty"), "--context", "missing")
        self.assertIn("systemMessage", result)
        self.assertNotIn("decision", result)

    def test_invalid_arguments_fail_open(self):
        result = self.invoke(self.event("certainty"), "--unknown")
        self.assertIn("systemMessage", result)

    def test_code_and_urls_do_not_trigger_continuation(self):
        result = self.invoke(self.event("`certainty`\n```\ncertainty\n```\nhttps://example.com/certainty"))
        self.assertEqual(result, {})

    def test_long_messages_get_bounded_deduplicated_feedback(self):
        self.value["concepts"][0]["aliases"] += ["assurance", "conviction", "belief"]
        self.save()
        result = self.invoke(self.event(("certainty assurance conviction belief\n" * 10000)))
        self.assertEqual(result["decision"], "block")
        self.assertLess(len(result["reason"]), 600)
        self.assertEqual(result["reason"].count("→"), 3)

    def test_example_configuration_is_json_with_static_command(self):
        config = json.loads((ROOT / "adapters/codex/hooks.example.json").read_text(encoding="utf-8"))
        command = config["hooks"]["Stop"][0]["hooks"][0]["command"]
        self.assertIn("/ABSOLUTE/PATH/", command)
        self.assertIn("--context content", command)
        self.assertNotIn("$", command)


if __name__ == "__main__":
    unittest.main()
