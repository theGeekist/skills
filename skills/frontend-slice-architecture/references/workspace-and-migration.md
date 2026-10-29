# Workspace roles and incremental migration

Apply these detailed rules when the core skill routes you to this concern. Preserve equivalent repository conventions; examples are illustrative.

## Existing monorepo adaptation

Use this when the repo already has `apps/*` + `packages/*` and cannot be reorganised in one move.

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

### Incremental migration

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
