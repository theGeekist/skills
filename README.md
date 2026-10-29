# Geekist Skills

[![Licence: MIT](https://img.shields.io/badge/Licence-MIT-blue.svg)](LICENSE)

Portable agent skills for architecture and shared project language. Review and evolve feature-first systems, establish domain meanings, and write material that technical and business readers can navigate.

The playbooks help coding agents make architecture decisions about ownership, public APIs, orchestration, dependencies and shared infrastructure. They are framework-neutral and adapt to the repository in front of them rather than imposing a fixed folder taxonomy.

Published by [Geekist](https://geekist.co).

## Find your route

| You want to… | Start here |
| --- | --- |
| Pick a workflow for today's work | [Choose a language skill](#choose-a-language-skill) or [architecture skill](#included-architecture-skills) |
| See how the skills work together | [A feature through the writing workflows](#follow-one-feature-through-the-workflows) and [the detailed walkthrough](docs/language-system/skill-walkthrough.md) |
| Understand what informed the guidance | [Research and inspiration](#research-and-inspiration) and [the skill-to-evidence map](standards/framework-evidence.md) |
| Follow meaning from discovery to maintained documents | [Reader route and system design](docs/language-system/architecture.md), then [lifecycles](docs/language-system/lifecycles.md) |
| Inspect the evidence and reproduce checks | [Framework evaluation](docs/language-system/framework-evaluation.md), [source register](docs/language-system/sources.json) and [validation results](docs/language-system/validation-results.md) |
| Install or integrate the collection | [Install](#install), [client integration](docs/language-system/integration.md) and [publishing](PUBLISHING.md) |
| Review the next improvements | [Recommendation pipeline](docs/language-system/recommendations.json) |

## Research and inspiration

The collection began with a practical problem: agents and project documents can introduce competing terms, dense explanations and evidence labels that stop useful work. The [original research](docs/language-system/research-baseline.md) is retained verbatim, alongside a [primary-source evaluation](docs/language-system/framework-evaluation.md) that corrects claims, records experiments and explains what was adopted, adapted or deferred.

These sources serve different jobs. Terminology establishes meaning; document patterns help readers find it; plain-language guidance explains it; tools catch specific repeatable mistakes. A style checker cannot settle a domain disagreement, and a readable sentence can still make a false claim.

| Inspiration | How it informs the collection | Follow the guidance |
| --- | --- | --- |
| [DDD bounded contexts](https://martinfowler.com/bliki/BoundedContext.html), [ISO 704](https://www.iso.org/standard/79077.html) and [W3C SKOS](https://www.w3.org/TR/skos-reference/) | Context-specific meanings, distinct concepts, stable identifiers and explicit preferred/alternative labels | [Establish project language](skills/establish-project-language/SKILL.md) and [terminology guidance](standards/writing.md) |
| [ISO plain-language principles](https://www.iso.org/standard/78907.html), [Microsoft](https://learn.microsoft.com/en-us/style-guide/word-choice/use-simple-words-concise-sentences) and [Google's jargon guidance](https://developers.google.com/style/jargon) | Reader purpose, concrete wording and explanations of necessary technical terms | [Shared baseline](standards/baseline.md) and [language review](skills/review-project-language/SKILL.md) |
| [Diátaxis](https://diataxis.fr/start-here/) and [The Good Docs Project](https://gitlab.com/tgdp/templates) | Choose between learning, completing a task, looking up a contract and understanding a concept; use practical templates selectively | [Technical documentation](skills/write-technical-documentation/SKILL.md) |
| [MADR](https://adr.github.io/madr/) | Record context, viable options, the decision and consequences without unnecessary ceremony | [Architecture decisions](skills/record-architecture-decisions/SKILL.md) |
| [arc42](https://arc42.org/overview/) | Check whether architecture explanations expose the relevant context, runtime, deployment, quality and glossary views | [Technical documentation guidance](standards/technical-documentation.md) |
| [Atlassian's voice and tone](https://atlassian.design/foundations/content/voice-tone/) | Match interface wording to the user's situation and next useful action | [Interface content](skills/write-interface-content/SKILL.md) |
| [Agent Skills](https://agentskills.io/specification) and [Vale](https://vale.sh/) | Package focused workflows with selective references; check selected wording patterns while retaining contextual review | [Skill design](docs/language-system/skill-design.md) and [tool experiments](docs/language-system/framework-evaluation.md#tools-installed-and-exercised) |

The [skill-to-evidence map](standards/framework-evidence.md) covers all eleven entry points, including the locally synthesised workflows:

| Skill | Basis and purpose |
| --- | --- |
| [`backend-slice-architecture`](skills/backend-slice-architecture/SKILL.md) | Jason's original backend rules; shared language guidance improves their explanation without changing the architecture |
| [`frontend-slice-architecture`](skills/frontend-slice-architecture/SKILL.md) | Jason's original frontend rules; shared language guidance improves their explanation without adding requirements |
| [`establish-project-language`](skills/establish-project-language/SKILL.md) | Contextual meaning from DDD, concept-first terminology from ISO 704 and concept/label distinctions from SKOS |
| [`write-implementation-tasks`](skills/write-implementation-tasks/SKILL.md) | Local synthesis of observable outcomes, concrete behaviour, validation and handoffs, using the shared terminology and plain-language baseline |
| [`record-architecture-decisions`](skills/record-architecture-decisions/SKILL.md) | MADR-inspired decision structure, adapted to existing project conventions |
| [`write-technical-documentation`](skills/write-technical-documentation/SKILL.md) | Diátaxis purpose selection, selected Good Docs patterns and arc42 completeness views |
| [`write-marketing-content`](skills/write-marketing-content/SKILL.md) | Local audience/value/claim structure using plain-language principles and source-grounded project meanings; not a converted marketing standard |
| [`write-interface-content`](skills/write-interface-content/SKILL.md) | Situational content guidance informed by Atlassian, alongside local state and next-action patterns |
| [`review-project-language`](skills/review-project-language/SKILL.md) | Shared reader-centred baseline, terminology consistency and contextual review of tool findings |
| [`advance-with-uncertainty`](skills/advance-with-uncertainty/SKILL.md) | Jason's requirement to keep evidence honest and implementation actionable; local task/ADR examples test that behaviour |
| [`write-project-content`](skills/write-project-content/SKILL.md) | Local explicit workflow chooser; routes to the relevant specialist rather than adding a new framework |

These are inspirations and adapted practices, not claims of certification or wholesale framework adoption. Jason's backend and frontend architecture rules remain the authority for those two playbooks; external frameworks do not authorise changing them.

The evaluation also records why DITA publishing infrastructure and ASD-STE100 adoption were deferred, why proprietary Information Mapping material was not converted, and why blanket Google/Diátaxis Vale rules were unsuitable. Full ISO normative texts were not acquired. Downloaded templates and executed tool checks are distinguished from public-source references and candidate sources in the [evaluation](docs/language-system/framework-evaluation.md).

The current checks cover package structure, terminology, reference consistency and selected agent cases. Actual client activation and human comprehension need their own observations; [validation results](docs/language-system/validation-results.md) makes those limits and next actions visible.

## Install

Install the versioned collection from the public repository:

```sh
npx skills add https://github.com/theGeekist/skills/tree/v1.5.1
```

This command installs skills into supported agent environments; it does not register a ChatGPT plugin or make the bundle available on mobile. ChatGPT plugin distribution requires a separate import or publishing step; see [publishing](PUBLISHING.md) and [installation observations](docs/language-system/installation-observations.md).

The skills use portable Markdown with YAML frontmatter and optional client metadata. They require no MCP server or runtime dependency. Optional repository checks and a Codex hook example are separate from skill installation.

Version **v1.5.1** makes framework sources and walkthroughs visible across all eleven skills and improves language while preserving architecture meaning. Version **v1.5.0** introduced the shared language system and focused writing workflows. See the [architecture and reader route](docs/language-system/architecture.md), [evaluation results](docs/language-system/validation-results.md) and [integration guide](docs/language-system/integration.md).

## Choose a language skill

Every skill carries the same short writing baseline. Choose by the requested work; a marketing author can use the marketing skill directly without loading architecture guidance.

| Requested work | Skill |
| --- | --- |
| Discover and reconcile project meanings | [`establish-project-language`](skills/establish-project-language/SKILL.md) |
| Engineering tickets, acceptance criteria and worker handoffs | [`write-implementation-tasks`](skills/write-implementation-tasks/SKILL.md) |
| Architecture decision records (ADRs) | [`record-architecture-decisions`](skills/record-architecture-decisions/SKILL.md) |
| Tutorials, how-to guides, technical references and explanations | [`write-technical-documentation`](skills/write-technical-documentation/SKILL.md) |
| Marketing copy, announcements and positioning | [`write-marketing-content`](skills/write-marketing-content/SKILL.md) |
| Interface labels, dashboard states, progress and errors | [`write-interface-content`](skills/write-interface-content/SKILL.md) |
| Review terminology, reader navigation and consistent meaning | [`review-project-language`](skills/review-project-language/SKILL.md) |
| Turn evidence gaps into useful next actions | [`advance-with-uncertainty`](skills/advance-with-uncertainty/SKILL.md) |

`write-project-content` remains a compatibility entry point for explicit callers who want help choosing a writing workflow. It is no longer the broad default authoring skill. Codex metadata disables its implicit invocation; other clients must apply their own selection rules.

The acceptance outcomes are consistency, accessibility, readability and repeatability. Full reference material is bundled for independent installation, while each skill explains which detail to load for the task.

## Follow one feature through the workflows

Consider an illustrative feature that lets customers export a report. Establish what “report”, “export” and “ready” mean from the project's contracts and current behaviour. Use the architecture skills only when deciding capability ownership or screen composition; record a consequential choice with the ADR skill. Turn the intended behaviour into implementation tasks with observable acceptance results.

After implementation, explain how to export and what the result contains in technical documentation. Translate the same capability into supported customer value for marketing, then write interface states such as “Preparing export” and “Download report”. Review these artefacts together: each can use different words for its audience while preserving the same meaning and constraints. When a claim still needs testing, use the uncertainty skill to name the bounded check and dependent decision.

This is a reader route, not a required sequence or a reason to invoke every skill. Choose the entry point that fits the work; use the explicit compatibility router only when you want help choosing. The [detailed walkthrough](docs/language-system/skill-walkthrough.md) follows all eleven skills through inputs, decisions and resulting artefacts.

## Included architecture skills

### Backend slice architecture

`backend-slice-architecture` applies a capability-first backend architecture. Behaviour starts inside an owned capability, cross-capability workflows remain explicit, and shared infrastructure is introduced only when reuse has been earned.

Use it to:

- review service and package boundaries;
- design explicit public APIs and prevent deep imports;
- separate capability rules from application orchestration;
- adapt capability ownership to `apps/`, `packages/`, `libs/`, modules or equivalent project roots;
- plan incremental migration through code already being changed.

### Frontend slice architecture

`frontend-slice-architecture` applies a feature-first frontend architecture. UI, state and hooks begin inside an owned feature, scenes stay thin, and shared components or hooks emerge only after genuine reuse.

Use it to:

- review feature ownership and scene composition;
- keep feature internals private behind explicit public surfaces;
- separate route-level orchestration from feature behaviour;
- support web, native and multi-platform frontends without prescribing a framework;
- migrate existing applications by touch instead of reorganising them wholesale.

## Architecture model

Both skills share the same operating model:

| Concern | Default home | Promoted home | Composition surface |
| --- | --- | --- | --- |
| Backend behaviour | Owned capability | Agnostic infrastructure or shared service | Application workflow or use case |
| Frontend behaviour | Owned feature | Agnostic component, hook or service | Scene, page or route |

The default direction of travel is local to shared. Early duplication is acceptable. Promotion happens when repetition is visible, the abstraction is stable and sharing improves correctness or reduces meaningful friction.

The backend playbook uses `package-shaped` for an independently testable boundary with an explicit public surface and enforceable dependencies, without requiring a `package.json` or publishable package. The frontend playbook keeps features ready for later packaging through explicit public surfaces and package-safe imports. Neither prescribes a particular workspace root name. See the [backend rules](skills/backend-slice-architecture/SKILL.md) and [frontend rules](skills/frontend-slice-architecture/SKILL.md) for their exact conditions and exceptions.

## Use with an agent

Invoke a skill explicitly in clients that support named skills:

```text
Use $backend-slice-architecture to review this service boundary and propose the smallest migration-by-touch.
```

```text
Use $frontend-slice-architecture to review this feature and scene composition without changing the framework.
```

Clients that support automatic skill selection can also select either playbook from its description.

## Install from a canonical local checkout

For active development, keep one Git checkout as the local source of truth and link its skill directories into compatible clients. This avoids copied, client-specific variants.

```sh
git clone https://github.com/theGeekist/skills.git
cd skills
./scripts/link-local.sh --client all --dry-run
./scripts/link-local.sh --client all
```

The linker uses:

- `~/.agents/skills` for Codex, Gemini CLI and desktop Antigravity;
- `~/.claude/skills` for Claude Code;
- `~/.gemini/antigravity-cli/skills` when Antigravity CLI is installed.

Correct links are left untouched. Existing destinations cause the command to fail safely. Use `--adopt` only after reviewing a conflict; it moves the existing entry to a timestamped backup before creating the link.

### Update the local checkout

```sh
./scripts/update-local.sh --dry-run
./scripts/update-local.sh
```

The updater refuses dirty or detached checkouts, pulls with `--ff-only`, runs the official GitHub Agent Skills validator when available, and verifies the client links.

## Repository structure

- `skills/`: independently installable skills with their own required references and optional client metadata.
- `standards/baseline.md`: the short authored baseline embedded in every skill.
- `standards/skill-profiles.json`: which canonical references each skill bundles.
- `standards/`: task-specific writing references and terminology.
- `scripts/`: baseline/reference generation and checks.
- `adapters/`: opt-in persistent instruction and runtime examples.
- `evaluations/`: public prompts, source snapshots, observed results and scope limitations.

Run `python3 scripts/sync-language-references.py` after changing the baseline or canonical references, and `python3 scripts/sync-language-references.py --check` before committing. Generated copies retain one source of truth while allowing each skill to be installed alone. Architecture-specific references are authored within their respective skill.

## Compatibility

The skills follow the portable Agent Skills shape and include optional Codex-facing display metadata under `agents/openai.yaml`. They can be used by compatible agent clients without changing the core instructions.

## Publishing

This repository is the canonical public source. Registry records should point back to an immutable release rather than carry edited copies. See [PUBLISHING.md](PUBLISHING.md) for the release checklist and account-specific steps.

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md) to propose changes and [SECURITY.md](SECURITY.md) to report vulnerabilities privately.

## Licence

MIT. See [LICENSE](LICENSE).
