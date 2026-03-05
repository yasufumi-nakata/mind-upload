---
layout: default
title: "Wiki：観測から推定へ"
description: "順問題、逆問題、ESI、DCM、SCM、因果同値類を、観測から推定へ進む流れで初歩から説明します。"
article_type: Wiki
subtitle: "観測したことと、再構成したことと、因果が分かったことは別です"
author: Mind Uploading Research Project
last_updated: "2026-03-06"
note: "Learning guide"
audience: "逆問題や因果モデルの言葉で止まりやすい人、EEG から何が言えるかを丁寧に整理したい人"
reading_time: "10〜15分"
page_intro: "このページは、EEG などの観測信号から脳内状態や因果構造を推定するときに出てくる言葉を、順問題、逆問題、ESI、DCM、SCM、因果同値類の順で整理する wiki です。『観測できた』と『再構成できた』と『因果が分かった』を混同しないことを目的にします。"
accuracy_note: "ここで示すのは読み方の足場です。個別手法の細部や数式は省いていますが、不確実性が残ることと、代替モデルがありうることは削りません。"
page_highlights:
  - "順問題と逆問題の違いを、日常語で先に分けます。"
  - "ESI、DCM、SCM がそれぞれ何を仮定しているかを整理します。"
  - "推定結果は点で読むのでなく、不確実性と代替説明ごと読むべきだと分かります。"
known_points:
  - "頭皮 EEG から脳内活動を一意に決めることは原理的に難しく、推定には仮定が入ります。"
  - "ESI、DCM、SCM は同じ種類の手法ではなく、役割が異なります。"
  - "複数のモデルが同じ観測を説明できる可能性を明示することは重要です。"
unknown_points:
  - "どのモデル化の組み合わせが WBE の検証に最も有効かは未確定です。"
  - "非侵襲計測からどこまで詳細な因果構造を復元できるかは研究途中です。"
wiki_links:
  - label: "Wiki: 計測からモデル化まで"
    url: "/wiki/measurement-and-modeling-terms.html"
    description: "計測、整理、推定、検証の全体マップへ戻れます。"
  - label: "Wiki: EEG前処理とQC"
    url: "/wiki/eeg-preprocessing-and-qc.html"
    description: "推定の前段で、何が結果を変えるかを補います。"
  - label: "Wiki: 検証基盤の基本"
    url: "/wiki/verification-basics.html"
    description: "推定結果をどう比較可能にするかを補います。"
recommended_pages:
  - label: "EEG入門"
    url: "/eeg_101.html"
  - label: "検証基盤"
    url: "/verification.html"
  - label: "用語集"
    url: "/glossary.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>いちばん短い地図</h2>
<p>
EEG で外から見えるのは、脳内活動の<strong>混ざった結果</strong>です。そこから中身を推定するには、まず「もし脳内にこの活動があったら、頭皮ではどう見えるか」という<strong>順問題</strong>を考え、その逆向きに「この頭皮信号を説明しうる脳内活動は何か」という<strong>逆問題</strong>を解きます。
</p>
</div>

<section class="section" id="three-levels">
<h2 class="section-title">まず 3 段階を分ける</h2>
<table class="data-table">
<thead>
<tr>
<th>段階</th>
<th>何をしているか</th>
<th>まだ言えないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>観測</strong></td>
<td>頭皮や外側で見える信号を測ります。</td>
<td>それだけで脳内状態を一意に再構成したとは言えません。</td>
</tr>
<tr>
<td><strong>推定</strong></td>
<td>モデルや仮定を使って、脳内活動や結合を推測します。</td>
<td>推定結果が唯一の真実だとは言えません。</td>
</tr>
<tr>
<td><strong>因果検証</strong></td>
<td>介入や反事実で、モデルがどこまで反応を再現するかを見ます。</td>
<td>出力一致だけで因果構造まで同じだと即断はできません。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="forward-inverse">
<h2 class="section-title">順問題と逆問題</h2>
<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>意味</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>順問題</strong></td>
<td>もし脳内にこの活動があるなら、頭皮ではどんな信号になるかを計算する問題です。</td>
</tr>
<tr>
<td><strong>逆問題</strong></td>
<td>頭皮でこの信号が見えたとき、脳内でどんな活動が起きていたかを推定する問題です。</td>
</tr>
</tbody>
</table>
<p>
順問題は、条件が分かっていれば比較的定めやすい一方、逆問題は<strong>複数の答えが同じ観測を作れてしまう</strong>のが難しさです。これが「逆問題は不良設定になりやすい」と言われる理由です。
</p>
</section>

<section class="section" id="esi">
<h2 class="section-title">ESI は何をしているのか</h2>
<p>
ESI は、逆問題を解いて「この頭皮信号なら、脳内ではこのあたりが活動していた可能性が高い」と推定する枠組みです。ここで重要なのは、ESI は魔法の位置特定ではなく、<strong>仮定付きの推定</strong>だという点です。
</p>
<div class="key-points">
<h4>ESI を読むときの 3 点</h4>
<ul>
<li><strong>何を仮定したか：</strong>頭部モデル、導電率、スパース性、MRI の有無など。</li>
<li><strong>不確実性を出しているか：</strong>点推定だけでなく、信用区間や事後分布があるか。</li>
<li><strong>代替説明を閉じていないか：</strong>別のソース配置でも同じ観測が作れないか。</li>
</ul>
</div>
</section>

<section class="section" id="dcm">
<h2 class="section-title">DCM は何を足しているのか</h2>
<p>
ESI が「どこが活動していそうか」を主に見るのに対し、DCM は「どの回路が、どうつながって動いていそうか」を見るための生成モデルです。つまり、単なる位置推定より一歩進んで、<strong>回路の動き方そのものを仮定して説明しようとする</strong>枠組みです。
</p>
<table class="data-table">
<thead>
<tr>
<th>ESI と DCM の違い</th>
<th>ひとことで言うと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>ESI</strong></td>
<td>どこが活動していそうかを推定します。</td>
</tr>
<tr>
<td><strong>DCM</strong></td>
<td>どの回路がどう結合していそうかを、生成モデルで比較します。</td>
</tr>
</tbody>
</table>
<p>
ただし DCM でも、候補モデルの置き方や比較の範囲に依存します。モデル比較で勝ったことは「候補の中では良い」という意味であり、世界で唯一正しいとまでは言えません。
</p>
</section>

<section class="section" id="scm">
<h2 class="section-title">SCM は何が違うのか</h2>
<p>
SCM は、因果関係を明示して「もしここを変えたら、他はどう変わるか」を扱いやすくする枠組みです。観測だけでなく、<strong>介入</strong>や<strong>反事実</strong>を定義しやすいのが特徴です。
</p>
<div class="note-box">
<strong>DCM と SCM の関係</strong>
<p>
DCM は神経回路の生成モデルとして有用で、SCM は介入や反事実を明示しやすい枠組みです。役割は重なる部分もありますが、同じものではありません。Mind-Upload では、相関ベースの予測から、介入ベースの検証へ進む橋として SCM 的な発想を重視します。
</p>
</div>
</section>

<section class="section" id="equivalence">
<h2 class="section-title">因果同値類とは何か</h2>
<p>
観測データだけでは、複数の因果モデルが同じ統計を作ることがあります。この「観測では区別できないモデルの集まり」を、ざっくり言えば<strong>因果同値類</strong>と考えると分かりやすいです。
</p>
<p>
ここで大事なのは、「このモデルが観測に合った」ことと「このモデルしかありえない」ことを分けることです。後者を主張するには、追加の介入、別データ、事前知識が必要になります。
</p>
</section>

<section class="section" id="how-to-read">
<h2 class="section-title">推定結果を読むときの最低チェック</h2>
<div class="key-points">
<h4>Checklist</h4>
<ul>
<li><strong>観測と推定を分けて書いているか：</strong>頭皮信号と脳内活動を同じ言葉で混ぜていないか。</li>
<li><strong>不確実性があるか：</strong>点推定だけでなく、幅や分布が示されているか。</li>
<li><strong>代替モデルを意識しているか：</strong>別説明の余地を認めているか。</li>
<li><strong>介入や反事実へ進めるか：</strong>相関で止まっていないか。</li>
</ul>
</div>
</section>

<section class="section" id="return">
<h2 class="section-title">次にどこへ戻るか</h2>
<p>
短い定義に戻るなら <a href="../glossary.html">用語集</a>、EEG の全体像へ戻るなら <a href="../eeg_101.html">EEG入門</a>、比較可能な検証へ戻るなら <a href="../verification.html">検証基盤</a> をご利用ください。
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="measurement-and-modeling-terms.html">計測からモデル化まで →</a></li>
<li><a href="eeg-preprocessing-and-qc.html">EEG前処理とQC →</a></li>
<li><a href="verification-basics.html">検証基盤の基本 →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../glossary.html">用語集 →</a></li>
<li><a href="../eeg_101.html">EEG入門 →</a></li>
<li><a href="../verification.html">検証基盤 →</a></li>
</ul>
</div>
</aside>
</main>
