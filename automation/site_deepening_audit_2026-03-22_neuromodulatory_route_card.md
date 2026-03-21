# Site Deepening Audit (2026-03-22, Neuromodulatory Route Card)

## Target

- Primary: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- Propagated rule changes: `verification.md`, `wbe_101.md`, `index.md`

## Why this topic was selected

- The site had already stated that `neuromodulation` remains a hidden-state family, but the public pages still treated it more loosely than adjacent topics such as myelin, ionic milieu, proteostasis, or clearance.
- In practice, a reader could still compress at least five different inferential objects into one label:
  - mixed arousal proxies such as pupil-linked covariation
  - local transmitter-sensor measurements
  - receptor / transporter atlas priors
  - occupancy PET under administered ligand
  - challenge-linked displacement / release-sensitive PET
- That compression is scientifically unsafe because the cited primary literature does not show that these rows share one direct observable, one time window, one spatial scope, or one claim ceiling.

## Evidence-backed critique

### 1. Mixed arousal proxies are not transmitter-specific state readouts

- Problem:
  - The site already warned that pupil or HRV should not be overread, but it still lacked a route card that prevented these covariates from being silently promoted to `current neuromodulatory state`.
- Evidence:
  - Reimer et al. (2016) showed that pupil fluctuations track both adrenergic and cholinergic cortical activity rather than a single transmitter-specific axis.
- Critique:
  - Therefore a pupil-linked result is a mixed arousal route, not a direct readout of a uniquely identified transmitter field.

### 2. Local cholinergic sensing is not the same object as atlas or PET evidence

- Problem:
  - Without an explicit route-card field, local ACh sensing can be conflated with receptor-density maps or human PET claims even though the measured objects differ sharply.
- Evidence:
  - Lohani et al. (2022) showed that cortical cholinergic coordination is spatially heterogeneous across behavioral states.
  - Neyhart et al. (2024) showed that cortical acetylcholine dynamics depend on both cholinergic axon activity and local clearance kinetics.
- Critique:
  - Therefore local transmitter sensing constrains a spatially and temporally bounded release-and-clearance regime, not a generic whole-brain neuromodulatory controller.

### 3. Human receptor / transporter atlases are regional priors, not current occupancy

- Problem:
  - The previous wording left too much room for a reader to treat chemoarchitectural maps as if they directly measured present receptor engagement or endogenous release.
- Evidence:
  - Hansen et al. (2022) constructed a normative PET-derived atlas of 19 receptors and transporters across more than 1,200 healthy individuals.
  - Goulas et al. (2021) described a natural axis of transmitter-receptor distribution in human cortex.
- Critique:
  - Therefore these papers constrain regional chemoarchitectural prior structure, not an individual's present receptor occupancy or momentary transmitter state.

### 4. Occupancy PET and displacement PET answer different questions

- Problem:
  - The site already named occupancy and displacement routes elsewhere, but the maintenance-state page still did not force a reader to say whether the PET design was about exogenous target engagement or endogenous challenge-linked release.
- Evidence:
  - Wong et al. (2013) quantified dopamine D2 receptor occupancy by lurasidone in healthy humans.
  - Koepp et al. (1998) used [11C]raclopride PET to infer task-linked endogenous dopamine release during a video game.
  - Lippert et al. (2019) showed time-dependent assessment of stimulus-evoked regional dopamine release.
  - Erritzoe et al. (2020) used [11C]CIMBI-36 with d-amphetamine challenge to estimate serotonin release in humans.
- Critique:
  - Therefore occupancy PET and challenge-linked displacement PET do not share one inferential object and should not be summarized as one generic `human neuromodulatory measurement`.

### 5. The missing route card weakened the human observability ladder

- Problem:
  - The site had already built a layered human-observability argument, but neuromodulatory evidence was underrepresented relative to its actual diversity and calibration burden.
- Evidence:
  - The cited papers span mixed proxy, local sensing, regional atlas, occupancy, and displacement designs, each with different model burden, spatial unit, and abstention boundary.
- Critique:
  - Therefore the site needed an explicit route card and corresponding observability / calibrator rows so that `neuromodulatory evidence exists` cannot be mistaken for `neuromodulatory state is directly measured`.

## Changes executed

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - Added new highlight / known-point / unknown-point entries so the neuromodulatory gap is visible in the page header.
  - Promoted neuromodulatory specificity into the page's short conclusion and maintenance-state table.
  - Added `#neuromodulatory-route-card` with explicit fields:
    - claim family
    - transmitter axis / receptor family
    - direct observable
    - driver / challenge route
    - quantification route / time window
    - spatial scope / calibrator role
    - abstention boundary
  - Added human observability rows for receptor / transporter atlas, occupancy PET, and displacement / release-sensitive PET.
  - Added calibrator-role matrix rows for those same three human routes.
  - Added primary references for Reimer, Lohani, Neyhart, Hansen, Goulas, Wong, Koepp, Lippert, and Erritzoe.
- `verification.md`
  - Added a page-highlight rule stating that neuromodulatory claims now require a route card.
  - Rewrote the neuromodulation addendum so submissions must disclose claim family, transmitter axis, direct observable, challenge / administered-drug route, time window / model burden, and abstention boundary.
- `wbe_101.md`
  - Added entry-level highlight and known-point bullets separating neuromodulatory evidence classes.
  - Added a note-box that points readers directly to the new neuromodulatory route card instead of leaving the front-door warning rhetorical.
  - Added missing references for Reimer and Neyhart in the public bibliography.
- `index.md`
  - Added a landing-page highlight separating neuromodulatory evidence families.
  - Strengthened the neuromodulation note so it cites representative primary papers and links directly to the new route card.

## Why this is better

- The site now criticizes neuromodulatory overclaim at the level where the mistake actually occurs: compression of distinct measurement classes into one inferred state.
- The public argument is more falsifiable because it now forces disclosure of the exact direct observable, perturbation regime, and model burden.
- The human observability ladder is more internally consistent because neuromodulatory evidence is now represented with the same route-card and calibrator discipline already applied to other maintenance-state families.

## External dependency kept separate

- Same-subject calibration benchmark for neuromodulatory claims
  - Owner: external PET / sensor / perturbation benchmark designers
  - Preconditions: same-subject datasets linking receptor atlas prior, occupancy PET, challenge-linked displacement PET, and an externally validated downstream target
  - Done when: the site can cite a public benchmark showing which human neuromodulatory proxy reduces which latent-state error term and under what perturbation regime

## References

1. Reimer J, McGinley MJ, Liu Y, et al. Pupil fluctuations track rapid changes in adrenergic and cholinergic activity in cortex. *Nature Communications*. 2016;7:13289.
   - https://doi.org/10.1038/ncomms13289
2. Lohani S, Moberly AH, Benisty H, et al. Spatiotemporally heterogeneous coordination of cholinergic and neocortical activity. *Nature Neuroscience*. 2022;25(12):1706-1713.
   - https://doi.org/10.1038/s41593-022-01202-6
3. Neyhart E, Zhou N, Munn BR, et al. Cortical acetylcholine dynamics are predicted by cholinergic axon activity and behavioral state. *Cell Reports*. 2024;43(10):114808.
   - https://doi.org/10.1016/j.celrep.2024.114808
4. Hansen JY, Shafiei G, Markello RD, et al. Mapping neurotransmitter systems to the structural and functional organization of the human neocortex. *Nature Neuroscience*. 2022;25(11):1569-1581.
   - https://doi.org/10.1038/s41593-022-01186-3
5. Goulas A, Changeux J-P, Wagstyl K, Amunts K, Palomero-Gallagher N, Hilgetag CC. The natural axis of transmitter receptor distribution in the human cerebral cortex. *Proceedings of the National Academy of Sciences USA*. 2021;118(3):e2020574118.
   - https://doi.org/10.1073/pnas.2020574118
6. Wong DF, Kuwabara H, Hsu DJ, et al. Determination of dopamine D2 receptor occupancy by lurasidone using positron emission tomography in healthy male subjects. *Psychopharmacology*. 2013;229(2):245-252.
   - https://doi.org/10.1007/s00213-013-3103-z
7. Koepp MJ, Gunn RN, Lawrence AD, et al. Evidence for striatal dopamine release during a video game. *Nature*. 1998;393(6682):266-268.
   - https://doi.org/10.1038/30498
8. Lippert RN, Cremer AL, Edwin Thanarajah S, et al. Time-dependent assessment of stimulus-evoked regional dopamine release. *Nature Communications*. 2019;10:336.
   - https://doi.org/10.1038/s41467-018-08143-4
9. Erritzoe D, Ashok AH, Searle GE, et al. Serotonin release measured in the human brain: a PET study with [11C]CIMBI-36 and d-amphetamine challenge. *Neuropsychopharmacology*. 2020;45(5):804-810.
   - https://doi.org/10.1038/s41386-019-0567-5
