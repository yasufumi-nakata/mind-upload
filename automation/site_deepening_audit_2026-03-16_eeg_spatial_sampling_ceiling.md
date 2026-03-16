# Site Deepening Audit (2026-03-16, EEG Spatial Sampling / Electrode Density Ceiling)

## 対象

- 主対象: `eeg_101.md`
- 副対象: `wiki/eeg-basics.md`

## 今回の選定理由

- 2026-03-16 時点の公開サイトは、EEG の `observability / identifiability / deployability` をかなり整理できていました。
- しかし `eeg_101.md` の「256ch まで増やしても独立自由度はセンサー数よりかなり少ない」という一文は、方向性としては正しい一方、次の 4 つをまだ十分に分けられていませんでした。
  - `電極本数`
  - `頭皮場の空間サンプリング`
  - `source localization の条件付き改善`
  - `WBE に十分な情報量`
- この混線は技術・自然科学の観点で重要です。なぜなら、一次文献は「高密度化が全く無意味」とも「高密度化で内部状態がほぼ分かった」とも言っておらず、改善する層と止まる層を分けているからです。

## 主要な批判点

### 1. 旧文面は `電極数の増加` を 1 本の意味で読める構造でした

- 問題:
  - 旧 `eeg_101.md` は `センサー数と独立情報は同じではない` と書いていました。
  - ただし、これだけでは読者が
    - `128ch を超える増設は全部無意味`
    - `256ch まで増やしたのでかなり state-complete に近づいた`
    のどちらにも誤読できる余地が残っていました。
- 根拠:
  - <https://doi.org/10.1046/j.1460-9568.1998.00269.x> の Srinivasan et al. (1998) は、頭蓋を介した空間 low-pass により scalp potential が広く相関しうることを示しました。
  - <https://doi.org/10.1088/1741-2552/ac288c> の Iivanainen et al. (2021) は、EEG head-surface field estimation が約 110 spatial samples までは改善しうると報告しました。
- 批判:
  - したがって、`少数電極で十分` も `電極数 = 独立自由度` も、どちらも一次文献の支持を超えています。

### 2. 旧文面は `local super-Nyquist benefit` を前面化できていませんでした

- 問題:
  - 旧版は高密度 EEG の価値を主として `深部 detectability` と `source imaging` の文脈で説明していました。
  - しかし、頭皮場 sampling 自体の前進を示す文献が出ていませんでした。
- 根拠:
  - <https://doi.org/10.1038/s41598-017-16377-3> の Robinson et al. (2017) は、視覚野上の 14 mm spacing の super-Nyquist-density EEG が、標準密度 subset より追加情報を与えると示しました。
- 批判:
  - したがって、`128ch 以上の増設は原理的に無意味` という読みは止める必要があります。
  - ただし改善対象は局所 cortical discriminability であり、これをそのまま `whole-brain state completeness` へ上げることもできません。

### 3. 旧文面は `count` と `coverage` を十分に分けていませんでした

- 問題:
  - 旧版は `チャンネル数を増やす` という表現が中心で、どこを覆うかという幾何学的条件が弱かったです。
- 根拠:
  - <https://doi.org/10.1046/j.1460-9568.2003.02483.x> の Lantz et al. (2003) は、31→63→123 electrodes で epileptic source localization が段階的に改善すると示しました。
  - <https://doi.org/10.1016/j.jneumeth.2015.08.015> の Song et al. (2015) は、superior scalp だけでなく inferior coverage を含む whole-head dense sampling が source localization を最も改善すると示しました。
- 批判:
  - したがって `本数だけ多ければよい` とも `本数だけ見れば比較できる` とも書けません。
  - site rule として、`spacing / coverage / MRI / conductivity / external validation` を一体で監査する必要があります。

### 4. 旧文面は `高密度化の価値` と `WBE に足りない理由` を同じ段で処理していました

- 問題:
  - 旧版は高密度化の ceiling を正しく保守的に書いていましたが、`何は改善しうるのか` と `それでも何が欠けるのか` の二層構造が弱かったです。
- 根拠:
  - <https://doi.org/10.1038/s41467-019-08725-w> の Seeber et al. (2019) は条件付きの subcortical detectability を示しました。
  - <https://doi.org/10.1093/braincomms/fcad023> の Unnwongse et al. (2023) は localization error が skull conductivity と source depth に依存することを示しました。
  - <https://doi.org/10.1111/epi.18552> の Hao et al. (2025) は simultaneous HD-EEG/SEEG で source power と source depth が誤差を大きく左右すると示しました。
- 批判:
  - これらは `conditional detectability` と `error auditability` を強めますが、cell / synapse / glia / neuromodulatory field を直接取得した証拠ではありません。
  - よって、高密度 EEG を `macro state constraint` としては強く評価しつつ、WBE sufficiency へは上げないと明文化する必要があります。

## 今回実行した変更

- `eeg_101.md`
  - `page_highlights` に、電極数・被覆・super-Nyquist・WBE sufficiency を同一視しないルールを追加
  - `EEGの情報理論的限界とWBEへの含意` 節を改稿
  - `問い / 一次文献 / 読み替え` の表を追加し、`field sampling`、`local cortical discriminability`、`source localization`、`WBE sufficiency` を分離
  - `何をもって改善と呼ぶか` に `spacing / coverage / conductivity / external validation` を追加
  - 参考文献に Srinivasan 1998、Lantz 2003、Song 2015、Robinson 2017、Iivanainen 2021 を追加
- `wiki/eeg-basics.md`
  - `last_updated` を 2026-03-16 に更新
  - `電極を増やすと何が変わるか` 節を新設
  - 初学者向けに `field sampling / local information / source localization / WBE sufficiency` を表で分離
  - 参考文献を追加

## 今回の結論

- `高密度 EEG に価値がある` と `EEG だけでかなり分かった` は別です。
- `128ch 以上は全部同じ` も、`電極数を増やせば内部状態の独立自由度が増える` も、どちらも一次文献の支持を超えます。
- 公開サイトでは今後、電極密度の話を
  - `head-surface field sampling`
  - `coverage-aware source localization`
  - `conditional detectability`
  - `WBE state-completeness ceiling`
  に分けて読みます。

## 参考文献

1. Srinivasan R, Nunez PL, Silberstein RB. Spatial filtering and neocortical dynamics: estimates of EEG coherence. *Electroencephalogr Clin Neurophysiol*. 1998;106(3):249-260. <https://doi.org/10.1046/j.1460-9568.1998.00269.x>
2. Lantz G, Grave de Peralta R, Spinelli L, Seeck M, Michel CM. Epileptic source localization with high density EEG: how many electrodes are needed? *Eur J Neurosci*. 2003;17(1):63-69. <https://doi.org/10.1046/j.1460-9568.2003.02483.x>
3. Song J, Davey C, Poulsen C, et al. EEG source localization: Sensor density and head surface coverage. *J Neurosci Methods*. 2015;256:9-21. <https://doi.org/10.1016/j.jneumeth.2015.08.015>
4. Robinson AK, Venkatesh P, Boring MJ, et al. Very high density EEG elucidates spatiotemporal aspects of early visual processing. *Sci Rep*. 2017;7:16248. <https://doi.org/10.1038/s41598-017-16377-3>
5. Iivanainen J, Stenroos M, Nummenmaa A, Parkkonen L. On the effect of spatial sampling in EEG head-surface field estimation and optimization. *J Neural Eng*. 2021. <https://doi.org/10.1088/1741-2552/ac288c>
6. Seeber M, Cantonas L-M, Hoevels M, et al. Subcortical electrophysiological activity is detectable with high-density EEG source imaging. *Nat Commun*. 2019;10:753. <https://doi.org/10.1038/s41467-019-08725-w>
7. Unnwongse K, Achakulvisut T, Wu JY, et al. Direct validation of EEG source imaging by intracranial electric stimulation in human patients. *Brain Commun*. 2023;5(2):fcad023. <https://doi.org/10.1093/braincomms/fcad023>
8. Hao S, Zhao H, Feng Z, et al. HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. *Epilepsia*. 2025;66(11):4451-4464. <https://doi.org/10.1111/epi.18552>
