---
layout: default
title: "Wiki：EEGからL0までの一本道"
description: "EEG の基礎を理解したあと、公開データの選定、L0 の最小ループ、Verification までを一本道で進むためのガイドです。"
article_type: Wiki
subtitle: "EEG入門から再現可能解析まで、戻り先を迷わないための実務ルート"
author: Mind Uploading Research Project
last_updated: "2026-03-06"
note: "Practical route"
audience: "EEGから手を動かし始めたい人、L0の最小ループまでの順番を固定したい人"
reading_time: "8〜12分"
page_intro: "このページは、EEG の基礎を読んだあとに、どの公開データで始め、何を一式として残し、どこで勝利条件を確認するかを一本道で整理する実務ガイドです。EEG 101、Datasets、Hands-on、Verification を往復しやすくするための補助線として使います。"
accuracy_note: "ここで扱うのは L0 の再現可能解析までの入口です。L1 以降の主張や本人性の議論は、このルートだけでは扱いません。"
page_highlights:
  - "EEG 101 → Datasets → Hands-on → Verification の順に、役割を分けて読めます。"
  - "各段階で『次に何を決めるか』と『何を残すか』を明示します。"
  - "手戻りしやすいポイントを、先回りで wiki に逃がします。"
known_points:
  - "EEG の基礎を理解したあとに、公開データで L0 を作る流れは比較的はっきりしています。"
  - "L0 では高精度より、再現可能な入力・QC・処理・出力・監査を一周させることが重要です。"
  - "Datasets と Hands-on と Verification は、同じ実務でも役割が違います。"
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
recommended_pages:
  - label: "EEG入門"
    url: "/eeg_101.html"
  - label: "データ&ベンチ"
    url: "/datasets.html"
  - label: "ハンズオン"
    url: "/hands_on.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>一本道で進める</h2>
<p>
EEG を学んだあとに迷いやすいのは、<strong>次にデータを選ぶのか</strong>、<strong>いきなり手を動かすのか</strong>、<strong>先に勝利条件を確認するのか</strong>が分からなくなることです。このルートでは、その順番を一本道に固定します。
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
<td>最初にどの公開データで L0 を始めるかを決めます。</td>
<td>スターターデータを 1 本に絞れたら次へ進みます。</td>
</tr>
<tr>
<td><strong>3</strong></td>
<td><a href="dataset-splits-and-leakage.html">データ分割とデータリーク</a></td>
<td>train/test の単位と、触ってはいけない test の境界を固定します。</td>
<td>分割規則を文章で書けたら次へ進みます。</td>
</tr>
<tr>
<td><strong>4</strong></td>
<td><a href="event-sync-and-measurement-logs.html">イベント同期と観測ログ</a></td>
<td>raw EEG のほかに events、刺激ログ、同期、bad segment を何として残すか決めます。</td>
<td>観測ログの最小項目を列挙できたら次へ進みます。</td>
</tr>
<tr>
<td><strong>5</strong></td>
<td><a href="../hands_on.html">Hands-on</a></td>
<td>BIDS、QC、前処理、ベースライン、失敗例を一周つなぐ手順を実行します。</td>
<td>L0 の成果物一式が揃ったら次へ進みます。</td>
</tr>
<tr>
<td><strong>6</strong></td>
<td><a href="../verification.html">Verification</a></td>
<td>いま作った L0 が、どの主張レベルで何を満たしているかを確認します。</td>
<td>L0 と L1 以降を混同しない説明ができたら一区切りです。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="what-to-output">
<h2 class="section-title">この一本道で最後に残したいもの</h2>
<div class="key-points">
<h4>Artifact Pack</h4>
<ul>
<li><strong>入力：</strong>BIDS 形式のデータ、メタデータ、events、同期情報。</li>
<li><strong>品質：</strong>QC ログ、除外基準、bad channel / bad segment の記録。</li>
<li><strong>処理：</strong>前処理条件、乱数、使用バージョン、実行手順。</li>
<li><strong>出力：</strong>最低 1 本のベースライン指標と、その再現ログ。</li>
<li><strong>監査：</strong>失敗例、うまくいかなかった条件、既知の弱点。</li>
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
<td>BIDS や Validator の役割差で止まる</td>
<td><a href="standards-repositories-validators-and-benchmarks.html">規格・置き場・Validator・ベンチマーク</a></td>
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
<li><strong>raw EEG だけあれば十分だと思う：</strong> events や同期ログがないと、比較可能な入力になりません。</li>
<li><strong>Hands-on 完了をそのまま L1 や L2 の成功と読む：</strong> まずは L0 の再現可能解析までです。</li>
<li><strong>Verification を最後に読まずに終える：</strong> 何が満たせていて何がまだ満たせていないかを明示しないと、主張レベルがずれます。</li>
</ul>
</div>
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
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../eeg_101.html">EEG入門 →</a></li>
<li><a href="../datasets.html">データ&ベンチ →</a></li>
<li><a href="../hands_on.html">ハンズオン →</a></li>
</ul>
</div>
</aside>
</main>
