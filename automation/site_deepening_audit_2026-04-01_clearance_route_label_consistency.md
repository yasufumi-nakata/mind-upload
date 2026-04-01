---
title: "2026-04-01 site deepening audit: clearance front-door route consistency"
date: "2026-04-01"
author: "Codex"
---

# Summary

The selected weakness was not the absence of clearance literature, but an internal inconsistency in how the site labeled that literature at the front door. Several core pages already treated current human clearance evidence as a **route-conditioned transport-side proxy family**. However, some high-visibility table labels still used the stronger phrase **`sleep-linked glymphatic clearance`** for Dagum et al. (2026), and one roadmap row still merged Hirschler et al. (2025) and Dagum et al. (2026) under **`CSF mobility / glymphatic clearance routes`**. That wording was weaker than the site's own route-card discipline.

# Why This Needed Correction

The site's current operating rule already says that human clearance evidence must be typed more narrowly than a generic `glymphatic` label. The reason is visible in the primary literature itself.

- Hirschler et al. (2025) measured **CSF mobility** with a specialized 7 T MRI method and explicitly stopped short of claiming net-flow direction or route-free clearance.
- Dagum et al. (2026) used a **randomized crossover design**, an **investigational wearable**, plasma Aβ / tau measurements, and a **multicompartment model** to infer overnight **brain-to-plasma biomarker efflux** under sleep-related physiology.

These papers are both important, but they do not share one direct observable, one transport object, or one model burden. Therefore, calling the Dagum route `glymphatic clearance` in a front-door table risks silently promoting a model-based transport inference into a more direct human measurement class than the rest of the site allows.

# Primary Source Basis

1. Hirschler et al. (2025). *Region-specific drivers of CSF mobility measured with MRI in humans*. Nature Neuroscience. https://doi.org/10.1038/s41593-025-02073-3
2. Dagum et al. (2026). *The glymphatic system clears amyloid beta and tau from brain to plasma in humans*. Nature Communications. https://doi.org/10.1038/s41467-026-68374-8

# Changes Executed In This Session

- Renamed the Dagum row in [`index.md`](/Users/yasufumi/Documents/GitHub/mind-upload/index.md) from `sleep-linked glymphatic clearance` to `model-based overnight biomarker efflux`.
- Renamed the Dagum row in [`wbe_101.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wbe_101.md) to the same route-typed label.
- Renamed the combined clearance row in [`tech_roadmap.md`](/Users/yasufumi/Documents/GitHub/mind-upload/tech_roadmap.md) from `CSF mobility / glymphatic clearance routes` to `CSF mobility / model-based biomarker-efflux routes`, and made explicit that these are different clearance-transport rows rather than one route-free glymphatic meter.
- Tightened the beginner explanation in [`wiki/claims-and-evidence.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/claims-and-evidence.md) so Hirschler is described as a mobility route whose sequence does not determine net-flow direction, while Dagum is described as model-based overnight biomarker efflux.

# Verification

- Regenerated [`summary_booklet.md`](/Users/yasufumi/Documents/GitHub/mind-upload/summary_booklet.md) with `ruby scripts/build_summary_booklet.rb`.
- Rebuilt the static site with `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`.
- Confirmed the new labels appear in `_site/index.html`, `_site/wbe_101.html`, `_site/tech_roadmap.html`, and `_site/wiki/claims-and-evidence.html`.

# Resulting Rule

On this site, Dagum et al. (2026) should now be read at the front door as a **model-based overnight biomarker-efflux route**, not as a generic or route-free human glymphatic meter. Hirschler et al. (2025) should be read as a **CSF-mobility route**, not as direct net-flow or solute-clearance ground truth. That change makes the public entry pages consistent with the stricter route-card logic already used elsewhere on the site.
