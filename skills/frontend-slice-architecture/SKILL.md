---
name: frontend-slice-architecture
description: "Use when creating, refactoring, reviewing, or incrementally migrating frontend architecture towards a feature-first, package-shaped model with explicit public APIs, thin scene-level composition, and earned shared UI and hooks."
license: MIT
metadata:
  author: Geekist
  homepage: https://geekist.co
---

# Frontend architecture

Keep related interface behaviour together, protect feature interfaces and make page-level coordination explicit. Apply this model when the user chooses it or requests a review against it.

<!-- shared-baseline:start -->
Use current project terms and decisions. Explain an unfamiliar term near its first consequential use; distinguish a proposed meaning from an accepted one. Preserve exact identifiers and technical constraints.

Lead with the reader's purpose and main point, then explain the consequences and supporting detail. Make substantial technical material navigable by a reader outside engineering, with descriptive headings and meaningful source links. Match depth to the request; use British English in authored prose.

Keep implementation progress separate from validation. Pair a material evidence gap with a bounded next action and completion evidence. Missing prior proof alone does not reject an option or halt authorised work. Name actual blockers precisely, continue independent authorised work, and preserve existing authorisation.

Check consistency, accessibility, readability and repeatability. Use sources for claims and real events for progress. Preserve uncertainty that affects a decision without inventing certainty or unnecessary approval gates.
<!-- shared-baseline:end -->

## Start with the repository

Read existing instructions, decisions, framework/platform conventions and affected code before recommending placement. Preserve established names where they express equivalent boundaries. These are strong defaults, not permission to reorganise unrelated code. Depart for a concrete local reason and keep the affected boundary consistent. React is optional.

A **feature** owns a cohesive area's user interface, state and implementation. Its **public surface** is the components, functions and types others may use. A **deep import** bypasses it to reach internals. **Package-shaped** means independently testable with an explicit interface and enforceable dependencies; a feature need not already have a `package.json`.

A **scene** is a page or screen shell that brings features together. **Orchestration** coordinates their workflow. A frontend **hook** connects components to state or framework behaviour; it differs from an agent lifecycle hook.

## Keep the decision core

- Start UI behaviour in its owning feature unless independent of feature rules from day one. Keep local UI, state, hooks and components together, with an explicit public interface appropriate to the ecosystem.
- Keep independently owned features as peers; organisational grouping may remain where it creates no hidden ownership or import boundary. Split independent nested features into siblings and coordinate them through scenes or a genuinely cross-platform composition helper.
- Scenes own route/page composition, layout, top-level navigation/parameters/loaders and composition-time policies. Keep workflow sequencing there; keep feature rules and state in their feature.
- Scenes may depend on feature public surfaces; features may use approved global components, hooks and services. A narrow, natural public dependency on a sibling is allowed when clearer than scene orchestration, but must not coordinate a workflow. Investigate a growing dependency graph rather than automatically rejecting every sibling dependency. Avoid scene-level reuse; promote reusable behaviour into features or shared components.
- Treat internals as private and mechanically enforce imports through the feature root or equivalent public surface. Expose intended feature components, public hooks, types and optional route fragments. Keep internal components, state wiring, API mappers and volatile implementation types private. Preserve package-safe imports so extraction can happen later.
- Allow early duplication. **Promotion** moves repeated, stable behaviour from feature-local code into shared code. Require repetition in two or more features, painful repeated edits and an obvious abstraction. Shared code must carry no feature semantics, leak no feature assumptions, and prevent meaningful correctness/consistency harm or constant rework. Avoid reversing the local-to-shared direction.
- Shared UI stays primitive/layout-focused and may own local interaction state, but not feature workflow rules. Use one export per file or a well-scoped component module. Global hooks must serve genuine cross-feature behaviour; global services are cross-cutting wrappers, not homes for feature semantics.
- Keep feature state local. Global state must genuinely span features and be stable. Prefer explicit data/events composed by scenes; introduce a shared store only when necessary and intentional.
- Prefer shallow files with meaningful names. Preserve component casing, recognised hook/platform/framework suffixes and established compound-name conventions. Add internal grouping for real boundaries, generated code, framework needs, substantial growth or navigation; avoid speculative taxonomy and repeated feature prefixes.
- Reuse feature behaviour across platforms; scene duplication is acceptable when presentation differs. Platform variants may live inside a feature while its public interface stays stable.
- Design internationalisation and configuration from the start. Feature copy stays with the feature; genuinely shared copy stays with its component. The runtime shell composes locale/configuration. Format locale-sensitive values appropriately even for one English locale.
- Adapt the model to established workspace roots. Add new behaviour through existing conventions and migrate old areas only when touched. Enforce boundaries mechanically and respond to oversized features/scenes, deep imports and workflow-heavy shared code with targeted changes.

## Load only the relevant detail

Read the indicated reference **before deciding or changing that concern**. A full architecture review needs all three; a narrow request needs only the relevant reference and this core.

| Concern | Required reference |
| --- | --- |
| Placement/naming, imports, promotion, state, platforms, locale, configuration or public interfaces | [Placement and contracts](references/placement-and-contracts.md) |
| Monorepo roles, migration, boundary enforcement or folder examples | [Workspace and migration](references/workspace-and-migration.md) |
| Architecture review, dependency smells, size or refactor completion | [Review signals and checklist](references/review.md) |

Each reference preserves the detailed rules; folder examples are options rather than mandatory names. Read only the relevant sections, not unrelated platform examples.

## Explain the recommendation

Give the affected boundary, evidence and smallest useful change before optional mechanisms. Link to current code, decisions and the relevant detailed rule. Preserve the shared baseline above when explaining proposals, evidence gaps and practical consequences to technical and business readers.
