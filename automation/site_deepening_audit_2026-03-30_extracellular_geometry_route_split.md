# Site Deepening Audit (2026-03-30, Shared Extracellular / Electrical-State Route Split)

## Scope

- Primary target: `wiki/connectome-is-not-enough.md`
- Secondary targets: `index.md`, `wbe_101.md`, `verification.md`, `faq.md`

## Why This Topic Was Chosen

- The site had already become much stronger at separating `ionic / chloride state`, `timing-state`, and `astrocyte / clearance support` from the connectome-only story.
- However, the public wording around `shared extracellular / electrical state` still leaned too heavily toward gap junctions, ephaptic effects, and inhibitory driving force.
- That left one technically important family undernamed: `extracellular-space geometry / diffusion-barrier / osmotic regime`.
- This matters because a chemical connectome can stay fixed while local extracellular dilution, spillover, sleep-linked interstitial-space width, and edema-linked excitability still move.

## Evidence-Backed Critique

### 1. Electrical coupling and extracellular geometry are not the same inferential object

- Problem:
  - The old wording could still let readers treat `electrical-state` as mostly a gap-junction / field-effect story.
- Evidence:
  - Galarreta & Hestrin (1999) constrained fast-spiking interneuron electrical-synapse networks.
  - Anastassiou et al. (2011) constrained endogenous-field-driven spike-timing bias.
  - Graydon et al. (2014) constrained local extracellular-volume-fraction geometry and transmitter dilution at a synapse.
- Critique:
  - Therefore `who is electrically coupled` and `how wide the extracellular pocket is` are different objects and should not share one unnamed bucket.

### 2. Osmotic extracellular-space contraction changes excitability without rewiring

- Problem:
  - The prior text did not force the reader to keep osmotic / edema-linked ECS changes visible.
- Evidence:
  - Kilb et al. (2006) showed that hypoosmolar conditions reduced ECS volume fraction in immature hippocampus and increased epileptiform activity.
  - Lauderdale et al. (2015) showed that osmotic edema rapidly increased neuronal excitability through NMDA-receptor-dependent slow inward currents.
- Critique:
  - Therefore `same synapse graph` does not imply `same local dilution / excitability regime`, especially when ECS width and cell swelling differ.

### 3. Sleep-wake ECS changes and human proxy clues have a lower claim ceiling than local mechanism papers

- Problem:
  - The old route card named a human perturbation clue, but it still undernamed sleep-wake ECS geometry and diffusion-MRI proxy evidence.
- Evidence:
  - Xie et al. (2013) showed that sleep or anesthesia enlarged interstitial space and increased CSF-interstitial exchange in mice.
  - Voldsbekk et al. (2020) reported wakefulness-related diffusion-MRI changes in human white matter consistent with reduced extra-axonal / extracellular volume.
  - Feld et al. (2026) showed that mefloquine before sleep impaired declarative-memory retention and spindle-to-slow-oscillation coupling, but with pharmacological caveats.
- Critique:
  - Therefore sleep-linked ECS geometry in mice, diffusion-MRI extra-axonal clues in humans, and pharmacological sleep perturbations in humans do not share one claim ceiling.

### 4. The route card needed to become `extracellular / electrical`, not only `electrical`

- Problem:
  - The old field names still said `direct electrical observable`, which was too narrow for diffusion constraints, extracellular width, or osmotic ECS measurements.
- Evidence:
  - The new literature split requires at least these families:
    - gap-junction coupling network
    - endogenous-field / ephaptic route
    - extracellular-space geometry / diffusion-barrier route
    - inhibitory-driving-force regime
    - activity-dependent electrical-synapse remodeling
    - human wakefulness-related ECS proxy clue
    - human perturbation-conditioned clue
- Critique:
  - Without renaming the route-card fields, the public rule would still underdescribe what the cited papers actually measure.

## Changes Executed In This Session

- `index.md`
  - Updated the landing-page highlight and known-point text so `chemical connectome != shared extracellular / electrical-state complete`.
  - Rewrote the front-door note to add Graydon, Kilb, Lauderdale, Xie, and Voldsbekk.
- `wbe_101.md`
  - Rewrote the entry-point route-card note to include extracellular-space geometry / diffusion-barrier / osmotic-regime families.
  - Expanded the hidden-state table row so spillover and extracellular dilution remain explicit.
  - Added primary references for Graydon, Kilb, Lauderdale, Xie, Voldsbekk, Burman, and Feld.
- `verification.md`
  - Broadened the rule from `direct electrical observable` to `direct extracellular / electrical observable`.
  - Expanded the Observability Budget and maintenance-state budget rows with extracellular-space geometry, diffusion-barrier, and human diffusion-MRI proxy fields.
  - Rewrote the addendum and augmentation row accordingly.
- `wiki/connectome-is-not-enough.md`
  - Rebuilt the main section around `shared extracellular / electrical state` so ECS geometry is no longer hidden behind the electrical-coupling label.
  - Updated the route-card table with extracellular-space and diffusion-proxy rows.
  - Added the new primary references and upgraded the augmentation / ablation wording.
- `faq.md`
  - Tightened the front-door guardrails and short answer so readers cannot silently overread a chemical connectome as extracellular-state complete.
  - Added the new primary references for the FAQ evidence chain.

## External Dependency Tasks

- None.
  - This pass was fully executable as literature review, site revision, build verification, and repository update.

## References

1. Galarreta M, Hestrin S. A network of fast-spiking cells in the neocortex connected by electrical synapses. *Nature*. 1999;402:72-75.
   - https://doi.org/10.1038/47029
2. Anastassiou CA, Perin R, Markram H, Koch C. Ephaptic coupling of cortical neurons. *Nature Neuroscience*. 2011;14(2):217-223.
   - https://doi.org/10.1038/nn.2727
3. Graydon CW, Cho S, Diamond JS, Kachar B, von Gersdorff H, Grimes WN. Specialized postsynaptic morphology enhances neurotransmitter dilution and high-frequency signaling at an auditory synapse. *Journal of Neuroscience*. 2014;34(24):8358-8372.
   - https://doi.org/10.1523/JNEUROSCI.4493-13.2014
4. Kilb W, Dierkes PW, Syková E, Vargová L, Luhmann HJ. Hypoosmolar conditions reduce extracellular volume fraction and enhance epileptiform activity in the CA3 region of the immature rat hippocampus. *Journal of Neuroscience Research*. 2006;84(1):119-129.
   - https://doi.org/10.1002/jnr.20871
5. Xie L, Kang H, Xu Q, Chen MJ, Liao Y, Thiyagarajan M, O'Donnell J, Christensen DJ, Nicholson C, Iliff JJ, Takano T, Deane R, Nedergaard M. Sleep drives metabolite clearance from the adult brain. *Science*. 2013;342(6156):373-377.
   - https://doi.org/10.1126/science.1241224
6. Lauderdale K, Murphy T, Tung T, Davila D, Binder DK, Fiacco TA. Osmotic Edema Rapidly Increases Neuronal Excitability Through Activation of NMDA Receptor-Dependent Slow Inward Currents in Juvenile and Adult Hippocampus. *ASN Neuro*. 2015;7(5):1759091415605115.
   - https://doi.org/10.1177/1759091415605115
7. Burman RJ, Brodersen PJN, Raimondo JV, Sen A, Akerman CJ. Active cortical networks promote shunting fast synaptic inhibition in vivo. *Neuron*. 2023;111(22):3531-3540.e6.
   - https://doi.org/10.1016/j.neuron.2023.08.005
8. Yang Y-C, Wang G-H, Chou P, Hsueh S-W, Lai Y-C, Kuo C-C. Dynamic electrical synapses rewire brain networks for persistent oscillations and epileptogenesis. *Proceedings of the National Academy of Sciences of the United States of America*. 2024;121(8):e2313042121.
   - https://doi.org/10.1073/pnas.2313042121
9. Selfe JS, et al. All-optical reporting of inhibitory receptor driving force in the nervous system. *Nature Communications*. 2024;15(1):8913.
   - https://doi.org/10.1038/s41467-024-53074-y
10. Voldsbekk I, Maximov II, Zak N, Roelfs D, Geier O, Due-Tønnessen P, Elvsåshagen T, Strømstad M, Bjørnerud A, Groote I. Evidence for wakefulness-related changes to extracellular space in human brain white matter from diffusion-weighted MRI. *NeuroImage*. 2020;212:116682.
   - https://doi.org/10.1016/j.neuroimage.2020.116682
11. Feld GB, Niethard N, Liu J, et al. Electrical Synapses Contribute to Sleep-Dependent Declarative Memory Retention. *European Journal of Neuroscience*. 2026;63(2):e70401.
   - https://doi.org/10.1111/ejn.70401
