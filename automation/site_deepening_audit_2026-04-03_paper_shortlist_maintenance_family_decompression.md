# Site Deepening Audit (2026-04-03, paper shortlist maintenance-family decompression)

## Target

- Main public page:
  - `mind_uploading_papers.md`
- Scope:
  - Technology
  - Natural science
- Explicitly excluded:
  - Philosophy
  - Law

## Summary

- The next unresolved weakness on the paper-archive front door was still a summary-layer compression problem.
- `mind_uploading_papers.md` already had detailed note boxes and downstream route cards distinguishing molecular, matrix, metabolic, vascular, immune, and astrocyte maintenance families.
- However, the high-visibility `2025-2026 technical-only shortlist` still presented those families through one broad row, which made the archive entrance scientifically looser than the detailed body of the same page.
- I therefore chose that shortlist row as the next page element to deepen and decompressed it into five narrower maintenance-family rows:
  - excitability / perturbation
  - RNA / phospho / proteostasis / cargo
  - ECM / PNN gate
  - bioenergetic / glial substrate-routing
  - neurovascular / immune / astrocyte

## Why This Needed Correction

### 1. The shortlist still lagged behind the page's own deeper reading rules

- The detailed note boxes on the same page already distinguished:
  - ECM / PNN route families
  - phospho-signaling / second-messenger route families
  - human clearance route families
  - neuroimmune PET route families
  - neurovascular / BBB / pericyte support
  - astrocyte multiday-trace and representation-support routes
- But the shortlist, which is the actual fast-entry surface for a technical reader, still compressed those families into one `Maintenance-state family split` row.

Critique:

- This was internally inconsistent.
- The page taught a strong route-family rule in the notes, then taught a weaker summary model at the entrance layer.
- A reader using only the shortlist could still leave with the incorrect impression that `maintenance-state` is one broad latent variable with a few example papers attached.

### 2. The old row hid molecular maintenance families behind prose instead of citations

- The old shortlist row mentioned RNA control, phospho-signaling, proteostasis, and cargo-routing in prose, but did not anchor those families with their own front-door citations.
- The page already had supporting literature for that split:
  - [Shi et al. (2018)](https://doi.org/10.1038/s41586-018-0666-1) for m6A-dependent translation control in memory
  - [Peterson et al. (2025)](https://doi.org/10.1126/scisignal.adr1442) for ADAR2-mediated GluA2 RNA-editing control in homeostatic synaptic plasticity
  - [Vierra et al. (2023)](https://doi.org/10.1038/s41467-023-40930-6) for compartmentalized Ca2+-activated PKA / signalosome routing
  - [Pandey et al. (2021)](https://doi.org/10.1080/15548627.2020.1775393) for learning-coupled autophagy / proteostasis
  - [Aiken & Holzbaur (2024)](https://doi.org/10.1016/j.cub.2024.03.010) for presynaptic cargo-delivery patterning

Critique:

- If a family is important enough to appear in the criticism, it is important enough to appear in the shortlist citations.
- Leaving those families unanchored at the front door made the shortlist easier to overread than the evidence base warranted.

### 3. ECM, metabolic support, and vascular / immune / astrocyte support do not share one claim ceiling

- [Alexander et al. (2025)](https://doi.org/10.1523/JNEUROSCI.1626-24.2024) and [Mehak et al. (2025)](https://doi.org/10.1111/acel.70139) constrain matrix-side gating routes.
- [Vishwanath et al. (2026)](https://doi.org/10.1038/s42255-026-01451-w), [Suzuki et al. (2011)](https://doi.org/10.1016/j.cell.2011.02.018), [Silva et al. (2022)](https://doi.org/10.1038/s42255-022-00528-6), [Pavlowsky et al. (2025)](https://doi.org/10.1038/s42255-025-01416-5), and [Greda et al. (2025)](https://doi.org/10.1038/s42255-025-01389-5) constrain metabolic or glial supplier-fuel routing.
- [Bell et al. (2010)](https://doi.org/10.1016/j.neuron.2010.09.043), [Kisler et al. (2020)](https://doi.org/10.3389/fncel.2020.00027), [Pandey et al. (2023)](https://doi.org/10.1016/j.neuron.2023.08.030), [Swissa et al. (2024)](https://doi.org/10.7554/eLife.89611), [Mai-Morente et al. (2025)](https://doi.org/10.1038/s41467-025-61312-0), [Kim et al. (2025)](https://doi.org/10.1016/j.cell.2025.02.022), [Dewa et al. (2025)](https://doi.org/10.1038/s41586-025-09619-2), and [Bukalo et al. (2026)](https://doi.org/10.1038/s41586-025-10068-0) constrain vascular, immune, lymphatic-microglial, or astrocytic support families.

Critique:

- Those families do not share one inferential object.
- They do not share one observability ceiling.
- They do not license the same shortcut from `support-related paper exists` to `hidden-state closure is getting close`.
- A single shortlist row therefore overstated conceptual uniformity exactly where the page is supposed to prevent it.

### 4. Excitability-side evidence also needed to be isolated from the other maintenance families

- [Hadzibegovic et al. (2025)](https://doi.org/10.1038/s41467-025-66975-3) constrains early intrinsic-excitability plasticity in neocortical engram formation.
- [Benoit et al. (2025)](https://doi.org/10.1038/s41593-025-02152-5), [Hengen et al. (2016)](https://doi.org/10.1016/j.cell.2016.01.046), [Tallman et al. (2025)](https://doi.org/10.1038/s41598-025-21967-7), [Huber et al. (2013)](https://doi.org/10.1093/cercor/bhs014), [Kuhn et al. (2016)](https://doi.org/10.1038/ncomms12455), [Zrenner et al. (2018)](https://doi.org/10.1016/j.brs.2017.11.016), [Khatri et al. (2025)](https://doi.org/10.1016/j.brs.2024.12.1193), [Fehér et al. (2026)](https://doi.org/10.1016/j.neuroimage.2026.121723), and [Alfonsa et al. (2025)](https://doi.org/10.1016/j.cub.2025.01.050) constrain AIS / channel-state, homeostatic set-point, sleep-homeostasis proxy, perturbation-window, or chloride-gating routes.

Critique:

- This family already differs mechanistically from RNA control, matrix gating, or glial supplier support.
- Keeping it in the same shortlist cell weakened the site's own `which controller family moved?` rule.

## Changes Executed In This Session

- `mind_uploading_papers.md`
  - Replaced the single `Maintenance-state family split` shortlist row with five narrower rows.
  - Added explicit front-door citations for molecular maintenance families that were previously mentioned only in prose.
  - Separated ECM / PNN gating from metabolic / glial substrate-routing.
  - Separated neurovascular / immune / astrocyte support from the other maintenance families.
  - Updated the page note so the front matter records the new maintenance-shortlist decomposition.

- `automation/site_deepening_audit_2026-04-03_paper_shortlist_maintenance_family_decompression.md`
  - Added this audit note to preserve the criticism, rationale, and reference trail behind the shortlist revision.

## Verification

- `git diff --check`
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
- `rg -n "Excitability / perturbation split|RNA / phospho / proteostasis / cargo split|ECM / PNN gate split|Bioenergetic / glial substrate-routing split|Neurovascular / immune / astrocyte split" mind_uploading_papers.md _site/mind_uploading_papers.html`

## External Dependency Tasks

- None.
  - This session covered literature checking, repository edits, build verification, and Git publication entirely within the current environment.

## References

1. Hadzibegovic N, Zhu L, Ginger M, et al. Early intrinsic excitability plasticity of neocortical engram neurons defines memory formation and precision. *Nature Communications*. 2025. https://doi.org/10.1038/s41467-025-66975-3
2. Shi H, Zhang X, Weng Y-L, et al. m6A facilitates hippocampus-dependent learning and memory through YTHDF1. *Nature*. 2018. https://doi.org/10.1038/s41586-018-0666-1
3. Peterson LN, Kasper JM, Allgaier JA, et al. ADAR2-mediated Q/R editing of GluA2 in homeostatic synaptic plasticity. *Science Signaling*. 2025. https://doi.org/10.1126/scisignal.adr1442
4. Vierra NC, et al. Neuronal ER-plasma membrane junctions couple excitation to Ca2+-activated PKA signaling. *Nature Communications*. 2023. https://doi.org/10.1038/s41467-023-40930-6
5. Pandey K, Yu X-W, Steinmetz A, Alberini CM. Autophagy coupled to translation is required for long-term memory formation. *Autophagy*. 2021. https://doi.org/10.1080/15548627.2020.1775393
6. Aiken J, Holzbaur ELF. Spastin locally amplifies microtubule dynamics to pattern the axon for presynaptic cargo delivery. *Current Biology*. 2024. https://doi.org/10.1016/j.cub.2024.03.010
7. Alexander et al. Perineuronal Nets on CA2 Pyramidal Cells and Parvalbumin-Expressing Cells Differentially Regulate Hippocampal-Dependent Memory. *Journal of Neuroscience*. 2024. https://doi.org/10.1523/JNEUROSCI.1626-24.2024
8. Mehak et al. Targeting CA2 Perineuronal Nets Restores Recognition Memory and Theta Oscillations in Aged Mice. *Aging Cell*. 2025. https://doi.org/10.1111/acel.70139
9. Vishwanath AA, Comyn T, Mira RG, et al. Mitochondrial Ca2+ efflux controls neuronal metabolism and long-term memory across species. *Nature Metabolism*. 2026. https://doi.org/10.1038/s42255-026-01451-w
10. Suzuki A, Stern SA, Bozdagi O, et al. Astrocyte-neuron lactate transport is required for long-term memory formation. *Cell*. 2011. https://doi.org/10.1016/j.cell.2011.02.018
11. Silva et al. Glia fuel neurons with locally synthesized ketone bodies to sustain memory under starvation. *Nature Metabolism*. 2022. https://doi.org/10.1038/s42255-022-00528-6
12. Pavlowsky et al. Neuronal fatty acid oxidation fuels memory after intensive learning in Drosophila. *Nature Metabolism*. 2025. https://doi.org/10.1038/s42255-025-01416-5
13. Greda et al. Interaction of sortilin with apolipoprotein E3 enables neurons to use long-chain fatty acids as alternative metabolic fuel. *Nature Metabolism*. 2025. https://doi.org/10.1038/s42255-025-01389-5
14. Bell RD, et al. Pericytes control key neurovascular functions and neuronal phenotype in the adult brain. *Neuron*. 2010. https://doi.org/10.1016/j.neuron.2010.09.043
15. Kisler K, Nelson AR, Montagne A, Zlokovic BV. Cerebral blood flow regulation and neurovascular dysfunction in Alzheimer disease. *Frontiers in Cellular Neuroscience*. 2020. https://doi.org/10.3389/fncel.2020.00027
16. Pandey et al. Neuronal activity drives IGF2 expression from pericytes to form long-term memory. *Neuron*. 2023. https://doi.org/10.1016/j.neuron.2023.08.030
17. Swissa et al. Cortical plasticity is associated with blood–brain barrier modulation. *eLife*. 2024. https://doi.org/10.7554/eLife.89611
18. Mai-Morente et al. Pericyte pannexin1 controls cerebral capillary diameter and supports memory function. *Nature Communications*. 2025. https://doi.org/10.1038/s41467-025-61312-0
19. Kim et al. Meningeal lymphatics-microglia axis regulates synaptic physiology. *Cell*. 2025. https://doi.org/10.1016/j.cell.2025.02.022
20. Dewa K, et al. The astrocytic ensemble acts as a multiday trace to stabilize memory. *Nature*. 2025. https://doi.org/10.1038/s41586-025-09619-2
21. Bukalo O, et al. Astrocytes enable amygdala neural representations supporting memory. *Nature*. 2026. https://doi.org/10.1038/s41586-025-10068-0
