# Preliminary source scan: Microplastics — Origin and Effects

_Compiled 2026-07-15 as raw material for Phase 2 findings tickets. This is a
scan, not a findings file: nothing below has been authored into a finding,
verified against full text, or audited by cluster yet. Every entry was
located via live search on the compile date; entries marked ⚠ VERIFY were
identified but not confirmed in enough detail to state their direction,
venue, or magnitude with confidence — check the full text before use. The
sourcing protocol (`../../docs/sourcing-protocol.md`) binds at
findings-authoring time, not here — but the no-fabrication rule is already in
force: nothing in this file is cited from memory alone._

Draft leaf IDs refer to the draft tree in [proposal.md](proposal.md).

## Search trail (queries run on 2026-07-15, per improvement I6)

1. `microplastics nanoplastics atheroma carotid plaque cardiovascular events Marfella 2024 NEJM hazard ratio`
2. `interlaboratory comparison microplastic quantification reproducibility variability methods harmonization`
3. `primary microplastics oceans sources tyre wear synthetic textiles Boucher Friot IUCN 2017 estimate`
4. `plastic particles human blood Leslie 2022 Environment International quantification donors polymers`
5. `microplastics human tissue detection contamination procedural blank false positive quality assurance criticism`
6. `SAPEA 2019 scientific perspective microplastics nature society human health risk conclusion`
7. `microplastics aquatic organisms meta-analysis effects growth reproduction environmentally relevant Bucci Rochman 2020`
8. `microplastic toxicology animal studies unrealistically high concentrations dose environmental relevance criticism`
9. `microbead ban effectiveness reduction microplastic pollution Microbead-Free Waters Act primary microplastics small fraction`
10. `Ragusa 2021 Plasticenta microplastics human placenta Environment International first evidence`
11. `Marfella microplastics atheroma NEJM criticism limitations letters confounding measurement methodology 2024`
12. `WHO 2019 microplastics drinking water health risk low concern conclusion`
13. `Koelmans microplastic risk assessment species sensitivity distribution threshold environmental concentrations exceed 2022`

Further per-flag queries will be logged in Stage 5 (verification) and appended
here.

---

## d_measure — can we even measure microplastics and our exposure?

This dimension is the measurement analogue of the UPF tool's NOVA-reliability
leaf: make the "can we even measure this" question **one scored leaf** so the
empirical harm leaves are judged on their own evidence rather than being held
hostage to it.

### Leaf: microplastic concentrations can be measured consistently across labs

**AGAINST (measurement is not reproducible across labs):**
- VAMAS/prestandardisation interlaboratory comparison, 84 analytical
  laboratories, five thermo-analytical + spectroscopic methods on a
  water-soluble matrix: reproducibility ranged ~62–117% (PE) and ~46–62%
  (PET) for thermo-analytical, ~121–129% (PE) and ~64–70% (PET) for
  spectroscopic — i.e. large between-lab variation; "urgent need for
  harmonisation of methodology and SOPs." *Analytical Chemistry* 2025
  (Ciornii et al., acs.analchem.4c05403 / PMC12044667). ⚠ VERIFY exact
  reproducibility ranges and lab count against full text. Tier: dedicated
  interlaboratory reproducibility study. Cluster hint: `interlab-vamas`.
- Broader methods critiques: different labs use different sampling, size
  thresholds, and analytical methods → "poorly comparable results." Cluster
  hint: `methods-critique`.

**FOR (methods are reproducible / adequately standardised):**
- Emerging reference-material and standardisation work (ISO/ASTM method
  development; innovative reference materials for interlaboratory validation,
  PMC10285000). ⚠ VERIFY whether any source demonstrates *achieved*
  cross-lab consistency rather than proposing the machinery to get there —
  likely the FOR side is thin (standardisation in progress, not attained).
  Cluster hint: `standardisation`.

### Leaf: microplastics are reliably detected inside the human body (not contamination)

**FOR (particles genuinely present in human tissue/fluids):**
- Leslie et al. 2022, *Environment International* 163:107199 — plastic
  particles ≥700 nm quantified in whole blood of 17/22 donors (~77%); mean
  sum concentration 1.6 µg/mL; PET, PE, polystyrene, PMMA. Pyr-GC/MS. ⚠
  VERIFY donor count, concentration, and detection method. Cluster hint:
  `blood-leslie`.
- Ragusa et al. 2021, *Environment International* 146:106274 ("Plasticenta")
  — 12 microplastic fragments (5–10 µm) found in 4 of 6 human placentas
  (maternal side, fetal side, membranes); Raman microspectroscopy;
  pigmented, several polypropylene. ⚠ VERIFY counts. Cluster hint:
  `placenta-ragusa`.

**AGAINST / COMPLICATES (much of the signal may be laboratory contamination):**
- Analytical-challenges reviews: plastics ubiquitous in labs; fibres from
  clothing, labware fragments, airborne dust introduced during processing;
  failing procedural-blank controls → false positives and overestimation;
  tissue fatty acids/proteins are known false positives for plastic; Nile
  Red staining false positives. Studies with rigorous multi-blank controls
  (mostly post-2023) report *lower, more realistic* concentrations. ⚠ VERIFY
  a citable review making the QA/contamination critique as its central claim
  (e.g. ScienceDirect S2666831926000081 systematic review of MNP in human
  tissues; MDPI 2039-4713/15/5/154). Cluster hint: `contamination-review`.

---

## d_origin — where do microplastics come from?

### Leaf: sources are identified/quantified well enough to target the biggest contributors

**FOR (dominant sources are identified and human-made):**
- Boucher & Friot 2017, IUCN, *Primary Microplastics in the Oceans: A Global
  Evaluation of Sources* — 15–31% of ocean plastic is primary microplastic;
  ~two-thirds of primary microplastics come from synthetic-textile washing
  and tyre abrasion; personal-care microbeads a small share (~2%). ⚠ VERIFY
  the 15–31%, the two-thirds textiles+tyres, and the ~2% microbead figure.
  Tier: national/international-body source-apportionment synthesis. Cluster
  hint: `boucher-friot`.
- EEA, *Microplastics from textiles: towards a circular economy* — textiles a
  major source; supporting synthesis. Cluster hint: `eea-textiles`.

**AGAINST / COMPLICATES (the quantification is too uncertain / secondary
fragmentation dominates and is poorly attributed):**
- Source-apportionment estimates carry very wide uncertainty and are
  model-dependent; the environmentally dominant fraction is **secondary**
  microplastic (fragmentation of larger mismanaged plastic waste), which is
  poorly quantified and not captured by primary-source inventories. ⚠ VERIFY
  a citable statement that secondary > primary in the environment and that
  primary source inventories disagree by large factors. Cluster hint:
  `secondary-dominance`.

---

## d_health — human health effects

### Leaf: higher microplastic burden is associated with worse human health outcomes

**FOR (a measured human association exists):**
- Marfella et al. 2024, *NEJM* 390:900–910 — prospective observational,
  257 carotid-endarterectomy patients; polyethylene detected in plaque of
  58.4% (mean 21.7±24.5 µg/mg), PVC in 12.1%; over ~34 months, MNP-positive
  patients had HR 4.53 (95% CI 2.00–10.27) for the composite of MI, stroke,
  or all-cause death. Authors state it does *not* prove causality;
  unmeasured confounding possible. ⚠ VERIFY HR, CI, percentages, follow-up.
  Tier: single prospective cohort (strong design, single study). Cluster
  hint: `marfella-nejm`.

**AGAINST / COMPLICATES (the association may be artefactual, confounded, or
unreplicated):**
- NEJM Letters (9 May 2024, NEJMc2404154 and replies) — no pre-analytical
  anti-contamination procedures beyond glass tubes; operating-room
  environment/equipment contain PE and PVC → high intraoperative
  contamination risk; no OR blank samples. Direct methodological challenge to
  whether the MNP measurement is credible. ⚠ VERIFY the letters' specific
  critiques. Cluster hint: `marfella-critique`.
- Weight-of-evidence reviews (SAPEA 2019; WHO 2019) conclude population-level
  human harm has not been demonstrated at current exposures — the broader
  human epidemiological base is essentially one contested study. Cluster
  hint: `sapea` / `who`.

### Leaf: controlled evidence shows microplastics cause harm at realistic doses

**FOR (mechanistic/organismal harm demonstrated in controlled models):**
- Toxicological-pathway reviews (animal + cellular models) reporting
  inflammation, oxidative stress, and organ/reproductive effects
  (ScienceDirect S0304389425007095 "Exploring toxicological pathways…";
  rodent kidney/other studies). ⚠ VERIFY that any FOR source reports effects
  at *environmentally/dietarily realistic* doses — most do not. Cluster hint:
  `tox-review`.

**AGAINST (harm not demonstrated at realistic doses):**
- Dose-realism critiques: reviews focusing on 'dose' find most exposure
  studies used concentrations orders of magnitude above real human exposure
  (nanogram–microgram/kg/day); a meta-analysis found ~83% of exposure trials
  used dramatically elevated dosages (only ~17% environmentally realistic,
  Bucci et al. 2020). SAPEA/WHO: insufficient evidence of adverse effects at
  current exposure. ⚠ VERIFY the 17%/83% figure attribution and a citable
  dose-realism review. Cluster hint: `dose-critique` (+ `sapea`, `who`).

---

## d_environ — environmental / ecological effects

### Leaf: microplastics harm aquatic organisms at environmentally realistic concentrations

**FOR (measured ecological effects):**
- Foley et al. 2018, *Science of the Total Environment* — meta-analysis of
  microplastic effects on fish and aquatic invertebrates: negative effects on
  consumption, growth, reproduction, survival for some taxa, though many
  effects neutral/variable across taxa. ⚠ VERIFY venue/year and the
  "consumption most consistent" result. Cluster hint: `foley-meta`.
- Later fish meta-analyses report inhibited growth, survival, reproduction,
  increased oxidative damage. Cluster hint: `fish-meta` (⚠ VERIFY
  independence from Foley).

**AGAINST / COMPLICATES (effects mostly at unrealistic concentrations; risk
exceeded only in hotspots):**
- Bucci, Tulio & Rochman 2020, *Ecological Applications*, "What is known and
  unknown about the effects of plastic pollution: A meta-analysis and
  systematic review" — only ~17% of tested exposure concentrations are
  environmentally realistic; many reported effects occur only above
  environmental levels. ⚠ VERIFY title/venue and the 17% figure. Cluster
  hint: `bucci-rochman`.
- Koelmans et al. 2022 risk framework (*Microplastics and Nanoplastics*) —
  species-sensitivity-distribution HC5 ≈ 33.3 particles/L (marine); modelled
  thresholds exceeded at only ~17–32% of sampled locations → ecological risk
  currently concentrated in hotspots, not ubiquitous. ⚠ VERIFY HC5 and the
  exceedance percentages. Cluster hint: `koelmans-ssd`.

---

## d_policy — what would microplastic policy change?

### Leaf: source-targeting policies (microbead bans) measurably reduce pollution

**FOR (targeted source reduction works for its target):**
- Microbead bans (US Microbead-Free Waters Act 2015; EU/UK bans on rinse-off
  microbeads; EU 2023 intentionally-added microplastic restriction) removed a
  controllable primary source at source. ⚠ VERIFY a citable *measured*
  reduction (monitoring data), not just the existence of the law — this may
  be thin. Cluster hint: `microbead-ban`.

**AGAINST / COMPLICATES (the targeted source is a tiny fraction of the total):**
- Personal-care microbeads are ~2% of primary microplastics, and primary
  microplastics are only 15–31% of ocean plastic; the environmental total is
  dominated by secondary fragmentation and by tyre/textile inputs that the
  cosmetic-microbead bans do not touch — so a ban that eliminates its target
  changes total microplastic pollution negligibly. Nutrient-label-style
  transportability gap (cf. the UPF Chile leaf). ⚠ VERIFY the fraction
  figures (reuse `boucher-friot`). Cluster hint: `secondary-dominance`.
- AGAINST-direction "bans did not reduce their target" not located at scan
  time; likely thin — say so.

---

## Candidate crosslinks (typed per `crosslinks.json` conventions)

1. Measurement-unreliable ↔ human-association (Marfella): if MNP
   quantification is not reproducible, the exposure/burden in the association
   study is measured with large error — `assumption-sensitivity` /
   `cross-dimension`.
2. Measurement-unreliable ↔ body-detection: the same measurement problem
   undercuts detection reliability — `cross-dimension`.
3. Contamination critique (body-detection) ↔ Marfella (human-association):
   the contamination critique of tissue detection applies directly to the
   plaque-MNP measurement — `cross-dimension` / `empirical-contradiction`.
4. Toxicology-harm ↔ dose-realism (within `n_health_cause`):
   `empirical-contradiction` (harm shown vs. not shown at realistic dose).
5. Ecology effects (Foley) ↔ concentration-realism (Bucci/Koelmans) (within
   `n_environ_wildlife`): `assumption-sensitivity` / `empirical-contradiction`.
6. Origin secondary-dominance ↔ microbead-ban policy: banning a small primary
   source barely dents a secondary-dominated total — `scope-aggregation` /
   `cross-dimension`.
7. Human dose-realism ↔ ecological concentration-realism: the same
   "realistic concentration" problem across human and wildlife leaves —
   `context-transportability`.
8. Body-detection (presence) ↔ health-causation (harm): finding particles in
   the body does not establish they cause harm — `assumption-sensitivity` /
   `cross-dimension`.
9. Human association (Marfella) ↔ human causation (toxicology): an
   observational human association and a controlled mechanistic effect are
   different estimands — `assumption-sensitivity`.

## Known gaps after this scan (Phase 2 to-do)

- Confirm the VAMAS interlab reproducibility ranges and lab count
  (`interlab-vamas`).
- A citable review whose *central* claim is the tissue-detection
  contamination/QA problem (`contamination-review`).
- A citable dose-realism review and the correct attribution of the ~17%
  environmentally-realistic-concentration figure (Bucci 2020 vs the 'dose'
  review) for both the human-cause and ecology leaves.
- Whether any FOR source demonstrates *achieved* cross-lab measurement
  consistency (else the reliability FOR side is thin).
- A *measured* microbead-ban reduction (monitoring), else the policy FOR side
  is thin.
- Whether a second, independent ecological meta-analysis exists distinct from
  Foley 2018 (`fish-meta` independence).
- Non-Western / freshwater and terrestrial evidence generally — scan is
  marine- and high-income-heavy; expect a standing external-validity caveat.
