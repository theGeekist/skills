# External skill source evaluation

This review covers each repository and reference raised in the product-narrative discussion. The 26 selected skills are compiled as separate packages. Their upstream `SKILL.md` files and selected supporting files are copied verbatim. Geekist adds catalogue/interface metadata, the original licence notice, attribution records and local interface icons.

## Evaluation scope

The review considered each source's stated job, fit for product communication or developer adoption, overlap with Geekist's current skills, supporting files and licence. This is a source and package-structure evaluation. The imported skills have not been benchmarked by generating and judging outputs against Geekist repositories. A claim in an upstream README remains that author's claim.

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
| [`coreyhaines31/marketingskills`](https://github.com/coreyhaines31/marketingskills/tree/2bf95edb4ebd37198ab7fd18b99ba95c2145ec64) | `copywriting`, `product-marketing` | Useful pair for direct web copy and a durable product-marketing context. The user-mentioned “Copywriting Skill” was interpreted as this repository's `copywriting` skill; the rest of the repository was not bulk-imported. |
| [`Gingiris-1031/gingiris-skills`](https://github.com/Gingiris-1031/gingiris-skills/tree/d22f7ae693568981b4a254b9469256c4b9e0e1b9) | `developer-marketing-playbook`, `gingiris-github-star-growth` | Adds developer relations, documentation, community and distribution playbooks. The two skills serve different scopes. Their source claims and promotional language remain unedited. |
| [`Infrasity-Labs/dev-gtm-claude-skills`](https://github.com/Infrasity-Labs/dev-gtm-claude-skills/tree/a9fe6aa9de4c86a64d9d2a216b42bdba74c2aa30) | `product-strategist` | Broader than README craft: product strategy, OKRs and competitive work can establish useful context before narrative writing. Included as an adjacent capability rather than a copywriting specialist. |
| [`alex-kashkarov/skills`](https://github.com/alex-kashkarov/skills/tree/c83409df59e0382201bd75940e850e537594b15d) | `landing-page-architect` | Focuses on landing-page structure, offer clarity and proof. Not a README tool, but a complementary product-narrative surface. |

## Not copied

| Candidate | Decision |
|---|---|
| [Flagrare Agent Skills](https://github.com/Flagrare/agent-skills) | Not copied because no repository licence was present at review time. The source remains linked for future reassessment. |
| [Charm's open-source marketing philosophy](https://charm.land/blog/100k/) | A useful reference on product demonstrations, personality and portfolio identity, but an article rather than an installable skill. No article text is reproduced. |
| [Gingiris Open Source mirror](https://github.com/Gingiris-1031/gingiris-open-source) | The mirror is archived. The current `gingiris-skills` repository was used for the two relevant playbooks instead. |
| “Copywriting Skill” | Interpreted as Corey Haines's `copywriting` skill in `marketingskills`; included under that name. |

## Why these remain separate

The sources address different jobs: positioning establishes what a product means in its market; storytelling shapes how that meaning is remembered; README and launch skills turn it into a developer-facing experience; developer-marketing playbooks address adoption paths; editing skills improve prose. There is real overlap in README writing, copywriting, messaging and humanisation. Keeping the original skills independent preserves their methods and gives us options to compare later. No skill is a mandatory prerequisite for another.

The catalogue also widens five Geekist writing triggers so ordinary requests can reach general writing, product communication, technical explanation, implementation-task writing and prose review without the user naming a skill or matching a narrow phrase.

## Licence handling

All 14 selected source repositories were checked for an MIT licence before their files were copied. Every imported package has the full original notice in `LICENSE.upstream`, preserving the upstream copyright holder and permission terms. Geekist's root licence applies to Geekist-authored material and does not replace upstream notices.

## Limitations and next evaluation

This is not a quality benchmark. The skills have not been tested against PulseGraph or another Geekist repository, and their generated README or product narratives have not been compared with current Geekist writing. Several packages contain scripts or external workflow instructions. Those files were copied but not executed.

A useful comparison would give a few relevant skills the same verified product facts, repository context and target reader. Review the outputs for positioning accuracy, intrigue, specificity, visual demonstration and technical trust. Keep all skills individually available regardless of the results.
