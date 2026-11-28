<p align="center">
  <a href="https://geekist.co"><img src="assets/branding/readme-banner.svg" width="720" alt="Geekist Skills: clear agent prose, consistent project meaning"></a>
</p>

# Geekist Skills

**Give AI agents a shared language for your project.**

13 Geekist-authored skills help teams carry terms, decisions and product facts into tasks, docs and customer-facing copy. 27 attributed skills add distinct approaches to README craft, positioning, storytelling and developer adoption.

[![Language checks][checks-badge]][checks-url]
[![Latest release][release-badge]][release-url]
[![40 skills][skills-badge]][catalogue-url]
[![MIT licence][license-badge]][license-url]

[Install](#quick-start) · [Choose a skill](#choose-by-the-work) · [See the walkthrough](docs/language-system/skill-walkthrough.md) · [Explore the research](#research-and-design)

## Why Geekist Skills

An agent can make a sentence sound polished while quietly changing what a project means. A queue becomes a service, an untested assumption becomes a release claim, and each document introduces a new name for the same feature.

Geekist Skills help teams carry shared meaning through everyday project work. Use them to clarify terms, shape implementation work, explain systems, write product copy and prepare professional outreach with the source facts in view.

## What you can do

- **Keep project language aligned.** Define domain terms and reuse them across code, decisions and documentation.
- **Turn decisions into useful work.** Write implementation tasks, acceptance criteria and architecture records with clear consequences.
- **Explain systems for their readers.** Create technical documentation, reports, interface messages and product stories from project facts.
- **Prepare product and launch content.** Clarify positioning, improve READMEs and shape launch materials for developers and customers.
- **Research and write professional outreach.** Find a credible reason to contact someone and write a message that reflects the real relationship.
- **Choose among distinct methods.** Thirteen Geekist-authored skills sit alongside 27 attributed skills for positioning, storytelling, editing, README craft and developer adoption.

Each skill can be installed on its own. Combine skills when a task benefits from more than one perspective.

## Quick start

Install the collection in an Agent Skills-compatible environment:

```sh
npx skills@latest add theGeekist/skills
```

Then ask for the work in ordinary language. For example:

```text
Clarify what “eligible” means in this project. Check the code, tests and product copy, then summarize the definitions and any conflicts.
```

To install a single skill, add `--skill` and its name:

```sh
npx skills@latest add theGeekist/skills --skill establish-project-language
```

## Choose by the work

| Work you have | Start with |
|---|---|
| A term has several meanings across code and documents | [Establish Project Language](docs/skills/establish-project-language.md) |
| A decision needs to become a ticket, plan or handoff | [Write Implementation Tasks](docs/skills/write-implementation-tasks.md) |
| A system needs an explanation for developers or customers | [Write Technical Documentation](docs/skills/write-technical-documentation.md) |
| Product claims and launch messages need a clear story | [Write Marketing Content](docs/skills/write-marketing-content.md) |
| A README needs stronger structure and visual guidance | [Readme Craft](docs/skills/readme-craft.md) |
| Ads and sales copy need a strong hook, story and offer | [Direct Response Copywriting](docs/skills/direct-response-copywriting.md) |
| A professional contact needs relevant research and a personal message | [Research Opportunities](docs/skills/research-outreach-opportunities.md) and [Write Outreach](docs/skills/write-outreach.md) |

[Browse all 40 skills](docs/skills/index.md) to compare their purposes, examples and sources.

## See the method in context

The walkthrough follows one feature from its original facts through an implementation task, an architecture decision and developer documentation. It shows how the wording changes for each reader while the underlying meaning stays consistent.

→ [Read the project walkthrough](docs/language-system/skill-walkthrough.md)

## Installation options

The `skills` CLI installs the full collection or an individual skill into a supported agent environment. After v1.10.0 is published, install that release with:

```sh
npx skills@latest add https://github.com/theGeekist/skills/tree/v1.10.0
```

The v1.10.0 release will include a dedicated ChatGPT plugin archive. [Client support and installation routes](docs/language-system/integration.md) describe the separate plugin distribution and local checkout options.

## Research and design

The Geekist-authored skills follow four principles:

| Principle | How it helps |
|---|---|
| **Consistency** | Keep shared meanings stable across project work. |
| **Accessibility** | Explain ideas at the level the reader needs while preserving technical accuracy. |
| **Readability** | Organise content around its purpose and use natural language. |
| **Repeatability** | Give contributors practices they can apply across tasks and documents. |

Read the [research foundations](docs/language-system/research-baseline.md), [framework adaptations](docs/language-system/framework-evaluation.md), [source map](standards/framework-evidence.md) and [comparison with other writing skills](docs/language-system/competing-writing-skills.md).

### Source and architecture

The 27 imported skills keep their upstream instructions, commit-pinned attribution and original MIT licence notices. The [external skills review](docs/language-system/external-skills-review.md) records package compatibility, runtime requirements and the source evaluation.

The backend and frontend playbooks express [@pipewrk's architecture rules](docs/language-system/architecture-rule-preservation.md). Geekist's writing guidance helps explain those decisions while their architecture remains attributed to its authors.

## Contribute and inspect

Canonical writing references live in `standards/`; generated skill overviews live in `docs/skills/`. [Contributing](CONTRIBUTING.md) explains how to update references, regenerate outputs and run local checks. [Validation results](docs/language-system/validation-results.md) and [recorded evaluations](evaluations/README.md) describe the scope of available evidence.

README crafted with [Readme Craft](docs/skills/readme-craft.md) · Published by [Geekist](https://geekist.co) · Architecture by [@pipewrk](https://github.com/pipewrk) · [MIT licence](LICENSE)

[checks-badge]: https://github.com/theGeekist/skills/actions/workflows/language-checks.yml/badge.svg
[checks-url]: https://github.com/theGeekist/skills/actions/workflows/language-checks.yml
[release-badge]: https://img.shields.io/github/v/release/theGeekist/skills
[release-url]: https://github.com/theGeekist/skills/releases
[skills-badge]: https://img.shields.io/badge/skills-40-ffde59
[catalogue-url]: docs/skills/index.md
[license-badge]: https://img.shields.io/badge/licence-MIT-blue.svg
[license-url]: LICENSE
