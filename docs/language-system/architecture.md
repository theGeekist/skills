# Shared language across agents and artefacts

Status: implemented foundation; selected runtime integrations remain experimental. Date: 29 October 2026.

## Purpose and decision

Help people understand the same project consistently across conversations, tasks, decisions, technical documentation and product content. A marketing reader should be able to navigate a technical document's purpose, decision and consequences, then find its deeper contracts and evidence.

Keep shared meaning and writing guidance independent of individual agent clients. Package task-specific guidance as portable skills. Keep persistent conversation guidance small. Make runtime hooks optional adapters.

## Where to find things

| Need | Location |
| --- | --- |
| Original research | [Unedited research baseline](research-baseline.md) |
| Verified sources, corrections and tool experiments | [Framework evaluation](framework-evaluation.md) and [source manifest](sources.json) |
| Writing and reader-navigation conventions | [Writing](../../standards/writing.md) and [content patterns](../../standards/content-patterns.md) |
| Discover or reconcile project meaning | [Establish project language](../../skills/establish-project-language/SKILL.md) |
| Choose an authoring or review skill | [Purpose-specific skill table](../../README.md#choose-a-skill) |
| Use the legacy entry point explicitly | [Writing workflow router](../../skills/write-project-content/SKILL.md) |
| Continue work through evidence gaps | [Advance with uncertainty](../../skills/advance-with-uncertainty/SKILL.md) and [shared conventions](../../standards/uncertainty.md) |
| User goals and scope additions | [Recorded requirements](requirements.md) |
| Operating and maintaining the system | [Lifecycles](lifecycles.md) |
| Install, check and experiment | [Integration guide](integration.md) |
| Remaining work and adoption decisions | [Recommendation pipeline](recommendations.json) |
| Actual project evidence and limitations | [Project evaluation](project-evaluation.md) and [validation results](validation-results.md) |
| Portable packaging and host boundaries | [Portability](portability.md) |
| Selection and reference loading | [Selection evaluation](selection-evaluation.md) and [architecture refactor](architecture-refactor.md) |

## Boundaries

The four acceptance outcomes are consistency, accessibility, readability and repeatability. Brevity is useful only when the meaning and reader's route survive.

Project owners retain their domain meanings and decision process. The shared system provides a record format and review method, rather than universal definitions for every project's vocabulary. Current repository decisions, schemas and tests inform discovery; contradictions require explicit resolution.

The backend and frontend playbooks retain their architecture rules, with smaller decision cores and conditionally loaded local references. Six specialist writing/review skills replace the broad authoring scope: tasks, ADRs, technical documentation, marketing, interface content and language review. Terminology discovery and actionable uncertainty remain focused skills. `write-project-content` is retained as an explicit compatibility router.

Every skill embeds the same short baseline generated from `standards/baseline.md`. This deliberate repetition makes the baseline available immediately after activation without requiring another skill or a full style guide. `standards/skill-profiles.json` declares purpose-specific bundled references. The sync checker detects drift in baseline blocks and reference copies. Read detail when the task requires it; bundling a file does not mean loading it on every invocation.

The registry and rules remain independent of agent runtime. The portable name/description identifies purpose; optional `agents/openai.yaml` carries Codex-facing metadata. Disabling the router's implicit invocation there is not a universal cross-agent switch. Other clients still use their own selection and loading semantics.

## Checks and judgement

The registry checker validates IDs, contexts, relationships and selected term collisions. Its text mode reports explicit aliases within a selected context. It does not discover undefined concepts, prove a definition correct or grade accessibility.

Vale supplies optional prose rules. Tool evaluation informs which rules are useful. Individual findings need context; broad commercial style packages can conflict with British English and ordinary conversation.

Independent agent cases test whether guidance transfers to realistic material. Catalogue-selection experiments show whether agents can distinguish the descriptions, and observed file reads show which staged resources they accessed. Neither establishes native runtime activation. Human comprehension remains a separate acceptance step. Hook subprocess tests establish adapter behaviour, not actual host support or replacement of already streamed prose.

## Alternatives considered

One large instruction file would load irrelevant detail into every exchange. Separate policies per agent would drift. References outside a skill directory would break independent installation. A fully formal RDF/TBX or XML publishing stack would add complexity before an interoperability need is demonstrated.

The initial JSON registry borrows context-aware labels and relationships from terminology practice and SKOS. It is not an implementation of SKOS, TBX or an ISO standard. Interchange can be added if a real consumer requires it.

## Consequences

The repository now includes optional local validation code and hook examples. This records the design discussion requested by CONTRIBUTING: the user explicitly approved tooling, evaluation, agent adapters and lifecycle checks. Skills remain usable as Markdown without installing validators, making network calls or enabling hooks.

Generated bundled references require a sync check. Runtime adapters require their own tests and version evidence. The public repo holds public sources and invented fixtures; private project material stays in a separate private evaluation record.

No global user configuration is overwritten. No project glossary is automatically approved. Publication remains a branch and reviewable pull request until merged.
