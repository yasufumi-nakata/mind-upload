# Site Deepening Audit (2026-03-21, Temporal Validity / State-Trait-Drift Sync)

## 対象

- 主対象: `wiki/state-trait-and-drift.md`
- 参照整合先: `verification.md`, `index.md`, `eeg_101.md`, `datasets.md`

## 今回の選定理由

- 2026-03-21 時点で、公開コアページ側には `Temporal Validity Card` がすでに導入されており、`fixed decoder interval`、`state annotation`、`interface / decoder drift`、`recalibration burden`、`transfer ceiling` を分ける site rule が前面化されていました。
- その一方で、背景説明を担う `wiki/state-trait-and-drift.md` は 2026-03-14 更新のままで、なお `state / trait / drift` の概念整理が中心で、カードの 5 項目を十分には分解できていませんでした。
- この不整合は技術・自然科学の観点で重要です。理由は、補助ページが古いままだと、読者が `same-day success`、`algorithmic stabilization`、`long-term deployability` を一つの連続的成功物語として読みやすくなるからです。

## 根拠付き批判

### 1. 旧ページは `fixed decoder durability` と `algorithmic rescue` をまだ十分に分けていませんでした

- 問題:
  - 旧 `wiki/state-trait-and-drift.md` は `fixed decoder degradation` と `recalibration burden` を挙げていました。
  - しかし、`何日間まったく更新せずに持ったか` と、`latent alignment や unsupervised recalibration によって維持したか` を別の claim object として固定していませんでした。
- 根拠:
  - Karpowicz et al. (2025) は latent dynamics alignment により BCI 安定化を示しましたが、これは drift 不在の証明ではなく `alignment-based rescue` です。
  - Wilson et al. (2025) は hidden Markov model による long-term unsupervised recalibration を示し、長期使用には drift 吸収の運用が必要であることを示しました。
- 批判:
  - したがって、`system stayed usable` と `original decoder stayed valid` は同じではありません。
  - 旧ページはこの差を明示しておらず、Temporal Validity Card の実務ルールより弱い説明に留まっていました。

### 2. 旧ページは `state annotation` を独立提出物として十分に押し出していませんでした

- 問題:
  - 旧ページは arousal や spontaneous behavior を扱っていましたが、`time-of-day / within-day context` を含む state annotation を明示的な提出欄として固定していませんでした。
- 根拠:
  - Musall et al. (2019) は uninstructed movement が cortex-wide neural activity を強く規定することを示しました。
  - Benisty et al. (2024) は spontaneous behavior が activity magnitude だけでなく functional-connectivity structure を急速に変えることを示しました。
  - Egger et al. (2024) は 10 時間スケールで MRCP dynamics が変動し、robust decoding には adaptive decoder が必要だと示しました。
- 批判:
  - したがって、same-day / cross-day の差を読む前に `その時どういう state だったか` を書かないのは粗すぎます。
  - 旧ページのままでは、state fluctuation を background note として読んでしまい、Temporal Validity Card の `state annotation` 欄が軽く見えてしまいます。

### 3. 旧ページは `transfer ceiling` を明示的な stop line として持っていませんでした

- 問題:
  - speech / cursor BCI の longitudinal success を読んだとき、`one participant`、`one implant`、`one task family`、`one site` といった ceiling を一文で止める規則が弱めでした。
- 根拠:
  - Littlejohn et al. (2025) は streaming brain-to-voice neuroprosthesis を示しました。
  - Wairagkar et al. (2025) は instantaneous voice-synthesis neuroprosthesis を示し、silence handling と fixed-decoder degradation を明示しました。
- 批判:
  - これらは強い communication-route progress ですが、generic transfer や indefinite fixed-decoder durability の証拠ではありません。
  - したがって `transfer ceiling` を独立欄にしなければ、読者は participant-specific success を過大読みにしやすいです。

### 4. trait 説明はあっても、`named backbone object` がまだ弱かったです

- 問題:
  - 旧ページは `trait-like backbone` を導入していましたが、提出時に `何を backbone と呼んだのか` を名前付きで固定する規則が弱めでした。
- 根拠:
  - Gallego et al. (2020) は aligned latent dynamics を支持しました。
  - Roth & Merriam (2023) は human V1 の representational drift を示しつつ relational structure の相対的安定性を示しました。
  - Noda et al. (2025) は single-neuron volatility と population map homeostasis の併存を示しました。
- 批判:
  - したがって `trait` は、単なる長期安定の形容詞ではなく、`latent dynamics`、`representational geometry`、`functional fingerprint` など named backbone object として提出させる必要があります。

## 今回実行した変更

- `wiki/state-trait-and-drift.md`
  - `last_updated` を `2026-03-21` に更新しました。
  - front matter の `page_highlights` / `known_points` / `unknown_points` を `Temporal Validity Card` の 5 項目へ同期しました。
  - 冒頭に `same-day success`、`algorithmic rescue`、`long-term stability` を分ける要約を追加しました。
  - 新規 section `The five fields this site now audits for time validity` を追加し、
    - fixed decoder interval
    - state annotation
    - interface / decoder drift
    - recalibration burden
    - transfer ceiling
    を独立欄として定義しました。
  - `Why the old three-way split is not enough` で、state fluctuation / trait-like backbone / biological drift / interface-drift の 4 層を再定義しました。
  - primary-literature section を更新し、Musall / Benisty / Egger / Gallego / Finn / Roth / Noda / Karpowicz / Wilson / Littlejohn / Wairagkar をもとに、
    - state annotation の必須性
    - backbone の named-object 化
    - stabilization と fixed-decoder durability の分離
    - participant-specific success と transfer ceiling の分離
    を明文化しました。
  - `Minimum submission` と `Common misreadings` を全面更新し、Temporal Validity Card の背景ページとして読める形へ再構成しました。

## 外部依存で保留

- cross-modal longitudinal benchmark の共通 schema 実装
  - 担当者: 実験系共同研究者 / benchmark 設計者 / maintainer
  - 前提条件: EEG、侵襲 BCI、speech neuroprosthesis などで、state annotation / fixed decoder interval / recalibration burden / transfer ceiling を同一 schema で公開するデータ
  - 完了条件: modality をまたいで temporal-validity fields を直接比較できる公開 benchmark board が整備されること

## 参考文献

1. Musall S, Kaufman MT, Juavinett AL, Gluf S, Churchland AK. Single-trial neural dynamics are dominated by richly varied movements. *Nature Neuroscience*. 2019;22:1677-1686.
   - https://doi.org/10.1038/s41593-019-0502-4
2. Benisty H, Barson D, Moberly AH, et al. Rapid fluctuations in functional connectivity of cortical networks encode spontaneous behavior. *Nature Neuroscience*. 2024;27:148-158.
   - https://doi.org/10.1038/s41593-023-01498-y
3. Egger A, Bayon C, d'Almeida J, et al. Chrono-EEG dynamics influencing hand gesture decoding: a 10-hour study. *Scientific Reports*. 2024;14:21209.
   - https://doi.org/10.1038/s41598-024-70609-x
4. Gallego JA, Perich MG, Chowdhury RH, Solla SA, Miller LE. Long-term stability of cortical population dynamics underlying consistent behavior. *Nature Neuroscience*. 2020;23:260-270.
   - https://doi.org/10.1038/s41593-019-0555-4
5. Finn ES, Shen X, Scheinost D, et al. Functional connectome fingerprinting: identifying individuals using patterns of brain connectivity. *Nature Neuroscience*. 2015;18:1664-1671.
   - https://doi.org/10.1038/nn.4135
6. Roth ZN, Merriam EP. Representations in human primary visual cortex drift over time. *Nature Communications*. 2023;14:4422.
   - https://doi.org/10.1038/s41467-023-40144-w
7. Noda T, Kienle E, Eppler J-B, et al. Homeostasis of a representational map in the neocortex. *Nature Neuroscience*. 2025;28:1533-1545.
   - https://doi.org/10.1038/s41593-025-01982-7
8. Karpowicz BM, O'Shea DJ, Wyche S, et al. Stabilizing brain-computer interfaces through alignment of latent dynamics. *Nature Communications*. 2025;16:3500.
   - https://doi.org/10.1038/s41467-025-59652-y
9. Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. *Nature Biomedical Engineering*. 2025.
   - https://doi.org/10.1038/s41551-025-01536-z
10. Littlejohn KT, Cho CJ, Liu JR, et al. A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. *Nature Neuroscience*. 2025;28:1318-1328.
   - https://doi.org/10.1038/s41593-025-01905-6
11. Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. *Nature*. 2025;644:145-152.
   - https://doi.org/10.1038/s41586-025-09127-3
