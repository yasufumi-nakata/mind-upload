---
title: "2026-04-04 site deepening audit: glossary excitability and ionic split"
date: "2026-04-04"
author: "Codex"
---

# Summary

The selected weakness was a **terminology gap in the glossary around intrinsic-excitability and ionic / chloride route language**.

By 2026-04-04, the public front door had already become stricter about two important maintenance-side stop lines:

- `intrinsic excitability` is not one row
- `ionic / chloride state` is not one row

The landing page and `WBE 101` already used a disciplined split:

- allocation / engram-selection bias
- AIS / ion-channel-state plasticity
- firing-rate set point / recovery control
- bounded human excitability proxies

and separately:

- local chloride set point
- KCC2-linked chloride regulation
- interstitial-ion state switching
- perisynaptic K+ clearance
- quantity-defined human sodium / ionic proxy families

But the central term page, [`/Users/yasufumi/Documents/GitHub/mind-upload/glossary.md`](/Users/yasufumi/Documents/GitHub/mind-upload/glossary.md), still did not define those distinctions at the front door.

That was not a cosmetic omission. It weakened the site's own reading discipline exactly where readers are supposed to recover quickly from confusion.

# Why This Needed Correction

## 1. The site already taught the split, but the glossary still compressed it

Recent public pages already told readers that:

- excitability evidence is not one class
- ionic evidence is not one class
- human sodium MRI is not direct chloride-state ground truth
- local unit or perturbation evidence is not a whole-brain controller readout

However, the glossary still stopped at broader labels such as `maintenance-state`, `support-state proxy`, and `shared extracellular / electrical state` without defining the excitability-side or chloride-side front-door terms needed to keep those warnings operational.

That created a predictable failure mode:

- the reader sees that `intrinsic excitability` matters
- but still has no short glossary definition for why allocation, AIS dynamics, and recovery control are different carried objects

and similarly:

- the reader sees that `ionic / chloride` matters
- but still has no short glossary definition for why chloride set point, interstitial-ion transitions, and sodium MRI are not the same inferential object

## 2. Primary literature does not support one generic `intrinsic excitability`

- [Yiu et al. (2014)](https://doi.org/10.1016/j.neuron.2014.07.017) support a **relative-excitability / allocation-bias** route.
- [Hadzibegovic et al. (2025)](https://doi.org/10.1038/s41467-025-66975-3) support an **early engram-excitability plasticity** route.
- [Benoit et al. (2025)](https://doi.org/10.1038/s41593-025-02152-5) support an **AIS-dynamics during learning** route.
- [Hengen et al. (2016)](https://doi.org/10.1016/j.cell.2016.01.046) support a **firing-rate set-point / recovery-control** route.
- [Tallman et al. (2025)](https://doi.org/10.1038/s41598-025-21967-7) provide a **human hippocampal clinical-unit allocation-linked** route, while explicitly keeping firing as an indirect index rather than a direct whole-brain excitability measurement.

Critique:

- allocation bias is not the same object as AIS geometry or Na+ channel distribution
- AIS dynamics are not the same object as the controller that returns a neuron or circuit toward a firing-rate set point
- a local human single-unit route is not the same thing as a whole-brain in vivo excitability readout

Therefore, one generic glossary meaning for `intrinsic excitability` was weaker than the literature and weaker than the rest of the site.

## 3. Primary literature does not support one generic `ionic / chloride state`

- [Glykys et al. (2014)](https://doi.org/10.1126/science.1245423) support a **local chloride-set-point** route.
- [Heubl et al. (2017)](https://doi.org/10.1038/s41467-017-01749-0) support an **activity-dependent KCC2 / WNK1 chloride-regulation** route.
- [Ding et al. (2016)](https://doi.org/10.1126/science.aad4821) support an **interstitial-ion state-switching** route across sleep and wake.
- [Byvaltsev et al. (2023)](https://doi.org/10.1016/j.celrep.2023.112934) support a **perisynaptic K+ clearance by reverse-mode KCC2** route.
- [Lyckenvik et al. (2025)](https://doi.org/10.1093/braincomms/fcaf201) support a **human CSF-ion regulation** route distinct from serum chemistry.
- [Qian et al. (2025)](https://doi.org/10.1038/s41598-025-07800-1) support a **mono-/bi-T2 sodium-signal separation** route in human sodium MRI rather than one universal ionic-state meter.

Critique:

- chloride set point is not the same object as KCC2 regulation kinetics
- KCC2-linked local clearance is not the same object as global sleep-wake ion composition shifts
- human CSF-ion regulation is not the same object as cell-specific chloride concentration
- sodium MRI quantity types are not interchangeable, and none of them automatically fixes local E_GABA_A or routine intra- versus extracellular partition ground truth

Therefore, one generic glossary meaning for `ionic state` or `ionic evidence` was again weaker than the literature and weaker than the public front door.

## 4. The missing glossary terms mattered exactly where the site tries to prevent overclaiming

Without these definitions, it becomes easier to slide from:

- `excitability matters`
- `ionic state matters`
- `human sodium MRI exists`
- `human single-unit allocation evidence exists`

to:

- `current excitability landscape is approximately known`
- `current chloride state is approximately known`
- `human ionic readout is already close to local controller truth`

The primary literature does not support those upgrades.

# Root Critique

The scientific criticism is therefore:

1. The front-door pages already used the correct split for excitability and ionic evidence.
2. The glossary still under-specified the exact terms readers now need to keep those splits operational.
3. Current primary literature does not justify one generic `intrinsic excitability` term or one generic `ionic / chloride` term.
4. Therefore, the glossary had to distinguish:
   - `intrinsic excitability / homeostatic-set-point route card`
   - `allocation / engram-selection bias`
   - `AIS / ion-channel-state route`
   - `homeostatic set point / recovery control`
   - `ionic / chloride route card`
   - `local chloride set point`
   - `E_GABA_A / inhibitory-driving-force regime`
   - `interstitial-ion state switching`
   - `quantity-defined human sodium / ionic proxy family`

# Web-Verified Primary Sources Checked On 2026-04-04

- Yiu et al. (2014), *Neuron*: https://doi.org/10.1016/j.neuron.2014.07.017
- Hadzibegovic et al. (2025), *Nature Communications*: https://doi.org/10.1038/s41467-025-66975-3
- Benoit et al. (2025), *Nature Neuroscience*: https://doi.org/10.1038/s41593-025-02152-5
- Hengen et al. (2016), *Cell*: https://doi.org/10.1016/j.cell.2016.01.046
- Tallman et al. (2025), *Scientific Reports*: https://doi.org/10.1038/s41598-025-21967-7
- Glykys et al. (2014), *Science*: https://doi.org/10.1126/science.1245423
- Heubl et al. (2017), *Nature Communications*: https://doi.org/10.1038/s41467-017-01749-0
- Ding et al. (2016), *Science*: https://doi.org/10.1126/science.aad4821
- Byvaltsev et al. (2023), *Cell Reports*: https://doi.org/10.1016/j.celrep.2023.112934
- Lyckenvik et al. (2025), *Brain Communications*: https://doi.org/10.1093/braincomms/fcaf201
- Qian et al. (2025), *Scientific Reports*: https://doi.org/10.1038/s41598-025-07800-1

# Changes Executed In This Session

- Updated [`/Users/yasufumi/Documents/GitHub/mind-upload/glossary.md`](/Users/yasufumi/Documents/GitHub/mind-upload/glossary.md)
  - kept `last_updated` at `2026-04-04`
  - updated the page note, highlights, and known points so the glossary now explicitly names the excitability / ionic route-card stop line
  - added a new note box explaining why `intrinsic excitability` is not one generic front-door term
  - added a new note box explaining why `ionic / chloride evidence` is not one generic front-door term
  - added glossary entries for:
    - `intrinsic excitability / homeostatic-set-point route card`
    - `allocation / engram-selection bias`
    - `AIS / ion-channel-state route`
    - `homeostatic set point / recovery control`
    - `ionic / chloride route card`
    - `local chloride set point`
    - `E_GABA_A / inhibitory-driving-force regime`
    - `interstitial-ion state switching`
    - `quantity-defined human sodium / ionic proxy family`
  - extended the glossary reference list with the excitability-side and ionic-side primary sources needed for those definitions

- Added [`/Users/yasufumi/Documents/GitHub/mind-upload/automation/site_deepening_audit_2026-04-04_glossary_excitability_ionic_split.md`](/Users/yasufumi/Documents/GitHub/mind-upload/automation/site_deepening_audit_2026-04-04_glossary_excitability_ionic_split.md)
  - records the criticism, rationale, and verified source trail for this correction

# Verification

- `git diff --check`
- `ruby scripts/build_summary_booklet.rb`
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
- `rg -n "intrinsic excitability / homeostatic-set-point route card|allocation / engram-selection bias|ionic / chloride route card|quantity-defined human sodium / ionic proxy family" glossary.md _site/glossary.html`

# External Dependency Tasks

- None.
  - This run stayed inside executable repository work: literature verification, markdown edits, local static-site build, and Git publication.

# References

1. Yiu AP, Mercaldo V, Yan C, et al. Neurons Are Recruited to a Memory Trace Based on Relative Neuronal Excitability Immediately before Training. *Neuron*. 2014. https://doi.org/10.1016/j.neuron.2014.07.017
2. Hadzibegovic S, Zhu L, Ginger M, et al. Early intrinsic excitability plasticity of neocortical engram neurons defines memory formation and precision. *Nature Communications*. 2025. https://doi.org/10.1038/s41467-025-66975-3
3. Benoit R, Galego DA, Schären MS, et al. Axon initial segment dynamics during associative fear learning. *Nature Neuroscience*. 2025. https://doi.org/10.1038/s41593-025-02152-5
4. Hengen KB, Torrado Pacheco A, McGregor JN, Van Hooser SD, Turrigiano GG. Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. *Cell*. 2016. https://doi.org/10.1016/j.cell.2016.01.046
5. Tallman CW, Steinmetz PN, Wixted JT. Neuronal allocation and sparse coding of episodic memories in the human hippocampus. *Scientific Reports*. 2025. https://doi.org/10.1038/s41598-025-21967-7
6. Glykys J, Dzhala V, Egawa K, et al. Local impermeant anions establish the neuronal chloride concentration. *Science*. 2014. https://doi.org/10.1126/science.1245423
7. Heubl M, Zhang J, Pressey JC, et al. GABAA receptor dependent synaptic inhibition rapidly tunes KCC2 activity via the Cl-sensitive WNK1 kinase. *Nature Communications*. 2017. https://doi.org/10.1038/s41467-017-01749-0
8. Ding F, O'Donnell J, Xu Q, et al. Changes in the composition of brain interstitial ions control the sleep-wake cycle. *Science*. 2016. https://doi.org/10.1126/science.aad4821
9. Byvaltsev E, Behbood M, Schleimer J-H, Gensch T, Semyanov A, Schreiber S, Strauss U. KCC2 reverse mode helps to clear postsynaptically released potassium at glutamatergic synapses. *Cell Reports*. 2023. https://doi.org/10.1016/j.celrep.2023.112934
10. Lyckenvik T, Forsberg M, Johansson K, et al. Ion concentrations in CSF and serum are differentially and precisely regulated. *Brain Communications*. 2025. https://doi.org/10.1093/braincomms/fcaf201
11. Qian Y, Lin Y-C, Chen X, et al. Single-quantum sodium MRI at 3 T for separation of mono- and bi-T2 sodium signals. *Scientific Reports*. 2025. https://doi.org/10.1038/s41598-025-07800-1
