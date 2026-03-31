# Site Deepening Audit (2026-04-01, measurement-modeling DCM-axis sync)

## 対象

- 主対象: `wiki/measurement-and-modeling-terms.md`
- 同期対象:
  - `github-wiki-export/measurement-and-modeling-terms.md`
- 調査範囲: 技術 / 自然科学のみ

## web確認対象

- `https://mind-upload.com/wiki/measurement-and-modeling-terms.html`
- `https://mind-upload.com/wiki/observation-to-estimation.html`
- `https://doi.org/10.1016/j.neuroimage.2004.03.026`
- `https://doi.org/10.1016/j.jneumeth.2012.04.013`
- `https://pubmed.ncbi.nlm.nih.gov/26004501/`
- `https://doi.org/10.1016/j.neuroimage.2020.117491`
- `https://doi.org/10.1016/j.neuroimage.2024.120954`
- `https://doi.org/10.1016/j.neuroimage.2019.116435`
- `https://doi.org/10.1002/hbm.26751`
- `https://doi.org/10.1016/j.neuroimage.2024.120604`

## 今回この箇所を選んだ理由

- `wiki/measurement-and-modeling-terms.md` は、`observation -> organization -> estimation -> verification` の入口ページであり、初学者が `ESI / DCM / SCM` を最初に同じ視界で学ぶ場所です。
- そのため、ここでの圧縮は他ページより危険です。より厳密なページで止めている誤読でも、入口が粗いと再導入されます。
- 実際、同サイトのより深い技術ページ `wiki/observation-to-estimation.md` はすでに
  - candidate model space
  - latent-confound / node-definition / sampling
  - processing policy
  - reliability
  - abstention
  を分けておりました。
- しかし `wiki/measurement-and-modeling-terms.md` は 2026-04-01 時点でも、`DCM` を
  - candidate-model comparison
  - tractability / scaling
  - processing sensitivity
  - reliability window
  に分けてはおらず、読者が `whole-brain DCM` や `fast DCM` をそのまま `causal certainty` の増加として読める余地を残していました。

## 根拠付き批判

### 1. 旧 beginner page は DCM 進歩をまだ 1 本の bar として誤読させうる

- 旧文面は
  - `DCM through candidate-model disclosure and model recovery`
  - `tractability, not automatic identifiability`
  までは書けていました。
- しかし、それだけでは
  - model comparison の前進
  - scalable search の前進
  - preprocessing / first-level design robustness
  - session/sample-size-bound reliability
  が別軸であることが入口で固定されません。
- 一次文献はこの圧縮を支持しません。
  - [Penny et al. (2004)](https://doi.org/10.1016/j.neuroimage.2004.03.026) は、DCM inference が compared model set に依存することを示しました。
  - [Rosa et al. (2012)](https://doi.org/10.1016/j.jneumeth.2012.04.013) は、post-hoc model-space search を高速化しましたが、これは searchability の改善であり、omitted competitor の消滅ではありません。
  - [Frässle et al. (2021)](https://doi.org/10.1016/j.neuroimage.2020.117491) と [Wu et al. (2024)](https://doi.org/10.1016/j.neuroimage.2024.120954) は tractability / scaling を強めましたが、candidate-family dependence を消していません。

### 2. reliability は tractability とは別軸です

- [Frässle et al. (2016)](https://pubmed.ncbi.nlm.nih.gov/26004501/) は、software version と priors によって DCM parameter reliability が動くことを示しました。
- これは `faster` や `whole-brain` と同じ軸ではありません。
- よって `whole-brain estimates` を読んだだけで `robust DCM` や `stable causal graph` を連想させる入口文言は弱いです。

### 3. processing policy は housekeeping ではなく claim ceiling を動かします

- [Almgren et al. (2020)](https://doi.org/10.1016/j.neuroimage.2019.116435) は、resting-state fMRI で global signal regression が DCM estimates of noise and effective connectivity を動かすことを示しました。
- [Zhang et al. (2024)](https://doi.org/10.1002/hbm.26751) は、task-fMRI において GLM design、activation contrast、GSR、thresholding などの reasonable processing choices が effective-connectivity patterns と parameter certainty を materially alter しうることを示しました。

批判:

- したがって `processing` を beginner page で名前だけしか出さないと、読者は `reasonable preprocessing` を暗黙に固定済みだと誤読します。
- DCM では processing / first-level design policy 自体が route card の一部です。

### 4. reliability window は scan duration / sample size にも縛られます

- [Ma et al. (2024)](https://doi.org/10.1016/j.neuroimage.2024.120604) は、resting-state fMRI DCM の reliability が scan duration と sample size に依存することを示しました。

批判:

- よって `reliable DCM exists` を、時間窓や sample regime を超えて一般化できるように読むのは誤りです。
- beginner page に `reliability window` を独立軸として明示しないのは、現在の site-wide rule に対して弱すぎました。

## 今回実行した変更

### `wiki/measurement-and-modeling-terms.md`

- `last_updated` を `2026-04-01` に更新しました。
- front matter の `page_highlights` / `known_points` / `unknown_points` に、DCM を 1 本の progress bar として読まない rule を追加しました。
- 冒頭 note として `2026-04-01 correction to the beginner route` を追加し、
  - candidate-model comparison / family search
  - tractability / scaling
  - processing sensitivity
  - reliability window
  が別軸であることを一次文献付きで固定しました。
- `Read DCM by candidate-model rule, not causal wording` 節の直下に `DCM axis` table を追加し、
  - what it actually strengthens
  - what it still does not close
  を 4 軸で明示しました。
- `Where the full rule lives` note を追加し、詳細ルールを `wiki/observation-to-estimation.md#effective-connectivity-route-card` へ接続しました。
- references に
  - Almgren et al. (2020)
  - Zhang et al. (2024)
  - Ma et al. (2024)
  を追加しました。

### `github-wiki-export/measurement-and-modeling-terms.md`

- `ruby scripts/export_github_wiki.rb` により、同じ DCM-axis split を GitHub Wiki export 側へ同期しました。

## 今回止めた誤読

- `whole-brain DCM` = `causal certainty increased`
- `fast DCM` = `candidate-model dependence is mostly solved`
- `reliability paper exists` = `all sessions / sites / scan lengths are stable`
- `processing` は housekeeping であり、effective connectivity claim の ceiling には影響しない
- `DCM` の進歩は 1 本の monotonic ladder として読んでよい

## 検証

- `ruby scripts/export_github_wiki.rb`
  - 成功
- `GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT=1 ruby scripts/check_github_wiki_export.rb`
  - 成功
- `bundle exec jekyll build`
  - 成功
- `rg -n "2026-04-01 correction to the beginner route|DCM axis|Processing / first-level design robustness|Where the full rule lives" _site/wiki/measurement-and-modeling-terms.html`
  - 追加した公開文面が build 出力へ入っていることを確認

## external dependency tasks

- なし
  - 今回の主作業は、一次文献確認、repo 内公開文面の修正、export 同期、ローカル build 検証、commit / push で完結できます。

## 参考文献

1. Penny WD, Stephan KE, Mechelli A, Friston KJ. Comparing dynamic causal models. *NeuroImage*. 2004.
   - https://doi.org/10.1016/j.neuroimage.2004.03.026
2. Rosa MJ, Friston K, Penny W. Post-hoc selection of dynamic causal models. *J Neurosci Methods*. 2012.
   - https://doi.org/10.1016/j.jneumeth.2012.04.013
3. Frässle S, Paulus FM, Krach S, Jansen A. Test-retest reliability of effective connectivity in the face perception network. *Hum Brain Mapp*. 2016.
   - https://pubmed.ncbi.nlm.nih.gov/26004501/
4. Frässle S, Manjaly ZM, Do CT, Kasper L, Pruessmann KP, Stephan KE. Whole-brain estimates of directed connectivity for human connectomics. *NeuroImage*. 2021.
   - https://doi.org/10.1016/j.neuroimage.2020.117491
5. Wu H, Hu X, Zeng Y. A fast dynamic causal modeling regression method for fMRI. *NeuroImage*. 2024.
   - https://doi.org/10.1016/j.neuroimage.2024.120954
6. Almgren H, Van de Steen F, Razi A, Friston K, Marinazzo D. The effect of global signal regression on DCM estimates of noise and effective connectivity from resting state fMRI. *NeuroImage*. 2020.
   - https://doi.org/10.1016/j.neuroimage.2019.116435
7. Zhang S, Jung K, Langner R, Florin E, Eickhoff SB, Popovych OV. Impact of data processing varieties on DCM estimates of effective connectivity from task-fMRI. *Hum Brain Mapp*. 2024.
   - https://doi.org/10.1002/hbm.26751
8. Ma L, Braun SE, Steinberg JL, Bjork JM, Martin CE, Keen LD II, Moeller FG. Effect of scanning duration and sample size on reliability in resting state fMRI dynamic causal modeling analysis. *NeuroImage*. 2024.
   - https://doi.org/10.1016/j.neuroimage.2024.120604
