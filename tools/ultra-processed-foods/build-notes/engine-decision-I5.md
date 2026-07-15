# Engine duplication decision (improvement I5)

_The session blueprint's improvement I5 requires that any session which
touches the engine either extract it to a shared module or re-affirm
duplication **in writing** — the one thing not allowed is silent drift.
This session generated a third copy of the engine, so the decision is owed._

## Decision: re-affirm duplication, but make it mechanical

The `BeliefEngine.tsx` component is still duplicated per tool
(`tools/<slug>/BeliefEngine.tsx`), consistent with the repository's
self-contained-tool design. What changed this session: the copy is no longer
hand-produced. `scripts/compose-tool.py` (step 5) generates each tool's
engine by reading the **reference tool's component body verbatim** and
swapping only the inline `DATA` constant. The reference
(`social-media-teen-mental-health`) is the single source of the component
logic; the other tools' engines are build products of it.

## Why not extract to a shared module now

- At three tools the duplication cost is still low, and the compose script
  removes the drift risk that motivated I5 — every regenerated engine is
  byte-identical in logic to the reference by construction, so the copies
  cannot silently diverge.
- Extracting to a shared `@belief-reflection/engine` module that takes `data`
  as a prop would break the "each `tools/<slug>/` is independently
  deployable and self-contained" property the repo README advertises, and
  would be a larger refactor than this topic-addition session should carry.

## The line in the sand (for the next session that touches the engine)

- The reference tool's `BeliefEngine.tsx` is the **canonical** component. Do
  not edit a generated tool's engine by hand — edit the reference, then
  re-run `scripts/compose-tool.py <slug>` for every tool.
- I5 is only *deferred*, not closed. The trigger to extract a shared module
  is the blueprint's own "wrong at five tools" threshold: when a fifth tool
  is added, or when the component logic itself (not the data) next needs a
  change, extract `BeliefEngine` to a shared module taking `data` as a prop
  rather than regenerating a fourth/fifth copy.
