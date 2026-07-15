# Structured source extraction (Phase 2, improvement I3)

_Built 2026-07-15 during Stage 5 verification. Findings in `findings.json`
are authored ONLY from this table, not from search-result summaries held in
working memory. Each entry records: verified claim, numbers, population,
design, limitations, and quotable conclusion — with the full-text/abstract
source read (I1) noted. Load-bearing findings (quote an effect size OR are a
node's sole support in a direction) are marked ★; those had their primary
source or its abstract/results read._

## ★ lane-umbrella — Lane et al. 2024, BMJ 384:e077310 (umbrella review)
- **Read:** PMC10899807 full text (results + limitations).
- **Design/scope:** umbrella review of 14 meta-analyses, 45 pooled analyses,
  n = 9,888,373. Observational inputs only.
- **Numbers (graded):** Class I "convincing": CVD mortality RR 1.50
  (1.37–1.63); T2D (dose-response) RR 1.12 (1.11–1.13); anxiety OR 1.48
  (1.37–1.59); common mental disorders OR 1.53 (1.43–1.63). Class II "highly
  suggestive": all-cause mortality RR 1.21 (1.15–1.27); obesity OR 1.55
  (1.36–1.77); depression HR 1.22 (1.16–1.28); adverse sleep OR 1.41
  (1.24–1.61).
- **Quotable conclusion:** direct associations found across mortality, mental
  health, metabolic outcomes; "further randomised controlled trials are
  needed," only short-term intermediate-outcome trials feasible.
- **Limitations (verbatim):** umbrella design "did not consider specific
  confounder or mediator adjustments"; "residual confounding being perhaps
  most pertinent."
- **Direction:** SUPPORTS n_assoc_magnitude. Cluster `lane-umbrella`.

## ★ bmj-cohort — Fang et al. 2024, BMJ 385:e078476 (NHS + HPFS cohort)
- **Read:** BMJ Group summary + Harvard Chan summary (numbers + subgroups).
- **Design/scope:** prospective cohort, 74,563 women + 39,501 men, 48,193
  deaths over 30+ years; self-reported diet (FFQ).
- **Numbers:** highest vs lowest quartile total UPF (≈7 vs 3 servings/day) =
  **+4% all-cause mortality** (1536 vs 1472 deaths/100,000 person-years);
  neurodegenerative +8%. **No association** with CVD, cancer, or respiratory
  mortality.
- **Subgroups:** processed meat strongest and most consistent; also
  associated: sugar-/artificially-sweetened beverages, dairy-based desserts,
  ultra-processed breakfast foods, miscellaneous. Several subgroups (fats/
  condiments/sauces, packaged sweet snacks/desserts, ready-to-eat dishes,
  packaged savory snacks) showed **no significant association** — NOT
  reported as protective/inverse (correction to the scan, which assumed
  named inverse subgroups).
- **Attenuation:** association "was less pronounced after overall dietary
  quality was taken into account, suggesting that dietary quality has a
  stronger influence on long term health than ultra-processed food
  consumption."
- **Directions:** SUPPORTS n_assoc_magnitude (modest); SUPPORTS + COMPLICATES
  n_assoc_subgroup (both from this one study — single-cluster flag);
  CHALLENGES n_assoc_confound (attenuation). Cluster `bmj-cohort`.

## ★ dietquality-review — Nutrients 2022 review of prospective cohorts (PMC8747015)
- **Read:** PMC full text (adjustment counts + conclusion).
- **Design/scope:** review of 37 prospective-cohort studies, 91 models, 87
  outcomes; 142 diet-quality adjustments examined.
- **Numbers:** 64 of 66 significant UPF–outcome associations remained
  significant after diet-quality/pattern adjustment; 136/142 adjustments did
  not explain the association (all-cause mortality 15/15 unchanged; CVD
  29/31; cancer 8/8; T2D 7/7; adiposity 40/43). Only 2 adjustments explained
  associations.
- **Quotable conclusion (verbatim):** "Our findings suggest that the adverse
  consequences of UPFs are independent of dietary quality or pattern,
  questioning the utility of reformulation."
- **Direction:** SUPPORTS n_assoc_confound; SUPPORTS n_concept_beyond.
  Cluster `dietquality-review`. NOTE: directly contradicts bmj-cohort
  attenuation → mandatory `empirical-contradiction` crosslink.

## ★ nova-reliability — Braesco et al. 2022, Eur J Clin Nutr (NOVA reproducibility)
- **Read:** publisher-blocked; figures confirmed via two independent
  secondary academic sources (globalharmonization commentary; ProQuest/
  oskar-bordeaux full-text index) — κ figures consistent across both.
- **Design/scope:** online survey of French food/nutrition specialists;
  120 marketed products WITH ingredient info (159 evaluators) + 111 generic
  items WITHOUT ingredient info (177 evaluators).
- **Numbers:** Fleiss' κ = **0.32** (marketed) and **0.34** (generic) — poor
  agreement. Only one 90-food cluster reached 91% NOVA-4 assignment; the rest
  heterogeneous.
- **Key nuance (correction to scan):** agreement stayed low **even when
  ingredient information was available** — not simply a data-access problem.
- **Quotable conclusion (verbatim):** "current NOVA criteria do not allow for
  robust and functional food assignments."
- **Direction:** CHALLENGES n_concept_reliable (load-bearing sole strong
  AGAINST). Cluster `nova-reliability`.

## nova-defence — Nova validity/utility defences (Nature Food 2026; AJCN 2023)
- **Read:** search-level abstracts only (not load-bearing FOR — the reliable
  claim's FOR side is thin by design).
- **Content:** argue the concept has validity/utility for science and policy;
  do NOT present a measured high inter-rater reliability rebuttal to Braesco.
- **Direction:** SUPPORTS n_concept_reliable but on UTILITY not measured
  reliability → carry as thin/COMPLICATES, honest thin-FOR flag. Cluster
  `nova-defence`.

## ★ hall-rct — Hall et al. 2019, Cell Metabolism 30(1):67-77 (inpatient RCT)
- **Read:** NIH release + PubMed abstract (matched vars, intake, weight,
  mechanism).
- **Design/scope:** randomized crossover, n = 20 (10M/10F), inpatient
  metabolic ward, 2 weeks each arm, 1 continuous month.
- **Matched:** presented calories, macronutrients, sugars, fat/carbohydrate,
  fibre, sodium, energy density.
- **Numbers:** ad libitum intake **+~500 kcal/day** on UP diet; **+0.9 kg**
  on UP vs equivalent loss on unprocessed.
- **Mechanism (verbatim-ish):** ate faster on UP diet; authors note "slight
  differences in protein levels ... could potentially explain as much as
  half the difference in calorie intake."
- **Directions:** SUPPORTS n_cause_intake (load-bearing); the protein/eating-
  rate/energy-density point → COMPLICATES on mechanism. Cluster `hall-rct`.

## ★ dicken-rct — Dicken et al. 2025, Nature Medicine (UPDATE crossover)
- **Read:** UCL release (magnitudes + caveats) + Nature Medicine
  critique/reply listing.
- **Design/scope:** randomized crossover, 55 adults (50 completed ≥1 arm),
  8-week arms, 4-week washout; BOTH diets followed UK healthy-eating
  guidance.
- **Numbers:** weight change **−2.06% (MPF) vs −1.05% (UPF)** at 8 weeks (≈2×);
  daily deficit ≈290 (MPF) vs 120 (UPF) kcal; projected 1-yr differences
  larger. Cardiometabolic markers: **no significant differences between
  diets**; both no-change-or-improved from baseline. 10 per group gained
  weight (adherence).
- **Caveats:** small; short; formal published critiques in Nature Medicine
  (Ludwig et al.; Robinson & Forde; Wang & Peng) + authors' reply — carry the
  dispute. The absolute between-diet gap is ~1 percentage point of body
  weight over 8 weeks.
- **Direction:** SUPPORTS n_cause_intake (independent cluster from hall).
  Cluster `dicken-rct`.

## ★ rct-review — Frontiers in Nutrition 2024 systematic review of UPF RCTs
- **Read:** Frontiers full text (counts + conclusion + limitations).
- **Design/scope:** systematic review of **4 RCTs**, 42 outcomes (pregnant
  women; obesity grades; children; the Hall ward study).
- **Numbers:** "No significant effects were observed in 30 out of the 42
  outcomes evaluated." 3 studies had 20–40% dropout.
- **Quotable conclusion (verbatim):** "the available evidence to date cannot
  establish a clear causal link between the degree of food processing and
  adverse health outcomes"; "the added value of classifying foods based on
  their industrial processing compared to traditional nutrient-based systems
  remains an unresolved controversy."
- **Directions:** CHALLENGES/COMPLICATES n_cause_intake (independent AGAINST
  cluster); COMPLICATES n_concept_beyond. Cluster `rct-review`.

## ★ dgac-2025 — 2025 US Dietary Guidelines Advisory Committee UPF systematic review
- **Read:** NESR systematic-review summary + FoodNavigator/STAT/Covington
  coverage.
- **Content:** graded the evidence insufficient to draw a conclusion on UPF
  and body composition/obesity; Committee made **no UPF-specific
  recommendation**, citing inconsistent UPF definitions and evidence gaps.
- **Direction:** CHALLENGES n_policy_guidance. Cluster `dgac-2025`. Tier 2
  (government advisory synthesis). I8: re-search before republish — FDA/USDA
  federal UPF definition due 2026 may move this.

## nordic-scoping — Juul & Bere 2024, scoping review for Nordic Nutrition Recommendations 2023 (PMC11077402)
- **Read:** search-level abstract + NNR page.
- **Content:** 12 systematic reviews (5 meta-analyses) + 44 studies;
  concludes evidence on weight gain, CVD, T2D, all-cause mortality is
  "strong enough to support dietary recommendations to limit" UPF.
- **Direction:** SUPPORTS n_policy_guidance; SUPPORTS n_assoc_magnitude.
  Cluster `nordic-scoping`. Contradicts dgac-2025 → mandatory
  `empirical-contradiction`.

## lancet-series — Monteiro et al. 2025, Lancet UPF Series (3 papers, 18 Nov 2025)
- **Read:** search-level abstracts + Science Media Centre expert reactions.
- **Content:** argues evidence justifies broad policy action (labelling,
  marketing restriction, reformulation). Authored by the concept's
  originators/advocates; drew mixed expert reaction.
- **Direction:** SUPPORTS n_policy_guidance — LABELLED advocacy-adjacent, not
  sole support (protocol). Cluster `lancet-series`.

## ★ chile-labels — Taillie et al. 2020, PLOS Medicine 17(2):e1003015
- **Read:** PMC7012389 full text (effect, design, target, bundling).
- **Design/scope:** before-after with preregulation-trend counterfactual;
  Kantar WorldPanel Chile, 2,383 households, 69,696 household-months,
  2015–2017.
- **Numbers:** high-in SSB purchases **−23.7% (95% CI −23.8 to −23.7)** vs
  counterfactual (−22.8 mL/capita/day).
- **Target/bundling (critical):** labels flagged NUTRIENTS (added sugar/
  sodium/saturated fat/calorie thresholds), **not** the NOVA processing
  category; bundled with child-marketing restriction + school-sales ban.
- **Direction:** SUPPORTS n_policy_labels (load-bearing sole FOR). Cluster
  `chile-labels`. Nutrient-target ≠ processing-target → mandatory
  `context-transportability` crosslink.

## Cluster independence summary (for the audit)
- `lane-umbrella`, `nordic-scoping` — distinct synthesis teams; both include
  overlapping primary cohorts, so treat as partially non-independent on
  magnitude but distinct on the policy verdict.
- `bmj-cohort` supplies BOTH directions on n_assoc_subgroup — single-cluster
  flag stands; independent subgroup cohort not located.
- `dietquality-review` vs `bmj-cohort` — genuine opposite results on
  attenuation; do not let them corroborate each other.
- `hall-rct`, `dicken-rct`, `rct-review` — three distinct clusters on the
  causal leaf (two FOR, one COMPLICATES/AGAINST).
