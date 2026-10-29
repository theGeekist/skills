# Forward tests: work with uncertainty

Three fresh-context workers used `advance-with-uncertainty` on two invented scenarios. One scenario was repeated independently. All three outputs preserve the useful work that can proceed, scope the remaining evidence gaps, and avoid claiming results that have not occurred. The publication scenario also preserves the explicit authority boundary.

These are agent-reviewed examples, not measured human-comprehension results or runtime tests. There was no pre-change control run, so they support the skill's behaviour on these cases rather than a quantified improvement or general success rate.

## Method and records

Each worker received the skill path, one raw input, an output path and the request to revise the task or ADR and recommend the next execution step. They were instructed not to implement or perform external actions. Workers had fresh conversation context and received no expected answer or assessment rubric. They could read the normal repository instructions and the skill's references and examples; this evaluates that package in its repository context, not the skill body in isolation.

The exact prompts, invented inputs, complete outputs and source-file hashes are retained under [evaluations/uncertainty](../../evaluations/uncertainty/manifest.json). Inputs contain no private project material. Workers wrote only their respective proposed revisions. No local prototype, parser tests, packaging operation, model evaluation or publication was performed in this exercise.

| Case | Input | Raw output | Purpose |
| --- | --- | --- | --- |
| Local adapter task | [Task](../../evaluations/uncertainty/adapter-task.md), [prompt](../../evaluations/uncertainty/adapter-prompt.txt) | [First output](../../evaluations/uncertainty/adapter-output.md) | Test a blanket rejection based on missing desktop evidence when reversible local work is authorised |
| Publishing decision | [ADR](../../evaluations/uncertainty/publishing-adr.md), [prompt](../../evaluations/uncertainty/publishing-prompt.txt) | [Output](../../evaluations/uncertainty/publishing-output.md) | Test missing model evidence alongside an actual irreversible-publication permission boundary |
| Local adapter repeat | Same task, [fresh prompt](../../evaluations/uncertainty/adapter-repeat-prompt.txt) | [Repeated output](../../evaluations/uncertainty/adapter-repeat-output.md) | Check whether the first outcome depends on one wording choice or worker thread |

## Observed behaviour

| Criterion | Adapter first run | Publication run | Adapter repeat |
| --- | --- | --- | --- |
| Separate implementation from evidence | States that no implementation or tests exist and desktop behaviour is untested | Distinguishes a written package and passing parser fixtures from packaging and named-model evaluation | Separates unimplemented adapter, chosen fixtures and untested desktop contract |
| Give a concrete authorised next action | Prepare synthetic contract fixtures, implement the small script, run harness cases | Run local parser tests, package candidate, prepare notes and evaluation instructions | Prepare fixture contract and three harness cases, then implement and run |
| Preserve actual blockers | Missing client limits desktop checks; publishing/account changes/rollout stay outside scope | Missing credential blocks named-model execution; lack of authorisation blocks irreversible publication | Missing client limits desktop validation, while local implementation continues |
| Define observable completion | Input, expected result, stdout, stderr and exit status; one continuation and repeat guard | Identified artefact, local results, draft notes and reproducible model-evaluation instructions | Clean case, mismatch case and both guard states; records exact tested contract |
| Avoid fabricated proof or authority | No compatibility or implementation claim; synthetic inputs are labelled | Does not label package unsafe or model-validated; never grants publication permission | Does not present assumed schema as observed desktop data |
| Preserve precise negative findings | Retains unverified desktop behaviour and unavailable client | Retains missing credential, absent model evaluation and prohibited publication | Retains untested desktop behaviour and possible missing schema inputs |
| Support a useful handoff | Gives the next implementation task and independent preparation | Gives local release-preparation steps and exact stop before publication | Gives executable local sequence and isolates any unavailable assertion |

### Adapter task

The first worker changed the task from “Disqualified” to ready for authorised local prototyping. It did not mistake local harness success for integration evidence. It also noticed an underspecified acceptance input: the task refers to an agreed terminology mismatch without supplying the actual pair. The output lets parsing and guard preparation continue while obtaining that input.

The repeat independently reached the same practical decision. It added a useful distinction: testing only the suppressed-continuation case would also pass an adapter that never requests continuation. Checking both indicator states makes the guard test meaningful. This is a stronger concrete acceptance example, not merely more positive wording.

Both outputs reserve desktop checks for a later authorised experiment. The scenario already authorises local tests but supplies no client, so this phrasing is slightly more cautious than necessary if a future reversible desktop check falls within the existing authorisation. Neither output stops the current work or asks the user to reauthorise it. A wider test set should check that the skill does not invent new permission gates for routine authorised validation.

### Publishing decision

The worker rejected both unsupported abandonment and unauthorised publication. It chose a locally prepared candidate, with named-model evidence still pending. It explicitly states that a passed model evaluation would not itself authorise publication. The missing credential and missing publication permission affect different actions and are recorded separately.

The proposed next task remains concrete: run available local tests, package the candidate if those checks pass, and prepare the remaining review materials. Independent documentation can continue after a local failure while the failure is investigated. The output preserves the initial publication's irreversible nature without generalising it into a stop on the entire programme.

## Assessment and next tests

These cases provide preliminary evidence for the intended distinction: incomplete evidence calls for scoped investigation; an actual authority boundary constrains the specific action. They also show repeatable local-task structure without requiring identical wording or banning words such as “untested” and “unverified”.

The outputs are substantial: 695, 903 and 799 words respectively. They give thorough handoffs, but future tests should request a compact task or ADR and check whether the package retains the same distinctions in fewer words. More detail is not itself evidence of accessibility.

Before claiming broader effectiveness, add cases for a demonstrated failed experiment, conflicting evidence, a mandatory external review, an explicit user stop, and work that genuinely cannot proceed without a missing input. Include a paired pre-change comparison and human review by both engineering and non-engineering readers. Runtime execution and natural skill activation require separate checks.

## Post-refinement compact run

After the initial runs, the skill and reference were refined to carry forward existing authorisation explicitly and to permit a few sentences instead of mandatory uncertainty sections. A fourth fresh-context worker received the same raw adapter input with an explicit limit of 150 words. The [exact prompt](../../evaluations/uncertainty/adapter-compact-prompt.txt), [raw output](../../evaluations/uncertainty/adapter-compact-output.md) and [separate snapshot/hash manifest](../../evaluations/uncertainty/compact-manifest.json) preserve this later run without changing the original records.

The output contains **144 words**, including the title and status. It states that implementation does not yet exist, names the authorised prototype, gives parser/mismatch/repeat-guard cases, identifies the harness evidence to capture, and limits the resulting claim to supplied payloads. It names the absent desktop client as the exact desktop-validation blocker and keeps publishing, account changes and rollout outside scope. The next step is to define the fixture and expected outputs, then implement and test within existing authorisation.

It introduces no additional permission gate for the future desktop check. It also retains accurate negative statements rather than applying a word ban. This case demonstrates that the important distinctions can fit a compact handoff under the revised package and an explicit length request.

The skill wording and prompt limit both changed, so this is not an isolated causal test of the refinement. The result does not establish naturally concise output when no length is requested, automatic skill activation, human comprehension or actual adapter behaviour. Those remain separate checks.
