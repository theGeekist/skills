# Contributing

Issues and pull requests are welcome when they improve the architecture guidance without turning it into framework doctrine.

Changes should preserve these qualities:

- feature ownership is the default;
- public surfaces protect internals;
- cross-feature composition stays explicit;
- shared abstractions are earned through demonstrated reuse;
- existing repositories can migrate incrementally;
- examples illustrate options rather than mandate a stack or naming taxonomy.

Keep `SKILL.md` self-contained and concise enough to load as agent context. Put client-specific presentation metadata under `agents/`. Do not add executable code, network dependencies or telemetry without an explicit design discussion.

Before proposing a change, validate each affected skill:

```sh
python /path/to/skill-creator/scripts/quick_validate.py skills/backend-slice-architecture
python /path/to/skill-creator/scripts/quick_validate.py skills/frontend-slice-architecture
```

Also test the changed skill against a realistic request. A wording check alone does not show that it makes good architecture decisions.
