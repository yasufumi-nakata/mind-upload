# Site Deepening Audit (2026-03-27, index multimodal bundle front-door stopline)

## 対象

- 主対象: `index.md`
- 派生同期: `summary_booklet.md`
- web確認対象:
  - `https://doi.org/10.1038/s41591-024-03019-1`
  - `https://doi.org/10.1093/brain/awac335`
  - `https://doi.org/10.1093/brain/awaf412`
  - `https://doi.org/10.1038/s41467-023-44363-z`
  - `https://doi.org/10.1038/s41467-025-64414-x`
  - `https://doi.org/10.1038/s41593-025-01945-y`
  - `https://doi.org/10.1038/s41593-025-02132-9`
- 調査範囲: 技術 / 自然科学のみ

## 今回この箇所を選んだ理由

- 深部ページではすでに
  - `Fusion Card`
  - `Human Proxy Composition Card`
  - `shared-vs-specific`
  - `common-driver / quantity-bridge`
  - `availability / complete-case / transfer`
  の停止線がかなり明確でした。
- しかし入口の `index.md` では、なお
  - `shared multimodal factor`
  までは止めていても、
  - `more modalities improved performance`
  - `tri-modal bundle`
  - `same-session multimodal`
  を
  - `robust same-subject cross-stack evidence`
  - `availability-agnostic bundle`
  - `transfer-stable state-identification`
  と誤読させない停止線が相対的に弱い状態でした。
- 入口でこの誤読を止めないと、詳細ページへ行く前に `multimodal = stronger truth` が再注入されます。

## 根拠付き批判

### 1. modality 数の増加は real gain ですが、それだけで robust bundle にはなりません

- [Rohaut et al. (2024)](https://doi.org/10.1038/s41591-024-03019-1) は、clinically unresponsive critical-care brain injury で multimodal assessment が neuroprognosis の不確実性を減らし、性能を改善しうることを示しました。

批判:

- この結果から直ちに言えるのは `bundle performance improved under the declared protocol` までです。
- ここから `bundle solved robustness / state-identification` へ飛ぶのは過大です。

### 2. direct same-sample multimodal comparison は complete-case subset に縮みえます

- [Amiri et al. (2023)](https://doi.org/10.1093/brain/awac335) は、same-sample multimodal comparison が `48 complete-feature patients` に依存しうることを示しました。
- つまり、paper に複数 modality が出てきても `every subject had the full bundle` を意味しません。

批判:

- `multimodal model improved` だけでは、gain が full cohort で得られたのか complete-case subset で得られたのかが分かりません。
- complete-case slice を出さない限り、general bundle claim は弱いです。

### 3. missing-modality policy と cross-centre transfer は fusion と別の故障点です

- [Manasova et al. (2026)](https://doi.org/10.1093/brain/awaf412) は second-level multimodal classifiers で `missing values are substituted with -1` を明示しました。
- 同論文は France で学習したモデルの generalization を Germany / Italy の available modalities で評価しています。

批判:

- したがって `same-session` や `multimodal` という語は、availability-agnostic も site-robust も保証しません。
- missing-modality handling と transfer window を出さない限り、bundle robustness は未評価です。

### 4. hard subgroup ほど disagreement が増えるなら headline gain だけでは足りません

- [Vafaii et al. (2024)](https://doi.org/10.1038/s41467-023-44363-z) は common と divergent structure の共存を示しました。
- [Chen et al. (2025)](https://doi.org/10.1038/s41467-025-64414-x) は simultaneous EEG-PET-MRI で coupled global progression と distinct network patterns の共存を示しました。
- [Bolt et al. (2025)](https://doi.org/10.1038/s41593-025-01945-y) は global fMRI mode の autonomic coupling を示しました。
- [Epp et al. (2025)](https://doi.org/10.1038/s41593-025-02132-9) は significant task BOLD の約 `40%` で oxygen-metabolism 変化が逆方向になりうることを示しました。
- [Manasova et al. (2026)](https://doi.org/10.1093/brain/awaf412) は minimally conscious / improving patients で inter-modality disagreement が高いことを示しました。

批判:

- 同時取得や bundle-level gain は、それだけで one latent state の solved evidence にはなりません。
- 特に hardest subgroup で disagreement が増えるなら、headline performance ではなく `where the bundle disagrees` まで出す必要があります。

## 今回実行した変更

- `index.md`
  - `page_highlights` に `multimodal gain ≠ robust bundle` の停止線を追加
  - `known_points` に complete-case / missing-modality / transfer regime の停止線を追加
  - front-door note-box `If A Multimodal Gain Sounds Like A Robust State-Identified Bundle` を追加
  - 新 note-box で
    - Rohaut 2024
    - Amiri 2023
    - Manasova 2026
    を使い、`bundle-performance evidence under a declared availability and transfer regime` という ceiling を入口で明示

- `summary_booklet.md`
  - `ruby scripts/build_summary_booklet.rb` による再生成対象として同期

## 今回止めた誤読

- `more modalities improved performance = robust bundle solved`
- `same-session tri-modal = same-subject cross-stack state identification`
- `paper lists several modalities = every subject had the full bundle`
- `shared factor exists = one latent neural state was identified`
- `multimodal gain = centre-robust / missing-modality-robust by default`

## 外部依存タスク

- なし
  - 今回の変更は repo 内の公開本文、派生 summary、監査記録の更新で完結しています。

## 参考文献

1. Rohaut B, Calligaris C, Hermann B, et al. Multimodal assessment improves neuroprognosis performance in clinically unresponsive critical-care patients with brain injury. *Nature Medicine*. 2024. https://doi.org/10.1038/s41591-024-03019-1
2. Amiri M, Andelic N, Westhall E, et al. Multimodal prediction of residual consciousness in the intensive care unit: the CONNECT-ME study. *Brain*. 2023. https://doi.org/10.1093/brain/awac335
3. Manasova D, Hermann B, Calligaris C, et al. Multimodal multicentre investigation of diagnostic and prognostic markers in disorders of consciousness. *Brain*. 2026. https://doi.org/10.1093/brain/awaf412
4. Vafaii H, Mandino F, Desrosiers-Grégoire G, et al. Multimodal measures of spontaneous brain activity reveal both common and divergent patterns of cortical functional organization. *Nature Communications*. 2024. https://doi.org/10.1038/s41467-023-44363-z
5. Chen JE, Lewis LD, Coursey SE, et al. Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep. *Nature Communications*. 2025. https://doi.org/10.1038/s41467-025-64414-x
6. Bolt TS, van den Brink RL, Song C, et al. Autonomic physiological coupling of the global fMRI signal. *Nature Neuroscience*. 2025. https://doi.org/10.1038/s41593-025-01945-y
7. Epp SM, Castrillón G, Yuan B, et al. BOLD signal changes can oppose oxygen metabolism across the human cortex. *Nature Neuroscience*. 2025. https://doi.org/10.1038/s41593-025-02132-9
