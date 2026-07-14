# belief-reflection

A belief-investigation tool. Given a topic, it builds a tree of questions
(root → dimensions → scored leaf claims), attaches evidence for/against each
scored leaf under a declared sourcing protocol, and surfaces the evidence and
its limits to a participant — who reports their own confidence per leaf. The
tool does not compute or update a belief score for you.

Core design choices (see `docs/reframe-changelog.md` for the full rationale):

- **Nodes are questions, not preloaded answers.** Only leaf nodes carry a
  `claim_evaluated` that the participant rates.
- **Self-reported confidence, not a Bayesian engine.** The tool records the
  participant's confidence; it does not sum, weight, or update it.
- **Evidence audited by source cluster**, not raw finding count, so a single
  heavily-cited source can't manufacture apparent consensus.
- **Honesty markers everywhere**: evidence type, source strength, caveats
  (correlational / assumption-dependent / advocacy-source), coverage notes
  for what a topic map deliberately excludes, and typed cross-node tensions.

## Repository layout

- `app/BeliefEngine.tsx` — the working prototype: a single-file React
  component (Claude-artifact style, embeds its topic data inline) that walks
  a participant through the node tree, shows findings per scored leaf, and
  records self-reported confidence. Tracks which branches have been visited
  and surfaces cross-node tensions inline.
- `app/BeliefEngine.legacy.jsx` — an earlier iteration of the same component,
  kept for reference (no visited-branch tracking, plainer styling, no
  tension markers on choice screens).
- `topics/<topic>/nodes.json` — the frozen node tree for a topic (topic →
  dimensions → scored leaves), each with research/simple-register question
  text, `claim_evaluated`, `evidence_quality`, and `evidence_caveats`.
- `topics/<topic>/findings.json` — every evidence finding (FOR / AGAINST /
  COMPLICATES) per node, with claim paragraph, effect size, source
  citation/cluster, evidence type, source strength, and caveat — in both
  research and simple registers.
- `topics/<topic>/crosslinks.json` — typed tensions between findings
  (empirical-contradiction / assumption-sensitivity / context-transportability
  / scope-aggregation / cross-dimension), in both registers.
- `topics/<topic>/evidence-map.md` — human-readable rendering of the node
  tree plus findings and crosslinks above, for reading outside the app.
- `topics/<topic>/evidence-audit.md` — independent-corroboration audit per
  scored leaf (source-cluster counts, not vote-counting), plus source-tier,
  recency, and evidence-type sweeps.
- `topics/<topic>/participant-state.example.json` — the shape of a
  participant's session state: current node, path taken, `seen_evidence`,
  and `self_reported_confidence` per scored leaf (recorded, never computed).
- `docs/phase1-to-phase2-handoff.md` — the frozen question list handed from
  node-authoring (Phase 1) to evidence-gathering (Phase 2) for a topic.
- `docs/reframe-changelog.md` — changelog mapping review findings to fixes,
  reframes, and accepted-as-features decisions.
- `docs/sourcing-protocol.md` — the rules applied at authoring time for every
  finding: inclusion-order tiering, tertiary-source ban, advocacy labelling,
  the both-directions rule, independence tagging via `source_cluster`,
  no-fabrication, recency flagging, and the `source_strength` rubric.

## Topics

- **Immigration** (`topics/immigration/`) — effects of immigration on the
  host country across labour market, public finances, innovation, and social
  outcomes. This is the topic currently embedded in `app/BeliefEngine.tsx`.
