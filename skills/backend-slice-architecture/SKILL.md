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

## Preserve the architecture rules

The architecture rules below and in the required references retain the original wording. Organisation and explanatory wording may change only while preserving every rule, exception and intended meaning. Any architectural rule change requires the user's explicit approval. The language baseline governs communication; it does not override or weaken architecture rules.

<!-- shared-baseline:start -->
Use current project terms and decisions. Explain an unfamiliar term near its first consequential use; distinguish a proposed meaning from an accepted one. Preserve exact identifiers and technical constraints.

Lead with the reader's purpose and main point, then explain the consequences and supporting detail. Make substantial technical material navigable by a reader outside engineering, with descriptive headings and meaningful source links. Match depth to the request; use British English in authored prose.

Keep implementation progress separate from validation. Pair a material evidence gap with a bounded next action and completion evidence. Missing prior proof alone does not reject an option or halt authorised work. Name actual blockers precisely, continue independent authorised work, and preserve existing authorisation.

Check consistency, accessibility, readability and repeatability. Use sources for claims and real events for progress. Preserve uncertainty that affects a decision without inventing certainty or unnecessary approval gates.
<!-- shared-baseline:end -->

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

## Load only the relevant detail

Read the indicated reference **before deciding or changing that concern**. A full architecture review needs all three; a narrow request needs only the relevant reference and this core.

| Concern | Required reference |
| --- | --- |
| File placement/naming, shared-code promotion, interfaces, delivery, locale or configuration | [Placement and contracts](references/placement-and-contracts.md) |
| Workspace roles, multiple runtimes, migration, enforcement tools or folder examples | [Workspace and migration](references/workspace-and-migration.md) |
| Architecture review, sizing, dependency smells or refactor completion | [Review signals and checklist](references/review.md) |

Each reference preserves the original detailed rules verbatim; examples illustrate options rather than mandate a stack. Use the smallest relevant section, and avoid loading examples for unrelated ecosystems.

## Explain the recommendation

Give the affected boundary, evidence and smallest useful change before optional mechanisms. Link to current code, decisions and the relevant detailed rule. Preserve the shared baseline above when explaining proposals, evidence gaps and practical consequences to technical and business readers.
