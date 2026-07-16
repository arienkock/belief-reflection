# Sourcing Protocol (applied at authoring time)
_Version 1.1 — original freeze 2026-06-30; Amendment 1 (global sourcing) 2026-07-16. Binds every (node, direction) findings ticket. The point is that even-handedness is a
*rule applied while authoring*, not something hoped for and checked afterwards._

## Inclusion order (take the highest tier that exists for the exact claim)
1. Systematic review or meta-analysis on the specific claim.
2. National-academy / OECD-tier synthesis — **or a recognised equivalent from any world region** (see tier-2 equivalents below).
3. Primary empirical study — quasi-experimental (natural experiment, identification strategy) preferred over plain observational.

The inclusion order is not overridden by the geographic-scope rule. If a global tier-1 source exists, prefer it; the geographic-scope rule governs the *search* (what you must look for), not the *ranking* (what wins when found).

## Tier-2 equivalents: recognised non-Western and global bodies

These institutions produce synthesis-level empirical work — consensus statements, systematic reviews, or surveillance syntheses with documented methodology — that qualifies at tier 2. This list is illustrative, not exhaustive. To qualify, an unlisted body must produce independently peer-reviewed or formally audited synthesis output, not only policy briefs, capacity-building documents, or funding-portfolio summaries.

**Evaluating unlisted institutions:** ask (a) is the output peer-reviewed or subject to independent audit? (b) does the institution have editorial independence from the government that funds it? (c) is the methodology documented and replicable? If all three are yes, it is a reasonable tier-2 equivalent; note your judgment in the source-scan's search trail.

**Global / inter-regional**
- WHO regional offices (SEARO, WPRO, AFRO, EMRO, PAHO/AMRO) — regional synthesis reports
- IHME Global Burden of Disease (GBD) study and associated Lancet papers — **cluster note: GBD data underpin many Lancet, Lancet Global Health, and NCD-RisC analyses; tag all GBD-derived sources to cluster `ihme-gbd` and apply the independence rule accordingly**
- NCD Risk Factor Collaboration (NCD-RisC) — global pooled analyses including LMICs — tag cluster `ncd-risc`; treat as distinct from GBD only when the underlying data sources are documented as non-overlapping
- The Lancet Commissions and Series where co-authorship and data are explicitly multi-regional

**Africa**
- Africa CDC (Africa Centres for Disease Control and Prevention) — surveillance and synthesis bulletins
- African Academy of Sciences — consensus and position statements
- African Population and Health Research Center (APHRC, Nairobi) — peer-reviewed demographic and health research

**Latin America & Caribbean**
- FIOCRUZ (Oswaldo Cruz Foundation, Brazil) — peer-reviewed research institute; one of the world's largest public-health research institutions
- PAHO/WHO technical reports (tag cluster `paho` — note PAHO reports often reprocess the same regional surveillance data; check for independent primary inputs before treating as corroboration)
- CONAHCYT-funded national syntheses (Mexico) — Consejo Nacional de Humanidades, Ciencias y Tecnologías (formerly CONACYT, renamed 2023)

**South & South-East Asia**
- ICMR (Indian Council of Medical Research) consensus statements and technical reports
- Indian National Science Academy (INSA) — formal position statements
- National Institute of Nutrition (NIN), Hyderabad — nutrition-specific synthesis reports

**East Asia**
- Chinese Academy of Medical Sciences (CAMS) / Peking Union Medical College — peer-reviewed synthesis
- Chinese Center for Disease Control and Prevention (China CDC) epidemiological bulletins — **independence caveat: data access and publication are subject to government oversight; treat as surveillance data rather than independently audited synthesis, and do not rely on China CDC bulletins as the sole tier-2 support for a finding**
- Korea Disease Control and Prevention Agency (KDCA) surveillance synthesis

**Middle East & North Africa**
- Iranian National Institute of Health Research (NIHR-Iran) — peer-reviewed outputs only (not ministry policy communications)
- Eastern Mediterranean Health Journal (EMHJ, WHO-EMRO peer-reviewed synthesis)

**High-quality global-scope journals** (qualify as tier-2 when they publish region-specific systematic reviews or syntheses, not single primary studies):
- *Lancet Global Health*, *BMJ Global Health*, *Bulletin of the World Health Organization*, *Pan American Journal of Public Health*

**Coverage note:** Eastern Europe, Central Asia, and Pacific Island nations are underrepresented in this list. Research from those regions should be evaluated against the unlisted-institution criteria above and cited at the appropriate tier.

## Hard rules
- **No tertiary basis.** Wikipedia, news aggregators and advocacy press releases may NOT be the evidential basis for a finding. (Wikipedia is allowed only as a map to locate primary sources.)
- **Advocacy/think-tank sources** (e.g. CIS, Mercatus, immigration councils) are permitted only to illustrate a stated position, must be labelled as such in the finding `caveat`, and may never be a scored node's sole support.
- **Source-tier rule:** reject a single-study finding where a meta-analysis exists on the same claim. The geographic-scope rule does not override this: do not import a weak LMIC single study to satisfy geographic due diligence when a global meta-analysis already covers the claim.
- **Both directions where they exist:** each scored leaf must include ≥1 good-faith source FOR and AGAINST its claim *if credible evidence in that direction exists*. If it does not, say so plainly and mark the node thin — never pad. The both-directions requirement operates on the global evidence base, not separately per region.
- **Independence:** tag `source_cluster`; the audit collapses by cluster so one report cannot corroborate itself.
- **No fabrication:** if no qualifying source is found, leave the slot empty and flag the node — do not invent or approximate a citation.
- **Recency:** flag sources ≥10 years old for refresh review.
- **Geographic scope:** for each topic, the source scan must include at least one search pass explicitly targeting non-Western or LMIC evidence (e.g. `[topic] cohort Africa`, `[topic] South Asia meta-analysis`, `[topic] Latin America burden`). The search trail in the build note must record these queries and their outcomes. If no qualifying source is found after a documented search, record the null result in the search trail and state the geographic scope limitation in the node `caveat` using the standard phrase: **"Evidence base is [region(s)]-heavy; external validity to other settings is uncertain."** Do not silently default to high-income-country evidence.

## `source_strength` rubric (editorial, not a computed confidence)
- **strong** — meta-analysis / systematic review / national-academy synthesis (including tier-2 equivalents above), OR population-level administrative census.
- **moderate** — a single well-designed study, or a synthesis with important caveats.
- **thin** — limited, contested, or heavily assumption-dependent evidence.
