# Publishing

The canonical source should be a public Geekist-owned GitHub repository. Registry records should reference an immutable release rather than carrying independently edited copies.

## Current release

- Repository: <https://github.com/theGeekist/skills>
- Release: `v1.3.0`
- Agent Skills validation: passed with `gh skill publish --dry-run`
- Direct install: `gh skill install theGeekist/skills`

## Release checklist

1. Confirm that Geekist is the copyright holder and MIT is the intended licence.
2. Replace the placeholder private-reporting wording in `SECURITY.md` with a real security email or disclosure URL.
3. Test installation in clean Codex and Claude Code environments.
4. Add tag protection for release immutability.
5. Enable any GitHub security features available to the organisation.

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

SkillsMD supports instruction-only skills and reviews each skill separately. Submit each top-level path from `skills/` and respond to review. Treat successful registry discovery as separate evidence from repository validation.

### 5. ToolHive Catalog and Dockyard

Open a short preflight issue with ToolHive maintainers first. The skills conform to the Agent Skills shape but intentionally declare no MCP dependencies, while ToolHive frames skills around MCP-assisted workflows.

If accepted, prepare one catalogue entry per skill under `registries/toolhive/skills/<slug>/`, including `skill.json`, `icon.svg` and `skill/SKILL.md`. Current criteria require permissive licensing, versioning, Agent Skills compliance and OCI as canonical distribution. Validate using the catalogue tasks and `thv skills validate`, then submit a pull request to `stacklok/toolhive-catalog`.

Do not invent `allowedTools`. Declare none unless a real ToolHive-hosted MCP dependency is introduced.

### 6. Secondary directories

After the canonical release is stable, consider explicit submissions to SkillsMD.dev or askill.sh and relevant maintained awesome lists. These improve discovery but should never become the source of truth.

ClawHub is technically compatible but publication applies MIT-0. Do not submit unless Geekist explicitly accepts that separate licensing consequence.

LF agentregistry and AWS Agent Registry are useful for self-hosted or organisation-scoped enterprise catalogues, not broad public discovery.

## Manual actions

The GitHub repository and `v1.0.0` release are already public. Remaining external publication requires a human with Geekist authority to:

- confirm the copyright holder and MIT licence;
- authenticate the Geekist GitHub, SkillMD and any optional registry accounts;
- submit and respond to ToolHive or directory reviews;
- provide a public security contact;
- configure a GitHub tag-protection ruleset;
- decide whether ClawHub's MIT-0 terms are acceptable.
