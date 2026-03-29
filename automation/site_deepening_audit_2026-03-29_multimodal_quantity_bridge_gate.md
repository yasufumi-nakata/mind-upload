# Site Deepening Audit (2026-03-29, multimodal quantity-bridge gate)

## 対象

- 主対象:
  - `wiki/multimodal-integration-basics.md`
- 同期確認対象:
  - `index.md`
  - `verification.md`
  - `research_harvest_50.md`
  - `wiki/human-proxy-composition.md`
- 調査範囲: 技術 / 自然科学のみ
- 明示的に除外した論点: 哲学、法学、制度論

## web確認対象

- `https://doi.org/10.1162/IMAG.a.136`
- `https://doi.org/10.1038/s41467-023-44363-z`
- `https://doi.org/10.1038/s41467-025-64414-x`
- `https://doi.org/10.1038/s41593-025-01945-y`
- `https://doi.org/10.1038/s41593-025-02132-9`
- `https://doi.org/10.1093/brain/awac335`
- `https://doi.org/10.1093/brain/awaf412`
- `https://doi.org/10.1016/j.neuroimage.2021.117864`
- `https://doi.org/10.1016/j.neuroimage.2020.116595`
- `https://doi.org/10.1038/s41591-024-03019-1`

## 今回この箇所を選んだ理由

- 2026-03-29 時点の site-wide rule では、multimodal の読み方はすでに
  - `synchronization infrastructure`
  - `shared-vs-specific component evidence`
  - `quantity bridge / physiology grounding`
  - `bundle robustness`
  に分けて扱われております。
- しかし `wiki/multimodal-integration-basics.md` では、
  - 同時取得であること
  - 共通因子があること
  - 実際に同じ生物学的量へ橋渡しできたこと
  の 3 段階目がまだ独立ゲートとして十分に固定されておりませんでした。
- このズレを放置すると、上位ページで止めている
  - `shared trajectory = same biological quantity`
  - `coupled multimodal dynamics = one solved neural state axis`
  という誤読が、基礎ページ側から再流入します。

## 主要結論

- multimodal の弱点は、もはや「同期できているか」だけではございません。
- 現在の一次文献では、少なくとも次を分けて読まなければなりません。
  - 共通時間軸があるか
  - 共通成分と modality-specific 成分を分離したか
  - その共通成分がどの biological axis に載るのか
  - 欠損モダリティ / complete-case / cross-centre で bundle が崩れないか
- したがって `wiki/multimodal-integration-basics.md` には、`quantity bridge / physiology grounding` を独立ゲートとして明示する必要がございました。

## 根拠付き批判

### 1. 共通因子があっても、同じ biological quantity を読んでいるとは限りません

- [Vafaii et al. (2024)](https://doi.org/10.1038/s41467-023-44363-z) は、simultaneous Ca2+ と BOLD で `common` と `divergent` の両方の構造を示しました。
- [Chen et al. (2025)](https://doi.org/10.1038/s41467-025-64414-x) は、simultaneous EEG-PET-MRI で wakefulness から NREM への descent において tightly coupled global progression を示しつつ、同時に distinct network patterns も示しました。

批判:

- したがって、`same-session` や `shared factor` を見た瞬間に `one solved biological variable` と読むのは不正確でございます。
- 共通成分の存在は、量の一致を保証せず、せいぜい `shared trajectory exists` まででございます。

### 2. グローバル multimodal mode は autonomic / arousal route を混ぜ得ます

- [Bolt et al. (2025)](https://doi.org/10.1038/s41593-025-01945-y) は、major low-frequency global fMRI mode が EEG と複数の autonomic signal に結びつくことを示しました。
- [Özbay et al. (2019)](https://doi.org/10.1038/s42003-019-0659-0) は、EEG-marked arousal change 中の fMRI signal に sympathetic activity が寄与しうることを示しました。

批判:

- これは `shared multimodal factor` が、そのまま target neural variable を意味しないことを示します。
- 少なくとも `shared neural candidate`、`mixed arousal physiology`、`unresolved common mode` のどれかを named axis として明示しない限り、biology-side の読解は強すぎます。

### 3. 量の向きすら一致しない場合があるため、quantity bridge は独立に要求されるべきです

- [Epp et al. (2025)](https://doi.org/10.1038/s41593-025-02132-9) は、significant task-related BOLD changes と oxygen-metabolism changes が多くの cortical voxels で opposite sign を取り得ることを示しました。

批判:

- これにより、`coupled hemodynamic and metabolic response` と `same quantity` は同義ではなくなります。
- shared-vs-specific decomposition を通しても、まだ `hemodynamic quantity` と `metabolic quantity` の橋渡しは残ります。
- したがって `quantity bridge / physiology grounding` は、`shared-vs-specific` とは別ゲートであるべきでございます。

### 4. bundle-level gain も quantity bridge を代替しません

- [Rohaut et al. (2024)](https://doi.org/10.1038/s41591-024-03019-1) は、acute brain injury において multimodal assessment の追加が prognostic uncertainty を下げ、accuracy を改善しうることを示しました。
- [Amiri et al. (2023)](https://doi.org/10.1093/brain/awac335) は、same-sample multimodal comparison が `48 complete-feature patients` に縮むことを示しました。
- [Manasova et al. (2026)](https://doi.org/10.1093/brain/awaf412) は、missing values を代入しつつ multicentre generalization を検証し、hard subgroup で inter-modality disagreement が上がることを示しました。

批判:

- これらは `bundle performance` と `bundle robustness` に関する一次 evidence であって、`same biological quantity` の証明ではございません。
- よって availability / transfer / disagreement を通ったとしても、quantity bridge を別に問わなければなりません。

### 5. 基礎ページだけが粗いままだと、上位ページの停止線が崩れます

- `research_harvest_50.md` では、すでに multimodal を
  - synchronization infrastructure
  - shared-vs-specific component evidence
  - quantity bridge / physiology grounding
  - bundle robustness
  に分けております。
- `verification.md` と `wiki/human-proxy-composition.md` でも、`common-driver / quantity-bridge gate` がすでに site rule として明示されております。

批判:

- それにもかかわらず `wiki/multimodal-integration-basics.md` だけが quantity bridge を独立 gate として固定しないと、サイト内で最も基礎的な multimodal 説明が最も古い読解規則を再生産してしまいます。

## 今回実行した変更

- `wiki/multimodal-integration-basics.md`
  - `9 audit gates` を `10 audit gates` に更新しました。
  - `shared-vs-specific` と独立した `Quantity-bridge / physiology-grounding gate` を追加しました。
  - 新規 note box `A coupled trajectory is not yet a quantity bridge` を追加しました。
  - `Minimum fusion package` に `quantity bridge / physiology grounding` を追加しました。
  - tri-modal EEG-PET-MRI 節を更新し、correlation と quantity bridge を区別するようにしました。

## 今回止めた誤読

- `same-session multimodal` = `same biological quantity`
- `shared factor` = `target neural variable`
- `bundle accuracy improved` = `quantity bridge solved`
- `hemodynamic-metabolic coupling` = `same physiology with same sign and same interpretation`
- `multimodal basics page だから少し粗くてよい`

## 外部依存タスク

- なし
  - 今回の変更は、web 上の一次文献確認、repo 内公開本文修正、監査メモ追加、検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Kothe C, Shirazi SY, Stenner T, et al. The lab streaming layer for synchronized multimodal recording. *Imaging Neuroscience*. 2025.
   - https://doi.org/10.1162/IMAG.a.136
2. Wei H, Jafarian A, Zeidman P, et al. Bayesian fusion and multimodal DCM for EEG and fMRI. *NeuroImage*. 2020.
   - https://doi.org/10.1016/j.neuroimage.2020.116595
3. Vafaii P, Raut RV, Snyder AZ, et al. Common and divergent organization of neural activity in the cortex across multiple timescales and modalities. *Nature Communications*. 2024.
   - https://doi.org/10.1038/s41467-023-44363-z
4. Chen M, Feng P, Zheng J, et al. Simultaneous EEG-PET-fMRI reveals coupled global and distinct network dynamics during the wakefulness-to-sleep transition. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-64414-x
5. Bolt TS, Turchi J, Moia S, et al. A major low-frequency global fMRI mode is coupled to EEG and autonomic physiology. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-01945-y
6. Özbay PS, Chang C, Picchioni D, et al. Sympathetic activity contributes to the fMRI signal. *Communications Biology*. 2019.
   - https://doi.org/10.1038/s42003-019-0659-0
7. Epp SM, Castrillon G, Yuan B, et al. BOLD signal changes can oppose oxygen metabolism across the human cortex. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-02132-9
8. Wirsich J, Jorge J, Iannotti GR, et al. The relationship between EEG and fMRI connectomes is reproducible across simultaneous EEG-fMRI studies from 1.5T to 7T. *NeuroImage*. 2021.
   - https://doi.org/10.1016/j.neuroimage.2021.117864
9. Amiri M, Claassen J, Geeraerts T, et al. Multimodal prediction of residual consciousness in the intensive care unit: the CONNECT-ME study. *Brain*. 2023.
   - https://doi.org/10.1093/brain/awac335
10. Rohaut B, Claassen J, Kondziella D, et al. Multimodal neurodiagnostic and prognostic evaluation of acute brain injury. *Nature Medicine*. 2024.
   - https://doi.org/10.1038/s41591-024-03019-1
11. Manasova D, Hermann B, Calligaris C, et al. Multimodal multicentre investigation of diagnostic and prognostic markers in disorders of consciousness. *Brain*. 2026.
   - https://doi.org/10.1093/brain/awaf412
