# Site Deepening Audit (2026-03-21, State-Continuity Bridge Background)

## 対象

- 主対象: `wiki/state-continuity-bridge.md`
- 参照整合先: `verification.md`, `wbe_101.md`, `index.md`, `tech_roadmap.md`, `wiki/human-proxy-composition.md`

## 今回の選定理由

- 2026-03-21 時点で、公開コアページ側には `State-Continuity Bridge Card` がすでに導入されていました。
- しかし、そのカードを支える独立 wiki が未整備で、`same-subject` / `same-brain` / `same-state` の差が verification 本文の短い停止線に圧縮されていました。
- この状態は技術・自然科学の観点で危険です。理由は、読者が
  - specimen identity
  - time continuity
  - physiological-regime continuity
  - coordinate continuity
  を一つの `same subject` という言葉に潰して読みやすかったからです。

## 根拠付き批判

### 1. `same-subject` は specimen identity しか保証しません

- 問題:
  - 既存サイトは same-subject shortcut を止めていましたが、背景説明が独立していなかったため、`何が continuity claim で、何が merely identity claim なのか` が前面化し切っていませんでした。
- 根拠:
  - Musall et al. (2019) は task 中の cortical variance の大部分が richly varied movement によって規定されることを示しました。
  - Benisty et al. (2024) は spontaneous behavior が activity magnitude だけでなく functional-connectivity structure も急速に変えることを示しました。
  - Egger et al. (2024) は 10 時間スケールで MRCP dynamics が変化し、adaptive decoders の必要性を示しました。
- 批判:
  - したがって、同一個体・同一脳であっても、bridge が within-day / cross-day / cross-regime であれば `same state` とは読めません。
  - `same-subject` を one-state sample の同義語として扱う説明密度は不足していました。

### 2. 保存・固定は中立な保存ではなく、bridge object 自体を変えうる操作です

- 問題:
  - 既存サイトは Lu et al. (2023) を引用していましたが、`fixation is itself an intervention on geometry and observability` という点を背景ページで独立に展開していませんでした。
- 根拠:
  - Lu et al. (2023) は conventional fixation による extracellular-space loss を前提に、whole-brain ECS-preserving perfusion を提案しました。
  - Idziak et al. (2023) は live-versus-fixed 比較で、subtle spine-morphology changes と substantial membrane damage を示しました。
- 批判:
  - したがって、live-to-fix bridge を `state was stored and later read out` と書くのは粗すぎます。
  - 保存法は bridge の外側の準備作業ではなく、bridge の内部で audit されるべき変換です。

### 3. correlative same-brain workflows は multistage local pipeline であり、same-state capture ではありません

- 問題:
  - 既存コアページは same-brain function + EM を sequential pipeline と書いていましたが、Bosch / Shapson-Coe / MICrONS をまとめて読む背景ページがありませんでした。
- 根拠:
  - Bosch et al. (2022) は in vivo physiology から synchrotron microtomography と serial block-face EM への multistage landmark-based workflow を示しました。
  - Shapson-Coe et al. (2024) は remarkable な human cortical fragment reconstruction を示しましたが、あくまで rapidly preserved local surgical fragment です。
  - MICrONS Consortium et al. (2025) は same-brain function plus EM を大きく前進させましたが、依然として in vivo の後に fixation / sectioning / ex vivo reconstruction を置く sequential local pipeline です。
- 批判:
  - したがって、`same-brain` という言葉を `same-state` や `same-time whole-state capture` へ昇格させるのは不適切です。
  - 既存サイトにはこの local scaffold / sequential bridge / same-state overread の切り分けを一箇所で読む場所が必要でした。

### 4. bridge validation は checkbox ではなく rung として読むべきです

- 問題:
  - 旧構成では `bridge validation rung` という verification 上の欄はありましたが、なぜ rung なのかが説明不足でした。
- 根拠:
  - Bosch et al. (2022) のような landmark-based correlative workflow と MICrONS Consortium et al. (2025) の same-brain local structure-function bridge は、どちらも高品質ですが validation object が同じではありません。
  - Lu et al. (2023) と Idziak et al. (2023) は preservation step 自体の品質評価が bridge validity の前提であることを示します。
- 批判:
  - したがって、`correlative workflow was used` を one-bit の validated / not validated に落とすのは不適切です。
  - validation rung の意味を background page で説明しない限り、読者は workflow sophistication を same-state validity と取り違えます。

## 今回実行した変更

- `wiki/state-continuity-bridge.md`
  - 新規追加しました。
  - `specimen continuity`, `time continuity`, `regime continuity`, `coordinate continuity` を分ける表を追加しました。
  - preservation / fixation, correlative same-brain workflow, biological turnover, cross-day reacquisition を別節で整理しました。
  - `bridge validation is a rung, not a checkbox` の table を追加しました。
  - `State-Continuity Bridge Card` が `Destructive-Structure Route Card`, `Human Proxy Composition Card`, `Temporal Validity Card` とどう stack するかを明文化しました。
- `verification.md`
  - `wiki_links` に `Wiki: State-Continuity Bridge` を追加しました。
  - `State-Continuity Bridge Card` 直後に、長い背景説明への導線 note を追加しました。
- `wbe_101.md`
  - entry-level の same-subject note に新 wiki への導線を追加しました。
- `index.md`
  - front-door note に `Wiki: State-Continuity Bridge` を追加し、verification 単独説明から脱却させました。
- `tech_roadmap.md`
  - `wiki_links` に `Wiki: State-Continuity Bridge` を追加しました。
  - human-observability 周辺の note に新 wiki を接続しました。
- `wiki/human-proxy-composition.md`
  - `wiki_links` に新 page を追加しました。
  - sequential-bridge section から新 page へ飛べるようにしました。

## 外部依存で保留

- same-state bridge benchmark の整備
  - 担当者: correlative imaging 研究者 / connectomics 研究者 / benchmark 設計者 / maintainer
  - 前提条件: live recording, repeated live reacquisition, fixation / ex vivo follow-up, landmark recovery, perturbation-linked correspondence を同一 schema で比較できる公開データ
  - 完了条件: bridge validation rung を modality 横断で比較できる公開 benchmark board が整備されること

## 参考文献

1. Lu X, Han X, Meirovitch Y, et al. Preserving extracellular space for high-quality optical and ultrastructural studies of whole mammalian brains. *Cell Reports Methods*. 2023.
   - https://doi.org/10.1016/j.crmeth.2023.100520
2. Idziak A, Inavalli VVGK, Bancelin S, Arizono M, Nagerl UV. The Impact of Chemical Fixation on the Microanatomy of Mouse Organotypic Hippocampal Slices. *eNeuro*. 2023.
   - https://doi.org/10.1523/ENEURO.0104-23.2023
3. Bosch C, Pacureanu A, Patino J, et al. Functional and multiscale 3D structural investigation of brain tissue through correlative in vivo physiology, synchrotron microtomography and volume electron microscopy. *Nature Communications*. 2022.
   - https://doi.org/10.1038/s41467-022-30199-6
4. Shapson-Coe A, Januszewski M, Berger DR, et al. A petavoxel fragment of human cerebral cortex reconstructed at nanoscale resolution. *Science*. 2024.
   - https://doi.org/10.1126/science.adk4858
5. MICrONS Consortium, Bae JA, Lee W-CA, et al. Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-08790-w
6. Attardo A, Fitzgerald JE, Schnitzer MJ. Impermanence of dendritic spines in live adult CA1 hippocampus. *Nature*. 2015.
   - https://doi.org/10.1038/nature14467
7. Musall S, Kaufman MT, Juavinett AL, Gluf S, Churchland AK. Single-trial neural dynamics are dominated by richly varied movements. *Nature Neuroscience*. 2019.
   - https://doi.org/10.1038/s41593-019-0502-4
8. Benisty H, Barson D, Moberly AH, et al. Rapid fluctuations in functional connectivity of cortical networks encode spontaneous behavior. *Nature Neuroscience*. 2024.
   - https://doi.org/10.1038/s41593-023-01498-y
9. Egger A, Bayon C, d'Almeida J, et al. Chrono-EEG dynamics influencing hand gesture decoding: a 10-hour study. *Scientific Reports*. 2024.
   - https://doi.org/10.1038/s41598-024-70609-x
