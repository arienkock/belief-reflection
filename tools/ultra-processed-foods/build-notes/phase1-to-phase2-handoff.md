# Phase 1 → Phase 2 Handoff: Frozen Question List (v1)
_Frozen 2026-07-15. Topic: Ultra-Processed Foods and Health._

Nodes are frozen — see [`nodes.json`](nodes.json). Each scored leaf below is
an independent ticket: gather evidence FOR and AGAINST its `claim_evaluated`
under [`../../docs/sourcing-protocol.md`](../../docs/sourcing-protocol.md)
(target 3–6 findings per leaf). Do not add/rename nodes while researching;
file a change request to Phase 1 instead. `evidence_quality` and
`evidence_caveats` in `nodes.json` are placeholders (`pending-phase2`) —
Phase 2 findings plus the source-cluster audit fill them.

Sourcing leads per ticket refer to sections of
[`source-scan.md`](source-scan.md); every ⚠ VERIFY entry there must be
confirmed against full text before it becomes a finding. Improvements
adopted from the session blueprint this round: **I1** (read the actual
paper/abstract for load-bearing findings), **I3** (structured extraction
table per source before authoring), **I4** (the compose script is committed
to `scripts/`), **I6** (search trail logged in `source-scan.md`), **I8**
(fast-moving policy sources pinned with a re-search instruction).

## Phase 1 decisions (and why)

1. **The definitional problem is a scored leaf, not the whole topic.** UPF
   was deferred by the previous session because "definitional fights over
   NOVA would dominate." Resolution: `n_concept_reliable` scores the
   reliability question directly (the participant rates whether NOVA can be
   applied consistently), so the empirical leaves are judged on their own
   evidence instead of being fogged by the definitional dispute. This is the
   single most important framing decision in the tree.
2. **Two distinct concept leaves.** `n_concept_reliable` (can raters agree?)
   and `n_concept_beyond` (does the category add information over nutrients?)
   are different failure modes — a category can be unreliable yet real, or
   reliable yet redundant. Kept separate.
3. **`n_concept_beyond` and `n_assoc_confound` ask the same statistical
   question from two sides and are deliberately NOT merged.** "The concept
   is redundant with nutrients" (a claim about the category) and "this
   association is confounded/attenuates" (a claim about a body of cohort
   evidence) are different claims a participant can rate differently. They
   share sources (the diet-quality-adjustment literature) and MUST be
   crosslinked, but they are scored apart. If Phase 2 finds their evidence
   truly indistinguishable, file a change request to merge — do not merge
   silently while authoring.
4. **The causal dimension scores only energy intake / weight.** That is
   where controlled-feeding trials exist (Hall 2019; Dicken 2025). Long-term
   disease endpoints can't be randomised and stay observational under
   `n_assoc`. Scoring a "processing causes CVD/cancer" leaf would be
   unsourceable as an RCT and would double-count the cohort evidence.
5. **`n_assoc_magnitude` keeps "meaningful magnitude" in the claim.** The
   existence of a broad association is not in serious dispute; magnitude and
   interpretation are. The `depends_on` requires findings to report the
   number (e.g. the ~+4% cohort hazard) so the participant sets the
   threshold.
6. **The policy label leaf is scoped to PURCHASES of TARGETED products, and
   flagged as nutrient-target ≠ processing-target.** The strong evidence
   (Chile) is a nutrient warning label bundled with marketing/school rules;
   it is honest evidence that front-of-pack labels change purchasing, but its
   transportability to a UPF-specific label is an assumption. The claim is
   worded to what the evidence supports (targeted products, purchases), and
   the gap to UPF-specific policy is a mandatory crosslink, not a silent
   generalisation.
7. **Advocacy handling.** The NOVA concept's originators (Monteiro et al.)
   are also its leading advocates (2025 Lancet Series). Their syntheses are
   permitted as labelled position evidence and may never be a scored node's
   sole support — same rule applied to Twenge in the Social Media tool.

## Scored leaf tickets

### `n_concept_reliable` — Can NOVA be applied consistently by different classifiers?
- claim to evaluate: **The NOVA 'ultra-processed' category can be applied consistently — different trained classifiers reliably assign the same foods to the same group.**
- sourcing leads: source-scan §d_concept/reliable — Braesco et al. inter-rater study (Fleiss' κ ≈ 0.32–0.34) is the load-bearing AGAINST (I1: confirm venue, year, κ, and the name-vs-ingredient-list dependence from the paper); NOVA-defence (Nature Food 2026 validity/utility paper; AJCN 2023 "YES") for the FOR side.
- expected flags: FOR side may be utility-not-reliability — if no source makes a MEASURED high-reliability claim, mark the FOR direction thin honestly. This is the one leaf where AGAINST is the well-evidenced side.

### `n_concept_beyond` — Does UPF status predict harm beyond nutrient profiling?
- claim to evaluate: **Ultra-processed status carries information about health risk over and above conventional nutrient profiling — the processing dimension adds predictive value.**
- sourcing leads: source-scan §d_concept/beyond — the diet-quality-adjustment review literature (Nutrients 2022 prospective-cohort review) FOR; NOVA-critique literature AGAINST. Shares evidence with `n_assoc_confound` — crosslink mandatory (`assumption-sensitivity`).
- expected flags: the "adds nothing beyond nutrients" side may lack a single MEASURED source (much of it is assertion in critiques) — if so, carry it as COMPLICATES from within the attenuation cohort, and flag thin.

### `n_assoc_magnitude` — Is higher UPF consumption associated with worse health at a meaningful magnitude?
- claim to evaluate: **Higher UPF consumption is associated with worse health outcomes (mortality, CVD, T2D, obesity) at a magnitude that is practically meaningful, not trivially small.**
- sourcing leads: source-scan §d_assoc/magnitude — Lane et al. *BMJ* 2024 umbrella review (I1: read abstract + results for which outcomes reached "convincing"/"highly suggestive" grades) and Juul & Bere Nordic scoping review FOR; the modest cohort hazard ratios (BMJ 2024 cohort, ~+4%) supply the magnitude-tempering read.
- expected flags: don't let the umbrella review dominate the audit; report numbers not adjectives; every finding carries the self-report-FFQ caveat.

### `n_assoc_confound` — Does the association reflect processing, not nutrients/confounding?
- claim to evaluate: **The UPF–disease association reflects a processing effect that survives adjustment for nutrient quality and confounders — not fully explained by nutrients or healthy-user bias.**
- sourcing leads: source-scan §d_assoc/confound — Nutrients 2022 review ("associations remained significant and unchanged after diet-quality adjustment") FOR; Fang et al. *BMJ* 2024 cohort ("less pronounced after dietary quality accounted for") and the E-value confounding analysis AGAINST. This is the pivotal leaf — both directions mandatory, `empirical-contradiction` crosslink between the survives/attenuates findings.
- expected flags: I1 REQUIRED here — read the actual attenuation numbers, do not author from the review's summary adjective. Over-adjustment (nutrients on the causal path) is a caveat on the AGAINST side.

### `n_assoc_subgroup` — Are harms concentrated in specific UPF subgroups?
- claim to evaluate: **Health harms are concentrated in specific UPF subgroups (processed meats, sugar-sweetened beverages) rather than uniform across all UPF.**
- sourcing leads: source-scan §d_assoc/subgroup — Fang et al. *BMJ* 2024 cohort subgroup breakdown supplies BOTH directions (harmful: meat/poultry/seafood RTE, sweetened beverages; neutral: whole-grain breads/cereals, some dairy). ⚠ VERIFY the null/inverse subgroups against full text.
- expected flags: single-cluster (`bmj-cohort`) supplies both directions — flag single-source-heavy and run a Phase 2 search for an independent cohort with subgroup breakdowns; if none qualifies, say so.

### `n_cause_intake` — Do UP diets cause excess intake/weight independent of nutrients?
- claim to evaluate: **Ultra-processed diets cause excess energy intake and weight gain relative to less-processed diets, independent of nutrient composition.**
- sourcing leads: source-scan §d_cause — Hall et al. *Cell Metabolism* 2019 inpatient RCT (~+500 kcal/day; I1: confirm the matched variables and the weight change) and Dicken et al. *Nature Medicine* 2025 UPDATE crossover FOR (⚠ VERIFY the weight-difference magnitude; carry the published Nature Medicine critiques in the caveat); Frontiers 2024 RCT systematic review as candidate independent COMPLICATES; the energy-density/eating-rate mechanism qualifier as COMPLICATES.
- expected flags: both trials small/short — transportability caveat standing on the leaf; the "is the lever really processing?" mechanism point must be a COMPLICATES, not dropped.

### `n_policy_guidance` — Is the evidence strong enough for UPF-specific guidance?
- claim to evaluate: **The evidence is strong enough to justify UPF-specific dietary guidance beyond nutrient-based advice.**
- sourcing leads: source-scan §d_policy/guidance — Nordic Nutrition Recommendations 2023 scoping review ("strong enough to recommend limiting") FOR; 2025 US DGAC systematic review + non-recommendation AGAINST; Lancet 2025 Series FOR (labelled advocacy, not sole support). `empirical-contradiction` crosslink Nordic↔DGAC mandatory.
- expected flags: this leaf's disagreement is partly about evidentiary standards + the definitional problem — the `depends_on` says so; don't present it as a pure data dispute. I8: pin authoring date; the FDA/USDA 2026 definition may move this — add a re-search instruction to the audit.

### `n_policy_labels` — Do front-of-pack warning labels reduce purchases?
- claim to evaluate: **Front-of-pack warning labels reduce purchases of the targeted products.**
- sourcing leads: source-scan §d_policy/labels — Taillie et al. *PLOS Medicine* 2020 (Chile, SSB purchases −23.7%) FOR; follow-up Chilean ITS studies are the SAME cluster (`chile-labels`), not independent. AGAINST (labels don't change purchases) not located — likely thin.
- expected flags: nutrient-target ≠ processing-target is the standing caveat; `context-transportability`/`scope-aggregation` crosslink to the concept and guidance leaves mandatory. Single-cluster FOR — flag it.

## Non-scored structural nodes
- `n_root` (topic) → n_concept, n_assoc, n_cause, n_policy
- `n_concept` (dimension) → n_concept_reliable, n_concept_beyond
- `n_assoc` (dimension) → n_assoc_magnitude, n_assoc_confound, n_assoc_subgroup
- `n_cause` (dimension) → n_cause_intake
- `n_policy` (dimension) → n_policy_guidance, n_policy_labels

## Candidate crosslinks carried from the scan
See source-scan §candidate-crosslinks — six typed candidates, of which the
mandatory ones are: `n_assoc_confound` survives↔attenuates
(`empirical-contradiction`); `n_concept_beyond`↔`n_assoc_confound`
(`assumption-sensitivity`); `n_assoc_subgroup`↔`n_assoc_magnitude`
(`scope-aggregation`); `n_policy_guidance` Nordic↔DGAC
(`empirical-contradiction`); `n_policy_labels`↔concept/guidance
(`context-transportability`); cohort magnitude↔RCT intake
(`assumption-sensitivity`).

## Graduation
Per [`../README.md`](../README.md), this topic graduates to
`tools/ultra-processed-foods/` when Phase 2 evidence-gathering starts: move
`nodes.json` into `tools/<slug>/data/`, this file, the proposal, and the
scan into `tools/<slug>/build-notes/`, and author `findings.json` /
`crosslinks.json` there under the protocol.
