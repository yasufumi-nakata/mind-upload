# Site Deepening Audit (2026-03-26, multimodal bundle robustness / availability / transfer)

## 対象

- 主対象: `wiki/multimodal-integration-basics.md`
- 同期対象: `verification.md`
- エクスポート同期: `github-wiki-export/multimodal-integration-basics.md`
- web確認対象:
  - `https://doi.org/10.1038/s41591-024-03019-1`
  - `https://doi.org/10.1093/brain/awac335`
  - `https://doi.org/10.1093/brain/awaf412`
  - `https://doi.org/10.1038/s41467-023-44363-z`
  - `https://doi.org/10.1038/s41467-025-64414-x`
  - `https://doi.org/10.1038/s41593-025-01945-y`
- 調査範囲: 技術 / 自然科学のみ

## 今回この箇所を選んだ理由

- `wiki/multimodal-integration-basics.md` は 2026-03-21 時点で、
  - `Fusion Card`
  - `shared-vs-specific`
  - `vascular-state / CVR`
  の停止線まではかなり明確でした。
- しかしなお、
  - `more modalities improved performance`
  - `same-session tri-modal`
  - `multimodal bundle`
  を、
  - `availability-agnostic`
  - `complete-case independent`
  - `cross-centre robust`
  - `hard-regime agreement`
  のように読み替える停止線が弱い状態でした。
- これは自然科学的に弱いです。一次文献が示しているのは、multimodal gain、自動的な bundle robustness、same-state inference が別問題だということだからです。

## 根拠付き批判

### 1. modality 数の増加は real gain ですが、それだけで stable bundle にはなりません

- [Rohaut et al. (2024)](https://doi.org/10.1038/s41591-024-03019-1) は acute brain injury で modality 数の増加が予後不確実性を下げ、予後精度を改善しうることを示しました。
- しかしこの事実から直ちに言えるのは `bundle performance can improve under the declared protocol` までです。

批判:

- `more modalities helped` を `bundle solved` に読み替えるのは過大です。
- 利得がどの availability regime で得られたか、どの subset で比較されたか、どこまで site 固有条件に依存したかを別に出さないと、multimodal gain は過読されます。

### 2. same-sample multimodal comparison は complete-case subset に縮むことがあります

- [Amiri et al. (2023)](https://doi.org/10.1093/brain/awac335) では、same-sample multimodal comparison が `n = 48` の complete-feature subset に依存していました。
- 同論文は、EEG features を組み合わせた same-sample model の改善が `markedly decreased sample size` と並んで報告されることも明示しています。

批判:

- したがって、multimodal paper に複数 modality が登場しても、それだけで `each patient had the full bundle` を意味しません。
- direct bundle comparison が complete-case subset に依存するなら、その slice を出さない限り general bundle claim は弱いです。

### 3. missing-modality handling と cross-centre transfer は fusion と別の故障点です

- [Manasova et al. (2026)](https://doi.org/10.1093/brain/awaf412) は second-level multimodal classifiers で `missing values are substituted with -1` を明示しました。
- 同論文は France で学習した unimodal models の generalization を Germany / Italy の independent datasets で評価し、一部 modality は chance を上回らない transfer を示しました。

批判:

- したがって `same protocol で multimodal model が動いた` を `site robust` に読み替えるのは不適切です。
- missing-modality policy と cross-centre window が不明なままでは、Fusion Card は acquisition transparency にはなっても bundle robustness disclosure にはなりません。

### 4. hard subgroup ほど inter-modality disagreement が増えうります

- [Vafaii et al. (2024)](https://doi.org/10.1038/s41467-023-44363-z) は multimodal recordings に common と divergent structure の両方が残ることを示しました。
- [Chen et al. (2025)](https://doi.org/10.1038/s41467-025-64414-x) は simultaneous EEG-PET-MRI で coupled global progression と distinct network patterns の共存を示しました。
- [Bolt et al. (2025)](https://doi.org/10.1038/s41593-025-01945-y) は global fMRI mode が autonomic physiology と substantial coupling を持つことを示しました。
- [Manasova et al. (2026)](https://doi.org/10.1093/brain/awaf412) は minimally conscious / improving patients で pairwise disagreement が高いことを示しました。

批判:

- したがって multimodal agreement は一様ではありません。
- 特に hardest subgroup で disagreement が増えるなら、bundle headline だけでは十分ではなく、`where the bundle disagrees` を出さない限り過読を止められません。

## 今回実行した変更

- `wiki/multimodal-integration-basics.md`
  - `last_updated` を `2026-03-26` に更新
  - front matter の `description`, `page_intro`, `page_highlights`, `known_points`, `unknown_points`, `wiki_links` を更新
  - `More modalities do not make the bundle availability-agnostic` note を追加
  - `Fusion Card does not replace the Human Proxy Composition Card` note を追加
  - audit gates を `8` から `9` に拡張し、`Bundle robustness gate` を追加
  - minimum fusion package に
    - availability / complete-case slice
    - missing-modality policy
    - cross-centre / cross-scanner transfer window
    を追加
  - tri-modal route の制約欄に bundle robustness disclosure を追加
  - `More modalities can help without making the bundle stable by default` 節を追加
  - reading rules に
    - multimodal gain
    - Human Proxy Composition Card の併用条件
    を追加
  - 参考文献に Rohaut 2024, Amiri 2023, Manasova 2026 を追加

- `verification.md`
  - Fusion Card addendum に availability / complete-case / transfer / disagreement の停止線を追加
  - Fusion Card table に
    - `Availability / complete-case slice`
    - `Transfer / disagreement window`
    を追加
  - minimum operating rule を更新し、narrow subset や unresolved imputation の場合は `bounded bundle-performance evidence` に止める rule を追加
  - `Additional audit logs` の Fusion Card 行に新しい disclosure fields を追加

- `github-wiki-export/multimodal-integration-basics.md`
  - export script で再生成して同期

## 今回止めた誤読

- `more modalities improved accuracy = bundle solved`
- `same-session tri-modal = availability-agnostic fused evidence`
- `modalities listed in one paper = every subject had the full bundle`
- `within-centre multimodal gain = cross-centre robust bundle`
- `bundle headline = agreement in the hardest subgroup`
- `Fusion Card = Human Proxy Composition Card の代替`

## 外部依存タスク

- なし
  - 今回の変更は repo 内の本文、監査メモ、export 同期、検証で完結します。

## 参考文献

1. Rohaut B, Calligaris C, Hermann B, et al. Multimodal assessment improves neuroprognosis performance in clinically unresponsive critical-care patients with brain injury. *Nature Medicine*. 2024. https://doi.org/10.1038/s41591-024-03019-1
2. Amiri M, Andelic N, Westhall E, et al. Multimodal prediction of residual consciousness in the intensive care unit: the CONNECT-ME study. *Brain*. 2023. https://doi.org/10.1093/brain/awac335
3. Manasova D, Hermann B, Calligaris C, et al. Multimodal multicentre investigation of diagnostic and prognostic markers in disorders of consciousness. *Brain*. 2026. https://doi.org/10.1093/brain/awaf412
4. Vafaii H, Mandino F, Desrosiers-Grégoire G, et al. Multimodal measures of spontaneous brain activity reveal both common and divergent patterns of cortical functional organization. *Nature Communications*. 2024. https://doi.org/10.1038/s41467-023-44363-z
5. Chen JE, Lewis LD, Coursey SE, et al. Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep. *Nature Communications*. 2025. https://doi.org/10.1038/s41467-025-64414-x
6. Bolt TS, van den Brink RL, Song C, et al. Autonomic physiological coupling of the global fMRI signal. *Nature Neuroscience*. 2025. https://doi.org/10.1038/s41593-025-01945-y
