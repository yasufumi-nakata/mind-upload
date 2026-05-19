---
layout: default
title: "モデルと因果"
description: "デコーディング、生成モデル、反事実、介入、閉ループを初歩から整理し、相関から因果へ進む難しさを説明します。"
article_type: Wiki
subtitle: "『当てる』から『なぜそうなるか』へ"
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
モデル化の難しさは、<strong>よく当たる予測器</strong>と<strong>本当に中身を表しているモデル</strong>が別物である点にあります。Mind-Upload では、デコーディングで終わらず、介入や反事実でモデルを崩しにいく設計を重視します。
</p>
</div>

<section class="section" id="ladder">
<h2 class="section-title">モデル化の階段</h2>
<table class="data-table">
<thead>
<tr>
<th>段階</th>
<th>何をするか</th>
<th>主な落とし穴</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>ベースライン</strong></td>
<td>単純な規則や既存手法と比べる</td>
<td>比較相手が弱すぎる</td>
</tr>
<tr>
<td><strong>デコーディング</strong></td>
<td>信号から状態や刺激を当てる</td>
<td>相関を因果と誤認する</td>
</tr>
<tr>
<td><strong>生成モデル</strong></td>
<td>将来の状態や未学習条件を予測する</td>
<td>分布外条件で壊れる</td>
</tr>
<tr>
<td><strong>因果モデル</strong></td>
<td>介入したらどう変わるかを表現する</td>
<td>反事実の正解が取りにくい</td>
</tr>
<tr>
<td><strong>閉ループ</strong></td>
<td>出力が次の入力へ戻る系を安定に動かす</td>
<td>短期的に当たっても長期安定しない</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="terms">
<h2 class="section-title">基礎語を短く押さえる</h2>
<div class="key-points">
<h4>Key Terms</h4>
<ul>
<li><strong>反事実：</strong>「もし条件を変えたらどうなったか」を問う考え方です。</li>
<li><strong>介入：</strong>刺激や入力条件を意図的に変え、応答の差を測ることです。</li>
<li><strong>SCM：</strong>構造的因果モデル。原因と結果の関係を明示しやすい枠組みです。</li>
<li><strong>DCM：</strong>神経回路の結合と入力を仮定してデータに合わせる手法です。</li>
<li><strong>閉ループ：</strong>モデルの出力が次の環境や入力へ戻る動的システムです。</li>
</ul>
</div>
</section>

<section class="section" id="why-hard">
<h2 class="section-title">なぜ『高精度』だけでは足りないか</h2>
<p>
脳データの予測では、言語モデルの事前分布、課題の偏り、データリークでスコアが高く見えることがあります。WBE に近い主張をするには、<strong>条件を変えたときにも説明できるか</strong>が必要です。
</p>
<div class="note-box">
<strong>典型的な事故</strong>
<p>
訓練分布の中では文章再構成がうまくいっても、刺激条件や文脈が変わると崩れることがあります。これは「翻訳器」としては優秀でも、「内部状態を再現した」とは限らないことを意味します。
</p>
</div>
<div class="cta-box">
<h4>Deep Dive</h4>
<p>主張の境界は <a href="{{ '/wiki/decode-vs-emulate.html' | relative_url }}">decode と emulate</a>、検証設計は <a href="{{ '/wiki/causal-verification.html' | relative_url }}">因果検証</a>、最小比較の組み方は <a href="{{ '/wiki/minimum-experiment-designs.html' | relative_url }}">最小実験設計</a>、反証の考え方は <a href="{{ '/wiki/falsification-and-stop-rules.html' | relative_url }}">反証条件と停止規則</a>、因果モデルの具体形は <a href="{{ '/wiki/dcm-and-scm.html' | relative_url }}">DCM / SCM</a> で詳しく整理しています。</p>
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
<td><strong>どの内部状態をモデル化すべきか</strong><br>発火率、位相、結合、潜在状態のどれが本質か。</td>
<td>観測できる量が限られ、理論側の合意も弱いからです。</td>
<td>モデルの粒度選択が恣意的になります。</td>
<td>必要十分な表現を絞り込めます。</td>
</tr>
<tr>
<td><strong>反事実の正解</strong><br>介入したとき本来どうなるべきか。</td>
<td>脳では同じ個体に同じ条件を完全再現しにくいからです。</td>
<td>因果モデルの評価が難しいです。</td>
<td>decode と emulate の差を定量化できます。</td>
</tr>
<tr>
<td><strong>分布外一般化</strong><br>未知条件でも予測が保てるか。</td>
<td>学習データの偏りが大きく、真の環境変化を十分カバーできません。</td>
<td>実運用や閉ループで壊れやすいです。</td>
<td>より強い L2〜L3 の主張へ進めます。</td>
</tr>
<tr>
<td><strong>モデルの解釈可能性</strong><br>高性能モデルが何を使っているか。</td>
<td>深層モデルや大規模言語モデルの寄与を切り分けにくいからです。</td>
<td>脳由来の情報量を誤認しやすいです。</td>
<td>本当に脳から取れた情報を見積もれます。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-it-matters">
<h2 class="section-title">このページが分かると何が進むか</h2>
<div class="key-points">
<h4>Practical Gain</h4>
<ul>
<li>単なる高スコアを、過剰に WBE の前進と読まなくなります。</li>
<li>どの実験が因果検証に向いているかを見積もれます。</li>
<li>Verification のベンチ設計が、なぜ反事実と閉ループを重視するか理解できます。</li>
</ul>
</div>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>関連Wiki</h4>
<ul>
<li><a href="{{ '/wiki/decode-vs-emulate.html' | relative_url }}">decode と emulate →</a></li>
<li><a href="{{ '/wiki/causal-verification.html' | relative_url }}">因果検証 →</a></li>
<li><a href="{{ '/wiki/dcm-and-scm.html' | relative_url }}">DCM / SCM →</a></li>
<li><a href="{{ '/wiki/minimum-experiment-designs.html' | relative_url }}">最小実験設計 →</a></li>
<li><a href="{{ '/wiki/falsification-and-stop-rules.html' | relative_url }}">反証条件と停止規則 →</a></li>
<li><a href="{{ '/wiki/wbe-basics.html' | relative_url }}">WBEの基礎 →</a></li>
<li><a href="{{ '/wiki/measurement-basics.html' | relative_url }}">計測とデータ →</a></li>
<li><a href="{{ '/wiki/reproducibility-basics.html' | relative_url }}">再現性とベンチ →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>元ページ</h4>
<ul>
<li><a href="{{ '/verification.html#deliverables' | relative_url }}">Verification: 成果物 →</a></li>
<li><a href="{{ '/tech_roadmap.html#reconstruction' | relative_url }}">Roadmap: 再構成 →</a></li>
<li><a href="{{ '/perspective.html#decoding-to-emulation-gap' | relative_url }}">Perspective: decode→emulate →</a></li>
<li><a href="{{ '/faq.html#q2' | relative_url }}">FAQ: decode と emulate →</a></li>
</ul>
</div>

</aside>
</main>
