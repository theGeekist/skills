---
name: backend-slice-architecture
description: "Use when creating, refactoring, reviewing, or incrementally migrating backend architecture towards a capability-first, package-shaped model with explicit public APIs, clear orchestration, and earned shared infrastructure across apps, packages, libraries, modules, or equivalent project roots."
license: MIT
metadata:
  author: Geekist
  homepage: https://geekist.co
---

# Backend architecture

Keep related backend behaviour together, protect its public interface and make cross-capability coordination explicit. Apply this model when the user chooses it or requests a review against it.

Organisation, rephrasing and simplification must preserve every architecture rule, exception and intended meaning. Architectural rule changes require the user's explicit approval; the writing baseline changes how rules are communicated, not what they require.

<!-- shared-baseline:start -->
Use current project terms and decisions. Explain an unfamiliar term near its first consequential use; distinguish a proposed meaning from an accepted one. Preserve exact identifiers and technical constraints.

Lead with the reader's purpose and main point, then explain the consequences and supporting detail. Make substantial technical material navigable by a reader outside engineering, with descriptive headings and meaningful source links. Match depth to the request; use British English in authored prose.

Keep implementation progress separate from validation. Pair a material evidence gap with a bounded next action and completion evidence. Missing prior proof alone does not reject an option or halt authorised work. Name actual blockers precisely, continue independent authorised work, and preserve existing authorisation.

Check consistency, accessibility, readability and repeatability. Use sources for claims and real events for progress. Preserve uncertainty that affects a decision without inventing certainty or unnecessary approval gates.
<!-- shared-baseline:end -->

## Start with the repository

Read existing instructions, decisions, project metadata and affected code before recommending placement. Preserve equivalent repository and framework conventions. These are strong defaults, not permission to rename roots or reorganise unrelated code. Depart from a default for a concrete local reason and keep the affected boundary consistent.

A **capability** owns a cohesive area's rules, state and implementation. Its **public surface** is the operations and types other parts may use; a **deep import** bypasses that interface to reach internals. **Package-shaped** means independently testable with an explicit public surface and enforceable dependencies, without requiring a `package.json`, a publishable package or a top-level `packages` directory.

These operating rules support legibility, autonomy and predictable change. They do not require strict adherence to domain-driven design (DDD), Hexagonal, Clean or model–view–controller (MVC) architecture.

## Keep the decision core

- Start new behaviour inside its owning capability unless it is explicitly independent of capability-specific rules from day one. Keep capability internals owned and private.
- Keep independently owned capabilities as peers. Domain grouping directories are acceptable when they create no hidden ownership or import boundary. Determine whether an apparently nested capability is truly an internal implementation detail before splitting it.
- Place cross-capability sequencing and coordination in the established application, use-case or workflow surface. This **orchestration** composes capabilities; their rules remain inside them.
- Orchestration may depend on capability public surfaces. Capabilities may depend on approved agnostic shared boundaries: shared code independent of capability-specific rules and assumptions. A narrow, natural dependency on a sibling's public surface is allowed when clearer than orchestration; it must not become workflow sequencing or coordination. Investigate a growing sibling-dependency graph rather than automatically rejecting it.
- Give every capability an ecosystem-appropriate public surface and mechanically block deep imports. Expose a small set of commands, queries, use cases, boundary data types and optional events; keep internal persistence models, internal helper utilities and volatile domain objects private.
- Allow early duplication. **Promotion** moves repeated reusable behaviour from capability-local code to shared code. Promote when two or more capabilities independently implement the same concept, repeated edits cause friction and the abstraction is clear. Shared code must have no business semantics, remain stable and reusable without leaking assumptions, and prevent correctness, security or consistency harm from duplication. Avoid reversing the local-to-shared direction.
- Prefer shallow internals and descriptive filenames. Preserve recognised framework forms and local compound-name conventions. Add directories for real boundaries, generated-code isolation, framework requirements, substantial growth or improved navigation; avoid speculative taxonomy and repeated capability prefixes.
- Treat application programming interfaces (APIs), command-line interfaces and external software development kits (SDKs) as delivery adapters. Requests map to orchestration. An internal SDK exposes capability public surfaces; an external SDK is built from transport contracts.
- Keep internationalisation and configuration in the design from the start. The originating capability owns string meaning; locale-sensitive presentation stays near delivery; machine identifiers remain language-neutral. Compose locale/configuration in the runtime shell and supply capabilities with required values.
- Follow configured workspace roots: `apps`, `packages`, `libs` or equivalents can express the same roles. Folder names alone do not determine architecture. Share orchestration across multiple runtimes rather than duplicating it.
- Migrate through real work: add behaviour in the appropriate existing boundary and move old code only when touched. Treat architecture smells as action triggers. Watch amber signals and act on red signals using the required review reference. Roughly 1,000 source lines in one file is a boundary warning; size is a smoke alarm, not dogma.

## Load only the relevant detail

Read the indicated reference **before deciding or changing that concern**. A full architecture review needs all three; a narrow request needs only the relevant reference and this core.

| Concern | Required reference |
| --- | --- |
| File placement/naming, shared-code promotion, interfaces, delivery, locale or configuration | [Placement and contracts](references/placement-and-contracts.md) |
| Workspace roles, multiple runtimes, migration, enforcement tools or folder examples | [Workspace and migration](references/workspace-and-migration.md) |
| Architecture review, sizing, dependency smells or refactor completion | [Review signals and checklist](references/review.md) |

Each reference preserves the detailed rules; examples illustrate options rather than mandate a stack. Use the smallest relevant section, and avoid loading examples for unrelated ecosystems.

## Explain the recommendation

Give the affected boundary, evidence and smallest useful change before optional mechanisms. Link to current code, decisions and the relevant detailed rule. Preserve the shared baseline above when explaining proposals, evidence gaps and practical consequences to technical and business readers.

## Sources and inspiration

For the origin of these rules and the writing guidance applied to them, see [sources and local adaptation](references/placement-and-contracts.md#sources-and-local-adaptation). This source note supports attribution; it does not add another required research read.
