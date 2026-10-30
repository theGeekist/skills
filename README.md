<p align="center">
  <a href="https://geekist.co"><img src="assets/branding/readme-banner.svg" width="900" alt="Geekist"></a>
</p>

# [Geekist](https://geekist.co) Skills

**Clear agent writing. Consistent project meaning. Work that keeps moving.**

[![Language checks](https://github.com/theGeekist/skills/actions/workflows/language-checks.yml/badge.svg)](https://github.com/theGeekist/skills/actions/workflows/language-checks.yml)
[![Release](https://img.shields.io/github/v/release/theGeekist/skills)](https://github.com/theGeekist/skills/releases)
[![Skills: 11](https://img.shields.io/badge/skills-11-ffde59)](#choose-a-skill)
[![Licence: MIT](https://img.shields.io/badge/Licence-MIT-blue.svg)](LICENSE)

[Install](#install) · [Choose a skill](#choose-a-skill) · [Walkthrough](docs/language-system/skill-walkthrough.md) · [Research](#research-and-inspiration) · [Alternatives](#alternatives-and-differences)

Agents can write fluent paragraphs while changing a term's meaning, hiding a constraint or treating an unrun check as a reason to stop. These eleven skills connect project terminology, evidence and purpose-specific writing so engineering and business readers can follow the same work.

Every skill carries a short baseline for **consistency, accessibility, readability and repeatability**. Detailed references load for the relevant concern.

## See the difference

This invented example describes an approved implementation, not a shipped feature.

| Dense draft | Clearer task |
| --- | --- |
| Implementation of the administrator-scoped CSV export capability is authorised, with project-isolated request serialisation. Cross-project capacity qualification remains outstanding and constrains capacity claims. | Build CSV export for administrators, with a separate queue for each project. Test capacity across projects before making a capacity claim. |

The revision preserves authorisation, access restrictions, queue boundaries and the pending capacity check. Those same meanings can guide the decision record, developer guide, announcement and interface copy. [Follow a complete example →](docs/language-system/skill-walkthrough.md)

## Install

```sh
npx skills add https://github.com/theGeekist/skills/tree/v1.6.0
```

Select the skills and supported agent environments you need. Portable skills require no MCP server or runtime dependency. This command installs skills; ChatGPT plugin registration and mobile availability use a separate distribution route. See [publishing](PUBLISHING.md) and [installation observations](docs/language-system/installation-observations.md).

<a id="choose-a-language-skill"></a>
<a id="included-architecture-skills"></a>

## Choose a skill

Each overview includes an example request, expected result, sources and installation command. Choose the work at hand; there is no mandatory eleven-step pipeline.

| Your task | Skill overview |
| --- | --- |
| Establish shared concepts and terms | [Establish project language](docs/skills/establish-project-language.md) |
| Write tickets, acceptance criteria and handoffs | [Write implementation tasks](docs/skills/write-implementation-tasks.md) |
| Record a decision and its consequences | [Record architecture decisions](docs/skills/record-architecture-decisions.md) |
| Write tutorials, guides, references and explanations | [Write technical documentation](docs/skills/write-technical-documentation.md) |
| Explain supported customer value | [Write marketing content](docs/skills/write-marketing-content.md) |
| Write labels, progress, errors and dashboard states | [Write interface content](docs/skills/write-interface-content.md) |
| Review meaning and readability across artefacts | [Review project language](docs/skills/review-project-language.md) |
| Turn evidence gaps into useful next actions | [Advance with uncertainty](docs/skills/advance-with-uncertainty.md) |
| Review backend boundaries and orchestration | [Backend slice architecture](docs/skills/backend-slice-architecture.md) |
| Review frontend features and scenes | [Frontend slice architecture](docs/skills/frontend-slice-architecture.md) |
| Explicitly ask which writing workflow fits | [Write project content](docs/skills/write-project-content.md) |

Substantial edits can include original wording, the revision, its reason and retained constraints. Small edits need no separate revision artefact. Task-selected skills and persistent conversation instructions have different roles; see [client integration](docs/language-system/integration.md).

## Research and inspiration

Clear writing has established foundations. This collection adapts them to shared project meanings and connected artefacts.

| Foundation | Applied purpose |
| --- | --- |
| DDD, SKOS and Good Docs terminology | Context-specific meanings, concepts, labels and definitions |
| Microsoft, Google and public ISO abstracts | Concrete wording, reader purpose and explained jargon |
| Diátaxis, Good Docs and arc42 | Documentation purpose, usable procedures and relevant architecture views |
| MADR | Decision context, options, outcome and consequences |
| Atlassian | Interface wording matched to the user's situation |
| Agent Skills and selected Vale rules | Portable workflows, selective references and bounded checks |

[Original research](docs/language-system/research-baseline.md) · [Sources for every skill](standards/framework-evidence.md) · [Adopted, adapted and deferred](docs/language-system/framework-evaluation.md) · [Source revisions and licences](docs/language-system/sources.json)

The backend and frontend playbooks retain [@pipewrk](https://github.com/pipewrk)'s architecture rules, including their conditions and exceptions. External writing guidance improves their explanation; architectural changes require explicit approval. Read the complete [backend](skills/backend-slice-architecture/SKILL.md) and [frontend](skills/frontend-slice-architecture/SKILL.md) rules when applying that model.

## Alternatives and differences

Humanizer, Plain Writing, Writing Clearly and Concisely, and Plain Language Editor offer useful editorial approaches. Our [competitive review](docs/language-system/competing-writing-skills.md) compares the actual versions, organisation and trade-offs fairly.

The [design and differences](docs/language-system/design-and-differences.md) explains this collection's focus: maintaining accepted meanings, constraints and evidence as work moves between project artefacts. It also identifies the established practices we reuse. No head-to-head prose-quality or search-ranking superiority is claimed.

## Explore the system

| Explore | Follow |
| --- | --- |
| How the pieces connect | [Reader route and design](docs/language-system/architecture.md) · [Lifecycles](docs/language-system/lifecycles.md) |
| What has been checked | [Validation results](docs/language-system/validation-results.md) · [Context costs](docs/language-system/context-budget.json) |
| How to maintain it | [Contributing](CONTRIBUTING.md) · [Publishing](PUBLISHING.md) · [Implementation map](docs/language-system/implementation-status.json) |

Checks cover package structure, reference consistency, selected language signals and recorded agent cases. Native client activation and human comprehension need their own observations. Human search discovery and agent skill selection are separate concerns.

<details>
<summary><strong>Use a canonical local checkout</strong></summary>

```sh
git clone https://github.com/theGeekist/skills.git
cd skills
./scripts/link-local.sh --client all --dry-run
./scripts/link-local.sh --client all
```

Review conflicts before using `--adopt`; the linker preserves existing destinations. Update a clean checkout with `./scripts/update-local.sh --dry-run`, then `./scripts/update-local.sh`. Client paths and limitations are documented in [integration](docs/language-system/integration.md).

Canonical references live in `standards/`; independently installable copies live in `skills/`. Presentation data in `standards/skill-catalogue.json` generates metadata and `docs/skills/` overviews. See [contributing](CONTRIBUTING.md) for generation and drift checks.

</details>

---

Published by [Geekist](https://geekist.co) · Architecture by [@pipewrk](https://github.com/pipewrk) · [MIT licence](LICENSE) · [Security](SECURITY.md)
