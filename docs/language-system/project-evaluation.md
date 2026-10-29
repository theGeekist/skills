# Project evaluation

Inspection date: 29 October 2026. Source inspection was followed by fresh-context agent authoring and navigation trials. These are qualitative agent evaluations, not human comprehension evidence or project runtime qualification.

## Coverage

| Project | Material inspected | Result |
| --- | --- | --- |
| `theGeekist/llm-core` | Repository instructions, package overview, schema decision, control contracts and their tests | Public, revision-pinned terminology and three cross-audience cases in `evaluations/projects/llm-core.json` |
| TaskGraph | Private instructions, overview, existing terminology material, decisions, contracts and test sources | Private assessment and cases retained separately; no private source copied into this repository |
| Simple Assembly | Private instructions, overview, authority material, contracts and test sources | Repository identity resolved and private assessment retained separately; no private source copied into this repository |

The public `llm-core` snapshot is `4f9e37ac92bcd055a836806ea463510ed32a8bcc`. Its cloud clone was used as research context. It is not a substitute for the maintainer's selected working checkout, task authority or integration evidence.

## Findings supported by public evidence

The `llm-core` repository distinguishes the shared documentation site from package-owned engineering authority. A language workflow must follow that distinction: discovery begins with the selected package's README and current decisions, rather than treating all Markdown as equally current.

Its package overview supplies an unusually useful plain-language boundary: the package supplies portable contracts, conformance, authority and evidence; a host chooses runtime integrations. A short explanation must preserve that choice. Calling the package an automatic agent executor would be clearer-sounding but wrong.

The control contracts also show why blanket word substitution is unsafe. A policy decision can require approval; that is distinct from an authenticated approval for the exact proposed action. A general-purpose rule that treats approval, authorisation and permission as interchangeable would erase behaviour exercised by existing tests.

ADR-003 supplies another material distinction: an evidence reference does not grant permission to disclose its content. The language system needs context and source references, rather than a global list of approved words.

## A marketing reader's route through technical material

For each case, the evaluator should be able to find five things without first reading implementation detail:

1. **Purpose:** what the capability contributes to the product or reader's work.
2. **Decision:** the choice or boundary that governs it.
3. **Implication:** what that choice means for adoption or communication.
4. **Terms:** a short explanation of the unfamiliar concepts needed here.
5. **Detail:** a direct route to the exact contract, decision and relevant tests.

The public fixture tests this route for the package overview, action approval and schema authority. The private project cases apply the same reader route to their own material. A marketing reader need not implement the contracts, but should be able to navigate to them and explain their consequences accurately.

## How to use the cases

Give an agent the case prompt, current skill and referenced source material. Capture the actual output before scoring it. The case's required facts and forbidden claims are evaluation criteria, not additional instructions to include in a blind run.

Assess consistency, accessibility, readability and repeatability separately. Check the retained technical facts before judging shorter prose as an improvement. Repeat representative cases with fresh context, retaining the prompt, source revision, skill revision, agent/runtime and observed output. A fixture validator establishes that the case is well formed; it does not establish the quality of an answer that has not been generated.

## Adoption recommendation

Start with the public `llm-core` package overview as the documentation pilot. It has explicit authority boundaries, readable product purpose and precise contracts, so semantic drift can be checked concretely. Use the private projects for further evaluation without publishing their implementation details. Resolve conflicting local guidance explicitly when proposing adoption; a shared style policy must not silently overwrite a project's accepted meaning.

## Forward-test results

Fresh workers received the skill, raw source artefacts and a bounded authoring request. They did not receive the fixture's required facts, forbidden claims or expected reader route. Their initial artefacts were preserved before revision. Private source and output details remain outside this public repository.

| Trial | Initial result | Revision or fresh retest |
| --- | --- | --- |
| Public terminology discovery | Retained the main adoption/action-control distinctions, but invented an unsupported lifecycle status for all 13 records. The actual checker rejected the registry despite the author's narrower self-checks. | The author separated observations from adoption status and passed the real checker. A fresh run with the clarified skill produced a 12-concept registry that also passed. |
| Private content authoring | Two independent authors missed terminology stored in a hidden planning directory. Their reported source inventory was incomplete. | Both corrected their inventories. A fresh run with the amended skill found the hidden reference without the earlier diagnostic prompt. |
| Independent repetition of an explanation | Main calculation boundaries survived, but the authors varied in which important related terms they explained. | Corrected fresh output retained the principal distinctions and explicit routes to the documented contract. Wording, scope and concept selection still varied. |
| Blind navigation review | A separate agent read completed artefacts only and located their purpose, main decision and practical consequence. | It identified unexplained specialist terms and weaker source navigation in the public domain explanation. The private explanation offered a clearer first click, but still assumed some domain knowledge. |

The initial failures led to two concrete skill changes: inspect tracked and hidden authority paths, and use the registry's declared lifecycle values while keeping observed meanings separate from adoption. The tests also exposed a provenance trap: the repository's baseline commit did not identify uncommitted skill content, so tested skill files need their own content hashes.

### Assessment against the four outcomes

| Outcome | Assessment | Evidence and limit |
| --- | --- | --- |
| Consistency | Promising, with specific corrections | Core source distinctions survived authoring. A registry that parses is still insufficient: the initial unsupported status and variation in concept naming required separate review. |
| Accessibility | Partial | The blind reader found purpose, decision and implications. It still had to guess specialist terms, and inline code paths were less navigable than descriptive clickable links. |
| Readability | Partial | Explanations led with product purpose and retained constraints, but some implementation vocabulary and detail remained dense for a reader outside engineering. |
| Repeatability | Partial | Independent runs retained the main boundaries; they did not consistently select the same concepts or explain all related terms. The sample is too small to establish reliability. |

The public artefacts retained the kernel/execution boundary, policy/approval distinction and exact-action controls. The initial discovery also explained schema authority and disclosure limits; the fresh bounded run selected a narrower concept set, so full schema-case repeatability was not established. Private trials assessed explanation and access-decision cases; lifecycle-specific and live-progress-copy prompts remain unrun.

Next evaluation should focus on first-use definitions, meaningful links, and a fresh reader locating the relevant contract without prior repository knowledge. Give future discovery runs an adopted registry when checking continuity: independently inventing IDs from an empty baseline is not a test of preserving existing IDs. Neither these trials nor source tests prove a live dashboard, native-host support or successful human comprehension.

## Revised public pilot

The [llm-core explanation](../../evaluations/pilots/llm-core/llm-core-domain.md) now explains HMAC, fenced ownership, host interfaces and conformance where they first matter. Its technical evidence links point to the inspected immutable public revision. The accompanying [source-derived terminology registry](../../evaluations/pilots/llm-core/llm-core-terminology.json) keeps every formulation proposed and adds pinned source links.

These are evaluation-coordinator revisions addressing the reader's findings. The proposed registry passes the actual repository checker, and the evidence-link paths were checked against the inspected Git revision. The revised explanation has not received a new blind-reader or human comprehension test. Its publication does not convert the earlier partial outcomes into a pass.
