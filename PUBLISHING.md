# Publishing

The canonical source should be a public Geekist-owned GitHub repository. Registry records should reference an immutable release rather than carrying independently edited copies.

## Release checklist

1. Confirm the public organisation and repository name. The prepared metadata assumes `theGeekist/skills`.
2. Confirm that Geekist is the copyright holder and MIT is the intended licence.
3. Replace the placeholder private-reporting wording in `SECURITY.md` with a real security email or disclosure URL.
4. Validate both skills and the Codex plugin.
5. Test installation in clean Codex and Claude Code environments.
6. Create a signed or annotated `v1.0.0` tag and GitHub release.
7. Enable the issue tracker and add the `agent-skills`, `codex`, `claude-code`, `architecture`, `backend` and `frontend` repository topics.

## Distribution order

### 1. GitHub and skills.sh

Publishing the public repository makes the skills installable with the skills CLI:

```sh
npx skills add theGeekist/skills
```

Discovery on skills.sh is install/crawler driven. Treat successful installation from GitHub as the acceptance test, not immediate appearance in search.

If available in the installed GitHub CLI, `gh skill publish` can validate the Agent Skills layout, apply the `agent-skills` topic and create a tagged GitHub release.

### 2. Geekist Codex marketplace

The repository includes a skill-only Codex plugin and a Geekist marketplace record. Test adding the published repository as a marketplace and installing `geekist-architecture-skills` before documenting the exact client command against the current Codex release.

OpenAI's curated plugin repository does not currently document open self-service submission. Geekist can self-publish immediately; curated inclusion would require a separate editorial or partner conversation.

### 3. Geekist Claude Code marketplace

The repository includes `.claude-plugin/marketplace.json`. After publication, test:

```text
/plugin marketplace add theGeekist/skills
/plugin install geekist-architecture-skills@geekist
```

This marketplace is Geekist-owned and does not require Anthropic review. Anthropic's official marketplace is separately curated and has no documented public submission route.

### 4. SkillMD

SkillMD supports instruction-only skills and reviewable multi-skill packs. A Geekist publisher must authenticate, run a dry run, publish and respond to review:

```sh
skillmd publish ./plugins/geekist-architecture-skills --dry-run --type pack
skillmd publish ./plugins/geekist-architecture-skills --type pack
```

Check the current CLI syntax before the live submission: <https://skillmd.com/docs/cli>.

### 5. ToolHive Catalog and Dockyard

Open a short preflight issue with ToolHive maintainers first. The skills conform to the Agent Skills shape but intentionally declare no MCP dependencies, while ToolHive frames skills around MCP-assisted workflows.

If accepted, prepare one catalogue entry per skill under `registries/toolhive/skills/<slug>/`, including `skill.json`, `icon.svg` and `skill/SKILL.md`. Current criteria require permissive licensing, versioning, Agent Skills compliance and OCI as canonical distribution. Validate using the catalogue tasks and `thv skills validate`, then submit a pull request to `stacklok/toolhive-catalog`.

Do not invent `allowedTools`. Declare none unless a real ToolHive-hosted MCP dependency is introduced.

### 6. Secondary directories

After the canonical release is stable, consider explicit submissions to SkillsMD.dev or askill.sh and relevant maintained awesome lists. These improve discovery but should never become the source of truth.

ClawHub is technically compatible but publication applies MIT-0. Do not submit unless Geekist explicitly accepts that separate licensing consequence.

LF agentregistry and AWS Agent Registry are useful for self-hosted or organisation-scoped enterprise catalogues, not broad public discovery.

## Manual actions

External publication requires a human with Geekist authority to:

- create or approve the public GitHub repository;
- confirm the repository name, copyright holder and MIT licence;
- authenticate the Geekist GitHub, SkillMD and any optional registry accounts;
- publish the initial tag/release;
- submit and respond to ToolHive or directory reviews;
- provide a public security contact;
- decide whether ClawHub's MIT-0 terms are acceptable.
