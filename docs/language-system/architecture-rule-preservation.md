# Preserve the user-owned architecture rules

The backend and frontend rules are authoritative. Organisation, rephrasing and simplification must preserve every rule, exception and intended meaning. Architectural changes require explicit user approval.

## Correction after the language refactor

An independent audit of each skill against the pre-language-system source at `fcbd5a9` found conflicting summaries: backend red/action signals had been softened, locale proximity had become ownership, shared boundaries had been narrowed, and frontend summaries added independent testability and an approval qualifier. Detailed references largely retained the original rules, but that did not make conflicting summaries acceptable.

The correction removes the rewritten decision cores. The original introductions, authority guidance, mental models and strong defaults are restored in the main skills; every remaining original section is retained verbatim in the three concern-specific references. The writing baseline governs communication and cannot override architectural rules.

`standards/architecture-rules/` stores the exact pre-refactor source. `tests/test_architecture_rule_preservation.py` checks that every original second-level section remains verbatim in the main skill or a bundled reference. This verifies textual preservation; future changes to the authoritative snapshots require explicit approval rather than updating a fixture merely to make a test pass.
