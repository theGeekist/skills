---
name: frontend-slice-architecture
description: Use when creating, refactoring, reviewing, or incrementally migrating frontend architecture towards a feature-first, package-shaped model with explicit public APIs, thin scene-level composition, and earned shared UI and hooks.
license: MIT
metadata:
  author: Geekist
  homepage: https://geekist.co
---

# Frontend architecture

Keep related interface behaviour inside its feature. Let scenes bring features together, and move reusable code into shared locations only when repetition justifies it. Apply this model when the user chooses it or asks for a review against it.

## Preserve meaning when editing

Organisation, rephrasing and simplification must preserve every architectural rule, exception and intended meaning. Architectural changes require the user's explicit approval. The shared language baseline governs communication; it does not replace architecture rules.

<!-- shared-baseline:start -->
Use current project terms and decisions. Explain an unfamiliar term near its first consequential use; distinguish a proposed meaning from an accepted one. Preserve exact identifiers and technical constraints.

Lead with the reader's purpose and main point, then explain the consequences and supporting detail. Make substantial technical material navigable by a reader outside engineering, with descriptive headings and meaningful source links. Match depth to the request; use British English in authored prose.

Keep implementation progress separate from validation. Pair a material evidence gap with a bounded next action and completion evidence. Missing prior proof alone does not reject an option or halt authorised work. Name actual blockers precisely, continue independent authorised work, and preserve existing authorisation.

Check consistency, accessibility, readability and repeatability. Use sources for claims and real events for progress. Preserve uncertainty that affects a decision without inventing certainty or unnecessary approval gates.
<!-- shared-baseline:end -->

## Start with the existing project

Read the repository's instructions, framework and platform conventions, decisions and affected code before recommending placement. Preserve established names where they express the same boundaries. These are strong defaults: depart when the local context gives a concrete reason, while keeping the affected boundary consistent. Migrate through work already in scope rather than reorganising unrelated code. This model supports legibility, autonomy, predictable change and future packaging; it does not require React.

A **feature** owns related user interface (UI), state, hooks and local components. A **scene** is a page or screen shell that composes features. **Orchestration** means coordinating their workflow. A **hook** connects components to state or framework behaviour; an agent lifecycle hook is a different concept.

A feature's **public surface**, or public application programming interface (API), is what other code may use. A **deep import** bypasses that surface to reach implementation details. **Package-ready** means keeping boundaries and imports suitable for giving the feature its own `package.json` later.

## Keep behaviour with its owner

- Start new UI behaviour in `features/<feature>` unless it is explicitly independent of feature rules from day one. Keep feature-specific UI, state, hooks and components together.
- Keep independently owned features as siblings. Organisational grouping directories are acceptable when they add no ownership or import boundary. When a feature contains a sub-feature, split them into siblings and coordinate through scenes, or a thin shared composition helper when truly cross-platform.
- Scenes in `scenes/<platform>/` own pages, routes, layout and feature composition. Features expose capabilities; they do not directly coordinate other features.
- Give each feature a clear public surface such as `index.ts`, `index.js`, package exports or the local equivalent. Treat its internals as private and block deep imports mechanically.

## Share through repetition

**Promotion** moves reusable code from a feature into a shared location. The direction is feature to global; avoid reversing it. Allow early duplication, especially hooks and small UI. Promote only when two or more features independently implement the same hook or component, repeated edits cause friction, and the abstraction is obvious rather than speculative.

Global code must have no feature semantics, be stable and reusable without leaking assumptions, and prevent duplication that harms correctness or consistency or causes constant rework.

- `components/` holds shared UI primitives and layout. These may own local interaction state, such as input or animation state, but should not carry feature workflow rules. Use one export per file or a well-scoped component module.
- `hooks/` holds genuinely cross-feature hooks; default placement remains feature-local.
- Optional global `services/` holds cross-cutting clients and wrappers, without feature semantics.

## Keep dependencies and state explicit

Scenes may depend on feature public surfaces; features may depend on global components, hooks and services. A narrow, natural dependency on another feature's public surface is allowed when clearer than scene orchestration. It must not sequence or coordinate a workflow. Investigate a growing sibling-dependency graph rather than treating it as an automatic violation. Avoid scene-level reuse; promote reusable behaviour into features or components.

Feature state belongs inside the feature. Global state is earned: it must truly span features and remain stable. Prefer passing data and events through scene composition; use a shared cross-feature store only when necessary and intentional.

## Load the relevant rules before deciding

Read the indicated reference **before deciding or changing that concern**. A full architecture review requires all three; a narrow request requires this core and the relevant reference.

| Concern | Required reference |
| --- | --- |
| File placement and naming, imports, promotion, state, platforms, locale, configuration or public interfaces | [Placement and contracts](references/placement-and-contracts.md) |
| Monorepo roles, migration, boundary enforcement or folder examples | [Workspace and migration](references/workspace-and-migration.md) |
| Review signals, dependency concerns, size or refactor completion | [Review signals and checklist](references/review.md) |

The references retain the detailed rules and their exceptions. Folder examples illustrate options rather than mandate names. Read the relevant sections rather than unrelated platform examples.

## Explain the recommendation

Lead with the affected boundary, evidence and smallest useful change. Link to the code, decision and detailed rule. Explain consequences before optional mechanisms so engineering and business readers can follow the recommendation.

## Sources and inspiration

For the origin of these rules and the writing guidance applied to them, see [sources and local adaptation](references/placement-and-contracts.md#sources-and-local-adaptation). This source note supports attribution; it does not add another required research read.
