# Install and check the language system

## Use the skills

Install from the branch or an eventual immutable release using a compatible Agent Skills client. The existing `scripts/link-local.sh --client all --dry-run` shows local destinations without changing them. Review the output before linking a canonical checkout. Installing a skill does not install hooks or persistent instructions.

Each skill includes its required references. The short shared baseline is inline, so a specialist does not need an umbrella skill or a full style-guide read. Authors edit `standards/baseline.md` or task-specific references and maintain their mapping in `standards/skill-profiles.json`, then run:

```sh
python3 scripts/sync-language-references.py
python3 scripts/sync-language-references.py --check
python3 -m unittest discover -s tests -v
```

The core checks require Python 3 and its standard library. Optional external validators are evaluation/development tools, not dependencies loaded by the skills.

Choose the specialist from the [purpose table](../../README.md#choose-a-language-skill). References are conditional: a small label change can use the inline baseline and local state, while a dashboard-state design can load interface patterns. A complete architecture review loads all relevant rule references; a narrow workspace question can load its mapping alone. Full reviews may use more total context, even though initial and narrow-task loads are smaller.

`write-project-content` remains an explicit compatibility router. Its Codex metadata disables implicit invocation; that field does not configure other clients. If installing a subset, use a specialist directly. No specialist requires the router or another specialist to be installed.

## Establish project terminology

Copy `skills/establish-project-language/assets/terminology.example.json` to the project's chosen reference location. Its invented concepts are proposals; replace them with the project's actual meanings and sources. Keep source revisions exact where possible. A working branch can identify an in-progress adoption, but published baselines should use immutable revisions.

```sh
python3 scripts/check-language.py registry /path/to/project/terminology.json
python3 scripts/check-language.py lint \
  --registry /path/to/project/terminology.json \
  --context assessment --audience dashboard /path/to/document.md
```

The registry uses version `1`, contexts and concepts. A concept records its ID, context, preferred term, definition and status. Optional aliases, audience labels, distinct concepts and a replacement support maintenance. Accepted concepts require source paths and revisions. The checker validates record structure and references, but does not fetch sources or prove definitions correct.

The lint command checks explicit aliases in one context. It ignores code and links and protects the preferred term and selected audience label. It reports warnings for review rather than applying substitutions. It does not infer context, grammar, meaning or unknown terms. Exit codes: `0` clean, `1` findings, `2` invalid input/configuration. Output is JSON.

## Keep conversation guidance persistent

Review `adapters/instructions/AGENTS.fragment.md` and merge its small policy into the instruction surface the runtime actually loads. Point at the project's chosen terminology and relevant decisions. Preserve existing instructions and resolve conflicts explicitly.

| Runtime | Integration route | Evidence in this change |
| --- | --- | --- |
| Codex local CLI | Project/global AGENTS.md; optional local Stop adapter | Documentation reviewed; adapter subprocess tested; live loading untested |
| Codex desktop or IDE | Verify instruction and hook loading in the selected execution mode | No live desktop or IDE test |
| ChatGPT Work Cloud | Use supported instructions and skills; local command hooks do not transfer automatically | This work uses skills; no hook registration or cloud instruction-loading test |
| Claude Code | Adapt the same policy to its persistent instructions; use portable skills | Documentation route reviewed; no host test or Claude hook adapter |
| Copilot | Adapt to supported repository or path instructions | Documentation route reviewed; no live loading test |
| Gemini / Antigravity | Existing linker provides skill destinations; verify client behaviour separately | Linker mechanics tested; current client discovery and hooks untested |

Shared Markdown is reusable; loading semantics and hook protocols are runtime-specific. A frontend framework hook and an agent lifecycle hook have different meanings even though both are called hooks.

## Try the optional Codex Stop adapter

The example `adapters/codex/hooks.example.json` uses static absolute paths. Replace every placeholder and review the selected registry/context before manually adding it to a supported local configuration. Do not add it to Work Cloud expecting a local shell command to run.

Smoke-test the adapter directly:

```sh
printf '%s' '{"hook_event_name":"Stop","stop_hook_active":false,"last_assistant_message":"Use path-of-correctness migration."}' |
  python3 adapters/codex/stop-language.py \
    --registry standards/terminology.json --context content
```

This requests a single continuation for a configured alias. The loop guard permits the subsequent turn to finish. Invalid input or configuration returns a generic notice and allows the turn to finish. No transcript is read and no network request is made.

A continuation can arrive after text has been displayed. It is not a clean replacement of streamed content, and this adapter checks vocabulary rather than overall writing quality. The host integration remains experimental until tested in a real client. See [official hook behaviour](https://learn.chatgpt.com/docs/hooks).

## Reproduce optional tool checks

Use the exact source commits and tool versions in [sources.json](sources.json). In an isolated evaluation directory:

```sh
python3 -m venv venv
venv/bin/pip install vale==3.25.1.0
git clone https://github.com/agentskills/agentskills.git
git -C agentskills checkout 69ef37e9424c0a7ea9dd2293b559e43ec8176379
venv/bin/pip install ./agentskills/skills-ref
```

Run `skills-ref validate /path/to/skill` for each skill. The Python Vale wrapper downloads its binary on first use; compare its version with the manifest. From the skills repository, run `vale --output=JSON skills standards docs/language-system/architecture.md` for the selected local rules. No Google or Diataxis package is enabled wholesale.

Set `VALE_BINARY` to the Vale executable when running the test suite to exercise the optional rule integration. The test is reported as skipped when the binary is unavailable. Exact npm versions for the CSpell/textlint experiments and the downloaded template revisions are in the manifest. Recheck false positives and licences before adopting additional rules.

The CI workflow also installs the reference validator from a pinned Agent Skills commit. See [portability](portability.md) for current primary sources and the Google `skill-reach` offline checks. See [selection evaluation](selection-evaluation.md) for ordinary-request catalogue trials and observed resource reads. These are separate from the native-client installation check below.

## Verify installation separately

After installation, ask the selected client to locate one skill reference and use it on a representative project request. Record client version, execution mode, source revision and observed result. Validate CLI, desktop and cloud independently. The tests in this repository do not certify that every compatible client discovers every installation path.
