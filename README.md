# belief-reflection

Interactive tools for challenging and reflecting on your own beliefs. Each
tool walks you through a topic's evidence — findings for and against, their
sourcing, and where they pull against each other — and asks you to report
your own confidence per claim. **The tool shows evidence and its limits; it
does not compute or update a belief score for you.**

This is a public repository, open to scrutiny and review. See
[`CONTRIBUTING.md`](CONTRIBUTING.md) to flag a sourcing problem, propose a
topic, or contribute code.

## Live site

Published via GitHub Pages: **https://arienkock.github.io/belief-reflection/**
(once Pages is enabled — see [Publishing](#publishing) below).

## Core design choices

- **Nodes are questions, not preloaded answers.** A topic tree is root →
  dimensions → scored leaves; only leaves carry a `claim_evaluated` that the
  participant rates.
- **Self-reported confidence, not a Bayesian engine.** The tool records the
  participant's confidence; it does not sum, weight, or update it.
- **Evidence audited by source cluster**, not raw finding count, so a single
  heavily-cited source can't manufacture apparent consensus.
- **Honesty markers everywhere**: evidence type, source strength, caveats
  (correlational / assumption-dependent / advocacy-source), coverage notes
  for what a topic map deliberately excludes, and typed cross-node tensions.

See [`docs/README.md`](docs/README.md) for the full build methodology and
[`docs/sourcing-protocol.md`](docs/sourcing-protocol.md) for the rules bound
to every finding.

## Repository layout

```
tools/<slug>/       one published web tool per topic (its own build entry)
  BeliefEngine.tsx    the component
  data/               nodes.json, findings.json, crosslinks.json, ...
  evidence-map.md      human-readable evidence rendering
  evidence-audit.md    source-cluster corroboration audit
  build-notes/          topic-specific working notes (Phase 1/2 handoff, changelog)
research/<slug>/    candidate topics not yet built into a tool
docs/               methodology that applies across every tool
site/               the landing page (lists published tools)
tools.json          manifest read by the landing page
```

- **`tools/`** — each subdirectory is a self-contained, independently
  deployable tool. `tools/immigration/` is the first one; see it for the
  concrete shape of `data/`, `evidence-map.md`, `evidence-audit.md`, and
  `build-notes/`.
- **`research/`** — where a topic lives while its node tree and scope are
  still being worked out, before it graduates to `tools/`. See
  [`research/README.md`](research/README.md).
- **`docs/`** — generic methodology (the sourcing protocol, the pipeline
  overview) that isn't specific to any one topic.
- **`site/`** — the landing page at the repo root, listing published tools
  from `tools.json`.

## Publishing

The site builds with Vite: the landing page (`index.html` + `site/`) plus one
build entry per `tools/<slug>/index.html`, deployed by
[`.github/workflows/pages.yml`](.github/workflows/pages.yml) on every push to
`main`. To turn this on for a fresh clone of this repo:

1. Push a `main` branch (this repo currently only has the working branch
   this was authored on).
2. In the repo's **Settings → Pages**, set **Source** to **GitHub Actions**.
3. Push to `main` — the workflow builds `dist/` and deploys it.

`vite.config.ts` sets `base: "/belief-reflection/"` to match this repo's
name; update it if the repo is ever renamed.

## Local development

```
npm install
npm run dev      # local dev server
npm run build    # production build to dist/ — mirrors what CI deploys
```

New tools are picked up automatically: any `tools/<slug>/index.html` becomes
its own build entry with no config changes needed (see
[`CONTRIBUTING.md`](CONTRIBUTING.md#adding-a-new-tool-directory)).

## License

MIT — see [`LICENSE`](LICENSE).
