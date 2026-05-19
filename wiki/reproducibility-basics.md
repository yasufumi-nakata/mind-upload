---
layout: default
title: "再現性とベンチ"
description: "Verification Commons、ベンチマーク、事前登録、モデルカード、監査ログを初歩から整理します。"
article_type: Wiki
subtitle: "『研究成果』を『比較可能な前進』へ変える基盤"
author: Mind Uploading Research Project
last_updated: "2026-03-06"
note: "Beginner-first"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>TL;DR</h2>
<p>
Mind-Upload が最初に作ろうとしているのは、完成した WBE ではなく、<strong>比較可能な研究を支える基盤</strong>です。データ標準、ベンチマーク、事前登録、モデルカード、監査ログがそろって初めて「前進した」と言えます。
</p>
</div>

<section class="section" id="components">
<h2 class="section-title">基盤を作る5つの部品</h2>
<table class="data-table">
<thead>
<tr>
<th>部品</th>
<th>初歩的な説明</th>
<th>ないと何が起きるか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>データ標準</strong></td>
<td>入力データとメタデータの置き方をそろえる。</td>
<td>同じ名目でも別物を比べてしまいます。</td>
</tr>
<tr>
<td><strong>ベンチマーク</strong></td>
<td>同じ条件で比較する共通テストです。</td>
<td>スコアが良くても前進か判断できません。</td>
</tr>
<tr>
<td><strong>事前登録</strong></td>
<td>評価指標や停止条件を先に固定する運用です。</td>
<td>都合の良い結果だけ報告しやすくなります。</td>
</tr>
<tr>
<td><strong>モデルカード</strong></td>
<td>性能だけでなく、弱点や失敗例も記録します。</td>
<td>何に強く何に弱いか見えません。</td>
</tr>
<tr>
<td><strong>監査ログ</strong></td>
<td>更新履歴、実行環境、失敗例を残します。</td>
<td>第三者が追試しにくくなります。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-it-matters">
<h2 class="section-title">なぜ土台づくりが先なのか</h2>
<p>
WBE のように主張が大きい分野では、評価基準が曖昧だと「すごそうなデモ」が積み上がるだけで終わりがちです。Mind-Upload が PDB、BIDS、PhysioNet、OSF の歴史を参照するのは、<strong>進歩を測れる状態</strong>を先に作った成功例だからです。
</p>
<div class="cta-box">
<h4>Deep Dive</h4>
<p>入力標準は <a href="{{ '/wiki/bids-and-eeg-bids.html' | relative_url }}">BIDS / EEG-BIDS</a>、出力評価は <a href="{{ '/wiki/causal-verification.html' | relative_url }}">因果検証</a>、主張の強さは <a href="{{ '/wiki/claim-ladder.html' | relative_url }}">クレーム階段</a>、反証のルールは <a href="{{ '/wiki/falsification-and-stop-rules.html' | relative_url }}">反証条件と停止規則</a>、文献導線は <a href="{{ '/wiki/literature-and-evidence-map.html' | relative_url }}">文献導線と証拠地図</a>、運用上の事故は <a href="{{ '/wiki/failure-modes.html' | relative_url }}">失敗様式カタログ</a> と <a href="{{ '/wiki/benchmark-pitfalls.html' | relative_url }}">ベンチマークの罠</a> で詳述しています。</p>
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
<td><strong>良いベンチの定義</strong><br>何を測れば WBE に近い前進を反映するか。</td>
<td>スコアが高いことと、因果的に正しいことが一致しないからです。</td>
<td>Goodhart の罠で、ベンチ最適化が目的化します。</td>
<td>研究の方向を誤らない物差しを作れます。</td>
</tr>
<tr>
<td><strong>公開とプライバシーの両立</strong><br>脳データをどこまで共有できるか。</td>
<td>神経データは個人識別や機微情報を含みうるからです。</td>
<td>オープンサイエンスと保護義務が衝突します。</td>
<td>安全に共有可能な運用基準を作れます。</td>
</tr>
<tr>
<td><strong>クロスラボ再現性</strong><br>施設が違っても比較可能か。</td>
<td>計測機器、刺激条件、前処理文化がラボごとに違うからです。</td>
<td>同じベンチでも本当は別条件になりがちです。</td>
<td>単発成功でなく、持続的な進歩を評価できます。</td>
</tr>
<tr>
<td><strong>失敗の公開ルール</strong><br>どこまでネガティブ結果を残すべきか。</td>
<td>研究文化として成功例が優先されやすいからです。</td>
<td>同じ失敗が繰り返されます。</td>
<td>分野全体の探索コストを下げられます。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-it-matters-2">
<h2 class="section-title">このページが分かると何が進むか</h2>
<div class="key-points">
<h4>Practical Gain</h4>
<ul>
<li>なぜ Mind-Upload が『実験結果そのもの』より『比較のルール』を重視するか説明できます。</li>
<li>データ収集、モデル開発、倫理運用が同じ基盤上でつながります。</li>
<li>既存分野の成功パターンを、WBE にどう移植するか考えやすくなります。</li>
</ul>
</div>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>関連Wiki</h4>
<ul>
<li><a href="{{ '/wiki/bids-and-eeg-bids.html' | relative_url }}">BIDS / EEG-BIDS →</a></li>
<li><a href="{{ '/wiki/causal-verification.html' | relative_url }}">因果検証 →</a></li>
<li><a href="{{ '/wiki/claim-ladder.html' | relative_url }}">クレーム階段 →</a></li>
<li><a href="{{ '/wiki/benchmark-pitfalls.html' | relative_url }}">ベンチマークの罠 →</a></li>
<li><a href="{{ '/wiki/falsification-and-stop-rules.html' | relative_url }}">反証条件と停止規則 →</a></li>
<li><a href="{{ '/wiki/literature-and-evidence-map.html' | relative_url }}">文献導線と証拠地図 →</a></li>
<li><a href="{{ '/wiki/failure-modes.html' | relative_url }}">失敗様式カタログ →</a></li>
<li><a href="{{ '/wiki/measurement-basics.html' | relative_url }}">計測とデータ →</a></li>
<li><a href="{{ '/wiki/modeling-basics.html' | relative_url }}">モデルと因果 →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>元ページ</h4>
<ul>
<li><a href="{{ '/verification.html' | relative_url }}">Verification →</a></li>
<li><a href="{{ '/datasets.html' | relative_url }}">データ&ベンチ →</a></li>
<li><a href="{{ '/casework.html' | relative_url }}">ケースワーク →</a></li>
<li><a href="{{ '/hands_on.html' | relative_url }}">ハンズオン →</a></li>
</ul>
</div>

</aside>
</main>
