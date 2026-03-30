# Site Deepening Audit (2026-03-31, perspective electrical-state family split)

## Target

- Primary target:
  - `perspective.md`
- Scope:
  - technology / natural science only

## Why This Area Was Chosen

- The site already had a good stop rule for `shared extracellular / electrical state` in:
  - `index.md`
  - `verification.md`
  - `wiki/connectome-is-not-enough.md`
- However, the central synthesis page, `perspective.md`, still treated that class too compactly.
- This mattered because `perspective.md` is the page most likely to be read as the site's integrated position.
- If that page leaves `electrical state` as one row, readers can still overread the literature as if:
  - gap-junction coupling,
  - ephaptic / endogenous-field effects,
  - extracellular-space geometry,
  - inhibitory driving-force regime,
  - and bounded human clues
  all constrained one shared hidden variable.
- Current primary literature does not support that compression.

## Evidence-Based Critique

### 1. The current central wording was still too coarse inside the electrical-state class

- `Galarreta & Hestrin (1999)` and `Yang et al. (2024)` constrain electrical-synapse topology and activity-dependent rewiring.
- `Anastassiou et al. (2011)` constrains endogenous-field / ephaptic spike-timing bias.
- `Graydon et al. (2014)`, `Kilb et al. (2006)`, `Lauderdale et al. (2015)`, and `Xie et al. (2013)` constrain extracellular-space geometry, dilution, osmotic contraction, edema-linked excitability, and sleep-linked interstitial-space expansion.
- `Burman et al. (2023)` and `Selfe et al. (2024)` constrain inhibitory driving-force regime, with `Selfe et al.` using a specialized direct optical assay rather than a field-ready whole-brain route.

Conclusion:

- These papers do not share one direct observable.
- They do not share one spatial regime.
- They do not share one human observability ceiling.
- Therefore they should not be left inside one generic sentence on the central page.

### 2. The human-facing side is still clue-level, not whole-brain ground truth

- `Voldsbekk et al. (2020)` is useful because it provides a bounded diffusion-MRI clue consistent with wakefulness-related extracellular-space change in human white matter.
- `Feld et al. (2026)` is useful because it provides a human sleep-perturbation clue that electrical synapses matter for declarative-memory retention.

But:

- `Voldsbekk et al. (2020)` is not a direct local readout of extracellular-volume fraction, tortuosity, spillover geometry, or inhibitory-driving-force regime.
- `Feld et al. (2026)` is not a whole-brain readout of coupling topology or electrotonic state; it is a perturbation-conditioned systems clue.

Conclusion:

- The central page needed to say explicitly that current human evidence remains a bounded clue layer rather than a route-free whole-brain electrical-state meter.

### 3. This correction belongs on the synthesis page, not only in route-card pages

- `verification.md` already had the stricter route-card logic.
- `index.md` already warned readers that electrical-state evidence is not one class.
- But if `perspective.md` stayed compressed, the site's own integrated interpretation would remain looser than its operational rules.

Conclusion:

- The correct fix for this session was to move the family split onto `perspective.md` itself.

## Changes Executed In This Session

- `perspective.md`
  - updated `last_updated` to `2026-03-31`
  - updated the note string to record the electrical-state family split
  - added a new page highlight stating that electrical-state evidence is split into internal claim families
  - tightened a `known_points` entry so the page no longer speaks only of `local electrical-coupling / inhibitory-driving-force regime`, but also names `extracellular-geometry`
  - added a new `known_points` entry stating that current human evidence remains bounded to proxy or perturbation clues
  - added a new note box:
    - `2026-03-31 correction: shared extracellular / electrical state is not one inferential object`
  - added a new table that separates:
    - gap-junction network routes
    - endogenous-field / ephaptic routes
    - extracellular-space geometry / osmotic routes
    - inhibitory-driving-force routes
    - human clue layer
  - tightened the hidden-state row so it now names:
    - extracellular-space geometry / diffusion barriers / osmotic regime
    - bounded human perturbation clues
  - added reference-list entries for the electrical-state family papers used in this update

## Misreadings Now Blocked More Explicitly

- `electrical-state evidence exists` = `the electrical regime was measured`
- `gap-junction evidence` = `extracellular-space geometry also matched`
- `human diffusion-MRI clue` = `direct in vivo extracellular-state ground truth`
- `human sleep perturbation clue` = `whole-brain coupling topology was measured`
- `chemical connectome plus nominal inhibition` = `electrical-state complete`

## Verification

- Planned verification for this session:
  - `git diff --check`
  - `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
  - focused diff review of `perspective.md`

## External Dependency Tasks

- None
  - The work for this session is fully executable inside the repository: literature confirmation, public-text revision, build verification, commit, and push.

## References

1. Galarreta M, Hestrin S. A network of fast-spiking cells in the neocortex connected by electrical synapses. *Nature*. 1999;402:72-75.
   - https://doi.org/10.1038/47029
2. Anastassiou CA, Perin R, Markram H, Koch C. Ephaptic coupling of cortical neurons. *Nature Neuroscience*. 2011;14:217-223.
   - https://doi.org/10.1038/nn.2727
3. Graydon CW, Cho S, Diamond JS, Kachar B, von Gersdorff H, Grimes WN. Specialized postsynaptic morphology enhances neurotransmitter dilution and high-frequency signaling at an auditory synapse. *Journal of Neuroscience*. 2014;34(23):7871-7885.
   - https://doi.org/10.1523/JNEUROSCI.4493-13.2014
4. Kilb W, Dierkes PW, Syková E, Vargová L, Luhmann HJ. Hypoosmolar conditions reduce extracellular volume fraction and enhance epileptiform activity in the CA3 region of the immature rat hippocampus. *Journal of Neuroscience Research*. 2006;84(2):361-371.
   - https://doi.org/10.1002/jnr.20871
5. Lauderdale K, Murphy T, Tung T, Davila D, Binder DK, Fiacco TA. Osmotic edema rapidly increases neuronal excitability through activation of NMDA receptor-dependent slow inward currents in juvenile and adult hippocampus. *ASN Neuro*. 2015;7(5).
   - https://doi.org/10.1177/1759091415605115
6. Xie L, Kang H, Xu Q, Chen MJ, Liao Y, Thiyagarajan M, O'Donnell J, Christensen DJ, Nicholson C, Iliff JJ, Takano T, Deane R, Nedergaard M. Sleep drives metabolite clearance from the adult brain. *Science*. 2013;342(6156):373-377.
   - https://doi.org/10.1126/science.1241224
7. Burman RJ, Brodersen PJN, Raimondo JV, Sen A, Akerman CJ. Active cortical networks promote shunting fast synaptic inhibition in vivo. *Neuron*. 2023;111(22):3545-3560.e6.
   - https://doi.org/10.1016/j.neuron.2023.08.005
8. Yang YC, Wang GH, Chou P, Hsueh SW, Lai YC, Kuo CC. Dynamic electrical synapses rewire brain networks for persistent oscillations and epileptogenesis. *Proceedings of the National Academy of Sciences*. 2024;121(8):e2313042121.
   - https://doi.org/10.1073/pnas.2313042121
9. Selfe JS, Steyn TJS, Shorer EF, Burman RJ, Düsterwald KM, Kraitzick AZ, Ju C, Goldman PS, Ibrahim BA, Syed P, Li L, Akerman CJ, Kullmann DM, Raimondo JV, Baker CA. All-optical reporting of inhibitory receptor driving force in the nervous system. *Nature Communications*. 2024;15:9752.
   - https://doi.org/10.1038/s41467-024-53074-y
10. Voldsbekk I, Maximov II, Zak N, Roelfs D, Geier O, Due-Tønnessen P, Elvsåshagen T, Strømstad M, Bjørnerud A, Groote I. Evidence for wakefulness-related changes to extracellular space in human brain white matter from diffusion-weighted MRI. *NeuroImage*. 2020;212:116682.
   - https://doi.org/10.1016/j.neuroimage.2020.116682
11. Feld GB, Niethard N, Liu J, Gebhardt S, Kleist L, Brugger K, Born J. Electrical synapses contribute to sleep-dependent declarative memory retention. *European Journal of Neuroscience*. 2026.
   - https://doi.org/10.1111/ejn.70401
