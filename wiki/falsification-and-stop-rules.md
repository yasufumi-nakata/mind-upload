---
layout: default
title: "反証条件と停止規則"
description: "Mind-Upload の強い主張に必要な、反証条件・停止規則・保留条件を初歩から整理します。"
article_type: Wiki
subtitle: "『どこで諦めるか』まで書いて初めて比較可能になる"
author: Mind Uploading Research Project
last_updated: "2026-03-06"
note: "Cross-cutting guide"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>TL;DR</h2>
<p>
反証条件は「何が起きたらその仮説を退けるか」です。停止規則は「何が起きたらその主張を一旦止めるか」です。似ていますが同じではありません。Mind-Upload では、<strong>主張の強さが上がるほど、この2つを先に書く必要があります</strong>。
</p>
</div>

<section class="section" id="difference">
<h2 class="section-title">まず3つを分けます</h2>
<table class="data-table">
<thead>
<tr>
<th>語</th>
<th>意味</th>
<th>例</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>反証条件</strong></td>
<td>仮説そのものを退ける条件です。</td>
<td>介入条件を少し広げただけで因果一致が崩れる。</td>
</tr>
<tr>
<td><strong>停止規則</strong></td>
<td>研究や公開主張を次段階へ進めない条件です。</td>
<td>ラボ間再現が取れないので L3 主張を止める。</td>
</tr>
<tr>
<td><strong>保留条件</strong></td>
<td>結論を強めも弱めもせず、追加検証待ちにする条件です。</td>
<td>サンプル不足で符号だけ一致し、効果量が不安定。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-hard">
<h2 class="section-title">なぜ書きにくいのか</h2>
<div class="key-points">
<h4>Blockers</h4>
<ul>
<li>脳データはノイズと個体差が大きく、1 回の失敗で理論全体を捨てにくいです。</li>
<li>WBE 系の主張は哲学、計測、モデル、制度が絡み、単一指標で切れません。</li>
<li>強い停止規則を置くと見栄えのよい主張が出しにくくなるため、研究文化的な抵抗もあります。</li>
</ul>
</div>
</section>

<section class="section" id="templates">
<h2 class="section-title">最低限の書き方</h2>
<div class="stage-list">
<div class="stage-item">
<div class="stage-number">1</div>
<div class="stage-body">
<h4>仮説単位を狭くする</h4>
<p>「WBE は可能か」ではなく、「特定の介入辞書で反事実一致が保てるか」のように切ります。</p>
</div>
</div>
<div class="stage-item">
<div class="stage-number">2</div>
<div class="stage-body">
<h4>崩れ方を先に列挙する</h4>
<p>精度低下だけでなく、遅延増大、ドリフト、散逸増加、ラボ依存も失敗様式として入れます。</p>
</div>
</div>
<div class="stage-item">
<div class="stage-number">3</div>
<div class="stage-body">
<h4>主張レベルと結びつける</h4>
<p>L1 の停止規則と L4 の停止規則は同じではありません。クレーム階段と一緒に管理します。</p>
</div>
</div>
</div>
</section>

<section class="section" id="examples">
<h2 class="section-title">U0〜U15 に対する典型例</h2>
<table class="data-table">
<thead>
<tr>
<th>対象</th>
<th>典型的な反証条件</th>
<th>典型的な停止規則</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>U0 同一性</strong></td>
<td>介入集合を少し広げただけで同一判定が崩れる。</td>
<td>閾値がラボや課題ごとに大きく揺れる。</td>
</tr>
<tr>
<td><strong>U4 因果同値</strong></td>
<td>介入方向を変えると応答関係が再現しない。</td>
<td>反事実一致が in-distribution のみで成り立つ。</td>
</tr>
<tr>
<td><strong>U8 閉ループ</strong></td>
<td>遅延やジッタを増やすと短時間で不安定化する。</td>
<td>安全運転領域を事前登録した範囲で示せない。</td>
</tr>
<tr>
<td><strong>U12 分岐本人性</strong></td>
<td>帰属規則が同一事例で相互矛盾する。</td>
<td>制度面の整合がなく、技術主張だけが先行する。</td>
</tr>
<tr>
<td><strong>U14 追試可能性</strong></td>
<td>別ラボで主要指標の符号すら再現しない。</td>
<td>差分ログと失敗例を十分に公開できない。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="unknowns">
<h2 class="section-title">まだ分かっていないこと</h2>
<table class="data-table">
<thead>
<tr>
<th>何が未解決か</th>
<th>なぜ未解決か</th>
<th>分かると何が嬉しいか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>主張レベル別の共通停止規則</strong><br>どこからどこまでを共通規格にできるか。</td>
<td>対象が多層で、純粋な性能指標だけでは足りないからです。</td>
<td>クレームの強さを、比較可能なルールで管理できます。</td>
</tr>
<tr>
<td><strong>ネガティブ結果の扱い</strong><br>どこまでを反証とみなし、どこからを保留とみなすか。</td>
<td>サンプル不足や測定誤差が大きく、失敗の解釈が難しいからです。</td>
<td>失敗共有を、単なる印象論でなく蓄積資産に変えられます。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-it-matters">
<h2 class="section-title">このページが分かると何が進むか</h2>
<div class="key-points">
<h4>Practical Gain</h4>
<ul>
<li>「うまくいったら話す」ではなく、「崩れたらどうするか」まで研究計画に含められます。</li>
<li>各 U ページの停止規則を、同じ読み方で比較できます。</li>
<li>強い主張ほど、どの失敗様式に弱いかを先に書けます。</li>
</ul>
</div>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>関連Wiki</h4>
<ul>
<li><a href="{{ '/wiki/minimum-experiment-designs.html' | relative_url }}">最小実験設計 →</a></li>
<li><a href="{{ '/wiki/failure-modes.html' | relative_url }}">失敗様式カタログ →</a></li>
<li><a href="{{ '/wiki/claim-ladder.html' | relative_url }}">クレーム階段 →</a></li>
<li><a href="{{ '/wiki/unsolved-questions.html' | relative_url }}">未解決問題カタログ →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>元ページ</h4>
<ul>
<li><a href="{{ '/verification.html' | relative_url }}">Verification →</a></li>
<li><a href="{{ '/casework.html' | relative_url }}">ケースワーク →</a></li>
<li><a href="{{ '/tech_roadmap.html#unsolved' | relative_url }}">Roadmap: 未解決問題 →</a></li>
</ul>
</div>

</aside>
</main>
