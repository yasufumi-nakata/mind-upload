---
layout: default
title: "Wiki：ベースライン・事前登録・モデルカード"
description: "ベースライン、ベンチマーク、事前登録、モデルカード、失敗例の役割を初歩から整理します。"
article_type: Wiki
subtitle: "『何を比べ、どう固定し、何を残すか』を分けて考える"
author: Mind Uploading Research Project
last_updated: "2026-03-16"
note: "Learning guide"
audience: "研究運用の言葉が似て見える人、比較可能性の作り方を初歩から理解したい人"
reading_time: "10〜15分"
page_intro: "このページは、Mind-Upload で繰り返し出てくる『ベースライン』『ベンチマーク』『事前登録』『モデルカード』『失敗例』の役割差を、初歩から整理する wiki です。高いスコアを出すことと、比較可能な前進を作ることの違いを理解する足場として使います。"
accuracy_note: "ここでは運用上の役割差を分かりやすく説明します。実際のテンプレートや仕様は公開ページ側で確認してください。"
page_highlights:
  - "ベースライン、ベンチマーク、事前登録、モデルカードは、役割が違います。"
  - "失敗例やネガティブ結果も、比較可能性の一部です。"
  - "multimodal や atlas prior を使う結果では、通常のモデルカードに加えて Fusion Card も必要です。"
  - "点数だけではなく、どう測り、どう失敗したかまで残すのが重要です。"
known_points:
  - "比較可能な前進には、出発点、採点基準、事前ルール、結果の記録が必要です。"
  - "ベースラインなしでは、改善を主張しにくくなります。"
  - "事前登録やモデルカードがないと、あとから都合よく解釈しやすくなります。"
unknown_points:
  - "どのテンプレートを WBE 全体で標準化するかは、まだ運用設計の途中です。"
  - "どこまでの失敗例やネガティブ結果を必須公開にするかは今後の整備対象です。"
wiki_links:
  - label: "Wiki: 検証基盤の基本"
    url: "/wiki/verification-basics.html"
    description: "まず Verification Commons の全体像へ戻れます。"
  - label: "Wiki: データ分割とリーク"
    url: "/wiki/dataset-splits-and-leakage.html"
    description: "ベンチマーク運用で特に危険なリークを補います。"
  - label: "Wiki Home"
    url: "/wiki/"
    description: "他の基礎ページへ戻れます。"
recommended_pages:
  - label: "検証基盤"
    url: "/verification.html"
  - label: "ハンズオン"
    url: "/datasets.html#l0-practice"
  - label: "ケースワーク"
    url: "/verification.html#casework"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>いちばん短い地図</h2>
<p>
ベースラインは「出発点」、ベンチマークは「採点基準」、事前登録は「やる前の約束」、モデルカードは「結果の成績表」、失敗例は「どこで崩れたかの記録」です。どれか 1 つだけでは、比較可能な前進になりません。
</p>
</div>

<div class="note-box">
<strong>2026-03 追補</strong>
<p>
L1 以上の結果では、通常のモデルカードに加えて <a href="../verification.html#observability-budget">Observability Budget</a> を添付し、measurement stack、直接観測量、残る latent state、claim ceiling、abstention 条件を明示する運用にそろえました。さらに multimodal / atlas prior 結果では <a href="../verification.html#fusion-card">Fusion Card</a> を添付し、取得関係、時計系、登録誤差、融合モデル、single-modality baseline との差分、外部妥当化を同時に残します。
</p>
</div>

<section class="section" id="roles">
<h2 class="section-title">まず役割を分ける</h2>
<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>役割</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>ベースライン</strong></td>
<td>最低限の比較相手です。改善を言うための出発点になります。</td>
</tr>
<tr>
<td><strong>ベンチマーク</strong></td>
<td>何を、どのデータで、どの指標で比べるかを固定します。</td>
</tr>
<tr>
<td><strong>事前登録</strong></td>
<td>やる前に、指標、停止条件、分析方針を固定します。</td>
</tr>
<tr>
<td><strong>モデルカード</strong></td>
<td>点数、弱点、リーク対策、失敗例、計算条件、さらに L1 以上では Observability Budget、multimodal / atlas prior 結果では Fusion Card を残します。</td>
</tr>
<tr>
<td><strong>失敗例・ネガティブ結果</strong></td>
<td>何が効かなかったか、どこで崩れたかを残します。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-all-needed">
<h2 class="section-title">なぜ全部必要なのか</h2>
<table class="data-table">
<thead>
<tr>
<th>欠けるもの</th>
<th>起こりやすい問題</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>ベースラインがない</strong></td>
<td>数字が良いのか悪いのか、改善なのか偶然なのか判断しにくくなります。</td>
</tr>
<tr>
<td><strong>ベンチマークがない</strong></td>
<td>人ごとに違う採点をしてしまい、比較が壊れます。</td>
</tr>
<tr>
<td><strong>事前登録がない</strong></td>
<td>あとから都合のよい条件だけを選びやすくなります。</td>
</tr>
<tr>
<td><strong>モデルカードがない</strong></td>
<td>点数だけが残り、弱点や再現手順が見えなくなります。</td>
</tr>
<tr>
<td><strong>失敗例がない</strong></td>
<td>どこで崩れるかが共有されず、同じ失敗を繰り返しやすくなります。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="simple-flow">
<h2 class="section-title">最小の流れで見る</h2>
<div class="stage-list">
<div class="stage-item">
<div class="stage-number">01</div>
<div class="stage-body">
<h4>ベースラインを置く</h4>
<p>まず単純でもよいので、比較の出発点を 1 本置きます。</p>
</div>
</div>
<div class="stage-item">
<div class="stage-number">02</div>
<div class="stage-body">
<h4>ベンチマークを固定する</h4>
<p>データ、分割、指標、禁止事項をそろえます。</p>
</div>
</div>
<div class="stage-item">
<div class="stage-number">03</div>
<div class="stage-body">
<h4>事前登録する</h4>
<p>どの条件で成功・失敗とみなすかを先に決めます。</p>
</div>
</div>
<div class="stage-item">
<div class="stage-number">04</div>
<div class="stage-body">
<h4>モデルカードと失敗例を残す</h4>
<p>点数だけでなく、弱点と崩れ方まで公開します。</p>
</div>
</div>
</div>
</section>

<section class="section" id="negative-results">
<h2 class="section-title">失敗例はなぜ大事か</h2>
<p>
成功例だけ集めると、たまたま勝った条件だけが残ります。Mind-Upload のように主張が大きい分野では、<strong>どの条件で崩れたか</strong>を残すことが、成功例を残すのと同じくらい重要です。
</p>
<div class="note-box">
<strong>失敗例に最低限ほしいもの</strong>
<p>
どの条件で、どの指標が、どれだけ崩れたか。リークや分割の問題だったのか、OOD で崩れたのか、計算資源が足りなかったのか、を切り分けて残す必要があります。
</p>
</div>
</section>

<section class="section" id="how-to-read">
<h2 class="section-title">公開ページを読むときの最低チェック</h2>
<div class="key-points">
<h4>Checklist</h4>
<ul>
<li><strong>ベースラインがあるか：</strong>何と比べたのかが明示されているか。</li>
<li><strong>ベンチマークが固定されているか：</strong>データ、分割、指標が書かれているか。</li>
<li><strong>事前登録があるか：</strong>あとから条件を変えていないか。</li>
<li><strong>モデルカードや失敗例があるか：</strong>弱点や崩れ方に加え、L1 以上では Observability Budget、multimodal / atlas prior 結果では Fusion Card が見えるか。</li>
</ul>
</div>
</section>

<section class="section" id="return">
<h2 class="section-title">次にどこへ戻るか</h2>
<p>
設計図へ戻るなら <a href="../verification.html">検証基盤</a>、実務へ戻るなら <a href="../datasets.html#l0-practice">ハンズオン</a>、他分野の先例へ戻るなら <a href="../verification.html#casework">ケースワーク</a> をご利用ください。
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="verification-basics.html">検証基盤の基本 →</a></li>
<li><a href="dataset-splits-and-leakage.html">データ分割とデータリーク →</a></li>
<li><a href="claims-and-evidence.html">主張と証拠の読み方 →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../verification.html">検証基盤 →</a></li>
<li><a href="../datasets.html#l0-practice">ハンズオン →</a></li>
<li><a href="../verification.html#casework">ケースワーク →</a></li>
</ul>
</div>
</aside>
</main>
