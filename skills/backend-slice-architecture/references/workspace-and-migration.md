# Workspace roles and incremental migration

Use this reference to map the architecture onto existing project roots, share orchestration across runtimes and migrate through work already in scope. Preserve equivalent repository conventions; folder examples illustrate options.

## Find the relevant section

- [Workspace mapping](#workspace-mapping)
- [Illustrative folder shapes](#illustrative-folder-shapes)
- [Evolution model](#evolution-model)

## Workspace mapping

Follow the workspace's configured project roots. `apps/`, `packages/`, and `libs/` are equally sound project-root conventions when their actual roles and dependency boundaries are explicit. Folder names do not determine the architecture.

### Common roles

A runtime entrypoint starts a deployable application. Its composition root connects dependencies and configuration; its orchestration sequences capabilities.

- `apps/*` commonly contains deployable runtime entrypoints (delivery + composition):
  - inbound adapters (HTTP/GraphQL/gRPC, workers, cron, command-line interfaces)
  - orchestration/workflows/use-cases (thin sequencing)
  - composition root (dependency injection, configuration and startup wiring)

- `apps/*` may also contain capability or library projects when that is the repository's established convention.
- `packages/*` commonly contains workspace packages, including runtime applications, capability boundaries, and shared infrastructure. A package may be internal or publishable.
- `libs/*` serves the same architectural role in repositories and toolchains that use library-oriented vocabulary.
- Use project metadata, public surfaces, and runtime responsibility rather than the root folder name to determine a project's role.

Capability packages or libraries contain:
  - capability slices: the owned boundaries where behaviour starts
  - shared agnostic plumbing: reusable adapters, services and utilities earned through repetition

Rules:
- New behaviour starts in a capability project under the workspace's established `packages/*`, `libs/*`, or equivalent root.
- Coordination across capability slices lives in the app’s orchestration surface (or a shared orchestration package if multiple runtimes exist).
- Slices expose an ecosystem-appropriate public surface; deep imports into slice internals are disallowed.
- Promotion to shared packages happens only when repetition is visible and the abstraction is obvious.
- Do not introduce new naming taxonomies unless the repo already uses them.

### Multiple apps rule

- If only one backend runtime exists, orchestration can live in that app.
- If multiple runtimes exist (`api`, `worker`, `admin`), do not duplicate orchestration logic.
- Share orchestration in a package, or route both runtimes through common orchestration entrypoints.

### Incremental migration

- Do not move old code first.
- Add new behaviour to capability projects under the repository's established workspace roots.
- Keep runtime composition in the relevant application project, whether that lives under `apps/*`, `packages/*`, or another configured root.
- Migrate old areas only when touched by real work.

### Boundary enforcement

Enforce boundaries through lint rules, builds or architecture tests. Naming conventions alone are insufficient.

- Allow runtime applications to depend on capability public surfaces.
- Allow capability projects to depend on approved agnostic infrastructure projects.
- Disallow deep imports between capability internals.
- Require imports through the ecosystem's public-surface mechanism.

Typical tooling options:
- TypeScript: ESLint import rules and TypeScript path mapping.
- Nx/Turborepo: module boundary rules.
- Java: package visibility + ArchUnit.

## Illustrative folder shapes

These are mappings of the same ownership model, not competing architectures or required names.

### JavaScript/TypeScript workspace with `apps` and `packages`

```text
apps/
  api/
    src/
      composition/
      workflows/

packages/
  checkout/
    src/
    package.json
  inventory/
    src/
    package.json
  observability/
    src/
    package.json
```

### Workspace with `apps` and `libs`

```text
apps/
  api/

libs/
  commerce/
    checkout/
    inventory/
  shared/
    observability/
```

### Workspace using `packages` for every project

```text
packages/
  api/
    src/
      composition/
  checkout/
    src/
  inventory/
    src/
  observability/
    src/
```

### Single-package service

```text
src/
  modules/
    checkout/
    inventory/
  application/
    workflows/
  infrastructure/
  main.ts

```

## Evolution model

1. Start capability-local and ship.
2. Promote agnostic patterns once repetition is clear.
3. Split large capabilities into sibling capabilities.
4. Let orchestration grow as thin workflow maps, not rule dumps.
5. Let package/service extraction emerge naturally.
