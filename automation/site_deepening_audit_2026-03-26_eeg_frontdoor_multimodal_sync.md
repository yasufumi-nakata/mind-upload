# Site Deepening Audit (2026-03-26, EEG front-door multimodal sync)

## 対象

- 主対象: `eeg_101.md`
- 同期対象: `wiki/eeg-basics.md`
- エクスポート同期: `github-wiki-export/eeg-basics.md`
- 再生成対象: `summary_booklet.md`
- web確認対象:
  - `https://doi.org/10.1162/IMAG.a.136`
  - `https://doi.org/10.1038/s41467-023-44363-z`
  - `https://doi.org/10.1038/s41467-025-64414-x`
  - `https://doi.org/10.1162/imag_a_00287`
  - `https://doi.org/10.1038/s42003-019-0659-0`
  - `https://doi.org/10.1038/s41593-025-02132-9`
  - `https://doi.org/10.1038/s41591-024-03019-1`
  - `https://doi.org/10.1093/brain/awac335`
  - `https://doi.org/10.1093/brain/awaf412`
- 調査範囲: 技術 / 自然科学のみ

## 今回この箇所を選んだ理由

- `verification.md` と `wiki/multimodal-integration-basics.md` ではすでに、
  - `Fusion Card`
  - `Human Proxy Composition Card`
  - shared-vs-specific decomposition
  - bundle robustness
  の停止線がかなり明確でした。
- しかし EEG の入口である `eeg_101.md` と、その beginner wiki である `wiki/eeg-basics.md` はまだ
  - `EEG に他モダリティを足すと空間情報が補える`
  - `same-session multimodal`
  - `shared factor`
  を、比較的素朴に読ませる構造が残っていました。
- そのままだと読者は
  - `同時計測できた`
  - `低周波の共通成分が見えた`
  - `精度が上がった`
  を、一続きの「multimodal なら state に近づく」という物語へ圧縮しやすいです。
- これは自然科学的に弱いです。一次文献が示しているのは、同期、融合妥当性、共有因子の特異性、bundle の可用性 / 転移性が別問題だということだからです。

## 根拠付き批判

### 1. `same-session multimodal` を `fusion validity` に読み替える停止線が EEG の入口で弱いままでした

- [Kothe et al. (2025)](https://doi.org/10.1162/IMAG.a.136) は LSL を `synchronization infrastructure` として整理しており、device-side delay truth そのものではありません。
- [Wei et al. (2020)](https://doi.org/10.1016/j.neuroimage.2020.116595) は EEG-fMRI fusion を model-conditioned inference problem として扱っています。
- [Vafaii et al. (2024)](https://doi.org/10.1038/s41467-023-44363-z) は simultaneous multimodal recordings に common と divergent の両方が残ることを示しました。
- [Chen et al. (2025)](https://doi.org/10.1038/s41467-025-64414-x) は simultaneous EEG-PET-MRI で coupled global dynamics と modality- / network-specific structure の共存を示しました。

批判:

- よって `same-session` と `multimodal` は acquisition property の強化ではあっても、直ちに one validated biological variable を意味しません。
- EEG の入口ページがこの停止線を front-door で書かないままだと、より厳密な wiki / verification の規律を入口で弱めてしまいます。

### 2. `shared cross-modal factor` を `target neural variable` に読み替える停止線が不十分でした

- [Gold et al. (2024)](https://doi.org/10.1162/imag_a_00287) は simultaneous EEG-fMRI-autonomic recordings で vigilance 低下に伴って fMRI-autonomic covariance が増えることを示しました。
- [Özbay et al. (2019)](https://doi.org/10.1038/s42003-019-0659-0) は sympathetic activity が fMRI signal に寄与することを示しました。
- [Epp et al. (2025)](https://doi.org/10.1038/s41593-025-02132-9) は significant BOLD changes を示す voxel の約 40% で oxygen metabolism change が reversed でありうることを示しました。

批判:

- よって EEG-fMRI や EEG-PET-MRI の `shared factor` は、それだけでは `shared neural candidate` なのか `physiology-linked global factor` なのか `mixed / unresolved` なのかを固定しません。
- 入口ページがこの分解を前面化しないと、`共通因子が出た = 目的状態を見た` という過読が再発します。

### 3. `more modalities improved performance` を `robust bundle` に読み替える停止線が EEG の入口で不足していました

- [Rohaut et al. (2024)](https://doi.org/10.1038/s41591-024-03019-1) は clinically unresponsive brain-injury cohort で multimodal assessment が prognostic uncertainty を減らし、精度を改善しうることを示しました。
- [Amiri et al. (2023)](https://doi.org/10.1093/brain/awac335) は acute DoC cohort で same-sample multimodal prediction を separate analysis として扱っています。
- [Manasova et al. (2026)](https://doi.org/10.1093/brain/awaf412) は multicentre evaluation、missing-value substitution、hard subgroup における inter-modality disagreement を扱っています。

批判:

- したがって `multimodal gain` は real でも、availability-agnostic, transfer-stable, disagreement-resistant bundle を意味しません。
- EEG の front door が `bundle robustness` を明示しないままだと、prediction gain と deployable / robust bundle が同じ意味に読まれてしまいます。

## 今回実行した変更

- `eeg_101.md`
  - `last_updated` を `2026-03-26` に更新しました。
  - front matter の `page_highlights` / `known_points` に
    - same-session multimodal は self-validating ではない
    - shared factor は mixed physiology たりうる
    - multimodal gain は bundle robustness ではない
    を追加しました。
  - 冒頭の `Misreadings worth stopping early` に `multimodal is not an escape hatch` を追加しました。
  - multimodal section を改稿し、
    - EEG + fMRI の vascular interpretation stop line
    - EEG + PET + MRI row
    - `Fusion Card` 必須
    - shared-factor specificity
    - bundle robustness / complete-case / transfer / disagreement
    - `Human Proxy Composition Card` 追加条件
    を front-door に前倒ししました。
  - 参考文献に Kothe 2025, Wei 2020, Vafaii 2024, Chen 2025, Gold 2024, Özbay 2019, Epp 2025, Rohaut 2024, Amiri 2023, Manasova 2026 を追加しました。

- `wiki/eeg-basics.md`
  - `last_updated` を `2026-03-26` に更新しました。
  - front matter の `page_highlights` / `known_points` を site-wide multimodal rule に同期しました。
  - `Wiki: Basics of multimodal integration` への導線を追加しました。
  - beginner note を追加し、
    - same-session multimodal
    - shared factor
    - bundle robustness
    を EEG beginner route の段階で止めるよう改稿しました。
  - `Fusion Card` と `Human Proxy Composition Card` への導線を追加しました。
  - 参考文献に上記 multimodal / bundle robustness 文献を追加しました。

## 今回止めた誤読

- `same-session multimodal = fusion validated`
- `shared cross-modal factor = target neural variable`
- `EEG + fMRI = added spatial truth`
- `EEG + PET + MRI = fused state ground truth`
- `more modalities improved performance = robust bundle`
- `multimodal alone = enough to raise the human claim ceiling`

## 外部依存タスク

- なし
  - 今回の変更は repo 内の公開本文、wiki、export、summary 再生成で完結しました。

## 参考文献

1. Kothe C, Shirazi SY, Stenner T, et al. The lab streaming layer for synchronized multimodal recording. *Imaging Neuroscience*. 2025;3:IMAG.a.136.
   - https://doi.org/10.1162/IMAG.a.136
2. Wei H, Jafarian A, Zeidman P, et al. Bayesian fusion and multimodal DCM for EEG and fMRI. *NeuroImage*. 2020;211:116595.
   - https://doi.org/10.1016/j.neuroimage.2020.116595
3. Vafaii H, Mandino F, Desrosiers-Grégoire G, et al. Multimodal measures of spontaneous brain activity reveal both common and divergent patterns of cortical functional organization. *Nature Communications*. 2024;15:581.
   - https://doi.org/10.1038/s41467-023-44363-z
4. Chen JE, Lewis LD, Coursey SE, et al. Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep. *Nature Communications*. 2025;16:8887.
   - https://doi.org/10.1038/s41467-025-64414-x
5. Gold BP, Goodale SE, Zhao C, et al. Functional MRI signals exhibit stronger covariation with peripheral autonomic measures as vigilance decreases. *Imaging Neuroscience*. 2024;2:IMAG.a.00287.
   - https://doi.org/10.1162/imag_a_00287
6. Özbay PS, Chang C, Picchioni D, et al. Sympathetic activity contributes to the fMRI signal. *Communications Biology*. 2019;2:421.
   - https://doi.org/10.1038/s42003-019-0659-0
7. Epp SM, Castrillón G, Yuan B, et al. BOLD signal changes can oppose oxygen metabolism across the human cortex. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-02132-9
8. Rohaut B, Hermann B, Kaufmann BC, et al. Multimodal assessment improves neuroprognosis performance in clinically unresponsive critical-care patients with brain injury. *Nature Medicine*. 2024;30:2482-2491.
   - https://doi.org/10.1038/s41591-024-03019-1
9. Amiri M, Bødker Andersen M, Jørgensen SH, et al. Multimodal prediction of residual consciousness in the intensive care unit: the CONNECT-ME study. *Brain*. 2023;146(1):50-64.
   - https://doi.org/10.1093/brain/awac335
10. Manasova D, Belloli LML, Rosenfelder MJ, et al. Multimodal multicentre investigation of diagnostic and prognostic markers in disorders of consciousness. *Brain*. 2026.
   - https://doi.org/10.1093/brain/awaf412
