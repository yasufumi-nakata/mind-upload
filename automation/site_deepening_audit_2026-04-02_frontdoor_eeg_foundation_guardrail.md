# Site Deepening Audit (2026-04-02, front-door EEG foundation-model guardrail)

## Target

- Primary targets: `index.md`, `faq.md`, `datasets.md`
- Scope: public-facing front-door explanations only
- Explicitly out of scope for this run: `issue.md` (per user instruction), philosophy, law

## Why this gap was selected

The repository already had a strong internal treatment of EEG foundation models in `wiki/eeg-foundation-models.md`, `eeg_101.md`, and `verification.md`. However, the shorter public entry pages still left one important overread too easy:

- `heterogeneous-device support` could still sound too close to `physiology-preserving equivalence`
- `benchmark win` could still sound too close to `portable general decoder`
- `works across layouts` could still sound too close to `works under label-limited subject-level deployment`

For a front-door page, that is a real technical problem. Readers who stop early can inherit the wrong ceiling before they ever reach the stricter wiki or verification cards.

## Web-verified primary sources checked on 2026-04-02

- Han et al. (2025), DIVER-0: `https://arxiv.org/abs/2507.14141`
- Chen et al. (2025), HEAR: `https://arxiv.org/abs/2510.12515`
- El Ouahidi et al. (2025), REVE: `https://arxiv.org/abs/2510.21585`
- Ma et al. (2026), structured prototype-guided adaptation: `https://arxiv.org/abs/2602.17251`
- Lahiri et al. (2026), PRISM: `https://arxiv.org/abs/2603.02268`
- Liu et al. (2026), EEG foundation-model benchmarking: `https://arxiv.org/abs/2601.17883`
- Lee et al. (2025), fine-tuning audit: `https://proceedings.mlr.press/v267/lee25a.html`
- EEG Challenge official homepage: `https://eeg2025.github.io/`
- EEG Challenge rules: `https://eeg2025.github.io/rules/`
- EEG Challenge submission page: `https://eeg2025.github.io/submission/`
- EEG Challenge leaderboard: `https://eeg2025.github.io/leaderboard/`

## Evidence-backed critique

### 1. Setup compatibility is a recording-frame advance, not yet a physiology-equivalence proof

- Han et al. (2025) center `channel permutation equivariance`.
- Chen et al. (2025) center `coordinate-based spatial embedding` across heterogeneous devices and more than 150 layouts.
- El Ouahidi et al. (2025) center large-scale `any-setup` pretraining across 92 datasets and more than 60,000 hours.

These are meaningful advances. But they are advances in handling heterogeneous recording frames. They do not by themselves prove that different montage choices, coordinate routes, and reference families already preserve one shared physiology-side representation.

### 2. Label-limited deployment burden remains a separate failure mode

- Ma et al. (2026) report that strong EEG foundation models can still generalize poorly when subject-level supervision is limited unless extra adaptation structure is added.
- Liu et al. (2026) separately benchmark leave-one-subject-out transfer and within-subject few-shot calibration.

Therefore, `works across layouts` and `works when labeled subject data are scarce` are different claims. A front-door summary that omits the second claim invites overreading.

### 3. Benchmark governance still changes what a leaderboard means

- The EEG Challenge homepage explicitly says the proposal preprint became out of date during execution and that the website plus Starter Kit should be treated as current.
- The rules and submission workflow fix an inference-stage code-submission regime plus a single-GPU 20 GB constraint.
- The final leaderboard states that the organizers failed to randomize Challenge 2 samples and then changed prize interpretation accordingly.

This means benchmark governance is not administrative detail. It is part of the scientific reading of the score.

## Changes executed in this run

- `index.md`
  - tightened front-matter guardrails for EEG foundation-model reading
  - rewrote the front-door note box so it now separates recording-frame compatibility, physiology-side equivalence, label-limited adaptation burden, and benchmark governance
- `faq.md`
  - tightened front-matter summary bullets
  - strengthened `Q1c2` so it now explicitly blocks `layout support = general decoder` and `layout support = physiology-equivalent representation`
  - extended the stop-rule sentence to require coordinate route, reference family, omitted-channel policy, and label budget disclosure
  - added the new primary references used in this pass
- `datasets.md`
  - tightened the page highlight for EEG foundation/self-supervised model usage
  - added a new 2026-04-02 addendum that separates setup diversity from physiology-equivalent transfer and deployment readiness
  - tightened the site rule to require coordinate-route and omitted-channel disclosure
  - added the new primary references and official challenge pages used in this pass

## Misreads blocked by this update

- `arbitrary-layout support = shared physiology-preserving coordinate system`
- `heterogeneous-device support = reference-invariant transfer`
- `works across setups = label-limited deployment readiness`
- `leaderboard strength = portable general EEG decoder`
- `benchmark governance = administrative detail`

## Verification results

- `git diff --check` -> passed
- `bundle exec jekyll build` -> passed
- `env GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT=1 ruby scripts/check_github_wiki_export.rb` -> passed
- `env VERIFY_GITHUB_WIKI_BUILD=1 ./scripts/verify_github_wiki_toolchain.sh` -> passed

## External dependency tasks

- None
  - This run stayed inside the current session boundary: literature check, public-page revision, verification, commit, and push.
