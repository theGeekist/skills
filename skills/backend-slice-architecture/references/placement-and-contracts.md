# Place behaviour and protect public interfaces

Use this reference to decide where behaviour belongs, which imports are allowed and what a capability exposes.

## Find the relevant rule

- [Name files and add directories](#name-files-and-add-directories)
- [Identify ownership and coordination](#identify-ownership-and-coordination)
- [Choose local or shared code](#choose-local-or-shared-code)
- [Promote repeated behaviour](#promote-repeated-behaviour)
- [Control dependencies and grouping](#control-dependencies-and-grouping)
- [Connect delivery channels](#connect-delivery-channels)
- [Plan language and configuration](#plan-language-and-configuration)
- [Define the public contract](#define-the-public-contract)

## Name files and add directories

Prefer shallow capability internals. Give files descriptive names before adding directories.

- Name a file for its main operation, subject, boundary or responsibility. Avoid repeating the enclosing capability name solely to make the filename globally unique.
- Follow the repository's ordering for comparable compound names: modifier–subject or subject–modifier. Operations, subjects, roles, platform suffixes and framework suffixes can retain their own established forms; avoid imposing one grammar on unlike names.
- Preserve framework-required and tool-recognised names, including `.controller`, `.module`, `.route`, `.test`, `.spec`, `.schema`, platform suffixes and generated filenames.
- Prefer descriptive files to type-based directories such as `services/`, `handlers/` or `utils/` while the capability remains easy to scan.
- Strongly discourage nesting created only for taxonomy, anticipated growth or file-count aesthetics. Add a directory only for substantial growth, a genuine internal boundary, generated-code isolation, framework requirements or materially better navigation.

For example, a shallow checkout capability can contain:

```text
packages/checkout/src/
  create-order.ts
  calculate-total.ts
  order-repository.ts
  routes.ts
  public.ts
```

This avoids repeating `checkout` in each filename or introducing speculative service, repository and handler layers.

## Identify ownership and coordination

A **capability** is a cohesive unit with its own rules and state, ownership of its implementation, a clear public interface and the ability to be extracted later. It can represent a business capability such as Checkout, a decision area such as Pricing, a technical capability such as Auth or UI-adjacent backend behaviour such as a template renderer.

The **orchestration surface** is the established application, use-case, workflow or composition boundary. It sequences capabilities and maps success and failure paths. It also handles cross-capability retries, idempotency (preventing duplicate effects from repeated requests) and sagas (multi-step workflows with compensating actions). Capability rules stay inside their capability.

Keep the **global agnostic layer** small. “Agnostic” means independent of capability-specific rules and assumptions. It can contain:

- Adapter boundaries for database, HTTP, queue, cache and bus wrappers, named `adapters/`, `infrastructure/`, `platform/` or the local equivalent.
- Cross-cutting services, in folders or workspace projects, for logging, telemetry, idempotency and generic authentication helpers.
- Generic utilities with no business meaning.

## Choose local or shared code

Behaviour belongs in a capability by default. Place it globally only when **all four conditions** hold:

1. It has no business semantics.
2. It can be reused across capabilities without leaking assumptions.
3. Its behaviour is stable.
4. Duplication would harm correctness, security or consistency.

## Promote repeated behaviour

Allow early duplication. Promote code to a shared boundary when at least two capabilities independently implement the same concept, repeated edits create friction and the abstraction is obvious rather than speculative.

Use the repository's cross-cutting service boundary for agnostic helpers, and its adapter, infrastructure or platform boundary for implementation wrappers. Create a standalone capability only when clearly warranted. Move from capability-local code towards shared code; avoid reversing that direction.

## Control dependencies and grouping

- Orchestration may depend on capability public interfaces.
- Capabilities may depend on approved agnostic shared boundaries.
- Capabilities must use another capability's public interface and must not depend on its internals. A **deep import** bypasses that public interface.
- A narrow, natural dependency on another capability's public interface is allowed when clearer than orchestration. It must not sequence or coordinate capabilities; that work belongs in orchestration.
- Investigate a growing graph of sibling dependencies as a boundary signal. Its growth alone is not an automatic violation.

When Capability A appears to own Capability B, first establish whether B is an internal implementation detail or independently owned. Keep independent capabilities as peers and move their coordination to orchestration. They may share a domain grouping, such as `packages/commerce/*` or `libs/commerce/*`, provided the grouping creates no ownership or import boundary.

## Connect delivery channels

Treat application programming interfaces (APIs), command-line interfaces (CLIs) and software development kits (SDKs) as delivery adapters rather than capabilities.

HTTP, GraphQL and gRPC endpoints map requests to orchestration; CLI commands do the same. An internal SDK consists of capability public interfaces. An external SDK is a separate artefact built from transport contracts, rather than capability internals.

## Plan language and configuration

Include internationalisation and configuration from the start, even with one language and one runtime configuration.

- Keep user-facing strings identifiable and owned by the capability that introduces them. Establish where strings are managed before translation is needed.
- Let the application or runtime shell compose locale behaviour and configuration sources. Add configuration requirements as capabilities are introduced or touched.
- Prefer cross-runtime primitives where practical. UnJS packages are options, not requirements.
- Keep locale-sensitive presentation near delivery while the originating capability owns its meaning.
- Keep machine-facing identifiers, error codes and protocol values language-neutral.
- Resolve configuration during application composition, then supply each capability with the values it needs.

## Define the public contract

Expose a small set of commands, queries or use cases, boundary data types such as data transfer objects (DTOs), and optionally emitted events.

Keep internal persistence models, internal helper utilities and volatile domain objects private.

## Sources and local adaptation

The architecture rules are Jason's original backend rules, preserved from the [pre-language-system playbook](https://github.com/theGeekist/skills/blob/fcbd5a9/skills/backend-slice-architecture/SKILL.md). External writing frameworks inform their explanation and navigation; they do not establish or override these architectural requirements.

[Microsoft's simple-word guidance](https://learn.microsoft.com/en-us/style-guide/word-choice/use-simple-words-concise-sentences) informs concise wording. [Google's jargon guidance](https://developers.google.com/style/jargon) informs explanations near first use. These principles are adapted to British English and the project's existing terms.
