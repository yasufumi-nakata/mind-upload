---
layout: default
title: "FEP / 能動的推論 / マルコフブランケット"
description: "自由エネルギー原理、能動的推論、マルコフブランケットの関係と、WBEへの含意を初歩から整理します。"
article_type: Wiki
subtitle: "脳を『受動的な読み出し装置』でなく『能動的な予測系』として見る"
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
FEP は、生体が予測誤差や驚きを抑えながら自己を維持するという大きな枠組みです。能動的推論はその実装側、マルコフブランケットはその境界概念です。Mind-Upload では、これらを<strong>動的プロセスとしての心</strong>を考えるために使います。
</p>
</div>

<section class="section" id="terms">
<h2 class="section-title">3つの語を分ける</h2>
<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>ざっくりした説明</th>
<th>WBEでの意味</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>FEP</strong></td>
<td>生体は長く存在するために予測誤差を抑える、という包括原理です。</td>
<td>自己維持する系として脳を捉える見方になります。</td>
</tr>
<tr>
<td><strong>能動的推論</strong></td>
<td>環境を変えながら、自分の予測に合う状態を作る行動理論です。</td>
<td>エミュレータを受動的デコーダーでなくエージェントとして設計します。</td>
</tr>
<tr>
<td><strong>マルコフブランケット</strong></td>
<td>系と環境の境界を表す統計的概念です。</td>
<td>どこまでを自己とみなすかの工学的ヒントになります。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-use">
<h2 class="section-title">なぜ Mind-Upload がこれを参照するのか</h2>
<p>
スキャン＆コピー型の発想だけでは、動的な相互作用や連続性をうまく扱えません。FEP と能動的推論を参照すると、脳を「状態を保ちながら環境とやり取りする系」として扱えます。これは段階的移行や閉ループ評価と相性が良いです。
</p>
<div class="cta-box">
<h4>Deep Dive</h4>
<p>段階的移行は <a href="{{ '/wiki/copy-problem-and-continuity.html' | relative_url }}">コピー問題と連続性</a>、散逸条件は <a href="{{ '/wiki/thermodynamics-and-ness.html' | relative_url }}">熱力学とNESS</a> で詳しく扱います。</p>
</div>
</section>

<section class="section" id="criticisms">
<h2 class="section-title">よくある批判</h2>
<div class="key-points">
<h4>Common Critiques</h4>
<ul>
<li><strong>包括的すぎる：</strong>何でも説明できるように見えて、反証が難しい。</li>
<li><strong>マルコフブランケットの実在性：</strong>統計境界を、そのまま主体の境界とみなしてよいか議論がある。</li>
<li><strong>意識との距離：</strong>自己維持や適応を説明できても、主観経験まで説明できるかは別問題です。</li>
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
<td><strong>FEP の反証可能性</strong><br>どこまで具体的に崩せる理論か。</td>
<td>包括原理として広く適用できてしまうからです。</td>
<td>設計原理として便利でも、科学的に強く言いにくいです。</td>
<td>採用範囲をより明確に限定できます。</td>
</tr>
<tr>
<td><strong>ブランケット境界の実装</strong><br>実際の脳-機械境界をどう定義するか。</td>
<td>理論概念を工学仕様へ直接落としにくいからです。</td>
<td>段階的移行の設計が曖昧になります。</td>
<td>ハイブリッド系の設計条件が具体化します。</td>
</tr>
<tr>
<td><strong>意識との接続</strong><br>FEP が主観経験まで説明するか。</td>
<td>適応原理と経験の質は別レイヤーだからです。</td>
<td>理論の使いどころを誤解しやすいです。</td>
<td>FEP を『実装原理』として限定して使えます。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-it-matters">
<h2 class="section-title">このページが分かると何が進むか</h2>
<div class="key-points">
<h4>Practical Gain</h4>
<ul>
<li>FEP を意識理論そのものと混同しにくくなります。</li>
<li>閉ループ、自律性、段階的移行の議論がつながります。</li>
<li>動的プロセスとしての WBE という見方の意味が見えます。</li>
</ul>
</div>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>関連Wiki</h4>
<ul>
<li><a href="{{ '/wiki/consciousness-basics.html' | relative_url }}">意識理論 →</a></li>
<li><a href="{{ '/wiki/consciousness-theory-comparison.html' | relative_url }}">意識理論比較 →</a></li>
<li><a href="{{ '/wiki/identity-and-ethics.html' | relative_url }}">本人性と倫理 →</a></li>
<li><a href="{{ '/wiki/copy-problem-and-continuity.html' | relative_url }}">コピー問題と連続性 →</a></li>
<li><a href="{{ '/wiki/thermodynamics-and-ness.html' | relative_url }}">熱力学とNESS →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Related U</h4>
<ul>
<li><a href="{{ '/wiki/u3-subject-boundary.html' | relative_url }}">U3 主体境界 →</a></li>
<li><a href="{{ '/wiki/u8-closed-loop-stability.html' | relative_url }}">U8 閉ループ安定性 →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>元ページ</h4>
<ul>
<li><a href="{{ '/idea.html' | relative_url }}">Framework →</a></li>
<li><a href="{{ '/perspective.html#technical-framework' | relative_url }}">Perspective: Technical Framework →</a></li>
<li><a href="{{ '/tech_roadmap.html#qa-r4' | relative_url }}">Roadmap: R4 →</a></li>
</ul>
</div>

</aside>
</main>
