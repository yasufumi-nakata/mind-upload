# Site Deepening Audit (2026-04-03, front-door BCSFB quantity split)

## 対象

- 主対象:
  - `index.md`
  - `faq.md`
  - `tech_roadmap.md`
  - `perspective.md`
  - `summary_booklet.md`
- 調査範囲: 技術 / 自然科学のみ
- 明示的に除外した論点: 哲学、法学、制度論

## 今回この箇所を選んだ理由

- 2026-04-03 時点の site は、深いページ側ではすでに `BBB water exchange` と `tracer-specific BBB transport` の区別をかなり前面化できておりました。
- しかし front door 側では、`blood-CSF barrier / choroid plexus` に関する human in vivo evidence がまだ圧縮気味で、読者が
  - `barrier-side human MRI exists`
  - `therefore maintenance-state observability is basically solved`
  - `BCSFB is close enough to BBB or clearance`
  と読める余地が残っておりました。
- これは科学的に危険でございます。human barrier-side evidence は少なくとも
  - choroid-plexus perfusion
  - blood-to-CSF water transport
  - choroid-plexus water cycling
  - apparent BCSFB water exchange
  - simultaneous BBB-vs-BCSFB ASL exchange modeling
  に分けて読まなければ、direct observable と inferential ceiling が混線いたします。

## 主要結論

- `human BCSFB evidence` は一つの可観測量ではございません。
- [Zhao et al. (2020)](https://pubmed.ncbi.nlm.nih.gov/32962708/) と [Sun et al. (2024)](https://doi.org/10.1186/s12987-024-00603-y) は主として `choroid-plexus perfusion` の route でございます。
- [Petitclerc et al. (2021)](https://pubmed.ncbi.nlm.nih.gov/34826596/) は `blood-to-CSF water transport` の route であり、generic BBB scalar ではございません。
- [Anderson et al. (2022)](https://pubmed.ncbi.nlm.nih.gov/34542012/) は `in vivo water cycling at the human choroid plexus` の route であり、whole-brain clearance truth ではございません。
- [Wu et al. (2026)](https://pubmed.ncbi.nlm.nih.gov/40832972/) は `apparent BCSFB water exchange` の route であり、validated maintenance-state ground truth ではございません。
- [Petitclerc et al. (2026)](https://journals.sagepub.com/doi/10.1177/0271678X261429042) は `BBB` と `BCSFB` を同じ measurement row に潰さず、むしろ同時推定して区別する必要があることを示しております。

## 根拠付き批判

### 1. `BCSFB/choroid plexus` を `BBB` の一部として要約すると測定対象が変わってしまいます

- [Petitclerc et al. (2026)](https://journals.sagepub.com/doi/10.1177/0271678X261429042) は、題名の時点で `blood-brain barrier` と `blood-CSF barrier` の水輸送を同時に測る設計を採っております。
- この時点で、`BBB water exchange` と `BCSFB water transport` は interchangeable ではございません。

批判:

- front door で barrier-side human evidence を一語で書くと、`BBB` と `BCSFB` の区別自体を消してしまいます。
- これは site が繰り返し強調している `same modality != same quantity` という原則に反します。

### 2. `choroid-plexus perfusion` と `blood-to-CSF transport` は同じ row ではございません

- [Zhao et al. (2020)](https://pubmed.ncbi.nlm.nih.gov/32962708/) は `Non-invasive measurement of choroid plexus apparent blood flow with arterial spin labeling` であり、主要 object は apparent blood flow でございます。
- [Sun et al. (2024)](https://doi.org/10.1186/s12987-024-00603-y) も `Choroid plexus aging: structural and vascular insights from the HCP-aging dataset` として perfusion / diffusion / volume を扱っております。
- 一方で [Petitclerc et al. (2021)](https://pubmed.ncbi.nlm.nih.gov/34826596/) は `Ultra-long-TE arterial spin labeling reveals rapid and brain-wide blood-to-CSF water transport in humans` と明示しており、主要 object は blood-to-CSF transport でございます。

批判:

- perfusion map があることを `blood-to-CSF transport is measured` に読み替えてはいけません。
- 両者は acquisition, compartment model, and biological claim ceiling が異なります。

### 3. `water cycling at the choroid plexus` もさらに別の inferential object でございます

- [Anderson et al. (2022)](https://pubmed.ncbi.nlm.nih.gov/34542012/) は `DCE-MRI of Brain Fluid Barriers: In Vivo Water Cycling at the Human Choroid Plexus` を報告しました。
- これは choroid plexus epithelium を介した water cycling を扱う route であり、generic clearance capacity や generic BBB permeability の単純代用ではございません。

批判:

- `water-related barrier signal exists` という一文では、perfusion, transport, cycling が同じ object に圧縮されます。
- その圧縮は、どこまでが direct observable でどこからが mechanistic interpretation かを不透明にします。

### 4. `apparent BCSFB exchange` は promising でも、validated maintenance-state truth ではございません

- [Wu et al. (2026)](https://pubmed.ncbi.nlm.nih.gov/40832972/) は `Feasibility of relaxation-exchange magnetic resonance imaging (REXI) for measuring water exchange across the blood-CSF barrier in the human choroid plexus` を報告しました。
- 題名どおり、ここで主張されているのは `feasibility` と `water exchange across the blood-CSF barrier` でございます。

批判:

- したがって front door でこの line を書く場合、`apparent exchange proxy` や `feasibility-stage route` という注意書きが必要でございます。
- これを省くと、読者は `human BCSFB function is already directly quantified at decision grade` と誤読しかねません。

### 5. front door での再圧縮は summary booklet の ceiling も下げます

- `summary_booklet.md` は source pages の front matter と主要本文から再構成されます。
- したがって `index.md`, `faq.md`, `tech_roadmap.md`, `perspective.md` が粗いままだと、summary layer でも `BCSFB` の internal split が失われます。

批判:

- 研究入口ページこそ、最初に `何が測れていて、何がまだ proxy なのか` を route-family 単位で固定すべきでございます。
- 深いページだけで厳密でも、front door が粗ければ public understanding はそこで止まります。

## 今回実行した変更

- `index.md`
  - human evidence list と neurovascular note を更新し、`blood-CSF barrier / choroid-plexus perfusion / blood-to-CSF transport / water-cycling / apparent-exchange proxies` を front door で独立に読めるようにしました。
  - maintenance-state caution box に、Zhao 2020 / Sun 2024 / Petitclerc 2021 / Anderson 2022 / Wu 2026 / Petitclerc 2026 を追加し、`which route and which quantity` を必須開示にしました。

- `faq.md`
  - human observability answer と route tables を更新し、`BBB water exchange`, `tracer-specific BBB transport`, `BCSFB/choroid-plexus family` を別 row にしました。
  - later-stage verification table にも `BCSFB` row を追加し、読者が `same modality` で quantity を混ぜないようにしました。

- `tech_roadmap.md`
  - page highlights と known points を更新し、human barrier-side evidence を `BBB` と `BCSFB` の両方で route-family 化しました。
  - roadmap table に `Human blood-CSF barrier / choroid-plexus perfusion / transport family` row を追加しました。

- `perspective.md`
  - front-door summary, note box, and route table を更新し、`BCSFB` の内部でも perfusion / transport / water cycling / apparent exchange を同列に潰さないようにしました。
  - human evidence classes の説明文でも、`BBB`, `BCSFB`, `clearance` を distinct rows として明示しました。

- `summary_booklet.md`
  - source updates を反映するために再生成し、summary layer にも `BCSFB/choroid-plexus` family split を反映しました。

## 今回止めた誤読

- `barrier-side human MRI exists` だから maintenance-state observability はほぼ解けている
- `BCSFB` は `BBB` の近縁なので同じ row に置いてよい
- `choroid-plexus perfusion` と `blood-to-CSF transport` はほぼ同じ量である
- `water cycling` や `apparent exchange` は generic clearance truth として読んでよい
- deep page だけ厳密なら front door の圧縮は問題にならない

## 検証

- `ruby scripts/build_summary_booklet.rb`
- `git diff --check`
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`
- `rg -n "blood-CSF|choroid-plexus|BCSFB" summary_booklet.md`
- `rg -n "blood-CSF|choroid-plexus|BCSFB" _site/index.html _site/faq.html _site/tech_roadmap.html _site/perspective.html _site/summary_booklet.html`

## 外部依存タスク

- なし
  - 今回の変更は、web 上の一次文献確認、repo 内改稿、summary regeneration、ローカル検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Zhao L, Taso M, Dai W, Press DZ, Alsop DC. Non-invasive measurement of choroid plexus apparent blood flow with arterial spin labeling. *Fluids Barriers CNS*. 2020. https://pubmed.ncbi.nlm.nih.gov/32962708/
2. Sun Z, Li C, Zhang J, Wisniewski T, Ge Y. Choroid plexus aging: structural and vascular insights from the HCP-aging dataset. *Fluids Barriers CNS*. 2024. https://doi.org/10.1186/s12987-024-00603-y
3. Petitclerc L, Hirschler L, Wells JA, Thomas DL, van Walderveen MAA, van Buchem MA, van Osch MJP. Ultra-long-TE arterial spin labeling reveals rapid and brain-wide blood-to-CSF water transport in humans. *NeuroImage*. 2021. https://pubmed.ncbi.nlm.nih.gov/34826596/
4. Anderson VC, Tagge IJ, Doud A, Li X, Springer CJ Jr, Quinn JF, Kaye J, Wild KV, Rooney WD. DCE-MRI of Brain Fluid Barriers: In Vivo Water Cycling at the Human Choroid Plexus. *Tissue Barriers*. 2022. https://pubmed.ncbi.nlm.nih.gov/34542012/
5. Wu X, Tan S, Zhang Y, Yin Y, Hsu YC, Xue R, Bai R. Feasibility of relaxation-exchange magnetic resonance imaging (REXI) for measuring water exchange across the blood-CSF barrier in the human choroid plexus. *J Cereb Blood Flow Metab*. 2026. https://pubmed.ncbi.nlm.nih.gov/40832972/
6. Petitclerc L, Durrant H, Hirschler L, Václavů L, van Osch MJP. Simultaneous measurement of water transport across the blood-brain and blood-CSF barrier in the human brain with arterial spin labeling MRI. *J Cereb Blood Flow Metab*. 2026. https://journals.sagepub.com/doi/10.1177/0271678X261429042
