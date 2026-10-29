# Placement and public contracts

Read these original rules before deciding or changing this concern.

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

## Capability public surface contract

Expose:
- small set of commands/queries/use-cases,
- boundary DTO-like types,
- optionally emitted events.

Do not expose:
- internal persistence models,
- internal helper utilities,
- volatile domain objects.
