---
title: "2026-04-02 site deepening audit: human clearance route front-door sync"
date: "2026-04-02"
author: "Codex"
---

# Summary

The selected weakness was not that the site lacked human clearance literature. The weakness was that the two literature front-door pages, [`mind_uploading_papers.md`](/Users/yasufumi/Documents/GitHub/mind-upload/mind_uploading_papers.md) and [`research_harvest_50.md`](/Users/yasufumi/Documents/GitHub/mind-upload/research_harvest_50.md), still underexposed the route-family split that other core pages had already adopted. In practice, that let a reader overcompress several distinct human transport-side observables into one generic `clearance-support` bucket.

The specific missing routes were:

- `respiration-conditioned CSF net flow` from Lim et al. (2025)
- `exercise-conditioned contrast influx / meningeal-lymphatic flow` from Yoo et al. (2025)

Those routes already mattered to the site's stricter measurement logic, because they do not share one direct observable, one perturbation regime, one physiological regime, or one model burden with Fultz, Kim, Eide, Hirschler, or Dagum.

# Why This Needed Correction

The site's stronger technical pages already distinguished several human clearance-adjacent route families:

- sleep-state CSF oscillation
- parenchyma-CSF water exchange
- respiration-conditioned CSF net flow
- exercise-conditioned contrast influx / meningeal-lymphatic flow
- intrathecal-tracer / CSF-to-blood-clearance capacity
- CSF mobility
- model-based brain-to-plasma biomarker efflux

However, the public literature-entry pages still made that family split less visible. That was a scientific weakness, not a wording preference. A reader entering through the paper lists could still misread the evidence as if the human literature already supported one broad, route-free maintenance or clearance meter. The primary papers do not support that compression.

# Evidence-Based Critique

## 1. Lim et al. (2025) is not the same route class as Kim et al. (2025)

Kim et al. (2025) used magnetization-transfer spin labeling to estimate age-dependent in vivo human glymphatic exchange. Lim et al. (2025), by contrast, quantified human CSF net flow enhanced by respiration during the awake state. These papers therefore do not share one direct observable or one physiological conditioning regime.

If the front door omits Lim while citing Kim, the site implicitly encourages a reader to collapse `exchange` and `respiration-conditioned net flow` into one transport class. That is a category error. The safe reading is that they constrain different transport-side route families.

## 2. Yoo et al. (2025) adds an intervention-conditioned contrast route, not a generic clearance meter

Yoo et al. (2025) reported long-term physical exercise effects on putative glymphatic and meningeal lymphatic vessel flow in humans. That is not the same claim class as spontaneous sleep-state oscillation, MT-based exchange, intrathecal tracer readout, or model-based overnight biomarker efflux.

Its dependence on exercise conditioning, contrast-derived inference, and meningeal-lymphatic interpretation means the paper is scientifically important but route-bounded. Compressing it into a general `clearance support` label hides the actual acquisition and interpretation burden.

## 3. Eide, Hirschler, and Dagum still do not close the same hidden state

Eide et al. (2023) tied plasma neurodegeneration biomarkers to intrathecal glymphatic and meningeal-lymphatic measures. Hirschler et al. (2025) quantified region-specific drivers of CSF mobility with MRI. Dagum et al. (2026) inferred overnight brain-to-plasma Aβ / tau efflux under an explicit multicompartment model. These are all valuable, but they remain different route classes with different model burdens.

Therefore, the technically correct site-wide rule is not `human clearance evidence exists`, but `human clearance-side proxy families exist, each with its own observable, regime, and ceiling`.

# Changes Executed In This Session

- Updated [`mind_uploading_papers.md`](/Users/yasufumi/Documents/GitHub/mind-upload/mind_uploading_papers.md) so the front door now explicitly lists `respiration-conditioned CSF net flow` and `exercise-conditioned contrast influx / meningeal-lymphatic flow` in the human in vivo clearance family, adds a dedicated note box, and expands the observability ladder accordingly.
- Updated [`research_harvest_50.md`](/Users/yasufumi/Documents/GitHub/mind-upload/research_harvest_50.md) so the U3 literature overview now treats Lim and Yoo as distinct route-family rows and states that these papers must not be read as one transport bucket.
- Updated [`wiki/measurement-stack-and-claim-ceiling.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/measurement-stack-and-claim-ceiling.md) to synchronize the human clearance ladder, the proxy-class rule, the support-state warning, and the bibliography with the same route-family split.

# Verification

- Rebuilt the static site with `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`.
- Ran `git diff --check`.
- Confirmed the new route-family labels appear in `_site/mind_uploading_papers.html`, `_site/research_harvest_50.html`, and `_site/wiki/measurement-stack-and-claim-ceiling.html`.

# Resulting Rule

On this site, the human clearance literature should now be read as a family of route-conditioned transport proxies rather than as one generic support meter. Lim et al. (2025) should be read as a `respiration-conditioned CSF net-flow` route. Yoo et al. (2025) should be read as an `exercise-conditioned contrast-influx / meningeal-lymphatic` route. Eide, Hirschler, and Dagum remain distinct bounded routes as well. That makes the literature front door consistent with the site's stricter measurement-ceiling logic.

# Primary References

1. Fultz NE, Bonmassar G, Setsompop K, et al. Coupled electrophysiological, hemodynamic, and cerebrospinal fluid oscillations in human sleep. *Science*. 2019.
   - https://doi.org/10.1126/science.aax5440
2. Kim D, Huang Y, Liu J. Non-invasive MRI measurements of age-dependent in vivo human glymphatic exchange using magnetization transfer spin labeling. *NeuroImage*. 2025.
   - https://doi.org/10.1016/j.neuroimage.2025.121142
3. Lim C, Chen C, Zhang C, et al. Human cerebrospinal fluid net flow enhanced by respiration during the awake state. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-66548-4
4. Yoo R-E, Kim J-H, Moon HY, et al. Long-term physical exercise facilitates putative glymphatic and meningeal lymphatic vessel flow in humans. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-58726-1
5. Eide PK, Lashkarivand A, Pripp AH, et al. Plasma neurodegeneration biomarker concentrations associate with glymphatic and meningeal lymphatic measures in neurological disorders. *Nature Communications*. 2023.
   - https://doi.org/10.1038/s41467-023-37685-5
6. Hirschler L, Runderkamp BAR, Decker A, et al. Region-specific drivers of CSF mobility measured with MRI in humans. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-02073-3
7. Dagum P, Elbert DL, Giovangrandi L, et al. The glymphatic system clears amyloid beta and tau from brain to plasma in humans. *Nature Communications*. 2026.
   - https://doi.org/10.1038/s41467-026-68374-8
