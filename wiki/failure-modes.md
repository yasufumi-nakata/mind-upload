---
layout: default
title: "失敗様式カタログ"
description: "Mind-Upload 研究で繰り返し起こる失敗の型を、原因・兆候・対策で整理したカタログです。"
article_type: Wiki
subtitle: "失敗の型を先に知っておくと、進歩を見誤りにくい"
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
Mind-Upload では、失敗は単に「性能が低かった」では終わりません。<strong>同じスコアでも、どの型の失敗かで意味が変わります</strong>。このページでは、典型的な失敗様式を、兆候、隠れた原因、効く対策で整理します。
</p>
</div>

<section class="section" id="catalog">
<h2 class="section-title">代表的な失敗様式</h2>
<table class="data-table">
<thead>
<tr>
<th>失敗様式</th>
<th>表面上の症状</th>
<th>隠れた原因</th>
<th>主に効くページ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>リーク成功</strong></td>
<td>評価スコアだけ異常に高い</td>
<td>前処理、分割、メタデータ経由で正解が漏れている</td>
<td><a href="{{ '/wiki/benchmark-pitfalls.html' | relative_url }}">ベンチマークの罠</a></td>
</tr>
<tr>
<td><strong>模倣成功</strong></td>
<td>行動や出力は似るが介入応答が違う</td>
<td>表面的な相関だけを拾っている</td>
<td><a href="{{ '/wiki/u13-imitation-separation.html' | relative_url }}">U13 模倣分離</a></td>
</tr>
<tr>
<td><strong>座標ずれ成功</strong></td>
<td>マルチモーダル統合が不安定</td>
<td>同期誤差、座標系不一致、装置差</td>
<td><a href="{{ '/wiki/u7-multimodal-alignment.html' | relative_url }}">U7 マルチモーダル整合</a></td>
</tr>
<tr>
<td><strong>短期成功・長期破綻</strong></td>
<td>短時間の閉ループは動くが持続しない</td>
<td>遅延、ドリフト、適応則の不安定</td>
<td><a href="{{ '/wiki/u8-closed-loop-stability.html' | relative_url }}">U8 閉ループ安定性</a></td>
</tr>
<tr>
<td><strong>高性能・高散逸</strong></td>
<td>精度は高いがコストや散逸が過大</td>
<td>熱力学制約や運用コストを指標に入れていない</td>
<td><a href="{{ '/wiki/u10-thermodynamic-consistency.html' | relative_url }}">U10 熱力学的一貫性</a></td>
</tr>
<tr>
<td><strong>制度未接続</strong></td>
<td>技術主張はあるが運用に乗らない</td>
<td>同意、監査、権利、責任分担が未整備</td>
<td><a href="{{ '/wiki/u15-governance-integration.html' | relative_url }}">U15 社会実装ガバナンス</a></td>
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
<td><strong>失敗様式の標準語彙</strong><br>同じ失敗を分野横断で同じ名前で呼べるか。</td>
<td>信号処理、ML、哲学、制度で失敗の見え方が違うからです。</td>
<td>ネガティブ結果を比較可能な資産へ変えられます。</td>
</tr>
<tr>
<td><strong>早期兆候の定量化</strong><br>破綻前に何を見れば危険を察知できるか。</td>
<td>多くの系で失敗が徐々にではなく急に現れるからです。</td>
<td>閉ループや長期追跡の安全性を高められます。</td>
</tr>
<tr>
<td><strong>失敗からの復旧条件</strong><br>どの失敗が修復可能で、どれが主張撤回を要するか。</td>
<td>技術的失敗と概念的失敗が混在するからです。</td>
<td>停止規則と再挑戦条件を分けて設計できます。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="mitigation">
<h2 class="section-title">最低限の対処原則</h2>
<div class="key-points">
<h4>Safeguards</h4>
<ul>
<li><strong>失敗名を付ける：</strong>単なる「再現失敗」ではなく、どの型かを分類します。</li>
<li><strong>対照を増やす：</strong>シャム、OOD、クロスラボ、長期追跡を使い分けます。</li>
<li><strong>公開粒度を上げる：</strong>成功条件だけでなく、壊れた条件も記録します。</li>
<li><strong>主張を巻き戻す：</strong>失敗した型に応じて、L3 から L2 へ戻すなど主張を明確に弱めます。</li>
</ul>
</div>
</section>

<section class="section" id="why-it-matters">
<h2 class="section-title">このページが分かると何が進むか</h2>
<div class="key-points">
<h4>Practical Gain</h4>
<ul>
<li>失敗を単発の不運ではなく、再発防止の知識へ変えられます。</li>
<li>ベンチ設計と停止規則を、失敗の型から逆算できます。</li>
<li>未解決問題ページの反証条件を、具体的な現象として読みやすくなります。</li>
</ul>
</div>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>関連Wiki</h4>
<ul>
<li><a href="{{ '/wiki/benchmark-pitfalls.html' | relative_url }}">ベンチマークの罠 →</a></li>
<li><a href="{{ '/wiki/falsification-and-stop-rules.html' | relative_url }}">反証条件と停止規則 →</a></li>
<li><a href="{{ '/wiki/minimum-experiment-designs.html' | relative_url }}">最小実験設計 →</a></li>
<li><a href="{{ '/wiki/unsolved-questions.html' | relative_url }}">未解決問題カタログ →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>元ページ</h4>
<ul>
<li><a href="{{ '/casework.html' | relative_url }}">ケースワーク →</a></li>
<li><a href="{{ '/verification.html' | relative_url }}">Verification →</a></li>
<li><a href="{{ '/faq.html#q5' | relative_url }}">FAQ: ベンチマークの罠 →</a></li>
</ul>
</div>

</aside>
</main>
