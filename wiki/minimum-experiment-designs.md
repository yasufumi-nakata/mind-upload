---
layout: default
title: "最小実験設計"
description: "Mind-Upload の各主張をどの最小比較で崩しにいくかを、初歩から整理したレシピ集です。"
article_type: Wiki
subtitle: "大きい主張を、小さい実験単位へ分解する"
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
大きい理論争点でも、最初に必要なのは「最低限どんな比較をすれば、その主張が一歩前に進むか」です。このページでは、Mind-Upload で頻出する実験設計を、<strong>最小実験単位</strong>として整理します。
</p>
</div>

<section class="section" id="principles">
<h2 class="section-title">最初に固定する4点</h2>
<div class="stage-list">
<div class="stage-item">
<div class="stage-number">1</div>
<div class="stage-body">
<h4>比較対象</h4>
<p>何と何を比べるのかを最初に固定します。個体内、個体間、bio-model、旧版-新版のどれかを曖昧にしません。</p>
</div>
</div>
<div class="stage-item">
<div class="stage-number">2</div>
<div class="stage-body">
<h4>介入</h4>
<p>刺激変更、条件入れ替え、局所抑制、閉ループ遅延など、何を意図的に変えるかを固定します。</p>
</div>
</div>
<div class="stage-item">
<div class="stage-number">3</div>
<div class="stage-body">
<h4>終点</h4>
<p>精度、分布差、安定性、散逸量、本人性保持率など、合格指標を先に決めます。</p>
</div>
</div>
<div class="stage-item">
<div class="stage-number">4</div>
<div class="stage-body">
<h4>停止規則</h4>
<p>何が起きたら主張を弱めるか、次段階へ進まないかを登録します。</p>
</div>
</div>
</div>
</section>

<section class="section" id="recipes">
<h2 class="section-title">よく使う最小レシピ</h2>
<table class="data-table">
<thead>
<tr>
<th>レシピ</th>
<th>何を見るか</th>
<th>最低限必要な比較</th>
<th>主に効く U</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>個体内反復</strong></td>
<td>日内・日間の安定性</td>
<td>同一被験者で複数セッションを比較する</td>
<td>U0, U5, U6</td>
</tr>
<tr>
<td><strong>介入あり/なし比較</strong></td>
<td>相関でなく因果応答</td>
<td>刺激または局所介入条件を切り替える</td>
<td>U4, U8, U13</td>
</tr>
<tr>
<td><strong>シャム対照</strong></td>
<td>見かけの効果を除去</td>
<td>介入手順は同じで有効成分だけ抜く</td>
<td>U4, U11, U13</td>
</tr>
<tr>
<td><strong>OOD 分割</strong></td>
<td>未知条件への一般化</td>
<td>訓練と評価で課題・環境・個体を分ける</td>
<td>U6, U9, U13</td>
</tr>
<tr>
<td><strong>マルチモーダル同期</strong></td>
<td>時刻合わせと座標整合</td>
<td>同一イベントを複数モダリティで計測する</td>
<td>U2, U7</td>
</tr>
<tr>
<td><strong>閉ループ遅延掃引</strong></td>
<td>安定運転領域</td>
<td>遅延とジッタを段階的に増やす</td>
<td>U8, U10</td>
</tr>
<tr>
<td><strong>クロスラボ追試</strong></td>
<td>ラボ依存の除去</td>
<td>別施設で同一プロトコルを再現する</td>
<td>U14, U15</td>
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
<td><strong>最小で十分な比較の定義</strong><br>どこまで比較すれば主張を次段階へ進めてよいか。</td>
<td>WBE 系の主張は層が多く、単一ベンチでは足りないからです。</td>
<td>過剰設計と過少設計の両方を避けられます。</td>
</tr>
<tr>
<td><strong>反事実の近似方法</strong><br>完全に同一の世界を再現できない中で何を対照とみなすか。</td>
<td>脳は同一個体でも時間変動し、真の反実仮想を観測できないためです。</td>
<td>U4 と U13 の検証が、思考実験で止まらず実験計画に落ちます。</td>
</tr>
<tr>
<td><strong>コスト制約下の設計優先順位</strong><br>高価なモダリティや長期追跡をいつ投入すべきか。</td>
<td>課題ごとに必要な情報量が違い、共通ルールがまだ弱いからです。</td>
<td>現実の研究計画へ落とし込みやすくなります。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="templates">
<h2 class="section-title">事前登録テンプレートの最小骨格</h2>
<div class="key-points">
<h4>Minimal Template</h4>
<ul>
<li><strong>主張：</strong>何を成立させたいのか。</li>
<li><strong>比較：</strong>何と何を比べるのか。</li>
<li><strong>介入：</strong>何を変えるのか。</li>
<li><strong>観測量：</strong>何を記録するのか。</li>
<li><strong>終点：</strong>どの指標で合否を決めるのか。</li>
<li><strong>反証条件：</strong>何が起きたら主張を退けるのか。</li>
<li><strong>停止規則：</strong>何が起きたら公開主張を弱めるのか。</li>
</ul>
</div>
</section>

<section class="section" id="why-it-matters">
<h2 class="section-title">このページが分かると何が進むか</h2>
<div class="key-points">
<h4>Practical Gain</h4>
<ul>
<li>未解決問題を、実際に組める比較へ分解できます。</li>
<li>評価指標だけ先に立って、対照が弱い実験を減らせます。</li>
<li>各 U ページの「最小実験設計」を横断的に読み比べやすくなります。</li>
</ul>
</div>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>関連Wiki</h4>
<ul>
<li><a href="{{ '/wiki/observables-and-proxies.html' | relative_url }}">観測量と代理指標 →</a></li>
<li><a href="{{ '/wiki/falsification-and-stop-rules.html' | relative_url }}">反証条件と停止規則 →</a></li>
<li><a href="{{ '/wiki/causal-verification.html' | relative_url }}">因果検証 →</a></li>
<li><a href="{{ '/wiki/unsolved-questions.html' | relative_url }}">未解決問題カタログ →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>元ページ</h4>
<ul>
<li><a href="{{ '/verification.html' | relative_url }}">Verification →</a></li>
<li><a href="{{ '/hands_on.html' | relative_url }}">ハンズオン →</a></li>
<li><a href="{{ '/casework.html' | relative_url }}">ケースワーク →</a></li>
</ul>
</div>

</aside>
</main>
