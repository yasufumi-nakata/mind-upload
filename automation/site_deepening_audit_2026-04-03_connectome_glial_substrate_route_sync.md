---
title: "2026-04-03 site deepening audit: central connectome page glial-substrate route sync"
date: "2026-04-03"
author: "Codex"
---

# Summary

The selected weakness was a **central-page taxonomy drift** inside [`wiki/connectome-is-not-enough.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/connectome-is-not-enough.md).

By 2026-04-03, the repository already treated `glial substrate-routing` as distinct from:

- neuronal `bioenergetic / mitochondrial state`
- `astrocyte-state`
- human macro energetic proxy routes
- human astrocyte-related PET routes

However, the central connectome page still lagged at the top layer. Its conclusion, main table, augmentation ladder, and reading rules still made it too easy to compress those objects back into one mixed `glial / energetic support` bucket.

# Why This Needed Correction

## 1. The central page contradicted the site's newer maintenance-state taxonomy

Before this run:

- the page still said `18 state classes and 1 putative wall`
- the main table had no independent `glial substrate-routing` row
- the maintenance-side addendum listed astrocyte / clearance / vascular rows but not glial substrate-routing
- the augmentation ladder had no `glial substrate-routing audit`
- the site rules still folded lactate support into `astrocyte-state`

That mismatch mattered because this page is the front door for the claim `connectome-complete is not emulation-complete`. If the front door keeps a category compressed that deeper pages already split, the reader relearns the weaker taxonomy.

## 2. Primary literature does not support one generic `glial support` object

- [Suzuki et al. (2011)](https://doi.org/10.1016/j.cell.2011.02.018) constrain a `lactate-shuttle support` route.
- [Silva et al. (2022)](https://doi.org/10.1038/s42255-022-00528-6) constrain a `glial ketogenesis / ketone-body export` route during starvation.
- [Pavlowsky et al. (2025)](https://doi.org/10.1038/s42255-025-01416-5) constrain an `intensive-learning glia-to-neuron fatty-acid` route.
- [Greda et al. (2025)](https://doi.org/10.1038/s42255-025-01389-5) constrain an `apoE / sortilin-dependent lipid-delivery and fuel-choice` route.
- [Qi et al. (2021)](https://doi.org/10.1016/j.celrep.2020.108572) show that even neuron-astrocyte fatty-acid coupling is genotype-sensitive.

Critique:

- These papers do not constrain one reusable `glial metabolism` scalar.
- They differ in supplier cell, neuronal sink, fuel object, and regime trigger.
- A central page that lacks a dedicated row teaches the wrong inferential object.

## 3. Astrocyte-state is a different causal family from glial fuel-routing

- [Cahill et al. (2024)](https://doi.org/10.1038/s41586-024-07311-5) constrain `minute-scale astrocyte-network encoding`.
- [Williamson et al. (2025)](https://doi.org/10.1038/s41586-024-08170-w) constrain `learning-associated astrocyte ensembles and recall`.
- [Dewa et al. (2025)](https://doi.org/10.1038/s41586-025-09619-2) constrain a `multiday astrocytic stabilization trace`.
- [Bukalo et al. (2026)](https://doi.org/10.1038/s41586-025-10068-0) constrain `amygdala astrocyte-enabled memory representations`.

Critique:

- Those papers do not identify the active lactate, ketone-body, fatty-acid, or apoE-lipid route.
- Conversely, fuel-routing papers do not fix astrocyte ensemble identity.
- The central page needed to stop collapsing those two families into one sentence.

## 4. Current human routes still stop below direct supplier-fuel-sink identification

- [Ren et al. (2015)](https://doi.org/10.1002/nbm.3384), [Ren et al. (2017)](https://doi.org/10.1002/mrm.26560), [Guo et al. (2024)](https://doi.org/10.3389/fnins.2024.1389111), [Kaiser et al. (2026)](https://doi.org/10.1177/0271678X261415784), [Karkouri et al. (2026)](https://doi.org/10.1002/mrm.70308), and [Li et al. (2025)](https://doi.org/10.1093/pnasnexus/pgaf072) constrain macro energetic quantity types.
- [Villemagne et al. (2022)](https://doi.org/10.2967/jnumed.121.263254), [Matsuoka et al. (2026)](https://doi.org/10.1007/s00259-025-07542-2), and [Tyacke et al. (2018)](https://doi.org/10.2967/jnumed.118.208009) constrain target-defined astrocyte-related PET routes.

Critique:

- Those are important observability advances, but they do not directly say which glial supplier delivered which fuel through which transport route to which neuronal sink.
- Therefore the central page needed a stronger human observability ceiling for `glial substrate-routing`.

# Changes Executed In This Session

- Updated [`/Users/yasufumi/Documents/GitHub/mind-upload/wiki/connectome-is-not-enough.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/connectome-is-not-enough.md)
  - raised the top-line count from `18` to `19 state classes`
  - added `glial substrate-routing` to front matter, highlights, known-points, and the conclusion paragraph
  - inserted a dedicated `Glial substrate-routing` row into the main table
  - added a new central-page section, `Glial substrate-routing is not generic astrocyte or energetic support`
  - added a human observability ceiling note that blocks overreading macro energetic imaging or astrocyte PET as supplier-fuel-sink truth
  - narrowed `astrocyte-state` so it now focuses on network / ensemble / representation families rather than lactate support
  - updated the augmentation ladder with a dedicated `+ glial substrate-routing audit`
  - updated reading rules and minimum-submission rules so omission of glial substrate-routing must now be stated explicitly
  - added the missing glial-routing and astrocyte-route references directly to the bibliography

# Verification

- Ran `ruby scripts/export_github_wiki.rb`.
- Ran `GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT=1 ruby scripts/check_github_wiki_export.rb`.
- Ran `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`.
- Ran `git diff --check`.
- Verified that `github-wiki-export/connectome-is-not-enough.md` and `_site/wiki/connectome-is-not-enough.html` now contain:
  - `19 state classes`
  - the new `Glial substrate-routing` row
  - the dedicated `+ glial substrate-routing audit`
  - supplier-fuel-sink wording in the human observability ceiling

# External Dependency Tasks

- None.
  - This run stays inside executable repository work: literature-backed markdown edits, local verification, wiki export checks, and Git publication.

# References

1. Suzuki A, Stern SA, Bozdagi O, et al. Astrocyte-neuron lactate transport is required for long-term memory formation. *Cell*. 2011.
   - https://doi.org/10.1016/j.cell.2011.02.018
2. Silva B, et al. Glial ketogenesis regulates memory maintenance during starvation. *Nature Metabolism*. 2022.
   - https://doi.org/10.1038/s42255-022-00528-6
3. Qi G, Mi Y, Shi X, Gu H, Brinton RD, Yin F. ApoE4 impairs neuron-astrocyte coupling of fatty acid metabolism. *Cell Reports*. 2021.
   - https://doi.org/10.1016/j.celrep.2020.108572
4. Pavlowsky A, et al. Neuronal fatty acid oxidation fuels memory after intensive learning in Drosophila. *Nature Metabolism*. 2025.
   - https://doi.org/10.1038/s42255-025-01416-5
5. Greda AK, et al. Interaction of sortilin with apolipoprotein E3 enables neurons to use long-chain fatty acids as alternative metabolic fuel. *Nature Metabolism*. 2025.
   - https://doi.org/10.1038/s42255-025-01389-5
6. Ren J, Sherry AD, Malloy CR. 31P-MRS of healthy human brain: ATP synthesis, metabolite concentrations, pH, and T1 relaxation times. *NMR in Biomedicine*. 2015.
   - https://doi.org/10.1002/nbm.3384
7. Ren J, Sherry AD, Malloy CR. Efficient 31P band inversion transfer approach for measuring creatine kinase activity, ATP synthesis, and molecular dynamics in the human brain at 7 T. *Magnetic Resonance in Medicine*. 2017.
   - https://doi.org/10.1002/mrm.26560
8. Guo R, et al. Mapping intracellular NAD content in entire human brain using phosphorus-31 MR spectroscopic imaging at 7 Tesla. *Frontiers in Neuroscience*. 2024.
   - https://doi.org/10.3389/fnins.2024.1389111
9. Kaiser A, et al. Ultra-high field 31P functional magnetic resonance spectroscopy reveals NAD+ dynamics in brain energy metabolism during visual stimulation. *Journal of Cerebral Blood Flow & Metabolism*. 2026.
   - https://doi.org/10.1177/0271678X261415784
10. Karkouri J, et al. Quantification of deuterated metabolite concentrations and rates in the human brain from dynamic deuterium metabolic imaging at 7 T. *Magnetic Resonance in Medicine*. 2026.
    - https://doi.org/10.1002/mrm.70308
11. Li X, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025.
    - https://doi.org/10.1093/pnasnexus/pgaf072
12. Villemagne VL, Harada R, Dore V, et al. First-in-Humans Evaluation of 18F-SMBT-1, a Novel 18F-Labeled Monoamine Oxidase-B PET Tracer for Imaging Reactive Astrogliosis. *Journal of Nuclear Medicine*. 2022.
    - https://doi.org/10.2967/jnumed.121.263254
13. Matsuoka K, Takado Y, Kimura Y, et al. Quantification of monoamine oxidase B expression with 11C-SL25.1188 for imaging reactive astrocytes in patients with Alzheimer's disease. *European Journal of Nuclear Medicine and Molecular Imaging*. 2026.
    - https://doi.org/10.1007/s00259-025-07542-2
14. Tyacke RJ, Myers JFM, Venkataraman A, et al. Evaluation of 11C-BU99008, a PET ligand for the imidazoline2 binding site in human brain. *Journal of Nuclear Medicine*. 2018.
    - https://doi.org/10.2967/jnumed.118.208009
15. Cahill MK, et al. Network-level encoding of local neurotransmitters in cortical astrocytes. *Nature*. 2024.
    - https://doi.org/10.1038/s41586-024-07311-5
16. Williamson NR, et al. Learning-associated astrocyte ensembles regulate memory recall. *Nature*. 2025.
    - https://doi.org/10.1038/s41586-024-08170-w
17. Dewa K, et al. The astrocytic ensemble acts as a multiday trace to stabilize memory. *Nature*. 2025.
    - https://doi.org/10.1038/s41586-025-09619-2
18. Bukalo O, et al. Astrocytes enable amygdala neural representations supporting memory. *Nature*. 2026.
    - https://doi.org/10.1038/s41586-025-10068-0
