# Portable skills, specific activation evidence

Reviewed 29 October 2026. Purpose-specific skills with short metadata and conditional references follow the portable Agent Skills model. The package can be shared; reliable selection and resource loading must also be checked in the client that runs it.

## What travels across agents

The [Agent Skills specification](https://agentskills.io/specification) defines a directory with `SKILL.md`, required name/description and optional supporting files. The whole main file loads after activation; referenced material is intended for use as needed. Keeping references inside the skill and linking directly to them supports independent installation. The specification recommends a main file below 500 lines and 5,000 tokens. Those are authoring guidelines rather than proof that a task will select or follow the skill.

Use the common format in the core. Keep client-specific UI metadata, invocation controls, hooks and installation configuration separate. A policy in `agents/openai.yaml` is not a universal control for Claude or Gemini. Instruction-only authoring skills avoid unnecessary runtime dependencies.

## Four questions need different tests

| Question | Suitable evidence | What it does not establish |
| --- | --- | --- |
| Is the package well formed? | Portable validator, file/link checks, isolated installation copy | The host discovers it or selects it |
| Does the description distinguish the purpose? | Ordinary-request catalogue tests, distractors and no-skill cases | Native runtime activation |
| Does the selected skill load useful detail? | Observed file reads or resource requests, output and context-size record | Every client loads the same files |
| Does the host actually select and execute it? | Installed client version/mode, trace of activation and completed task | Universal support across CLI, desktop and cloud |

A fresh agent choosing from a supplied metadata catalogue is useful selection evidence. It is not a native loader test. An explicitly named skill tests execution after selection. Keep those result types separate in reports.

## Documented installation routes

The following routes were reviewed on 29 October 2026. Refer to the linked client documentation when selecting a supported surface.

| Host surface | Route | Integration boundary |
| --- | --- | --- |
| Codex CLI / IDE | Local `.agents/skills`, explicit mention or description matching; optional OpenAI metadata | Native discovery and implicit activation depend on the installed client |
| ChatGPT desktop / Work / web / mobile | Supported standalone-skill or plugin distribution | Repository publication is separate from account installation; availability varies by surface |
| Claude Code CLI | `.claude/skills` or a plugin; relevance-based or explicit invocation | Claude-specific extensions are separate from the portable core |
| Claude desktop / Cowork / cloud | Supported account skill or plugin installation | A local skill directory alone does not install an account plugin |
| Copilot CLI | Project `.github/skills`, `.claude/skills` or `.agents/skills`; personal `.copilot/skills` or `.agents/skills` | Skill listing, selection and resource loading are client behaviours |
| Copilot app / VS Code / cloud | Skill and instruction features supported by the selected product | Deployment settings and execution modes remain surface-specific |
| Gemini CLI | `.gemini/skills` or `.agents/skills`; metadata matching followed by activation | Client invocation controls are separate from package structure |
| Antigravity desktop / CLI | Destinations supplied by the local repository linker | A linked path is not native activation evidence |

Primary references: [OpenAI skill authoring](https://learn.chatgpt.com/docs/build-skills), [Claude Code skills](https://code.claude.com/docs/en/skills), [Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills), [Copilot surfaces](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills), [Gemini CLI](https://geminicli.com/docs/cli/skills/). Retrieval details are in [the source manifest](portability-sources.json).

## Keep growing catalogues useful

OpenAI's documentation says the initial list can shorten descriptions and, at sufficient scale, omit entries. It recommends front-loading the task and trigger words. Its main instructions still load in full on selection. Claude Code likewise describes a listing budget that may drop descriptions; it also supports platform-specific extensions beyond the portable format. Prefer a concise common description with distinctive purpose, and put host-specific controls in adapters. Do not raise context budgets as a substitute for removing overlap.

More skills trade a larger metadata catalogue for smaller activated bodies. Measure both. Avoid an umbrella skill that repeats specialist workflows or requires a second activation for every ordinary task. A marketing agent is a role, not a different file format: its request should match marketing-specific terms without requiring architecture vocabulary. Test competitor descriptions and unrelated requests so improved recall does not become excessive activation.

## Offline selection analysis

[Google's skill-reach](https://github.com/google/skill-reach) is a relevant existing Apache-2.0 evaluation tool. Its README describes offline frontmatter linting and lexical overlap analysis, plus empirical probes through supported agent runtimes. The tool was installed and its offline lint/overlap commands were executed against the final 11-skill catalogue, using the local keyword driver. Strict lint returned success with no warnings or errors and four informational handoff suggestions. A lexical score is a collision signal rather than native activation evidence.

### Executed offline checks

The isolated checkout is pinned to `d86d81fa35c0705a4d92a1fa2a0b08d48ce044ff`, package version `0.1.0`, with its Apache-2.0 licence and lockfile inspected. Installation used Python 3.12 and `uv sync --frozen --no-dev`; this also installed the checkout's default documentation group. No global agent configuration changed.

Reproduce from that checkout after pointing `CATALOGUE` at an isolated copy of the skills directory:

```sh
.venv/bin/reach lint --strict "$CATALOGUE" --agent keyword --format json
.venv/bin/reach overlap "$CATALOGUE" --all --no-truncate --agent keyword --format json
```

Both commands returned exit code `0`. The lint suggestions identify backend/frontend and decision/task vocabulary overlap. They are informational: preserve the explicit task boundaries and exercise ambiguous requests rather than add mandatory sibling dependencies to independently installable skills.

The nearest lexical pairs are backend/frontend (rival ratios 0.52/0.56), marketing/interface (0.44/0.44) and decisions/tasks (0.36/0.30). No skill was outranked by another for its own vocabulary in this analysis. These figures help choose collision cases; they are not precision, recall or native-trigger success rates.

[Raw results and source hashes](../../evaluations/portability/offline-manifest.json) identify the exact skill files analysed. The first snapshot is retained separately under `evaluations/portability/initial/`; the final run follows the task-description boundary refinement. This offline analysis made no model calls or native client probes. Native activation is outside the recorded result.

## Evidence boundary

Published checks cover portable packaging, metadata selection and observed staged resource access. They do not establish native activation across the listed clients. The [selection evaluation](selection-evaluation.md) identifies the exact cases, prompts and observed results.

The [original research](research-baseline.md) is retained separately. Tool licences apply to their own code and resources; adopting a shared file layout does not transfer a vendor's runtime features into other agents.
