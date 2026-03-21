# Site Deepening Audit (2026-03-22, Tech Roadmap Longitudinal Validity)

## 対象

- 主対象: `tech_roadmap.md`
- 参照整合先: `wiki/state-trait-and-drift.md`, `verification.md`, `wiki/state-continuity-bridge.md`

## 今回の選定理由

- `tech_roadmap.md` はサイトの主要な公開導線ですが、`M7 Longitudinal` と `V4 Long-term` だけが他の 2026-03 更新に比べて相対的に薄い状態でした。
- 既存サイト全体ではすでに
  - `Temporal Validity Card`
  - `State-Continuity Bridge Card`
  - `maintenance-state error budget`
  - `state / trait / drift`
  の区別が導入されていました。
- しかし Roadmap 側では、なお `same person across time` を一つの縦断的成功として読みやすく、入口ページとしての停止線が不十分でした。

## 根拠付き批判

### 1. 旧 `M7` は same-day fluctuation と longitudinal stability を分け切れていませんでした

- 問題:
  - 旧 `M7` は「同一個体でも変動する。何がその人らしさか」という抽象的記述に留まり、
    - within-day state fluctuation
    - cross-day trait-like backbone
    - biological drift
    - interface / decoder drift
    - recalibration burden
    を分けていませんでした。
- 根拠:
  - Musall et al. (2019) は trial-to-trial cortical dynamics が richly varied movements に強く支配されることを示しました。
  - Benisty et al. (2024) は spontaneous behavior が functional-connectivity structure まで急速に変えることを示しました。
  - Egger et al. (2024) は 10-hour EEG dynamics が decoding を実質的に動かし、adaptive decoder を要することを示しました。
- 批判:
  - したがって `same person, different day` を一括して trait / drift の問題にするのは粗すぎます。
  - state annotation が無いまま cross-day score を読むと、state shift を trait instability や system failure と誤読できます。

### 2. trait は単一 unit の不変性ではなく backbone object の安定性として読むべきでした

- 問題:
  - 旧 `M7` は `personal characteristics` という表現に留まり、何を backbone object とみなすかが見えませんでした。
- 根拠:
  - Gallego et al. (2020) は unit turnover があっても aligned latent dynamics が長期に安定しうることを示しました。
  - Noda et al. (2025) は selective neuron loss 後にも population-level representational map が回復しうることを示しました。
- 批判:
  - よって longitudinal claim を読むときは、`何が stable object なのか` を named backbone として書かなければなりません。
  - これが無いと、unit drift と population backbone stability が同じ箱に潰れます。

### 3. adaptive rescue と fixed-decoder durability は同じ成功ではありませんでした

- 問題:
  - 旧 `M7` / `V4` は drift を long-term issue として挙げていましたが、`fixed decoder が持った` のか `rescue し続けた` のかを分けていませんでした。
- 根拠:
  - Karpowicz et al. (2025) は latent-dynamics alignment による BCI stabilization を示しました。
  - Wilson et al. (2025) は hidden Markov model を用いた unsupervised recalibration により long-term cursor iBCI を維持しました。
  - Wairagkar et al. (2025) は強い communication route を示す一方で、earlier-day decoder の degradation も定量しました。
- 批判:
  - したがって `system stayed usable` を `original decoder stayed valid` と読むのは誤りです。
  - longitudinal verification では
    - fixed decoder interval
    - recalibration frequency
    - rescue mode
    - failure / fallback
    を独立項目として残す必要があります。

### 4. 旧 `V4` は verification artifact の束を要求していませんでした

- 問題:
  - 旧 `V4` は「どこまで変化を許すか」という抽象課題に留まり、現在の site rule が要求する artifact bundle を前景化していませんでした。
- 批判:
  - 現在の site 水準では、long-term claim は少なくとも
    - `Temporal Validity Card`
    - cross-regime / cross-day bridge なら `State-Continuity Bridge Card`
    - persistence / forgetting / recovery claim なら `maintenance-state error budget`
    の束で読まれるべきです。
  - Roadmap がここを薄く書いたままだと、Verification 本文の厳しさが入口で失われます。

## 今回実行した変更

- `tech_roadmap.md`
  - `last_updated` を `2026-03-22` に更新しました。
  - front matter の `page_highlights` / `known_points` / `unknown_points` に longitudinal validity の停止線を追加しました。
  - `M7` を全面改稿し、
    - state annotation
    - trait-like backbone
    - biological drift
    - interface / decoder drift
    - fixed decoder interval / recalibration burden
    の 5 項目で読む表を追加しました。
  - `M7` に decision rule を追加し、必要な開示が欠ける場合の claim ceiling を明示しました。
  - `V4` を改稿し、long-term verification を
    - temporal validity
    - bridge validity
    - maintenance-route disclosure
    の束として再定義しました。
  - references に longitudinal validity 用の primary sources を追記しました。

## 外部依存で保留

- cross-modal longitudinal benchmark の整備
  - 担当者: longitudinal EEG / invasive BCI / multimodal benchmark 設計者
  - 前提条件: same subject で state annotation, fixed decoder hold, recalibration log, cross-day reacquisition, maintenance-route proxy を同一 schema で比較できる公開データ
  - 完了条件: `state fluctuation / backbone / biological drift / interface drift / recalibration burden` を modality 横断で比較できる benchmark board が公開されること

## 参考文献

1. Musall S, Kaufman MT, Juavinett AL, Gluf S, Churchland AK. Single-trial neural dynamics are dominated by richly varied movements. *Nature Neuroscience*. 2019.
   - https://doi.org/10.1038/s41593-019-0502-4
2. Benisty H, Barson D, Moberly AH, et al. Rapid fluctuations in functional connectivity of cortical networks encode spontaneous behavior. *Nature Neuroscience*. 2024.
   - https://doi.org/10.1038/s41593-023-01498-y
3. Egger A, Bayon C, d'Almeida J, et al. Chrono-EEG dynamics influencing hand gesture decoding: a 10-hour study. *Scientific Reports*. 2024.
   - https://doi.org/10.1038/s41598-024-70609-x
4. Gallego JA, Perich MG, Chowdhury RH, Solla SA, Miller LE. Long-term stability of cortical population dynamics underlying consistent behavior. *Nature Neuroscience*. 2020.
   - https://doi.org/10.1038/s41593-019-0555-4
5. Noda T, Kienle E, Eppler J-B, et al. Homeostasis of a representational map in the neocortex. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-01982-7
6. Karpowicz BM, Ali YH, Wimalasena LN, et al. Stabilizing brain-computer interfaces through alignment of latent dynamics. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-59652-y
7. Wilson GH, Stein EA, Kamdar F, et al. Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. *Nature Biomedical Engineering*. 2025.
   - https://doi.org/10.1038/s41551-025-01536-z
8. Wairagkar M, Card NS, Singer-Clark T, et al. An instantaneous voice-synthesis neuroprosthesis. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-09127-3
