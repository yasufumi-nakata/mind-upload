---
layout: default
title: "ベンチマークの罠"
description: "Goodhartの罠、データリーク、過学習、運用乖離、リーダーボード最適化を整理します。"
article_type: Wiki
subtitle: "『スコアが高い』と『前進した』は同じではない"
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
ベンチマークの罠とは、指標に勝つことが本来の目的とずれていく現象です。Mind-Upload では、WBE に近い主張ほどこの罠が危険になるため、<strong>失敗例、リーク検査、モデルカード、事前登録</strong>をセットで運用します。
</p>
</div>

<section class="section" id="patterns">
<h2 class="section-title">典型的な罠</h2>
<table class="data-table">
<thead>
<tr>
<th>罠</th>
<th>何が起きるか</th>
<th>なぜ危険か</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>データリーク</strong></td>
<td>訓練情報が評価に混ざる。</td>
<td>性能が高く見えても再現不能です。</td>
</tr>
<tr>
<td><strong>過学習</strong></td>
<td>ベンチ固有の癖だけに適応する。</td>
<td>未知条件で壊れます。</td>
</tr>
<tr>
<td><strong>代理目標化</strong></td>
<td>スコア改善そのものが目的化する。</td>
<td>WBE に必要な因果性や安定性が抜け落ちます。</td>
</tr>
<tr>
<td><strong>運用コスト無視</strong></td>
<td>高性能でも再利用不能な手法が勝つ。</td>
<td>公共財として積み上がりません。</td>
</tr>
<tr>
<td><strong>ネガティブ結果の欠落</strong></td>
<td>成功例だけが共有される。</td>
<td>同じ失敗が繰り返されます。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="countermeasures">
<h2 class="section-title">Mind-Upload が入れる防波堤</h2>
<div class="key-points">
<h4>Safeguards</h4>
<ul>
<li><strong>ベースライン固定：</strong>弱い比較相手で勝っただけを防ぐ。</li>
<li><strong>リーク検査：</strong>入力シャッフルや条件入れ替えを含める。</li>
<li><strong>モデルカード：</strong>失敗条件と既知の弱点を公開する。</li>
<li><strong>事前登録：</strong>評価指標と停止条件を後出ししない。</li>
<li><strong>クロスラボ再現：</strong>別環境でも評価可能かを見る。</li>
</ul>
</div>
<div class="cta-box">
<h4>Deep Dive</h4>
<p>失敗の型で整理したい場合は <a href="{{ '/wiki/failure-modes.html' | relative_url }}">失敗様式カタログ</a>、どこで主張を止めるかは <a href="{{ '/wiki/falsification-and-stop-rules.html' | relative_url }}">反証条件と停止規則</a>、最小の比較設計は <a href="{{ '/wiki/minimum-experiment-designs.html' | relative_url }}">最小実験設計</a> を参照してください。</p>
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
<td><strong>WBEに効く良い指標</strong><br>何を測れば本当の前進か。</td>
<td>高スコアと因果的妥当性が一致しないからです。</td>
<td>研究がスコア最適化へ流れやすいです。</td>
<td>分野全体の方向を誤りにくくなります。</td>
</tr>
<tr>
<td><strong>失敗共有の標準</strong><br>どこまでネガティブ結果を公開すべきか。</td>
<td>研究文化として成功偏重が強いからです。</td>
<td>同じ試行錯誤を再発します。</td>
<td>探索コストを削減できます。</td>
</tr>
<tr>
<td><strong>運用可能性の評価</strong><br>再現コストや監査コストをどう指標化するか。</td>
<td>性能指標に比べて定量化しにくいからです。</td>
<td>公共財として使えない手法が上位に来ます。</td>
<td>持続的に積み上がるベンチを作れます。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-it-matters">
<h2 class="section-title">このページが分かると何が進むか</h2>
<div class="key-points">
<h4>Practical Gain</h4>
<ul>
<li>スコアの上昇を、そのまま進歩と読まなくなります。</li>
<li>ベンチ設計と監査設計を一体で考えられます。</li>
<li>ケースワークがなぜ重要かを、より具体的に説明できます。</li>
</ul>
</div>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>関連Wiki</h4>
<ul>
<li><a href="{{ '/wiki/reproducibility-basics.html' | relative_url }}">再現性とベンチ →</a></li>
<li><a href="{{ '/wiki/causal-verification.html' | relative_url }}">因果検証 →</a></li>
<li><a href="{{ '/wiki/claim-ladder.html' | relative_url }}">クレーム階段 →</a></li>
<li><a href="{{ '/wiki/failure-modes.html' | relative_url }}">失敗様式カタログ →</a></li>
<li><a href="{{ '/wiki/falsification-and-stop-rules.html' | relative_url }}">反証条件と停止規則 →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Related U</h4>
<ul>
<li><a href="{{ '/wiki/u6-personalization-vs-generalization.html' | relative_url }}">U6 個人化と汎化 →</a></li>
<li><a href="{{ '/wiki/u9-ood-robustness.html' | relative_url }}">U9 OOD 頑健性 →</a></li>
<li><a href="{{ '/wiki/u13-imitation-separation.html' | relative_url }}">U13 模倣分離 →</a></li>
<li><a href="{{ '/wiki/u14-reproducibility-operations.html' | relative_url }}">U14 追試可能性 →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>元ページ</h4>
<ul>
<li><a href="{{ '/faq.html#q5' | relative_url }}">FAQ: ベンチマークの罠 →</a></li>
<li><a href="{{ '/casework.html#benchmarks' | relative_url }}">Casework: ベンチマーク →</a></li>
<li><a href="{{ '/verification.html' | relative_url }}">Verification →</a></li>
</ul>
</div>

</aside>
</main>
