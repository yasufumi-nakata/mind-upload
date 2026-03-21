# Site Deepening Audit (2026-03-21, FAQ State-Continuity Front Door)

## 対象

- 主対象: `faq.md`
- 参照整合先: `verification.md`, `wbe_101.md`, `wiki/state-continuity-bridge.md`, `wiki/human-proxy-composition.md`

## 今回の選定理由

- 2026-03-21 時点で、サイト本体には `State-Continuity Bridge Card` と対応 wiki がすでに導入されておりました。
- しかし、入口ページである `faq.md` は依然として front-door guard を `8 つ` としており、`same-subject / same-brain ≠ same-state` が独立した停止線として前面化していませんでした。
- そのため、FAQ だけ読んだ読者が
  - `same subject`
  - `same brain`
  - `same session`
  - `correlative workflow`
  を一つの「ほぼ同じ状態を捕まえた」という意味に圧縮して読む余地が残っていました。

## 根拠付き批判

### 1. FAQ の guardrail 列挙が、現行コアページの科学的停止線より 1 段弱い状態でした

- 問題:
  - `index.md`, `wbe_101.md`, `verification.md`, `wiki/state-continuity-bridge.md` では、既に sequential bridge の問題が独立の監査対象になっていました。
  - 一方で `faq.md` は、front door の guardrail として
    - connectome insufficiency
    - proxy composition ceiling
    - shortcut / specificity
    - connectivity ceiling
    - hemodynamic vascular-state ceiling
    - effective-connectivity model ceiling
    - thermodynamic route ceiling
    - latency / boundary ceiling
    までは出していましたが、bridge ceiling を同じ強度では提示していませんでした。
- 批判:
  - FAQ は「短いから仕方ない」では済みません。入口で止めない誤読は、その後のページで補正されにくいからです。
  - とくに `same-subject` は、読者に安心感を与える言葉であり、ここを front door で独立停止線にしないのは危険でした。

### 2. preservation / fixation は bridge の外部条件ではなく bridge 内部の変換です

- 根拠:
  - Lu et al. (2023) は、conventional fixation では extracellular-space retention が崩れることを示し、ECS-preserving route を提案しました。
  - Idziak et al. (2023) は、live-versus-fixed 比較で subtle spine-morphology changes と substantial membrane damage を示しました。
- 批判:
  - したがって、live-to-fix bridge を「同じ対象を後で詳しく見た」と書くのは粗すぎます。
  - FAQ がこの停止線を持たないままだと、destructive local ultrastructure を living-human ladder の延長として誤読しやすい状態が残ります。

### 3. correlative same-brain workflow は高度でも sequential local bridge のままです

- 根拠:
  - Bosch et al. (2022) は in vivo physiology から synchrotron microtomography と volume EM への landmark-based multistage workflow を示しました。
  - MICrONS Consortium et al. (2025) は、same-brain structure-function bridge を大きく前進させましたが、なお in vivo の後に fixation / ex vivo reconstruction を置く sequential local pipeline です。
- 批判:
  - したがって、`same-brain` という語を FAQ で独立停止線にしないと、読者は workflow sophistication を same-state evidence と取り違えます。

### 4. live stack でも cross-day / cross-regime なら state continuity は崩れうります

- 根拠:
  - Benisty et al. (2024) は spontaneous behavior が activity magnitude だけでなく functional-connectivity structure も変えることを示しました。
  - Egger et al. (2024) は 10 時間スケールの EEG dynamics が decoding を動かし、adaptive decoders を要することを示しました。
- 批判:
  - よって、fixation が無い場合でも、`same subject` や `cross-day stable` を one-state sample と読んではいけません。
  - FAQ が `high score` や `cross-day stability` の話だけで止まり、bridge validity を別立てしていなかった点は改善対象でした。

## 今回実行した変更

- `faq.md`
  - front matter の `page_highlights` を `eight technical guardrails` から `nine technical guardrails` に更新しました。
  - `known_points` に `same-subject / same-brain wording does not by itself make a sequential workflow one state sample` を追加しました。
  - `wiki_links` に `Wiki: State-Continuity Bridge` を追加しました。
  - 本文の front-door note を `Nine technical guards now fixed at the front door` に更新し、`Verification: State-Continuity Bridge Card` と `Wiki: State-Continuity Bridge` への導線を追加しました。
  - 早見表に `Q2e` を追加しました。
  - 新規節 `Q2e. If a paper says same-subject or same-brain, does that mean one state was captured?` を追加しました。
    - specimen identity と state continuity を分離
    - preservation / fixation
    - correlative same-brain workflow
    - cross-day / cross-regime drift
    - bridge validation rung
    を FAQ 入口レベルで止める構成にしました。

## 今回修正しなかったもの

- `summary_booklet.md`
  - 自動生成ファイルであり、今回の改善主対象は FAQ の front-door scientific guardrail でした。
  - FAQ 改訂を要約冊子へどう反映するかは、冊子の採録対象ページをどこまで広げるかの設計判断が先に必要です。

## 外部依存タスク

- bridge benchmark の公開整備
  - 担当者: correlative imaging / connectomics / benchmark 設計の各担当者
  - 前提条件: live reacquisition, fixation follow-up, landmark recovery, perturbation-linked validation を同一 schema で比較できる公開データ
  - 完了条件: bridge validation rung を modality 横断で比較できる公開 benchmark board が用意されること

## 参考文献

1. Lu X, Han X, Meirovitch Y, et al. Preserving extracellular space for high-quality optical and ultrastructural studies of whole mammalian brains. *Cell Reports Methods*. 2023.
   - https://doi.org/10.1016/j.crmeth.2023.100520
2. Idziak A, Inavalli VVGK, Bancelin S, Arizono M, Nagerl UV. The Impact of Chemical Fixation on the Microanatomy of Mouse Organotypic Hippocampal Slices. *eNeuro*. 2023.
   - https://doi.org/10.1523/ENEURO.0104-23.2023
3. Bosch C, Pacureanu A, Patino J, et al. Functional and multiscale 3D structural investigation of brain tissue through correlative in vivo physiology, synchrotron microtomography and volume electron microscopy. *Nature Communications*. 2022.
   - https://doi.org/10.1038/s41467-022-30199-6
4. MICrONS Consortium, Bae JA, Lee W-CA, et al. Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-08790-w
5. Benisty H, Barson D, Moberly AH, et al. Rapid fluctuations in functional connectivity of cortical networks encode spontaneous behavior. *Nature Neuroscience*. 2024.
   - https://doi.org/10.1038/s41593-023-01498-y
6. Egger A, Bayon C, d'Almeida J, et al. Chrono-EEG dynamics influencing hand gesture decoding: a 10-hour study. *Scientific Reports*. 2024.
   - https://doi.org/10.1038/s41598-024-70609-x
