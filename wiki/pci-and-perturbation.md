---
layout: default
title: "PCI と摂動応答"
description: "PCI / PCI-ST が何を測っているか、なぜ意識指標として使われるか、どこに限界があるかを整理します。"
article_type: Wiki
subtitle: "『複雑さ』を、摂動で測る"
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
PCI は、脳に摂動を与えたときの応答が、どれだけ<strong>広く・複雑に・まとまりを持って伝わるか</strong>を測る指標です。Mind-Upload では、理論そのものより、こうした摂動応答の比較可能性を重視します。
</p>
</div>

<section class="section" id="what-it-is">
<h2 class="section-title">PCI / PCI-ST とは何か</h2>
<table class="data-table">
<thead>
<tr>
<th>指標</th>
<th>ざっくりした意味</th>
<th>典型的な使い方</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>PCI</strong></td>
<td>TMS などの摂動後に、脳活動がどれだけ統合されつつ複雑かを見る。</td>
<td>覚醒、睡眠、麻酔、意識障害の比較。</td>
</tr>
<tr>
<td><strong>PCI-ST</strong></td>
<td>状態遷移の複雑性を、より高速・一般的に扱う派生手法。</td>
<td>実務上の比較や拡張指標として利用。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-useful">
<h2 class="section-title">なぜ有用なのか</h2>
<p>
単に脳が活動しているだけでは、意識の有無やレベルを十分に区別できません。PCI 系は、<strong>外から揺らしたときに、どれだけ豊かに応答できるか</strong>を測るため、静的な相関指標より強い検証力を持ちます。
</p>
</section>

<section class="section" id="limits">
<h2 class="section-title">何が分かり、何が分からないか</h2>
<table class="data-table">
<thead>
<tr>
<th>分かりやすいこと</th>
<th>分かりにくいこと</th>
</tr>
</thead>
<tbody>
<tr>
<td>脳状態の違いによる応答複雑性の差</td>
<td>主観経験の質そのもの</td>
</tr>
<tr>
<td>摂動に対する反応の広がりと統合性</td>
<td>本人性や価値観の連続性</td>
</tr>
<tr>
<td>行動報告に頼りすぎない比較</td>
<td>どの意識理論が正しいかの最終判定</td>
</tr>
</tbody>
</table>
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
<td><strong>PCI と主観経験の対応</strong><br>高い PCI が何をどこまで意味するか。</td>
<td>主観経験を第三者が直接参照できないからです。</td>
<td>指標の解釈を強く言い切れません。</td>
<td>理論非依存な合否指標として使いやすくなります。</td>
</tr>
<tr>
<td><strong>スカラー値の限界</strong><br>値が同じでも内部構造が違う可能性。</td>
<td>複雑さの総量だけでは、質的な構造差を潰してしまうからです。</td>
<td>生体脳とエミュレーションの比較が粗くなります。</td>
<td>空間分布や位相構造を追加する方向が見えます。</td>
</tr>
<tr>
<td><strong>摂動手法の移植可能性</strong><br>TMS 以外でどこまで代用できるか。</td>
<td>摂動の物理意味と可達部位が違うからです。</td>
<td>非侵襲・低負荷な評価へ展開しにくいです。</td>
<td>より多くのデータセットで評価できます。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-it-matters">
<h2 class="section-title">このページが分かると何が進むか</h2>
<div class="key-points">
<h4>Practical Gain</h4>
<ul>
<li>なぜ Mind-Upload が PCI 系を重視するか理解できます。</li>
<li>理論争いと経験指標の役割分担が明確になります。</li>
<li>意識レベルの評価と、本人性の評価を混同しにくくなります。</li>
</ul>
</div>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>関連Wiki</h4>
<ul>
<li><a href="{{ '/wiki/consciousness-basics.html' | relative_url }}">意識理論 →</a></li>
<li><a href="{{ '/wiki/causal-verification.html' | relative_url }}">因果検証 →</a></li>
<li><a href="{{ '/wiki/consciousness-theory-comparison.html' | relative_url }}">意識理論比較 →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Related U</h4>
<ul>
<li><a href="{{ '/wiki/u11-consciousness-metric-approximation.html' | relative_url }}">U11 IIT近似の妥当性 →</a></li>
<li><a href="{{ '/wiki/u4-counterfactual-equivalence.html' | relative_url }}">U4 因果同値 →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>元ページ</h4>
<ul>
<li><a href="{{ '/eeg_101.html#information-theoretic-limits' | relative_url }}">EEG入門: 情報理論的限界 →</a></li>
<li><a href="{{ '/verification.html#causal-perturbation-suite' | relative_url }}">Verification: 摂動スイート →</a></li>
<li><a href="{{ '/perspective.html#eeg-consciousness-roadmap' | relative_url }}">Perspective: EEGで意識を測る →</a></li>
</ul>
</div>

</aside>
</main>
