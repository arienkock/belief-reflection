# Structured source extraction (Phase 2, improvement I3)

_Built 2026-07-15 during Stage 5 verification. Findings in `findings.json` are
authored ONLY from this table, not from search-result summaries held in
working memory. Each entry records: verified claim, numbers, population,
design, limitations, and quotable conclusion — with the source read (I1)
noted. Load-bearing findings (quote an effect size OR are a node's sole
support in a direction) are marked ★._

## ★ interlab-vamas — Ciornii et al. 2025, Analytical Chemistry 97:8719 (VAMAS interlaboratory comparison)
- **Read:** abstract + PMC12044667 summary.
- **Design/scope:** VAMAS prestandardisation interlaboratory comparison; 84
  analytical laboratories worldwide; five methods (two thermo-analytical,
  three spectroscopic) on a water-soluble matrix.
- **Numbers:** reproducibility ~62–117% (PE) and ~46–62% (PET) for
  thermo-analytical; ~121–129% (PE) and ~64–70% (PET) for spectroscopic —
  large between-lab variation.
- **Quotable:** "urgent need for harmonisation of methodology and standard
  operating procedures"; different labs use different sampling, size
  thresholds, methods → "poorly comparable results."
- **Direction:** CHALLENGES n_measure_reliable (load-bearing sole strong
  AGAINST). Cluster `interlab-vamas`.

## standardisation — reference-material / ISO-standardisation work
- **Read:** search-level abstracts (PMC10285000 innovative reference
  materials; ISO/ASTM method development).
- **Content:** develops reference materials and ring-trial machinery to
  *improve* comparability; does NOT demonstrate that cross-lab consistency is
  currently *achieved*.
- **Direction:** SUPPORTS n_measure_reliable but on "standardisation
  underway", not measured achieved reproducibility → carry thin/COMPLICATES,
  honest thin-FOR flag. Cluster `standardisation`.

## ★ blood-leslie — Leslie et al. 2022, Environment International 163:107199
- **Read:** abstract (ScienceDirect S0160412022001258) + VU Amsterdam summary.
- **Design/scope:** Pyr-GC/MS, plastic particles ≥700 nm in whole blood of 22
  healthy volunteers.
- **Numbers:** quantifiable particles in **17/22 donors (~77%)**; mean sum
  concentration **1.6 µg/mL**; PET, PE, polystyrene, PMMA the main polymers.
- **Limitations:** small n; first-of-kind method; background contamination a
  standing concern for all such studies.
- **Direction:** SUPPORTS n_measure_body. Cluster `blood-leslie`.

## ★ placenta-ragusa — Ragusa et al. 2021, Environment International 146:106274 ("Plasticenta")
- **Read:** abstract + ScienceDirect S0160412020322297.
- **Design/scope:** Raman microspectroscopy; 6 human placentas.
- **Numbers:** **12 microplastic fragments (5–10 µm) in 4 of 6 placentas**
  (fetal side, maternal side, membranes); all pigmented; three stained
  polypropylene, rest identified by pigment.
- **Limitations:** very small n (6); only ~4% of each placenta analysed;
  contamination controls limited.
- **Direction:** SUPPORTS n_measure_body. Cluster `placenta-ragusa`.

## ★ contamination-review — analytical-QA critique of human-tissue detection
- **Read:** systematic review (ScienceDirect S2666831926000081, MNP in human
  tissues) + MDPI 15/5/154 + PMC12691203.
- **Content:** plastics ubiquitous in labs (air, clothing, labware) → false
  positives; procedural-blank failures cause overestimation; tissue lipids
  and proteins are known false positives; Nile Red stains non-plastic organic
  matter. Studies with rigorous multi-blank controls (mostly post-2023)
  report **lower, more realistic concentrations**; absence of blanks
  correlates with apparent overestimation.
- **Direction:** CHALLENGES n_measure_body (load-bearing methodological
  AGAINST). Cluster `contamination-review`. Same critique applies to Marfella
  → mandatory cross-dimension crosslink.

## ★ boucher-friot — Boucher & Friot 2017, IUCN, Primary Microplastics in the Oceans
- **Read:** IUCN news release + Policy Commons summary + SCIRP reference
  (PDF full text 403'd; figures confirmed across two independent secondary
  academic sources).
- **Numbers:** primary microplastics = **15–31%** of the ~9.5 Mt of ocean
  plastic; **synthetic textiles ~35%** and **tyres ~28%** of primary MP
  (together ~two-thirds); **personal-care cosmetics/microbeads ~2%**.
- **Quotable:** cosmetics "only contribute 2% of the releases of primary
  microplastics... banning microbeads from cosmetics is an illustrative
  action but will not solve the wider problem."
- **Directions:** SUPPORTS n_origin_sources (dominant sources identified/
  ranked); CHALLENGES n_policy_bans (target is ~2%). Cluster `boucher-friot`.

## secondary-dominance — secondary fragmentation dominates the environmental total
- **Read:** search-level (microbead/policy reviews; the primary-vs-secondary
  distinction is standard).
- **Content:** the most abundant environmental microplastic is **secondary**
  (fragmentation of larger mismanaged plastic waste), which primary-source
  inventories do not capture and which is poorly quantified; primary is only
  15–31% of the total.
- **Direction:** CHALLENGES n_origin_sources (the dominant fraction is
  unattributed → "quantified well enough for the total" is contested);
  COMPLICATES n_policy / n_root. Cluster `secondary-dominance`.

## ★ marfella-nejm — Marfella et al. 2024, NEJM 390:900–910
- **Read:** NEJM abstract + Medscape/NEJM summaries (numbers) — I1 load-bearing.
- **Design/scope:** prospective, multicentre, observational; **257** patients
  undergoing carotid endarterectomy for asymptomatic disease; MNPs measured
  in excised plaque (Pyr-GC/MS + electron microscopy).
- **Numbers:** polyethylene detected in **58.4%** (mean **21.7±24.5 µg/mg**);
  PVC in **12.1%**. Over mean follow-up **~34 months**, MNP-positive patients
  had **HR 4.53 (95% CI 2.00–10.27; P<0.001)** for the composite of MI,
  stroke, or all-cause death.
- **Limitations (authors):** does NOT prove causation; unmeasured confounding
  possible; single patient population (carotid-endarterectomy).
- **Direction:** SUPPORTS n_health_assoc (load-bearing sole FOR). Cluster
  `marfella-nejm`.

## ★ marfella-critique — NEJM Letters, 9 May 2024 (NEJMc2404154 + replies)
- **Read:** NEJM correspondence summaries.
- **Content:** no pre-analytical anti-contamination procedures beyond glass
  tubes; the operating-room environment/equipment contain PE and PVC → high
  intraoperative contamination risk; no operating-room blank samples tested;
  questions whether the MNP detection is credible.
- **Direction:** CHALLENGES n_health_assoc (load-bearing). Cluster
  `marfella-critique`.

## ★ tox-review — toxicological-pathway reviews (animal + cellular)
- **Read:** ScienceDirect S0304389425007095 ("Exploring toxicological
  pathways of microplastics and nanoplastics…", J. Hazardous Materials 2025)
  + rodent studies.
- **Content:** controlled models show inflammation, oxidative stress, gut and
  reproductive/organ effects — i.e. microplastics CAN cause biological harm.
- **Critical limitation:** the majority of these effects are demonstrated at
  doses/concentrations well above real human exposure (see dose-critique).
- **Direction:** SUPPORTS n_health_cause (harm demonstrated) — but the
  realistic-dose part is weak; carry the dose caveat. Cluster `tox-review`.

## ★ dose-critique — dose-realism critique
- **Read:** J. Hazardous Materials S0304389421010487 ("Micro/nanoplastics
  effects on organisms: A review focusing on 'dose'") + Bucci 2020 (below).
- **Numbers:** nanoplastic exposure doses in studies range orders of
  magnitude above estimated human intake (ng–µg/kg/day); the debate over
  environmental risk persists "because of unrealistically high exposures
  studied in most experiments."
- **Direction:** CHALLENGES n_health_cause (harm at REALISTIC dose not
  demonstrated). Cluster `dose-critique`.

## ★ foley-meta — Foley et al. 2018, Science of the Total Environment 631-632:550–559
- **Read:** PubMed 29529442 abstract (I1).
- **Design/scope:** meta-analysis of microplastic effects on fish and aquatic
  invertebrates; response categories: consumption, growth, reproduction,
  survival.
- **Numbers/finding:** negative effects on some taxa for all four categories;
  **most consistent effect = reduced consumption of natural prey**; **many
  effects neutral — "highly variable across taxa"**; zooplankton
  particularly susceptible.
- **Direction:** SUPPORTS n_environ_wildlife. Cluster `foley-meta`.

## ★ bucci-rochman — Bucci, Tulio & Rochman 2020, Ecological Applications 30(2):e02044
- **Read:** abstract + two independent secondary sources for the 17% figure.
- **Design/scope:** meta-analysis + systematic review; **139 studies, 577
  independent effects** across taxa, plastic types/sizes/shapes.
- **Numbers:** **only ~17%** of laboratory studies used environmentally
  relevant concentrations — i.e. most demonstrated effects occur at
  concentrations above those in most of the environment.
- **Direction:** CHALLENGES n_environ_wildlife (effects mostly at unrealistic
  concentrations). Cluster `bucci-rochman`.

## ★ koelmans-ssd — Koelmans et al. 2022, Microplastics and Nanoplastics 2:12 (risk framework)
- **Read:** Springer full text summary + PMC.
- **Design/scope:** species-sensitivity-distribution risk framework; 290 data
  points from 21 quality-screened toxicity studies; four management
  thresholds.
- **Numbers:** marine **HC5 ≈ 33.3 particles/L** (95% CI 0.36–13,943);
  freshwater HC5 ≈ 75.6 particles/L; sediment thresholds exceeded at only
  ~**17–32%** of sampled locations → risk currently concentrated in hotspots.
- **Direction:** CHALLENGES / COMPLICATES n_environ_wildlife (modelled risk
  exceeded only in a minority of places). Cluster `koelmans-ssd`.

## ★ microbead-ban — measured reduction after cosmetic-microbead bans
- **Read:** ACS ES&T Water 2023 (acsestwater.3c00526) summary.
- **Design/scope:** microbead abundance in Toronto WWTP effluents (2016–2019)
  and Lake Ontario surface water (2015 vs 2018) — before/after US (2017) and
  Canada (2018) bans.
- **Numbers:** median polyethylene microbeads in effluents **declined up to
  ~86%** (from 8.4–14.3 to 2.0–2.2 particles/m³) after the bans.
- **Direction:** SUPPORTS n_policy_bans (a targeted ban measurably reduced its
  target). Cluster `microbead-ban`.

## sapea / who — weight-of-evidence bodies
- **sapea** — SAPEA 2019, *A Scientific Perspective on Microplastics in Nature
  and Society*: at current environmental concentrations, widespread
  population-level human harm has NOT been demonstrated, with major
  uncertainties and a call for long-term monitoring. COMPLICATES n_root /
  n_health; CHALLENGES n_health_cause. Cluster `sapea`.
- **who** — WHO 2019, *Microplastics in drinking-water*: low health concern on
  available evidence; particles >150 µm not absorbed; insufficient data on
  nanoplastics; "based on incomplete information." COMPLICATES n_health_assoc.
  Cluster `who`.

## Cluster independence summary (for the audit)
- `blood-leslie`, `placenta-ragusa` — distinct teams/tissues; two independent
  detection clusters FOR n_measure_body; `contamination-review` the AGAINST.
- `marfella-nejm` supplies the ONLY FOR on n_health_assoc — single-cluster,
  flag thin; `marfella-critique` + `who` the AGAINST/COMPLICATES.
- `tox-review` (FOR) vs `dose-critique` + `sapea` (AGAINST) on n_health_cause
  — the FOR is high-dose; carry the dose caveat.
- `foley-meta` (FOR) vs `bucci-rochman` + `koelmans-ssd` (AGAINST) on
  n_environ_wildlife — three distinct clusters, genuinely two-sided.
- `microbead-ban` (FOR) vs `boucher-friot` (AGAINST, ~2% target) on
  n_policy_bans — both measured; the tension is scope, not existence.
- `boucher-friot` appears on both n_origin_sources (FOR) and n_policy_bans
  (AGAINST) — same source, two nodes; the audit collapses per node so no
  self-corroboration.
