# Site Deepening Audit (2026-03-28, verification walkthrough route-card stack)

## 対象

- 主対象: `wiki/verification-example-walkthrough.md`

## web確認対象

- `https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/events.html`
- `https://doi.org/10.1038/s41597-025-05791-2`
- `https://doi.org/10.1162/IMAG.a.136`
- `https://doi.org/10.3758/s13428-024-02508-y`
- `https://doi.org/10.1038/s41746-019-0178-x`
- `https://doi.org/10.3389/fnhum.2021.672946`
- `https://doi.org/10.3389/fnhum.2020.00103`
- `https://doi.org/10.1038/s41598-024-70609-x`
- `https://doi.org/10.1080/01621459.2017.1307116`

## 今回この箇所を選んだ理由

- `wiki/verification-example-walkthrough.md` は `last_updated: 2026-03-14` のままで、現行 site-wide ルールより一世代古い tutorial になっていました。
- 問題は単に古いことではありません。このページは `verification.md` の抽象度を下げる入口ですので、ここが古いと、`event contract`、`shortcut audit`、`temporal validity`、`calibration / abstention` などの厳格化を入口で再び弱めてしまいます。
- 技術・自然科学の観点では、この弱点は大きいです。なぜなら、初学者は最初の worked example を “最小十分条件” として覚えるため、ここで `BIDS + split + score` を教えると、現在の一次文献が止めている誤読を site 自身が再注入してしまうからです。

## 根拠付き批判

### 1. 旧 walkthrough は `4要素` のままで、現行の route-card stack を教えていませんでした

- 根拠:
  - BIDS events specification は `onset` を「対応する task data file に保存された最初の data point からの時刻」と定義しており、physical onset truth そのものではありません。
  - Hermes et al. (2025) は HED-SCORE schema により EEG event annotation の machine-readability を強めましたが、これは semantics の前進であり、timing truth の保証ではありません。
  - Kothe et al. (2025) は LSL を LAN 上の software-based synchronization として位置づけ、offset correction / jitter compensation を支える一方、device-side delay や actual output timing を自動で真値化するものではないことを明示しました。
- 批判:
  - したがって tutorial が `BIDS format + event definitions` だけを Step 1 として教えるのは、今の site rule では弱いです。
  - 現在の最小 tutorial には、少なくとも `event contract`、`observability budget`、`shortcut audit` を明示して、`input shape` と `claim ceiling` を分けて教える必要があります。

### 2. 旧 walkthrough は `subject/session split` を temporal validity や identity confounding から切り離していました

- 根拠:
  - Chaibub Neto et al. (2019) は、repeated measurements を record-wise split すると classifier が subject identification を学び、prediction error を大きく過小評価しうることを示しました。
  - Di et al. (2021) は resting-state EEG の individual identification が、少なくとも 2 週間以上離れた 3 回の recording でも高精度に保たれうることを示しました。
  - Xu et al. (2020) は cross-dataset EEG decoding が amplifier, cap, sampling rate, filtering などの environmental variability によって劣化することを示しました。
- 批判:
  - したがって `train/validation/test を分けた` だけでは、target neural variable を読んだのか、subject / session fingerprint や acquisition-distribution shortcut を読んだのかが分かりません。
  - tutorial は `independent hold-out unit`、`raw-recording ancestry`、`metadata-only or identity baseline`、`setup disjointness` を最初から要求すべきでした。

### 3. 旧 walkthrough は same-session score を temporal claim から十分に切り離していませんでした

- 根拠:
  - Egger et al. (2024) は hand-gesture EEG を 10 時間スケールで追い、2 p.m. から 12 a.m. にかけて MRCP dynamics と decoding performance が変化することを示しました。
  - 同論文では、更新しない classifier では性能が連続的に低下し、更新戦略と固定戦略が同じ achievement ではないことが示されています。
- 批判:
  - したがって `small EEG classification example` でも、same-session success と cross-session durability を同じ欄で教えるべきではありません。
  - tutorial には `temporal scope`、`fixed decoder interval`、`state annotation`、`recalibration burden` を最低限の列として入れる必要がありました。

### 4. 旧 walkthrough は calibration / abstention を欠いたまま score を閉じていました

- 根拠:
  - Lei et al. (2018) は split conformal inference を含む distribution-free predictive inference を整理し、fit と calibration の分離が coverage interpretation に必要であることを示しました。
  - site 本体でも 2026-03 時点で `Calibration & Abstention Card` を minimum submission として固定しています。
- 批判:
  - したがって `accuracy + confusion matrix + failure examples` だけで tutorial を閉じるのは、現在の運用水準では弱いです。
  - probability, prediction set, reject option, or thresholded output を少しでも扱うなら、fit / calibration / test separation と abstention policy を明示しなければなりません。

### 5. 旧 walkthrough は EEG decode の claim ceiling を tutorial 内で明示していませんでした

- 根拠:
  - BIDS / HED / LSL / timing-validation literature は observation contract を強めますが、それだけで causal or hidden-state claim を可能にするわけではありません。
  - Chaibub Neto et al. (2019), Di et al. (2021), Xu et al. (2020), Egger et al. (2024) は、split hygiene, shortcut resistance, temporal validity が別々の stop line であることを示しています。
- 批判:
  - したがって、この tutorial が最後に明示すべき strongest safe claim は `bounded reproducible EEG decode under a named observation contract` であって、`stable biomarker` や `state readout` ではありません。

## 今回実行した変更

- `wiki/verification-example-walkthrough.md`
  - `last_updated` を `2026-03-28` に更新
  - front matter の `description` / `page_intro` / `page_highlights` / `known_points` を、現行の verification stack に同期
  - tutorial の骨格を `core scaffold` と `companion cards` に再編
  - Step 1 を `input + event contract` へ改稿し、
    - BIDS event anchor
    - HED semantics
    - clock domain
    - timing-validation class
    - label provenance
    を分離
  - Step 2 を `benchmark object + independence unit` へ改稿し、
    - raw-recording ancestry
    - subject / session / site / device / reference disjointness
    - metadata-only / identity baseline
    - temporal scope
    を追加
  - Step 3 を `registry before training` へ改稿し、stopping claim と fit / calibration / test split を明記
  - Step 4 を新設し、tutorial でも
    - Observability Budget
    - Specificity & Shortcut Card
    - Temporal Validity note
    - Calibration & Abstention note
    を積む構造に変更
  - Step 5 を `model card + failure ledger` へ改稿し、calibration / abstention / failure slice を追加
  - `What this example supports / still does not support` table を新設
  - references を一次文献ベースで追加

## 今回の修正で止めた誤読

- `BIDS events がある` = `timing も semantics も solved`
- `subject/session split をした` = `identity confounding が解けた`
- `same-session EEG score` = `cross-day durability`
- `accuracy + confusion matrix を出した` = `uncertainty / abstention まで十分`
- `small EEG tutorial` = `state-specific biomarker or hidden-state readout`

## 外部依存タスク

- なし
  - 今回の変更は、公開 tutorial と監査記録の更新で完結しています。

## 参考文献

1. Brain Imaging Data Structure. Events.
   - https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/events.html
2. Hermes D, Pal Attia T, Beniczky S, et al. Hierarchical Event Descriptor library schema for EEG data annotation. *Scientific Data*. 2025.
   - https://doi.org/10.1038/s41597-025-05791-2
3. Kothe C, et al. The Lab Streaming Layer for synchronized multimodal recording. *Imaging Neuroscience*. 2025.
   - https://doi.org/10.1162/IMAG.a.136
4. Lepauvre A, Hirschhorn R, Bendtz K, Mudrik L, Melloni L. A standardized framework to test event-based experiments. *Behavior Research Methods*. 2024.
   - https://doi.org/10.3758/s13428-024-02508-y
5. Chaibub Neto E, et al. Detecting the impact of subject characteristics on machine learning-based diagnostic applications. *npj Digital Medicine*. 2019;2:99.
   - https://doi.org/10.1038/s41746-019-0178-x
6. Di Y, et al. The Time-Robustness Analysis of Individual Identification Based on Resting-State EEG. *Frontiers in Human Neuroscience*. 2021;15:672946.
   - https://doi.org/10.3389/fnhum.2021.672946
7. Xu L, et al. Cross-Dataset Variability Problem in EEG Decoding With Deep Learning. *Frontiers in Human Neuroscience*. 2020;14:103.
   - https://doi.org/10.3389/fnhum.2020.00103
8. Egger J, et al. Chrono-EEG dynamics influencing hand gesture decoding: a 10-hour study. *Scientific Reports*. 2024;14:20247.
   - https://doi.org/10.1038/s41598-024-70609-x
9. Lei J, G'Sell M, Rinaldo A, Tibshirani RJ, Wasserman L. Distribution-Free Predictive Inference for Regression. *Journal of the American Statistical Association*. 2018;113(523):1094-1111.
   - https://doi.org/10.1080/01621459.2017.1307116
