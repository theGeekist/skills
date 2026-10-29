# Placement and public contracts

Read the relevant sections before deciding or changing this concern. These rules preserve the original architecture; the wording and organisation support navigation.

## Find the relevant rule

- [File naming and nesting](#file-naming-and-nesting)
- [Folder guidance](#folder-guidance)
- [Public import guidance](#public-import-guidance)
- [Rules for decisions](#rules-for-decisions)
- [State guidance](#state-guidance)
- [Multi-platform rule (web/native)](#multi-platform-rule-webnative)
- [Internationalisation and configuration](#internationalisation-and-configuration)
- [Feature public surface contract](#feature-public-surface-contract)

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

* user interface (UI) and feature state,
* local hooks,
* local components,
* optional routing within the feature, while scenes own top-level routing,
* a public application programming interface (API), exposed through `index.*`.

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

### `components/*`: shared UI without feature rules

Shared components are UI primitives/layout only:

* may hold local UI state (toggling, animation, input state),
* should not encode feature workflow rules,
* one export per file (or a well-scoped component module).

### `hooks/*`: hooks shared across features

Only genuinely cross-feature hooks:

* auth/session, platform lifecycle, media queries, analytics wrappers.
* Default placement is feature-local; global is earned.

### `services/*`: optional shared clients and wrappers

Use only for cross-cutting front-end services, meaning services used across features:

* analytics client wrapper
* feature flag client wrapper
* error reporting wrapper
* internationalisation (i18n) wrapper

Keep feature-specific meaning and workflow rules out of this shared location.

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

* no feature-specific meaning or workflow rules,
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

* reducers (state update functions), stores, query keys (identifiers for cached requests) and state machines belong inside the feature.

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

## Sources and local adaptation

The architecture rules are Jason's original frontend rules, preserved from the [pre-language-system playbook](https://github.com/theGeekist/skills/blob/fcbd5a9/skills/frontend-slice-architecture/SKILL.md). External writing frameworks inform their explanation and navigation; they do not establish or override these architectural requirements.

[Microsoft's simple-word guidance](https://learn.microsoft.com/en-us/style-guide/word-choice/use-simple-words-concise-sentences) informs concise wording. [Google's jargon guidance](https://developers.google.com/style/jargon) informs explanations near first use. These principles are adapted to British English and the project's existing terms.
