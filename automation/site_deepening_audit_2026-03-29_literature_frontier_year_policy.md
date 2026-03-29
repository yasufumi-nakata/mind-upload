# Site Deepening Audit (2026-03-29, literature frontier year-policy split)

## 対象

- 主対象:
  - `mind_uploading_papers.md`
  - `research_harvest_50.md`
- 調査範囲: 技術 / 自然科学のみ
- 明示的に除外した論点: 哲学、法学、制度論

## 今回この箇所を選んだ理由

- 主要ページでは、local causal maintenance-state frontier と bounded living-human observability frontier を別ラダーとして扱う規則がかなり明確になっております。
- しかし文献アーカイブと evidence bank では、2025-2026 の frontier を速く読む導線が強くなった一方で、
  - online-first 日付
  - issue-year citation
  - local causal maintenance-state papers
  - living-human observability papers
  が高速読みにおいて再圧縮される余地がまだ残っておりました。
- この歪みは単なる書誌整形ではなく、何が「人で直接観測された前進」なのか、何が「局所因果的に latent family を増やした前進」なのかを誤読させます。

## 主要結論

- 文献 front door には、`issue year を採用するが、raw year adjacency は one frontier step と読まない` という明示的な chronology policy が必要でございます。
- 2025-2026 近傍では、少なくとも
  - `U3 / maintenance-state local causality`
  - `U1/U7 / bounded human observability`
  を別ラダーとして先に固定しないと、年順そのものが誤情報になります。
- したがって、mixed archive と evidence bank の入口にも、absolute dates 付きでこの stop-rule を入れるべきでございます。

## 根拠付き批判

### 1. 2025-2026 の technical frontier は one ladder ではありません

- [Terceros et al.](https://doi.org/10.1038/s41586-025-09774-6) は Nature metadata 上で **Published: 26 November 2025** ですが、citation line は **Nature volume 649, pages 1254-1263 (2026)** でございます。
- [Dewa et al.](https://doi.org/10.1038/s41586-025-09619-2) は **Published: 15 October 2025**、**Issue date: 04 December 2025** でございます。
- [Bukalo et al.](https://doi.org/10.1038/s41586-025-10068-0) は **Published: 11 February 2026** でございます。
- [Hirschler et al.](https://doi.org/10.1038/s41593-025-02073-3) は **Published: 14 October 2025** でございます。
- [Dagum et al.](https://doi.org/10.1038/s41467-026-68374-8) は **Published: 27 January 2026** でございます。

批判:

- これらを単純な `2025-2026 frontier` として並べると、published-online timing と issue-year citation のズレが、そのまま frontier の連続性に見えてしまいます。
- しかし site-wide rule は `何の inferential object を強めたか` を先に固定する設計であり、日付近接は evidence class を上書きしてはなりません。

### 2. local causal maintenance-state と bounded human observability は技術的に別ラダーです

- [Terceros et al.](https://doi.org/10.1038/s41586-025-09774-6), [Dewa et al.](https://doi.org/10.1038/s41586-025-09619-2), [Bukalo et al.](https://doi.org/10.1038/s41586-025-10068-0) は、controller-side / local-circuit causal dependence を sharpen する論文でございます。
- [Hirschler et al.](https://doi.org/10.1038/s41593-025-02073-3), [Dagum et al.](https://doi.org/10.1038/s41467-026-68374-8) は、bounded human observability classes や clearance-support physiology を sharpen する論文でございます。

批判:

- 前者は「latent family が残ること」を増やす局所因果エビデンスであり、後者は「living-human route がどこまで proxy として観測可能か」を増やす observability evidence でございます。
- species, spatial unit, direct observable, causal leverage が違うため、chronology だけで並べると「人でそこまで直接見えるようになったから controller causality に近づいた」という誤推論を誘発します。

### 3. archive / evidence bank 側で規則が弱いと、front page 側の厳密さを相殺します

- `mind_uploading_papers.md` は mixed archive であり、law / philosophy / culture も含みます。
- `research_harvest_50.md` は unresolved-question map であり、technical priority route を front door に持っています。
- どちらも `最初に読む導線` を担うため、ここで chronology rule が曖昧だと、深いページに行く前に reader model が歪みます。

批判:

- site の深部だけで rule が正しくても、front door が `fast chronology = frontier` を許すなら、誤読防止の主戦場を落としているのと同じでございます。
- 文献導線は summary page より taxonomy が粗くてよい場所ではなく、むしろ最初に evidence class と ladder identity を固定する場所であるべきでございます。

## 今回実行した変更

- `mind_uploading_papers.md`
  - front matter に chronology-policy の known point / highlight を追加しました。
  - front door に `Technical chronology policy for the 2025-2026 frontier` を追加し、absolute dates と ladder split を明示しました。
  - `Do not merge the maintenance-state frontier with the human-observability frontier` を更新し、Terceros / Dewa / Dagum / Bukalo の具体日付を入れて stop-rule を強化しました。

- `research_harvest_50.md`
  - front matter に chronology-policy の highlight / known point を追加しました。
  - priority-route section の冒頭に `Technical chronology policy for the 2025-2026 frontier` を追加しました。
  - `Do not let chronology fuse U3 causality with U1/U7 observability` を更新し、published / issue dates を explicit にして、frontier judgment の規則を強化しました。

## 今回止めた誤読

- `2025-2026 に papers が固まっている` = `one technical frontier is moving together`
- `published online in late 2025` = `cite as 2025 everywhere`
- `controller-side causal paper` + `human proxy paper` = `same evidential ladder`
- `year adjacency` = `observability and causality are converging into one readout frontier`

## 外部依存タスク

- なし
  - 今回の作業は publisher metadata の確認、repo 内本文修正、監査メモ追加、検証、commit、push までこのセッションで完結できます。

## 参考文献

1. Terceros A, Chen C, Harada Y, et al. *Thalamocortical transcriptional gates coordinate memory stabilization*. Nature. Metadata page shows **Published: 26 November 2025** and citation line **Nature 649, 1254-1263 (2026)**.
   - https://doi.org/10.1038/s41586-025-09774-6
2. Dewa Ki, Kaseda K, Kuwahara A, et al. *The astrocytic ensemble acts as a multiday trace to stabilize memory*. Nature. Metadata page shows **Published: 15 October 2025** and **Issue date: 04 December 2025**.
   - https://doi.org/10.1038/s41586-025-09619-2
3. Bukalo O, O'Sullivan R, Tanisumi Y, et al. *Astrocytes enable amygdala neural representations supporting memory*. Nature. Metadata page shows **Published: 11 February 2026**.
   - https://doi.org/10.1038/s41586-025-10068-0
4. Hirschler L, Runderkamp BA, Decker A, et al. *Region-specific drivers of CSF mobility measured with MRI in humans*. Nature Neuroscience. Metadata page shows **Published: 14 October 2025**.
   - https://doi.org/10.1038/s41593-025-02073-3
5. Dagum P, Elbert DL, Giovangrandi L, et al. *The glymphatic system clears amyloid beta and tau from brain to plasma in humans*. Nature Communications. Metadata page shows **Published: 27 January 2026**.
   - https://doi.org/10.1038/s41467-026-68374-8
