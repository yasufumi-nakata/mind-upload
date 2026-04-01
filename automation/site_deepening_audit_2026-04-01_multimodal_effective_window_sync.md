# Site Deepening Audit (2026-04-01, multimodal effective-window sync)

## 対象

- 主対象:
  - `wiki/multimodal-integration-basics.md`
  - `verification.md`
- 同期対象:
  - `github-wiki-export/multimodal-integration-basics.md`
- 調査範囲:
  - 技術
  - 自然科学
- 明示的に除外した論点:
  - 哲学
  - 法学

## web確認対象

- `https://mind-upload.com/wiki/multimodal-integration-basics.html`
- `https://mind-upload.com/verification.html#fusion-card`
- `https://doi.org/10.1155/2016/4182483`
- `https://doi.org/10.1016/j.neuroimage.2021.118131`
- `https://doi.org/10.1038/s41467-025-64414-x`
- `https://doi.org/10.1038/s41593-025-01945-y`
- `https://doi.org/10.1038/s41593-025-02132-9`

## 今回この箇所を選んだ理由

- `wiki/multimodal-integration-basics.md` と `verification.md#fusion-card` は、同サイトの `same-session` / `multimodal` / `tri-modal` 読解規則を決める入口でございます。
- 既存ページはすでに
  - shared-vs-specific
  - quantity bridge / physiology grounding
  - bundle robustness
  を分けておりました。
- しかし 2026-04-01 時点でも、`same-session` が
  - same clock
  - same temporal object
  - same state sample
  を区別せずに読まれうる余地が残っておりました。
- とくに Fusion Card には
  - acquisition relation
  - lag audit
  はあっても、
  - `effective-window / temporal-kernel relation`
  が提出項目として固定されていませんでした。

## 主要結論

- 同時取得は、`same timestamps` を強めても、`same effective window` や `same state object` を自動では与えません。
- よって、このサイトでは multimodal / atlas-prior claim に対しても、Fusion Card に
  - `effective-window / temporal-kernel relation`
  を明示的に追加する必要がございました。
- 安全な読解上限は
  - `synchronized cross-stack evidence`
  - `shared transition evidence`
  - `coordinated multi-timescale dynamics`
  のいずれかに留めるべきであり、同時取得だけで `one synchronous latent-state sample` に昇格させるべきではございません。

## 根拠付き批判

### 1. EEG-fMRI は同時取得でも temporal mismatch を自動解消しません

- [Nguyen et al. (2016)](https://doi.org/10.1155/2016/4182483) は、spatiotemporally constrained EEG-fMRI source imaging を提案しつつ、`temporal mismatch between EEG and fMRI still persists` と明示しました。

批判:

- したがって `simultaneous EEG-fMRI` をそのまま `same temporal object` と読むのは不正確でございます。
- `lag audit` だけでは足りず、各 modality がどの temporal kernel を持つかを別項目で固定する必要がございます。

### 2. simultaneous PET/fMRI でも PET 側は scan-window average として読まれます

- [Ripp et al. (2021)](https://doi.org/10.1016/j.neuroimage.2021.118131) は simultaneous FDG-PET/fMRI working-memory study で、FDG-PET を `steady-state during the recording interval` を前提とする proxy とし、baseline を `44-60 min post-injection`、task を `63-71 min post-injection` の sum image として比較しました。

批判:

- これは `same-session` であっても PET が event-scale timing を直接担っていないことを示します。
- よって `EEG + PET + MRI` の tri-modal claim を、秒スケール EEG と同一 temporal object の読出しとして扱うのは過大読解でございます。

### 3. tri-modal EEG-PET-MRI は multi-timescale coordination であって instantaneous state meter ではありません

- [Chen et al. (2025)](https://doi.org/10.1038/s41467-025-64414-x) は simultaneous EEG-PET-MRI で wakefulness から NREM にわたる temporally coupled hemodynamic / metabolic progression と distinct network patterns を示しました。

批判:

- これは重要な前進ですが、強化しているのは
  - shared acquisition window
  - coordinated progression across stacks
  - structured multimodal comparison
  であって、
  - one matched instantaneous latent-state sample
  の自動確立ではございません。
- サイト入口でこの stop line を明示しないと、tri-modal という語だけで state identification へ滑ります。

### 4. 共通因子が見えても、なお target variable と temporal object は未確定です

- [Bolt et al. (2025)](https://doi.org/10.1038/s41593-025-01945-y) は global fMRI signal が EEG と多数の autonomic signals に low-frequency range で coupling することを示しました。
- [Epp et al. (2025)](https://doi.org/10.1038/s41593-025-02132-9) は、task BOLD change が oxygen metabolism と反対方向に動く cortical voxels があることを示しました。

批判:

- したがって
  - same-session
  - shared factor
  - coupled trajectory
  のどれも、それ単体では `same biological quantity on the same temporal object` を意味しません。
- Fusion Card で時間窓 / kernel を固定しないまま quantity bridge だけを書くと、reader は temporal mismatch を見落としたまま `one solved variable` と誤読できます。

## 今回実行した変更

### `wiki/multimodal-integration-basics.md`

- `last_updated` を `2026-04-01` に更新しました。
- front matter の `page_highlights` / `known_points` / `unknown_points` に、`same-session ≠ same effective window` の規則を追加しました。
- `Same session is not yet the same effective window` note-box を追加しました。
- audit gates を `10` から `11` に更新し、`Effective-window / temporal-kernel gate` を追加しました。
- `Minimum fusion package` に `effective-window / temporal-kernel relation` を追加しました。
- route table の
  - `Simultaneous measurement EEG + fMRI`
  - `Simultaneous EEG + PET + MRI`
  に temporal-kernel disclosure を明示しました。
- `What each route actually adds` の EEG+fMRI / EEG+PET+MRI 節に、multi-timescale 読解の補正を追加しました。
- `Reading rules adopted on this site` の `same-session / atlas-informed` と `EEG + PET + MRI` rule を更新しました。
- references に
  - Nguyen et al. (2016)
  - Ripp et al. (2021)
  を追加しました。

### `verification.md`

- front matter の `page_highlights` に、Fusion Card が `effective-window / temporal-kernel relation` を含むことを明記しました。
- `Fusion Card` の addendum 本文に
  - EEG-fMRI temporal mismatch
  - PET scan-window average
  を示す一次文献を追加しました。
- Fusion Card table に `Effective-window / temporal-kernel relation` row を追加しました。
- `Same session is not yet the same temporal object` note-box を追加しました。
- `Minimum operating rule` に、同項目が欠落した場合は `synchronized multi-timescale evidence` に留める旨を追加しました。
- 末尾の `Fusion Card` 提出要件リストにも同項目を反映しました。
- references に
  - Nguyen et al. (2016)
  - Ripp et al. (2021)
  を追加しました。

### `github-wiki-export/multimodal-integration-basics.md`

- `ruby scripts/export_github_wiki.rb` により、GitHub Wiki export 側にも同じ effective-window rule を同期しました。

## 今回止めた誤読

- `same-session multimodal acquisition = one synchronous latent-state sample`
- `tri-modal EEG-PET-MRI = fused ground truth`
- `shared timestamp = same temporal object`
- `shared factor = same biological quantity`
- `PET task result = event-scale metabolic timing`
- `EEG-fMRI synchrony = event-scale neural state already matched to the BOLD object`

## 検証

- `ruby scripts/export_github_wiki.rb`
  - 成功
- `GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT=1 ruby scripts/check_github_wiki_export.rb`
  - 成功
- `bundle exec jekyll build`
  - 成功
- `git diff --check`
  - 成功
- `rg -n "Same session is not yet the same effective window|Effective-window / temporal-kernel gate|coordinated multi-timescale evidence|effective-window / temporal-kernel relation" _site/wiki/multimodal-integration-basics.html _site/verification.html github-wiki-export/multimodal-integration-basics.md`
  - 追加した公開文面と export 同期を確認

## external dependency tasks

- なし
  - 今回の主作業は一次文献確認、repo 内公開文面修正、wiki export 同期、ローカル build 検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Nguyen T, Potter T, Nguyen T, Karmonik C, Grossman R, Zhang Y. EEG Source Imaging Guided by Spatiotemporal Specific fMRI: Toward an Understanding of Dynamic Cognitive Processes. *Neural Plasticity*. 2016.
   - https://doi.org/10.1155/2016/4182483
2. Ripp I, Wallenwein LA, Wu Q, Emch M, Koch K, Cumming P, Yakushev I. Working memory task induced neural activation: A simultaneous PET/fMRI study. *NeuroImage*. 2021.
   - https://doi.org/10.1016/j.neuroimage.2021.118131
3. Chen JE, Lewis LD, Coursey SE, Catana C, Polimeni JR, Fan J, Droppa KS, Patel R, Wey H-Y, Chang C, Manoach DS, Price JC, Sander CY, Rosen BR. Simultaneous EEG-PET-MRI identifies temporally coupled and spatially structured brain dynamics across wakefulness and NREM sleep. *Nature Communications*. 2025.
   - https://doi.org/10.1038/s41467-025-64414-x
4. Bolt TS, van den Brink RL, Song C, et al. Autonomic physiological coupling of the global fMRI signal. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-01945-y
5. Epp SM, Castrillon G, Yuan B, Andrews-Hanna J, Preibisch C, Riedl V. BOLD signal changes can oppose oxygen metabolism across the human cortex. *Nature Neuroscience*. 2025.
   - https://doi.org/10.1038/s41593-025-02132-9
