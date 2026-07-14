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

- `topics/<topic>/nodes.json` — the frozen node tree for a topic (topic →
  dimensions → scored leaves), each with research/simple-register question
  text, `claim_evaluated`, `evidence_quality`, and `evidence_caveats`.
- `topics/<topic>/evidence-map.md` — human-readable rendering of the same
  tree with FOR / AGAINST / COMPLICATES findings per scored leaf, sources,
  and a typed cross-node tensions section.
- `topics/<topic>/evidence-audit.md` — independent-corroboration audit per
  scored leaf (source-cluster counts, not vote-counting), plus source-tier,
  recency, and evidence-type sweeps.
- `docs/phase1-to-phase2-handoff.md` — the frozen question list handed from
  node-authoring (Phase 1) to evidence-gathering (Phase 2) for a topic.
- `docs/reframe-changelog.md` — changelog mapping review findings to fixes,
  reframes, and accepted-as-features decisions.

## Topics

- **Immigration** (`topics/immigration/`) — effects of immigration on the
  host country across labour market, public finances, innovation, and social
  outcomes.
