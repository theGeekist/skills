# Editorial-pattern usage case

This isolated task checks whether the review skill uses the structured pattern reference while retaining source facts and permission boundaries. The input is invented. It is not a native activation or human-comprehension test.

## Task

> Use the review-project-language skill to review draft.md against source.md. Give structured findings with relevant editorial pattern IDs, then revise the draft. Preserve the source facts and the author's actual permissions. Save response.md and draft-revised.md. Read no files outside the case directory and publish nothing.

The executed task also identified its absolute isolated working directory. To replay, copy the current review skill beside these files and verify the staged Markdown hashes in `instruction-hashes.json`.

## Result

The [response](response.md) applies E001 to the changed verification/acceptance meaning, E003 to the invented performance result, and E004/E002 to the blanket stop and omitted publication boundary. The [revision](draft-revised.md) retains the matching checksum, pending manager decision, authorised local prototype, unmeasured throughput and absence of production-publication permission.

No prototype, load test or publication was performed. This is an observed editorial result on the supplied case, not evidence of universal correctness or superiority to another writing skill.
