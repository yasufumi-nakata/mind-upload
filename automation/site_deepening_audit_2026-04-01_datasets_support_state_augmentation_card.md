# Site Deepening Audit (2026-04-01, datasets support-state augmentation card)

## 対象

- 主対象:
  - `datasets.md`
- 調査範囲:
  - 技術
  - 自然科学
- 明示的に除外した論点:
  - 哲学
  - 法学

## web確認対象

- `https://mind-upload.com/datasets.html`
- `https://mind-upload.com/verification.html#human-proxy-composition-card`
- `https://mind-upload.com/verification.html#fusion-card`
- `https://doi.org/10.1038/s41467-023-44363-z`
- `https://doi.org/10.1038/s41467-025-64414-x`
- `https://doi.org/10.1038/s41593-025-01945-y`
- `https://doi.org/10.1038/s41593-025-02132-9`
- `https://doi.org/10.1038/s41591-024-03019-1`
- `https://doi.org/10.1093/brain/awac335`
- `https://doi.org/10.1093/brain/awaf412`
- `https://doi.org/10.1186/s41747-024-00426-4`
- `https://doi.org/10.1016/j.neuroimage.2021.117864`

## 今回この箇所を選んだ理由

- `datasets.md` は公開サイト上の実務入口であり、読者が `どのデータから始めるか` と `どこまで読んでよいか` を最初に学ぶページでございます。
- 2026-03-31 時点の更新により、同ページにはすでに
  - maintenance-state family の分離
  - component-addition / ablation ladder
  - strongest-single-row versus full bundle
  が導入されておりました。
- しかしなお、`same-subject` かつ `same-session` の support-state rows が複数あると、それ自体がほぼ一つの aligned biological variable であるかのように読まれうる余地が残っておりました。
- この誤読は practical page として危険でございます。なぜなら、実際の multimodal 文献では
  - common structure
  - divergent structure
  - common driver
  - smaller complete-case subset
  - disagreement topology
  - row-local repeatability
  が分離されており、`co-acquired bundle = one solved variable` ではないためでございます。

## 主要結論

- 同一被験者・同一セッションの support-state bundle であっても、それだけで `one aligned biological variable` や `minimum required biological configuration` を読んではなりません。
- 公開 practical page には、family split の次段として、`support-state augmentation card` を固定する必要がございました。
- 安全な読解上限は
  - `family-split augmentation evidence`
  - `same-subject bundle gain under a named availability slice`
  - `bounded multimodal uncertainty reduction`
  のいずれかに留めるべきであり、bundle 追加だけで controller identity や U3 closure に進めるべきではございません。

## 根拠付き批判

### 1. `same-subject bundle` は `one biological quantity` を自動では与えません

- [Vafaii et al. (2024)](https://doi.org/10.1038/s41467-023-44363-z) は、spontaneous multimodal measures から cortical functional organization の `common` pattern と `divergent` pattern の両方が読めることを示しました。
- [Chen et al. (2025)](https://doi.org/10.1038/s41467-025-64414-x) は simultaneous EEG-PET-MRI により wakefulness から NREM への temporally coupled dynamics を示しつつ、hemodynamic と metabolic pattern が spatially distinct であることも示しました。

批判:

- 同時取得や同一被験者という条件だけでは、rows が
  - same quantity
  - same temporal object
  - same physiological regime
  を共有しているとは言えません。
- よって `datasets.md` でも、bundle の前に route class, effective window, quantity type を固定しなければ、読者は `same-subject = same latent variable` と誤読できます。

### 2. multimodal coupling には common driver と sign disagreement が入り得ます

- [Bolt et al. (2025)](https://doi.org/10.1038/s41593-025-01945-y) は、low-frequency global fMRI pattern が EEG と autonomic physiology に大きく coupling することを示しました。
- [Epp et al. (2025)](https://doi.org/10.1038/s41593-025-02132-9) は、有意な task BOLD changes を示す gray-matter voxels の約 40% で oxygen metabolism が反対方向に変化することを示しました。

批判:

- したがって、bundle 内の row 同士が関連して見えても、それが
  - direct quantity bridge
  - shared driver
  - opposite-sign coupled response
  のどれであるかは別途監査が必要でございます。
- 既存の `datasets.md` は family split までは強くても、bundle-level の common-driver audit と disagreement topology を practical field としてまだ固定しておりませんでした。

### 3. bundle gain は complete-case shrinkage と disagreement concentration を隠し得ます

- [Rohaut et al. (2024)](https://doi.org/10.1038/s41591-024-03019-1) は multimodal assessment が neuroprognosis を改善しうることを示しました。
- [Amiri et al. (2023)](https://doi.org/10.1093/brain/awac335) は multimodal residual-consciousness prediction で、direct same-sample comparison が EEG と fMRI の全 feature を備える 48 patients に縮むことを明示しました。
- [Manasova et al. (2026)](https://doi.org/10.1093/brain/awaf412) は performance 向上を示しつつ、minimally conscious or improving patients で inter-modality disagreement が高いことを報告しました。

批判:

- bundle の headline improvement だけでは、
  - smaller complete-case slice に依存していないか
  - disagreement が hardest regime に集中していないか
  - strongest single row を実際に上回っているか
  が分かりません。
- 実務入口のページでこの disclosure を欠くと、reader は `more modalities beat baseline` をそのまま `more biology was identified` と誤読できます。

### 4. row-local repeatability と transfer window は bundle claim と別問題でございます

- [Bøgh et al. (2024)](https://doi.org/10.1186/s41747-024-00426-4) は 3 T deuterium metabolic imaging に関する named repeatability window を示しました。
- [Wirsich et al. (2021)](https://doi.org/10.1016/j.neuroimage.2021.117864) は EEG-fMRI connectome relation の reproducibility を示しつつ、それが harmonized simultaneous acquisition に依存することも示しました。

批判:

- 同じ support-state family に属する row でも、repeatability, hardware dependence, centre transferability は個別に監査しなければなりません。
- そのため practical page でも、bundle claim の前に `row-local repeatability and transfer window` を card field として持つ必要がございました。

## 今回実行した変更

### `datasets.md`

- `last_updated` を `2026-04-01` に更新しました。
- front matter の `page_highlights` に、same-subject support-state bundle を自己解釈させないための必須 field 群を追加しました。
- `known_points` に、family-split augmentation を強く読む前に augmentation card が必要であることを追加しました。
- `Starter EEG datasets are still only the baseline arm of this ladder` の直後に、新しい note-box `A same-subject support-state bundle still needs its own augmentation card` を追加しました。
- 新しい section `A practical support-state augmentation card for dataset bundles` を追加し、以下を table で固定しました。
  - route class and bridge type
  - effective time window and physiological regime
  - direct observable and quantity type
  - shared-driver / quantity-bridge audit
  - availability slice and missing-modality policy
  - strongest single row and disagreement topology
  - row-local repeatability and transfer window
  - abstention and stopping claim
- 同 section に `What this card changes in practice` note-box を追加し、
  - neuron-first baseline
  - strongest single added row
  - full bundle
  を同一 split / availability slice / abstention rule で比較しない限り、support-state addition を `family-split augmentation evidence` に留めるルールを明記しました。
- 参考文献リストに今回の multimodal bundle critique を支える primary papers を追加しました。

## 今回止めた誤読

- `same subject` だから rows は同じ biological variable を測っている
- `same session` だから physiological regime は自動で一致している
- `bundle beats baseline` だから minimum biological configuration が見えた
- `correlated rows` だから direct quantity bridge が確立した
- `multimodal improvement` だから hardest regime の disagreement は無視できる
- `one successful setup` だから row はそのまま cross-centre に移る

## 検証

- `bundle exec jekyll build`
  - 成功
- `git diff --check`
  - 成功
- `rg -n "A same-subject support-state bundle still needs its own augmentation card|A practical support-state augmentation card for dataset bundles|Route class and bridge type|What this card changes in practice" _site/datasets.html`
  - 追加文面が build 後 HTML に反映されていることを確認

## external dependency tasks

- なし
  - 今回の主作業は web 上の一次資料確認、repo 内 public page 修正、ローカル build 検証、監査メモ追加、commit、push までこのセッションで完結可能でございます。

## 参考文献

1. Vafaii P, White TP, Jones E, et al. Multimodal measures of spontaneous brain activity reveal both common and divergent patterns of cortical functional organization. *Nature Communications*. 2024;15:517. https://doi.org/10.1038/s41467-023-44363-z
2. Chen JE, Lewis LD, Coursey SE, et al. Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep. *Nature Communications*. 2025. https://doi.org/10.1038/s41467-025-64414-x
3. Bolt TS, van den Brink RL, Song C, et al. Autonomic physiological coupling of the global fMRI signal. *Nature Neuroscience*. 2025. https://doi.org/10.1038/s41593-025-01945-y
4. Epp SM, Castrillon G, Yuan B, et al. BOLD signal changes can oppose oxygen metabolism across the human cortex. *Nature Neuroscience*. 2025. https://doi.org/10.1038/s41593-025-02132-9
5. Rohaut B, Boileau M, Raimondo F, et al. Multimodal assessment improves neuroprognosis performance in clinically unresponsive critical-care patients with brain injury. *Nature Medicine*. 2024;30:2049-2058. https://doi.org/10.1038/s41591-024-03019-1
6. Amiri M, Monti MM, Rieger SW, et al. Multimodal prediction of residual consciousness in the intensive care unit: the CONNECT-ME study. *Brain*. 2023;146(1):321-336. https://doi.org/10.1093/brain/awac335
7. Manasova D, Bareham C, Kondziella D, et al. Multimodal multicentre investigation of diagnostic and prognostic markers in disorders of consciousness. *Brain*. 2026. https://doi.org/10.1093/brain/awaf412
8. Bøgh N, Mørup M, Laustsen C, et al. Repeatability of deuterium metabolic imaging of healthy volunteers at 3 T. *European Radiology Experimental*. 2024;8:81. https://doi.org/10.1186/s41747-024-00426-4
9. Wirsich J, Jorge J, Iannotti GR, et al. The relationship between EEG and fMRI connectomes is reproducible across simultaneous EEG-fMRI studies from 1.5 T to 7T. *NeuroImage*. 2021;231:117864. https://doi.org/10.1016/j.neuroimage.2021.117864
