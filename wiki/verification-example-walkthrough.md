---
layout: default
title: "Wiki：Verification の具体例ウォークスルー"
description: "EEG の小さな例で、Data Standard、Benchmark、Registry、Model Card がどう噛み合うかを順番に説明します。"
article_type: Wiki
subtitle: "設計図を、1本の小さな実例に落として読む"
author: Mind Uploading Research Project
last_updated: "2026-03-14"
note: "Worked example"
audience: "Verification ページが抽象的に感じる人、要素同士の関係を具体例で理解したい人"
reading_time: "10〜15分"
page_intro: "このページは、Verification Commons の設計図を『EEG で状態分類を行う小さな例』に落として順番に読むための wiki です。抽象語を増やすのではなく、入力、手順、評価、反証がどうつながるかを見える形にします。"
accuracy_note: "ここで扱うのは理解用の最小例です。これだけで WBE の強い主張を支えられるわけではなく、L0〜L2 の入口を具体化する補講です。"
page_highlights:
  - "Data Standard、Benchmark、Registry、Model Card の役割差を 1 本の例で見られます。"
  - "なぜ『データがある』だけでは足りないかを、作業順で理解できます。"
  - "どこから先が未解決かも、実例の中で切り分けています。"
known_points:
  - "公開 EEG データでも、Verification Commons の最小形を作る練習はできます。"
  - "入力、手順、評価、反証を分けて残すだけで、比較可能性は大きく上がります。"
  - "小さな例でも、リーク対策と失敗記録は必須です。"
unknown_points:
  - "このような小さな例だけで、本人性や現象的意識の検証へ進めるわけではありません。"
  - "どのタスクが将来の L3 以降へ最も強くつながるかは、まだ開拓中です。"
wiki_links:
  - label: "Wiki: 検証基盤の基本"
    url: "/wiki/verification-basics.html"
    description: "まず役割の全体像を押さえたい人向けです。"
  - label: "Wiki: データ分割とリーク"
    url: "/wiki/dataset-splits-and-leakage.html"
    description: "この例で前提にしている train/test の境界を補います。"
  - label: "Wiki Home"
    url: "/wiki/"
    description: "他の補助ページへ戻れます。"
recommended_pages:
  - label: "検証基盤"
    url: "/verification.html"
  - label: "ハンズオン"
    url: "/datasets.html#l0-practice"
  - label: "データ&ベンチ"
    url: "/datasets.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>今回の小さな例</h2>
<p>
ここでは「公開 EEG データを使って、2 つの状態を分類する小さなモデル」を例にします。目的は高精度を出すことではなく、<strong>他の人が同じ条件で確かめられる最小セット</strong>を理解することです。
</p>
</div>

<section class="section" id="whole-picture">
<h2 class="section-title">4つの部品を先に並べる</h2>
<table class="data-table">
<thead>
<tr>
<th>部品</th>
<th>この例で何を置くか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Data Standard</strong></td>
<td>BIDS 形式の EEG データ、被験者情報、イベント定義、QC ログです。</td>
</tr>
<tr>
<td><strong>Benchmark</strong></td>
<td>何を予測するか、どの分割で比べるか、どの指標で採点するかです。</td>
</tr>
<tr>
<td><strong>Registry</strong></td>
<td>前処理条件、分割規則、停止条件、ベースラインを事前に固定した記録です。</td>
</tr>
<tr>
<td><strong>Model Card</strong></td>
<td>最終スコア、失敗例、リーク検査、弱点、計算条件のまとめです。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="step1">
<h2 class="section-title">Step 1: まず入力の形を固定する</h2>
<p>
同じ EEG データでも、イベント定義や電極情報が欠けると、他の人は同じ解析を再現できません。最初に必要なのは「すごいモデル」ではなく、<strong>何を入力として渡しているかが明確な状態</strong>です。
</p>
<div class="key-points">
<h4>最低限ほしいもの</h4>
<ul>
<li><strong>BIDS 形式：</strong>ファイルの置き方とメタデータの形をそろえます。</li>
<li><strong>QC ログ：</strong>欠損、ノイズ、除外理由を残します。</li>
<li><strong>分割単位：</strong>被験者単位なのか、セッション単位なのかを明記します。</li>
</ul>
</div>
</section>

<section class="section" id="step2">
<h2 class="section-title">Step 2: 比べ方を固定する</h2>
<p>
次に Benchmark を置きます。これは「何を正解とみなし、何と比べるか」を決める部分です。ここが曖昧だと、後から都合のよい指標へ逃げられてしまいます。
</p>
<table class="data-table">
<thead>
<tr>
<th>項目</th>
<th>この例での固定内容</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>課題</strong></td>
<td>2 状態分類を行う、と最初に固定します。</td>
</tr>
<tr>
<td><strong>分割</strong></td>
<td>被験者単位で train/validation/test を分けます。</td>
</tr>
<tr>
<td><strong>指標</strong></td>
<td>精度だけでなく、混同行列や失敗例も残します。</td>
</tr>
<tr>
<td><strong>ベースライン</strong></td>
<td>単純な分類器を 1 本置き、改善幅を見ます。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="step3">
<h2 class="section-title">Step 3: やる前の約束を残す</h2>
<p>
Registry は「後から条件を変えて勝ったことにしない」ための部品です。たとえば、どの前処理を使うか、いつ止めるか、test をどこで使わないかを先に書いておきます。
</p>
<div class="note-box">
<strong>ここで先に書いておきたいこと</strong>
<p>
前処理の候補、分割規則、ベースライン、採点指標、失敗とみなす条件、更新時に何を差分として残すか、でございます。豪華な書式より、後から読み返して監査できることが重要です。
</p>
</div>
</section>

<section class="section" id="step4">
<h2 class="section-title">Step 4: 最後に Model Card で公開する</h2>
<p>
最後に必要なのは、点数だけの発表ではなく、「どこで勝ち、どこで崩れたか」を残すことです。これが Model Card の役目です。
</p>
<div class="key-points">
<h4>最低限入れたい項目</h4>
<ul>
<li><strong>結果：</strong>主要指標、ベースラインとの差、再実行条件。</li>
<li><strong>リーク検査：</strong>分割や前処理で test 情報が混ざっていないか。</li>
<li><strong>失敗例：</strong>どの被験者、どの条件で崩れやすいか。</li>
<li><strong>弱点：</strong>OOD、ノイズ、計算コスト、既知の限界。</li>
</ul>
</div>
</section>

<section class="section" id="boundary">
<h2 class="section-title">この例で分かること / 分からないこと</h2>
<table class="data-table">
<thead>
<tr>
<th>この例で分かること</th>
<th>この例だけでは分からないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td>再現可能な L0〜L1 の最小ループをどう作るか。</td>
<td>本人性、現象的意識、L4 以降の成立条件。</td>
</tr>
<tr>
<td>リークを避けた比較可能な評価の形。</td>
<td>介入や閉ループまで含む強い因果主張。</td>
</tr>
<tr>
<td>何を記録すれば他者が追試しやすいか。</td>
<td>どの理論が最終的に意識の説明として正しいか。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="return">
<h2 class="section-title">次にどこへ戻るか</h2>
<p>
設計図そのものへ戻るなら <a href="../verification.html">検証基盤</a>、実際に最小ループを動かすなら <a href="../datasets.html#l0-practice">ハンズオン</a>、入口データを見直すなら <a href="../datasets.html">データ&ベンチ</a> を読んでください。
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="verification-basics.html">検証基盤の基本 →</a></li>
<li><a href="dataset-splits-and-leakage.html">データ分割とデータリーク →</a></li>
<li><a href="eeg-preprocessing-and-qc.html">EEG前処理とQC →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../verification.html">検証基盤 →</a></li>
<li><a href="../datasets.html#l0-practice">ハンズオン →</a></li>
<li><a href="../datasets.html">データ&ベンチ →</a></li>
</ul>
</div>
</aside>
</main>
