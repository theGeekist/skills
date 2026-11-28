# External skill source evaluation

This review covers each repository and reference raised in the product-narrative discussion. The 26 selected skills are compiled as separate packages. Their upstream `SKILL.md` files and selected supporting files are copied verbatim. Geekist adds catalogue/interface metadata, the original licence notice, attribution records and local interface icons.

## Evaluation scope

The review considered each source's stated job, fit for product communication or developer adoption, overlap with Geekist's current skills, supporting files and licence. This evaluation covers source selection and package structure. Output quality remains unevaluated against Geekist repositories; statements in upstream READMEs remain claims by their authors.

Each source link is pinned to the commit included in this collection. Every copied package has a `references/GEEKIST-UPSTREAM.md` file linking its exact source path and commit, plus the source repository's full MIT `LICENSE.upstream`.

## Included sources

| Source repository | Skills included | Assessment |
|---|---|---|
| [`motiful/readme-craft`](https://github.com/motiful/readme-craft/tree/7bcde93a01b4834eb5974fa457a0c241064c4429) | `readme-craft` | The closest direct fit for README craft. Combines positioning and a three-tier reading experience with GitHub formatting, comparison visuals and logo guidance. Kept as a distinct README specialist. |
| [`MJorgin/github-launch-studio`](https://github.com/MJorgin/github-launch-studio/tree/a7d590818e2819bc83b8707f78cd0516b5b11654) | `github-launch-studio` | Extends beyond README writing into launch positioning, demo assets, release notes and announcements. Useful when the repository needs a coordinated launch package; overlaps with README Craft at the README layer. |
| [`marketingskills/open-source-growth`](https://github.com/marketingskills/open-source-growth/tree/bed1df081f9dd6908581fa4c68ff99b3762f3be3) | `repo-growth-operator`, `ecosystem-inclusion-operator` | Strong developer-adoption fit: repository audit and discoverability on one side, relevant ecosystem contributions on the other. Its scripts include network and GitHub operations; copied as source and not executed. |
| [`adam-lagerhausen/b2b-marketing-skills`](https://github.com/adam-lagerhausen/b2b-marketing-skills/tree/cce10438ff2d011cb7ed1ac99023a862503f6e15) | `positioning-messaging-framework`, `voice-of-customer-synthesis` | Strong fit for complex technical products. Separates strategic positioning from synthesis of customer language and proof, which makes both useful without requiring the same workflow. |
| [`realjaymes/marketingagentskills`](https://github.com/realjaymes/marketingagentskills/tree/cf3c48f1092caa66ca7391308c2e760216302f77) | `portfolio-positioning`, `storytelling-framework` | Directly addresses portfolio architecture and product narrative across a family of products. Particularly relevant to how Geekist presents multiple independent tools. |
| [`wondelai/skills`](https://github.com/wondelai/skills/tree/c37678106e63ef1c5472d848fb3d8b8c5b33fafe) | `obviously-awesome`, `made-to-stick` | Adds two distinct lenses: market positioning and message memorability. Useful intellectual foundations; outputs still need evaluation against real product facts and audience. |
| [`msimchowitz/writing-skills`](https://github.com/msimchowitz/writing-skills/tree/214981fe02326f27b0fc8790d00eb4b731607073) | `general-writing`, `non-autoregressive-writing-pass`, `writing-cadence`, `better-usage`, `academic-voice`, `humanizer` | The most editorially differentiated source. Includes a whole-draft revision pass and focused diagnostics for cadence, semantic fit and register. Overlaps with Geekist's reviewer and writer, so preserved as alternatives for later comparison. |
| [`hridoy43/agent-skills`](https://github.com/hridoy43/agent-skills/tree/966b696aaa1873421f9f0b901e03f647906c48d0) | `conversion-storytelling`, `github-readme-and-profile-writing` | Pairs product-story structure with GitHub-specific README and profile work. README overlaps with Readme Craft and GitHub Launch Studio; keeping all three allows independent use of each source's method. |
| [`blisse-code/bespoke`](https://github.com/blisse-code/bespoke/tree/92edcd70b121d13d52fbf6ed2cc1b813205e86ed) | `bespoke` | A distinct voice-profiling and content-refinement approach. Relevant when the README or launch writing should sound like a particular author rather than generic product copy. |
| [`phuryn/work-humanizer`](https://github.com/phuryn/work-humanizer/tree/0a9065791d021f3dda695f3887cb2ae4c0eacbcf) | `work-humanizer` | Workplace-specific rewrite and interview modes, with attention to facts and commitments. Adjacent to the general humanizer; useful as a separate, narrower option. |
| [`coreyhaines31/marketingskills`](https://github.com/coreyhaines31/marketingskills/tree/2bf95edb4ebd37198ab7fd18b99ba95c2145ec64) | `copywriting`, `product-marketing` | Useful pair for direct web copy and a durable product-marketing context. Both skills remain in the collection alongside separately authored alternatives. |
| [`Gingiris-1031/gingiris-skills`](https://github.com/Gingiris-1031/gingiris-skills/tree/d22f7ae693568981b4a254b9469256c4b9e0e1b9) | `developer-marketing-playbook`, `gingiris-github-star-growth` | Adds developer relations, documentation, community and distribution playbooks. The two skills serve different scopes. Their source claims and promotional language remain unedited. |
| [`Infrasity-Labs/dev-gtm-claude-skills`](https://github.com/Infrasity-Labs/dev-gtm-claude-skills/tree/a9fe6aa9de4c86a64d9d2a216b42bdba74c2aa30) | `product-strategist` | Broader than README craft: product strategy, OKRs and competitive work can establish useful context before narrative writing. Included as an adjacent capability rather than a copywriting specialist. |
| [`alex-kashkarov/skills`](https://github.com/alex-kashkarov/skills/tree/c83409df59e0382201bd75940e850e537594b15d) | `landing-page-architect` | Focuses on landing-page structure, offer clarity and proof. Not a README tool, but a complementary product-narrative surface. |

## Other candidate evaluations

| Candidate | Decision |
|---|---|
| [Flagrare Agent Skills](https://github.com/Flagrare/agent-skills) | The repository had no published reuse licence at review time. Keep the source link for future reassessment. |
| [Charm's open-source marketing philosophy](https://charm.land/blog/100k/) | A useful reference on product demonstrations, personality and portfolio identity. It is an article, so the collection treats it as context rather than an installable skill. |
| [Gingiris Open Source mirror](https://github.com/Gingiris-1031/gingiris-open-source) | The mirror is archived. The current `gingiris-skills` repository supplies the two relevant playbooks. |
| [Prajeevan/copywriting-skill](https://github.com/Prajeevan/copywriting-skill/tree/fcce41e3a3617beca31e7a534c9db13502e2d97d) | Relevant and self-contained, with a distinct direct-response emphasis based on Sam Parr and Joseph Sugarman. The repository includes an MIT licence, a 38 KB `SKILL.md`, and no supporting files or runtime dependencies. Its own README attributes substantial material to interviews and *The Adweek Copywriting Handbook*, and the skill includes numerous attributed formulations from those sources. Separate evidence of reuse rights for those third-party passages would support a future review. The existing Corey Haines `copywriting` and `product-marketing` skills remain included. |

## Why these remain separate

The sources address different jobs: positioning establishes what a product means in its market; storytelling shapes how that meaning is remembered; README and launch skills turn it into a developer-facing experience; developer-marketing playbooks address adoption paths; editing skills improve prose. There is real overlap in README writing, copywriting, messaging and humanisation. Each skill remains independently selectable, and projects can combine them when useful.

The catalogue also widens five Geekist writing triggers so ordinary requests can reach general writing, product communication, technical explanation, implementation-task writing and prose review without the user naming a skill or matching a narrow phrase.

## Licence handling

All 14 selected source repositories were checked for an MIT licence before their files were copied. Every imported package has the full original notice in `LICENSE.upstream`, preserving the upstream copyright holder and permission terms. Each upstream notice continues to apply to its source material alongside Geekist's root licence for Geekist-authored work.

## Limitations and next evaluation

## Compatibility and runtime notes

The pinned Agent Skills validator reports five exact upstream notices. Each is recorded in [`upstream-compatibility.json`](../../standards/upstream-compatibility.json), including its effect and available resolution. CI accepts only those exact messages and checks that every recorded notice still occurs. A different message or a new failure blocks the check.

| Skill | Validator result | Practical effect |
|---|---|---|
| `bespoke` | Its 1,082-character description exceeds the 1,024-character limit. | Strict validators can reject its metadata before installation or discovery. |
| `developer-marketing-playbook` | Frontmatter includes `source` and `tags`, fields outside the validator schema. | Strict validators can reject the package before loading its instructions. |
| `gingiris-github-star-growth` | Frontmatter includes `when_to_use`, a field outside the validator schema. | Strict validators can reject the package before loading its instructions. |
| `portfolio-positioning` | Frontmatter includes `argument-hint` and `version`, fields outside the validator schema. | Strict validators can reject the package before loading its instructions. |
| `storytelling-framework` | Frontmatter includes `argument-hint` and `version`, fields outside the validator schema. | Strict validators can reject the package before loading its instructions. |

The isolated-package check now covers every bundled Markdown file. [`upstream-compatibility.json`](../../standards/upstream-compatibility.json) records each exact link whose target is a generated README destination, a placeholder, a sibling skill, or a repository-root file. The practical effect and resolution are recorded beside each link. The discovered package resource omissions were Readme Craft's `docs/logo-gallery.md` and its preview SVGs, plus GitHub Launch Studio's `benchmarks/representative-tools.json`; these files are now included from their pinned MIT sources.

| Package | Runtime and external services | Scope |
|---|---|---|
| `readme-craft` | Node.js 18+ and npm install its declared packages. Playwright comparison screenshots also use Chromium. GitHub metadata steps use `gh` and the GitHub API. | Its scripts provide logo and comparison generation; README guidance is in the skill and references. |
| `github-launch-studio` | Python 3 runs its scripts. Benchmark refreshes use the public GitHub API and can use `GITHUB_TOKEN` for a higher rate limit. Social-card and demo rendering use Pillow; demo video rendering also uses `ffmpeg`. | Its audit and writing workflow can be used separately from optional renderers and live benchmark refreshes. |
| `repo-growth-operator`, `ecosystem-inclusion-operator` | Python 3 runs the bundled scripts. Discovery and scoring call the GitHub API; `repo-growth-operator` star actions use authenticated `gh`. | File-based analysis and planning work separately from network lookups and account actions. |
| Other imported packages with helper scripts | The inspected Python helpers use the standard library. | Their listed scripts are optional aids to the written skill workflow. |

Readme Craft's `scripts/setup.sh` installs its npm dependencies. The comparison screenshot helper additionally uses the Playwright Chromium browser. Package installation is required for the bundled scripts; the skill instructions and references carry the README guidance.

Other imported packages include scripts or external workflow steps. Those files remain source-faithful; this review did not execute them. One open-source-growth example references an image path absent from the pinned upstream commit, which is recorded here as an upstream example limitation.

The team plans to assess output quality organically through real project work, using verified product facts and project context as the evaluation basis.

A useful comparison would give a few relevant skills the same verified product facts, repository context and target reader. Review the outputs for positioning accuracy, intrigue, specificity, visual demonstration and technical trust. Keep all skills individually available regardless of the results.
