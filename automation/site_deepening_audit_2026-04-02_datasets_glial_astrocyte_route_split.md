---
title: "2026-04-02 site deepening audit: datasets glial-substrate and astrocyte route split"
date: "2026-04-02"
author: "Codex"
---

# Summary

The selected weakness was inside the public practical page [`datasets.md`](/Users/yasufumi/Documents/GitHub/mind-upload/datasets.md). The page already had a useful component-addition / ablation ladder for maintenance-state routes, but one row still compressed `astrocyte-state` and `glial substrate-routing` into a single `Astrocyte / glial route`.

That compression was technically unstable because the rest of the site had already adopted the opposite rule:

- `astrocyte-state` is a distinct family from `glial substrate-routing`
- `astrocyte-state` is a distinct family from `clearance / immune support`
- `glial substrate-routing` is a distinct family from generic energetic support

If the practical entry page keeps those families fused, the site reintroduces exactly the category mistake that its central theory and verification pages are designed to stop.

# Why This Topic Was Chosen

`datasets.md` is not only a resource list. It is the page that teaches readers how to turn a reproducible neuron-first baseline into a stronger multimodal claim. That makes its route taxonomy operationally important.

The page had already become much stricter about:

- neuron-first baseline versus support-state augmentation
- strongest-single-row versus full-bundle comparison
- missingness / common-driver / disagreement audits

However, the first row in the augmentation ladder still implied that one dataset design could stand in equally for:

- astrocyte ensemble state
- glia-to-neuron fuel routing

The primary literature does not support that equivalence.

# Evidence-Based Critique

## 1. Astrocyte-state and glial substrate-routing do not share one direct observable

The recent astrocyte literature is not mainly about fuel class or supplier-sink identity.

- Cahill et al. (2024, DOI `10.1038/s41586-024-07311-5`) showed that local neurotransmitter inputs are encoded by broad cortical astrocyte networks over a minutes-long timescale.
- Williamson et al. (2025, DOI `10.1038/s41586-024-08170-w`) showed that learning-associated astrocyte ensembles regulate memory recall.
- Dewa et al. (2025, DOI `10.1038/s41586-025-09619-2`) showed an astrocytic ensemble acting as a multiday trace that stabilizes labile memory.
- Bukalo et al. (2026, DOI `10.1038/s41586-025-10068-0`) showed that astrocytes support amygdala neural representations linked to memory.

These papers constrain astrocyte ensemble identity, network-scale Ca2+-linked signaling, recall support, and multiday stabilization. They do not define one supplier cell / neuronal sink / carrier object route.

## 2. Glial substrate-routing is a different family with different regime logic

The glial substrate-routing literature is not about astrocyte ensembles in the same sense. It is about fuel-transfer pathways and nutrient-regime logic.

- Suzuki et al. (2011, DOI `10.1016/j.cell.2011.02.018`) established an astrocyte-neuron lactate transport route required for long-term memory formation.
- Silva et al. (2022, DOI `10.1038/s42255-022-00528-6`) established a glial ketogenesis / ketone-body route during starvation.
- Pavlowsky et al. (2025, DOI `10.1038/s42255-025-01416-5`) established a learning-linked fatty-acid route after intensive learning.
- Greda et al. (2025, DOI `10.1038/s42255-025-01389-5`) established an apoE / sortilin-dependent lipid-delivery route that changes neuronal fuel choice when glucose is limited.

These papers do not share one fuel object, one carrier, one supplier-sink relation, or one regime trigger. Compressing them into `Astrocyte / glial route` silently removes exactly the route-defining fields that a practical augmentation design needs.

## 3. The old row created the wrong minimum-data rule

The previous dataset-ladder row asked for:

- a named astrocyte observable or perturbation

That requirement fits `astrocyte-state` papers, but it does not fit `glial substrate-routing` papers, which additionally require:

- supplier cell
- neuronal sink
- fuel object / carrier
- nutrient or learning regime

So the old row did not merely simplify wording. It prescribed the wrong practical evidence fields for one of the two families.

## 4. The old stop line was also wrong

The previous stop line warned against overclaiming a whole-brain astrocyte controller or generalizing one glial effect across timescales. That warning was useful, but incomplete. It still allowed a reader to miss that:

- astrocyte-state evidence does not identify fuel-routing identity
- glial fuel-routing evidence does not identify astrocyte ensemble state

For a public practical page, that missing split matters because it affects how a reader designs augmentation data, perturbations, and abstention boundaries.

# Changes Executed In This Session

- Updated [`datasets.md`](/Users/yasufumi/Documents/GitHub/mind-upload/datasets.md) front matter so the page highlights now state that the maintenance-state ladder separates `glial substrate-routing` from `astrocyte-state`.
- Added a new `known_points` bullet stating directly that astrocyte observables do not fix supplier cell / neuronal sink / fuel object, and that glial fuel-support routes do not by themselves identify astrocyte ensembles.
- Rewrote the practical note box before the augmentation ladder so it now cites distinct astrocyte-state papers and distinct glial substrate-routing papers rather than one generic glial-support bucket.
- Replaced the old single `Astrocyte / glial route` row in the practical ladder with two rows:
  - `Glial substrate-routing route`
  - `Astrocyte-state route`
- Rewrote the starter-dataset warning so it now keeps `glial substrate-routing` and `astrocyte-state` separate in the public practical stop line.
- Added the missing primary references for Cahill, Suzuki, Silva, Pavlowsky, and Greda to the bibliography.

# Why The New Split Is Better

The new ladder now matches the actual scientific objects:

- `Astrocyte-state route`
  - asks for astrocyte observables / perturbations aligned to recall, stabilization, or fear-state windows
- `Glial substrate-routing route`
  - asks for supplier-sink-fuel fields aligned to nutrient or learning regime

That makes the practical page consistent with the site's broader rule that maintenance-state families should be split by direct observable, regime, and claim ceiling before bundle promotion is judged.

# Verification

- Rebuilt generated summary content with `ruby scripts/build_summary_booklet.rb`.
- Rebuilt the static site with `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`.
- Ran `git diff --check`.
- Confirmed the new route labels appear in `_site/datasets.html`.

# External Dependency Tasks

- None.
  - The work in this session was fully executable as literature review, repository edits, local generation, verification, and Git operations.

# Primary References

1. Cahill MK, Collard M, Tse V, et al. Network-level encoding of local neurotransmitters in cortical astrocytes. *Nature*. 2024.
   - https://doi.org/10.1038/s41586-024-07311-5
2. Williamson MR, Kwon W, Woo J, et al. Learning-associated astrocyte ensembles regulate memory recall. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-024-08170-w
3. Dewa K, Kaseda K, Kuwahara A, et al. The astrocytic ensemble acts as a multiday trace to stabilize memory. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-09619-2
4. Bukalo O, O'Sullivan R, Tanisumi Y, et al. Astrocytes enable amygdala neural representations supporting memory. *Nature*. 2026.
   - https://doi.org/10.1038/s41586-025-10068-0
5. Suzuki A, Stern SA, Bozdagi O, et al. Astrocyte-neuron lactate transport is required for long-term memory formation. *Cell*. 2011.
   - https://doi.org/10.1016/j.cell.2011.02.018
6. Silva B, Mantha OL, Schor J, et al. Glial ketogenesis regulates memory maintenance during starvation. *Nature Metabolism*. 2022.
   - https://doi.org/10.1038/s42255-022-00528-6
7. Pavlowsky A, et al. Neuronal fatty acid oxidation fuels memory after intensive learning in Drosophila. *Nature Metabolism*. 2025.
   - https://doi.org/10.1038/s42255-025-01416-5
8. Greda AK, et al. Interaction of sortilin with apolipoprotein E3 enables neurons to use long-chain fatty acids as alternative metabolic fuel. *Nature Metabolism*. 2025.
   - https://doi.org/10.1038/s42255-025-01389-5
9. Mai-Morente S, Isasi E, Rafael A, et al. Pericyte pannexin1 controls cerebral capillary diameter and supports memory function. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-61312-0
10. Kim K, Abramishvili D, Du S, et al. Meningeal lymphatics-microglia axis regulates synaptic physiology. *Cell*. 2025.
    - https://doi.org/10.1016/j.cell.2025.02.022
11. Hirschler L, Runderkamp BAR, Decker A, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nature Neuroscience*. 2025.
    - https://doi.org/10.1038/s41593-025-02073-3
12. Chung KJ, Abdelhafez YG, Spencer BA, et al. Quantitative PET imaging and modeling of molecular blood-brain barrier permeability. *Nature Communications*. 2025.
    - https://doi.org/10.1038/s41467-025-58356-7
13. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026.
    - https://doi.org/10.1038/s41467-026-68374-8
