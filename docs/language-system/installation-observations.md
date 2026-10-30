# Installation and distribution

The collection contains eleven independently installable skills. Each package includes its main instructions, presentation metadata and required local references. A source archive, a local skill installation and a registered ChatGPT plugin are separate distribution steps.

## Install the versioned collection

```sh
npx skills add https://github.com/theGeekist/skills/tree/v1.7.0
```

Use `--skill <name>` to select one workflow. Each [skill overview](../skills/index.md) provides its exact command, example request and source links. Choose the target client and installation scope supported by that client.

For a canonical checkout shared by local clients, follow [the local installation guide](integration.md) and inspect `scripts/link-local.sh --client all --dry-run` before linking files.

## Current source and tagged releases

The v1.7.0 source includes the E001–E008 editorial-pattern reference and explicit final editing passes. Its versioned command becomes available when the release is published. The immutable v1.6.0 package predates those additions.

Use a published versioned tag for a fixed package, or pin a commit when evaluating newer instructions. Documentation and source changes do not move an existing release tag.

## Verify the installed package

Check that the client exposes the intended skill and can read its bundled reference. Use a representative task and record the client version and execution mode when reporting an installation issue. A successful portable-format check establishes package structure; it does not establish that every client discovers the same directory or loads the same instructions.

Presentation metadata declares icon paths within each skill. Clients may render or normalise those assets differently. See [brand provenance](../../assets/branding/README.md) for the packaged wordmark and assets.

## ChatGPT and mobile

Publishing a GitHub release does not register or install a ChatGPT plugin. The skills CLI installs into supported agent environments; ChatGPT distribution uses its supported skill or plugin installation route. Mobile availability depends on an installed plugin bundle and the account's supported surfaces, rather than the presence of repository files alone.

Consult the [official plugin guide](https://learn.chatgpt.com/docs/plugins) and [skill authoring guide](https://learn.chatgpt.com/docs/build-skills) for the current surface-specific routes. The [portability guide](portability.md) distinguishes package support from native activation evidence.

## Release verification

Published archives include a release manifest with the commit, Git tree and skill list, plus checksums. The v1.6.0 manifest identifies commit `8bc52c98bb1c79db223f087d819a5a4aca360730`, tree `091e7a0423505fa0df79f2a11cc5f42857212fa4` and all eleven skills. See [release and distribution](../../PUBLISHING.md) for archive verification and versioning.

Documentation updates can be published without creating a new skill release. Versioned install commands continue to identify the instructions in that release.
