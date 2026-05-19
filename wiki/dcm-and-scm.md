---
layout: default
title: "DCM / SCM"
description: "Dynamic Causal Modeling と Structural Causal Model の違い、役割、限界を整理します。"
article_type: Wiki
subtitle: "脳の因果をどうモデル化するか"
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
DCM は、神経回路のダイナミクスを仮定してデータに合わせる実践的モデルです。SCM は、原因と結果の関係をより一般的に記述する因果枠組みです。Mind-Upload では、DCM を脳データの具体的推定に、SCM を介入と反事実の整理に使います。
</p>
</div>

<section class="section" id="compare">
<h2 class="section-title">DCM と SCM の違い</h2>
<table class="data-table">
<thead>
<tr>
<th>観点</th>
<th>DCM</th>
<th>SCM</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>主目的</strong></td>
<td>神経ダイナミクスを推定する。</td>
<td>因果関係と介入を明示する。</td>
</tr>
<tr>
<td><strong>強み</strong></td>
<td>脳計測データに近い。</td>
<td>反事実や do 演算に向く。</td>
</tr>
<tr>
<td><strong>難所</strong></td>
<td>モデル同定可能性、モデル空間の大きさ。</td>
<td>脳の再帰構造や潜在変数の扱い。</td>
</tr>
<tr>
<td><strong>WBEでの使い方</strong></td>
<td>生成モデルの候補を具体化する。</td>
<td>何を介入で検証すべきかを定める。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="workflow">
<h2 class="section-title">どう使い分けるか</h2>
<div class="key-points">
<h4>Workflow</h4>
<ul>
<li><strong>DCM：</strong>どの領域がどの入力でどう結合するかをモデル化する。</li>
<li><strong>SCM：</strong>条件を変えたらどの変数がどう変わるかを整理する。</li>
<li><strong>接続：</strong>DCM で得た生成仮説を、SCM 的な介入評価へ接続する。</li>
</ul>
</div>
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
<td><strong>モデル同定可能性</strong><br>複数モデルのどれが正しいか。</td>
<td>似た観測を複数の構造が生みうるからです。</td>
<td>有効結合の解釈が揺れます。</td>
<td>より強い因果主張ができます。</td>
</tr>
<tr>
<td><strong>サイクルの扱い</strong><br>脳の再帰的接続を SCM でどう扱うか。</td>
<td>単純な DAG 仮定が成り立たないからです。</td>
<td>反事実評価の理論整理が難しいです。</td>
<td>より現実的な因果モデルに近づけます。</td>
</tr>
<tr>
<td><strong>個人差と縦断安定性</strong><br>推定結合が安定特徴か一時状態か。</td>
<td>日内変動や計測ノイズの影響が大きいからです。</td>
<td>本人性指標へつなぎにくいです。</td>
<td>個人特性としての因果指紋に近づけます。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-it-matters">
<h2 class="section-title">このページが分かると何が進むか</h2>
<div class="key-points">
<h4>Practical Gain</h4>
<ul>
<li>因果モデルの名前を、役割の違いとして理解できます。</li>
<li>なぜ観察だけでなく介入が必要か説明できます。</li>
<li>生成モデルと検証プロトコルをつなぐ見取り図ができます。</li>
</ul>
</div>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>関連Wiki</h4>
<ul>
<li><a href="{{ '/wiki/modeling-basics.html' | relative_url }}">モデルと因果 →</a></li>
<li><a href="{{ '/wiki/causal-verification.html' | relative_url }}">因果検証 →</a></li>
<li><a href="{{ '/wiki/inverse-problem-and-esi.html' | relative_url }}">逆問題とESI →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Related U</h4>
<ul>
<li><a href="{{ '/wiki/u1-inverse-identifiability.html' | relative_url }}">U1 逆問題の同定可能性 →</a></li>
<li><a href="{{ '/wiki/u4-counterfactual-equivalence.html' | relative_url }}">U4 因果同値 →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>元ページ</h4>
<ul>
<li><a href="{{ '/glossary.html#modeling' | relative_url }}">Glossary: モデル化 →</a></li>
<li><a href="{{ '/perspective.html#technical-framework' | relative_url }}">Perspective: Technical Framework →</a></li>
<li><a href="{{ '/proposals.html#integrated-streams' | relative_url }}">Proposals: 統合本文 →</a></li>
</ul>
</div>

</aside>
</main>
