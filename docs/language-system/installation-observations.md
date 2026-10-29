# Installation observations: v1.5.0

Recorded 29 October 2026. This is the initial v1.5.0 checkpoint; current language and source changes are recorded in [the v1.5.1 review](architecture-language-review.md).

## Completed

GitHub release `v1.5.0` is published from commit `d81fcb974ef24e0e8a80998d1a4a46bab1428516`, with source archives, checksums and a release manifest. The release workflow and language checks passed.

All eleven collection skills were installed in the owner's ChatGPT account through the supported personal-skill import/save workflow. The saved main files, references and packaged brand assets match the released source. Display names and prompts are preserved. The compatibility chooser retains `allow_implicit_invocation: false`.

## Brand assets and this import path

The initial portable packages include a G extracted from the site's handwritten wordmark. Jason subsequently clarified that the intended brand mark is Gk. The released G asset is therefore an incomplete brand adaptation; the Gk correction remains outstanding. Its `agents/openai.yaml` declares local small/large icon paths. See [brand provenance](../../assets/branding/README.md).

During this ChatGPT import, the service normalised metadata and assigned generated icons under `assets/icon.svg`, instead of using the declared Geekist icon paths. A single bounded attempt to replace that normalised display asset was restored to the service's default during saving. The original Geekist SVG assets remain saved with each skill.

This establishes a limitation of the exercised import path, not that every ChatGPT icon-customisation route is unavailable. No alternative account UI or native client icon route was tested. Further display-icon work should use a documented supported route rather than repeatedly editing a generated asset.

The personal skills were saved successfully. This does not establish ChatGPT plugin registration or mobile availability; the GitHub release and standalone personal-skill installation are separate from installing a plugin bundle. Clients consuming the portable icon metadata can use the packaged assets; verify their actual display when testing each client.

## Remaining adoption checks

Verify the distribution route for the intended surface before diagnosing a cache problem. Run the recorded ordinary-request selection cases in the intended client and capture native activation and reference loading. Installation and saved content are separate evidence from native implicit selection or displayed-icon support.

## v1.5.1 update verification

All eleven personal skills were updated after the language and attribution revisions. The saved remote main bodies and every bundled reference were compared with the v1.5.1 source and matched. This verifies saved personal-skill content, not mobile plugin installation or native implicit activation. Both GitHub workflows passed, and the published release manifest matches commit `3ef8ff5689871472dc4b5f8b600d057573a7593a`, tree `1ccb5aa3ea04f08f6d450d8e008ae7de130ac4a5` and all eleven skill names.

## v1.6.0 update verification

All eleven personal skills were updated after the editorial examples and presentation-catalogue changes. Saved remote main bodies, every bundled reference, display names, short descriptions and default prompts match the v1.6.0 source. The compatibility router remains explicit. Normalised display-icon behaviour is unchanged. This verifies saved personal content, not mobile plugin installation or native implicit selection.

The published v1.6.0 release manifest matches commit `8bc52c98bb1c79db223f087d819a5a4aca360730`, tree `091e7a0423505fa0df79f2a11cc5f42857212fa4` and all eleven skills. The release validation includes the new catalogue checks. GitHub About settings remain prepared rather than applied, as recorded in [discoverability](discoverability.md).
