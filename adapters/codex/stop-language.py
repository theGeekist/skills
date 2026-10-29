#!/usr/bin/env python3
"""Optional Stop continuation check using an explicitly configured registry.

See https://learn.chatgpt.com/docs/hooks. A block requests continuation; it does
not replace content that the interface may already have displayed. This adapter
is opt-in and fails open when its input or configuration cannot be checked.
"""

import argparse
import importlib.util
import json
from pathlib import Path
import sys


NOTICE = {"systemMessage": "Language check skipped: input or configuration could not be checked."}


def main(argv=None):
    class Parser(argparse.ArgumentParser):
        def error(self, message):
            raise ValueError("Invalid adapter arguments")

    parser = Parser(description=__doc__)
    parser.add_argument("--registry", required=True)
    parser.add_argument("--context", required=True)
    parser.add_argument("--audience")
    try:
        args = parser.parse_args(argv)
        payload = json.load(sys.stdin)
        if not isinstance(payload, dict) or payload.get("hook_event_name") != "Stop":
            raise ValueError("Expected Stop event")
        active = payload.get("stop_hook_active", False)
        if not isinstance(active, bool):
            raise ValueError("Invalid loop guard")
        if active:
            result = {}
        else:
            message = payload.get("last_assistant_message")
            if message is None or message == "":
                result = {}
            elif not isinstance(message, str):
                raise ValueError("Expected assistant text")
            else:
                checker_path = Path(__file__).resolve().parents[2] / "scripts/check-language.py"
                spec = importlib.util.spec_from_file_location("language_checker", checker_path)
                checker = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(checker)
                registry = checker.load_registry(args.registry)
                findings = checker.lint_text(message, registry, args.context, args.audience)
                if not findings:
                    result = {}
                else:
                    pairs = []
                    for finding in findings:
                        pair = (finding["term"], finding["preferred"])
                        if pair not in pairs:
                            pairs.append(pair)
                        if len(pairs) == 3:
                            break

                    def short(value):
                        # Keep one-line feedback bounded, even with unusual registry labels.
                        return " ".join(value.split())[:60]

                    suggestions = "; ".join(f"{short(term)} → {short(preferred)}" for term, preferred in pairs)
                    result = {
                        "decision": "block",
                        "reason": (
                            f"Check project terminology: {suggestions}. "
                            "Validate the context, then revise only relevant wording while preserving meaning."
                        ),
                    }
    except Exception:
        # Do not echo payloads, document text, filesystem paths or parser details.
        result = NOTICE
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
