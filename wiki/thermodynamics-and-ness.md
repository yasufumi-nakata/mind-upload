---
layout: default
title: "熱力学とNESS"
description: "NESS、EPR、Landauer限界、論理コストと散逸コストの違いを初歩から整理します。"
article_type: Wiki
subtitle: "『計算できる』だけでなく『どんな物理コストで動くか』を見る"
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
熱力学の論点は、「同じ計算をした」だけでは脳の物理的条件を再現したことにならないかもしれない、という問題です。Mind-Upload では、論理コストと散逸コストを分け、<strong>NESS と EPR</strong> を補助的な検証要件として扱います。
</p>
</div>

<section class="section" id="terms">
<h2 class="section-title">最初に押さえる3語</h2>
<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>ざっくりした意味</th>
<th>WBEでの意味</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>NESS</strong></td>
<td>非平衡定常状態。外からエネルギーを受け取りつつ定常的に存在する状態です。</td>
<td>脳のような散逸構造をどう模倣するかに関係します。</td>
</tr>
<tr>
<td><strong>EPR</strong></td>
<td>エントロピー生成速度。どれだけ不可逆な散逸があるかの指標です。</td>
<td>物理的整合性の補助指標として参照されます。</td>
</tr>
<tr>
<td><strong>Landauer限界</strong></td>
<td>情報消去に必要な理論下限エネルギーです。</td>
<td>論理操作の下限であり、脳全体の散逸をそれだけで表せるわけではありません。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="two-costs">
<h2 class="section-title">論理コストと散逸コストは別物</h2>
<table class="data-table">
<thead>
<tr>
<th>コスト</th>
<th>何を見るか</th>
<th>例</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>論理コスト</strong></td>
<td>何回計算したか。</td>
<td>FLOPs、メモリアクセス。</td>
</tr>
<tr>
<td><strong>散逸コスト</strong></td>
<td>どれだけ不可逆にエネルギーを使ったか。</td>
<td>EPR、通信対計算のエネルギー比。</td>
</tr>
</tbody>
</table>
<p>
Mind-Upload が両者を分けるのは、計算量が同じでも、物理的な実装のされ方で系の性質が変わる可能性があるからです。
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
<td><strong>脳に必要な散逸条件</strong><br>どの程度の EPR や NESS が本質か。</td>
<td>脳全体の散逸と意識状態の対応がまだ限定的だからです。</td>
<td>物理要件を強く言い切れません。</td>
<td>実装基盤の比較軸が増えます。</td>
</tr>
<tr>
<td><strong>EPR の実測法</strong><br>神経データからどう安定に推定するか。</td>
<td>観測ノイズ、非定常性、代理指標の多さがあるからです。</td>
<td>ベンチに組み込みにくいです。</td>
<td>物理的整合性を比較可能にできます。</td>
</tr>
<tr>
<td><strong>熱力学と本人性の関係</strong><br>散逸条件が意識や連続性にどこまで効くか。</td>
<td>情報論的指標との橋渡しが未完成だからです。</td>
<td>L4 以降への接続が弱いです。</td>
<td>物理基盤と主観的主張をつなぐ補助線になります。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-it-matters">
<h2 class="section-title">このページが分かると何が進むか</h2>
<div class="key-points">
<h4>Practical Gain</h4>
<ul>
<li>熱力学要件が、単なる計算量議論ではないと分かります。</li>
<li>基盤比較に、物理的コストという軸を追加できます。</li>
<li>理論・実装・検証をつなぐ補助指標として EPR を位置づけられます。</li>
</ul>
</div>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>関連Wiki</h4>
<ul>
<li><a href="{{ '/wiki/neuromorphic-hardware.html' | relative_url }}">ニューロモルフィック基盤 →</a></li>
<li><a href="{{ '/wiki/consciousness-theory-comparison.html' | relative_url }}">意識理論比較 →</a></li>
<li><a href="{{ '/wiki/pci-and-perturbation.html' | relative_url }}">PCI と摂動応答 →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Related U</h4>
<ul>
<li><a href="{{ '/wiki/u10-thermodynamic-consistency.html' | relative_url }}">U10 熱力学的一貫性 →</a></li>
<li><a href="{{ '/wiki/u8-closed-loop-stability.html' | relative_url }}">U8 閉ループ安定性 →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>元ページ</h4>
<ul>
<li><a href="{{ '/verification.html#thermodynamic-verification' | relative_url }}">Verification: 熱力学的検証要件 →</a></li>
<li><a href="{{ '/tech_roadmap.html#qa-i9' | relative_url }}">Roadmap: I9 →</a></li>
<li><a href="{{ '/idea.html' | relative_url }}">Framework →</a></li>
</ul>
</div>

</aside>
</main>
