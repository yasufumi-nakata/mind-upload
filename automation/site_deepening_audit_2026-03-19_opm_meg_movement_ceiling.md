# Site Deepening Audit (2026-03-19, OPM-MEG / Movement-Tolerant Measurement Ceiling)

## 対象

- 主対象: `perspective.md`
- 副対象: `tech_roadmap.md`
- 副対象: `wiki/multimodal-integration-basics.md`

## 今回の選定理由

- 2026-03-19 時点の公開サイトは、`connectome != state-complete`、`BOLD != neural difference without vascular audit`、`low latency != solved embodiment` など、主要な過大読解をかなり強く止められていました。
- その一方で `OPM-MEG / wearable MEG` の記述だけは相対的に薄く、`動ける`、`自然な課題に近い`、`hyperscanning もできる` といった語が、他ページの厳しい claim ceiling に比べて一段楽に読める状態でした。
- これは技術・自然科学の観点で弱点です。一次文献は、OPM-MEG が本当に前進していることを示す一方で、その前進が
  - `shielding`
  - `active field control`
  - `sensor calibration / co-registration`
  - `anatomy route`
  - `crosstalk management`
  の上に成り立っていることも明確に示しているからです。

## 根拠付き批判

### 1. 旧本文は `wearable` を `measurement condition eased` と読みやすくしていました

- 問題:
  - `perspective.md` の proposal 48 は、OPM-MEG の portability と freedom of movement を前面に出しており、読者が `自然主義的課題での高時間分解能計測がほぼ技術的に解けた` と受け取りやすい構造でした。
- 根拠:
  - Boto et al. (2018) は wearable OPM-MEG の重要な proof-of-concept を示しました。
  - Seymour et al. (2021) は standing / mobile participant 条件へ進めました。
- 批判:
  - しかし、これらは `movement-tolerant measurement became possible` を支えるのであって、`ordinary-room naturalistic measurement is routine` を支えるわけではありません。
  - `wearable` は claim ceiling を自動で上げません。まず固定すべきは measurement condition です。

### 2. 旧 OPM 記述は `movement tolerance` と `magnetic-environment control` を分離していませんでした

- 問題:
  - 公開本文は OPM-MEG の利点を述べていましたが、`zero-field requirement`、`shielded room`、`active nulling`、`motion-aware correction` がどこまで必須かを十分に前景化していませんでした。
- 根拠:
  - Mellor et al. (2022) は moving OP-MEG で field mapping / correction が必要になることを示しました。
  - Rea et al. (2021) は precision magnetic field modelling and control を示しました。
  - Holmes et al. (2023) は matrix coil active shielding により ambulatory movement を可能にしました。
  - Holmes et al. (2025) は lightly shielded environment でも tSSS と active compensation が要ることを示しました。
- 批判:
  - したがって `movement tolerance` は `field environment solved` と同義ではありません。
  - 安全な読解は `movement-tolerant macro electrophysiology under disclosed magnetic control` です。

### 3. 旧 site は `source reconstruction ceiling` を OPM 側では十分に書けていませんでした

- 問題:
  - OPM の portability を強く読むと、読者は source reconstruction まで一緒に成熟したかのように受け取りやすくなります。
- 根拠:
  - Iivanainen et al. (2022) は sensor gain / position / orientation calibration を独立課題として扱っています。
  - Rhodes et al. (2025) は pseudo-MRI route が useful である一方、individual MRI が gold standard であることを明示しています。
- 批判:
  - したがって OPM は `head-mounted sensor` であっても、`calibration-free` や `anatomy-free` ではありません。
  - source claim はなお sensor localization と anatomy route の disclosure を必要とします。

### 4. 旧 site は `higher channel density` を engineering maturity と取り違えうる状態でした

- 問題:
  - OPM arrays は今後の高密度化が期待されますが、channel 数の増加だけを progress と読むと sensor-level error が隠れます。
- 根拠:
  - Wu et al. (2025) は OPM array の crosstalk reduction を独立課題として扱い、noise floor を約 45 から 20 fT/Hz^1/2 へ下げたことを示しました。
- 批判:
  - これは `array engineering` がまだ測定 ceiling の一部であることを意味します。
  - よって `more sensors` は `mature measurement class` の同義語ではありません。

### 5. `hyperscanning` も proof-of-concept と general route を分ける必要がありました

- 問題:
  - proposal 48 の見出しは `OPM-MEG/Hyper-scanning` を並列に置いていましたが、どこまでが proof-of-concept でどこから一般化不能かを本文が明示していませんでした。
- 根拠:
  - Holmes et al. (2023) は 2 人課題で wearable MEG hyperscanning を実証しましたが、matrix-coil field nulling と constrained task を伴う proof-of-concept でした。
- 批判:
  - したがって safe reading は `two-person interactive proof-of-concept under field nulling`, であり、`dual-brain naturalistic route is mature` ではありません。

## 今回実行した変更

- `perspective.md`
  - proposal 48 を全面改稿しました。
  - `OPM-MEG / hyperscanning` を `movement-tolerant measurement under shielding and calibration gates` として再定義しました。
  - `wearable != shield-free`, `wearable != calibration-free`, `wearable != state-complete` を本文で固定しました。
  - OPM-specific references を追加しました。
- `tech_roadmap.md`
  - page highlights / known points に OPM-MEG の safe reading を追加しました。
  - `M5` に 2026-03-19 supplement を追加し、field control / calibration / anatomy route を明示しました。
  - literature row `Measurement extension (OPM etc.)` を実際の OPM primary literature に差し替えました。
  - 参考文献を追加しました。
- `wiki/multimodal-integration-basics.md`
  - `last_updated` を `2026-03-19` に更新しました。
  - OPM row を改稿し、movement-tolerant advance と engineering ceiling を分けました。
  - 新規節 `OPM-MEG expands movement tolerance, but not without magnetic-field and source-model audits` を追加しました。
  - site rule に `wearable does not waive shielding / field nulling / co-registration / anatomy / crosstalk audit` を追加しました。
  - 参考文献を追加しました。

## 外部依存で保留

- なし
  - 今回の作業は、公開本文・参考文献・claim ceiling の改稿で完結しています。

## 参考文献

1. Boto E, Holmes N, Leggett J, et al. Moving magnetoencephalography towards real-world applications with a wearable system. *Nature*. 2018;555:657-661.
   - https://doi.org/10.1038/nature26147
2. Seymour RA, Alexander N, Mellor S, et al. Using OPMs to measure neural activity in standing, mobile participants. *NeuroImage*. 2021;244:118604.
   - https://doi.org/10.1016/j.neuroimage.2021.118604
3. Mellor SJ, Tierney TM, O'Neill GC, et al. Magnetic Field Mapping and Correction for Moving OP-MEG. *IEEE Transactions on Biomedical Engineering*. 2022;69(2):528-536.
   - https://doi.org/10.1109/TBME.2021.3100770
4. Rea M, Holmes N, Hill RM, et al. Precision magnetic field modelling and control for wearable magnetoencephalography. *NeuroImage*. 2021;241:118401.
   - https://doi.org/10.1016/j.neuroimage.2021.118401
5. Holmes N, Rea M, Hill RM, et al. Enabling ambulatory movement in wearable magnetoencephalography with matrix coil active magnetic shielding. *NeuroImage*. 2023;274:120157.
   - https://doi.org/10.1016/j.neuroimage.2023.120157
6. Holmes N, Rea M, Hill RM, et al. Naturalistic hyperscanning with wearable magnetoencephalography. *Sensors*. 2023;23(12):5454.
   - https://doi.org/10.3390/s23125454
7. Holmes N, Leggett J, Hill RM, et al. Wearable magnetoencephalography in a lightly shielded environment. *IEEE Transactions on Biomedical Engineering*. 2025;72(2):609-618.
   - https://doi.org/10.1109/TBME.2024.3465654
8. Iivanainen J, Borna A, Zetter R, et al. Calibration and Localization of Optically Pumped Magnetometers Using Electromagnetic Coils. *Sensors*. 2022;22(8):3059.
   - https://doi.org/10.3390/s22083059
9. Rhodes N, Rier L, Boto E, Hill RM, Brookes MJ. Source reconstruction without an MRI using optically pumped magnetometer-based magnetoencephalography. *Imaging Neuroscience*. 2025;3:IMAG.a.8.
   - https://doi.org/10.1162/IMAG.a.8
10. Wu T, Xiao W, Peng X, Wu T, Guo H. Crosstalk reduction in optically pumped magnetometers arrays for biomagnetic measurement. *Review of Scientific Instruments*. 2025;96(8):085004.
   - https://doi.org/10.1063/5.0273491
