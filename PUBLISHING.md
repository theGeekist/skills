# Release and distribution

GitHub is the canonical source for the collection. A versioned release binds the plugin metadata, portable skills, references and notices to one commit.

## Release v1.9.3

The v1.9.3 release excludes non-production evaluation records from its downloadable source archives. The repository retains them for contributor and reviewer reference. The tag and archives become available after the release workflow publishes them.

- Repository: <https://github.com/theGeekist/skills>
- Release: <https://github.com/theGeekist/skills/releases/tag/v1.9.3>
- Both plugin manifests use version `1.9.3`.
- Release notes: [v1.9.3](release-notes/v1.9.3.md).
- The distribution retains the existing `geekist-architecture-skills` plugin identifier for compatibility; its displayed name is Geekist Skills.

Install the pinned collection:

```sh
npx skills add https://github.com/theGeekist/skills/tree/v1.9.3
```

The skills CLI prompts for skills and target agents. Its default scope is the current project; add `-g` for a user-wide installation. Review the selected destinations rather than assuming every installed client has the same discovery path. ChatGPT personal-skill installation uses its own supported installation mechanism, separately from this CLI.

For a canonical checkout shared by local clients:

```sh
git clone --branch v1.9.3 https://github.com/theGeekist/skills.git
cd skills
./scripts/link-local.sh --client all --dry-run
./scripts/link-local.sh --client all
```

Existing conflicts are preserved. Review a conflict before using `--adopt`, which moves it to a timestamped backup. Skill installation does not enable hooks or change global conversational instructions.

## Release workflow

`.github/workflows/release.yml` supports manual dispatch with a stable version tag. It also runs when the plugin manifests or release workflow change on `main`, using the version declared in both manifests. A release version is deliberately changed only when preparing a release.

The workflow:

1. Checks that both plugin versions and the versioned notes agree.
2. Preserves an existing release and tag without changing their assets.
3. Runs shared-source, terminology, deterministic and pinned portable-format checks.
4. Builds deterministic source archives without the non-production `evaluations/` directory, plus a dedicated ChatGPT plugin ZIP, checksums and a release manifest.
5. Verifies the evaluation directory is absent from both source archives.
6. Creates the tag at the checked commit if absent and publishes the GitHub release using the repository's normal Actions token.

An existing tag is never moved. If a tag exists but its release is missing, a run on a different commit stops with a recovery instruction. Run the workflow on the existing tag to finish publication for that commit. A same-version metadata update after publication is a no-op; a new release requires a new version and notes.

## Prepare the next release

Update `.codex-plugin/plugin.json` and `.claude-plugin/plugin.json` to the same next version. Set the same tag in `standards/skill-catalogue.json` and regenerate with `python3 scripts/sync-skill-catalogue.py`. Write `release-notes/vX.Y.Z.md`, update the install reference in this file and README, and run the checks documented in CONTRIBUTING. Review brand/source notices with the release contents. Merge the prepared change or manually run the workflow on its intended commit, then verify the published tag, manifest and checksums.

Published tags and release assets are immutable. Use a new version when released contents change.

## ChatGPT plugin upload

Download the dedicated `geekist-skills-chatgpt-v1.9.3.zip` release asset, **not** the source archive `geekist-skills-v1.9.3.zip`. The ChatGPT archive includes `.codex-plugin/plugin.json`, the MIT `LICENSE`, and the complete `skills/` tree. It omits repository-level marketplace definitions, evaluations, tests, scripts and documentation that make a source ZIP unsuitable for direct plugin upload. The source ZIP and tarball also omit `evaluations/`, including evaluation hash manifests and recorded outputs; contributors can still inspect that evidence in the repository.

The build is reproducible:

```sh
python3 scripts/package-chatgpt-plugin.py --output dist/geekist-skills-chatgpt-v1.9.3.zip
unzip -l dist/geekist-skills-chatgpt-v1.9.3.zip
```

In ChatGPT web, open Plugins → Personal → Add plugin and select that ZIP. The upload is an account-level installation, separate from local Fedora skills and from the GitHub release itself.

## Other distribution channels

The public release makes the collection available to compatible Agent Skills clients. Discovery on skills.sh is separate from successful installation; registry indexing can follow its own schedule.

The repository also carries Geekist-owned Codex and Claude marketplace metadata. Test the actual selected client and version before publishing command-level installation claims for that surface. The portable format does not establish native activation across CLI, desktop and cloud automatically.

Directory mirrors should identify the canonical repository and source revision. A directory listing, a local installation and a ChatGPT plugin installation are separate distribution states. Verify the selected client's documented installation route before publishing client-specific instructions.
