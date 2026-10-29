# Review signals and completion checklist

Apply these detailed rules when the core skill routes you to this concern. Preserve equivalent repository conventions; examples are illustrative.

## Amber / red flags

Amber (watch):
- simple changes repeatedly touch multiple capabilities,
- cross-capability imports begin appearing,
- orchestration files grow rapidly,
- duplicate logic appears across capabilities,
- onboarding feedback says "hard to know where to start".

Red (act now):
- deep imports across capabilities become normal,
- a single capability, orchestration, service, or adapter file exceeds roughly 1,000 source lines of code (SLOC),
- orchestration becomes a rule monolith,
- CI slows and teams compensate with long-lived branches.

Standard responses:
- duplication -> promote once abstraction is obvious,
- oversized capability -> split into sibling capabilities,
- oversized orchestration -> split workflows and push rules back into capabilities,
- cross-imports -> enforce public surfaces and refactor immediately.
## Sizing rules

Use size as a smoke alarm, not dogma.

- Rough threshold: ~1K SLOC in one adapter/service/orchestration/capability file is a boundary warning.
- If one behaviour lifecycle requires hunting across many folders, boundary placement is wrong.
## Review/refactor checklist

1. Start every new behaviour inside an owned capability boundary.
2. Verify each capability exposes a clear public surface appropriate to the ecosystem.
3. Remove deep imports and replace with public-surface imports.
4. Keep cross-capability sequencing in the established orchestration surface.
5. Track repeated logic and promote only when abstraction is obvious.
6. Split oversized capabilities/workflows before they become team bottlenecks.
7. In workspaces, follow the configured `apps/*`, `packages/*`, `libs/*`, or equivalent project roots and remove direct internal cross-boundary imports.
