---
layout: default
title: "クレーム階段"
description: "L0〜L5の主張レベルを、必要証拠・典型的な言い過ぎ・未解決点と合わせて整理します。"
article_type: Wiki
subtitle: "どこまで言ってよいかを先に固定する"
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
クレーム階段は、研究成果を<strong>どの強さの主張として言ってよいか</strong>をそろえる仕組みです。これがないと、L1 のデコーディング結果を L4 の本人性のように語る「すり替え」が起きやすくなります。
</p>
</div>

<section class="section" id="levels">
<h2 class="section-title">L0〜L5 を一度に見る</h2>
<table class="data-table">
<thead>
<tr>
<th>レベル</th>
<th>最低限の意味</th>
<th>必要証拠</th>
<th>まだ言ってはいけないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>L0</strong></td>
<td>再現可能な解析がある</td>
<td>データ、コード、環境、ログ、失敗例</td>
<td>「脳を読めた」「意識を扱えた」</td>
</tr>
<tr>
<td><strong>L1</strong></td>
<td>神経信号から状態や刺激を予測できる</td>
<td>ベースライン比較、リーク検査、汎化評価</td>
<td>「内部状態を再現した」</td>
</tr>
<tr>
<td><strong>L2</strong></td>
<td>条件変更や介入に対する予測ができる</td>
<td>反事実テスト、介入応答、分布外評価</td>
<td>「本人性が保存された」</td>
</tr>
<tr>
<td><strong>L3</strong></td>
<td>閉ループで安定に動く</td>
<td>長期安定性、制御破綻の監査、リアルタイム性能</td>
<td>「意識の同一性が証明された」</td>
</tr>
<tr>
<td><strong>L4</strong></td>
<td>本人性や連続性に関する事前登録テストを通る</td>
<td>記憶・価値観・学習・摂動応答の継続評価</td>
<td>「法的に完全な本人である」</td>
</tr>
<tr>
<td><strong>L5</strong></td>
<td>社会運用まで含めて扱える</td>
<td>権利、安全、停止権、監査制度、責任分担</td>
<td>これ以上の強い主張はありません</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-skips-happen">
<h2 class="section-title">なぜレベル飛ばしが起きるのか</h2>
<div class="key-points">
<h4>Typical Failure</h4>
<ul>
<li><strong>L0 → L4 の飛躍：</strong>再現可能な解析があるだけで、本人性の議論へ進んでしまう。</li>
<li><strong>L1 → L3 の飛躍：</strong>高い分類精度を、閉ループ制御の成功と混同してしまう。</li>
<li><strong>L2 → L5 の飛躍：</strong>介入予測が当たることを、社会実装可能性と読み替えてしまう。</li>
</ul>
</div>
<p>
この飛躍が起きる理由は、派手な成果ほど強い言葉で語りたくなる一方で、必要証拠がレベルごとに違うからです。クレーム階段は、成果の価値を下げるためではなく、<strong>価値を正しく言うため</strong>にあります。
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
<td><strong>L1 と L2 の境界</strong><br>どこから因果的予測と呼べるか。</td>
<td>高性能な相関モデルが、介入に弱い場合でも見かけ上は強く見えるからです。</td>
<td>decode と emulate の区別が曖昧になります。</td>
<td>モデルの達成度をより厳密に比較できます。</td>
</tr>
<tr>
<td><strong>L3 の合格条件</strong><br>どれくらい安定なら閉ループ成功か。</td>
<td>短時間の安定と長期安定で意味が違い、課題依存性も大きいからです。</td>
<td>制御系の成果を過大評価しやすいです。</td>
<td>実装段階の停止条件を先に決められます。</td>
</tr>
<tr>
<td><strong>L4 のテスト設計</strong><br>本人性や連続性を何で測るか。</td>
<td>自然科学だけで決まらず、哲学や法の前提が入るからです。</td>
<td>強い主張の検証が止まりやすいです。</td>
<td>本人性の議論を、少なくとも比較可能なテストへ落とせます。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-it-matters">
<h2 class="section-title">このページが分かると何が進むか</h2>
<div class="key-points">
<h4>Practical Gain</h4>
<ul>
<li>研究成果を、言い過ぎずに強く説明できます。</li>
<li>どの証拠が次のレベルへ必要かを整理できます。</li>
<li>レビュー時に、成果そのものより「主張の強さ」を監査できます。</li>
</ul>
</div>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>関連Wiki</h4>
<ul>
<li><a href="{{ '/wiki/wbe-basics.html' | relative_url }}">WBEの基礎 →</a></li>
<li><a href="{{ '/wiki/decode-vs-emulate.html' | relative_url }}">decode と emulate →</a></li>
<li><a href="{{ '/wiki/identity-and-ethics.html' | relative_url }}">本人性と倫理 →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Related U</h4>
<ul>
<li><a href="{{ '/wiki/u0-operational-identity.html' | relative_url }}">U0 操作的同一性 →</a></li>
<li><a href="{{ '/wiki/u4-counterfactual-equivalence.html' | relative_url }}">U4 因果同値 →</a></li>
<li><a href="{{ '/wiki/u12-branching-identity.html' | relative_url }}">U12 分岐本人性 →</a></li>
<li><a href="{{ '/wiki/u13-imitation-separation.html' | relative_url }}">U13 模倣分離 →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>元ページ</h4>
<ul>
<li><a href="{{ '/wbe_101.html#claim-ladder' | relative_url }}">WBE入門: クレーム階段 →</a></li>
<li><a href="{{ '/tech_roadmap.html#qa-p1' | relative_url }}">Roadmap: P1 →</a></li>
<li><a href="{{ '/verification.html' | relative_url }}">Verification →</a></li>
</ul>
</div>

</aside>
</main>
