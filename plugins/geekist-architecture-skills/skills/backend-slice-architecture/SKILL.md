---
name: backend-slice-architecture
description: Use when creating, refactoring, reviewing, or incrementally migrating backend architecture towards a feature-first, package-shaped model with explicit public APIs, a clear orchestration surface, and earned shared infrastructure.
license: MIT
metadata:
  author: Geekist
  homepage: https://geekist.co
---

# Backend Architecture Playbook

Apply this architecture when the user chooses this model or asks for a review against it.

## Authority and adaptation

Inspect the repository's existing conventions and constraints before proposing placement or changes. Treat this playbook as an architecture lens and target direction, not permission to reorganise unrelated code. Preserve established naming where it expresses the same boundaries, and migrate existing systems through the work already in scope.

## What this architecture is

Use a feature-first, package-shaped backend where work starts local inside a feature/capability and is promoted outward only when it becomes genuinely agnostic.

Do not treat this as a strict DDD/Hexagonal/Clean/MVC doctrine. Treat it as operating rules that optimize legibility, autonomy, and predictable change.

## Core mental model

Two homes, one direction of travel:

1. `features/<capability>` (default)
- Place capability-specific behavior here.
- Let each feature own its internals.

2. Global agnostic layer (earned)
- Keep thin reusable plumbing in `adapters/` and `services/` only when truly capability-agnostic.

Direction of travel: feature -> global via promotion. Avoid reverse movement.

Orchestration is one surface:
- Place cross-capability stories in `application/`.
- Do not allow features to coordinate other features directly.

## Invariants (non-negotiable)

1. Start in a feature
- Implement new behavior in a feature unless it is explicitly agnostic from day one.

2. Isolate features
- Never reach into another feature's internals.
- Depend only on another feature's public surface.

3. Keep one orchestration surface
- Put cross-feature sequencing and coordination in `application/`.
- Compose feature behavior there; do not move feature rules there.

4. Do not nest features
- Never place one feature under another.
- Split into sibling capabilities and coordinate in orchestration.

5. Earn promotion through repetition
- Allow early duplication.
- Promote only when repetition is visible and painful.

6. Make public surfaces explicit
- Give every feature a front door (`index.ts` or `public.ts`).
- Block deep imports.

7. Surface amber/red flags
- Treat architecture smells as action triggers, not style debates.

## Key concepts

### Feature / capability

Treat a feature as a cohesive unit with:
- its own rules/state,
- internal implementation ownership,
- a clear public surface,
- future extractability.

Feature kinds can include business capabilities (Checkout), decision surfaces (Pricing), technical capabilities (Auth), and UI-adjacent backend capabilities (Template renderer).

### Orchestration surface

Use `application/` to:
- sequence features,
- handle cross-feature flow concerns (idempotency, retries, sagas/workflows),
- map success/failure story paths.

Do not encode feature domain rules here.

### Global agnostic layer

Keep this layer intentionally small:
- `adapters/`: DB/HTTP/queue/cache/bus wrappers,
- `services/`: logging, telemetry, idempotency, generic auth helpers,
- generic utilities with no business semantics.

## Rules for decisions

### Placement rules

Default placement: feature.

Place in global only if all are true:
- no business semantics,
- reusable across features without leaking assumptions,
- behavior is stable,
- duplication would harm correctness/security/consistency.

### Promotion rules

Promote when:
- 2+ features independently implement the same concept,
- repeated edits create friction,
- abstraction is obvious (not speculative).

Promotion targets:
- `services/` for cross-cutting helpers,
- `adapters/` for implementation wrappers,
- standalone capability only when clearly warranted.

### Dependency rules

- `application/` may depend on feature public surfaces.
- Features may depend on global `adapters/` and `services/`.
- Features must not depend on other features' internals.
- A feature may take a narrow, natural dependency on another feature's public surface when that is clearer than orchestration.
- Do not use sibling dependencies for sequencing or coordination; keep those in `application/`.
- Treat a growing sibling-dependency graph as a boundary signal to investigate, not as an automatic violation.

### No nesting rule

If Feature A appears to contain a sub-feature:
- split into Feature A + Feature B as siblings,
- move coordination into orchestration.

## Amber / red flags

Amber (watch):
- simple changes repeatedly touch multiple features,
- cross-feature imports begin appearing,
- orchestration files grow rapidly,
- duplicate logic appears across features,
- onboarding feedback says "hard to know where to start".

Red (act now):
- deep imports across features become normal,
- single feature/orchestration/service/adapters file exceeds roughly 1K SLOC,
- orchestration becomes a rule monolith,
- CI slows and teams compensate with long-lived branches.

Standard responses:
- duplication -> promote once abstraction is obvious,
- oversized feature -> split into sibling capabilities,
- oversized orchestration -> split workflows and push rules back into features,
- cross-imports -> enforce public surfaces and refactor immediately.

## Sizing rules

Use size as a smoke alarm, not dogma.

- Rough threshold: ~1K SLOC in one adapter/service/orchestration/feature file is a boundary warning.
- If one behavior lifecycle requires hunting across many folders, boundary placement is wrong.

## Delivery channels

Treat API/CLI/SDK as delivery adapters, not features.

- HTTP/GraphQL/gRPC endpoints map requests to orchestration.
- CLI commands map to orchestration.
- Internal SDK is feature public surfaces.
- External SDK is a separate artifact built from transport contracts, not feature internals.

## Internationalisation and configuration

Treat internationalisation and configuration as normal architecture concerns from the start, even when the application initially has one language and one runtime configuration.

- Keep user-facing strings identifiable and owned by the feature that introduces them.
- This establishes where strings are managed before translation becomes necessary.
- Let the application or runtime shell compose locale behaviour and configuration sources.
- Add configuration requirements as features are introduced or touched.
- Prefer cross-runtime primitives where practical. UnJS packages can be useful options without becoming required choices.
- Keep locale-sensitive presentation near delivery while the originating feature owns the meaning.
- Keep machine-facing identifiers, error codes and protocol values language-neutral.
- Resolve configuration during application composition and provide features with the values they require.

## Existing monorepo adaptation

Use this when a repo already has `apps/*` + `packages/*` and cannot be reorganized in one move.

### Monorepo mapping (naming-agnostic)

- Treat `apps/*` as runtime entrypoints (delivery + composition):
  - inbound adapters (HTTP/GraphQL/gRPC, workers, cron, CLI)
  - orchestration/workflows/use-cases (thin sequencing)
  - composition root (DI/config/bootstrap)

- Treat `packages/*` as extractable slices:
  - feature/capability slices (default home for behaviour)
  - shared agnostic plumbing (earned home for adapters/services/utilities)

Rules:
- New behaviour starts in a feature slice inside `packages/*`.
- Cross-slice coordination lives in the app’s orchestration surface (or a shared orchestration package if multiple runtimes exist).
- Slices expose a public API file; deep imports into slice internals are disallowed.
- Promotion to shared packages happens only when repetition is visible and the abstraction is obvious.
- Do not introduce new naming taxonomies unless the repo already uses them.

### Multiple apps rule

- If only one backend runtime exists, orchestration can live in that app.
- If multiple runtimes exist (`api`, `worker`, `admin`), do not duplicate orchestration logic.
- Share orchestration in a package, or route both runtimes through common orchestration entrypoints.

### Path-of-correctness migration

- Do not move old code first.
- Add a new lane for all new behavior:
- new capability packages in `packages/cap-*`,
- new platform packages in `packages/platform-*`,
- app orchestration under `apps/<runtime>/`.
- Migrate old areas only when touched by real work.

### Boundary enforcement

Enforce mechanically (lint/build/architecture tests), not by convention alone.

- Allow `apps/* -> packages/*`.
- Allow capability packages -> platform packages.
- Disallow deep imports between capability internals.
- Require imports from `index.ts` or `public.ts` only.

Typical tooling options:
- TypeScript: ESLint import rules + TS path mapping.
- Nx/Turborepo: module boundary rules.
- Java: package visibility + ArchUnit.

## Suggested folder shape

```text
features/
  <capability>/
    domain/      (optional)
    services/
    ports/
    adapters/    (optional)
    index.ts or public.ts

application/
  workflows/ or use-cases/

adapters/
  db, queues, cache, http, bus wrappers

services/
  logging, telemetry, idempotency, auth helpers

app/
  composition root, DI wiring, bootstrap
```

### Suggested folder shape (existing monorepo)

```text
apps/
  api/
    adapters/
    orchestration/
    app/
  worker/
    jobs/
    app/

packages/
  cap-checkout/
    domain/
    services/
    ports/
    public.ts
  cap-inventory/
  cap-pricing/

  platform-db/
  platform-messaging/
  platform-observability/

```

## Feature public surface contract

Expose:
- small set of commands/queries/use-cases,
- boundary DTO-like types,
- optionally emitted events.

Do not expose:
- internal persistence models,
- internal helper utilities,
- volatile domain objects.

## Evolution model

1. Start feature-local and ship.
2. Promote agnostic patterns once repetition is clear.
3. Split large features into sibling capabilities.
4. Let orchestration grow as thin workflow maps, not rule dumps.
5. Let package/service extraction emerge naturally.

## Review/refactor checklist

1. Start every new behavior in a feature.
2. Verify each feature exports a clear public API file.
3. Remove deep imports and replace with public-surface imports.
4. Keep cross-feature sequencing in `application/` only.
5. Track repeated logic and promote only when abstraction is obvious.
6. Split oversized features/workflows before they become team bottlenecks.
7. In monorepos, route all new work to `packages/cap-*` and remove direct cross-boundary imports.
