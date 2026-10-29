# Match technical documentation to the reader's purpose

Use Diátaxis's four reader needs to choose the main purpose. A request may need linked pages with different purposes; it does not automatically need four documents.

| Reader need | Form | Keep in focus |
| --- | --- | --- |
| Learn by doing | Tutorial | Supported activities and observable learning outcomes |
| Complete a task | How-to guide | Goal, requirements, actions and verification |
| Look up a contract | Reference | Exact inputs, outputs, states, constraints and examples |
| Understand a concept | Explanation | Purpose, relationships, reasoning and trade-offs |

For tutorials, provide a workable starting point and explain what the learner should observe. For how-to guides, respect established expertise and describe recovery where it affects success. For reference, preserve exact identifiers, units, defaults and failure behaviour. For explanations, connect mechanisms to their reasons rather than reproducing a type inventory.

## Give technical and business readers a route

Start a substantial document with the problem, main behaviour or decision, and practical consequence. Introduce required specialist terms near first use; link to their accepted definitions. Use descriptive headings and clickable links into exact contracts, decisions and examples.

Keep meaningful constraints visible in the main explanation. Put detailed signatures and protocol mechanics in labelled sections. Avoid hiding essential distinctions behind jargon, acronym lists or a diagram alone. Use semantic headings, table headers and text alternatives for essential visuals.

An explanation of signed approvals might describe a signature as a check that the approval came from an authorised source and was not changed, then link to the exact cryptographic contract. Do not call signing encryption or imply that a valid identity automatically grants permission.

## Choose useful architecture views

For an architecture explanation, use [arc42's overview](https://arc42.org/overview/) as a coverage prompt. Show the relevant system context and boundaries, runtime interactions, deployment responsibilities, quality concerns and terminology. Choose only views that answer the reader's question; this is a documentation check, not permission to change the architecture or require twelve sections.

## Validate the content

Check claims against the selected revision. Run a documented procedure where available and authorised, recording its actual result. Treat source inspection, executed checks and planned verification distinctly. Link a pending check to the next action without declaring the design invalid merely because it has not yet been exercised.

Ask an outside-specialism reader to find the purpose, main point, consequence and technical detail. Keep their observed difficulties separate from automated spelling and style findings.

## Sources and local adaptation

[Diátaxis](https://diataxis.fr/start-here/) supplies the four reader purposes. The downloaded [Good Docs concept and how-to templates](https://gitlab.com/tgdp/templates) inform explanation and procedure structure. The [arc42 overview](https://arc42.org/overview/) offers architecture views for checking coverage; select views that serve the reader rather than imposing the full template. These sources guide document structure, not the system's architectural rules.
