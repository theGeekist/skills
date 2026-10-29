# Release and distribution

GitHub is the canonical source for the collection. A versioned release binds the plugin metadata, portable skills, references, branding and evaluation record to one commit.

## Release v1.5.0

- Repository: <https://github.com/theGeekist/skills>
- Release: <https://github.com/theGeekist/skills/releases/tag/v1.5.0>
- Both plugin manifests use version `1.5.0`.
- Release notes: [v1.5.0](release-notes/v1.5.0.md).
- The distribution retains the existing `geekist-architecture-skills` plugin identifier for compatibility; its displayed name is Geekist Skills.

Install the pinned collection:

```sh
npx skills add https://github.com/theGeekist/skills/tree/v1.5.0
```

The skills CLI prompts for skills and target agents. Its default scope is the current project; add `-g` for a user-wide installation. Review the selected destinations rather than assuming every installed client has the same discovery path. ChatGPT personal-skill installation uses its own supported installation mechanism, separately from this CLI.

For a canonical checkout shared by local clients:

```sh
git clone --branch v1.5.0 https://github.com/theGeekist/skills.git
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
4. Builds deterministic Git source archives, checksums and a release manifest.
5. Creates the tag at the checked commit if absent and publishes the GitHub release using the repository's normal Actions token.

An existing tag is never moved. If a tag exists but its release is missing, a run on a different commit stops with a recovery instruction. Run the workflow on the existing tag to finish publication for that commit. A same-version metadata update after publication is a no-op; a new release requires a new version and notes.

## Prepare the next release

Update `.codex-plugin/plugin.json` and `.claude-plugin/plugin.json` to the same next version. Write `release-notes/vX.Y.Z.md`, update the install reference in this file and README, and run the checks documented in CONTRIBUTING. Review brand/source notices with the release contents. Merge the prepared change or manually run the workflow on its intended commit, then verify the published tag, manifest and checksums.

Tag protection and additional repository security settings can strengthen immutability. They are maintenance tasks, not substitutes for the release checks or a reason to abandon an authorised release. Do not overwrite a published tag to repair a release; use a new version where content changes.

## Other distribution channels

The public release makes the collection available to compatible Agent Skills clients. Discovery on skills.sh is separate from successful installation; registry indexing can follow its own schedule.

The repository also carries Geekist-owned Codex and Claude marketplace metadata. Test the actual selected client and version before publishing command-level installation claims for that surface. The portable format does not establish native activation across CLI, desktop and cloud automatically.

External catalogue submissions, OCI packaging and self-hosted registries are optional follow-up work. Their account credentials, review processes and licensing terms are separate from the GitHub release. Keep registry records pointed at the canonical immutable release rather than maintaining independently edited copies. Do not accept a different licence, such as MIT-0, for a third-party catalogue without the owner's explicit choice.
