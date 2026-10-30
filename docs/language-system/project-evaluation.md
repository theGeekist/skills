# Project evaluation

The public pilot evaluates terminology discovery and cross-audience explanation against [`theGeekist/llm-core`](https://github.com/theGeekist/llm-core) at revision `4f9e37ac92bcd055a836806ea463510ed32a8bcc`. Source inspection and agent writing/navigation trials were completed on 29 October 2026. The results below concern those cases, rather than project runtime qualification or human comprehension.

## Source contracts and reader meaning

The inspected repository distinguishes package-owned engineering authority from a shared documentation site. The pilot follows the package README and current decisions instead of treating all Markdown as equally current.

Its contracts supply several distinctions that a readable summary must retain:

- The package supplies portable contracts, conformance, authority and evidence; a host selects runtime integrations.
- A policy decision that requires approval differs from authenticated approval for an exact proposed action.
- An evidence reference does not grant permission to disclose the referenced content.
- Schema authority and user-facing explanations have different responsibilities.

Replacing these concepts with a global list of simpler synonyms would change behaviour. The [public cases](../../evaluations/projects/llm-core.json) make retained facts and unsupported claims explicit.

## Recorded results

| Trial | Observation | Implemented correction or recorded scope |
| --- | --- | --- |
| Terminology discovery | The initial output retained important boundaries but assigned an unsupported lifecycle status to thirteen records | Discovery guidance names the registry's allowed statuses. A corrected output and a fresh twelve-concept run passed the actual checker |
| Authority-source discovery | An incomplete source inventory missed terminology in hidden project planning paths | Discovery guidance explicitly includes tracked and declared hidden authority paths |
| Repeated explanations | Main boundaries survived, but concept selection and first-use explanations varied | Revised guidance and examples retain governing meanings and provide direct contract links |
| Navigation assessment | A separate agent found purpose, decision and implications, while identifying unexplained terms and weak source routes | The public pilot explains necessary terms near first use and links to the pinned contracts |

The [revised explanation](../../evaluations/pilots/llm-core/llm-core-domain.md) introduces HMAC, fenced ownership, host interfaces and conformance where they matter. The accompanying [terminology registry](../../evaluations/pilots/llm-core/llm-core-terminology.json) records its source-derived formulations as proposals with pinned sources. Its records pass the repository checker.

The revised explanation has not received a new human comprehension study. Its publication does not turn earlier partial navigation results into a measured pass.

## Assessment

| Outcome | Evidence from the pilot |
| --- | --- |
| Consistency | The principal contract distinctions survive; registry structure and retained meaning require separate checks |
| Accessibility | Agent navigation finds purpose, decision and implications; specialist definitions and source routes affect entry into detail |
| Readability | Explanations lead with purpose while retaining technical constraints; the small sample does not establish a general reading level |
| Repeatability | Independent runs retain the main boundaries but vary in wording and concept selection |

The pilot tests whether an explanation gives readers a route from purpose to decision, consequence, necessary terms and exact contract. It does not test a live dashboard, native client activation or production integration. Non-public project cases are excluded from the reproducible public result.

## Reproduce the evaluation

Give an agent a case prompt, the selected skill and the pinned public sources. Retain the initial output before assessment. Keep required facts and forbidden claims separate from a blind authoring prompt.

Compare retained meaning, source accuracy and navigation before judging brevity. Record the prompt, source revision, skill revision or content hashes, output and assessment. Reusing an existing adopted registry tests continuity; creating new IDs from an empty baseline tests discovery instead.
