# 2026-03-29 site deepening audit: beginner spectroscopy route taxonomy sync

## 1. Why this was the highest-value gap today

- The public front-door pages had already become much stricter about human proxy taxonomy, but the beginner/wiki layer still lagged behind in one scientifically important way.
- Several beginner-support pages still allowed readers to compress:
  - `31P metabolite / pH balance`
  - `31P MT exchange-flux`
  - `31P NAD-content mapping`
  - `localized functional 31P NAD-dynamics`
  - `deuterium metabolite-mapping / absolute-quantification`
  - `deuterium kinetic-rate imaging`
  into a much smaller set of labels such as `31P energetic balance` or `deuterium metabolite / rate imaging`.
- That compression is not a cosmetic wording issue. It changes what the route is taken to measure, what burden is hidden, and what hidden-state family the route can safely calibrate.

## 2. Evidence-driven criticism

### 2.1 Route-name compression was reintroducing quantity-type collapse below the front door

- The public site had already moved to the rule that human spectroscopy rows must be typed by `what inferential object they constrain`, not just by modality family.
- However, the beginner-support pages were still lagging in places where `31P energetic balance` and `deuterium metabolite / rate imaging` could be read as if they were each one stable route family.
- This is technically unsafe because the primary literature does not support a single spectroscopy ladder here.

### 2.2 The 31P rows do not answer the same measurement question

- [Ren et al. (2015)](https://doi.org/10.1002/nbm.3384) is a resting human `31P metabolite / pH balance` route. It estimates ATP-synthesis-related, phosphorus-metabolite, and intra-/extracellular pH quantities in a resting healthy cohort.
- [Ren et al. (2017)](https://doi.org/10.1002/mrm.26560) is a `31P MT exchange-flux` route. It is a 7 T magnetization-transfer study with explicit exchange-model burden; it is not the same inferential object as resting metabolite / pH balance.
- [Guo et al. (2024)](https://doi.org/10.3389/fnins.2024.1389111) is a `whole-brain intracellular NAD-content mapping` route. It constrains a low-concentration whole-brain map under 7 T spectroscopy and denoising / fitting burden.
- [Kaiser et al. (2026)](https://doi.org/10.1177/0271678X261415784) is a `localized functional 31P NAD-dynamics` route. It uses prior fMRI localization and a task-locked occipital voxel, not a whole-brain map.
- Therefore, `31P spectroscopy` or even `31P energetic balance` is too coarse as a beginner route label, because the current literature already separates at least resting balance, exchange flux, static NAD content, and localized task dynamics.

### 2.3 The deuterium rows also do not answer the same measurement question

- [Karkouri et al. (2026)](https://doi.org/10.1002/mrm.70308) is an `absolute-quantification` route with explicit metabolite maps and calibration burden under a specialized 7 T workflow.
- [Li et al. (2025)](https://doi.org/10.1093/pnasnexus/pgaf072) is a `dynamic deuterium kinetic-rate imaging` route with 0.7 cc nominal voxels, 2.5 min temporal frames, blood-input acquisition, and explicit kinetic modeling in five healthy participants.
- These are not the same direct observable. One route emphasizes calibrated metabolite distributions; the other explicitly adds kinetic-model burden to recover rate terms such as glucose-transport and metabolic-rate variables.
- Therefore, `deuterium metabolite / rate imaging` is not an acceptable compressed label when the site is trying to stop quantity-type collapse.

### 2.4 Operating-point literature makes generic route names even less defensible

- [Ahmadian et al. (2025)](https://doi.org/10.1002/jmri.29532) showed that human brain-side deuterated-glucose and downstream Glx visibility depend materially on administered `[6,6'-2H2]glucose` dose.
- [Bøgh et al. (2024)](https://doi.org/10.1186/s41747-024-00426-4) showed that repeatability at 3 T is a property of a named DMI protocol and time-point regime, not a universal guarantee for all deuterium routes.
- Therefore, even after splitting `absolute metabolite mapping` from `kinetic-rate imaging`, the site still has to name operating-point burden rather than letting `deuterium imaging` carry the claim.

## 3. What I changed in this session

- Synchronized beginner/public wording so `Ren et al. (2015)` is consistently treated as `31P metabolite / pH balance`, not the older compressed `31P energetic balance` label.
- Added the missing `31P MT exchange-flux` row to beginner-facing comparison tables that had not yet caught up with the front-door taxonomy.
- Rewrote beginner proxy-bundle language so spectroscopy rows are split into:
  - `1H-MRSI similarity`
  - `31P metabolite / pH balance`
  - `31P MT exchange-flux`
  - `31P NAD-content mapping`
  - `localized functional 31P NAD-dynamics`
  - `deuterium metabolite-mapping / absolute-quantification`
  - `deuterium kinetic-rate imaging`
- Updated public-facing summaries that still used the older compressed wording, so the site no longer teaches one taxonomy on the front door and another in the supporting pages.

## 4. Files updated

- `index.md`
- `faq.md`
- `perspective.md`
- `tech_roadmap.md`
- `verification.md`
- `wiki/verification-basics.md`
- `wiki/mind-upload-basics.md`
- `wiki/measurement-stack-and-claim-ceiling.md`
- `wiki/human-proxy-composition.md`

## 5. Verification to run after edits

- `ruby scripts/build_summary_booklet.rb`
- `ruby scripts/export_github_wiki.rb`
- `ruby scripts/check_github_wiki_export.rb`
- `bundle exec jekyll build`
- `rg` check for remaining compressed route names
- `git diff --check`

## 6. References

1. Ren J, Sherry AD, Malloy CR. Efficient 31P band inversion transfer approach to measure adenosine triphosphate synthesis and inorganic phosphate pool size in the human brain at 7T. *NMR in Biomedicine*. 2015. https://doi.org/10.1002/nbm.3384
2. Ren J, Sherry AD, Malloy CR. 31P-MRS saturation transfer detects altered ATP metabolism in response to an acute exercise challenge. *Magnetic Resonance in Medicine*. 2017. https://doi.org/10.1002/mrm.26560
3. Guo J, et al. Whole-brain mapping of intracellular NAD contents in humans using 31P-MRSI at 7 T. *Frontiers in Neuroscience*. 2024. https://doi.org/10.3389/fnins.2024.1389111
4. Kaiser RH, et al. Functional 31P-MRS reveals task-evoked NAD+ dynamics in human visual cortex. *Journal of Cerebral Blood Flow & Metabolism*. 2026. https://doi.org/10.1177/0271678X261415784
5. Karkouri J, et al. Human brain deuterium imaging with absolute quantification at 7 T. *Magnetic Resonance in Medicine*. 2026. https://doi.org/10.1002/mrm.70308
6. Li X, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025. https://doi.org/10.1093/pnasnexus/pgaf072
7. Ahmadian R, et al. Human brain deuterium metabolic imaging at 7 T: impact of different [6,6'-2H2]glucose doses. *Journal of Magnetic Resonance Imaging*. 2025. https://doi.org/10.1002/jmri.29532
8. Bøgh N, et al. Repeatability of deuterium metabolic imaging of healthy volunteers at 3 T. *European Radiology Experimental*. 2024. https://doi.org/10.1186/s41747-024-00426-4
