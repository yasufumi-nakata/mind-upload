---
layout: default
title: "WBEの基礎"
description: "マインドアップロード、WBE、クレーム階段、decode と emulate の違いを初歩から整理します。"
article_type: Wiki
subtitle: "まず『何を達成したいのか』を言い直す"
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
WBE の議論が難しくなる最大の理由は、<strong>「何を再現したいのか」</strong>が曖昧なまま話が進みやすいからです。Mind-Upload では、まず主張の強さを分け、decode と emulate を分け、最後に本人性のような強い主張へ進みます。
</p>
</div>

<section class="section" id="terms">
<h2 class="section-title">最初にそろえる4語</h2>
<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>初歩的な説明</th>
<th>Mind-Uploadでの意味</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>マインドアップロード</strong></td>
<td>心や記憶を別の基盤へ移せるか、という大きな問いです。</td>
<td>広い一般名です。強い主張を直接せず、下位の検証課題に分解します。</td>
</tr>
<tr>
<td><strong>WBE</strong></td>
<td>Whole Brain Emulation。脳の機能を別の計算基盤で再現する試みです。</td>
<td>「どの機能を」「どの精度で」再現するかを操作的に定義して扱います。</td>
</tr>
<tr>
<td><strong>クレーム階段</strong></td>
<td>主張の強さを段階で分ける整理法です。</td>
<td>L0〜L5 で、再現可能な解析から社会実装までを分けます。</td>
</tr>
<tr>
<td><strong>Verification Commons</strong></td>
<td>比較可能な研究にするための共通土台です。</td>
<td>データ、評価、事前登録、監査をまとめて公開する構想です。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="claim-ladder">
<h2 class="section-title">なぜクレーム階段が必要か</h2>
<p>
「脳活動から文章が出た」「人らしい応答が返った」という事実だけでは、WBE に必要な意味での再現とは限りません。そこで、Mind-Upload では次のように段階を分けます。
</p>
<div class="key-points">
<h4>Claim Levels</h4>
<ul>
<li><strong>L0：</strong>同じ解析を第三者が再現できる</li>
<li><strong>L1：</strong>神経信号から状態や刺激を予測できる</li>
<li><strong>L2：</strong>条件変更に対する予測や介入応答を当てられる</li>
<li><strong>L3：</strong>閉ループで安定に動く</li>
<li><strong>L4：</strong>本人性や連続性のテストに進む</li>
<li><strong>L5：</strong>法・安全・運用まで含める</li>
</ul>
</div>
<p>
この分け方の利点は、<strong>今どのレベルの話をしているか</strong>を明示できることです。L1 の成果を L4 の言葉で宣伝しないための安全装置でもあります。
</p>
<div class="cta-box">
<h4>Deep Dive</h4>
<p>レベルごとの必要証拠と言い過ぎ例を分けて読む場合は、<a href="{{ '/wiki/claim-ladder.html' | relative_url }}">クレーム階段</a> を参照してください。</p>
</div>
</section>

<section class="section" id="decode-emulate">
<h2 class="section-title">decode と emulate は何が違うか</h2>
<table class="data-table">
<thead>
<tr>
<th>観点</th>
<th>Decode</th>
<th>Emulate</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>役割</strong></td>
<td>観測された信号を翻訳する</td>
<td>内部状態を持ち、自分で将来の出力を生成する</td>
</tr>
<tr>
<td><strong>強い点</strong></td>
<td>評価しやすい、現状技術で進めやすい</td>
<td>WBEの核心に近い</td>
</tr>
<tr>
<td><strong>弱い点</strong></td>
<td>相関に留まりやすい</td>
<td>検証設計が難しい</td>
</tr>
<tr>
<td><strong>必要なテスト</strong></td>
<td>汎化、リーク検査、ベースライン比較</td>
<td>介入、反事実、閉ループ、長期安定性</td>
</tr>
</tbody>
</table>
<div class="cta-box">
<h4>Deep Dive</h4>
<p>この差をもっと詳しく追う場合は、<a href="{{ '/wiki/decode-vs-emulate.html' | relative_url }}">decode と emulate</a> と <a href="{{ '/wiki/causal-verification.html' | relative_url }}">因果検証</a> が対応しています。</p>
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
<td><strong>復元対象</strong><br>記憶、行動傾向、因果構造、主観経験のどれを必須とするか。</td>
<td>分野ごとに成功条件が違い、単一の合意がありません。</td>
<td>ロードマップと評価指標がぶれます。</td>
<td>「何を満たしたら前進か」を先に固定できます。</td>
</tr>
<tr>
<td><strong>機能的等価性と意識の関係</strong><br>同じ機能なら同じ意識と言えるか。</td>
<td>経験の同一性を直接観測する方法がありません。</td>
<td>L4 以降の強い主張が検証しにくいです。</td>
<td>WBE の成功条件を哲学と工学の両面で狭められます。</td>
</tr>
<tr>
<td><strong>本人性の連続性</strong><br>コピーと段階的移行を同じに扱えるか。</td>
<td>心理的連続性、生物学的連続性、プロセス連続性が競合します。</td>
<td>どの方式を採用するかで設計が変わります。</td>
<td>スキャン型と段階移行型を比較評価できます。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-it-matters">
<h2 class="section-title">このページが分かると何が進むか</h2>
<div class="key-points">
<h4>Practical Gain</h4>
<ul>
<li>強い言葉に引っ張られず、成果のレベルを見分けられます。</li>
<li>「面白い結果」と「WBEに必要な結果」を分けて読めます。</li>
<li>後続の計測・モデル・倫理の議論が、どの主張レベルを支えているか追跡できます。</li>
</ul>
</div>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>関連Wiki</h4>
<ul>
<li><a href="{{ '/wiki/claim-ladder.html' | relative_url }}">クレーム階段 →</a></li>
<li><a href="{{ '/wiki/decode-vs-emulate.html' | relative_url }}">decode と emulate →</a></li>
<li><a href="{{ '/wiki/modeling-basics.html' | relative_url }}">モデルと因果 →</a></li>
<li><a href="{{ '/wiki/identity-and-ethics.html' | relative_url }}">本人性と倫理 →</a></li>
<li><a href="{{ '/wiki/consciousness-basics.html' | relative_url }}">意識理論 →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>元ページ</h4>
<ul>
<li><a href="{{ '/wbe_101.html' | relative_url }}">WBE入門 →</a></li>
<li><a href="{{ '/verification.html' | relative_url }}">検証基盤 →</a></li>
<li><a href="{{ '/tech_roadmap.html#definition' | relative_url }}">Roadmap: 前進の定義 →</a></li>
<li><a href="{{ '/faq.html#q7' | relative_url }}">FAQ: コピー問題 →</a></li>
</ul>
</div>

</aside>
</main>
