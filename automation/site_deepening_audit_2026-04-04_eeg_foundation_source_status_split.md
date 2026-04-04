# Site Deepening Audit: EEG foundation-model source-status split

Date: 2026-04-04

## Why this topic was selected

The EEG foundation-model front door was technically important and already cautious, but it still required readers to infer too much about the difference between three distinct source-status lanes:

1. peer-reviewed route papers,
2. official benchmark-operation pages that define the current executable benchmark object,
3. arXiv preprints that extend, warn about, or compare the frontier.

That hidden compression mattered because the claim ceiling changes across those lanes. A peer-reviewed transfer paper, an organizer postmortem, and an exploratory benchmark-warning preprint do not directly strengthen the same claim.

## Critical findings

### Finding 1: the FAQ still mixed route claims, benchmark operations, and exploratory warnings in one paragraph

`faq.md#q1c2` already separated representation learning, recording-frame compatibility, adaptation rescue, and benchmark governance. However, the page still left the reader to infer that Jiang 2024 / Lee 2025, EEG Challenge operational pages, and multiple arXiv papers should be read at different evidence strengths.

That was too weak for a front-door page. The official benchmark pages now materially change what the score means, so source status has to be explicit, not implied.

### Finding 2: the archive page exposed evidence class but not the source-status split inside the EEG-FM lane

`mind_uploading_papers.md` already links to the wiki page on source types and status labels, but the archive still benefited from one local rule that made the EEG foundation-model lane explicit:

- accepted proceedings set route claims,
- official benchmark pages set the current benchmark object and postmortem,
- arXiv papers remain exploratory extensions or warnings until narrowed by acceptance or independent reruns.

Without that local rule, the archive still risks being read as one homogeneous frontier stack.

### Finding 3: the landing page still needed one sentence making source-status visible

`index.md` already warned against overreading EEG foundation-model headlines, but the front-door note still let mixed source types sit too close together. A landing-page sentence was warranted because this is one of the highest-risk shortcut routes for new readers.

## Evidence base used for this audit

### Peer-reviewed route papers

- Jiang et al. (ICLR 2024): [official proceedings](https://proceedings.iclr.cc/paper_files/paper/2024/hash/47393e8594c82ce8fd83adc672cf9872-Abstract-Conference.html)
- Lee et al. (PMLR / ICML 2025): [official proceedings](https://proceedings.mlr.press/v267/lee25a.html)

These are the accepted-paper lane and are safe to cite as peer-reviewed route claims.

### Official benchmark-operation sources

- EEG Challenge homepage: [official site](https://eeg2025.github.io/)
- EEG Challenge data page: [official data page](https://eeg2025.github.io/data/)
- EEG Challenge rules: [official rules](https://eeg2025.github.io/rules/)
- EEG Challenge submission page: [official submission page](https://eeg2025.github.io/submission/)
- EEG Challenge leaderboard / organizer correction: [official leaderboard](https://eeg2025.github.io/leaderboard/)

These sources explicitly change the benchmark object by:

- marking the proposal preprint as out of date during execution,
- fixing the current rules snapshot and inference-stage constraints,
- disclosing the Challenge 2 randomization error and revised prize interpretation.

### Exploratory preprint / benchmark-warning lane

- Han et al. (2025), DIVER-0: [arXiv](https://arxiv.org/abs/2507.14141)
- Chen et al. (2025), HEAR: [arXiv](https://arxiv.org/abs/2510.12515)
- El Ouahidi et al. (2025), REVE: [arXiv](https://arxiv.org/abs/2510.21585)
- Ma et al. (2026), structured adaptation: [arXiv](https://arxiv.org/abs/2602.17251)
- Xiong et al. (2025/2026), EEG-FM-Bench: [arXiv](https://arxiv.org/abs/2508.17742)
- Liu et al. (2026), EEG foundation-model benchmarking survey: [arXiv](https://arxiv.org/abs/2601.17883)
- Lahiri et al. (2026), PRISM: [arXiv](https://arxiv.org/abs/2603.02268)

These sources are valuable, but they remain exploratory or warning-bearing unless reinforced by accepted publication or independent reruns.

## Changes executed in this session

### Public pages updated

- `faq.md`
  - Added an explicit source-status split for EEG foundation-model reading.
  - Added a three-row table separating peer-reviewed route papers, official benchmark operations/postmortems, and arXiv preprints.
  - Added a direct route to the wiki page on source types and status labels.

- `mind_uploading_papers.md`
  - Added a note box that fixes the EEG foundation-model source-status rule inside the archive itself.
  - Rewrote the recommended reading path for EEG foundation models so readers separate peer-reviewed route papers, official benchmark operations, and exploratory arXiv papers before reading rankings.

- `index.md`
  - Added one landing-page sentence making the source-status split visible in the EEG foundation-model warning box.

## External dependency tasks

None for this pass.

## Verification

- `bundle exec jekyll build`
- `git diff --check`

Both were run after the edits to confirm that the site still builds and that the patch introduced no whitespace or patch-format problems.
