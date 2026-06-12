---
name: sdg-mapping-standard
description: >
  Defines how research topics and outputs are mapped to the 17 UN Sustainable
  Development Goals and India's NEP 2020 priorities. Provides a scoring rubric
  for SDG impact assessment used by the opportunity-scout, work-product-reviewer,
  and sdg-impact-audit workflow.
version: 2.0.0
created: 2026-05-29
tags: [SDG, impact, NEP2020, sustainability]
---

# SDG Mapping Standard

## Purpose

Every research output at REVA should be evaluable for its contribution to the UN Sustainable Development Goals (SDGs) and India's national development priorities. This standard defines:

1. How to identify primary and secondary SDG relevance for a research topic
2. How to score the depth of SDG impact
3. How to connect research findings to India-specific SDG implementation gaps

---

## The 17 SDGs — Research Relevance Quick-Map

| SDG | Theme | Typical REVA Research Connections |
|-----|-------|-----------------------------------|
| SDG 1 | No Poverty | Microfinance tech, rural livelihood, social entrepreneurship |
| SDG 2 | Zero Hunger | Precision agriculture, food supply chain, crop disease AI |
| SDG 3 | Good Health | Health informatics, medical devices, rural healthcare AI, mental health |
| SDG 4 | Quality Education | EdTech, learning analytics, access equity, NEP implementation |
| SDG 5 | Gender Equality | Workplace gender studies, women in STEM, safety tech |
| SDG 6 | Clean Water | Water quality sensors, wastewater treatment, IoT monitoring |
| SDG 7 | Clean Energy | Solar, wind, energy storage, smart grids, energy poverty |
| SDG 8 | Decent Work & Growth | Gig economy, skill development, Industry 4.0 employment |
| SDG 9 | Industry, Innovation, Infrastructure | Manufacturing 4.0, infrastructure resilience, startup ecosystems |
| SDG 10 | Reduced Inequalities | Disability tech, digital divide, social inclusion analytics |
| SDG 11 | Sustainable Cities | Smart cities, urban planning, traffic, waste management |
| SDG 12 | Responsible Consumption | Circular economy, e-waste, sustainable supply chains |
| SDG 13 | Climate Action | Carbon modelling, climate adaptation, disaster risk |
| SDG 14 | Life Below Water | Marine pollution, coastal management (less relevant for REVA) |
| SDG 15 | Life on Land | Biodiversity, forest monitoring, land use AI |
| SDG 16 | Peace, Justice, Institutions | Legal tech, e-governance, cybersecurity, anti-corruption |
| SDG 17 | Partnerships for Goals | Research collaboration, open data, international MoUs |

---

## SDG Impact Scoring Rubric

Rate each dimension 0–3 for the primary SDG:

| Dimension | 0 | 1 | 2 | 3 |
|-----------|---|---|---|---|
| **Problem Proximity** | Tangentially related | Addresses a sub-problem | Directly addresses the SDG challenge | Core SDG bottleneck solved |
| **Evidence Rigour** | Claim only | Anecdotal evidence | Quantitative indicators | Validated with SDG-aligned metrics |
| **Scale Potential** | Lab/theoretical | Local pilot | Regional applicability | National/global scalability |
| **Stakeholder Benefit** | Only researchers benefit | Narrow community | Broad demographic | Marginalised or vulnerable groups prioritised |

**Total Score /12**: 
- 10–12: High SDG impact — prominently feature in proposals and publications
- 6–9: Moderate impact — can be strengthened with specific pilot data
- 3–5: Low impact — consider reframing the problem or adding a community component
- 0–2: Negligible — do not claim SDG alignment without redesign

---

## India SDG Priority Alignment

India's VNR (Voluntary National Review) identifies these as priority focus areas:

1. **SDG 3 + SDG 1**: Health coverage and poverty elimination — especially in rural/semi-urban contexts
2. **SDG 4**: Foundational literacy, higher education access, vocational skilling (directly linked to NEP 2020)
3. **SDG 6 + SDG 7**: Clean water access and renewable energy — Karnataka-specific opportunities (solar, river systems)
4. **SDG 9**: Atmanirbhar Bharat — indigenous manufacturing, deep tech, semiconductor research
5. **SDG 11**: Smart Cities Mission — urban mobility, housing, digital services

---

## NEP 2020 Research Priority Areas

Beyond SDGs, NEP 2020 specifically prioritises:

- **Indian Knowledge Systems (IKS)**: Ayurveda, Yoga research, traditional mathematics, classical languages
- **Multidisciplinary Centres**: Research that crosses at least two disciplinary boundaries
- **Community Engagement**: Research that actively involves rural or tribal communities
- **Open Access**: Prioritise open-access publication and open datasets
- **Entrepreneurship**: Research with a startup or technology transfer pathway

---

## Output Format for SDG Tagging

When tagging any research work, produce:

```
**Primary SDG**: SDG [N] — [Name]
**Secondary SDGs**: SDG [N], SDG [N]
**SDG Impact Score**: [X]/12 — [High/Moderate/Low]
**India Priority Fit**: [Yes/Partial/No] — [which VNR priority]
**NEP 2020 Alignment**: [Yes/No] — [which NEP thrust]
**Strengthening Suggestion**: [one specific change to improve SDG alignment]
```
