# Phase 1 → Phase 2 Handoff: Frozen Question List (v1)
_Frozen 2026-07-15. Topic: Microplastics — Origin and Effects._

Nodes are frozen — see [`nodes.json`](nodes.json). Each scored leaf below is
an independent ticket: gather evidence FOR and AGAINST its `claim_evaluated`
under [`../../docs/sourcing-protocol.md`](../../docs/sourcing-protocol.md)
(target 3–6 findings per leaf). Do not add/rename nodes while researching;
file a change request to Phase 1 instead. `evidence_quality` and
`evidence_caveats` in `nodes.json` are placeholders (`pending-phase2`) —
Phase 2 findings plus the source-cluster audit fill them.

Sourcing leads per ticket refer to sections of
[`source-scan.md`](source-scan.md); every ⚠ VERIFY entry there must be
confirmed against full text before it becomes a finding. Improvements carried
from the session blueprint this round: **I1** (read the paper/abstract for
load-bearing findings), **I3** (structured extraction table per source before
authoring), **I4** (the compose script is already committed to `scripts/`),
**I6** (search trail logged in `source-scan.md`), **I8** (fast-moving sources
pinned with a re-search instruction).

## Phase 1 decisions (and why)

1. **The measurement problem is a scored leaf, not the whole topic.** As the
   UPF tool made NOVA inter-rater reliability a scored leaf, `n_measure_reliable`
   scores cross-laboratory reproducibility directly, so the harm leaves are
   judged on their own evidence instead of being fogged by "you can't even
   measure this." This is the most important framing decision in the tree.
2. **Two distinct measurement leaves.** `n_measure_reliable` (do labs agree on
   the number?) and `n_measure_body` (is a tissue detection real or lab
   contamination?) are different failure modes — measurement can be
   irreproducible across labs yet detect something real, or a detection can be
   real yet the concentration wrong. Kept separate. The contamination
   sub-question is scored HERE (as detection validity), and its critique is
   crosslinked into `n_health_assoc`, where the same contamination problem
   applies to the plaque-MNP measurement — but they are scored apart because
   "is tissue detection contaminated" and "is this association real" are
   different claims a participant can rate differently.
3. **The presence/harm split is the spine of the tree.** The deliberate design
   is that `n_measure_body` and `n_origin_sources` (PRESENCE, better evidenced)
   sit in the same tree as `n_health_assoc`/`n_health_cause` (HARM, poorly
   evidenced) precisely so a participant cannot let confidence on presence
   leak into confidence on harm. Findings must never write a detection result
   as if it were a harm result (I7 register check targets this).
4. **The human-association leaf is expected to be honestly THIN.** It rests
   essentially on one study (Marfella 2024) plus its published critiques.
   Score it, flag it thin, and do NOT pad it with a manufactured body of
   replication that does not exist. This is the single-study analogue of the
   UPF subgroup leaf.
5. **The causal leaf scores harm AT REALISTIC DOSES, not harm at any dose.**
   The claim wording ("at doses relevant to real human exposure") is load-
   bearing: controlled models frequently show harm, but mostly at inflated
   doses. Splitting "harm at all" from "harm at realistic dose" in the
   `depends_on` is what keeps the leaf honest; a FOR finding that only shows
   high-dose harm must carry the dose-realism caveat, and the dose-realism
   critique is a mandatory AGAINST.
6. **The ecology leaf mirrors the causal leaf's dose framing.**
   `n_environ_wildlife` scores harm AT ENVIRONMENTALLY REALISTIC
   CONCENTRATIONS, so the meta-analytic effect evidence (FOR) and the
   concentration-realism / hotspots-only risk work (AGAINST) are both
   mandatory. The shared "realistic concentration" problem across the human
   and ecological leaves is a mandatory `context-transportability` crosslink.
7. **The policy leaf is scoped to the transportability gap.** Like the UPF
   Chile label leaf, the honest structure is: a targeted ban can remove its
   target (FOR, possibly thin on measured reduction), but that target
   (personal-care microbeads ≈ 2% of primary microplastics) is a tiny share
   of a secondary-fragmentation-dominated total (AGAINST/COMPLICATES). The
   gap between "removed the target" and "reduced pollution" is a mandatory
   `scope-aggregation` / cross-dimension crosslink to `n_origin_sources`.
8. **Advocacy/interested-source handling.** Both industry-adjacent reassurance
   and campaign-group alarm exist. Neither may be a scored leaf's sole
   support; authoritative weight-of-evidence bodies (SAPEA 2019, WHO 2019,
   the Koelmans risk-assessment group) are preferred and carry the
   institutional weight where a leaf would otherwise rest on interested
   sources.

## Scored leaf tickets

### `n_measure_reliable` — Can microplastic concentrations be measured consistently across labs?
- claim to evaluate: **Microplastic concentrations can be measured consistently across laboratories and methods — reproducible, not method-dependent.**
- sourcing leads: source-scan §d_measure/reliable — the VAMAS interlaboratory comparison (84 labs; *Analytical Chemistry* 2025) is the load-bearing AGAINST (I1: confirm lab count and the reproducibility ranges from the paper); reference-material / ISO-standardisation work for the FOR side.
- expected flags: the FOR side likely argues that standardisation is *underway*, not that cross-lab consistency is *achieved* — if no source demonstrates achieved reproducibility, mark the FOR direction thin honestly. This is the one leaf where AGAINST is the well-evidenced side (cf. UPF `n_concept_reliable`).

### `n_measure_body` — Are microplastics reliably detected in the body, not contamination?
- claim to evaluate: **Microplastics are reliably detected inside the human body at levels indicating genuine internal exposure — not sampling/laboratory contamination.**
- sourcing leads: source-scan §d_measure/body — Leslie 2022 (blood, 17/22 donors) and Ragusa 2021 (placenta, 4/6) FOR; the analytical-contamination/QA review literature AGAINST. Shares the contamination critique with `n_health_assoc` — crosslink mandatory (`cross-dimension`).
- expected flags: the AGAINST is a methodological challenge, not a competing measurement — type it CHALLENGES where it disputes that detections are real, COMPLICATES where it only cautions. Both directions genuinely exist here.

### `n_origin_sources` — Are sources identified/quantified well enough to act on?
- claim to evaluate: **Major sources are identified and quantified well enough to target the biggest contributors (tyre wear, textiles, fragmentation).**
- sourcing leads: source-scan §d_origin — Boucher & Friot 2017 IUCN (15–31% primary; ~two-thirds textiles+tyres; microbeads ~2%) FOR; the secondary-fragmentation-dominance / apportionment-uncertainty point as COMPLICATES/AGAINST. I1: confirm the fraction figures from the IUCN report.
- expected flags: "sources are human-made" is near-uncontested, so keep the CLAIM on the contested part (quantified well enough to act); if the only AGAINST is uncertainty/secondary-dominance carried as COMPLICATES, the leaf may be one-sided FOR — flag it honestly.

### `n_health_assoc` — Is human microplastic burden associated with worse outcomes?
- claim to evaluate: **Higher microplastic exposure/burden is associated with worse human health outcomes.**
- sourcing leads: source-scan §d_health/assoc — Marfella et al. *NEJM* 2024 (HR 4.53, plaque MNPs) FOR (I1 REQUIRED: read the abstract/results for HR, CI, %, follow-up); the NEJM contamination-critique letters AGAINST; SAPEA/WHO "population-level harm not demonstrated" as COMPLICATES.
- expected flags: single-study FOR (`marfella-nejm`) — flag thin; do not imply replication. The contamination critique is the same one scored under `n_measure_body` — crosslink mandatory.

### `n_health_cause` — Does controlled evidence show harm at realistic doses?
- claim to evaluate: **Controlled animal/in-vitro evidence shows microplastics cause biological harm at doses relevant to real human exposure.**
- sourcing leads: source-scan §d_health/cause — toxicological-pathway reviews (inflammation, oxidative stress) FOR; the dose-realism critique (only ~17% of tested concentrations realistic; nanoplastic doses orders of magnitude high) and SAPEA/WHO AGAINST. I1: confirm the ~17% figure's source (Bucci 2020) and a citable dose-realism review.
- expected flags: the FOR side shows harm mostly at HIGH doses — every FOR finding must carry the dose-realism caveat, and the "at realistic doses, not demonstrated" side is mandatory, not optional. Do not let high-dose harm read as everyday-exposure harm (I7).

### `n_environ_wildlife` — Harm to aquatic organisms at realistic concentrations?
- claim to evaluate: **Microplastics cause measurable harm to aquatic organisms at environmentally realistic concentrations.**
- sourcing leads: source-scan §d_environ — Foley et al. 2018 meta-analysis (consumption/growth/reproduction/survival effects) FOR; Bucci & Rochman 2020 (only ~17% realistic concentrations) and Koelmans 2022 SSD risk framework (thresholds exceeded only in a minority of locations) AGAINST/COMPLICATES. I1: confirm Foley venue and the Bucci/Koelmans figures.
- expected flags: FOR effects are real but concentration-inflated; the claim is scoped to REALISTIC concentrations, so the realism critique is central, not a footnote. Shared realism problem with `n_health_cause` → mandatory `context-transportability` crosslink.

### `n_policy_bans` — Do source bans measurably reduce pollution?
- claim to evaluate: **Source-targeting policies such as microbead bans measurably reduce microplastic pollution.**
- sourcing leads: source-scan §d_policy — microbead-ban legislation (US Microbead-Free Waters Act 2015; EU 2023 restriction) FOR (⚠ VERIFY a MEASURED reduction, not just the law); the microbeads-are-~2%-of-primary / secondary-dominance point AGAINST/COMPLICATES (reuse `boucher-friot`).
- expected flags: FOR may be thin (measured before/after reduction scarce) — flag it. Transportability gap "removed target ≠ reduced pollution" is a mandatory `scope-aggregation`/cross-dimension crosslink to `n_origin_sources`. I8: EU/global-plastics-treaty policy is fast-moving — pin a re-search instruction.

## Non-scored structural nodes
- `n_root` (topic) → n_measure, n_origin, n_health, n_environ, n_policy
- `n_measure` (dimension) → n_measure_reliable, n_measure_body
- `n_origin` (dimension) → n_origin_sources
- `n_health` (dimension) → n_health_assoc, n_health_cause
- `n_environ` (dimension) → n_environ_wildlife
- `n_policy` (dimension) → n_policy_bans

## Candidate crosslinks carried from the scan
See source-scan §candidate-crosslinks — nine typed candidates. Mandatory ones:
`n_measure_reliable`↔`n_health_assoc` (`assumption-sensitivity`);
`n_measure_body` contamination↔`n_health_assoc` (`cross-dimension`);
`n_health_cause` harm↔dose-realism (`empirical-contradiction`, within leaf);
`n_environ_wildlife` effects↔concentration-realism (`empirical-contradiction`,
within leaf); `n_origin_sources`↔`n_policy_bans` (`scope-aggregation`);
`n_health_cause`↔`n_environ_wildlife` shared realism (`context-transportability`);
`n_measure_body` presence↔`n_health_cause` harm (`assumption-sensitivity`).

## Graduation
Per [`../README.md`](../README.md), this topic graduates to
`tools/microplastics/` when Phase 2 evidence-gathering starts: move
`nodes.json` into `tools/<slug>/data/`, this file, the proposal, and the scan
into `tools/<slug>/build-notes/`, and author `findings.json` /
`crosslinks.json` there under the protocol.
