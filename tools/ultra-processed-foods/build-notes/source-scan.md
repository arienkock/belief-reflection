# Preliminary source scan: Ultra-Processed Foods and Health

_Compiled 2026-07-15 as raw material for Phase 2 findings tickets. This is a
scan, not a findings file: nothing below has been authored into a finding,
verified against full text, or audited by cluster yet. Every entry was
located via live search on the compile date; entries marked ⚠ VERIFY were
identified but not confirmed in enough detail to state their direction,
venue, or magnitude with confidence — check the full text before use. The
sourcing protocol (`../../docs/sourcing-protocol.md`) binds at
findings-authoring time, not here — but the no-fabrication rule is already
in force: nothing in this file is cited from memory alone._

Draft leaf IDs refer to the draft tree in [proposal.md](proposal.md).

## Search trail (queries run on 2026-07-15, per improvement I6)

1. `ultra-processed foods policy 2026 FDA definition dietary guidelines debate evidence`
2. `ultra-processed food umbrella review meta-analysis adverse health outcomes BMJ 2024 Lane`
3. `ultra-processed food mortality 30-year cohort BMJ 2024 subgroups processed meat sugary beverages`
4. `Hall 2019 ultra-processed diet randomized controlled trial ad libitum energy intake 500 kcal Cell Metabolism`
5. `Dicken 2025 ultra-processed versus minimally processed diet randomized trial Nature Medicine weight loss UCL`
6. `NOVA classification criticism inter-rater reliability Braesco consistent assignment ultra-processed`
7. `Dietary Guidelines Advisory Committee ultra-processed foods "limited evidence" conclusion growth obesity 2024`
8. `Nordic Nutrition Recommendations 2023 ultra-processed food scoping review evidence insufficient NOVA`
9. `Lancet 2025 series ultra-processed foods Monteiro main thesis evidence critique`
10. `ultra-processed food addiction Gearhardt BMJ 2023 criticism construct validity debate` (scope-boundary check — addiction construct is OUT of scope, see proposal)
11. `Chile front-of-pack warning labels law sugary drink purchases reduction natural experiment Taillie 2020 PLOS Medicine`
12. `ultra-processed food association attenuated adjustment nutrient quality confounding residual healthy user bias`

Further per-flag queries will be logged in Stage 5 (verification) and
appended here.

---

## d_concept — is "ultra-processed" a valid, usable category?

This dimension is what made the topic previously *deferred* (see the Social
Media tool's proposal: "definitional fights over the NOVA classification
would dominate"). The resolution is to make the definitional question **one
scored leaf**, not the whole topic — so the empirical leaves can be judged
on their own evidence rather than being held hostage to it.

### Leaf: NOVA can be applied consistently/reliably (inter-rater reliability)

**AGAINST (the classification is not reliably applied):**
- Braesco et al. — inter-rater reliability test: Fleiss' κ = 0.32 (marketed
  foods) and 0.34 (generic foods), i.e. poor agreement between raters
  assigning foods to NOVA groups. ⚠ VERIFY exact venue/year and κ figures
  (located via secondary review coverage: *European Journal of Clinical
  Nutrition* "how functional is the NOVA system?", and a *Proceedings of the
  Nutrition Society* critical review). Tier: primary reliability study.
  Cluster hint: `nova-reliability`.
- Critical reviews of NOVA robustness: *Proceedings of the Nutrition
  Society*, "Are all ultra-processed foods bad? A critical review of the
  NOVA classification system"; *European Journal of Clinical Nutrition*
  2022, "Ultra-processed foods: how functional is the NOVA system?" — argue
  the category lacks clear, reproducible criteria. ⚠ VERIFY which make
  measured reliability claims vs. narrative critique. Cluster hint:
  `nova-critique`.

**FOR (the category is coherent/usable enough for policy):**
- Nova proponents / validity defence: Nature Food 2026, "The validity and
  utility of Nova and the concept of ultra-processed foods for science and
  policy"; AJCN 2023 "does the concept of UPF help inform dietary
  guidelines... YES". ⚠ VERIFY these argue reliability/validity specifically
  (vs. utility). Cluster hint: `nova-defence`.

### Leaf: UPF status predicts harm beyond conventional nutrient profiling

**FOR (processing adds predictive information beyond nutrients):**
- Reviews of prospective cohorts reporting the majority of UPF–outcome
  associations "remained significant and unchanged in magnitude after
  adjustment for diet quality" (Nutrients 2022 review of prospective cohort
  studies, PMC8747015). ⚠ VERIFY the "unchanged in magnitude" claim against
  the actual attenuation numbers. Cluster hint: `dietquality-review`.

**AGAINST (the concept adds little beyond salt/sugar/fat):**
- NOVA-critique literature (above) argues UPF harm is largely explained by
  established nutrient profiles (energy density, sugar, sodium, saturated
  fat) already captured by conventional nutrient-based schemes. ⚠ VERIFY a
  source that makes this as a measured claim, not just assertion.
- OVERLAPS with `n_assoc_confound` below — keep the two leaves distinct:
  this one is "does the *category* add information"; that one is "does
  *adjustment* explain the association away."

---

## d_assoc — observational association with disease

### Leaf: higher UPF consumption is associated with worse health (magnitude)

**FOR (association exists, and is broad):**
- Lane et al. 2024, *BMJ* 384:e077310, "Ultra-processed food exposure and
  adverse health outcomes: umbrella review of epidemiological
  meta-analyses" — 14 meta-analyses, 45 pooled analyses, n ≈ 9.89M;
  "convincing" or "highly suggestive" evidence for direct associations of
  higher UPF exposure with all-cause mortality, CVD mortality, common mental
  disorders, and overweight/obesity/type-2 diabetes. Tier 1 (umbrella review
  of meta-analyses). Cluster hint: `lane-umbrella`. NOTE: the authors state
  the design "does not allow us to establish causality."
- Juul & Bere 2024, scoping review for Nordic Nutrition Recommendations 2023
  (*Food & Nutrition Research*, PMC11077402) — 12 systematic reviews
  (5 meta-analyses) + 44 studies; concludes evidence on weight gain, CVD,
  T2D, and all-cause mortality is "strong enough to support dietary
  recommendations to limit" UPF. Tier 1/2 (national-nutrition-body
  synthesis). Cluster hint: `nordic-scoping`.

**AGAINST / COMPLICATES (the magnitude is modest and confounded):**
- Note: on this leaf the "AGAINST" is really "the association is small,"
  which is best carried by the cohort magnitudes themselves (BMJ 2024
  cohort: highest vs lowest quartile ≈ +4% all-cause mortality — see
  `n_assoc_confound`) and by the confounding leaf. The existence of *some*
  association is not seriously disputed; keep the magnitude number on the
  card, not an adjective.

### Leaf: the association reflects processing, not just nutrients / confounding

This is the pivotal, genuinely two-sided empirical leaf.

**FOR (survives adjustment — processing matters independently):**
- Nutrients 2022 review of prospective cohorts (PMC8747015): majority of
  UPF–outcome associations remained significant after adjustment for diet
  quality — read as evidence processing contributes independently. ⚠ VERIFY
  wording and how many associations attenuated. Cluster hint:
  `dietquality-review`.

**AGAINST (attenuates / plausibly explained by nutrients + healthy-user bias):**
- Fang et al. 2024 BMJ cohort (Nurses' Health Study + HPFS; below) — the
  UPF–mortality association "was less pronounced after overall dietary
  quality was taken into account, suggesting dietary quality has a stronger
  influence... than UPF consumption." Cluster hint: `bmj-cohort`.
- E-value analysis of unmeasured confounding for UPF and weight gain
  (medRxiv 2024, 2024.03.11.24304100) — ⚠ VERIFY conclusion/direction and
  whether it qualifies (preprint; check for a published version). Tests how
  much unmeasured confounding could explain the association.
- STANDING CAVEAT for the whole dimension: near-entirely observational +
  self-reported diet (FFQ); residual confounding and healthy-user bias are
  live. Every finding must state design.

### Leaf: harms are concentrated in specific UPF subgroups, not uniform

**FOR (concentration — some UPF subgroups drive the risk):**
- Fang, Zhang et al. 2024, *BMJ* 385:e078476, "Association of ultra-processed
  food consumption with all cause and cause specific mortality" (Nurses'
  Health Study + Health Professionals Follow-up Study; 74,563 women +
  39,501 men; ~48k deaths over 30+ yrs). Highest vs lowest quartile of total
  UPF ≈ **+4% all-cause mortality**; the association was driven by specific
  subgroups — meat/poultry/seafood-based ready-to-eat products (strongest),
  then sugar- and artificially-sweetened beverages, dairy-based desserts,
  ultra-processed breakfast foods. Cluster hint: `bmj-cohort`. Tier 1
  (large prospective cohort).

**AGAINST / COMPLICATES (some UPF subgroups are neutral or beneficial):**
- Same BMJ 2024 cohort carries the mirror: several UPF subgroups (e.g.
  whole-grain breads and cereals, yogurt/dairy-based) were NOT associated
  with higher mortality — evidence AGAINST a uniform "all UPF are harmful"
  reading. ⚠ VERIFY which subgroups were null/inverse. Same cluster
  (`bmj-cohort`) — the leaf's two directions come from one study; flag
  single-cluster and seek an independent subgroup source in Phase 2.

---

## d_cause — does processing itself cause harm? (controlled trials)

### Leaf: UP diets cause excess energy intake / weight gain independent of nutrients

**FOR (processing per se drives overeating):**
- Hall et al. 2019, *Cell Metabolism* 30(1):67-77, inpatient RCT (n = 20,
  crossover, 2 wks each): ad libitum intake ≈ **+500 kcal/day** on the
  ultra-processed vs unprocessed diet, with weight gain — despite diets
  matched for presented calories, energy density, macronutrients, sugar,
  sodium, fibre. Tier 3 (small but tightly controlled RCT), strong
  identification of a processing effect. Cluster hint: `hall-rct`.
- Dicken et al. 2025, *Nature Medicine*, UPDATE trial — randomised crossover,
  55 adults, 8-wk UPF vs MPF diets both following UK healthy-eating
  guidance: weight loss ~2× greater on the minimally-processed diet. Tier 3
  RCT (longest UPF diet trial to date). ⚠ VERIFY exact weight-difference
  magnitude. Cluster hint: `dicken-rct`. NOTE: Nature Medicine also
  published critiques (Ludwig et al.; Robinson & Forde; Wang & Peng) and the
  authors' reply — carry as caveat, not a separate cluster.

**AGAINST / COMPLICATES (processing effect is small, confounded by other levers, or mechanism-specific):**
- Frontiers in Nutrition 2024 systematic review of RCTs on UPF and
  health-related outcomes (10.3389/fnut.2024.1421728) — ⚠ VERIFY: how many
  qualifying trials, and whether the pooled/qualitative conclusion supports
  or tempers a processing effect. Candidate independent AGAINST/COMPLICATES
  cluster. Cluster hint: `rct-review`.
- Mechanism debate: Hall's own follow-up work attributes much of the +500
  kcal to energy density and hyper-palatability / eating rate rather than
  "processing" as such — i.e. the causal lever may be nutrient/texture
  properties that nutrient profiling could target. Carry as COMPLICATES.
  ⚠ VERIFY a citable statement of this.

---

## d_policy — what would UPF-specific policy change?

### Leaf: evidence is strong enough to justify UPF-specific dietary guidance

**AGAINST (authorities declined UPF-specific guidance):**
- 2025 US Dietary Guidelines Advisory Committee — systematic review
  (nesr.usda.gov, "Dietary Patterns with Ultra-Processed Foods and Growth,
  Body Composition, and Risk of Obesity", Nov 2024) graded the evidence
  insufficient to draw a conclusion; the Committee made **no UPF-specific
  recommendation**, citing inconsistent definitions and evidence gaps. Tier 2
  (government advisory synthesis). Cluster hint: `dgac-2025`.

**FOR (authorities / bodies say evidence suffices):**
- Nordic Nutrition Recommendations 2023 scoping review (above,
  `nordic-scoping`) — concluded evidence *is* strong enough to support
  recommendations to limit UPF. Direct FOR-vs-AGAINST institutional
  disagreement with the DGAC — a clean `empirical-contradiction`
  crosslink candidate.
- Lancet 2025 UPF Series (Monteiro et al., 3 papers, 18 Nov 2025) — argues
  the evidence base justifies broad policy action (labelling, marketing
  restriction, reformulation). Tier: expert series / advocacy-adjacent —
  ⚠ VERIFY and treat framing carefully; the Series is a stated position by
  the concept's originators, and drew published critique (Science Media
  Centre expert reactions). Cluster hint: `lancet-series`.

### Leaf: front-of-pack warning labels reduce purchases of targeted products

**FOR (labels change purchasing — measured natural experiment):**
- Taillie et al. 2020, *PLOS Medicine* 17(2):e1003015 — Chile's 2016 Law of
  Food Labeling: high-in **sugar-sweetened-beverage purchases fell ≈ 23.7%**
  after implementation (before-and-after with counterfactual). Tier 3
  (policy natural experiment), strong. Cluster hint: `chile-labels`.
- Follow-ups: *Lancet Planetary Health* 2021 (school-food changes); *PLOS
  Medicine* 2023 interrupted-time-series (PMID/journal.pmed.1004463):
  3-yr declines in purchased energy, sugar, saturated fat, sodium. Same
  Chilean policy — same cluster (`chile-labels`), not independent
  corroboration.

**AGAINST / COMPLICATES:**
- SCOPE CAVEAT: Chile's warning labels target **nutrients** (high-in sugar/
  salt/sat-fat/calories), NOT the NOVA "ultra-processed" category. This is
  evidence that *nutrient*-based front-of-pack labels work — its
  transportability to a *UPF*-specific label is an assumption. Mandatory
  `context-transportability` / `scope-aggregation` crosslink to the concept
  leaves. AGAINST-direction (labels don't change purchases) not located at
  scan time; likely thin — say so.

---

## Candidate crosslinks (typed per `crosslinks.json` conventions)

1. Cohort association magnitude ↔ RCT causal intake effect —
   `scope-aggregation` / `assumption-sensitivity` (a small observational
   HR and a large controlled-feeding intake effect answer different
   questions).
2. Association-survives-adjustment ↔ association-attenuates-after-adjustment —
   `empirical-contradiction` (the pivotal processing-vs-nutrients dispute).
3. NOVA-unreliable ↔ association-magnitude — `assumption-sensitivity`
   (if the exposure can't be classified consistently, what does a pooled
   association measure?).
4. Subgroup concentration ↔ total-UPF association — `scope-aggregation`
   (a total-UPF average hides that some subgroups drive it and others are
   null/inverse).
5. Nordic "evidence suffices" ↔ DGAC "evidence insufficient" —
   `empirical-contradiction` (same literature, opposite policy verdict).
6. Chile nutrient-label effect ↔ UPF-specific policy — `context-transportability`
   (a nutrient-targeted label's success does not establish a
   processing-targeted one's).

## Known gaps after this scan (Phase 2 to-do)

- Confirm Braesco κ figures and venue (`nova-reliability`).
- An independent (non-`bmj-cohort`) source for UPF-subgroup heterogeneity.
- A citable statement of the "processing effect is really energy-density/
  palatability" mechanism qualifier.
- The Frontiers 2024 RCT review's actual conclusion (`rct-review`) — is it a
  genuine independent AGAINST/COMPLICATES on the causal leaf?
- Whether any qualifying source makes a *measured* "adds nothing beyond
  nutrients" claim for `n_concept_beyond`, or whether that side is thin.
- Non-US/Nordic/UK evidence generally — scan is high-income-country heavy;
  expect a standing external-validity caveat.
