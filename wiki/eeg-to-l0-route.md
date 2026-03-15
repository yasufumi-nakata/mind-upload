---
layout: default
title: "Wiki：EEGからL0までの一本道"
description: "EEG の基礎を理解したあと、公開データの選定、split 固定、観測ログ、derivative lineage、Verification までを一本道で進むためのガイドです。"
article_type: Wiki
subtitle: "EEG入門から再現可能解析まで、raw / derivative 境界を迷わず固定する"
author: Mind Uploading Research Project
last_updated: "2026-03-15"
note: "Practical route"
audience: "EEGから手を動かし始めたい人、L0の最小ループまでの順番を固定したい人"
reading_time: "10〜15分"
page_intro: "このページは、EEG の基礎を読んだあとに、どの公開データで始め、何を一式として残し、どこで勝利条件を確認するかを一本道で整理する実務ガイドです。2026-03 の更新では、event semantics だけでなく derivative lineage と実行環境 pin まで L0 ルートへ組み込みました。"
accuracy_note: "ここで扱うのは L0 の再現可能解析までの入口です。L1 以降の主張や本人性の議論は、このルートだけでは扱いません。ここで固定した provenance は研究妥当性の十分条件ではありませんが、監査可能性の最低条件です。"
page_highlights:
  - "EEG 101 → Datasets → split → 観測ログ → derivative lineage → Verification の順に、役割を分けて読めます。"
  - "raw / derivative の境界、split manifest、container tag ないし lockfile を L0 の必須項目へ含めます。"
  - "各段階で『次に何を決めるか』と『何を残すか』を明示します。"
known_points:
  - "EEG の基礎を理解したあとに、公開データで L0 を作る流れは比較的はっきりしています。"
  - "L0 では高精度より、再現可能な入力・QC・処理・出力・監査を一周させることが重要です。"
  - "Datasets と Hands-on と Verification は、同じ実務でも役割が違います。"
  - "cleaned EEG や feature table は raw の言い換えではなく、lineage を持つ derivative として扱う方が安全です。"
unknown_points:
  - "どのスターターデータが将来の L2 や L3 に最もつながるかは、まだ固定していません。"
  - "L0 のあと、どの課題で生成・介入予測へ進むのが最短かは課題依存です。"
wiki_links:
  - label: "Wiki: EEGの基本"
    url: "/wiki/eeg-basics.html"
    description: "EEG の信号やノイズの初歩に戻りたい人向けです。"
  - label: "Wiki: 実務系ページの読み分けガイド"
    url: "/wiki/practical-pages-reading-guide.html"
    description: "Datasets、Hands-on、Verification の役割差を先に整理できます。"
  - label: "Wiki: L0で最低限そろえる成果物パック"
    url: "/wiki/l0-minimum-artifact-pack.html"
    description: "最終的に何を一式で残すかを 1 枚で確認できます。"
  - label: "Wiki: データ分割とデータリーク"
    url: "/wiki/dataset-splits-and-leakage.html"
    description: "分割単位やリーク事故で手戻りしたくない人向けです。"
  - label: "Wiki: イベント同期と観測ログ"
    url: "/wiki/event-sync-and-measurement-logs.html"
    description: "raw EEG 以外に何を残すべきかを補います。"
  - label: "Wiki: 規格・置き場・Validator・ベンチマーク"
    url: "/wiki/standards-repositories-validators-and-benchmarks.html"
    description: "BIDS、HED、LSL、MNE-BIDS、MOABB の役割差を補います。"
recommended_pages:
  - label: "EEG入門"
    url: "/eeg_101.html"
  - label: "データ&ベンチ"
    url: "/datasets.html"
  - label: "ハンズオン"
    url: "/datasets.html#l0-practice"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>一本道で進める</h2>
<p>
EEG を学んだあとに迷いやすいのは、<strong>次にデータを選ぶのか</strong>、<strong>いきなり手を動かすのか</strong>、<strong>先に勝利条件を確認するのか</strong>が分からなくなることです。このルートでは、その順番を一本道に固定します。2026-03 の更新では、<strong>raw と derivative の境界</strong>もこの一本道の中へ戻しました。
</p>
</div>

<div class="note-box">
<strong>2026-03 の site rule</strong>
<p>
このルートでは、<strong>cleaned EDF/FIF が 1 個ある</strong>ことを L0 完了とみなしません。EEG-BIDS と COBIDAS-MEEG が acquisition / reporting の床を与え、BIDS Derivatives が pipeline lineage を、BIDS Apps が containerized execution の再現性を押し上げたためでございます。したがって本サイトでは、<strong>split manifest</strong>、<strong><code>GeneratedBy</code> / <code>SourceDatasets</code></strong>、<strong>command provenance</strong>、<strong>container tag ないし lockfile</strong> が無ければ L0 は exploratory に止めます。
</p>
</div>

<section class="section" id="route">
<h2 class="section-title">EEGからL0までの6ステップ</h2>
<table class="data-table">
<thead>
<tr>
<th>順番</th>
<th>開くページ</th>
<th>ここで決めること</th>
<th>次へ進む条件</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1</strong></td>
<td><a href="../eeg_101.html">EEG 101</a></td>
<td>EEG が何を測れて、何を単体では言えないかを理解します。</td>
<td>EEG を魔法の読心術として読まない前提ができたら次へ進みます。</td>
</tr>
<tr>
<td><strong>2</strong></td>
<td><a href="../datasets.html">Datasets</a></td>
<td>最初にどの公開データで L0 を始めるかを決め、dataset version と label provenance を確認します。</td>
<td>スターターデータを 1 本に絞り、snapshot / version / DOI を書けたら次へ進みます。</td>
</tr>
<tr>
<td><strong>3</strong></td>
<td><a href="dataset-splits-and-leakage.html">データ分割とデータリーク</a></td>
<td>train/test の単位、独立 ID、test frozen rule、split manifest を固定します。</td>
<td>分割規則を文章と manifest の両方で書けたら次へ進みます。</td>
</tr>
<tr>
<td><strong>4</strong></td>
<td><a href="event-sync-and-measurement-logs.html">イベント同期と観測ログ</a></td>
<td>raw EEG のほかに events、event semantics、label provenance、同期、bad segment、clock domain を何として残すか決めます。</td>
<td>観測ログの最小項目を列挙し、同じ label の意味を説明できたら次へ進みます。</td>
</tr>
<tr>
<td><strong>5</strong></td>
<td><a href="../datasets.html#l0-practice">Hands-on</a></td>
<td>BIDS、QC、前処理、ベースラインを一周つなぎ、derivatives 側に <code>GeneratedBy</code> / <code>SourceDatasets</code>、command provenance、seed、container tag ないし lockfile を残します。</td>
<td>raw input、derivative lineage、baseline、failure log が一式で揃ったら次へ進みます。</td>
</tr>
<tr>
<td><strong>6</strong></td>
<td><a href="../verification.html">Verification</a></td>
<td>いま作った L0 が、どの主張レベルで何を満たしているかを確認し、止める主張も明示します。</td>
<td>L0 と L1 以降を混同せず、何がまだ欠けているかまで説明できたら一区切りです。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="three-ids">
<h2 class="section-title">この一本道で先に固定する 3 つの ID</h2>
<table class="data-table">
<thead>
<tr>
<th>ID</th>
<th>最低限の中身</th>
<th>これが無いと止まる主張</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>raw identity</strong></td>
<td>dataset version、DOI、取得日、raw BIDS metadata。</td>
<td>「同じ入力を使った」という再現主張です。</td>
</tr>
<tr>
<td><strong>derivative identity</strong></td>
<td><code>DatasetType=derivative</code>、<code>GeneratedBy</code>、<code>SourceDatasets</code>、必要な file-level lineage。</td>
<td>「この cleaned output はこの raw から生成された」という lineage 主張です。</td>
</tr>
<tr>
<td><strong>run identity</strong></td>
<td>split manifest、command、git commit、seed、container tag ないし lockfile、主要 parameter file。</td>
<td>「この score はこの条件で出た」という比較可能性の主張です。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="what-to-output">
<h2 class="section-title">この一本道で最後に残したいもの</h2>
<div class="key-points">
<h4>Artifact Pack</h4>
<ul>
<li><strong>入力：</strong>raw BIDS 形式のデータ、dataset version、events、event semantics、clock domain。</li>
<li><strong>品質：</strong>QC ログ、除外基準、bad channel / bad segment の記録。</li>
<li><strong>lineage：</strong>derivatives 側の <code>dataset_description.json</code>、<code>GeneratedBy</code>、<code>SourceDatasets</code>。</li>
<li><strong>評価：</strong>split manifest、baseline、scoring rule、test frozen rule。</li>
<li><strong>実行：</strong>command、主要パラメータ、seed、git commit、container tag ないし lockfile。</li>
<li><strong>監査：</strong>失敗例、うまくいかなかった条件、止めた主張、既知の弱点。</li>
</ul>
</div>
<p>
提出物の形だけを 1 枚で確認したい場合は <a href="l0-minimum-artifact-pack.html">L0で最低限そろえる成果物パック</a> が対応する補助ページです。
</p>
</section>

<section class="section" id="where-to-bounce">
<h2 class="section-title">途中で戻る先</h2>
<table class="data-table">
<thead>
<tr>
<th>止まる場所</th>
<th>戻るとよいページ</th>
</tr>
</thead>
<tbody>
<tr>
<td>EEG そのものの意味で止まる</td>
<td><a href="eeg-basics.html">EEGの基本</a> / <a href="../eeg_101.html">EEG 101</a></td>
</tr>
<tr>
<td>Datasets と Hands-on の違いで止まる</td>
<td><a href="practical-pages-reading-guide.html">実務系ページの読み分けガイド</a></td>
</tr>
<tr>
<td>BIDS、HED、Validator、derivatives の役割差で止まる</td>
<td><a href="standards-repositories-validators-and-benchmarks.html">規格・置き場・Validator・ベンチマーク</a></td>
</tr>
<tr>
<td>event semantics や同期の書き方で止まる</td>
<td><a href="event-sync-and-measurement-logs.html">イベント同期と観測ログ</a></td>
</tr>
<tr>
<td>ベースラインや事前登録の役割で止まる</td>
<td><a href="baselines-prereg-and-model-cards.html">ベースライン・事前登録・モデルカード</a></td>
</tr>
<tr>
<td>L0 のあとにどこへ進むかで止まる</td>
<td><a href="claim-level-reading-routes.html">L0〜L5ごとの読み進め方</a></td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="common-mistakes">
<h2 class="section-title">このルートで起きやすい事故</h2>
<div class="key-points">
<h4>Mistake</h4>
<ul>
<li><strong>EEG 101 の次にすぐモデルを作る：</strong> 先にデータ選定と分割規則を固定しないと、あとで数字が崩れます。</li>
<li><strong>raw EEG だけあれば十分だと思う：</strong> events、event semantics、同期ログがないと、比較可能な入力になりません。</li>
<li><strong>cleaned file を raw の延長だと思う：</strong> derivative lineage が切れると、どの処理から出た結果か追えません。</li>
<li><strong>score を出してから split を整える：</strong> split hash が無い比較は、後から監査できません。</li>
<li><strong>Hands-on 完了をそのまま L1 や L2 の成功と読む：</strong> まずは L0 の再現可能解析までです。</li>
<li><strong>Verification を最後に読まずに終える：</strong> 何が満たせていて何がまだ満たせていないかを明示しないと、主張レベルがずれます。</li>
</ul>
</div>
</section>

<section class="section" id="references">
<h2 class="section-title">参考文献</h2>
<ol>
<li>Gorgolewski KJ, Auer T, Calhoun VD, et al. The brain imaging data structure, a format for organizing and describing outputs of neuroimaging experiments. <em>Sci Data</em>. 2016. <a href="https://doi.org/10.1038/sdata.2016.44" target="_blank">doi:10.1038/sdata.2016.44</a></li>
<li>Pernet CR, Appelhoff S, Gorgolewski KJ, et al. EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. <em>Sci Data</em>. 2019. <a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">doi:10.1038/s41597-019-0104-8</a></li>
<li>Pernet C, Garrido MI, Gramfort A, et al. Issues and recommendations from the OHBM COBIDAS MEEG committee for reproducible EEG and MEG research. <em>Nat Neurosci</em>. 2020. <a href="https://doi.org/10.1038/s41593-020-00709-0" target="_blank">doi:10.1038/s41593-020-00709-0</a></li>
<li>Gorgolewski KJ, Esteban O, Ellis DG, et al. BIDS apps: Improving ease of use, accessibility, and reproducibility of neuroimaging data analysis methods. <em>PLoS Comput Biol</em>. 2017. <a href="https://doi.org/10.1371/journal.pcbi.1005209" target="_blank">doi:10.1371/journal.pcbi.1005209</a></li>
<li>BIDS Specification (stable). Derived dataset and pipeline description. <a href="https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files/dataset-description.html" target="_blank">official documentation</a></li>
</ol>
</section>

<section class="section" id="next-step">
<h2 class="section-title">次に戻る場所</h2>
<p>
EEG の入口へ戻るなら <a href="../eeg_101.html">EEG入門</a>、実務ページの役割差へ戻るなら <a href="practical-pages-reading-guide.html">実務系ページの読み分けガイド</a>、L0 の後の進み方を見るなら <a href="claim-level-reading-routes.html">L0〜L5ごとの読み進め方</a> をご利用ください。
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="practical-pages-reading-guide.html">実務系ページの読み分けガイド →</a></li>
<li><a href="l0-minimum-artifact-pack.html">L0で最低限そろえる成果物パック →</a></li>
<li><a href="dataset-splits-and-leakage.html">データ分割とデータリーク →</a></li>
<li><a href="standards-repositories-validators-and-benchmarks.html">規格・置き場・Validator・ベンチマーク →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../eeg_101.html">EEG入門 →</a></li>
<li><a href="../datasets.html">データ&ベンチ →</a></li>
<li><a href="../datasets.html#l0-practice">ハンズオン →</a></li>
</ul>
</div>
</aside>
</main>
