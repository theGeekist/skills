# Editorial review

Reviewed `draft.md` against `source.md` using the local review-project-language skill, including its review criteria, uncertainty guidance and editorial patterns. Three material findings require correction.

| Location | Observed wording | Pattern | Effect | Smallest useful correction and governing facts |
| --- | --- | --- | --- | --- |
| `draft.md`, paragraph 1, sentence 1 | “fully accepted for processing” | E001: Changed project meaning | Converts checksum verification into an operations approval that has not occurred. | Say that the file is verified because its checksum matches, and that acceptance for processing awaits the operations manager's decision. `source.md` defines verified and accepted separately; the manager has not decided. |
| `draft.md`, paragraph 1, sentence 2 | “proven processing engine will halve completion time” | E003: Invented result | Asserts proof and a quantified time saving without supporting measurements. | Remove both claims. State that throughput has not been measured and require a representative load check before making throughput claims. The source supplies no completion-time result. |
| `draft.md`, paragraph 1, sentence 3 | “Throughput is unproven, so all local prototype work must stop.” | E004: Evidence gap becomes a blanket stop; E002: Lost condition | Treats missing measurements as a withdrawal of permission and omits the actual boundary on production publication. | Preserve authorisation for the reversible local prototype. Name the representative load check as the next evidence-gathering action and retain the absence of permission to publish a production release. |

The revision in `draft-revised.md` retains the short update format. It restores the verification/acceptance distinction, removes unsupported performance claims, and separates authorised local work from production publication. A representative load check should produce throughput measurements under representative conditions before any throughput claim is made; no outcome is presumed.

Checked the revised text against every source fact: matching checksum; no manager decision; reversible local prototype authorised; throughput unmeasured; representative load check required before throughput claims; no permission to publish a production release. No approval gate has been added to the authorised local prototype work. No prototype, load check or publication was performed as part of this editorial task.
