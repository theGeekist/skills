<p align="center">
  <a href="https://geekist.co"><img src="assets/branding/readme-banner.svg" width="900" alt="Geekist"></a>
</p>

# Geekist Skills

**Eleven agent skills for clearer writing and consistent project meaning.**

[![Language checks](https://github.com/theGeekist/skills/actions/workflows/language-checks.yml/badge.svg)](https://github.com/theGeekist/skills/actions/workflows/language-checks.yml)
[![Release](https://img.shields.io/github/v/release/theGeekist/skills)](https://github.com/theGeekist/skills/releases)
[![Skills: 11](https://img.shields.io/badge/skills-11-ffde59)](#find-the-right-skill)
[![Licence: MIT](https://img.shields.io/badge/Licence-MIT-blue.svg)](LICENSE)

**[Install](#installation) · [Choose a skill](#find-the-right-skill) · [Worked example](docs/language-system/skill-walkthrough.md) · [Research](#we-looked-at-what-already-existed) · [Competitor comparison](docs/language-system/competing-writing-skills.md)**

Agents have become remarkably articulate. They can produce technical documentation that would impress a committee of architects, draft elaborate implementation plans and explain relatively ordinary features with the sort of vocabulary once reserved for doctoral dissertations. Given enough encouragement, an agent could probably produce an entire philosophy of button placement before anyone gets around to implementing the button.

The difficulty becomes apparent when several agents begin working on the same project.

A feature originally described as a *project queue* might become a *tenant-isolated processing capability* in an architecture decision. Another agent subsequently documents its *request serialisation service*, while marketing announces a *distributed workflow engine* that the engineering team has yet to encounter.

Some of these descriptions might even be technically defensible. Unfortunately, the people responsible for implementing the feature must now establish whether everyone is discussing the same thing.

Similar problems appear throughout project documentation. Implementation tasks acquire elaborate abstractions that obscure fairly straightforward requirements. Architecture decisions explain the technology without adequately explaining the decision. Meanwhile, an outstanding capacity test can inspire an agent to declare the entire undertaking inadequately validated, despite the work being authorised and otherwise ready to proceed.

**Geekist Skills** grew out of these frustrations. We wanted agents to establish a common language for the work they were doing, with writing practices that remained useful as that work moved between different documents and audiences.

Four principles guide the collection:

| Principle | What it means |
|---|---|
| **Consistency** | Establish shared meanings and preserve them throughout a project. |
| **Accessibility** | Explain concepts at a level appropriate to the reader without sacrificing technical accuracy. |
| **Readability** | Organise information around its purpose and express it in natural language. |
| **Repeatability** | Give contributing agents dependable writing practices they can apply across the project. |

These principles matter because project documentation serves people with different responsibilities. An engineer may need a precise contract, while a product manager needs to understand what the capability makes possible. Marketing should be able to explain its value without accidentally inventing new functionality.

The language should adapt to the reader while the underlying meaning remains dependable.

## From impressive prose to useful work

Consider an ordinary feature. Administrators need to export data to CSV, with each project using a separate queue. The implementation has been authorised, although capacity testing across projects remains outstanding.

An agent might produce the following task:

| Before | After |
|---|---|
| Implementation of the administrator-scoped CSV export capability is authorised, with project-isolated request serialisation. Cross-project capacity qualification remains outstanding. | Build CSV export for administrators, with a separate queue for each project. Test capacity across projects before making a capacity claim. |

The original statement sounds important enough to warrant a steering committee, but the revised task is much easier to act upon.

Administrator permissions remain explicit, as does the requirement for queue isolation. The outstanding test has become an actionable item rather than a vaguely ominous qualification attached to the implementation.

This is a modest example of the approach behind Geekist. Improving a document requires understanding its source material and the reader's purpose, then making editorial decisions that preserve the requirements.

*The example uses invented source facts for demonstration.*

The **[worked example](docs/language-system/skill-walkthrough.md)** follows this feature through the project lifecycle. It shows how the implementation task informs an architecture decision and how that decision can subsequently be explained in developer documentation. The customer-facing material then presents the same capability in language appropriate to its audience.

The documents serve different purposes, but they remain accountable to the same source facts.

<a id="install"></a>

## Installation

Install the current collection:

`npx skills add theGeekist/skills`

Choose the skills and agent environments appropriate to your work. Each skill provides a short baseline with more detailed references available when the task warrants them.

There's no requirement to invoke the entire collection whenever an agent needs to write something. Software development has already accumulated enough ceremony without making technical prose another spectator sport.

For a reproducible installation of the v1.7.0 release:

`npx skills add https://github.com/theGeekist/skills/tree/v1.7.0`

This documentation accompanies v1.7.0. The versioned command becomes available when that release is published; the unversioned command installs the current default branch. See **[installation and client support](docs/language-system/integration.md)** for the available installation routes and supported client environments, including the separate ChatGPT plugin distribution process.

<a id="choose-a-skill"></a>
<a id="choose-a-language-skill"></a>
<a id="included-architecture-skills"></a>

## Find the right skill

The collection covers several parts of project communication, from establishing terminology through to producing the documents that depend upon it. Architecture guidance is included because the way we organise a system influences the language used to describe it.

| Skill | Purpose |
|---|---|
| **[Establish project language](docs/skills/establish-project-language.md)** | Establish agreed meanings for project concepts before contributing agents develop incompatible vocabularies. |
| **[Advance with uncertainty](docs/skills/advance-with-uncertainty.md)** | Describe evidence gaps accurately and connect them to useful next actions. |
| **[Write implementation tasks](docs/skills/write-implementation-tasks.md)** | Express implementation work through clear objectives and acceptance criteria, with the relevant constraints preserved. |
| **[Record architecture decisions](docs/skills/record-architecture-decisions.md)** | Document the reasoning behind technical decisions while that reasoning is still available to the people who made them. |
| **[Write technical documentation](docs/skills/write-technical-documentation.md)** | Explain systems according to reader needs while retaining their technical contracts. |
| **[Write marketing content](docs/skills/write-marketing-content.md)** | Communicate product value through credible claims and an appropriate editorial voice. |
| **[Write interface content](docs/skills/write-interface-content.md)** | Explain application behaviour so users understand what happened and how to proceed. |
| **[Review project language](docs/skills/review-project-language.md)** | Improve writing while checking its consistency with established terminology and source material. |
| **[Backend slice architecture](docs/skills/backend-slice-architecture.md)** | Apply capability-first organisation with explicit orchestration and protected public boundaries. |
| **[Frontend slice architecture](docs/skills/frontend-slice-architecture.md)** | Organise frontend features around clear ownership and appropriate shared components. |
| **[Write project content](docs/skills/write-project-content.md)** | Select the appropriate writing workflow without requiring callers to understand the entire collection. |

Each skill has a dedicated overview with a practical example. The overview also provides installation instructions and references to the sources behind its guidance.

<a id="research-and-inspiration"></a>
<a id="alternatives-and-differences"></a>

## We looked at what already existed

The problems that motivated Geekist have been studied for considerably longer than agents have been producing documentation.

Domain-driven design introduced many engineers to the importance of shared terminology. Technical-writing frameworks have explored how documentation should be organised around the reader's purpose. Editorial guidance has spent decades encouraging authors to communicate clearly, often with the heroic ambition of convincing technical specialists to use ordinary verbs.

More recently, agent skills have brought these practices into automated writing workflows.

We examined existing implementations to understand the approaches they offered. Some were especially useful for preserving meaning during revision, while others addressed document structure or the recognisable habits of generated prose.

The research informed changes to our own skills, with the resulting practices incorporated into their instructions and supporting material.

| Existing skill | Practices incorporated |
|---|---|
| **Humanizer** | Check revisions for invented claims and changed meaning. Preserve deliberate authorial voice where appropriate. |
| **Plain Writing** | Prefer concrete explanations over needless abstraction. |
| **Hamel's Plain Writing variant** | Make consequential edits inspectable by showing the original and explaining what changed. |
| **Plain Language Editor** | Examine a document's purpose and structure before concentrating on individual sentences. |
| **Writing Clearly and Concisely** | Keep instructions economical while providing deeper references when needed. |

We adapted these practices rather than importing complete editorial systems. The examples and editorial patterns in Geekist are locally authored, with attribution to the work that influenced them.

This distinction is important because writing serves different purposes. A reflective essay may benefit from an unusual rhythm, while an architecture decision depends upon exact technical qualifications. Marketing presents another editorial problem altogether.

An approach that flattens every document into the same voice may improve superficial consistency at the expense of the writing itself.

**[Competitor comparison](docs/language-system/competing-writing-skills.md) · [Incorporated practices](docs/language-system/competitive-adoption.md) · [Implementation map](docs/language-system/implementation-status.json)**

## Frameworks behind the collection

Our research also explored established frameworks whose principles could support consistent project communication.

| Foundation | Contribution |
|---|---|
| **DDD and SKOS** | Shared concepts and context-specific meanings, with distinctions between concepts and their labels. |
| **Good Docs terminology guidance** | Practical patterns for defining project language. |
| **Diátaxis and Good Docs** | Documentation organised around what readers need to accomplish. |
| **MADR** | Recording decisions with their context and consequences. |
| **arc42** | Useful architecture views and supporting technical explanations. |
| **Microsoft, Google and plain-language guidance** | Reader-focused expression and concrete explanations. |
| **Atlassian content guidance** | Interface writing informed by the user's situation. |

Each framework addresses a particular concern. DDD provides a useful foundation for establishing meaning within a bounded context, while Diátaxis helps authors recognise that a tutorial serves a different purpose from a reference document.

MADR offers a disciplined way to explain architecture decisions, particularly when future maintainers need to understand why an alternative was rejected.

Geekist brings these ideas into workflows that agents can apply during ordinary project work. The research remains available for anyone interested in the original approaches and our adaptations.

**[Original research](docs/language-system/research-baseline.md) · [Framework adaptations](docs/language-system/framework-evaluation.md) · [Source references](standards/framework-evidence.md)**

## Keeping a project consistent

One of the limitations of treating writing as an isolated editing problem is that a document can become clearer while the project becomes more confusing.

Imagine an engineering report stating that the required checks have been completed. A subsequent release announcement describes the feature as approved, although the report never established that approval had been granted.

The distinction may seem minor to someone concentrating exclusively on sentence quality. It becomes much more significant when the announcement is used to justify a release.

Geekist approaches writing through the meaning established by its sources. The terminology belongs to the project, and each document has a responsibility to represent that terminology accurately. Editorial changes may improve how information is presented, but they must respect the authority of the material being revised.

The approach also applies to uncertainty. When an assumption requires testing, the documentation should explain what remains to be established. Where the work can proceed within known constraints, an agent should be able to express that position without turning every pending measurement into a constitutional crisis.

This becomes especially useful across long-running projects, where new contributors inherit decisions made months earlier. A shared language reduces the effort required to understand what has already been established and helps prevent subsequent documents from quietly redefining it.

Each skill carries the common writing baseline and refers to more specialised guidance when needed. That allows the collection to remain coherent without burdening every small writing task with unrelated instructions.

## Architecture rules have an owner

The backend and frontend playbooks express **[@pipewrk](https://github.com/pipewrk)'s architecture rules**.

Those rules describe particular engineering choices. Geekist's editorial guidance helps explain them more clearly while preserving the underlying decisions.

The distinction deserves explicit attribution. Readers should understand that the architecture rules originate with @pipewrk, while the writing practices provide a consistent way to communicate them.

**[Backend rules](skills/backend-slice-architecture/SKILL.md) · [Frontend rules](skills/frontend-slice-architecture/SKILL.md) · [Architecture source and preservation](docs/language-system/architecture-rule-preservation.md)**

## Inspect the work

We have made the research available alongside the implementation so readers can examine the sources and understand how particular practices found their way into the collection.

| Area | References |
|---|---|
| How the skills work together | **[Walkthrough](docs/language-system/skill-walkthrough.md) · [System design](docs/language-system/architecture.md)** |
| Research foundations | **[Research](#we-looked-at-what-already-existed) · [Source map](standards/framework-evidence.md) · [Competitor comparison](docs/language-system/competing-writing-skills.md)** |
| Validation evidence | **[Validation results](docs/language-system/validation-results.md) · [Recorded trials](evaluations/README.md) · [Context measurements](docs/language-system/context-budget.json)** |
| Maintenance and distribution | **[Contributing](CONTRIBUTING.md) · [Publishing](PUBLISHING.md) · [Client integration](docs/language-system/integration.md)** |

The recorded trials and package checks are presented with their actual scope. They provide useful evidence about implementation behaviour, although their results should not be interpreted as controlled studies of human comprehension.

That distinction is particularly relevant for a collection whose purpose includes preserving source integrity. Our own documentation should meet the same standards we expect agents to apply elsewhere.

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

Published by **[Geekist](https://geekist.co)** · Architecture by **[@pipewrk](https://github.com/pipewrk)** · **[MIT licence](LICENSE)**
