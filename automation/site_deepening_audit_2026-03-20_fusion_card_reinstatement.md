# Site Deepening Audit (2026-03-20, Fusion Card Reinstatement)

## 対象

- 主対象: `verification.md`
- 副対象: `wbe_101.md`
- 副対象: `wiki/measurement-stack-and-claim-ceiling.md`
- 副対象: `wiki/baselines-prereg-and-model-cards.md`
- 副対象: `wiki/standards-repositories-validators-and-benchmarks.md`

## 今回の選定理由

- 2026-03-20 時点の公開サイトは、`Observability Budget`、`Pretraining Card`、`tractography route card`、`effective-connectivity route card` など、各種 route card をかなり整理できておりました。
- しかし同時に、`verification.md` の page highlight ではすでに `Fusion Card` を必須 artifact として宣言しているのに、本文には独立の `Fusion Card` 節が存在していませんでした。
- この不整合は技術・自然科学の観点で重要です。なぜなら、読者は
  - `simultaneous`
  - `multimodal`
  - `atlas-informed`
  - `same-session`
  という語を見た時点で、融合そのものの妥当性が既に監査済みだと誤読しやすいからです。
- したがって、今回は `Fusion Card` を Verification の本文へ再実装し、front door と補助 wiki まで一貫させるのが、現状もっとも深掘りして更新すべき点だと判断しました。

## 根拠付き批判

### 1. 旧 site は「multimodal」という語の中に別々の技術課題を折り畳みすぎていました

- 問題:
  - 旧 `verification.md` は `Fusion Card` を page highlight で要求していましたが、本文には
    - acquisition relation
    - synchronization / lag audit
    - co-registration scope
    - fusion model
    - unimodal baseline
    - external calibration
    を固定する実体の table がありませんでした。
- 根拠:
  - Kothe et al. (2025) は Lab Streaming Layer を synchronized multimodal recording の基盤として整理しましたが、LSL 自体は device-side delay truth や biological equivalence を保証しません。
  - Wei et al. (2020) は EEG-fMRI fusion を Bayesian fusion / multimodal DCM として扱い、融合が直接観測ではなく model-conditioned inference であることを明示しました。
- 批判:
  - したがって、`streams are synchronized` と `latent biological state is jointly identified` は別問題です。
  - 旧 site はこの区別を方針文では知っていたのに、運用テーブルへ落とし込めていませんでした。

### 2. 旧 site は「同時取得できた」ことを「融合妥当性が高い」ことと十分に分離していませんでした

- 問題:
  - `wbe_101.md` と `wiki/measurement-stack-and-claim-ceiling.md` は human proxy composition をかなり強く批判していましたが、same-session multimodal acquisition 自体の ceiling を十分に front door で固定していませんでした。
- 根拠:
  - Vafaii et al. (2024) は spontaneous brain activity の multimodal measures において、common pattern だけでなく divergent pattern も存在すると示しました。
  - Chen et al. (2025) は simultaneous EEG-PET-MRI で wakefulness / NREM sleep にまたがる temporally coupled かつ spatially structured な差を示し、modalities が one-to-one に潰れるわけではないことを示しました。
- 批判:
  - これは multimodal acquisition が無意味という意味ではありません。
  - しかし、`same-session` や `simultaneous` を見ただけで state-complete direction を強く読むのは不当です。
  - site 側では、これを `Fusion Card` によって運用上明示する必要がありました。

### 3. 旧 site は standards / validators / synchronization と fusion validity をまだ十分に分離していませんでした

- 問題:
  - `wiki/standards-repositories-validators-and-benchmarks.md` は BIDS/HED/LSL/MNE-BIDS/MOABB の役割差をよく整理していましたが、`standards + synchronization infrastructure != multimodal validity package` を十分に明文化していませんでした。
- 根拠:
  - Kothe et al. (2025) は LSL を synchronized transport / alignment infrastructure として整理しており、それ自体は fusion claim の calibration artifact ではありません。
  - Wei et al. (2020), Vafaii et al. (2024), Chen et al. (2025) は、時間合わせや同時取得の上に、さらに fusion model と external validation の問題が残ることを示します。
- 批判:
  - したがって、`BIDS + HED + LSL を使った` というだけでは `Fusion Card` の代用になりません。
  - standards page 側でも、この境界をはっきり固定する必要がありました。

## 今回実行した変更

- `verification.md`
  - `#fusion-card` 節を新設しました。
  - `Fusion Card field` table を追加し、
    - acquisition relation
    - clock / lag audit
    - geometry / registration scope
    - fusion object and model burden
    - incremental evidence over unimodal / prior-only baselines
    - external calibration and abstention
    を必須 disclosure として明文化しました。
  - `Additional audit logs` に `Fusion Card` を追加しました。
  - 参考文献として Kothe (2025), Wei (2020), Vafaii (2024), Chen (2025) を追加しました。
- `wbe_101.md`
  - human observability ladder の入口に、`same-session multimodal human evidence` でも `Fusion Card` が必要であることを示す note-box を追加しました。
  - hidden-state criticism を operational rule へ変換する箇所に、`Observability Budget` に加えて `Fusion Card` を明記しました。
  - 参考文献を追加しました。
- `wiki/measurement-stack-and-claim-ceiling.md`
  - `last_updated` を `2026-03-20` に更新しました。
  - `Cross-stack fusion adds only observables` の行を、Wei / Vafaii / Chen を使って更新しました。
  - composition rule note に `Fusion Card` への導線を追加しました。
  - 参考文献を追加しました。
- `wiki/baselines-prereg-and-model-cards.md`
  - `last_updated` を `2026-03-20` に更新しました。
  - page highlights / known points に `Fusion Card` を追加しました。
  - `2026-03-20 Addendum` を追加し、通常の model card + Observability Budget では multimodal / atlas-prior 結果には不十分であることを明記しました。
  - roles table と `When a normal model card is not enough` table に `Fusion Card` を追加しました。
  - checklist と参考文献も更新しました。
- `wiki/standards-repositories-validators-and-benchmarks.md`
  - `last_updated` を `2026-03-20` に更新しました。
  - page highlights / known points に、`BIDS/HED/LSL != Fusion Card` を追加しました。
  - `synchronization infrastructure is not a Fusion Card` addendum を追加しました。
  - Kothe DOI link を現在の表記に修正し、関連参考文献を追加しました。

## 今回の修正で読者に明示した「修正すべき点」

- `multimodal` を「複数センサーを使った」という意味と「融合妥当性まで監査した」という意味で混用しないこと。
- `same-session` を「時刻合わせされた」に限定し、`same biological state identified` と読まないこと。
- atlas prior を live measurement と混ぜた場合、`prior-conditioned interpretation` と `direct observation` を分離して書くこと。
- fusion の改善は、必ず unimodal baseline と prior-only baseline に対する増分として示すこと。
- standards / validators / synchronization を整えたことと、cross-stack calibration が済んだことを区別すること。

## 外部依存で保留

- なし
  - 今回の作業は公開本文、運用ルール、参考文献、監査導線の改稿で完結しています。

## 参考文献

1. Kothe C, Shirazi SY, Stenner T, Medine D, Boulay C, Grivich MI, Artoni F, Mullen T, Delorme A, Makeig S. The lab streaming layer for synchronized multimodal recording. *Imaging Neuroscience*. 2025.
   - https://doi.org/10.1162/IMAG.a.136
2. Wei H, Jafarian A, Zeidman P, Litvak V, Razi A, Garrido M, Friston K, Daunizeau J. Bayesian fusion and multimodal DCM for EEG and fMRI. *NeuroImage*. 2020;211:116595.
   - https://doi.org/10.1016/j.neuroimage.2020.116595
3. Vafaii H, Mandino F, Desrosiers-Grégoire G, et al. Multimodal measures of spontaneous brain activity reveal both common and divergent patterns of cortical functional organization. *Nature Communications*. 2024.
   - https://doi.org/10.1038/s41467-023-44363-z
4. Chen Z, Ye M, Moradi F, et al. Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-64414-x
