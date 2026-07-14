# Building a tool

This directory holds methodology that applies across every tool in `tools/`,
independent of topic. Topic-specific working notes (what was actually done
for a given topic, including its false starts) live with that tool, under
`tools/<slug>/build-notes/`.

## The pipeline, as practiced

The Immigration tool (`tools/immigration/`) is the first worked example, and
its build notes are the closest thing to a spec:

1. **Phase 1 — node authoring.** Define the topic's question tree: a root
   topic question, dimension nodes it splits into, and leaf nodes that each
   carry one falsifiable-in-principle `claim_evaluated`. Nodes are questions,
   not preloaded answers — see `tools/immigration/data/nodes.json` for the
   schema and `tools/immigration/build-notes/phase1-to-phase2-handoff.md`
   for what a frozen node list looks like at handoff.
2. **Phase 2 — evidence gathering.** For each scored leaf, gather findings
   FOR and AGAINST its claim under [`sourcing-protocol.md`](sourcing-protocol.md)
   — the inclusion-order tiering, tertiary-source ban, advocacy-source
   labelling, both-directions rule, `source_cluster` independence tagging,
   no-fabrication rule, and the `source_strength` rubric. See
   `tools/immigration/data/findings.json` for the resulting shape.
3. **Cross-linking.** Findings that pull against each other across nodes get
   typed as a tension (`empirical-contradiction`, `assumption-sensitivity`,
   `context-transportability`, `scope-aggregation`, or `cross-dimension`) —
   see `tools/immigration/data/crosslinks.json`.
4. **Audit.** Before publishing, collapse findings by `source_cluster` per
   node to check independent corroboration in each direction — vote-counting
   raw findings double-counts a single heavily-cited source. See
   `tools/immigration/evidence-audit.md` and the audit table's honesty flags
   (e.g. "no independent AGAINST; one-sided/single-source").
5. **Build the tool.** A self-contained React component (see
   `tools/immigration/BeliefEngine.tsx`) walks a participant through the
   tree, shows findings per scored leaf in both a research and a plain-language
   register, and records `self_reported_confidence` per leaf — see
   `tools/immigration/data/participant-state.example.json`. The tool never
   computes or updates that number; it only records what the participant
   reports.
6. **Reframe under review.** `tools/immigration/build-notes/reframe-changelog.md`
   is a worked example of taking outside review seriously: it maps each
   critique to reframed / fixed / accepted-as-feature / open, rather than
   arguing every finding down to nothing.

## Docs in this directory

- [`sourcing-protocol.md`](sourcing-protocol.md) — the rules bound to every
  (node, direction) findings ticket, applied at authoring time.

## Starting a new tool

See [`research/README.md`](../research/README.md) for how a topic moves from
a candidate idea to a `tools/<slug>/` directory.
