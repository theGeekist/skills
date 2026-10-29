# Geekist Skills

[![Licence: MIT](https://img.shields.io/badge/Licence-MIT-blue.svg)](LICENSE)

Portable agent skills for architecture and shared project language. Review and evolve feature-first systems, establish domain meanings, and write material that technical and business readers can navigate.

The playbooks help coding agents make architecture decisions about ownership, public APIs, orchestration, dependencies and shared infrastructure. They are framework-neutral and adapt to the repository in front of them rather than imposing a fixed folder taxonomy.

Published by [Geekist](https://geekist.co).

## Install

Install the collection from the public repository:

```sh
npx skills add theGeekist/skills
```

The skills use portable Markdown with YAML frontmatter and optional client metadata. They require no MCP server or runtime dependency. Optional repository checks and a Codex hook example are separate from skill installation.

The language-system changes on this branch are unreleased. See the [architecture and reader route](docs/language-system/architecture.md), [evaluation results](docs/language-system/validation-results.md) and [integration guide](docs/language-system/integration.md).

## Included language skills

### Establish project language

`establish-project-language` discovers concepts from current code, schemas, tests and decisions. It records context, accepted meanings, proposals and source evidence, so different agents and artefacts can share the same definitions.

### Write project content

`write-project-content` applies that meaning to tasks, decisions, documentation and product content. It makes purpose, decisions and consequences easy to find, with a direct route to technical detail. The acceptance outcomes are consistency, accessibility, readability and repeatability.

### Advance with uncertainty

`advance-with-uncertainty` turns evidence gaps into bounded next actions in tasks, ADRs and worker handoffs. It keeps implementation progress separate from validation, preserves real blockers and prevents missing prior proof from becoming an unsupported rejection or blanket stop.

## Included architecture skills

### Backend slice architecture

`backend-slice-architecture` applies a capability-first backend architecture. Behaviour starts inside an owned capability, cross-capability workflows remain explicit, and shared infrastructure is introduced only when reuse has been earned.

Use it to:

- review service and package boundaries;
- design explicit public APIs and prevent deep imports;
- separate capability rules from application orchestration;
- adapt capability ownership to `apps/`, `packages/`, `libs/`, modules or equivalent project roots;
- plan incremental migration through code already being changed.

### Frontend slice architecture

`frontend-slice-architecture` applies a feature-first frontend architecture. UI, state and hooks begin inside an owned feature, scenes stay thin, and shared components or hooks emerge only after genuine reuse.

Use it to:

- review feature ownership and scene composition;
- keep feature internals private behind explicit public surfaces;
- separate route-level orchestration from feature behaviour;
- support web, native and multi-platform frontends without prescribing a framework;
- migrate existing applications by touch instead of reorganising them wholesale.

## Architecture model

Both skills share the same operating model:

| Concern | Default home | Promoted home | Composition surface |
| --- | --- | --- | --- |
| Backend behaviour | Owned capability | Agnostic infrastructure or shared service | Application workflow or use case |
| Frontend behaviour | Owned feature | Agnostic component, hook or service | Scene, page or route |

The default direction of travel is local to shared. Early duplication is acceptable. Promotion happens when repetition is visible, the abstraction is stable and sharing improves correctness or reduces meaningful friction.

`Package-shaped` means independently testable, with an explicit public surface and enforceable dependency boundaries. It does not require a `package.json`, a publishable package or a particular top-level directory.

## Use with an agent

Invoke a skill explicitly in clients that support named skills:

```text
Use $backend-slice-architecture to review this service boundary and propose the smallest migration-by-touch.
```

```text
Use $frontend-slice-architecture to review this feature and scene composition without changing the framework.
```

Clients that support automatic skill selection can also select either playbook from its description.

## Install from a canonical local checkout

For active development, keep one Git checkout as the local source of truth and link its skill directories into compatible clients. This avoids copied, client-specific variants.

```sh
git clone https://github.com/theGeekist/skills.git
cd skills
./scripts/link-local.sh --client all --dry-run
./scripts/link-local.sh --client all
```

The linker uses:

- `~/.agents/skills` for Codex, Gemini CLI and desktop Antigravity;
- `~/.claude/skills` for Claude Code;
- `~/.gemini/antigravity-cli/skills` when Antigravity CLI is installed.

Correct links are left untouched. Existing destinations cause the command to fail safely. Use `--adopt` only after reviewing a conflict; it moves the existing entry to a timestamped backup before creating the link.

### Update the local checkout

```sh
./scripts/update-local.sh --dry-run
./scripts/update-local.sh
```

The updater refuses dirty or detached checkouts, pulls with `--ff-only`, runs the official GitHub Agent Skills validator when available, and verifies the client links.

## Repository structure

```text
.codex-plugin/
  plugin.json
.claude-plugin/
  marketplace.json
  plugin.json
skills/
  backend-slice-architecture/
    SKILL.md
    agents/openai.yaml
  frontend-slice-architecture/
    SKILL.md
    agents/openai.yaml
  establish-project-language/
    SKILL.md
    references/
    assets/
  write-project-content/
    SKILL.md
    references/
    assets/
  advance-with-uncertainty/
    SKILL.md
    references/
    assets/
standards/
adapters/
evaluations/
scripts/
  link-local.sh
  update-local.sh
```

The repository root is the plugin and `skills/` is the canonical collection exposed to clients and registries. Each skill keeps its instructions and required references within its own directory. `standards/` holds canonical writing references; a sync check keeps their bundled copies consistent. `adapters/` holds optional agent integration examples, and `evaluations/` holds public test cases. Repository-wide automation stays under `scripts/`.

## Compatibility

The skills follow the portable Agent Skills shape and include optional Codex-facing display metadata under `agents/openai.yaml`. They can be used by compatible agent clients without changing the core instructions.

## Publishing

This repository is the canonical public source. Registry records should point back to an immutable release rather than carry edited copies. See [PUBLISHING.md](PUBLISHING.md) for the release checklist and account-specific steps.

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md) to propose changes and [SECURITY.md](SECURITY.md) to report vulnerabilities privately.

## Licence

MIT. See [LICENSE](LICENSE).
