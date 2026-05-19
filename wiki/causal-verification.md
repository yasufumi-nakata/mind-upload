---
layout: default
title: "因果検証"
description: "観察・介入・反事実の違いと、Mind-Uploadが因果的摂動プロトコルを必要とする理由を整理します。"
article_type: Wiki
subtitle: "『当たった』だけでなく『変えたらどうなるか』まで問う"
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
観察だけでは、「何が原因で何が結果か」は十分に分かりません。Mind-Upload が WBE に近い主張をするには、<strong>介入</strong>と<strong>反事実</strong>を含む検証が必要です。これが因果検証です。
</p>
</div>

<section class="section" id="ladder">
<h2 class="section-title">観察・介入・反事実の違い</h2>
<table class="data-table">
<thead>
<tr>
<th>段階</th>
<th>問い</th>
<th>例</th>
<th>限界</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>観察</strong></td>
<td>何と何が一緒に起きるか。</td>
<td>EEGから覚醒状態を推定する。</td>
<td>相関止まりです。</td>
</tr>
<tr>
<td><strong>介入</strong></td>
<td>条件を変えたら何が起きるか。</td>
<td>刺激強度を変えて応答差を見る。</td>
<td>介入の設計自体が難しいです。</td>
</tr>
<tr>
<td><strong>反事実</strong></td>
<td>実際には起きなかった別分岐ならどうなったか。</td>
<td>同じ内部状態で別刺激だったら、をモデルで比較する。</td>
<td>正解の取得が難しいです。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-needed">
<h2 class="section-title">なぜ WBE に因果検証が必要か</h2>
<p>
WBE が目指すのは、観測信号をうまく翻訳することではなく、内部状態がどのように将来を生むかを再現することです。そのため、Mind-Upload では <strong>Causal Perturbation Suite</strong> のような摂動ベースの検証を中心に置きます。
</p>
<div class="key-points">
<h4>Typical Tests</h4>
<ul>
<li><strong>入力摂動：</strong>刺激や課題条件の変更に対する応答一致。</li>
<li><strong>局所介入：</strong>TMS/tDCS 相当の局所変化に対する分岐比較。</li>
<li><strong>閉ループ摂動：</strong>制御系の入力を揺らして安定性と回復をみる。</li>
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
<td><strong>人間で取りうる介入の範囲</strong><br>どの摂動が十分に因果的か。</td>
<td>倫理・安全上、強い介入を自由に使えないからです。</td>
<td>Ground Truth が弱くなります。</td>
<td>現実的な実験設計の上限が見えます。</td>
</tr>
<tr>
<td><strong>反事実の識別可能性</strong><br>観測と介入だけで十分か。</td>
<td>脳は高次元で潜在変数が多く、完全観測できないからです。</td>
<td>因果モデルの正しさを言い切りにくいです。</td>
<td>必要な追加計測や仮定を明示できます。</td>
</tr>
<tr>
<td><strong>サロゲート摂動の妥当性</strong><br>TMS 以外の刺激を代用できるか。</td>
<td>摂動の物理的意味が異なると、同じテストにならないからです。</td>
<td>PCI系評価の移植に限界があります。</td>
<td>臨床・非侵襲系でも使える評価を増やせます。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-it-matters">
<h2 class="section-title">このページが分かると何が進むか</h2>
<div class="key-points">
<h4>Practical Gain</h4>
<ul>
<li>ベンチマークに介入や反事実が必要な理由を説明できます。</li>
<li>単なる相関モデルと、より強い生成モデルを区別できます。</li>
<li>Verification の評価スイートを、何に向けて設計しているか読み解けます。</li>
</ul>
</div>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>関連Wiki</h4>
<ul>
<li><a href="{{ '/wiki/decode-vs-emulate.html' | relative_url }}">decode と emulate →</a></li>
<li><a href="{{ '/wiki/modeling-basics.html' | relative_url }}">モデルと因果 →</a></li>
<li><a href="{{ '/wiki/pci-and-perturbation.html' | relative_url }}">PCI と摂動応答 →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Related U</h4>
<ul>
<li><a href="{{ '/wiki/u4-counterfactual-equivalence.html' | relative_url }}">U4 因果同値 →</a></li>
<li><a href="{{ '/wiki/u8-closed-loop-stability.html' | relative_url }}">U8 閉ループ安定性 →</a></li>
<li><a href="{{ '/wiki/u13-imitation-separation.html' | relative_url }}">U13 模倣分離 →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>元ページ</h4>
<ul>
<li><a href="{{ '/verification.html#causal-perturbation-suite' | relative_url }}">Verification: 因果的摂動スイート →</a></li>
<li><a href="{{ '/perspective.html#decoding-to-emulation-gap' | relative_url }}">Perspective: decode→emulate →</a></li>
<li><a href="{{ '/tech_roadmap.html#verification' | relative_url }}">Roadmap: 検証 →</a></li>
</ul>
</div>

</aside>
</main>
