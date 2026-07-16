# Immigration — source scan

_This tool (the repo's first) was authored before the standardised source-scan
format existed; its Phase 1/2 reasoning lives in
`phase1-to-phase2-handoff.md` and `reframe-changelog.md`. This file was added
2026-07-16 to record the **geographic-scope pass** under sourcing-protocol.md
§Geographic scope (protocol v1.1). Earlier sourcing is documented in the two
build notes above and in each finding's `source_citation` / `caveat`._

## Geographic scope (protocol v1.1, §Geographic scope) — COMPLETED 2026-07-16

The immigration tool's evidence base is US-centric (anchored on the 2016 US
National Academies report) with some European sources (Dinesen, Germany-CESifo,
EuroCrime). Every leaf already carried a standing "US-centric evidence" caveat;
this pass searched explicitly for non-Western / LMIC destination evidence,
recorded outcomes, and authored findings where a qualifying source was found.

Queries run and outcomes:

- `immigration labor market wage effects developing countries South-South migration review` →
  **FOUND (decisive).** OECD/ILO 2018, *How Immigrants Contribute to Developing
  Countries' Economies* (ECLM programme; ten LMIC partner countries: Argentina,
  Costa Rica, Côte d'Ivoire, Dominican Republic, Ghana, Kyrgyzstan, Nepal,
  Rwanda, South Africa, Thailand). Verified from the full-report PDF: "Immigration
  has a limited impact on the labour market outcomes of native-born workers"; the
  immigrant-share/native-employment relationship is "generally negligible in the
  partner countries." Added as **F-geo-1** (CHALLENGES n_econ_wages_overall,
  strong, cluster `oecd-ilo-devecon`).
- `immigrants fiscal / economic effects non-Western receiving countries South Africa Gulf Côte d'Ivoire` →
  **FOUND (same source, decisive).** Same OECD/ILO report: immigrant contribution
  to GDP ~1% (Ghana) to 19% (Côte d'Ivoire), average ~7%; "overall, immigration is
  unlikely to depress GDP per capita" (→ **F-geo-2**, SUPPORTS n_econ_gdp_pc,
  strong). Fiscal: immigrants raise revenues but "the increase may not be always
  sufficient to offset the public expenditures they generate" — a sub-1%-of-GDP
  deficit in Kyrgyzstan and Nepal, net-positive in the other partner countries
  with data (→ **F-geo-3**, COMPLICATES n_fiscal_lowskill, moderate). All three
  tagged `oecd-ilo-devecon`; institutional overlap with the `OECD-migration`
  cluster flagged (partial non-independence).
- `immigration crime social trust cohesion Global South Latin America Africa Asia` →
  **FOUND (context only; no qualifying quantitative finding authored).** The
  cross-context syntheses located were either qualitative or scoped to *forced
  displacement / refugees* (World Bank social-cohesion syntheses) rather than
  general immigration, or edited-handbook chapters whose specific estimates could
  not be verified at authoring. A UK immigration-crime series mirrors the US "no
  effect / modestly negative" pattern but is not non-Western. **NULL** for a
  qualifying non-Western quantitative immigration-crime or immigration-trust
  study. Standard caveat applied to n_social_crime, n_social_trust,
  n_social_integration.

Bodies checked: OECD (International Migration Outlook `OECD-migration` vs the ILO
co-produced DevEcon programme `oecd-ilo-devecon` — treated as partially
non-independent, same institution). World Bank (forced-displacement social
cohesion — construct mismatch with general immigration, not authored).

New findings authored: F-geo-1, F-geo-2, F-geo-3. New crosslink tensions:
F-geo-1↔F-wl-1 (context-transportability), F-geo-2↔F-gp-1 (context-transportability,
with institutional-overlap note), F-geo-3↔F-fl-1 (context-transportability).

Remaining geographic gaps after documented search (standard caveat applied per
protocol: **"Evidence base is [region(s)]-heavy; external validity to other
settings is uncertain."**):
- Economic/fiscal dimensions now carry LMIC coverage via OECD-ILO (F-geo-1..3),
  but the low-skill-specific wage estimate, high-skill fiscal, and long-run
  dynamic-scoring leaves remain US-anchored.
- Innovation dimension: no LMIC immigrant-innovation study located.
- Social dimension (crime, trust, integration): no qualifying non-Western
  quantitative study located; evidence remains US/European.
