# Site Deepening Audit (2026-03-28, literature-hub multimodal route split)

## 対象

- 主対象:
  - `research_harvest_50.md`
  - `mind_uploading_papers.md`
- 調査範囲: 技術 / 自然科学のみ

## web確認対象

- `https://doi.org/10.1162/imag.a.136`
- `https://doi.org/10.1038/s41467-023-44363-z`
- `https://doi.org/10.1038/s41467-025-64414-x`
- `https://doi.org/10.1038/s41593-025-01945-y`
- `https://doi.org/10.1038/s41593-025-02132-9`
- `https://doi.org/10.1093/brain/awac335`
- `https://doi.org/10.1093/brain/awaf412`

## 今回この箇所を選んだ理由

- 公開サイトの core pages と wiki pages では、2026-03-28 時点ですでに multimodal を
  - synchronization infrastructure
  - shared-vs-specific component
  - hemodynamic / metabolic quantity bridge
  - bundle robustness under missing-modality / cross-centre stress
  に分けて読む stop line がかなり整っていました。
- しかし文献ハブである `mind_uploading_papers.md` と `research_harvest_50.md` では、この split がまだ弱く、
  - `multimodal`
  - `simultaneous`
  - `shared factor`
  - `better prediction`
  が入口で一つの進歩列として読める余地が残っていました。
- 文献ハブの front door が粗いと、詳細ページで止めている誤読が archive 側から再注入されます。

## 根拠付き批判

### 1. synchronized acquisition は device-side timing truth と同じではありません

- 根拠:
  - [Kothe et al. (2025)](https://doi.org/10.1162/imag.a.136) は、LSL が most neurobehavioral research に十分な msec-scale synchronization を提供しつつも、device-side delay は自動では分からず、各 stream ごとの測定が必要であることを明示しました。
- 批判:
  - したがって `shared clock` をそのまま `timing truth` と読むのは技術的に誤りでございます。
  - 文献ハブで multimodal を一語で扱うと、この difference が消えます。

### 2. common factor は target biological variable と同じではありません

- 根拠:
  - [Vafaii et al. (2024)](https://doi.org/10.1038/s41467-023-44363-z) は、simultaneous Ca2+ / BOLD から common organization だけでなく divergent organization も示しました。
  - [Chen et al. (2025)](https://doi.org/10.1038/s41467-025-64414-x) は、EEG-PET-MRI で coupled global dynamics と distinct network patterns を同時に示しました。
- 批判:
  - したがって `cross-modal commonality` を見たことと、`one state variable was identified` は別の成果でございます。
  - 文献ハブがこれを分けないと、multimodal gain が target-state identification に読み替えられます。

### 3. shared factor は autonomic / vascular physiology や quantity mismatch を含みえます

- 根拠:
  - [Bolt et al. (2025)](https://doi.org/10.1038/s41593-025-01945-y) は、major global fMRI mode が EEG と複数の peripheral autonomic signal にまたがる arousal response の substantial component であることを示しました。
  - [Epp et al. (2025)](https://doi.org/10.1038/s41593-025-02132-9) は、significant task-related BOLD voxels の約 40% で oxygen metabolism change が逆符号になりうることを示しました。
- 批判:
  - よって `shared low-frequency factor` や `same-session BOLD coupling` は、そのまま neural target variable ではありません。
  - 文献ハブは `shared physiology` と `quantity mismatch` を front door で止める必要があります。

### 4. multimodal gain は availability-agnostic robustness と同じではありません

- 根拠:
  - [Amiri et al. (2023)](https://doi.org/10.1093/brain/awac335) は、acute DoC の multimodal same-sample models が `n=48` の same-patient subset に依存したことを明示しました。
  - [Manasova et al. (2026)](https://doi.org/10.1093/brain/awaf412) は、multicentre multimodal setting で gain を示しつつ、pairwise disagreement が minimally conscious / improving patients で高いことを示しました。
- 批判:
  - `more modalities improved prediction` を `bundle is robust` に読み替えるのは科学的に弱いです。
  - complete-case slice、missing-modality handling、cross-centre transfer、hard-regime disagreement は別監査でございます。

## 今回実行した変更

- `research_harvest_50.md`
  - front matter の `page_highlights` / `known_points` に、U7 の multimodal route split を追加しました。
  - 技術優先 table の `Measurement and human observability` 行を更新し、multimodal paper の advance を
    - synchronized acquisition
    - shared-vs-specific component
    - quantity bridge
    - bundle robustness
    に分けて読むよう改稿しました。
  - 新規 note-box `Read U7 as more than synchronized clocks` を追加し、Kothe 2025, Vafaii 2024, Chen 2025, Bolt 2025, Epp 2025, Amiri 2023, Manasova 2026 を使って literature-hub の stop line を明文化しました。
  - `U7: Multimodal alignment` の traction / unresolved bullets を更新し、sync-only 読解を止めました。
  - U7 の representative references と major studies に multimodal shared-vs-specific / quantity mismatch / bundle robustness の一次文献を追加しました。

- `mind_uploading_papers.md`
  - front matter の `known_points` / `page_highlights` に multimodal route split を追加しました。
  - 技術導入文の multimodal clause を、単なる hemodynamic ceiling から
    - synchronized acquisition
    - shared-vs-specific structure
    - quantity bridge / hemodynamic grounding
    - robustness under missing-modality and centre-transfer stress
    へ更新しました。
  - technical-fast-lane table の `multimodal` row を全面改稿し、7 本の primary papers で route split を明示しました。
  - quick-start row `I want to see the multimodal ceiling` を更新し、multimodal paper を何順に読むかを operational に固定しました。

## 今回止めた誤読

- `simultaneous multimodal` = `timing truth まで解けた`
- `shared factor` = `target neural variable が同定された`
- `same-session hemodynamic-metabolic coupling` = `quantity bridge が解けた`
- `multimodal prediction improved` = `bundle が complete-case / transfer / disagreement に対して頑健`
- `multimodal` = one monotonic progress bar

## 外部依存タスク

- なし
  - 今回の変更は repo 内文書、監査メモ、検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Kothe C, Medine D, Grivich M, et al. The lab streaming layer for synchronized multimodal recording. *Imaging Neuroscience*. 2025.
   - https://doi.org/10.1162/imag.a.136
2. Vafaii H, Mandino F, Desrosiers-Grégoire G, et al. Multimodal measures of spontaneous brain activity reveal both common and divergent patterns of cortical functional organization. *Nature Communications*. 2024.
   - https://doi.org/10.1038/s41467-023-44363-z
3. Chen JE, Lewis LD, Coursey SE, et al. Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-64414-x
4. Bolt T, Wang S, Nomi JS, et al. Autonomic physiological coupling of the global fMRI signal. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-01945-y
5. Epp SM, Castrillón G, Yuan B, et al. BOLD signal changes can oppose oxygen metabolism across the human cortex. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-02132-9
6. Amiri M, Othman MH, Falah M, et al. Multimodal prediction of residual consciousness in the intensive care unit: the CONNECT-ME study. *Brain*. 2023.
   - https://doi.org/10.1093/brain/awac335
7. Manasova D, Belloli LML, Rosenfelder MJ, et al. Multimodal multicentre investigation of diagnostic and prognostic markers in disorders of consciousness. *Brain*. 2026.
   - https://doi.org/10.1093/brain/awaf412
