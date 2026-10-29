---
name: frontend-slice-architecture
description: Use when creating, refactoring, reviewing, or incrementally migrating frontend architecture towards a feature-first, package-shaped model with explicit public APIs, thin scene-level composition, and earned shared UI and hooks.
license: MIT
metadata:
  author: Geekist
  homepage: https://geekist.co
---

# Frontend Slice Architecture Playbook

Apply this architecture when the user chooses this model or asks for a review against it.

## Preserve the architecture rules

The architecture rules below and in the required references retain the original wording. Organisation and explanatory wording may change only while preserving every rule, exception and intended meaning. Any architectural rule change requires the user's explicit approval. The language baseline governs communication; it does not override or weaken architecture rules.

<!-- shared-baseline:start -->
Use current project terms and decisions. Explain an unfamiliar term near its first consequential use; distinguish a proposed meaning from an accepted one. Preserve exact identifiers and technical constraints.

Lead with the reader's purpose and main point, then explain the consequences and supporting detail. Make substantial technical material navigable by a reader outside engineering, with descriptive headings and meaningful source links. Match depth to the request; use British English in authored prose.

Keep implementation progress separate from validation. Pair a material evidence gap with a bounded next action and completion evidence. Missing prior proof alone does not reject an option or halt authorised work. Name actual blockers precisely, continue independent authorised work, and preserve existing authorisation.

Check consistency, accessibility, readability and repeatability. Use sources for claims and real events for progress. Preserve uncertainty that affects a decision without inventing certainty or unnecessary approval gates.
<!-- shared-baseline:end -->

## Authority and adaptation

Inspect the repository's framework, platform conventions and existing boundaries before proposing placement or changes. Treat this playbook as a set of strong defaults and an architecture lens, not filesystem directives or permission to reorganise unrelated code. Preserve established naming where it expresses the same boundaries, and migrate existing systems through the work already in scope.

## What this architecture is

Use a feature-first, package-shaped frontend where work starts local inside a feature and is promoted outward only when it becomes genuinely agnostic.

Do not treat this as a strict React doctrine. Treat it as operating rules that optimize legibility, autonomy, predictable change, and packaging readiness.

## Core mental model

Two homes, one direction of travel:

1. `features/<feature>` (default)

* Place feature-specific UI, state, hooks, and local components here.
* Let the feature own its internals.

2. Global agnostic layer (earned)

* Keep reusable UI and hooks in `components/` and `hooks/` only when truly feature-agnostic.

Direction of travel: feature -> global via promotion. Avoid reverse movement.

Orchestration is thin and explicit:

* Place route-level composition in `scenes/<platform>/`.
* Do not allow features to orchestrate other features directly.

## Strong defaults

Depart from these defaults when the local context provides a concrete reason, and preserve consistency within the affected boundary.

1. Start in a feature

* Implement new UI behaviour inside a feature unless it is explicitly agnostic from day one.

2. Isolate feature internals

* Avoid deep-importing another feature’s internals.
* Depend only on another feature’s public surface (`features/<feature>/index.*`).

3. Scenes own composition

* Scenes compose pages/routes, layout, and feature modules.
* Features do not coordinate other features; they expose capability.

4. Do not hide feature boundaries

* Avoid making an independently owned feature an internal implementation detail of another feature.
* Organisational grouping directories are acceptable when they do not create ownership or import boundaries.
* Prefer sibling features and explicit scene composition for independently owned behaviour.

5. Earn promotion through repetition

* Allow early duplication (especially hooks and small UI).
* Promote only when repetition is visible and painful.

6. Make public surfaces explicit

* Prefer a clear feature front door (`index.ts`, `index.js`, package exports, or the local equivalent).
* Block deep imports.

7. Keep components honest

* Shared `components/*` should remain UI primitives/layout rather than carrying feature workflow state.
* Shared `hooks/*` are cross-feature hooks only.

8. Package-ready by default

* Assume any feature subtree can receive a `package.json` later.
* Keep boundaries and imports package-safe.

## Load only the relevant detail

Read the indicated reference **before deciding or changing that concern**. A full architecture review needs all three; a narrow request needs only the relevant reference and this core.

| Concern | Required reference |
| --- | --- |
| Placement/naming, imports, promotion, state, platforms, locale, configuration or public interfaces | [Placement and contracts](references/placement-and-contracts.md) |
| Monorepo roles, migration, boundary enforcement or folder examples | [Workspace and migration](references/workspace-and-migration.md) |
| Architecture review, dependency smells, size or refactor completion | [Review signals and checklist](references/review.md) |

Each reference preserves the original detailed rules verbatim; folder examples are options rather than mandatory names. Read only the relevant sections, not unrelated platform examples.

## Explain the recommendation

Give the affected boundary, evidence and smallest useful change before optional mechanisms. Link to current code, decisions and the relevant detailed rule. Preserve the shared baseline above when explaining proposals, evidence gaps and practical consequences to technical and business readers.
