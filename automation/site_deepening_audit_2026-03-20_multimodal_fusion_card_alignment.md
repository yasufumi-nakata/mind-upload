# Site Deepening Audit (2026-03-20, Multimodal Fusion-Card Alignment)

## 対象

- 主対象: `wiki/multimodal-integration-basics.md`
- 参照整合先: `verification.md`, `wbe_101.md`, `wiki/measurement-stack-and-claim-ceiling.md`, `wiki/baselines-prereg-and-model-cards.md`

## 今回の選定理由

- 2026-03-20 時点で公開サイトは、`verification.md` と `wbe_101.md` で `Fusion Card` をすでに必須 artifact として扱っていました。
- その一方で、`wiki/multimodal-integration-basics.md` は依然として `synchronization / geometry / external validation` を主軸に読ませており、`same-session multimodal acquisition != validated fusion` という site-wide rule が本文で十分に表現されていませんでした。
- この不整合は技術・自然科学の観点で優先度が高いです。理由は、読者が `simultaneous` `multimodal` `atlas-informed` という語を見た時点で、融合そのものの妥当性まで通過済みと誤読しやすいからです。

## 根拠付き批判

### 1. 旧ページは同期と融合妥当性をまだ十分に分離していませんでした

- 問題:
  - 旧 `wiki/multimodal-integration-basics.md` は six audit gates により、shared clock, geometry, noise, hemodynamic transfer, external validation, state coverage を整理していました。
  - しかし `fusion model`, `unimodal / prior-only baseline`, `external calibration`, `abstention boundary` を固定する独立の gate がありませんでした。
- 根拠:
  - Kothe et al. (2025) は LSL を synchronized multimodal recording の infrastructure として整理しましたが、device-side delay truth や biological equivalence の証明ではありません。
  - Wei et al. (2020) は EEG-fMRI fusion を Bayesian fusion / multimodal DCM として扱い、融合が依然 model-conditioned inference であることを明示しました。
- 批判:
  - したがって `streams are synchronized` と `latent biological state is jointly identified` は別問題です。
  - 旧ページは前者をかなり丁寧に整理していた一方、後者を operational artifact として固定できていませんでした。

### 2. 旧ページは `same-session` を `same biological state identified` に近く読ませる余地を残していました

- 問題:
  - route table は EEG+fMRI, EEG+MEG, EEG+invasive をよく整理していましたが、`same-session` や `simultaneous` の ceiling が依然として弱めでした。
- 根拠:
  - Vafaii et al. (2024) は simultaneous Ca2+ imaging + fMRI で、multimodal measures が common pattern だけでなく divergent pattern も保持することを示しました。
  - Chen et al. (2025) は simultaneous EEG-PET-MRI で、wakefulness / NREM sleep にまたがる temporally coupled global dynamics と network-specific structure を同時に示しましたが、それでも one-to-one fused ground truth を主張しているわけではありません。
- 批判:
  - これは multimodal acquisition が弱いという意味ではありません。
  - しかし `same-session` や `tri-modal` という語を見ただけで、state-complete direction を強く読むのは不当です。

### 3. tri-modal frontier が欠けることで、現行の multimodal page は最新の model burden を十分に示していませんでした

- 問題:
  - 旧ページの主要 route は EEG+MRI, EEG+MEG, EEG+fMRI, EEG+invasive, OPM-MEG に集中していました。
  - そのため、2025 時点の simultaneous EEG-PET-MRI のような `hemodynamic + metabolic + electrophysiological` fusion route がまだ public rule に入っていませんでした。
- 根拠:
  - Chen et al. (2025) は tri-modal acquisition により arousal-state transition をまたぐ coupled dynamics と distinct network structure を示しました。
- 批判:
  - したがって current multimodal page でも `fusion object` と `model burden` をより強く front door で固定しなければ、最新 route を正しく読む入口として不足していました。

## 今回実行した変更

- `wiki/multimodal-integration-basics.md`
  - `last_updated` を `2026-03-20` に更新しました。
  - front matter の `page_highlights` / `known_points` / `wiki_links` を、site-wide `Fusion Card` rule に同期しました。
  - 冒頭に `Even same-session multimodal acquisition still needs a Fusion Card` note を追加しました。
  - `Six audit gates` を `Seven audit gates` に改め、`Fusion Card gate` を新設しました。
  - `Minimum fusion package on this site` note を追加し、必要 disclosure を `verification.md#fusion-card` と整合させました。
  - route table に `Simultaneous EEG + PET + MRI` を追加しました。
  - 本文に `EEG + PET + MRI adds arousal-state fusion, not fused ground truth` 節を追加しました。
  - reading rules に `same-session / atlas-informed` と `EEG + PET + MRI` の safe reading を追加しました。
  - 参考文献に Kothe (2025), Wei (2020), Vafaii (2024), Chen (2025) を追加しました。

## 今回の修正で読者に明示した「修正すべき点」

- `simultaneous` を `fusion validity passed` と同義に読まないこと。
- `atlas-informed` を `directly observed in one shared biological state space` と読まないこと。
- multimodal の改善は、必ず unimodal / prior-only baseline に対する増分として示すこと。
- synchronized transport, co-registration, fusion model, external calibration を別々の監査項目として書くこと。
- tri-modal route を見ても、`coupled dynamics observed` と `hidden-state completeness approached` を混同しないこと。

## 外部依存で保留

- なし
  - 今回の作業は公開本文の更新と監査メモで完結しています。

## 参考文献

1. Kothe C, Shirazi SY, Stenner T, Medine D, Boulay C, Grivich MI, Artoni F, Mullen T, Delorme A, Makeig S. The lab streaming layer for synchronized multimodal recording. *Imaging Neuroscience*. 2025;3:IMAG.a.136.
   - https://doi.org/10.1162/IMAG.a.136
2. Wei H, Jafarian A, Zeidman P, Litvak V, Razi A, Garrido M, Friston K, Daunizeau J. Bayesian fusion and multimodal DCM for EEG and fMRI. *NeuroImage*. 2020;211:116595.
   - https://doi.org/10.1016/j.neuroimage.2020.116595
3. Vafaii H, Mandino F, Desrosiers-Grégoire G, O'Connor D, Markicevic M, Shen X, Ge X, Herman P, Hyder F, Papademetris X, Chakravarty M, Crair MC, Constable RT, Lake EMR, Pessoa L. Multimodal measures of spontaneous brain activity reveal both common and divergent patterns of cortical functional organization. *Nature Communications*. 2024;15:229.
   - https://doi.org/10.1038/s41467-023-44363-z
4. Chen JE, Lewis LD, Coursey SE, Catana C, Polimeni JR, Fan J, Droppa KS, Patel R, Wey H-Y, Chang C, Manoach DS, Price JC, Sander CY, Rosen BR. Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep. *Nature Communications*. 2025;16:8887.
   - https://doi.org/10.1038/s41467-025-64414-x
