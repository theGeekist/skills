# Recognise architecture signals and complete the review

Architecture smells trigger action rather than style debates. Distinguish signals to watch from conditions requiring action now.

## Watch amber signals

Watch for simple changes repeatedly touching several capabilities, new cross-capability imports, rapidly growing orchestration files, repeated logic across capabilities and onboarding feedback that readers cannot find where to start.

## Act on red signals

Act now when deep imports across capabilities become normal, one capability/orchestration/service/adapter file exceeds roughly 1,000 source lines of code (SLOC), orchestration becomes a monolith of capability rules, or continuous integration (CI) slows and teams compensate with long-lived branches.

Use these responses:

| Signal | Response |
| --- | --- |
| Repeated logic | Promote once the abstraction is obvious |
| Oversized capability | Split into sibling capabilities |
| Oversized orchestration | Split workflows and return capability rules to their capabilities |
| Cross-imports | Enforce public interfaces and refactor immediately |

Use size as a smoke alarm, not dogma. Roughly 1,000 SLOC in one adapter, service, orchestration or capability file is a boundary warning. If understanding one behaviour's lifecycle requires searching across many folders, its boundary placement is wrong.

## Check the completed change

1. Start each new behaviour inside an owned capability boundary.
2. Verify that each capability has a clear public interface appropriate to its ecosystem.
3. Replace deep imports with imports through that interface.
4. Keep cross-capability sequencing in the established orchestration surface.
5. Track repeated logic and promote it only when the abstraction is obvious.
6. Split oversized capabilities and workflows before they become team bottlenecks.
7. In workspaces, follow the configured `apps/*`, `packages/*`, `libs/*` or equivalent roots, and remove direct imports into another boundary's internals.
