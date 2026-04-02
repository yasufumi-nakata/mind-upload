# Site Deepening Audit (2026-04-02, EEG foundation setup compatibility vs physiology equivalence)

## 対象

- 主対象: `wiki/eeg-foundation-models.md`
- 副対象: `eeg_101.md`
- 整合性修正: `verification.md`

## 今回この箇所を選んだ理由

- `EEG foundation / self-supervised pretraining` 周辺はすでにかなり整っておりましたが、なお 1 つ重要な圧縮が残っておりました。
- それは、`arbitrary electrode layouts` や `heterogeneous devices` に対応できることが、そのまま `one shared physiology-preserving representation` へ読まれうる点でございます。
- 技術・自然科学の観点では、ここを止めないと `recording-frame compatibility` と `physiology-side equivalence` が混ざります。
- 2025-2026 の一次ソースは、この 2 つをまだ同一視できないことをむしろ強く示しております。

## web確認対象

- `https://arxiv.org/abs/2507.14141`
- `https://arxiv.org/abs/2510.12515`
- `https://arxiv.org/abs/2510.21585`
- `https://arxiv.org/abs/2602.17251`
- `https://arxiv.org/abs/2603.02268`
- `https://arxiv.org/abs/2601.17883`
- `https://proceedings.mlr.press/v267/lee25a.html`
- `https://eeg2025.github.io/`
- `https://eeg2025.github.io/rules/`
- `https://eeg2025.github.io/submission/`
- `https://eeg2025.github.io/leaderboard/`

## 根拠付き批判

### 1. heterogeneous-layout support は physiology equivalence ではございません

- 根拠:
  - Han et al. (2025) は `channel permutation equivariance` を明示的な技術課題として置いております。
  - Chen et al. (2025) は `heterogeneous EEG devices` と `varying electrode layouts / counts` を直接の対象として、`coordinate-based spatial embedding` を導入しております。
  - El Ouahidi et al. (2025) は `arbitrary length and electrode arrangement` を扱う大規模 pretraining を前面に出しております。
- 批判:
  - したがって、現在の前進はまず `different sensor organizations can be processed more coherently` という recording-side の前進であり、`different montages now preserve one common physiology automatically` を意味しません。
  - 特に `electrode-coordinate route`、`reference family`、`omitted/interpolated channel policy` を明示しない限り、layout robustness を physiology robustness に言い換えることはできません。

### 2. label-limited deployment burden は setup compatibility とは別問題でございます

- 根拠:
  - Ma et al. (2026) は、EEG foundation models が `subject-level supervision is limited` な条件で一般化不良を起こすと述べ、追加の structured adaptation を導入しております。
  - Liu et al. (2026) も `leave-one-subject-out` と `within-subject few-shot` を分けて評価しております。
- 批判:
  - よって、`works across layouts` と `works when labels are scarce` は別の能力でございます。
  - 前者だけをもって deployment-ready な transfer と読むのは、適応負担を隠した過読でございます。

### 3. benchmark reversal は architecture だけでなく comparison regime の問題でもございます

- 根拠:
  - Lahiri et al. (2026) は `split construction`、`checkpoint selection`、`segment length`、`normalization` が比較結果を大きく動かしうることを示しております。
  - EEG Challenge 2025 の公式 leaderboard は Challenge 2 に sample randomization の問題があったことを後から明示しております。
  - Lee et al. (2025) は current LBMs の gain を `0.5%` 程度の marginal improvement とし、LoRA による parameter-efficiency も示しております。
- 批判:
  - したがって、heterogeneous-device paper の score improvement を architecture 固有の frontier gain と読む前に、comparison regime と operations budget を分離しなければなりません。

### 4. 既存サイトの harmonization gate は少し粗く、geometry route を隠しやすい状態でした

- 根拠:
  - 旧 wording は `channel mapping / reference / sample rate / normalization` まではよく見えておりました。
  - しかし、2025-2026 の heterogeneous-device papers では、`coordinate-based embedding` や `channel-permutation equivariance` そのものが主要設計点になっております。
- 批判:
  - よって `harmonization` の中に geometry 問題を埋めるだけでは弱く、少なくとも `geometry route / reference family / omitted-channel policy` を公開上で見えるようにする必要がございました。

## 今回実行した変更

- `wiki/eeg-foundation-models.md`
  - `last_updated` を `2026-04-02` に更新
  - page highlights / known / unknown に `setup compatibility != physiology equivalence` を追加
  - 新規 note box `A unified spatial embedding is not yet a common physiological coordinate system` を追加
  - 新規 section `2026-04-02 correction: setup compatibility is not physiological equivalence` を追加
  - G3 を `harmonization / geometry route` へ改稿
  - Pretraining Card の harmonization row を `coordinate route / reference family / omitted-channel policy` を含む形へ改稿
  - operating rules に heterogeneous-device support の停止線を追加
  - 参考文献に DIVER-0 / HEAR / SCOPE を追加
- `eeg_101.md`
  - `last_updated` を `2026-04-02` に更新
  - front-door highlights / known / unknown を更新
  - foundation-model note を改稿し、DIVER-0 / HEAR / SCOPE を用いて
    - recording-frame compatibility
    - coordinate route
    - reference family
    - omitted-channel policy
    - label-limited adaptation burden
    を分離
  - references に DIVER-0 / HEAR / SCOPE を追加
- `verification.md`
  - `last_updated` を `2026-04-02` に更新
  - top highlight と Pretraining Card harmonization row を公開 rule に合わせて改稿

## 今回止めた誤読

- `arbitrary-layout support = one shared physiology-preserving representation`
- `heterogeneous-device support = reference-invariant transfer`
- `layout robustness = label-limited deployment readiness`
- `benchmark reversal is mainly model quality reversal`
- `harmonization disclosure があれば geometry route disclosure は不要`

## 検証結果

- これから以下を実行して確認いたします
  - `git diff --check`
  - `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
  - `env GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT=1 ruby scripts/check_github_wiki_export.rb`
  - `env VERIFY_GITHUB_WIKI_BUILD=1 ./scripts/verify_github_wiki_toolchain.sh`

## 外部依存タスク

- なし
  - 今回の変更は一次ソース確認、公開文面更新、検証、commit、push までこのセッションで完結可能でございます。

## 参考文献

1. Han DD, Lee AL, Lee T, Gwon Y, Lee S, Lee S, Park DK, Yoo S, Cha J, Chung CK. DIVER-0: A Fully Channel Equivariant EEG Foundation Model. *ICML 2025 Workshop on GenBio / arXiv*. 2025.
   - https://arxiv.org/abs/2507.14141
2. Chen Z, Qin C, You W, Liu R, Chu C, Yang R, Tan KC, Wu J. HEAR: An EEG Foundation Model with Heterogeneous Electrode Adaptive Representation. *arXiv*. 2025.
   - https://arxiv.org/abs/2510.12515
3. El Ouahidi Y, Lys J, Thölke P, Farrugia N, Pasdeloup B, Gripon V, Jerbi K, Lioi G. REVE: A Foundation Model for EEG -- Adapting to Any Setup with Large-Scale Pretraining on 25,000 Subjects. *arXiv*. 2025.
   - https://arxiv.org/abs/2510.21585
4. Ma J, Wu F, Xing Y, Lin Q, Liu T, Liu C, Jia Z, Feng M. Structured Prototype-Guided Adaptation for EEG Foundation Models. *arXiv*. 2026.
   - https://arxiv.org/abs/2602.17251
5. Lahiri JB, Runwal P, Kulkarni A, Jain M, Mishra AR, Panwar S, Singh S. PRISM: Exploring Heterogeneous Pretrained EEG Foundation Model Transfer to Clinical Differential Diagnosis. *arXiv*. 2026.
   - https://arxiv.org/abs/2603.02268
6. Liu D, Chen Y, Chen Z, Cui Z, Wen Y, An J, Luo J, Wu D. EEG Foundation Models: Progresses, Benchmarking, and Open Problems. *arXiv*. 2026.
   - https://arxiv.org/abs/2601.17883
7. Lee N, Barmpas K, Panagakis Y, Adamos D, Laskaris N, Zafeiriou S. Are Large Brainwave Foundation Models Capable Yet? Insights from Fine-Tuning. *Proceedings of the 42nd International Conference on Machine Learning*. 2025.
   - https://proceedings.mlr.press/v267/lee25a.html
8. EEG Foundation Challenge (2025). Official homepage.
   - https://eeg2025.github.io/
9. EEG Foundation Challenge (2025). Rules.
   - https://eeg2025.github.io/rules/
10. EEG Foundation Challenge (2025). Submission.
   - https://eeg2025.github.io/submission/
11. EEG Foundation Challenge (2025). Leaderboard.
   - https://eeg2025.github.io/leaderboard/
