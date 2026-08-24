# Geekist Architecture Skills

Portable agent skills for reviewing, creating and incrementally migrating backend and frontend codebases towards feature-first, package-shaped architecture.

Published by [Geekist](https://geekist.co).

## Skills

- `backend-slice-architecture`: feature-owned backend behaviour, explicit public surfaces, thin application orchestration and earned shared infrastructure.
- `frontend-slice-architecture`: feature-owned UI and state, thin scene composition, explicit public surfaces and earned shared components and hooks.

The playbooks are intentionally framework-neutral. They describe ownership and dependency boundaries without imposing a particular framework, package manager or repository taxonomy.

## Install locally from the canonical checkout

Keep one Git checkout as the local source of truth and link its skill directories into each compatible client. Do not maintain copied client-specific variants.

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

It leaves correct links untouched and fails if a destination already exists. Use `--adopt` only after reviewing the conflict; adoption moves the existing entry to a timestamped backup before creating the link.

### Update

```sh
./scripts/update-local.sh --dry-run
./scripts/update-local.sh
```

The updater refuses dirty or detached checkouts, pulls with `--ff-only`, runs the official GitHub Agent Skills validator when available, and verifies the client links.

### Consumer installation

External users who do not need a source checkout can install the published release:

```sh
gh skill install theGeekist/skills
```

Product-specific metadata lives under `agents/` and does not change the portable `SKILL.md` instructions.

## Repository structure

```text
plugins/
  geekist-architecture-skills/
    .codex-plugin/
      plugin.json
    skills/
      backend-slice-architecture/
        SKILL.md
        agents/openai.yaml
      frontend-slice-architecture/
        SKILL.md
        agents/openai.yaml
scripts/
  link-local.sh
  update-local.sh
```

The plugin and skill nesting is intentional distribution structure, not domain taxonomy. Each skill keeps its instructions at the root and uses only the client metadata directory defined by the Agent Skills conventions. Repository automation is isolated under `scripts/` because it operates across skills and does not belong to either skill package.

## Use

Invoke either skill explicitly when supported:

```text
Use $backend-slice-architecture to review this service boundary and propose the smallest migration-by-touch.
```

```text
Use $frontend-slice-architecture to review this feature and scene composition without changing the framework.
```

Both skills can also be selected automatically from their descriptions by clients that support implicit skill invocation.

## Compatibility

The core content is plain Markdown with YAML frontmatter. The optional `agents/openai.yaml` files provide Codex-facing display metadata. No MCP server, executable, network access or external dependency is required.

## Publishing

This repository is the canonical public source. Registry-specific records should point back here rather than carrying edited copies. See [PUBLISHING.md](PUBLISHING.md) for the release checklist and manual account steps.

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md) for proposed changes and [SECURITY.md](SECURITY.md) for private vulnerability reports.

## Licence

MIT. See [LICENSE](LICENSE).
