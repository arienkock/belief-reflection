# Reframe + Fixes — changelog
_2026-06-30. Maps each review finding to an action: **reframed**, **fixed**, **feature** (turned into visible content), or **open**._

## Reframe (subtracts the over-claim the reviewers were auditing against)
- **Bayesian engine → self-reported confidence.** `ParticipantState.belief_scores` (system-computed 0–1) is gone, replaced by `self_reported_confidence` that the *participant* sets per scored leaf. The tool records, it does not compute or update. → dissolves "Bayesian engine can't run", "incommensurable effect sizes" (nothing is summed), "root not falsifiable".
- **Nodes are questions; only leaves are scored.** Directional labels ("does not depress wages") → neutral questions + an explicit `claim_evaluated`. Removes answer-preloading. Root/dimensions are `role: topic|dimension`, not scored hypotheses.

## Methodology change (the one real one)
- **Declared sourcing protocol** (`sourcing-protocol.md`) applied at authoring time: inclusion order, tertiary ban, advocacy-labelling, both-directions rule, independence tagging, no-fabrication, recency. The audit now **collapses by `source_cluster`** instead of counting findings → fixes "vote-counting" and "non-independence" (NAS was 16/45).

## Content fixes
- **Crime cherry-pick fixed** (F-cr-1): now reports BOTH the ~0 cross-sectional and the −0.15 longitudinal estimate, and notes r≈−0.15 is weak (~2% variance).
- **Tertiary source removed**: the Wikipedia-routed 2002 Dutch figure is deleted and replaced by two peer-reviewed European studies — a 38-country correlational study finding a positive association for specific offences (F-cr-4), and an identification-aware German panel finding no general increase (F-cr-5).
- **Inflated confidence corrected**: single-study F-is-1 downgraded strong→moderate; `confidence` renamed `source_strength` with a written rubric.
- **Honesty markers added** to every finding: `evidence_type` and a plain-language `caveat` (correlational / assumption-dependent / advocacy-source). Node-level `evidence_caveats` computed automatically (US-centric, mostly-correlational, single-source-heavy).
- **Tensions typed**: each cross-link now carries a `kind` (empirical-contradiction / assumption-sensitivity / context-transportability / scope-aggregation / cross-dimension), so assumption-sensitivity is no longer dressed up as contradiction.
- **Coverage gaps surfaced**: root `coverage_note` lists what the map omits (housing, public-service congestion, gains to capital, origin-country effects, political effects).

## Accepted as features (the critique IS the curriculum)
- Correlational-not-causal, partial coverage, source concentration, "net good?" is many questions — all now shown to the participant rather than hidden.

## Open / not fixed by design
- **Construct validity of "social cohesion"** remains genuinely contested; handled by thin-flagging + COMPLICATES, not solved.
- **External validity** is flagged per-node, not corrected (the literature is US-heavy; we label rather than invent non-US evidence).
- **Shared-blind-spot of self-review**: only an outside reviewer choosing different sources can catch omitted findings. Unchanged.
