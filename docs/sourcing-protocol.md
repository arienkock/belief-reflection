# Sourcing Protocol (applied at authoring time)
_Frozen 2026-06-30; amended 2026-07-16 to add global-sourcing requirements. Binds every (node, direction) findings ticket. The point is that even-handedness is a
*rule applied while authoring*, not something hoped for and checked afterwards._

## Inclusion order (take the highest tier that exists for the exact claim)
1. Systematic review or meta-analysis on the specific claim.
2. National-academy / OECD-tier synthesis — **or a recognised equivalent from any world region** (see tier-2 equivalents below).
3. Primary empirical study — quasi-experimental (natural experiment, identification strategy) preferred over plain observational.

## Tier-2 equivalents: recognised non-Western and global bodies

These institutions produce synthesis-level work that qualifies at tier 2 on equal footing with Western national academies and OECD bodies. This list is illustrative, not exhaustive.

**Global / inter-regional**
- WHO regional offices (SEARO, WPRO, AFRO, EMRO, PAHO/AMRO) — regional synthesis reports
- IHME Global Burden of Disease (GBD) study and associated Lancet papers
- NCD Risk Factor Collaboration (NCD-RisC) — global pooled analyses including LMICs
- The Lancet Commissions and Series where co-authorship and data are explicitly multi-regional

**Africa**
- Africa CDC (Africa Centres for Disease Control and Prevention)
- African Academy of Sciences
- COHRED (Council on Health Research for Development)

**Latin America & Caribbean**
- FIOCRUZ (Oswaldo Cruz Foundation, Brazil) — one of the world's largest public-health research institutions
- PAHO/WHO technical reports
- CONACYT-funded national syntheses (Mexico)

**South & South-East Asia**
- ICMR (Indian Council of Medical Research) consensus statements and technical reports
- Indian National Science Academy (INSA)
- National Institute of Nutrition (NIN), Hyderabad — nutrition-specific synthesis
- SEAMEO TROPMED network regional synthesis

**East Asia**
- Chinese Center for Disease Control and Prevention (China CDC) epidemiological bulletins
- Chinese Academy of Medical Sciences (CAMS) / Peking Union Medical College
- National Natural Science Foundation of China (NSFC) programme reviews
- Korea Disease Control and Prevention Agency (KDCA) surveillance synthesis

**Middle East & North Africa**
- Iranian National Institute of Health Research (NIHR-Iran)
- Eastern Mediterranean Health Journal (EMHJ, WHO-EMRO peer-reviewed synthesis)

**High-quality global-scope journals** (supplement to tier-2 bodies when they publish region-specific syntheses):
- *Lancet Global Health*, *BMJ Global Health*, *Bulletin of the World Health Organization*, *Pan American Journal of Public Health*

## Hard rules
- **No tertiary basis.** Wikipedia, news aggregators and advocacy press releases may NOT be the evidential basis for a finding. (Wikipedia is allowed only as a map to locate primary sources.)
- **Advocacy/think-tank sources** (e.g. CIS, Mercatus, immigration councils) are permitted only to illustrate a stated position, must be labelled as such in the finding `caveat`, and may never be a scored node's sole support.
- **Source-tier rule:** reject a single-study finding where a meta-analysis exists on the same claim.
- **Both directions where they exist:** each scored leaf must include ≥1 good-faith source FOR and AGAINST its claim *if credible evidence in that direction exists*. If it does not, say so plainly and mark the node thin — never pad.
- **Independence:** tag `source_cluster`; the audit collapses by cluster so one report cannot corroborate itself.
- **No fabrication:** if no qualifying source is found, leave the slot empty and flag the node — do not invent or approximate a citation.
- **Recency:** flag sources ≥10 years old for refresh review.
- **Geographic scope:** for each topic, at least one source-scan query must explicitly target non-Western or LMIC evidence (e.g. `[topic] cohort Africa`, `[topic] South Asia meta-analysis`, `[topic] Latin America burden`). If the search returns nothing qualifying, document this explicitly — do not silently default to high-income-country evidence. Where evidence is concentrated in one region, state the geographic scope limitation in the node `caveat` using the phrase **"evidence base is [region]-heavy; generalisability to other settings uncertain."**

## `source_strength` rubric (editorial, not a computed confidence)
- **strong** — meta-analysis / systematic review / national-academy synthesis (including tier-2 equivalents above), OR population-level administrative census.
- **moderate** — a single well-designed study, or a synthesis with important caveats.
- **thin** — limited, contested, or heavily assumption-dependent evidence.
