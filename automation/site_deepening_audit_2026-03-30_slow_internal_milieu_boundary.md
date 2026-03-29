# Site Deepening Audit (2026-03-30, Slow Internal-Milieu Boundary)

## Scope

- Primary target: `verification.md`
- Secondary targets: `wbe_101.md`, `tech_roadmap.md`, `faq.md`
- Companion wiki target: `wiki/closed-loop-latency-jitter-and-safety-stops.md`

## Why This Topic Was Chosen

- The public site had already become strong at separating fast loop variables such as latency, tactile feedback, self-motion, respiration, and arousal from stronger embodiment claims.
- However, the same public rule still left a slower class undernamed: `slow internal milieu`, especially circadian phase, glucocorticoid state, and insulin / metabolic regime.
- This gap matters technically because it leaves room to overread a stable local closed loop as if the relevant biological operating regime had been matched, when the primary literature shows that hippocampal retrieval, plasticity, and human memory can change under those slower body-state variables without any change in the visible fast I/O contract.

## Evidence-Based Critique

### 1. The existing Body / Environment Boundary Card stopped too early at fast loop covariates

- Problem:
  - The live site required disclosure of sensory, motor, interoceptive, and surrogate-body routes.
  - It did not yet require a dedicated row for slow internal-milieu variables such as circadian phase, corticosteroid exposure, or insulin / feeding regime.
- Why this is technically weak:
  - `same actuator + same task + same latency` does not imply `same hippocampal operating regime`.
  - The omission made it too easy to treat slow endocrine and circadian state as mere nuisance background rather than as independent state-setting variables.
- Primary evidence:
  - de Quervain et al. (1998) showed that glucocorticoids impair memory retrieval.
  - Oei et al. (2007) showed hydrocortisone-linked decreases in human hippocampal and prefrontal retrieval activity.

### 2. The front-door L3 explanation risked reducing boundary disclosure to respiration, arousal, and feedback only

- Problem:
  - The front-door pages correctly said that low latency does not solve the body/environment boundary.
  - But the examples visible at the front door were still dominated by movement, multisensory cues, respiration, arousal, and tactile feedback.
- Why this is technically weak:
  - That wording could still let a reader conclude that once those faster routes are logged, the rest of the biological boundary is already mostly fixed.
  - The primary literature does not support that shortcut.
- Primary evidence:
  - McCauley et al. (2020) showed circadian modulation of neurons and astrocytes controls CA1 plasticity.
  - Barone et al. (2023) showed BMAL1-linked circadian gating of hippocampal synaptic plasticity and long-term memory.
  - Birnie et al. (2023) showed that corticosteroid treatment disrupts circadian regulation of hippocampal function and impairs hippocampal-dependent memory.

### 3. Human-facing observability rules undernamed slow internal-milieu proxies and perturbations

- Problem:
  - The site already gave careful names to PET, MRSI, BBB, myelin, and glymphatic proxy classes.
  - It did not yet give equally explicit logging rules for slow internal-milieu human evidence.
- Why this is technically weak:
  - Human evidence for this layer exists, but it is heterogeneous and ceiling-limited.
  - Without an explicit logging rule, cortisol assays, clock-time labels, actigraphy-derived circadian consistency, and intranasal-insulin interventions can be silently mixed or ignored.
- Primary evidence:
  - Benedict et al. (2004) showed that intranasal insulin improves declarative memory in humans.
  - Reger et al. (2008) showed dose-dependent memory effects of intranasal insulin in memory-impaired older adults.
  - Sherman et al. (2015) showed that more consistent circadian activity rhythms are associated with better associative memory and stronger hippocampal activity in older adults.

## Changes Executed In This Session

- `verification.md`
  - Expanded the Body / Environment Boundary Card so it now explicitly covers `slow internal-milieu / circadian / endocrine-metabolic routes`.
  - Added a new operating note that separates fast-loop disclosure from slow internal-milieu disclosure.
  - Updated page highlights and known-points text so `low latency != solved body/environment boundary` now includes the slow-milieu ceiling.
- `wbe_101.md`
  - Strengthened the front-door L3 note so it now names circadian, glucocorticoid, and insulin / metabolic routes as additional boundary variables.
  - Updated top-level highlights and known points accordingly.
- `tech_roadmap.md`
  - Upgraded M4 and V2 wording so body/environment disclosure now includes slow internal-milieu routes, not only fast sensory / motor / interoceptive loops.
- `faq.md`
  - Tightened the short answer on low latency so it explicitly blocks overreading when circadian or endocrine-metabolic state was not disclosed.
- `wiki/closed-loop-latency-jitter-and-safety-stops.md`
  - Added the slow internal-milieu layer to the timing-side companion page.
  - Extended the boundary table, minimum-log checklist, and reading questions so readers are forced to ask about circadian phase, glucocorticoid state, and insulin / metabolic regime.

## External Dependency Tasks

- None.
  - This session only required literature review, public rule revision, and repository updates that were executable locally.

## References

1. de Quervain DJ, Roozendaal B, McGaugh JL. Stress and glucocorticoids impair retrieval of long-term spatial memory. *Nature*. 1998;394(6695):787-790.
   - https://doi.org/10.1038/29542
2. Oei NYL, Elzinga BM, Wolf OT, de Ruiter MB, Damoiseaux JS, Kuijer JPA, Veltman DJ, Scheltens P, Rombouts SARB. Glucocorticoids decrease hippocampal and prefrontal activation during declarative memory retrieval in young men. *Brain Imaging and Behavior*. 2007;1(1-2):31-41.
   - https://doi.org/10.1007/s11682-007-9003-2
3. McCauley JP, Petroccione MA, D'Brant LY, et al. Circadian modulation of neurons and astrocytes controls synaptic plasticity in hippocampal area CA1. *Cell Reports*. 2020;33(2):108255.
   - https://doi.org/10.1016/j.celrep.2020.108255
4. Barone I, Gilette NM, Hawks-Mayer H, et al. Synaptic BMAL1 phosphorylation controls circadian hippocampal plasticity. *Science Advances*. 2023;9(43):eadj1010.
   - https://doi.org/10.1126/sciadv.adj1010
5. Birnie MT, Begum G, Sugden D, et al. Circadian regulation of hippocampal function is disrupted with corticosteroid treatment. *Proceedings of the National Academy of Sciences of the United States of America*. 2023;120(15):e2211996120.
   - https://doi.org/10.1073/pnas.2211996120
6. Benedict C, Hallschmid M, Hatke A, Schultes B, Fehm HL, Born J, Kern W. Intranasal insulin improves memory in humans. *Psychoneuroendocrinology*. 2004;29(10):1326-1334.
   - https://doi.org/10.1016/j.psyneuen.2004.04.003
7. Reger MA, Watson GS, Green PS, et al. Intranasal insulin administration dose-dependently modulates verbal memory and plasma amyloid-beta in memory-impaired older adults. *Journal of Alzheimer's Disease*. 2008;13(3):323-331.
   - https://doi.org/10.3233/JAD-2008-13309
8. Sherman SM, Mumford JA, Schnyer DM. Hippocampal activity mediates the relationship between circadian activity rhythms and memory in older adults. *Neuropsychologia*. 2015;75:617-625.
   - https://doi.org/10.1016/j.neuropsychologia.2015.07.020
