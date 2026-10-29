# Geekist Skills identity

The skill icon uses the exact handwritten **G** from Geekist.co's yellow wordmark, centred on the site's charcoal background. It keeps the existing brand rather than introducing an unrelated symbol.

## Source and adaptation

- Site: <https://geekist.co/>, inspected 29 October 2026.
- The site's exported homepage references `/wp-content/uploads/Geekist.co_.svg` as its logo, with the alternative text “Geekist.co logo in yellow handwritten-style text”.
- Pinned source: [Geekist wordmark](https://github.com/theGeekist/geekiststatic/blob/ce75a57ab41ab37a8b3de4b8948501381c1b8de5/wp-content/uploads/Geekist.co_.svg).
- Original Git blob: `753611043c69f9bfa802af2ada0f505280ca7df7`.
- Preserved source copy: `geekist-wordmark-source.svg`; SHA-256 `b1ce8b3b39c9d6fdf8ed40a16f03e28559c859e46c0b7f3125ef99afa9460236`.

The original wordmark is one compound path. The icon retains its first closed subpath (the G) without redrawing its geometry. It applies `translate(43 16) scale(1.02)` inside a `256 × 256` view box, with a rounded charcoal tile. Yellow `#ffde59` comes from the wordmark; charcoal `#161616` comes from the site's base colour.

`geekist.svg` is the 512-pixel nominal version; `geekist-small.svg` uses identical geometry with a 128-pixel nominal size. Both remain resolution-independent SVGs. Each skill bundles its own copies and references them through `interface.icon_small` and `interface.icon_large` in `agents/openai.yaml`.

The source wordmark and both adaptations were rendered and visually checked, including the small icon. No text, font dependency, external image, script or network reference is embedded in the adapted SVGs.

## Attribution

Geekist branding belongs to Geekist. The adaptation was requested by its owner for this skill collection. This note records provenance; it does not assert a separate open trademark or brand licence. The repository's software licence remains unchanged.
