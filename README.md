# Geekist Architecture Skills

Portable agent skills for reviewing, creating and incrementally migrating backend and frontend codebases towards feature-first, package-shaped architecture.

Published by [Geekist](https://geekist.co).

## Skills

- `backend-slice-architecture`: feature-owned backend behaviour, explicit public surfaces, thin application orchestration and earned shared infrastructure.
- `frontend-slice-architecture`: feature-owned UI and state, thin scene composition, explicit public surfaces and earned shared components and hooks.

The playbooks are intentionally framework-neutral. They describe ownership and dependency boundaries without imposing a particular framework, package manager or repository taxonomy.

## Install

These folders follow the Agent Skills `SKILL.md` convention and can be copied or linked into a compatible agent's skill directory.

### Codex

```sh
git clone https://github.com/theGeekist/skills.git
mkdir -p ~/.agents/skills
ln -s "$PWD/skills/plugins/geekist-architecture-skills/skills/backend-slice-architecture" ~/.agents/skills/backend-slice-architecture
ln -s "$PWD/skills/plugins/geekist-architecture-skills/skills/frontend-slice-architecture" ~/.agents/skills/frontend-slice-architecture
```

If Codex is configured to discover `~/.codex/skills` instead, link the same folders there. Keep one canonical copy rather than maintaining divergent client-specific variants.

### Other compatible agents

Copy either folder under `plugins/geekist-architecture-skills/skills/` into the skill directory supported by the client. Product-specific metadata lives under `agents/` and does not change the portable `SKILL.md` instructions.

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
