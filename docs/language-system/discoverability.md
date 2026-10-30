# Find and install the right skill

Start with the [skill selector](../skills/index.md). Each overview explains the purpose, gives an example request and expected result, links the underlying sources and provides a versioned installation command.

## Three ways to find guidance

| Reader need | Route |
| --- | --- |
| Complete a specific task | Choose the matching skill from the [overview pages](../skills/index.md) |
| Understand how the workflows connect | Follow the [worked example](skill-walkthrough.md) |
| Inspect the underlying reasoning | Read the [source map](../../standards/framework-evidence.md) and [alternative-skills comparison](competing-writing-skills.md) |

The overview pages are human-facing documentation. Installable `SKILL.md` files contain the instructions an agent selects, with local references for more detail. Reading the entire collection is unnecessary for a focused task.

## Installation and client discovery

Follow the versioned command on the chosen overview page or the [collection installation instructions](../../README.md#install). Choose the target agent and installation scope when prompted.

The portable Agent Skills format describes how a skill is packaged. Individual clients control discovery, selection and reference loading. The CLI installation route is separate from importing and installing a ChatGPT plugin bundle; publishing a GitHub release does not register a plugin in ChatGPT or establish mobile availability. See [client integration](integration.md) and [release and distribution](../../PUBLISHING.md).

## How presentation stays consistent

[skill-catalogue.json](../../standards/skill-catalogue.json) supplies overview copy, prompts and plugin presentation. Regenerate those files after editing the catalogue:

```sh
python3 scripts/sync-skill-catalogue.py
python3 scripts/sync-skill-catalogue.py --check
```

Activation descriptions remain authored in each `SKILL.md`. The generator checks their agreement with the catalogue rather than rewriting their scope. It also preserves the stable plugin identity and the explicit compatibility-router policy.

Directory mirrors may publish different revisions or variants. Check the linked repository and commit before comparing instructions or relying on a package's description.

## Directory presentation

The root [skills.sh.json](../../skills.sh.json) groups the collection by purpose. Project language covers terminology and review, while project writing covers tasks and decisions alongside technical documentation. Product content has its own route, with architecture and the explicit workflow chooser kept separate.

The configuration is generated from the same catalogue as the overview pages. It changes directory presentation without changing skill instructions or activation scope. The [skills.sh customisation guide](https://skills.sh/docs/customize) describes its supported fields and refresh process; adding a valid file does not establish that a cached listing has refreshed.

Skill activation uses the descriptions in `SKILL.md`. Client presentation uses supported metadata such as `agents/openai.yaml` and plugin manifests. The README gives prospective users a broader explanation with practical examples and visible research attribution. Each surface carries the information relevant to its reader rather than relying on every directory to read the same file.

The collection's landing-page destination is `https://geekist.co/skills`. Installation commands and research links in this repository remain direct, so those routes do not depend on the landing page's availability.

## Search visibility

Descriptive page titles, useful examples and meaningful links help people and search engines understand the collection. They are not ranking guarantees. The [Google Search Central guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) explains crawling, indexing and search presentation.

Search visibility and native agent selection are separate from prose quality. The [validation record](validation-results.md) identifies which checks and task trials have been executed.
