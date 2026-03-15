# Site Deepening Audit (2026-03-16, Verification Commons / Multimodal Fusion Card)

## 対象

- 主対象: `verification.md`
- 関連対象: `wiki/standards-repositories-validators-and-benchmarks.md`
- 関連対象: `wiki/baselines-prereg-and-model-cards.md`
- 関連整合: `wiki/multimodal-integration-basics.md`

## 今回の選定理由

- 2026-03-16 時点で、`wiki/multimodal-integration-basics.md` と `eeg_101.md` は `multimodal` を 4 種類の取得関係へかなり明確に分解できていました。
- その一方で、サイト全体の中心設計図である `verification.md` は、`Observability Budget` と `latent-state error budget` までは提出物要件として固定していたものの、`multimodal result` をどう監査するかを site-wide のカード仕様としてまだ明文化できていませんでした。
- これは技術・自然科学の観点で弱点です。なぜなら、BIDS / HED / LSL / Motion-BIDS は入力と同期の床を与えても、`どうモダリティを結び付けたか`、`どの融合モデルを使ったか`、`single-modality baseline をどこまで超えたか`、`どこで外部妥当化したか` までは自動で与えないからです。

## 主要な批判点

### 1. 既存 Verification は `何を直接見たか` を固定していましたが、`どう結び付けたか` をまだ固定していませんでした

- 問題:
  - `Observability Budget` は measurement stack と direct observable をかなりうまく固定していました。
  - しかし、EEG+fMRI、EEG+MRI、EEG+SEEG、atlas prior を伴う推定を、結果カードの粒度ではまだ切り分けられていませんでした。
  - そのため、読者が `multimodal` を 1 種類の前進と読み、shared clock、geometry prior、coverage-limited validation、atlas prior を同じ強さの証拠として扱う余地が残っていました。
- 根拠:
  - Pernet et al. (2019) は EEG-BIDS が modality-specific metadata の器を与えることを示しました。
  - Jeung et al. (2024) は Motion-BIDS が motion 系 metadata を別 schema で保持する必要を示しました。
  - Kothe et al. (2025) は LSL が synchronized multimodal recording に有効でも、device-side delay / jitter の ground truth を自動で確定しないことを示しました。
- 修正:
  - `verification.md` に `2026-03 追補：multimodal 結果には Fusion Card を添付する` 節を新設しました。
  - `Fusion Card` を `Observability Budget` と別カードとして定義し、acquisition relation、clock audit、geometry / registration、fusion model、incremental evidence、external validator、coverage boundary / raw retention を必須項目化しました。

### 2. 旧 core page は、融合後の map を raw truth へ近く読ませる危険を残していました

- 問題:
  - wiki 側では `fusion output は推定` と明確化済みでしたが、`verification.md` の提出物仕様には同じ強さの境界が入っていませんでした。
  - この状態では、結果カードだけ読む利用者が `multimodal だから state coverage が増えた` と誤読しやすくなります。
- 根拠:
  - Wei et al. (2020) は Bayesian fusion / multimodal DCM が shared latent model を明示して初めて EEG と fMRI を結び付けることを示しました。
  - Jorge et al. (2015) は simultaneous EEG-fMRI で artifact prevention と safety assessment が成立条件であることを示しました。
  - Aydin et al. (2014) は EEG+MEG の改善が calibrated realistic volume conductor model に依存することを示しました。
- 修正:
  - `verification.md` の `Fusion Card` に `fusion model and uncertainty` と `geometry and registration` を追加しました。
  - `wiki/standards-repositories-validators-and-benchmarks.md` にも、BIDS / HED / LSL だけでは fusion validity は足りず、器の外側に `Fusion Card` が必要だと追記しました。

### 3. 旧 site-wide schema は、multimodal gain を baseline 差分として固定していませんでした

- 問題:
  - これまでの `Fusion Card` 概念は取得関係と較正をかなり整理できていましたが、`本当に modality を足した価値があったのか` を明示する欄がありませんでした。
  - そのため、強い prior や geometry を足しただけの改善と、同時計測による追加証拠が区別しにくい状態でした。
- 根拠:
  - Wei et al. (2020) は information gain を、単独 modality との比較の中で解釈しています。
  - これは本文そのものの要求というより、本サイトがそこから引く運用上の推論です。multimodal gain を書くなら、single-modality baseline または missing-modality ablation を残さなければ比較不能という判断でございます。
- 修正:
  - `verification.md` の `Fusion Card` に `incremental evidence` を追加しました。
  - `wiki/multimodal-integration-basics.md` の card 仕様も同じ欄へ更新し、missing-modality ablation が無い場合は multimodal gain を書かない site rule を追記しました。

### 4. 旧 model-card 説明は `Observability Budget` までで止まり、multimodal result の追加カードを明示していませんでした

- 問題:
  - `wiki/baselines-prereg-and-model-cards.md` は L1 以上で `Observability Budget` を付ける運用を正しく説明していました。
  - しかし、multimodal / atlas prior result に対する追加カードの話が無かったため、model card の実務運用としては 1 段弱い状態でした。
- 修正:
  - `wiki/baselines-prereg-and-model-cards.md` を 2026-03-16 更新とし、multimodal / atlas prior result では `Fusion Card` を併記する運用へ更新しました。

## 今回実行した変更

- `verification.md`
  - `last_updated` を 2026-03-16 に更新
  - front matter に `Fusion Card` の要旨を追加
  - deliverables 節の `Leaderboard & Model Cards` を `Observability Budget + Fusion Card + latent-state error budget` の 3 層へ更新
  - `multimodal / atlas prior` 結果で `Fusion Card` を要求する note を追加
  - `2026-03 追補：multimodal 結果には Fusion Card を添付する` 節を新設
  - 参考文献へ Motion-BIDS / LSL / Bayesian fusion / EEG-fMRI safety / calibrated EEG+MEG / Mikulan 2020 を追加
  - Hao et al. (2025) の文献表記を `doi:10.1111/epi.18552` に修正
- `wiki/standards-repositories-validators-and-benchmarks.md`
  - `last_updated` を 2026-03-16 に更新
  - BIDS / HED / Motion-BIDS / LSL の外側に `Fusion Card` が必要であることを追記
  - EEG 例の節に `multimodal でさらに必要なもの` note を追加
- `wiki/baselines-prereg-and-model-cards.md`
  - `last_updated` を 2026-03-16 に更新
  - `Observability Budget` に加えて `Fusion Card` を要求する運用へ更新
- `wiki/multimodal-integration-basics.md`
  - `Fusion Card` に `Incremental evidence` 行を追加
  - single-modality baseline / missing-modality ablation が無い場合は multimodal gain を書かない rule を追記

## 外部依存で保留

- なし
  - 今回の変更はすべてこのリポジトリ内で完結し、外部実験や追加データ収集を前提にしていません。

## 参考文献

- Pernet CR, Appelhoff S, Gorgolewski KJ, et al. EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. *Sci Data*. 2019;6:103.
  - https://doi.org/10.1038/s41597-019-0104-8
- Jeung J, Burns M, Nii L, et al. Motion-BIDS: an extension to the brain imaging data structure to organize motion data for reproducible research. *Sci Data*. 2024;11:857.
  - https://doi.org/10.1038/s41597-024-03559-8
- Kothe CA, Appelhoff S, Bullock T, et al. The lab streaming layer for synchronized multimodal recording. *Imaging Neurosci*. 2025;3:IMAG.a.136.
  - https://doi.org/10.1162/imag.a.136
- Wei H, Jafarian A, Zeidman P, et al. Bayesian fusion and multimodal DCM for EEG and fMRI. *NeuroImage*. 2020;211:116595.
  - https://doi.org/10.1016/j.neuroimage.2019.116595
- Jorge J, Grouiller F, Ipek O, et al. Simultaneous EEG-fMRI at ultra-high field: artifact prevention and safety assessment. *NeuroImage*. 2015;105:132-144.
  - https://doi.org/10.1016/j.neuroimage.2014.10.055
- Aydin U, Vorwerk J, Kupper P, et al. Combining EEG and MEG for the reconstruction of epileptic activity using a calibrated realistic volume conductor model. *PLoS One*. 2014;9(3):e93154.
  - https://doi.org/10.1371/journal.pone.0093154
- Mikulan E, Russo S, Pellon Maison M, et al. Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. *Sci Data*. 2020;7:127.
  - https://doi.org/10.1038/s41597-020-0467-x
- Unnwongse K, Achakulvisut T, Wu JY, et al. Direct validation of EEG source imaging by intracranial electric stimulation in human patients. *Brain Commun*. 2023;5(2):fcad023.
  - https://doi.org/10.1093/braincomms/fcad023
