# Site Deepening Audit (2026-04-01, wearable OPM-MEG route sync)

## 対象

- 主対象:
  - `eeg_101.md`
  - `wiki/eeg-basics.md`
  - `wiki/measurement-stack-and-claim-ceiling.md`
  - `mind_uploading_papers.md`
  - `research_harvest_50.md`
- 同期対象:
  - `github-wiki-export/eeg-basics.md`
  - `github-wiki-export/measurement-stack-and-claim-ceiling.md`
- 調査範囲:
  - 技術
  - 自然科学
- 明示的に除外した論点:
  - 哲学
  - 法学

## web確認対象

- `https://doi.org/10.1038/nature26147`
- `https://doi.org/10.1016/j.neuroimage.2021.118401`
- `https://doi.org/10.1109/TBME.2021.3100770`
- `https://doi.org/10.1109/TBME.2024.3465654`
- `https://doi.org/10.1162/IMAG.a.8`
- `https://doi.org/10.1063/5.0273491`
- `https://doi.org/10.3390/s25134160`
- `https://doi.org/10.1016/j.neuroimage.2021.118604`
- `https://pmc.ncbi.nlm.nih.gov/articles/PMC12319812/`
- `https://pmc.ncbi.nlm.nih.gov/articles/PMC12252452/`

## 今回この箇所を選んだ理由

- site 内の深い説明では、すでに
  - `wiki/multimodal-integration-basics.md`
  - `tech_roadmap.md`
  で `wearable OPM-MEG` を
  - shielding
  - field control
  - calibration / co-registration
  - anatomy route
  の burden 付きで止めておりました。
- しかし入口・front door 側では、
  - `eeg_101.md`
  - `wiki/eeg-basics.md`
  - `mind_uploading_papers.md`
  - `research_harvest_50.md`
  がまだ十分には同期しておらず、`wearable MEG` を
  - `promising`
  - `movement during recording`
  程度の粗い単位で再導入しうる状態でした。
- これは site-wide rule に対して危険でございます。深いページで厳密に止めた誤読が、入口ページの粗さで再流入するためでございます。

## 主要結論

- `wearable OPM-MEG` は 1 本の進歩 bar ではなく、少なくとも次の 6 軸で分けて読む必要がございました。
  - `shielding class`
  - `field nulling / interference suppression`
  - `sensor calibration / co-registration`
  - `anatomy route`
  - `array crosstalk burden`
  - `task / sample regime`
- したがって safe ceiling は
  - `movement-tolerant macro electrophysiology under disclosed shielding, field control, calibration / coregistration, anatomy route, crosstalk, and task regime`
  に留めるのが妥当でございます。
- `portable naturalistic brain readout`
  - `ordinary-room MEG`
  - `MRI-free source truth`
  - `state-complete observation`
  への昇格は、現行一次文献では支持されません。

## 根拠付き批判

### 1. movement tolerance は field environment burden を消しません

- [Boto et al. (2018)](https://doi.org/10.1038/nature26147) は wearable feasibility を示しましたが、background-field control なしでは head movement により sensor saturation risk が実際に残ることも同時に示しました。
- [Rea et al. (2021)](https://doi.org/10.1016/j.neuroimage.2021.118401) と [Mellor et al. (2022)](https://doi.org/10.1109/TBME.2021.3100770) は precision magnetic-field modelling / correction 自体が route burden であることを示しました。

批判:

- よって `wearable` を `portable enough that environment no longer matters` と読むのは誤りでございます。
- 実際には `movement becomes measurable only after the magnetic environment is engineered tightly enough` と読むべきでございます。

### 2. lighter shielding は ordinary-room portability の別名ではありません

- [Holmes et al. (2025)](https://doi.org/10.1109/TBME.2024.3465654) は lightly shielded environment を示しましたが、それは active compensation と `tSSS` を前提にしております。

批判:

- したがって `lightly shielded` は `shield-free` ではございません。
- `wearable OPM-MEG` を ordinary-room deployability の近似として front door で語るのは、engineering burden を落としすぎでございます。

### 3. anatomy route はまだ消えておりません

- [Rhodes et al. (2025)](https://doi.org/10.1162/IMAG.a.8) は pseudo-MRI route の有用性を示しましたが、individual MRI を gold standard として残しております。

批判:

- したがって `MRI-free OPM source reconstruction` を generic source-truth route と読むのは不適切でございます。
- これは `anatomy-light substitute under stated conditions` であり、`anatomy burden solved` ではございません。

### 4. array engineering も独立 burden です

- [Wu et al. (2025)](https://doi.org/10.1063/5.0273491) は OPM arrays の crosstalk reduction を独立 engineering problem として示しました。

批判:

- よって `wearable MEG works` を `array-level interference no longer materially shapes the claim` と読むことはできません。
- `crosstalk` は site 側でも独立 audit 項目として visible にすべきでございました。

### 5. 最新の whole-body proof でも narrow task / small sample ceiling が残ります

- [Spedden et al. (2025)](https://doi.org/10.3390/s25134160) は human stepping 中の wearable MEG feasibility を示しましたが、healthy adults `3` 名での narrow sensorimotor beta paradigm でございます。

批判:

- したがって `whole-body movement shown` を `broad naturalistic coverage solved` と読むのは過剰でございます。
- task regime と sample regime は still part of the claim であり、front door で省略すべきではございません。

## 今回実行した変更

### `eeg_101.md`

- `last_updated` を `2026-04-01` に更新しました。
- front matter の `page_highlights` / `known_points` / `unknown_points` に OPM-MEG route burden を追加しました。
- multimodal section の `OPM-MEG` bullet を、単なる promising language から route-conditioned reading へ更新しました。
- `2026-04-01 addendum: wearable OPM-MEG is not one portable route` note-box を追加しました。
- references に
  - Rea et al. (2021)
  - Mellor et al. (2022)
  - Holmes et al. (2025)
  - Rhodes et al. (2025)
  - Wu et al. (2025)
  - Spedden et al. (2025)
  を追加しました。

### `wiki/eeg-basics.md`

- `last_updated` を `2026-04-01` に更新しました。
- front matter の `page_highlights` / `known_points` / `unknown_points` に OPM-MEG route burden を追加しました。
- beginner route に `2026-04-01 correction: wearable OPM-MEG is not a portable free pass` note-box を追加しました。
- references を追加しました。

### `wiki/measurement-stack-and-claim-ceiling.md`

- front matter の `page_highlights` / `known_points` に、OPM-MEG が EEG / MEG ceiling の外へ出ないことを追加しました。
- measurement-stack table の `EEG / MEG` row に、movement-tolerant MEG も field-control 条件付きであることを追記しました。
- `2026-04-01 addendum: wearable OPM-MEG is still inside the EEG / MEG ceiling` note-box を追加しました。
- `Operating rule for EEG / MEG` に OPM disclosure bundle を追記しました。
- references を追加しました。

### `mind_uploading_papers.md`

- front matter の `known_points` / `page_highlights` に OPM-MEG route-conditioned reading を追加しました。
- note を `tractography and wearable OPM-MEG route splits` に更新しました。
- technical fast-lane table に `Wearable OPM-MEG / movement-tolerant macro electrophysiology` row を追加しました。

### `research_harvest_50.md`

- front matter の `page_highlights` / `known_points` に OPM-MEG route-conditioned reading を追加しました。
- priority-route table の U1/U7 row に `wearable OPM-MEG` の first-pass check を追加しました。
- `Read wearable OPM-MEG as a field-control route, not as portable naturalistic readout` note-box を追加しました。

### `github-wiki-export/*`

- `ruby scripts/export_github_wiki.rb` により、`wiki/eeg-basics.md` と `wiki/measurement-stack-and-claim-ceiling.md` の変更を export 側へ同期しました。

## 今回止めた誤読

- `wearable OPM-MEG` = `portable naturalistic readout`
- `lightly shielded` = `ordinary-room`
- `pseudo-MRI works` = `anatomy route is solved`
- `movement proof-of-concept exists` = `broad everyday source reconstruction is close`
- `wearable MEG` = `a separate modality ceiling above EEG/MEG`

## 検証

- `ruby scripts/export_github_wiki.rb`
  - 成功
- `GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT=1 ruby scripts/check_github_wiki_export.rb`
  - 成功
- `bundle exec jekyll build`
  - 成功
- `git diff --check`
  - 成功
- `rg -n "wearable OPM-MEG is not one portable route|wearable OPM-MEG is not a portable free pass|wearable OPM-MEG is still inside the EEG / MEG ceiling|movement-tolerant macro electrophysiology" _site/eeg_101.html _site/wiki/eeg-basics.html _site/wiki/measurement-stack-and-claim-ceiling.html github-wiki-export/eeg-basics.md github-wiki-export/measurement-stack-and-claim-ceiling.md`
  - 追加文面が build 出力と export 出力に反映されていることを確認

## external dependency tasks

- なし
  - 今回の主作業は、一次文献確認、公開文面の改稿、wiki export 同期、build 検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Boto E, Holmes N, Leggett J, et al. Moving magnetoencephalography towards real-world applications with a wearable system. *Nature*. 2018. https://doi.org/10.1038/nature26147
2. Rea M, Holmes N, Hill RM, et al. Precision magnetic field modelling and control for wearable magnetoencephalography. *NeuroImage*. 2021. https://doi.org/10.1016/j.neuroimage.2021.118401
3. Mellor SJ, Tierney TM, O'Neill GC, et al. Magnetic field mapping and correction for moving OP-MEG. *IEEE Transactions on Biomedical Engineering*. 2022. https://doi.org/10.1109/TBME.2021.3100770
4. Holmes N, Leggett J, Hill RM, et al. Wearable magnetoencephalography in a lightly shielded environment. *IEEE Transactions on Biomedical Engineering*. 2025. https://doi.org/10.1109/TBME.2024.3465654
5. Rhodes N, Rier L, Boto E, Hill RM, Brookes MJ. Source reconstruction without an MRI using optically pumped magnetometer-based magnetoencephalography. *Imaging Neuroscience*. 2025. https://doi.org/10.1162/IMAG.a.8
6. Wu T, Xiao W, Peng X, Wu T, Guo H. Crosstalk reduction in optically pumped magnetometers arrays for biomagnetic measurement. *Review of Scientific Instruments*. 2025. https://doi.org/10.1063/5.0273491
7. Spedden ME, O'Neill GC, West TO, et al. Using wearable MEG to study the neural control of human stepping. *Sensors*. 2025. https://doi.org/10.3390/s25134160
