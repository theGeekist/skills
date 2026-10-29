# Where the guidance comes from

Use this map to follow a skill's guidance back to its sources and local decisions. Frameworks inform selected practices; they do not certify the skills, prove reader comprehension or authorise changes to Jason's architecture rules.

## How sources are used

The [original research](../docs/language-system/research-baseline.md) is retained as supplied. The [framework evaluation](../docs/language-system/framework-evaluation.md) records what was adopted, adapted or deferred, including contrary findings. The [source manifest](../docs/language-system/sources.json) records reviewed pages, downloaded revisions, licences and executed experiments. These are different evidence states, not interchangeable endorsements.

The Good Docs Project, MADR, arc42, Agent Skills and Vale rule repositories were downloaded at recorded revisions. Selected templates were inspected; Vale and Agent Skills checks were executed. ISO 704 and ISO 24495-1 were reviewed through public abstracts only. The active guidance below is selective local writing, not a wholesale conversion of those standards or templates.

## Sources used by each skill

| Skill | Applied source or local authority | Where it changes the guidance |
| --- | --- | --- |
| `establish-project-language` | [DDD bounded contexts](https://martinfowler.com/bliki/BoundedContext.html), [SKOS labels and concepts](https://www.w3.org/TR/skos-reference/), [Good Docs terminology template](https://gitlab.com/tgdp/templates/-/tree/main/terminology-system); ISO 704 public abstract | Establish meaning within a context; keep preferred and alternative terms, definitions, relationships and source records. The JSON registry is a local model, not SKOS/RDF or ISO conformity. |
| `advance-with-uncertainty` | Jason's explicit requirement and the local uncertainty conventions | Keep evidence and implementation state distinct; pair a gap with a bounded next action. This is a local workflow rule, not a named external framework or proof that an option works. |
| `write-implementation-tasks` | Local task/handoff pattern; [Good Docs how-to guidance](https://gitlab.com/tgdp/templates/-/tree/main/how-to) informs goal and completion-oriented structure | Specify outcome, observable behaviour, validation and dependencies. This is not the Good Docs how-to template repurposed as a ticket, nor a mandatory Scrum process. |
| `record-architecture-decisions` | [MADR](https://adr.github.io/madr/) | Record context, viable options, outcome and consequences while retaining the project's ADR convention. Evidence/reconsideration and worker-continuation guidance are local additions. |
| `write-technical-documentation` | [Diátaxis](https://diataxis.fr/start-here/), [Good Docs concept/how-to templates](https://gitlab.com/tgdp/templates), [arc42 overview](https://arc42.org/overview/) | Select the reader's purpose; provide a usable procedure or concept explanation; use relevant architecture views for navigation. Do not require four documents or all twelve arc42 sections. |
| `write-marketing-content` | Local audience/value/claim patterns; [Microsoft plain words](https://learn.microsoft.com/en-us/style-guide/word-choice/use-simple-words-concise-sentences) and [Google jargon guidance](https://developers.google.com/style/jargon) inform expression | Explain supported value in words the audience can use. No downloaded marketing strategy framework or empirical conversion claim underpins this skill. |
| `write-interface-content` | [Atlassian voice and tone](https://atlassian.design/foundations/content/voice-tone/) plus local domain/state rules | Match wording to the user's situation. Distinguishing progress, confidence and eligibility, and requiring actual progress events, are local rules. |
| `review-project-language` | [Microsoft plain words](https://learn.microsoft.com/en-us/style-guide/word-choice/use-simple-words-concise-sentences), [Google jargon guidance](https://developers.google.com/style/jargon), [ISO 24495-1 public abstract](https://www.iso.org/standard/78907.html) | Check purpose, findability, explained terms and usable meaning. The four named repository outcomes are Jason's priorities, not a quoted ISO checklist or certification. |
| `backend-slice-architecture` | Jason's pre-language-system backend rules | External writing guides improve explanation and navigation only. DDD research on terminology is not authority to impose DDD architecture or change backend boundaries. |
| `frontend-slice-architecture` | Jason's pre-language-system frontend rules | External writing guides improve explanation and navigation only. Framework citations do not introduce new frontend requirements. |
| `write-project-content` | Local routing and context-budget decision; [Agent Skills specification](https://agentskills.io/specification) informs packaging | Select the purpose-specific workflow on explicit request. No external writing framework mandates this router or guarantees native host activation. |

All skills carry the shared language baseline. [Microsoft](https://learn.microsoft.com/en-us/style-guide/word-choice/use-simple-words-concise-sentences), [Google](https://developers.google.com/style/jargon) and the ISO plain-language abstract informed its reader-focused expression; its architecture authority and uncertainty boundaries remain local decisions. Purpose-specific references link directly to the relevant primary sources so an independently installed skill retains its evidence route without loading this entire map.

## Sources not converted into active requirements

- **ISO 1087 and TBX:** present in the original research, but not independently evaluated or implemented in this pass. No formal terminology-exchange feature is claimed.
- **DITA:** structured-topic and reuse ideas were considered; XML publishing infrastructure was deferred. The inspected official index lists DITA 2.0 as a draft.
- **Information Mapping:** the public information-types article was reviewed. Proprietary training and a converted method were not acquired or implemented.
- **ASD-STE100:** retrieval was blocked; controlled aerospace vocabulary was not adopted.
- **GOV.UK:** the evaluated URL redirected without substantive replacement content; it remains a research candidate rather than a claimed applied source.
- **Google/Diátaxis Vale packages:** executed experiments exposed false positives. Selected local advisory rules are active; the complete upstream styles are not enforced.

This map makes the lineage inspectable. The next check is whether the active wording faithfully applies the selected principle to its reader and task; a citation alone does not establish that.
