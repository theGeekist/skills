# Geekist Skills

[![Licence: MIT](https://img.shields.io/badge/Licence-MIT-blue.svg)](LICENSE)

Portable agent skills for architecture and shared project language. Review and evolve feature-first systems, establish domain meanings, and write material that technical and business readers can navigate.

The playbooks help coding agents make architecture decisions about ownership, public APIs, orchestration, dependencies and shared infrastructure. They are framework-neutral and adapt to the repository in front of them rather than imposing a fixed folder taxonomy.

Published by [Geekist](https://geekist.co).

## Install

Install the versioned collection from the public repository:

```sh
npx skills add https://github.com/theGeekist/skills/tree/v1.5.0
```

The skills use portable Markdown with YAML frontmatter and optional client metadata. They require no MCP server or runtime dependency. Optional repository checks and a Codex hook example are separate from skill installation.

Version **v1.5.0** introduces the shared language system and focused writing workflows. See the [architecture and reader route](docs/language-system/architecture.md), [evaluation results](docs/language-system/validation-results.md) and [integration guide](docs/language-system/integration.md).

## Choose a language skill

Every skill carries the same short writing baseline. Choose by the requested work; a marketing author can use the marketing skill directly without loading architecture guidance.

| Requested work | Skill |
| --- | --- |
| Discover and reconcile project meanings | `establish-project-language` |
| Engineering tickets, acceptance criteria and worker handoffs | `write-implementation-tasks` |
| Architecture decision records (ADRs) | `record-architecture-decisions` |
| Tutorials, how-to guides, technical references and explanations | `write-technical-documentation` |
| Marketing copy, announcements and positioning | `write-marketing-content` |
| Interface labels, dashboard states, progress and errors | `write-interface-content` |
| Review terminology, reader navigation and consistent meaning | `review-project-language` |
| Turn evidence gaps into useful next actions | `advance-with-uncertainty` |

`write-project-content` remains a compatibility entry point for explicit callers who want help choosing a writing workflow. It is no longer the broad default authoring skill. Codex metadata disables its implicit invocation; other clients must apply their own selection rules.

The acceptance outcomes are consistency, accessibility, readability and repeatability. Full reference material is bundled for independent installation, while each skill explains which detail to load for the task.

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

- `skills/`: independently installable skills with their own required references and optional client metadata.
- `standards/baseline.md`: the short authored baseline embedded in every skill.
- `standards/skill-profiles.json`: which canonical references each skill bundles.
- `standards/`: task-specific writing references and terminology.
- `scripts/`: baseline/reference generation and checks.
- `adapters/`: opt-in persistent instruction and runtime examples.
- `evaluations/`: public prompts, source snapshots, observed results and scope limitations.

Run `python3 scripts/sync-language-references.py` after changing the baseline or canonical references, and `python3 scripts/sync-language-references.py --check` before committing. Generated copies retain one source of truth while allowing each skill to be installed alone. Architecture-specific references are authored within their respective skill.

## Compatibility

The skills follow the portable Agent Skills shape and include optional Codex-facing display metadata under `agents/openai.yaml`. They can be used by compatible agent clients without changing the core instructions.

## Publishing

This repository is the canonical public source. Registry records should point back to an immutable release rather than carry edited copies. See [PUBLISHING.md](PUBLISHING.md) for the release checklist and account-specific steps.

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md) to propose changes and [SECURITY.md](SECURITY.md) to report vulnerabilities privately.

## Licence

MIT. See [LICENSE](LICENSE).
