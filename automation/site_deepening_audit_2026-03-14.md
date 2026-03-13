# Site Deepening Audit (2026-03-14)

## 対象

- 主対象: `eeg_101.md`
- 副対象: `datasets.md`

## 今回の選定理由

- この2ページは、公開サイト内で「EEG が WBE にどこまで寄与できるか」を読む際の基準点でございます。
- ここが曖昧だと、他ページの `decode vs emulate`、`verification`、`roadmap` の主張も甘く読まれやすくなります。
- 既存説明は大筋で正しい一方、`必須要件`、`有望な候補手法`、`将来の拡張` が一部混在しており、source imaging を過大評価しやすい構造が残っていました。

## 主要な批判点

### 1. `eeg_101.md` は手法名を先に出しすぎていた

- 問題:
  - 既存の ESI 節では、Champagne、HBM、ASR、ZapLine-plus などが、あたかも現在の標準解であるかのように読める箇所がありました。
  - しかし、Michel & Brunet (2019) は個体別 MRI、実測電極位置、conductivity 仮定、visual inspection を重視しており、固定レシピを標準化していません。
  - COBIDAS-MEEG も、まず重視するのは透明な報告と再現可能な記録であり、特定アルゴリズムの採択そのものではありません。
- 修正:
  - `報告の床 / 幾何の床 / 妥当化の床` という3段の証拠鎖へ再編しました。
  - `必須` と `有望だが候補` を分離し、手法名より benchmark と誤差報告を先に置く構成へ変更しました。

### 2. 深部 source に関する説明は、成立条件をもっと明示すべきだった

- 問題:
  - 既存ページは「深部はまったく不可能ではない」と正しく補足していましたが、その一方で、どの程度 task-specific で、どの程度誤差が残るかの記述が薄めでした。
  - Seeber et al. (2019) は 256ch HD-EEG と同時 DBS 記録で深部検出の可能性を示しましたが、一般的な一意復元を示した研究ではありません。
  - Unnwongse et al. (2023) は、頭蓋内刺激を ground truth にした直接妥当化で、平均 localization error が 14.4–23.4 mm に達し、source depth と skull conductivity に強く依存することを示しています。
  - Mouthaan et al. (2019) の systematic review でも、presurgical epilepsy における source imaging は summary sensitivity 82%、specificity 53% で、全研究にバイアスが残っていました。
- 修正:
  - `実測エビデンスが示す上限` 節を追加し、「detectable」と「general reconstruction」は別だと明記しました。
  - 臨床・直接妥当化の結果を benchmark の上限として紹介し、WBE へ直結させない表現へ改めました。

### 3. `datasets.md` は「スターターデータの限界」は書いていたが、次の段階が弱かった

- 問題:
  - 既存ページは EEGMMI / CHB-MIT / Sleep-EDF / TUH EEG を適切に L0〜L1 の練習台として位置づけていました。
  - ただし、「では source imaging を深掘りしたいとき、何のデータへ進むべきか」が十分に固定されていませんでした。
  - その結果、読者が A 段階のスターターデータの延長で ESI 改善を主張できるかのように誤読する余地がありました。
- 修正:
  - `A: 練習台 / B: 解剖制約つき再構成 / C: 直接妥当化` の3段階データ階段を追加しました。
  - C 段階の具体例として、Localize-MI、頭蓋内刺激、同時 HD-EEG/SEEG、術後転帰つき cohort を明示しました。

## 今回実行した変更

- `eeg_101.md`
  - ESI 節を全面的に書き換え
  - multimodal integration 節を「利点」中心から「利点 + 追加監査負荷」へ修正
  - 参考文献に COBIDAS-MEEG、Mouthaan et al. (2019)、Jorge et al. (2015)、Aydin et al. (2014)、Boto et al. (2018) を追加
- `datasets.md`
  - `source imaging を深掘りするなら、データを3段階に分ける` 節を新設
  - Localize-MI、Hao et al. (2025)、Mouthaan et al. (2019) を参考文献へ追加

## 外部依存で保留

- 公開サイト全体で future-looking な reference を再監査する作業
  - 担当者: AI / maintainer
  - 前提条件: 全ページ参照リンクの棚卸し
  - 完了条件: DOI または一次ソース未確認の引用が site-wide でゼロ

## 参考文献

- Michel CM, Brunet D. EEG source imaging: a practical review of the analysis steps. Front Neurol. 2019.
  - https://doi.org/10.3389/fneur.2019.00325
- Pernet CR, et al. EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. Sci Data. 2019.
  - https://doi.org/10.1038/s41597-019-0104-8
- Pernet CR, et al. Best practices in data analysis and sharing in neuroimaging using MEEG. Nat Neurosci. 2020.
  - https://doi.org/10.1038/s41593-020-00709-0
- Hämäläinen MS, Ilmoniemi RJ. Interpreting magnetic fields of the brain: minimum norm estimates. NeuroImage. 1994.
  - https://doi.org/10.1016/1053-8119(94)90016-7
- Seeber M, et al. Subcortical electrophysiological activity is detectable with high-density EEG source imaging. Nat Commun. 2019.
  - https://doi.org/10.1038/s41467-019-08725-w
- Unnwongse K, et al. Validating EEG source imaging using intracranial electrical stimulation in focal epilepsy. Brain Commun. 2023.
  - https://doi.org/10.1093/braincomms/fcad023
- Mouthaan BE, et al. Diagnostic accuracy of interictal source imaging in presurgical epilepsy evaluation: a systematic review from the E-PILEPSY consortium. Clin Neurophysiol. 2019.
  - https://doi.org/10.1016/j.clinph.2018.12.016
- Mikulan E, et al. Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. Sci Data. 2020.
  - https://doi.org/10.1038/s41597-020-0467-x
- Hao Y, et al. HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. Epilepsia. 2025.
  - https://doi.org/10.1111/epi.18552
- Jorge J, et al. Simultaneous EEG-fMRI at ultra-high field: artifact prevention and safety assessment. NeuroImage. 2015.
  - https://doi.org/10.1016/j.neuroimage.2014.10.055
- Aydin U, et al. Combining EEG and MEG for the reconstruction of epileptic activity using a calibrated realistic volume conductor model. PLoS One. 2014.
  - https://doi.org/10.1371/journal.pone.0093154
- Boto E, et al. Moving magnetoencephalography towards real-world applications with a wearable system. Nature. 2018.
  - https://doi.org/10.1038/nature26147
