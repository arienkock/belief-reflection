# Contributing

This is a public repository, open to scrutiny and review. Corrections to
evidence, sourcing, or framing are as welcome as code contributions — often
more valuable.

## Ways to contribute

- **Flag a problem with a published tool's evidence** — a mis-cited source, a
  finding that misrepresents what its source says, a missing AGAINST where
  credible evidence exists, a claim that's gone stale. Open an issue naming
  the tool, the node or `finding_id`, and what's wrong. This is the most
  valuable kind of contribution to this project.
- **Propose a new topic.** See [`research/README.md`](research/README.md) for
  what makes a good candidate and how to write it up.
- **Work on an existing topic's evidence** (Phase 2 findings authoring) under
  [`docs/sourcing-protocol.md`](docs/sourcing-protocol.md) — every finding you
  add must follow the inclusion-order tiering, be tagged with a
  `source_cluster`, and carry an honest `caveat`.
- **Improve the app** — `tools/<slug>/` components, the landing page in
  `site/`, or the build setup.

## Review

Evidence changes get read the same way code does: does the source say what
the finding claims, is the `source_strength` and `evidence_type` honest, does
a `caveat` exist where one is warranted, is the opposing direction represented
if credible evidence for it exists. Don't expect content to be accepted just
because it's sourced — advocacy/think-tank sources are permitted only as
labelled position evidence, never as a scored node's sole support (see the
sourcing protocol's hard rules).

## Local development

```
npm install
npm run dev      # local dev server
npm run build    # production build to dist/, mirrors what CI deploys to Pages
```

Every `tools/<slug>/index.html` becomes its own build entry automatically —
add a new tool directory with an `index.html` and it's picked up by
`vite.config.ts` without further changes. Register it in `tools.json` so it
shows up on the landing page.

## Adding a new tool directory

A tool graduates from `research/<slug>/` once its nodes are frozen. At
minimum a `tools/<slug>/` directory needs:

- `data/nodes.json`, `data/findings.json`, `data/crosslinks.json` — see
  `tools/immigration/data/` for the schema.
- `evidence-map.md`, `evidence-audit.md` — human-readable renderings, kept in
  sync with the JSON.
- `build-notes/` — the Phase 1→2 handoff and any reframe/review changelog,
  kept even after publishing so the reasoning stays visible.
- `index.html` + `main.tsx` + the component itself — see
  `tools/immigration/` for a working example.

Then add an entry to root `tools.json` so it appears on the landing page.
