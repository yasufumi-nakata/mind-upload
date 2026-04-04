---
title: "2026-04-04 site deepening audit: glossary bridge-witness split"
date: "2026-04-04"
author: "Codex"
---

# Summary

The selected weakness was a **terminology gap in the glossary around state-continuity language**.

By 2026-04-04, the public pages had already become stricter about a key stop line:

- `same-subject` is not yet `same-state`
- `same-brain` is not yet `same-state`
- `landmarks`, `latent manifolds`, `representational geometry`, and `fingerprint features` are not one bridge witness
- `alignment rescue` and `recalibration rescue` are not proof that the carried object stayed unchanged

However, the central term page, [`/Users/yasufumi/Documents/GitHub/mind-upload/glossary.md`](/Users/yasufumi/Documents/GitHub/mind-upload/glossary.md), still lacked short front-door definitions for those bridge-witness types.

That was not a cosmetic omission. It weakened the site's own reading discipline.

# Why This Needed Correction

## 1. The site already taught a stricter bridge rule than the glossary exposed

Recent public pages already used language such as:

- `State-Continuity Bridge Card`
- `same-state evidence`
- `landmarks`
- `latent manifolds`
- `representational geometry`
- `fingerprint features`
- `alignment`
- `recalibration`

But the glossary still stopped too early.

It defined the bridge card itself, yet not the main witness families that readers now need in order to interpret same-subject or same-brain claims correctly.

That created a practical failure mode:

- a reader could remember that `same-state evidence` is stricter
- but still have no short glossary definition explaining *why* one bridge witness is weaker or different than another

## 2. Primary literature does not support one generic `bridge witness`

- [Bosch et al. (2022)](https://doi.org/10.1038/s41467-022-30199-6) provide a correlative in vivo-to-structure workflow. That is a **specimen-linkage / correspondence** witness.
- [MICrONS Consortium et al. (2025)](https://doi.org/10.1038/s41586-025-08790-w) provide a **co-registered same-brain structure-function scaffold** with dense calcium imaging matched to later EM.
- [Gallego et al. (2020)](https://doi.org/10.1038/s41593-019-0555-4) show **stable latent population dynamics** underlying consistent behavior.
- [Guntupalli et al. (2016)](https://doi.org/10.1093/cercor/bhw068) show a **shared representational-space / geometry** witness through hyperalignment.
- [Van De Ville et al. (2021)](https://doi.org/10.1126/sciadv.abj0751) show that **brain fingerprints are time-scale dependent**.
- [Karpowicz et al. (2025)](https://doi.org/10.1038/s41467-025-59652-y) show that stable BCI use can depend on **alignment of latent dynamics**.
- [Wilson et al. (2025)](https://doi.org/10.1038/s41551-025-01536-z) show that long-term use can depend on **unsupervised recalibration** rather than one unchanged decoder relation.

Critique:

- co-registered landmarks are not the same object as stable latent dynamics
- stable latent dynamics are not the same object as preserved representational geometry
- representational geometry is not the same object as fingerprint identifiability
- alignment rescue is not the same object as recalibration rescue
- none of these, by themselves, automatically proves route-free continuity of the relevant hidden biological state

Therefore, a glossary that leaves them inside vague `same-subject / same-brain` language is scientifically weaker than the literature and weaker than the rest of the site.

## 3. The missing definitions mattered exactly where the site tries to prevent overclaiming

This project now relies on a specific stop line:

1. specimen identity is not enough
2. coordinate transfer is not enough
3. bridge witness type has to be named
4. rescue mechanism has to be named
5. only then can a claim ceiling be judged

If the glossary omits the witness types, it makes it easier to slide from:

- `same participant`
- `same brain`
- `same decoder family`
- `stable after alignment`

to:

- `same state was preserved`

The primary literature does not support that upgrade.

# Root Critique

The scientific criticism is therefore:

1. The site already had the correct bridge rule in the deeper pages.
2. The glossary still under-specified the witness objects needed to read that rule.
3. Current primary literature does not justify one generic continuity witness.
4. Therefore the glossary had to distinguish:
   - `same-subject / same-brain label`
   - `bridge witness`
   - `landmark / correspondence-point witness`
   - `latent-manifold witness`
   - `representational-space / geometry witness`
   - `fingerprint witness`
   - `alignment rescue`
   - `recalibration rescue`

# Web-Verified Primary Sources Checked On 2026-04-04

- Bosch et al. (2022), *Nature Communications*: https://doi.org/10.1038/s41467-022-30199-6
- MICrONS Consortium et al. (2025), *Nature*: https://doi.org/10.1038/s41586-025-08790-w
- Gallego et al. (2020), *Nature Neuroscience*: https://doi.org/10.1038/s41593-019-0555-4
- Guntupalli et al. (2016), *Cerebral Cortex*: https://doi.org/10.1093/cercor/bhw068
- Van De Ville et al. (2021), *Science Advances*: https://doi.org/10.1126/sciadv.abj0751
- Karpowicz et al. (2025), *Nature Communications*: https://doi.org/10.1038/s41467-025-59652-y
- Wilson et al. (2025), *Nature Biomedical Engineering*: https://doi.org/10.1038/s41551-025-01536-z

# Changes Executed In This Session

- Updated [`/Users/yasufumi/Documents/GitHub/mind-upload/glossary.md`](/Users/yasufumi/Documents/GitHub/mind-upload/glossary.md)
  - updated `last_updated` to `2026-04-04`
  - updated the page note / highlights / known points so the glossary now explicitly names the bridge-witness stop line
  - added a new note box explaining why `same-subject` and `same-brain` are not generic proof terms
  - added new glossary entries for:
    - `same-subject / same-brain label`
    - `bridge witness`
    - `landmark / correspondence-point witness`
    - `latent-manifold witness`
    - `representational-space / geometry witness`
    - `fingerprint witness`
    - `alignment rescue`
    - `recalibration rescue`

- Added [`/Users/yasufumi/Documents/GitHub/mind-upload/automation/site_deepening_audit_2026-04-04_glossary_bridge_witness_split.md`](/Users/yasufumi/Documents/GitHub/mind-upload/automation/site_deepening_audit_2026-04-04_glossary_bridge_witness_split.md)
  - records the criticism, rationale, and verified source trail for this correction

# Verification

- `git diff --check`
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
- `rg -n "bridge witness|latent-manifold witness|representational-space / geometry witness|alignment rescue|recalibration rescue" glossary.md _site/glossary.html`

# External Dependency Tasks

- None.
  - This run stayed inside executable repository work: literature verification, markdown edits, local static-site build, and Git publication.

# References

1. Bosch C, Ackels T, Pacureanu A, et al. Functional and multiscale 3D structural investigation of brain tissue through correlative in vivo physiology, synchrotron microtomography and volume electron microscopy. *Nature Communications*. 2022. https://doi.org/10.1038/s41467-022-30199-6
2. MICrONS Consortium, Bae JA, Lee W-CA, et al. Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*. 2025. https://doi.org/10.1038/s41586-025-08790-w
3. Gallego JA, Perich MG, Chowdhury RH, et al. Long-term stability of cortical population dynamics underlying consistent behavior. *Nature Neuroscience*. 2020. https://doi.org/10.1038/s41593-019-0555-4
4. Guntupalli JS, Hanke M, Halchenko YO, et al. A model of representational spaces in human cortex. *Cerebral Cortex*. 2016. https://doi.org/10.1093/cercor/bhw068
5. Van De Ville D, Farouj Y, Preti MG, Liégeois R, Amico E. When makes you unique: Temporality of the human brain fingerprint. *Science Advances*. 2021. https://doi.org/10.1126/sciadv.abj0751
6. Karpowicz BM, Ali YH, Wimalasena LN, et al. Stabilizing brain-computer interfaces through alignment of latent dynamics. *Nature Communications*. 2025. https://doi.org/10.1038/s41467-025-59652-y
7. Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. *Nature Biomedical Engineering*. 2025. https://doi.org/10.1038/s41551-025-01536-z
