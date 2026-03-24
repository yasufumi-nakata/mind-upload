# Site Deepening Audit (2026-03-25, literature hub state-continuity bridge)

## 対象

- 主対象: `mind_uploading_papers.md`
- 副対象: `research_harvest_50.md`
- 参照整合先: `verification.md`, `wbe_101.md`, `tech_roadmap.md`, `wiki/state-continuity-bridge.md`

## 今回の選定理由

- コアページ側では、2026-03 時点で `State-Continuity Bridge Card` と対応 wiki がすでに導入されております。
- しかし、技術・自然科学読者が最初に流入しやすい文献ハブ `mind_uploading_papers.md` と `research_harvest_50.md` では、この停止線が優先読書ルートとして独立していませんでした。
- その結果、
  - `same-subject`
  - `same-brain`
  - `same-day multistack`
  - `cross-day reacquisition`
  - `correlative workflow`
  を一つの「ほぼ同じ状態を捕まえた」証拠として圧縮する余地が残っていました。
- 本件は哲学や法学の論点ではなく、保存法・計測順序・生理状態・登録誤差・時間変動という、純粋に技術と自然科学の問題です。

## 根拠付き批判

### 1. コアページと文献ハブの間で、bridge の強度が揃っておりませんでした

- `verification.md`, `wbe_101.md`, `tech_roadmap.md`, `wiki/state-continuity-bridge.md` では、すでに
  - live-to-fix
  - same-brain plus EM
  - cross-day reacquisition
  - cross-regime composition
  を独立の監査対象として扱っております。
- 一方で文献ハブは、
  - destructive ultrastructure
  - living-human observability
  - maintenance-state boundary
  を強く分けていたにもかかわらず、その間をつなぐ `bridge validity` を front door で独立ルート化していませんでした。
- この不整合は、`same specimen` を `same state` と読み替える誤読をハブ側で許すため、科学的停止線として弱い状態でした。

### 2. preservation / fixation は橋渡しの外側条件ではなく、橋渡しそのものを変える内部変換です

- 根拠:
  - Lu et al. (2023) は、preservation route によって extracellular-space retention と downstream ultrastructure が変わることを示しました。
  - Idziak et al. (2023) は、live-versus-fixed 比較で subtle spine-morphology change と substantial membrane damage を示しました。
- 批判:
  - したがって、live measurement の後に fixation / EM を置く workflow を「同じ対象を後で詳しく見た」とだけ読むのは粗すぎます。
  - 文献ハブがこの停止線を独立ルートとして出さないままだと、destructive paper の解像度や scale 表現が、そのまま same-state evidence に見えてしまいます。

### 3. correlative same-brain workflow は高度であっても sequential bridge のままです

- 根拠:
  - Bosch et al. (2022) は in vivo physiology から synchrotron microtomography と serial block-face EM への multistage landmark workflow を示しました。
  - MICrONS Consortium et al. (2025) は、same-brain function plus EM を大きく前進させましたが、依然として in vivo の後に fixation / ex vivo reconstruction を置く sequential local pipeline です。
- 批判:
  - workflow sophistication は高く評価されるべきですが、それを same-state continuity と読むのは別問題です。
  - 文献ハブでこの点が独立していないと、読者は `same-brain` という語に過剰な連続性を読み込みます。

### 4. non-destructive repeated measurement でも bridge 問題は消えません

- 根拠:
  - Egger et al. (2024) は、10 時間スケールの EEG dynamics が decoding を動かし adaptive decoder を要することを示しました。
  - コアページが既に示す通り、same-subject であっても regime continuity と temporal validity は別監査です。
- 批判:
  - fixation が無い場合でも、cross-day や long-session を one-state sample と読んではいけません。
  - よって bridge problem は destructive follow-up に限定されず、live stack の longitudinal reacquisition にも及びます。

## 今回実行した変更

### `mind_uploading_papers.md`

- `last_updated` を `2026-03-25` に更新しました。
- front matter の `known_points` / `page_highlights` に、`same-subject / same-brain` を独立の bridge 問題として扱う旨を追加しました。
- 技術 addendum を `three explicit corrections` から `four explicit corrections` に改め、bridge audit を独立項目として追加しました。
- `technical-fast-lane` の優先ルートに
  - `state-continuity bridge / sequential same-brain claims`
  を追加しました。
- 同節に bridge critique の note-box を追加し、`Wiki: State-Continuity Bridge` と `Verification: State-Continuity Bridge Card` への導線を作りました。
- `technical-only shortlist` に `State-continuity bridge` を追加し、技術読者が law / philosophy を飛ばして bridge literature に直行できるようにしました。

### `research_harvest_50.md`

- `last_updated` を `2026-03-25` に更新しました。
- front matter の技術ルート記述を `U1/U7 -> bridge (U7/U8) -> U4 -> U13 -> U8 -> U3 -> U10` に更新しました。
- `page_highlights` / `known_points` に、bridge-limited evidence を明示する文を追加しました。
- 技術優先ルートの本文に `sequential bridge validity` を追加し、根拠文献列に Lu / Bosch / MICrONS / Egger を追加しました。
- 優先ルート table に `2. Sequential bridge validity` を追加しました。
- `Read same-subject / same-brain papers as bridge-limited evidence` の note-box を新設しました。
- 中盤の route selection table と route summary も bridge 導線に同期しました。

## 今回修正しなかったもの

- `verification.md` と `wiki/state-continuity-bridge.md` の card 本体は、今回の主対象ではありません。
  - これらは既に科学的停止線として十分に強く、今回の弱点は front door の文献ハブ側にありました。
- `issue.md` は前提として把握済みのため、再読していません。
- 哲学・法学・personhood 側の整理は今回の修正対象から外しました。

## 外部依存タスク

- bridge benchmark の公開整備
  - 担当者: correlative imaging / connectomics / longitudinal benchmark 設計の担当者
  - 前提条件: live-to-fix, same-brain correlative registration, repeated-live reacquisition, cross-day regime annotation を同一 schema で比較できる公開 benchmark
  - 完了条件: bridge validation rung を modality 横断で比較できる benchmark board が整備されること

## 参考文献

1. Lu X, Han X, Meirovitch Y, et al. Preserving extracellular space for high-quality optical and ultrastructural studies of whole mammalian brains. *Cell Reports Methods*. 2023.
   - https://doi.org/10.1016/j.crmeth.2023.100520
2. Idziak A, Inavalli VVGK, Bancelin S, Arizono M, Nagerl UV. The Impact of Chemical Fixation on the Microanatomy of Mouse Organotypic Hippocampal Slices. *eNeuro*. 2023.
   - https://doi.org/10.1523/ENEURO.0104-23.2023
3. Bosch C, Pacureanu A, Patino J, et al. Functional and multiscale 3D structural investigation of brain tissue through correlative in vivo physiology, synchrotron microtomography and volume electron microscopy. *Nature Communications*. 2022.
   - https://doi.org/10.1038/s41467-022-30199-6
4. MICrONS Consortium, Bae JA, Lee W-CA, et al. Functional connectomics spanning multiple areas of mouse visual cortex. *Nature*. 2025.
   - https://doi.org/10.1038/s41586-025-08790-w
5. Egger J, Bayon C, d'Almeida J, et al. Chrono-EEG dynamics influencing hand gesture decoding: a 10-hour study. *Scientific Reports*. 2024.
   - https://doi.org/10.1038/s41598-024-70609-x
