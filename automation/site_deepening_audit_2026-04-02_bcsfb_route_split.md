---
title: "2026-04-02 site deepening audit: blood-CSF-barrier route split"
date: "2026-04-02"
author: "Codex"
---

# Summary

The selected weakness was not that the site lacked neurovascular literature. The weakness was that the public technical pages still undernamed one distinct human in vivo route family: `blood-CSF barrier / choroid-plexus perfusion / blood-to-CSF transport`. As long as that family stayed implicit, a careful reader could still overcompress three different objects into one bucket:

- `BBB water exchange`
- `tracer-specific BBB transport`
- `BCSFB / choroid-plexus / blood-to-CSF transport`

That compression was scientifically weaker than the site's own measurement logic. The primary papers do not support reading those routes as one common scalar.

# Why This Needed Correction

The stronger pages on this site already ask readers to name:

- the direct observable
- the crossed boundary
- the carrier class
- the model burden
- the validation ceiling

However, the neurovascular wording still made it too easy to read human choroid-plexus and blood-to-CSF studies as either `one more BBB paper` or `one more clearance paper`. That is not a harmless wording shortcut. It changes the claim class.

The blood-brain barrier and the blood-CSF barrier are not interchangeable biological interfaces. Even when both are probed with MRI-based water methods, they do not share one anatomy, one transport path, one observable, or one safe interpretation ceiling. A site that insists on route cards elsewhere should name that split explicitly here as well.

# Evidence-Based Critique

## 1. Zhao (2020) and Petitclerc (2021) do not describe generic BBB permeability

Zhao et al. (2020) measured apparent blood flow at the human choroid plexus with arterial spin labeling. Petitclerc et al. (2021) used ultra-long-TE arterial spin labeling to reveal rapid and brain-wide `blood-to-CSF water transport` in humans. Those observables are not the same object as cortical or gray-matter BBB water exchange.

Therefore, if the site mentions human BBB routes but leaves these papers unnamed, it encourages the wrong compression: it makes a choroid-plexus / blood-to-CSF readout look like a reusable BBB scalar. The papers do not justify that move.

## 2. Anderson (2022) and Wu (2026) show that BCSFB water cycling has its own acquisition and repeatability burden

Anderson et al. (2022) used DCE-MRI to study in vivo water cycling at the human choroid plexus. Wu et al. (2026) applied REXI to estimate water exchange across the BCSFB in healthy humans and reported scan-rescan repeatability metrics alongside an age effect. These are scientifically important because they show that the BCSFB route is measurable, but also because they show that the route comes with its own sequence-specific and model-specific burden.

That means the correct reading is not `human barrier transport is now measured`, full stop. The correct reading is `a distinct BCSFB route family is now measurable under bounded protocols`.

## 3. Petitclerc (2026) makes the split explicit inside one acquisition framework

Petitclerc et al. (2026) reported simultaneous measurement of water transport across the blood-brain and blood-CSF barriers in the human brain with arterial spin labeling MRI. This matters more than a mere extra citation. It directly demonstrates that the current frontier no longer treats BBB and BCSFB as one route by default, even when the acquisition family is shared.

Once that paper exists, any front door that still speaks only about `human BBB imaging` understates the route taxonomy now required by the literature itself.

## 4. Collapsing BCSFB into `clearance` is also incorrect

The site already tracks human clearance-side routes such as parenchyma-CSF exchange, intrathecal tracer retention, CSF mobility, and model-based biomarker efflux. But BCSFB / choroid-plexus transport is not reducible to those rows either. It sits at a different interface and should not be silently folded into a generic clearance-support lane.

The scientifically safe rule is stricter: `BBB water exchange`, `tracer BBB transport`, `BCSFB / choroid-plexus transport`, and `downstream clearance-side mobility or efflux` are separate route families unless a paper explicitly bridges them.

# Changes Executed In This Session

- Updated [`/Users/yasufumi/Documents/GitHub/mind-upload/wiki/homeostatic-plasticity-and-maintenance-state.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/homeostatic-plasticity-and-maintenance-state.md) so the neurovascular route card now explicitly includes `blood-CSF barrier / choroid-plexus transport`, adds a dedicated human observability row, and states that BBB and BCSFB papers do not measure one common controller object.
- Updated [`/Users/yasufumi/Documents/GitHub/mind-upload/wbe_101.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wbe_101.md) so the introduction now distinguishes BBB water exchange, tracer-specific BBB transport, and human BCSFB / choroid-plexus transport in the observability ladder and composition warnings.
- Updated [`/Users/yasufumi/Documents/GitHub/mind-upload/mind_uploading_papers.md`](/Users/yasufumi/Documents/GitHub/mind-upload/mind_uploading_papers.md) so the front-door technical addendum and route rows now treat the BCSFB / choroid-plexus literature as its own route family rather than a BBB or clearance footnote.

# Verification

- Rebuilt the static site with `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`.
- Ran `git diff --check`.
- Confirmed the new route-family labels appear in the built HTML for the edited pages.

# Resulting Rule

On this site, human neurovascular evidence should now be read as at least four distinct route families:

1. BBB water-exchange proxy
2. tracer-specific BBB transport proxy
3. blood-CSF barrier / choroid-plexus perfusion / blood-to-CSF transport proxy
4. clearance-side exchange / mobility / retention / efflux proxy

That rule does not make the literature weaker. It makes the claim ceiling honest.

# Primary References

1. Zhao MY, Mezue M, Segerdahl AR, et al. Non-invasive measurement of choroid plexus apparent blood flow with arterial spin labeling. *Fluids and Barriers of the CNS*. 2020.
   - https://doi.org/10.1186/s12987-020-00218-z
2. Petitclerc L, Hirschler L, Wells JA, et al. Ultra-long-TE arterial spin labeling reveals rapid and brain-wide blood-to-CSF water transport in humans. *NeuroImage*. 2021.
   - https://doi.org/10.1016/j.neuroimage.2021.118755
3. Anderson VC, Bouhrara M, Reiter DA, et al. DCE-MRI of Brain Fluid Barriers: In Vivo Water Cycling at the Human Choroid Plexus. *Fluids and Barriers of the CNS*. 2022.
   - https://doi.org/10.1080/21688370.2021.1963143
4. Morgan KNK, Tochon-Danguy H, Han M, et al. Measuring water exchange across the blood-brain barrier using diffusion-prepared arterial spin labelling in healthy volunteers and head and neck cancer patients. *NMR in Biomedicine*. 2024.
   - https://doi.org/10.1002/nbm.5256
5. Chung M, Choi S, Kim J, et al. Reduced blood-brain barrier penetration of urea in cognitively normal apolipoprotein E4 carriers. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-58356-7
6. Wu Z, Tarumi T, Martin-Cook K, et al. Age-related decline in water exchange across the blood-CSF barrier in humans. *Journal of Cerebral Blood Flow & Metabolism*. 2026.
   - https://doi.org/10.1177/0271678X251369218
7. Petitclerc L, Beqiri A, Chai YJ, et al. Simultaneous measurement of water transport across the blood-brain and blood-CSF barrier in the human brain with arterial spin labeling MRI. *Journal of Cerebral Blood Flow & Metabolism*. 2026.
   - https://doi.org/10.1177/0271678X261429042
