# Installation observations: v1.5.0

Recorded 29 October 2026.

## Completed

GitHub release `v1.5.0` is published from commit `d81fcb974ef24e0e8a80998d1a4a46bab1428516`, with source archives, checksums and a release manifest. The release workflow and language checks passed.

All eleven collection skills were installed in the owner's ChatGPT account through the supported personal-skill import/save workflow. The saved main files, references and packaged brand assets match the released source. Display names and prompts are preserved. The compatibility chooser retains `allow_implicit_invocation: false`.

## Brand assets and this import path

Every portable package includes the actual Geekist handwritten G, adapted from the current site's wordmark. Its `agents/openai.yaml` declares local small/large icon paths. See [brand provenance](../../assets/branding/README.md).

During this ChatGPT import, the service normalised metadata and assigned generated icons under `assets/icon.svg`, instead of using the declared Geekist icon paths. A single bounded attempt to replace that normalised display asset was restored to the service's default during saving. The original Geekist SVG assets remain saved with each skill.

This establishes a limitation of the exercised import path, not that every ChatGPT icon-customisation route is unavailable. No alternative account UI or native client icon route was tested. Further display-icon work should use a documented supported route rather than repeatedly editing a generated asset.

The skills are installed and usable independently of this cosmetic issue. Clients consuming the portable icon metadata can use the packaged assets; verify their actual display when testing each client.

## Remaining adoption checks

Reopen the Skills page if its installed list is cached. Run the recorded ordinary-request selection cases in the intended client and capture native activation and reference loading. Installation and saved content are separate evidence from native implicit selection or displayed-icon support.
