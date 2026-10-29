# Contributing

Issues and pull requests are welcome when they improve the architecture guidance without turning it into framework doctrine.

Changes should preserve these qualities:

- feature ownership is the default;
- public surfaces protect internals;
- cross-feature composition stays explicit;
- shared abstractions are earned through demonstrated reuse;
- existing repositories can migrate incrementally;
- examples illustrate options rather than mandate a stack or naming taxonomy.

Keep `SKILL.md` concise enough to load as agent context, with required references bundled inside the skill for independent installation. Put client-specific presentation metadata under `agents/`. Optional validation and adapters are described in [the language-system decision](docs/language-system/architecture.md). Do not add executable code, network dependencies or telemetry without an explicit design discussion.

Before proposing a change, validate each affected skill:

```sh
python /path/to/skill-creator/scripts/quick_validate.py skills/backend-slice-architecture
python /path/to/skill-creator/scripts/quick_validate.py skills/frontend-slice-architecture
```

Also test the changed skill against a realistic request. A wording check alone does not show that it makes good architecture decisions.

For language-system changes, run:

```sh
python3 scripts/sync-language-references.py --check
python3 scripts/check-language.py registry standards/terminology.json
python3 -m unittest discover -s tests -v
```

Change canonical references under `standards/`, then regenerate with `python3 scripts/sync-language-references.py`. Keep private project evidence out of this public repository. Record separate results for deterministic checks, independent agent review, human comprehension and actual runtime integration.
