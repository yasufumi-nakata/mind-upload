---
layout: default
title: "decode と emulate"
description: "デコーディングとエミュレーションの違いを、必要な証拠・ありがちな混同・未解決点とともに整理します。"
article_type: Wiki
subtitle: "『翻訳できる』と『再現できる』は別物"
author: Mind Uploading Research Project
last_updated: "2026-03-06"
note: "Concept Deep Dive"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>TL;DR</h2>
<p>
decode は、観測した脳信号から意味や状態を<strong>読み出す</strong>ことです。emulate は、内部状態が時間発展し、介入に反応し、将来の出力を<strong>自分で生成する</strong>ことです。WBE に近い主張をするには後者の証拠が必要です。
</p>
</div>

<section class="section" id="comparison">
<h2 class="section-title">何が違うのか</h2>
<table class="data-table">
<thead>
<tr>
<th>観点</th>
<th>decode</th>
<th>emulate</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>入力依存性</strong></td>
<td>観測データが主役です。</td>
<td>内部状態と環境との相互作用が主役です。</td>
</tr>
<tr>
<td><strong>評価</strong></td>
<td>精度、再現率、汎化。</td>
<td>介入応答、反事実、安定性、長期ダイナミクス。</td>
</tr>
<tr>
<td><strong>主張の強さ</strong></td>
<td>「予測できた」。</td>
<td>「生成・制御・応答を再現した」。</td>
</tr>
<tr>
<td><strong>典型的な事故</strong></td>
<td>相関を因果と誤認する。</td>
<td>閉ループや因果構造を十分検証せずに強く言う。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="tests">
<h2 class="section-title">emulate に近づくための4つのテスト</h2>
<div class="key-points">
<h4>Minimum Tests</h4>
<ul>
<li><strong>分布外一般化：</strong>未学習条件でどこまで予測が保てるか。</li>
<li><strong>介入応答：</strong>刺激や入力条件を変えたときの分岐を当てられるか。</li>
<li><strong>反事実：</strong>「もし別条件だったら」をモデル内で整合的に扱えるか。</li>
<li><strong>閉ループ安定性：</strong>出力が次の入力に戻る状況でも破綻しないか。</li>
</ul>
</div>
</section>

<section class="section" id="why-confused">
<h2 class="section-title">なぜ混同されやすいか</h2>
<p>
脳信号から自然な文章や画像が再構成されると、それだけで「内部状態を再現した」ように見えます。しかし実際には、言語モデルや事前分布が大きく寄与している可能性があります。そこで Mind-Upload では、<strong>脳由来の情報量を反事実入力で切り分ける</strong>ことを重視します。
</p>
</section>

<section class="section" id="unknowns">
<h2 class="section-title">まだ分かっていないこと</h2>
<table class="data-table">
<thead>
<tr>
<th>何が分かっていないか</th>
<th>なぜ分からないか</th>
<th>今どこで詰まるか</th>
<th>分かると何が嬉しいか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>どの条件を満たせば emulate と呼べるか</strong></td>
<td>単一の定義がなく、課題によって必要条件が違うからです。</td>
<td>L1 と L2 の境界がぶれます。</td>
<td>WBE に近い成果を一貫して比較できます。</td>
</tr>
<tr>
<td><strong>脳由来情報とモデル事前分布の分離</strong></td>
<td>出力が自然であるほど、事前分布の寄与を見落としやすいからです。</td>
<td>「読めた」ことを過大評価しやすいです。</td>
<td>真に脳から得た情報量を見積もれます。</td>
</tr>
<tr>
<td><strong>反事実の正解</strong><br>介入していない分岐をどう評価するか。</td>
<td>同一個体・同一状態で反復できない条件が多いからです。</td>
<td>因果検証の難易度が高いです。</td>
<td>decode 止まりの成果を、より強い生成モデルへ押し上げられます。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-it-matters">
<h2 class="section-title">このページが分かると何が進むか</h2>
<div class="key-points">
<h4>Practical Gain</h4>
<ul>
<li>派手な再構成結果を、どのレベルの主張か見極められます。</li>
<li>ベンチマーク設計に、介入や閉ループが必要な理由を説明できます。</li>
<li>WBE に必要な「生成」の意味を、相関ベースの成功から切り離して理解できます。</li>
</ul>
</div>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>関連Wiki</h4>
<ul>
<li><a href="{{ '/wiki/claim-ladder.html' | relative_url }}">クレーム階段 →</a></li>
<li><a href="{{ '/wiki/modeling-basics.html' | relative_url }}">モデルと因果 →</a></li>
<li><a href="{{ '/wiki/causal-verification.html' | relative_url }}">因果検証 →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Related U</h4>
<ul>
<li><a href="{{ '/wiki/u0-operational-identity.html' | relative_url }}">U0 操作的同一性 →</a></li>
<li><a href="{{ '/wiki/u4-counterfactual-equivalence.html' | relative_url }}">U4 因果同値 →</a></li>
<li><a href="{{ '/wiki/u13-imitation-separation.html' | relative_url }}">U13 模倣分離 →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>元ページ</h4>
<ul>
<li><a href="{{ '/wbe_101.html#decode-vs-emulate' | relative_url }}">WBE入門: decode と emulate →</a></li>
<li><a href="{{ '/faq.html#q2' | relative_url }}">FAQ: decode と emulate →</a></li>
<li><a href="{{ '/perspective.html#decoding-to-emulation-gap' | relative_url }}">Perspective: decode→emulate →</a></li>
</ul>
</div>

</aside>
</main>
