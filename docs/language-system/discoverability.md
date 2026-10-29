# Make the collection easier to find and choose

The collection has two audiences: people looking for useful writing skills and agents choosing a workflow. Search visibility, directory listings and native skill activation need separate observations.

## Implemented presentation changes

- The README leads with the writing problem, a source-constrained before/after example, installation and a route to all eleven skills.
- Each skill has a generated [human overview](../skills/index.md) with an example request, expected result, sources and a pinned installation command.
- `standards/skill-catalogue.json` supplies presentation copy, plugin keywords, prompts and source routes. `scripts/sync-skill-catalogue.py --check` detects drift in generated pages and presentation metadata.
- Skill activation descriptions remain authored in `SKILL.md` and are checked against the catalogue. Presentation generation cannot silently broaden activation intent.
- The stable plugin identifier and explicit compatibility-router policy are retained.

The human pages are repository documentation rather than extra context bundled into every skill. No automatic session-start injection or new always-on skill was introduced.

## Repository About settings to apply

The GitHub connection available in this session can write repository files but does not expose a repository-settings update operation. These settings are prepared for the supported settings UI; they are not claimed as applied.

| Setting | Intended value |
| --- | --- |
| Description | Clear agent prose, shared project terminology and practical architecture workflows from Geekist. |
| Website | https://geekist.co |
| Topics | agent-skills, plain-language, technical-writing, documentation, terminology, architecture, copywriting, adr, claude-code, codex, backend, frontend |

The description and first ten topics match the canonical presentation catalogue. Existing backend/frontend topics remain relevant to the original playbooks. The website identifies the publisher; it does not imply that a new skill landing page has been published there.

## Directory coverage and web pages

The source review retrieved a SkillsCat snapshot containing the original two architecture skills. Current coverage of all eleven needs direct verification. Retrieval of the Geekist skills.sh route failed, so no absence or indexing failure is inferred. Use the directory's supported submission or refresh route after checking its actual coverage.

A future Geekist article can link directly to the human overview for each skill. If separate website landing pages are useful, give each a clear reader purpose, one useful example, installation steps and source links. Keep the repository as the versioned instruction source. A machine-readable catalogue can assist discovery, but no untested claim of automatic agent discovery follows from exposing JSON.

## Measure the effects

Record whether readers can identify the appropriate skill and complete installation. Test ordinary requests for native skill selection in the client that matters. For website discovery, inspect indexing and actual query/impression/visit changes over time using available analytics.

These presentation changes provide clearer routes. Improved ranking, traffic, native activation and installation on mobile require their own evidence. See the [competitive review](competing-writing-skills.md) for the observed alternatives and the [Google Search Central guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) for the website-discovery principles considered.
