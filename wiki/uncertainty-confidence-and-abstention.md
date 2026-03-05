---
layout: default
title: "Wiki：不確実性・信頼区間・棄権"
description: "点推定、信頼区間、信用区間、不確実性の伝播、低信頼時の棄権を初歩から説明します。"
article_type: Wiki
subtitle: "1つの数字だけを見て信じ切らないための補講"
author: Mind Uploading Research Project
last_updated: "2026-03-06"
note: "Learning guide"
audience: "不確実性の話で止まりやすい人、点推定だけの主張を読み違えたくない人"
reading_time: "10〜15分"
page_intro: "このページは、Mind-Upload で頻繁に出てくる『不確実性』『信頼区間』『信用区間』『不確実性の伝播』『棄権』を、初歩から整理する wiki です。数字が 1 つ出たときに、それをどこまで信じてよいかを見分ける足場を作ることが目的です。"
accuracy_note: "ここでは数理統計の厳密な定義より、読み方の実務を優先します。ただし『幅がある』『幅が次段階へ伝わる』『低信頼なら出力しない方がよい』という要点は曖昧にしません。"
page_highlights:
  - "点推定だけでは、どれくらい不安定かが分かりません。"
  - "信頼区間や信用区間は、結果の幅を示すための道具です。"
  - "低信頼時に無理に答えない『棄権』も、検証設計の一部です。"
known_points:
  - "観測、前処理、逆問題、モデル化のどこでも不確実性は生じます。"
  - "1つのスコアや推定値だけでは、結果の安定性や幅は分かりません。"
  - "不確実性を隠すより、明示して低信頼時に棄権する方が安全です。"
unknown_points:
  - "どの不確実性指標を全課題で標準化するかは、まだ運用設計の途中です。"
  - "どこまでの幅なら WBE 検証として許容できるかは、段階ごとに詰める必要があります。"
wiki_links:
  - label: "Wiki: 観測から推定へ"
    url: "/wiki/observation-to-estimation.html"
    description: "逆問題や推定モデルの不確実性へ戻れます。"
  - label: "Wiki: 検証基盤の基本"
    url: "/wiki/verification-basics.html"
    description: "不確実性を公開ルールへどう組み込むかを補います。"
  - label: "Wiki Home"
    url: "/wiki/"
    description: "他の基礎ページへ戻れます。"
recommended_pages:
  - label: "EEG入門"
    url: "/eeg_101.html"
  - label: "検証基盤"
    url: "/verification.html"
  - label: "研究ノート"
    url: "/perspective.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>いちばん短い説明</h2>
<p>
1つの数字だけ出されても、その結果がどれくらい安定かは分かりません。不確実性とは、「この結果にはどれくらい幅や揺れがあるか」を見える形で残すことです。
</p>
</div>

<section class="section" id="why-one-number-is-not-enough">
<h2 class="section-title">なぜ 1 つの数字だけでは足りないのか</h2>
<p>
たとえば、あるモデルが 80% の精度を出したとしても、その 80% が条件を少し変えても安定なのか、データが変わると大きく崩れるのかは、数字 1 つでは分かりません。ESI でも同様で、「この部位が活動した」と 1 点だけ示されても、その推定がどれくらい揺れうるかが見えません。
</p>
</section>

<section class="section" id="point-vs-interval">
<h2 class="section-title">点推定と区間の違い</h2>
<table class="data-table">
<thead>
<tr>
<th>見せ方</th>
<th>何が分かるか</th>
<th>何がまだ分からないか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>点推定</strong></td>
<td>いまの代表値が分かります。</td>
<td>どれくらい不安定か、どの範囲で揺れるかは見えません。</td>
</tr>
<tr>
<td><strong>区間付き</strong></td>
<td>代表値の周りに、どれくらい幅があるかが見えます。</td>
<td>幅の理由や、別段階への伝播までは追加説明が必要です。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="confidence-vs-credible">
<h2 class="section-title">信頼区間と信用区間を雑に混同しない</h2>
<p>
厳密には統計的な意味が異なりますが、初歩ではまず「<strong>推定値に幅を持たせる</strong>」という共通点を押さえると十分です。Mind-Upload の文脈では、どちらを使うにせよ、<strong>点だけで断言しない</strong>ことが重要です。
</p>
<div class="note-box">
<strong>初歩の読み方</strong>
<p>
ここではまず、「幅が狭いほど精密」「幅が広いほど不確か」という読み方で問題ありません。ただし、幅が広いから即座に間違いとは限らず、「まだ強く言えない」と読むのが安全です。
</p>
</div>
</section>

<section class="section" id="where-uncertainty-comes-from">
<h2 class="section-title">不確実性はどこで生まれるのか</h2>
<table class="data-table">
<thead>
<tr>
<th>段階</th>
<th>不確実性の例</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>観測</strong></td>
<td>ノイズ、同期ずれ、欠損、電極状態の揺れ。</td>
</tr>
<tr>
<td><strong>前処理</strong></td>
<td>参照法、フィルタ、除外閾値の選び方。</td>
</tr>
<tr>
<td><strong>逆問題・推定</strong></td>
<td>頭部モデル、導電率、ソース配置、代替モデル。</td>
</tr>
<tr>
<td><strong>評価</strong></td>
<td>データ分割、OOD 条件、摂動条件、ベースラインの置き方。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="propagation">
<h2 class="section-title">不確実性は次の段階へ伝わる</h2>
<p>
観測段階で生じた揺れは、前処理、推定、評価へそのまま影響します。たとえば、頭蓋骨の導電率が不確かなら、ESI の結果にも幅が出ます。そしてその幅は、後続の因果モデルや検証スコアにも伝わります。
</p>
<p>
このため、各段階で「ここまでは不確か」と書き残さないと、最後だけきれいな数字に見えてしまいます。
</p>
</section>

<section class="section" id="abstention">
<h2 class="section-title">棄権とは何か</h2>
<p>
棄権とは、「自信が低いときに無理に答えを出さない」設計です。これは弱気ではなく、<strong>不確実性を隠して誤答を出すより安全</strong>だから必要になります。
</p>
<div class="key-points">
<h4>棄権が役立つ場面</h4>
<ul>
<li><strong>脳信号由来の情報が弱いとき：</strong>LLM の補完だけでそれっぽく見える出力を防げます。</li>
<li><strong>ESI の幅が広すぎるとき：</strong>位置を断言しない方が安全です。</li>
<li><strong>OOD 条件で根拠が薄いとき：</strong>再計測や要追試へ回す判断ができます。</li>
</ul>
</div>
</section>

<section class="section" id="how-to-read">
<h2 class="section-title">不確実性の話を読むときの最低チェック</h2>
<div class="key-points">
<h4>Checklist</h4>
<ul>
<li><strong>点だけでなく幅があるか：</strong>区間、分布、集中度などが示されているか。</li>
<li><strong>どこ由来の不確実性か：</strong>観測、前処理、推定、評価のどこで生じたかが書かれているか。</li>
<li><strong>次段階へ伝播しているか：</strong>前段の揺れを後段で無視していないか。</li>
<li><strong>低信頼時の扱いがあるか：</strong>棄権、要再計測、要追試のルールがあるか。</li>
</ul>
</div>
</section>

<section class="section" id="return">
<h2 class="section-title">次にどこへ戻るか</h2>
<p>
EEG の具体例へ戻るなら <a href="../eeg_101.html">EEG入門</a>、公開ルールへ戻るなら <a href="../verification.html">検証基盤</a>、長文の研究ノートへ戻るなら <a href="../perspective.html">研究ノート</a> をご利用ください。
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="observation-to-estimation.html">観測から推定へ →</a></li>
<li><a href="verification-basics.html">検証基盤の基本 →</a></li>
<li><a href="measurement-and-modeling-terms.html">計測からモデル化まで →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../eeg_101.html">EEG入門 →</a></li>
<li><a href="../verification.html">検証基盤 →</a></li>
<li><a href="../perspective.html">研究ノート →</a></li>
</ul>
</div>
</aside>
</main>
