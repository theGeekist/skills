---
name: backend-slice-architecture
description: Use when creating, refactoring, reviewing, or incrementally migrating backend architecture towards a capability-first, package-shaped model with explicit public APIs, clear orchestration, and earned shared infrastructure across apps, packages, libraries, modules, or equivalent project roots.
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

Use a capability-first, package-shaped backend where behaviour starts inside an owned capability boundary and is promoted outward only when it becomes genuinely agnostic.

`Package-shaped` describes an independently testable boundary with an explicit public surface and enforceable dependencies. It does not require a `package.json`, a publishable package, or a top-level directory named `packages`.

Do not treat this as a strict DDD/Hexagonal/Clean/MVC doctrine. Treat it as operating rules that optimise legibility, autonomy, and predictable change.

## Core mental model

Two homes, one direction of travel:

1. Capability boundary (default)
- Place capability-specific behaviour in the repository's established package, library, module, or source boundary.
- In workspaces this commonly means `packages/<capability>` or `libs/<capability>`.
- In a single-package service this commonly means `src/<capability>` or `src/modules/<capability>`.
- Let each capability own its internals.

2. Agnostic shared boundary (earned)
- Keep reusable infrastructure and cross-cutting helpers in the repository's established shared packages, libraries, adapters, or services only when genuinely capability-agnostic.

Direction of travel: capability -> shared through promotion. Avoid reverse movement.

Orchestration is one explicit role:
- Place cross-capability stories in the repository's application, use-case, workflow, or runtime composition surface.
- Do not allow capabilities to coordinate other capabilities implicitly.

## Strong defaults

These are decision guides, not filesystem directives. Follow established repository and framework conventions when they express the same ownership and dependency boundaries. Depart from a default when the local context provides a concrete reason, and preserve consistency within the affected boundary.

1. Start in a capability
- Implement new behaviour inside an owned capability boundary unless it is explicitly agnostic from day one.

2. Isolate capabilities
- Avoid reaching into another capability's internals.
- Depend only on another capability's public surface.

3. Keep orchestration explicit
- Put cross-capability sequencing and coordination in the repository's established orchestration surface.
- Compose capability behaviour there; do not move capability rules there.

4. Do not hide capability boundaries
- Do not make an independently owned capability an internal implementation detail of another capability.
- Organisational grouping directories are fine when they do not create ownership or import boundaries.
- Keep independently owned capabilities as peers within the relevant grouping and coordinate them explicitly.

5. Earn promotion through repetition
- Allow early duplication.
- Promote only when repetition is visible and painful.

6. Make public surfaces explicit
- Give every capability a front door appropriate to the ecosystem, such as package exports, `index.ts`, `public.ts`, module visibility, or an equivalent public API.
- Block deep imports.

7. Surface amber/red flags
- Treat architecture smells as action triggers, not style debates.

## File naming and nesting

Prefer shallow capability internals. Add meaning to filenames before adding directories.

- Name a file for its primary operation, subject, boundary, or responsibility.
- Do not repeat the enclosing capability name merely to make a filename globally unique.
- Choose the repository's established ordering for compound names, whether modifier-subject (`<modifier>-<subject>`) or subject-modifier (`<subject>-<modifier>`), and use it consistently when combining comparable name parts.
- Do not force unlike names into artificial grammar: operations, subjects, roles, platform suffixes, and framework suffixes may have different established forms.
- Preserve framework-required and tool-recognised forms such as `.controller`, `.module`, `.route`, `.test`, `.spec`, `.schema`, platform suffixes, and generated filenames.
- Prefer additional descriptive filenames over type-based directories such as `services/`, `handlers/`, or `utils/` while the capability remains easy to scan.
- Strongly discourage nesting introduced only for taxonomy, anticipated growth, or file count aesthetics.
- Add a directory only when substantial growth, a genuine internal boundary, generated-code isolation, framework requirements, or materially improved navigation justifies it.

For example, prefer a shallow capability such as:

```text
packages/checkout/src/
  create-order.ts
  calculate-total.ts
  order-repository.ts
  routes.ts
  public.ts
```

over repeating `checkout` in every filename or creating speculative `services/`, `repositories/`, and `handlers/` layers.

## Key concepts

### Capability

Treat a capability as a cohesive unit with:
- its own rules/state,
- internal implementation ownership,
- a clear public surface,
- future extractability.

Capabilities can include business capabilities (Checkout), decision surfaces (Pricing), technical capabilities (Auth), and UI-adjacent backend capabilities (Template renderer).

### Orchestration surface

Use the repository's application, use-case, workflow, or composition boundary to:
- sequence capabilities,
- handle cross-capability flow concerns (idempotency, retries, sagas/workflows),
- map success/failure story paths.

Do not encode capability rules here.

### Global agnostic layer

Keep this layer intentionally small:
- adapter boundaries, which may be named `adapters/`, `infrastructure/`, `platform/`, or according to local convention: DB/HTTP/queue/cache/bus wrappers,
- cross-cutting service boundaries, which may be folders or workspace projects: logging, telemetry, idempotency, generic auth helpers,
- generic utilities with no business semantics.

## Rules for decisions

### Placement rules

Default placement: capability.

Place in global only if all are true:
- no business semantics,
- reusable across capabilities without leaking assumptions,
- behaviour is stable,
- duplication would harm correctness/security/consistency.

### Promotion rules

Promote when:
- 2+ capabilities independently implement the same concept,
- repeated edits create friction,
- abstraction is obvious (not speculative).

Promotion targets:
- the repository's cross-cutting service boundary for agnostic helpers,
- its adapter, infrastructure, or platform boundary for implementation wrappers,
- standalone capability only when clearly warranted.

### Dependency rules

- Orchestration may depend on capability public surfaces.
- Capabilities may depend on approved agnostic shared boundaries.
- Capabilities must not depend on other capabilities' internals.
- A capability may take a narrow, natural dependency on another capability's public surface when that is clearer than orchestration.
- Do not use sibling dependencies for sequencing or coordination; keep those in the established orchestration surface.
- Treat a growing sibling-dependency graph as a boundary signal to investigate, not as an automatic violation.

### Capability grouping rule

If Capability A appears to own Capability B, determine whether B is genuinely an internal implementation detail or an independently owned boundary. Keep independent capabilities as peers, which may sit beneath a shared domain grouping such as `packages/commerce/*` or `libs/commerce/*`. Move their coordination into the established orchestration surface.

## Amber / red flags

Amber (watch):
- simple changes repeatedly touch multiple capabilities,
- cross-capability imports begin appearing,
- orchestration files grow rapidly,
- duplicate logic appears across capabilities,
- onboarding feedback says "hard to know where to start".

Red (act now):
- deep imports across capabilities become normal,
- a single capability, orchestration, service, or adapter file exceeds roughly 1K SLOC,
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

## Delivery channels

Treat API/CLI/SDK as delivery adapters, not capabilities.

- HTTP/GraphQL/gRPC endpoints map requests to orchestration.
- CLI commands map to orchestration.
- Internal SDK is capability public surfaces.
- External SDK is a separate artifact built from transport contracts, not capability internals.

## Internationalisation and configuration

Treat internationalisation and configuration as normal architecture concerns from the start, even when the application initially has one language and one runtime configuration.

- Keep user-facing strings identifiable and owned by the capability that introduces them.
- This establishes where strings are managed before translation becomes necessary.
- Let the application or runtime shell compose locale behaviour and configuration sources.
- Add configuration requirements as capabilities are introduced or touched.
- Prefer cross-runtime primitives where practical. UnJS packages can be useful options without becoming required choices.
- Keep locale-sensitive presentation near delivery while the originating capability owns the meaning.
- Keep machine-facing identifiers, error codes and protocol values language-neutral.
- Resolve configuration during application composition and provide capabilities with the values they require.

## Workspace mapping

Follow the workspace's configured project roots. `apps/`, `packages/`, and `libs/` are equally sound project-root conventions when their actual roles and dependency boundaries are explicit. Folder names do not determine the architecture.

### Common roles

- `apps/*` commonly contains deployable runtime entrypoints (delivery + composition):
  - inbound adapters (HTTP/GraphQL/gRPC, workers, cron, CLI)
  - orchestration/workflows/use-cases (thin sequencing)
  - composition root (DI/config/bootstrap)

- `apps/*` may also contain capability or library projects when that is the repository's established convention.
- `packages/*` commonly contains workspace packages, including runtime applications, capability boundaries, and shared infrastructure. A package may be internal or publishable.
- `libs/*` serves the same architectural role in repositories and toolchains that use library-oriented vocabulary.
- Use project metadata, public surfaces, and runtime responsibility rather than the root folder name to determine a project's role.

Capability packages or libraries contain:
  - capability slices (default home for behaviour)
  - shared agnostic plumbing (earned home for adapters/services/utilities)

Rules:
- New behaviour starts in a capability project under the workspace's established `packages/*`, `libs/*`, or equivalent root.
- Cross-slice coordination lives in the app’s orchestration surface (or a shared orchestration package if multiple runtimes exist).
- Slices expose an ecosystem-appropriate public surface; deep imports into slice internals are disallowed.
- Promotion to shared packages happens only when repetition is visible and the abstraction is obvious.
- Do not introduce new naming taxonomies unless the repo already uses them.

### Multiple apps rule

- If only one backend runtime exists, orchestration can live in that app.
- If multiple runtimes exist (`api`, `worker`, `admin`), do not duplicate orchestration logic.
- Share orchestration in a package, or route both runtimes through common orchestration entrypoints.

### Path-of-correctness migration

- Do not move old code first.
- Add new behaviour to capability projects under the repository's established workspace roots.
- Keep runtime composition in the relevant application project, whether that lives under `apps/*`, `packages/*`, or another configured root.
- Migrate old areas only when touched by real work.

### Boundary enforcement

Enforce mechanically (lint/build/architecture tests), not by convention alone.

- Allow runtime applications to depend on capability public surfaces.
- Allow capability projects to depend on approved agnostic infrastructure projects.
- Disallow deep imports between capability internals.
- Require imports through the ecosystem's public-surface mechanism.

Typical tooling options:
- TypeScript: ESLint import rules + TS path mapping.
- Nx/Turborepo: module boundary rules.
- Java: package visibility + ArchUnit.

## Illustrative folder shapes

These are mappings of the same ownership model, not competing architectures or required names.

### JavaScript/TypeScript workspace with `apps` and `packages`

```text
apps/
  api/
    src/
      composition/
      workflows/

packages/
  checkout/
    src/
    package.json
  inventory/
    src/
    package.json
  observability/
    src/
    package.json
```

### Workspace with `apps` and `libs`

```text
apps/
  api/

libs/
  commerce/
    checkout/
    inventory/
  shared/
    observability/
```

### Workspace using `packages` for every project

```text
packages/
  api/
    src/
      composition/
  checkout/
    src/
  inventory/
    src/
  observability/
    src/
```

### Single-package service

```text
src/
  modules/
    checkout/
    inventory/
  application/
    workflows/
  infrastructure/
  main.ts

```

## Capability public surface contract

Expose:
- small set of commands/queries/use-cases,
- boundary DTO-like types,
- optionally emitted events.

Do not expose:
- internal persistence models,
- internal helper utilities,
- volatile domain objects.

## Evolution model

1. Start capability-local and ship.
2. Promote agnostic patterns once repetition is clear.
3. Split large capabilities into sibling capabilities.
4. Let orchestration grow as thin workflow maps, not rule dumps.
5. Let package/service extraction emerge naturally.

## Review/refactor checklist

1. Start every new behaviour inside an owned capability boundary.
2. Verify each capability exposes a clear public surface appropriate to the ecosystem.
3. Remove deep imports and replace with public-surface imports.
4. Keep cross-capability sequencing in the established orchestration surface.
5. Track repeated logic and promote only when abstraction is obvious.
6. Split oversized capabilities/workflows before they become team bottlenecks.
7. In workspaces, follow the configured `apps/*`, `packages/*`, `libs/*`, or equivalent project roots and remove direct internal cross-boundary imports.
