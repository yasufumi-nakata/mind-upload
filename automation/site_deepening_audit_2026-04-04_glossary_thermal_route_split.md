---
title: "2026-04-04 site deepening audit: glossary thermal-route split"
date: "2026-04-04"
author: "Codex"
---

# Summary

The selected weakness was a **terminology gap around thermal-state language in the glossary**.

By 2026-04-04, the deeper public pages already treated thermal evidence as a split family:

- local operating-point physiology
- field-potential confound
- sequence / rhythm perturbation
- device- or preparation-linked heating / cooling artifact
- brain-state proxy route
- human passive / task-linked macro thermometry
- human perturbation-conditioned thermal routes

However, the front-door term page, [`/Users/yasufumi/Documents/GitHub/mind-upload/glossary.md`](/Users/yasufumi/Documents/GitHub/mind-upload/glossary.md), still exposed only a short single-line `Thermal-state` definition.

That was scientifically too weak for the site's current standard.

# Why This Needed Correction

## 1. The glossary was behind the site's own stronger public rule

Recent public pages already used a stricter thermal stop line:

- thermal-state is not timing-state
- thermal-state is not bioenergetic-state
- human thermometry is not one route
- perturbation-conditioned human thermal work is not the same object as passive or task-linked thermometry
- heating artifacts and field-potential thermal confounds are not evidence of the intended neural mechanism

The glossary did not yet expose those distinctions at the term level.

That created a practical reading failure:

- a reader could learn from `index.md`, `faq.md`, `verification.md`, or the homeostatic wiki that thermal evidence is split
- but still return to the glossary and find only one compressed thermal label

That mismatch weakens the site's own front-door discipline.

## 2. Primary literature does not support one generic `thermal evidence` bucket

- [Hardingham & Larkman (1998)](https://doi.org/10.1111/j.1469-7793.1998.249bu.x) and [Volgushev et al. (2000)](https://doi.org/10.1111/j.1469-7793.2000.00059.x) constrain **temperature-dependent synaptic / membrane operating point**.
- [Moser et al. (1993)](https://doi.org/10.1126/science.8446900) constrains a **field-potential confound**.
- [Long & Fee (2008)](https://doi.org/10.1038/nature07448) constrains **sequence-timing perturbation under cooling**.
- [Owen et al. (2019)](https://doi.org/10.1038/s41593-019-0422-3) and [Boorman et al. (2023)](https://doi.org/10.1038/s42003-023-04542-6) constrain **device- or preparation-linked heating / cooling burden**.
- [Lazopulo et al. (2025)](https://doi.org/10.1038/s41598-025-21175-3) constrains a **brain-state proxy route** rather than a local controller readout.
- [Rzechorzek et al. (2022)](https://doi.org/10.1093/brain/awab466), [Rogala et al. (2024)](https://doi.org/10.3389/fnhum.2024.1398034), and [Tan et al. (2025)](https://doi.org/10.1007/s00062-024-01467-3) constrain **human passive / task-linked macro thermometry**.
- [Tan et al. (2024)](https://doi.org/10.1016/j.jshs.2023.09.001) and [Inoue et al. (2025)](https://doi.org/10.1016/j.clinph.2025.02.262) constrain **human perturbation-conditioned thermal routes**.

These papers do not share one direct observable, one spatial unit, one intervention regime, one model burden, or one human observability ceiling.

Therefore, a glossary that leaves them under one generic thermal label is weaker than the literature and weaker than the rest of the site.

## 3. The missing split matters exactly where the site tries to prevent overclaiming

If thermal language stays compressed, readers can slide too easily from:

- `temperature matters`
- `brain temperature can be measured`
- `thermal perturbation changes physiology`

to:

- `local thermal-state is now effectively observed`

The current primary literature does not justify that upgrade.

Current human routes still stop at macro thermometry or perturbation-conditioned sensitivity, not cell-specific microtemperature, synapse-specific heating burden, or local thermal-controller identity.

# Root Critique

The scientific criticism is therefore:

1. The site already had the correct thermal split in deeper pages.
2. The glossary still compressed that split into one minimal term.
3. Current primary literature does not support one generic `thermal evidence` object.
4. Therefore the glossary had to distinguish:
   - `Thermal-state`
   - `Thermal route card`
   - `Field-potential thermal confound`
   - `Device- or preparation-linked heating artifact`
   - `Brain-state proxy route`
   - `Human passive / task-linked macro thermometry`
   - `Human perturbation-conditioned thermal route`

# Web-Verified Primary Sources Checked On 2026-04-04

- Hardingham & Larkman (1998), *The Journal of Physiology*: https://doi.org/10.1111/j.1469-7793.1998.249bu.x
- Volgushev et al. (2000), *The Journal of Physiology*: https://doi.org/10.1111/j.1469-7793.2000.00059.x
- Moser et al. (1993), *Science*: https://doi.org/10.1126/science.8446900
- Long & Fee (2008), *Nature*: https://doi.org/10.1038/nature07448
- Owen et al. (2019), *Nature Neuroscience*: https://doi.org/10.1038/s41593-019-0422-3
- Boorman et al. (2023), *Communications Biology*: https://doi.org/10.1038/s42003-023-04542-6
- Rzechorzek et al. (2022), *Brain*: https://doi.org/10.1093/brain/awab466
- Rogala et al. (2024), *Frontiers in Human Neuroscience*: https://doi.org/10.3389/fnhum.2024.1398034
- Tan et al. (2024), *Journal of Sport and Health Science*: https://doi.org/10.1016/j.jshs.2023.09.001
- Tan et al. (2025), *Clinical Neuroradiology*: https://doi.org/10.1007/s00062-024-01467-3
- Inoue et al. (2025), *Clinical Neurophysiology*: https://doi.org/10.1016/j.clinph.2025.02.262
- Lazopulo et al. (2025), *Scientific Reports*: https://doi.org/10.1038/s41598-025-21175-3

# Changes Executed In This Session

- Updated [`/Users/yasufumi/Documents/GitHub/mind-upload/glossary.md`](/Users/yasufumi/Documents/GitHub/mind-upload/glossary.md)
  - updated the page note / highlights / known points so the thermal stop line is explicit at the front door
  - added a new note box explaining why `thermal-state` is not one interchangeable meter
  - expanded the existing `Thermal-state` definition
  - added new glossary entries for:
    - `Thermal route card`
    - `Field-potential thermal confound`
    - `Device- or preparation-linked heating artifact`
    - `Brain-state proxy route`
    - `Human passive / task-linked macro thermometry`
    - `Human perturbation-conditioned thermal route`
  - added the thermal literature needed to support those glossary definitions

- Added [`/Users/yasufumi/Documents/GitHub/mind-upload/automation/site_deepening_audit_2026-04-04_glossary_thermal_route_split.md`](/Users/yasufumi/Documents/GitHub/mind-upload/automation/site_deepening_audit_2026-04-04_glossary_thermal_route_split.md)
  - records the criticism, source trail, and why this was a scientific correction rather than a cosmetic rewrite

# Verification

- `git diff --check`
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
- `rg -n "Thermal route card|Field-potential thermal confound|Human passive / task-linked macro thermometry|Human perturbation-conditioned thermal route" glossary.md _site/glossary.html`

# External Dependency Tasks

- None.
  - This run stayed inside executable repository work: literature verification, markdown edits, static-site build, and Git publication.

# References

1. Hardingham NR, Larkman AU. The reliability of excitatory synaptic transmission in slices of rat visual cortex in vitro is temperature dependent. *The Journal of Physiology*. 1998. https://doi.org/10.1111/j.1469-7793.1998.249bu.x
2. Volgushev M, Vidyasagar TR, Chistiakova M, Yousef T, Eysel UT. Membrane properties and spike generation in rat visual cortical cells during reversible cooling. *The Journal of Physiology*. 2000. https://doi.org/10.1111/j.1469-7793.2000.00059.x
3. Moser E, Mathiesen I, Andersen P. Association between brain temperature and dentate field potentials in exploring and swimming rats. *Science*. 1993. https://doi.org/10.1126/science.8446900
4. Long MA, Fee MS. Using temperature to analyse temporal dynamics in the songbird motor pathway. *Nature*. 2008. https://doi.org/10.1038/nature07448
5. Owen SF, Liu MH, Kreitzer AC. Thermal constraints on in vivo optogenetic manipulations. *Nature Neuroscience*. 2019. https://doi.org/10.1038/s41593-019-0422-3
6. Boorman LW, Harris SS, Shabir O, et al. Bidirectional alterations in brain temperature profoundly modulate spatiotemporal neurovascular responses in-vivo. *Communications Biology*. 2023. https://doi.org/10.1038/s42003-023-04542-6
7. Rzechorzek NM, Thrippleton MJ, Chappell FM, et al. A daily temperature rhythm in the human brain predicts survival after brain injury. *Brain*. 2022. https://doi.org/10.1093/brain/awab466
8. Rogala J, Dreszer J, Sińczuk M, et al. Local variation in brain temperature explains gender-specificity of working memory performance. *Frontiers in Human Neuroscience*. 2024. https://doi.org/10.3389/fnhum.2024.1398034
9. Tan XR, Stephenson MC, Alhadad S, et al. Elevated brain temperature under severe heat exposure impairs cortical motor activity and executive function. *Journal of Sport and Health Science*. 2024. https://doi.org/10.1016/j.jshs.2023.09.001
10. Tan Y, Liu W, Li Y, et al. Measurement of Healthy Adult Brain Temperature Using <sup>1</sup>H Magnetic Resonance Spectroscopy Thermometry. *Clinical Neuroradiology*. 2025. https://doi.org/10.1007/s00062-024-01467-3
11. Inoue T, Nomura S, Yamakawa T, et al. Intraoperative evaluation using a multimodality probe of temperature-dependent neurovascular modulation during focal brain cooling. *Clinical Neurophysiology*. 2025. https://doi.org/10.1016/j.clinph.2025.02.262
12. Lazopulo A, Emmenegger Y, Đukanović N, et al. Brain temperature as proxy for brain state and oscillatory activity in the mouse. *Scientific Reports*. 2025. https://doi.org/10.1038/s41598-025-21175-3
