---
layout: default
title: "Wiki：反事実・介入・摂動の検証"
description: "held-out 精度、介入、反事実、摂動ベース検証の違いを、初歩から整理します。"
article_type: Wiki
subtitle: "当たることと、条件を変えても正しく反応することは別です"
author: Mind Uploading Research Project
last_updated: "2026-03-06"
note: "Learning guide"
audience: "decode と emulate の差をもう一段ていねいに理解したい人、因果検証の入口で止まりやすい人"
reading_time: "10〜15分"
page_intro: "このページは、held-out 精度が高いこと、介入に正しく反応すること、反事実の分岐を再現できること、摂動に対する応答構造が一致することを、初歩から切り分ける wiki です。『精度が高い = 中身も同じ』という誤解を避けることを目的にします。"
accuracy_note: "ここで扱うのは検証の考え方です。個別の摂動プロトコルや数式は省きますが、因果検証が held-out 精度より厳しいという点は崩しません。"
page_highlights:
  - "held-out 精度と因果検証の違いを、段階ごとに分けます。"
  - "介入、反事実、摂動が何を確かめるかを、日常語で整理します。"
  - "Benchmark、Registry、Model Card がなぜここで必要かが分かります。"
known_points:
  - "学習していないデータで当たることは重要ですが、それだけで因果構造の一致は言えません。"
  - "条件をわざと変えたときの反応を見る検証は、出力一致より強いテストです。"
  - "反事実や摂動の検証には、失敗条件とログの固定が必要です。"
unknown_points:
  - "どの摂動セットが WBE の本人性主張へ最も効くかは未解決です。"
  - "反事実等価性をどこまで満たせば十分かは、理論と工学の両面で研究途中です。"
wiki_links:
  - label: "Wiki: Decode と Emulate"
    url: "/wiki/decode-vs-emulate.html"
    description: "まず翻訳と生成の違いへ戻りたい人向けです。"
  - label: "Wiki: 観測から推定へ"
    url: "/wiki/observation-to-estimation.html"
    description: "推定モデルと因果モデルの違いを補います。"
  - label: "Wiki: 検証基盤の基本"
    url: "/wiki/verification-basics.html"
    description: "Benchmark、Registry、Model Card の役割を補います。"
recommended_pages:
  - label: "WBE入門"
    url: "/wbe_101.html"
  - label: "検証基盤"
    url: "/verification.html"
  - label: "FAQ"
    url: "/faq.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>いちばん短い違い</h2>
<p>
held-out 精度は「見たことのない問題でも当たるか」を見るテストです。介入や反事実の検証は、「条件を変えたとき、どの方向へどう崩れ、どう持ち直すかまで再現できるか」を見るテストです。
</p>
</div>

<section class="section" id="ladder">
<h2 class="section-title">まず検証の強さを 4 段階で分ける</h2>
<table class="data-table">
<thead>
<tr>
<th>段階</th>
<th>何を見ているか</th>
<th>まだ言えないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. held-out 精度</strong></td>
<td>見たことのないデータでも当たるか。</td>
<td>条件変更への反応や因果構造の一致はまだ言えません。</td>
</tr>
<tr>
<td><strong>2. OOD / 新規条件</strong></td>
<td>少し違う条件でも崩れにくいか。</td>
<td>介入したときに中の仕組みが同じように動くかまでは言えません。</td>
</tr>
<tr>
<td><strong>3. 介入</strong></td>
<td>刺激や入力条件をわざと変えたとき、応答が正しく変わるか。</td>
<td>「もし別の分岐だったら」という反事実全体まではまだ十分でない場合があります。</td>
</tr>
<tr>
<td><strong>4. 反事実・摂動構造</strong></td>
<td>分岐全体や応答伝播の構造が、生体と同じように動くか。</td>
<td>それでも本人性や社会実装まで即断はできません。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-accuracy-not-enough">
<h2 class="section-title">なぜ精度だけでは足りないのか</h2>
<p>
テスト問題で高得点でも、問題の癖を覚えただけかもしれません。同じように、モデルが高精度でも、それが<strong>本当に中の仕組みを捉えたのか</strong>、それとも表面のパターンを拾っただけかは、精度だけでは分かりません。
</p>
<div class="note-box">
<strong>よくある事故</strong>
<p>
データリーク、分布の偏り、言語モデルの事前分布、評価条件の甘さがあると、見かけのスコアだけが上がります。だから Mind-Upload では、スコアの前に失敗条件と検証条件を固定します。
</p>
</div>
</section>

<section class="section" id="intervention-counterfactual">
<h2 class="section-title">介入と反事実はどう違うのか</h2>
<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>ひとことで言うと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>介入</strong></td>
<td>実際に条件を変えて、その結果を見ます。</td>
</tr>
<tr>
<td><strong>反事実</strong></td>
<td>「もし別の条件だったら」と、起きなかった分岐まで含めて考えます。</td>
</tr>
<tr>
<td><strong>摂動</strong></td>
<td>システムへ小さな変化や刺激を加えて、応答の広がり方を見ることです。</td>
</tr>
</tbody>
</table>
<p>
介入は実験で行いやすい入口で、反事実はより強い問いです。摂動は、その入口として「条件をわざと揺らして、応答構造を見る」具体的なやり方だと考えると分かりやすいです。
</p>
</section>

<section class="section" id="simple-example">
<h2 class="section-title">小さな例で考える</h2>
<table class="data-table">
<thead>
<tr>
<th>テスト</th>
<th>何を確かめているか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>held-out EEG 分類</strong></td>
<td>未見データでも状態ラベルを当てられるか。</td>
</tr>
<tr>
<td><strong>新規刺激条件での予測</strong></td>
<td>学習していない条件でも、応答傾向が崩れないか。</td>
</tr>
<tr>
<td><strong>仮想摂動の応答比較</strong></td>
<td>条件を変えたときの伝播や回復の仕方が似ているか。</td>
</tr>
<tr>
<td><strong>反事実分岐の比較</strong></td>
<td>「もし刺激位置や条件が違ったら」という分岐構造まで追えるか。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="commons-role">
<h2 class="section-title">なぜ Benchmark / Registry / Model Card が要るのか</h2>
<div class="key-points">
<h4>役割分担</h4>
<ul>
<li><strong>Benchmark：</strong>どの介入や摂動を行い、何で採点するかを固定します。</li>
<li><strong>Registry：</strong>どの条件で失敗とみなすか、どこまでを事前に決めるかを固定します。</li>
<li><strong>Model Card：</strong>どの摂動で崩れたか、どの OOD 条件に弱いかを残します。</li>
</ul>
</div>
<p>
ここが曖昧だと、後から都合のよい摂動だけを選んで「中身も同じ」と言えてしまいます。
</p>
</section>

<section class="section" id="how-to-read">
<h2 class="section-title">因果検証の話を読むときの最低チェック</h2>
<div class="key-points">
<h4>Checklist</h4>
<ul>
<li><strong>ただの held-out 精度ではないか：</strong>条件変更が本当に入っているか。</li>
<li><strong>介入内容が明示されているか：</strong>何をどれだけ変えたかが書かれているか。</li>
<li><strong>失敗条件があるか：</strong>どんな結果なら不一致とみなすかが先に決まっているか。</li>
<li><strong>失敗例が残っているか：</strong>うまくいかなかった摂動も公開されているか。</li>
</ul>
</div>
</section>

<section class="section" id="return">
<h2 class="section-title">次にどこへ戻るか</h2>
<p>
翻訳と生成の違いへ戻るなら <a href="../wbe_101.html">WBE入門</a>、検証設計へ戻るなら <a href="../verification.html">検証基盤</a>、短い Q&A へ戻るなら <a href="../faq.html">FAQ</a> をご利用ください。
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="decode-vs-emulate.html">Decode と Emulate →</a></li>
<li><a href="observation-to-estimation.html">観測から推定へ →</a></li>
<li><a href="verification-basics.html">検証基盤の基本 →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../wbe_101.html">WBE入門 →</a></li>
<li><a href="../verification.html">検証基盤 →</a></li>
<li><a href="../faq.html">FAQ →</a></li>
</ul>
</div>
</aside>
</main>
