---
title: "2026-04-03 site deepening audit: shared extracellular / electrical-state human clue split"
date: "2026-04-03"
author: "Codex"
---

# Summary

The selected weakness was a **front-door overcompression inside shared extracellular / electrical-state evidence**.

The animal-mechanistic side was already reasonably separated on the site:

- gap-junction coupling
- endogenous-field / ephaptic effects
- extracellular-space geometry / dilution
- osmotic extracellular-space contraction
- inhibitory-driving-force regime
- activity-dependent electrical-synapse remodeling

However, the human side still looked too flat on several entry pages. In practice, the public reading model was still close to:

- `Voldsbekk et al. (2020)` = human diffusion clue
- `Feld et al. (2026)` = human perturbation clue

That was too weak, because a third bounded human row was already available in the primary literature:

- `Örzsik et al. (2023)` = sleep-conditioned higher-order diffusion / glymphatic clue

# Why This Needed Correction

## 1. The human side was still being compressed into "one diffusion clue plus one perturbation clue"

- [Voldsbekk et al. (2020)](https://doi.org/10.1016/j.neuroimage.2020.116682) is a **wakefulness-related diffusion-MRI clue** about extra-axonal versus extracellular volume in human white matter.
- [Örzsik et al. (2023)](https://doi.org/10.1016/j.neuroimage.2023.120124) is not the same row. It used a **within-subject wake-versus-sleep design**, with **sleep deprivation plus zolpidem**, and interpreted **higher-order diffusion / MAP-MRI changes** as compatible with increased interstitial-fluid volume and glymphatic-like clearance.
- [Feld et al. (2026)](https://doi.org/10.1111/ejn.70401) is a **perturbation-conditioned clue** about electrical coupling and spindle-to-slow-oscillation coordination during sleep, not a geometric readout.

Critique:

- These three papers do not share the same direct observable.
- They do not share the same regime.
- They do not share the same model burden.
- Therefore, they should not sit under one vague label such as `human clue for extracellular / electrical state`.

## 2. The site correctly warned that human evidence is bounded, but it still under-specified *how* it is bounded

The actual bounded rows are different:

- `wakefulness-related diffusion clue`
- `sleep-conditioned higher-order diffusion / glymphatic clue`
- `perturbation-conditioned clue`

These are three different inferential ceilings.

Critique:

- A wakefulness-related compartment clue is not the same as a sleep-conditioned interstitial-fluid clue.
- Neither is the same as a perturbation result that shifts spindle-to-slow-oscillation coupling.
- If this split is not made explicit, readers can silently overread "some human evidence exists" as if one local human route to extracellular / electrical state were already emerging.

## 3. This overcompression directly matters for the site's central anti-shortcut argument

The whole point of the `connectome is not enough` argument is not merely that variables are missing, but that they are missing in **different ways** and remain observable only through **different ceilings**.

If the site itself compresses the human side of shared extracellular / electrical-state evidence, then it weakens its own strongest methodological point:

- `structure != state`
- `a proxy row != a direct readout`
- `one bounded human clue != one emerging state meter`

# Changes Executed In This Session

## Entry pages

- [`/Users/yasufumi/Documents/GitHub/mind-upload/index.md`](/Users/yasufumi/Documents/GitHub/mind-upload/index.md)
  - split the human side of the electrical-state warning into:
    - wakefulness-related diffusion clue
    - sleep-conditioned higher-order diffusion / glymphatic clue
    - perturbation-conditioned clue
- [`/Users/yasufumi/Documents/GitHub/mind-upload/wbe_101.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wbe_101.md)
  - updated the beginner route-card summary so `Örzsik et al. (2023)` appears as a distinct human clue class rather than disappearing inside the generic diffusion lane
- [`/Users/yasufumi/Documents/GitHub/mind-upload/faq.md`](/Users/yasufumi/Documents/GitHub/mind-upload/faq.md)
  - split the short-answer front door into electrical perturbation clue versus extracellular-geometry diffusion clue
  - added the sleep-conditioned higher-order diffusion / glymphatic clue explicitly

## Route-rule pages

- [`/Users/yasufumi/Documents/GitHub/mind-upload/verification.md`](/Users/yasufumi/Documents/GitHub/mind-upload/verification.md)
  - updated the route-card addendum so verification-side human evidence classes now include the sleep-conditioned higher-order diffusion clue explicitly
- [`/Users/yasufumi/Documents/GitHub/mind-upload/wiki/connectome-is-not-enough.md`](/Users/yasufumi/Documents/GitHub/mind-upload/wiki/connectome-is-not-enough.md)
  - updated the electrical-state route card and human observability ceiling
  - split human diffusion evidence into wakefulness-related versus sleep-conditioned rows

## Terminology support

- [`/Users/yasufumi/Documents/GitHub/mind-upload/glossary.md`](/Users/yasufumi/Documents/GitHub/mind-upload/glossary.md)
  - added glossary entries for:
    - shared extracellular / electrical state
    - human ECS proxy clue
    - human perturbation-conditioned clue

# Verification

- `git diff --check`
- `ruby scripts/build_summary_booklet.rb`
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
- `rg -n "Örzsik et al. \\(2023\\)|sleep-conditioned higher-order diffusion / glymphatic clue|Human ECS proxy clue" index.md wbe_101.md faq.md verification.md wiki/connectome-is-not-enough.md glossary.md`

# External Dependency Tasks

- None.
  - This run stayed inside executable repository work: literature verification, markdown edits, local build verification, and Git publication.

# References

1. Galarreta M, Hestrin S. A network of fast-spiking cells in the neocortex connected by electrical synapses. *Nature*. 1999.
   - https://doi.org/10.1038/47029
2. Anastassiou CA, Perin R, Buzsáki G, Markram H, Koch C. Ephaptic coupling of cortical neurons. *Nature Neuroscience*. 2011.
   - https://doi.org/10.1038/nn.2727
3. Graydon CW, Cho S, Li GL, et al. Cell-type-specific properties of neurotransmitter diffusion near synapses. *Journal of Neuroscience*. 2014.
   - https://doi.org/10.1523/JNEUROSCI.4493-13.2014
4. Kilb W, Dierkes PW, Luhmann HJ. Development of the subplate and early cortical circuits. *Journal of Neuroscience Research*. 2006.
   - https://doi.org/10.1002/jnr.20871
5. Lauderdale KJ, Murphy T, Jacobs RE, Foehring RC. Osmotic edema rapidly increases neuronal excitability through changes in extracellular volume. *Fluids and Barriers of the CNS*. 2015.
   - https://doi.org/10.1177/1759091415605115
6. Xie L, Kang H, Xu Q, et al. Sleep drives metabolite clearance from the adult brain. *Science*. 2013.
   - https://doi.org/10.1126/science.1241224
7. Voldsbekk I, et al. Evidence for wakefulness-related changes to extracellular space in human brain white matter from diffusion-weighted MRI. *NeuroImage*. 2020.
   - https://doi.org/10.1016/j.neuroimage.2020.116682
8. Örzsik B, Palombo M, Asllani I, Dijk DJ, Harrison NA, Cercignani M. Higher order diffusion imaging as a putative index of human sleep-related microstructural changes and glymphatic clearance. *NeuroImage*. 2023.
   - https://doi.org/10.1016/j.neuroimage.2023.120124
9. Burman RJ, Brodersen PJN, Raimondo JV, Sen A, Akerman CJ. Active cortical networks promote shunting fast synaptic inhibition in vivo. *Neuron*. 2023.
   - https://doi.org/10.1016/j.neuron.2023.08.005
10. Yang X, et al. Dynamic electrical synapses rewire brain networks for persistent oscillations. *PNAS*. 2024.
    - https://doi.org/10.1073/pnas.2313042121
11. Selfe JS, et al. All-optical reporting of inhibitory receptor driving force in the nervous system. *Nature Communications*. 2024.
    - https://doi.org/10.1038/s41467-024-53074-y
12. Feld GB, et al. Electrical Synapses Contribute to Sleep-Dependent Declarative Memory Retention. *European Journal of Neuroscience*. 2026.
    - https://doi.org/10.1111/ejn.70401
