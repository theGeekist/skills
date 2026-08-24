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

## File naming and nesting

Prefer shallow feature internals. Add meaning to filenames before adding directories.

* Name a file for its primary component, hook, operation, subject, boundary, or responsibility.
* Do not repeat the enclosing feature name merely to make a filename globally unique.
* Choose the repository's established ordering for compound names, whether modifier-subject (`<modifier>-<subject>`) or subject-modifier (`<subject>-<modifier>`), and use it consistently when combining comparable name parts.
* Do not force unlike names into artificial grammar: components, hooks, operations, roles, platform variants, and framework suffixes may have different established forms.
* Preserve framework-required and tool-recognised forms such as component casing, `use*` hooks, `.test`, `.spec`, `.stories`, `.web`, `.native`, `.ios`, `.android`, and generated filenames.
* Prefer additional descriptive files over `components/`, `hooks/`, `state/`, `services/`, or `utils/` subdirectories while the feature remains easy to scan.
* Strongly discourage nesting introduced only for taxonomy, anticipated growth, or file count aesthetics.
* Add a directory only when substantial growth, a genuine internal boundary, generated-code isolation, framework requirements, or materially improved navigation justifies it.

For example, a small feature can remain shallow:

```text
features/editor/
  EditorCanvas.tsx
  useEditorState.ts
  save-document.ts
  editor-api.ts
  index.ts
```

The feature name need not prefix every file. When the directory grows considerably, introduce the smallest meaningful grouping supported by the files that actually exist.

## Folder guidance

### `features/<feature>/` (default home)

A feature is a cohesive unit with:

* UI + feature state,
* local hooks,
* local components,
* optional local routing within the feature (but scenes own top-level routing),
* a public API (`index.*`).

For a feature large enough to justify internal grouping, one possible shape is:

```text
features/
  <feature>/
    components/
    hooks/
    state/            (store, machines, reducers, query keys)
    services/         (feature-local API client wrappers, mappers)
    routes/           (optional: feature-local route parts)
    index.ts
```

### `scenes/<platform>/` (orchestration surface)

Scenes are the page/screen shells and route composition:

* wiring multiple features together,
* page layout and navigation,
* top-level route params and loaders,
* composition-time policies (guards, redirects, tracking).

Recommended scene shape:

```text
scenes/
  web/
    routes/
      <RouteName>Scene.tsx
    layout/
    router.ts
  native/
    screens/
      <ScreenName>Screen.tsx
    nav/
```

### `components/*` (global agnostic UI)

Shared components are UI primitives/layout only:

* may hold local UI state (toggling, animation, input state),
* should not encode feature workflow rules,
* one export per file (or a well-scoped component module).

### `hooks/*` (global agnostic hooks)

Only genuinely cross-feature hooks:

* auth/session, platform lifecycle, media queries, analytics wrappers.
* Default placement is feature-local; global is earned.

### `services/*` (optional global)

Use only for cross-cutting front-end services:

* analytics client wrapper
* feature flag client wrapper
* error reporting wrapper
* i18n wrapper

Do not put feature semantics here.

## Public import guidance

Import features from the feature root only.

Prefer:

* `import { Editor } from '@/features/editor'`
* `import { useAuth } from '@/hooks/useAuth'`
* `import { Button } from '@/components/Button'`

Avoid:

* `import useEditorState from '@/features/editor/hooks/useEditorState'`
* `import Canvas from '@/features/editor/components/Canvas'`

Treat feature internals as private implementation details.

## Rules for decisions

### Placement rules

Default placement: feature.

Place in global only if all are true:

* no feature semantics,
* reusable across features without leaking assumptions,
* behaviour is stable,
* duplication would harm correctness/consistency (or create constant rework).

### Promotion rules

Promote when:

* 2+ features independently implement the same hook/component,
* repeated edits create friction,
* the abstraction is obvious (not speculative).

Promotion targets:

* `components/` for UI primitives/layout,
* `hooks/` for cross-feature hooks,
* `services/` for cross-cutting clients/wrappers.

### Dependency rules

* Scenes may depend on feature public surfaces.
* Features may depend on global components/hooks/services.
* Features should not depend on other features’ internals.
* A feature may take a narrow, natural dependency on another feature’s public surface when that is clearer than scene orchestration.
* Do not use sibling dependencies for workflow sequencing or coordination; keep those in scenes.
* Treat a growing sibling-dependency graph as a boundary signal to investigate, not as an automatic violation.
* Avoid scene-level reuse; prefer promoting into features/components instead.

### No nesting rule

If Feature A appears to contain a sub-feature:

* split into Feature A + Feature B as siblings,
* coordinate in scenes (or a thin shared composition helper if truly cross-platform).

## State guidance

1. Feature state lives with the feature

* reducers, stores, query keys, state machines belong inside the feature.

2. Global state is earned

* global state exists only when it truly spans multiple features and is stable (e.g., auth/session).

3. Prefer explicit composition over hidden coupling

* pass data/events via props from scenes when composing features,
* or use a shared cross-feature store only when necessary and intentional.

## Multi-platform rule (web/native)

* Prefer **feature reuse** across platforms where behaviour is the same.
* Accept **scene duplication** across platforms when presentation differs.
* Allow feature internals to have platform variants when needed (`.web`, `.native`, `.ios`, `.android`) but keep the public API stable.

## Internationalisation and configuration

Treat internationalisation and configuration as normal architecture concerns from the start, even when the application initially has one language and one runtime configuration.

* Keep user-facing strings identifiable and owned by the feature that introduces them.
* This establishes where strings are managed before translation becomes necessary.
* Let the application or runtime shell compose locale behaviour and configuration sources.
* Add configuration requirements as features are introduced or touched.
* Prefer cross-runtime primitives where practical. UnJS packages can be useful options without becoming required choices.
* Use locale-aware formatting for dates, numbers, currencies, lists and similar values, even when English is the only current locale.
* Keep feature copy with the feature and genuinely agnostic component copy with the component.

## Amber / red flags

Amber (watch):

* a simple UI change touches multiple features,
* scenes start accumulating business rules,
* duplicate hooks appearing across features,
* imports begin reaching into feature internals,
* onboarding feedback says “hard to find where behaviour lives”.

Red (act now):

* deep imports across features become normal,
* a scene becomes a “god file” (route + rules + state + UI),
* shared components start carrying feature workflow logic,
* global hooks become a dumping ground,
* features exceed size thresholds and become mini-monoliths.

Standard responses:

* duplication -> promote once abstraction is obvious,
* oversized feature -> split into sibling features,
* oversized scene -> push rules/state back into features; keep scene thin,
* deep imports -> enforce public surfaces and refactor immediately.

## Existing monorepo adaptation

Use this when the repo already has `apps/*` + `packages/*` and cannot be reorganized in one move.

### Monorepo mapping (naming-agnostic)

- Treat `apps/*` as runtime shells:
  - routing/navigation, providers, platform bootstrap,
  - scene composition (page/screen orchestration),
  - environment wiring.

- Treat `packages/*` as extractable slices:
  - feature slices (whatever naming you already use),
  - shared UI primitives/components (only when earned),
  - shared cross-cutting wrappers/services (only when earned).

Prefer adding a new slice under existing conventions and enforcing boundaries via public APIs + import rules.

### Path-of-correctness migration

* Do not move old code first.
* Add a new lane for all new behaviour:

  * new features under `features/*` (or `packages/feat-*`),
  * enforce public APIs and import rules,
  * migrate old areas only when touched.

### Boundary enforcement

Enforce mechanically (lint/build), not by convention alone:

* Disallow deep imports into `features/<x>/**` except `features/<x>/index.*`
* Disallow feature-to-feature internal imports
* Allow scenes to compose features only via public surfaces

## Illustrative folder shape for a larger feature

```text
components/
hooks/
services/          (optional)
features/
  <feature>/
    components/
    hooks/
    state/
    services/
    index.ts
scenes/
  web/
    routes/
    layout/
  native/
    screens/
    nav/
app/               (bootstrap/providers)
```

## Feature public surface contract

Expose:

* one or more top-level components (feature entrypoints),
* feature hooks intended for consumption,
* feature types,
* optionally route fragments for scenes to compose.

Do not expose:

* internal components,
* internal state wiring,
* internal API mappers,
* volatile feature implementation types.

## Review/refactor checklist

1. Start every new behaviour in a feature.
2. Verify each feature exports a clear `index.*` public API.
3. Remove deep imports and replace with public-surface imports.
4. Keep route/page composition in scenes only; keep scenes thin.
5. Promote shared hooks/components only when repetition is painful.
6. Split oversized features/scenes before they become team bottlenecks.
7. Keep shared components free of feature workflow rules.
8. Preserve package-readiness: stable imports, clean boundaries.
