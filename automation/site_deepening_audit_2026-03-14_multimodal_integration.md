# Site Deepening Audit (2026-03-14, EEG Multimodal Integration)

## 対象

- 主対象: `wiki/multimodal-integration-basics.md`
- 参照ページ: `eeg_101.md`

## 今回の選定理由

- `eeg_101.md` 自体は 2026-03-14 時点でかなり具体化されていましたが、そこから飛ぶ `wiki/multimodal-integration-basics.md` は 2026-03-06 時点の一般説明に留まっていました。
- 現行 wiki は「どの組み合わせが何を補うか」は書いていましたが、一次文献、成立条件、失敗条件、外部妥当化が欠けていました。
- そのため、公開サイト内で `EEGだけでは足りない → では何を足せばよいか` の導線が、科学的にはやや楽観的に見える状態でした。

## 主要な批判点

### 1. 現行ページは「補完関係」の説明で止まり、統合の成立条件を監査していませんでした

- 問題:
  - `EEG + fMRI`, `EEG + MEG`, `EEG + MRI`, `EEG + ECoG` を並べていましたが、共有時計、座標合わせ、forward model、導電率仮定、artifact 管理のどれが必須かを書いていませんでした。
  - その結果、「モダリティを増やせば強くなる」という読まれ方をしやすい構造でした。
- 根拠:
  - COBIDAS-MEEG (Pernet et al., 2020) は、MEEG 研究で acquisition・analysis・reporting・sharing を明示しないと再利用性が崩れることを整理しています。
  - EEG-BIDS (Pernet et al., 2019) も、raw data と metadata を構造化して残すこと自体が再現性の前提であることを示しています。
- 修正:
  - 公開ページを `5つの監査ゲート` で再構成し、同期・幾何・ノイズ/場・外部妥当化・state coverage を先に固定しました。

### 2. EEG+fMRI の説明が、artifact と safety の厳しさを落としていました

- 問題:
  - 現行ページは `時間変化と空間分布を補い合います` という一般論に留まり、同時計測の実務上の難所を落としていました。
- 根拠:
  - Jorge et al. (2015, doi:10.1016/j.neuroimage.2014.10.055) は、3T 超で artifact と safety 問題が大きくなることを示しました。
  - Jorge et al. (2015, doi:10.1016/j.neuroimage.2015.07.020) は、7T で head motion artifact の検出と低減が中心課題になることを示しました。
  - Wirsich et al. (2021) は、1.5T〜7T にわたる simultaneous EEG-fMRI connectome の再現性を示しましたが、それは適切な setup と cleaning の上に成立しています。
- 修正:
  - `EEG + fMRI` を「時空間補完」ではなく、「高磁場ほど artifact と安全管理が増える route」として書き換えました。

### 3. EEG+MEG の改善を、物理モデル抜きに書いていました

- 問題:
  - 現行ページは `感度分布を補完します` とだけ書いていましたが、その利得が skull conductivity 校正や realistic head model に依存する点が抜けていました。
- 根拠:
  - Aydin et al. (2014) は、calibrated realistic volume conductor model を伴う EEG/MEG 統合が source reconstruction を改善しうることを示しました。
  - 逆にいえば、単なる modality stacking だけでは同等の主張はできません。
- 修正:
  - `EEG + MEG` を、物理モデルの改善込みで効く route として再定義しました。

### 4. 侵襲記録との統合を「高SNRが得られる」とだけ書き、validation route としての位置づけが弱かった

- 問題:
  - 現行ページでは ECoG/侵襲計測を高 SNR の局所計測として紹介していましたが、公開サイトの文脈では、むしろ `外部妥当化と calibration` の役割が重要です。
- 根拠:
  - Zhang et al. (2006) は simultaneous scalp EEG/ECoG で cortical potential imaging を検証しました。
  - Seeber et al. (2019) は simultaneous DBS + 256ch scalp EEG で subcortical detectability を示しました。
  - ただしどちらも coverage-limited であり、全脳 ground truth を与えるわけではありません。
- 修正:
  - `EEG + 侵襲記録` を、gold standard ではなく `coverage-limited な validation route` として記述し直しました。

### 5. OPM-MEG を将来有望な装置として書けても、現時点の前提条件が抜けていました

- 問題:
  - 現行ページは OPM-MEG を前向きな extension として読める一方で、background field nulling と motion correction を伴う system engineering が不可欠な点を落としていました。
- 根拠:
  - Boto et al. (2018) は wearable OPM-MEG の可能性を示しましたが、同時に shielded environment と system-level engineering の重要性も示しています。
- 修正:
  - `簡単な携帯代替装置ではない` ことを明示しました。

## 今回実行した変更

- `wiki/multimodal-integration-basics.md`
  - front matter を技術・自然科学中心へ更新
  - 一般論中心の説明を削除し、一次文献ベースの `5つの監査ゲート` に再構成
  - `EEG + MRI`, `EEG + MEG`, `EEG + fMRI`, `EEG + 侵襲記録`, `OPM-MEG` を evidence-based に比較
  - 公開サイトでの読み替えルールを明記
  - 参考文献を一次文献中心で新設

## 外部依存で保留

- simultaneous scalp EEG + intracranial recording の 2024-2026 年系 validation literature の継続監視
  - 担当者: AI / maintainer
  - 前提条件: peer-reviewed の新規 validation 論文が継続的に出ること
  - 完了条件: scalp-to-intracranial mapping の generalization 限界が、preprint ではなく査読済み文献で追加整理されること

## 参考文献

- Pernet CR, Appelhoff S, Gorgolewski KJ, et al. EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. Sci Data. 2019.
  - https://doi.org/10.1038/s41597-019-0104-8
- Pernet C, Garrido MI, Gramfort A, et al. Issues and recommendations from the OHBM COBIDAS MEEG committee for reproducible EEG and MEG research. Nat Neurosci. 2020.
  - https://doi.org/10.1038/s41593-020-00709-0
- Jorge J, Grouiller F, Ipek O, et al. Simultaneous EEG-fMRI at ultra-high field: artifact prevention and safety assessment. NeuroImage. 2015.
  - https://doi.org/10.1016/j.neuroimage.2014.10.055
- Jorge J, Grouiller F, Gruetter R, et al. Towards high-quality simultaneous EEG-fMRI at 7 T: Detection and reduction of EEG artifacts due to head motion. NeuroImage. 2015.
  - https://doi.org/10.1016/j.neuroimage.2015.07.020
- Wirsich J, Jorge J, Iannotti GR, et al. The relationship between EEG and fMRI connectomes is reproducible across simultaneous EEG-fMRI studies from 1.5T to 7T. NeuroImage. 2021.
  - https://doi.org/10.1016/j.neuroimage.2021.117864
- Aydin U, Vorwerk J, Kupper P, et al. Combining EEG and MEG for the reconstruction of epileptic activity using a calibrated realistic volume conductor model. PLoS ONE. 2014.
  - https://doi.org/10.1371/journal.pone.0093154
- Zhang Y, Ding L, van Drongelen W, et al. A cortical potential imaging study from simultaneous extra- and intracranial electrical recordings by means of the finite element method. NeuroImage. 2006.
  - https://doi.org/10.1016/j.neuroimage.2006.02.027
- Seeber M, Cantonas LM, Hoevels M, et al. Subcortical electrophysiological activity is detectable with high-density EEG source imaging. Nat Commun. 2019.
  - https://doi.org/10.1038/s41467-019-08725-w
- Unnwongse K, Achakulvisut T, Wu JY, et al. Direct validation of EEG source imaging by intracranial electric stimulation in human patients. Brain Commun. 2023.
  - https://doi.org/10.1093/braincomms/fcad023
- Boto E, Holmes N, Leggett J, et al. Moving magnetoencephalography towards real-world applications with a wearable system. Nature. 2018.
  - https://doi.org/10.1038/nature26147
