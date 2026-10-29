# Workspace and migration

Read the relevant sections before deciding or changing this concern. These rules preserve the original architecture; the wording and organisation support navigation.

## Find the relevant rule

- [Existing monorepo adaptation](#existing-monorepo-adaptation)
- [Illustrative folder shape for a larger feature](#illustrative-folder-shape-for-a-larger-feature)

## Existing monorepo adaptation

Use this when the repo already has `apps/*` + `packages/*` and cannot be reorganised in one move.

### Map runtime and feature responsibilities

- Treat `apps/*` as runtime shells (application startup and composition):
  - routing/navigation, providers, platform startup,
  - scene composition (page/screen orchestration),
  - environment wiring.

- Treat `packages/*` as extractable slices:
  - feature slices (whatever naming you already use),
  - shared UI primitives/components (only when earned),
  - shared cross-cutting wrappers/services (only when earned).

Prefer adding a new slice under existing conventions and enforcing boundaries through public APIs and import rules.

### Incremental migration

* Do not move old code first.
* Add a new lane for all new behaviour:

  * new features under `features/*` (or `packages/feat-*`),
  * enforce public APIs and import rules,
  * migrate old areas only when touched.

### Boundary enforcement

Enforce with lint or build checks, rather than relying on convention alone:

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
