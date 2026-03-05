---
layout: default
title: "ハンズオン：再現可能なEEG解析（L0）を最短で作る"
description: "公開データでも自前データでも使える、BIDS→QC→前処理→評価の“最小ループ”を作る手順。"
article_type: Tutorial
subtitle: "まずは“再現できる”を達成してから、性能を競う"
author: Mind Uploading Research Project
last_updated: "2026-03-06"
note: "Practical"
audience: "最初の再現可能解析を作りたい人、公開データで手を動かしたい人"
reading_time: "10〜15分"
page_intro: "このページは、公開データを使って『他の人が同じ結果を再現できる最小ループ』を作るための実務ガイドです。高精度を競う前に、入力・QC・処理・出力・監査を一周つなぐことを優先します。"
accuracy_note: "ここで示す手順は最小構成です。これだけで研究が十分になるわけではありませんが、再現性を持たせる出発点になります。"
page_highlights:
  - "最初に目指すのはSOTAではなく、L0の再現可能解析です。"
  - "BIDS、QCログ、前処理条件、ベースライン指標を最小セットとして扱います。"
  - "失敗例や除外基準も残すことを、成功条件の一部として含めています。"
recommended_pages:
  - label: "データ&ベンチ"
    url: "/datasets.html"
  - label: "EEG入門"
    url: "/eeg_101.html"
  - label: "検証基盤"
    url: "/verification.html"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Goal</h2>
<p>
ここでの目標は「すごい精度を出す」ことではなく、<strong>他の人が同じ結果を再現できる最小ループ（L0）</strong>を作ることです。L0がないと、どれだけ高性能に見えても、あとから正しさを確認できません。
</p>
</div>

<div class="note-box">
<strong>このページの約束</strong>
<p>
ここでは、実験や大規模設備を前提にせず、今ある公開データと一般的なツールで始められる範囲に絞っています。つまり、「今この場で動かせる最小構成」を作るためのページです。
</p>
</div>

<section class="section" id="overview">
<h2 class="section-title">最小ループ（L0）の形</h2>
<div class="key-points">
<h4>L0 Loop</h4>
<ul>
<li><strong>入力：</strong>BIDS（データ + メタデータ）</li>
<li><strong>品質：</strong>QCログ（数値で）</li>
<li><strong>処理：</strong>前処理の設定・バージョン・乱数を記録</li>
<li><strong>出力：</strong>ベースライン指標（最低1つ）</li>
<li><strong>監査：</strong>失敗例・除外基準も残す</li>
</ul>
</div>
</section>

<section class="section" id="common-blockers">
<h2 class="section-title">最初に詰まりやすい点</h2>
<table class="data-table">
<thead>
<tr>
<th>詰まりやすい点</th>
<th>先に切り分けること</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>BIDSの形で止まる</strong></td>
<td>まずは実データの有無より、ディレクトリ骨格とメタデータ雛形を先に作ってください。形がないと、後の修正点が見えません。</td>
</tr>
<tr>
<td><strong>QCをどこまで残すか迷う</strong></td>
<td>完璧を狙わず、欠損・ノイズ・アーティファクト・除外理由の4つを最低ラインにしてください。</td>
</tr>
<tr>
<td><strong>ベースラインが決められない</strong></td>
<td>難しいモデルより、単純でも再現しやすい1本を先に置く方が前に進みます。</td>
</tr>
<tr>
<td><strong>共有前に不安になる</strong></td>
<td>BIDS Validator が通るか、実行手順が他人に渡せるか、失敗例を残しているかの3点でまず判定してください。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="bids-skeleton">
<h2 class="section-title">Step 1：BIDSの“骨格”を作る</h2>
<p>EEGのBIDSは「置き方が決まっている」のが強みです。まずは最小構成で形だけ作ります。</p>

<div class="note-box">
<strong>例：最小ディレクトリ</strong>
<p>（実データがなくても、構造だけは先に作れます）</p>
</div>

```text
my_bids_eeg/
  dataset_description.json
  participants.tsv
  sub-01/
    eeg/
      sub-01_task-rest_eeg.edf
      sub-01_task-rest_eeg.json
      sub-01_task-rest_channels.tsv
      sub-01_task-rest_events.tsv
```

<p>
`dataset_description.json` はすでにこのリポジトリにも雛形があります（概念段階ですが、発想は同じです）。
</p>
</section>

<section class="section" id="validator">
<h2 class="section-title">Step 2：BIDS Validator を回す</h2>
<p>
機械で検証できる項目はBIDS Validatorに任せ、最初の段階で規格違反を洗い出してください。この手順を全データ投入前に挟むだけで、後工程の手戻りがほぼ無くなり、レビュー負荷も抑えられます。
</p>

```bash
# Node.js がある環境で
npx bids-validator my_bids_eeg
```

<div class="note-box">
<strong>ポイント</strong>
<p>
Validatorが通る＝研究として十分、ではありません。でも、通らない状態で“共有”はほぼ成立しません。
</p>
</div>
</section>

<section class="section" id="qc">
<h2 class="section-title">Step 3：QCログを“数値”で残す</h2>
<p>
再現性が壊れる典型は「どのデータが悪かったか」が人依存になることです。最低限、次をログにします。
</p>
<div class="key-points">
<h4>QC Items</h4>
<ul>
<li><strong>欠損/飽和：</strong>チャンネルごとの欠損率、飽和区間</li>
<li><strong>ノイズ：</strong>電源周波数のピーク、ノイズフロア推定</li>
<li><strong>アーティファクト：</strong>眼球/筋電/動きの混入指標</li>
<li><strong>除外基準：</strong>どの閾値で除外したか（理由つき）</li>
</ul>
</div>
</section>

<section class="section" id="baseline">
<h2 class="section-title">Step 4：ベースラインを1本置く（最初は小さく）</h2>
<p>
最初は “たった1つの指標” で十分です。例：
安静EEGのスペクトル要約、睡眠段階分類のベースライン、運動想起の2クラス分類など。
</p>
<div class="note-box">
<strong>重要</strong>
<p>
「ベースラインがある」と「改善を主張できる」ようになります。ベースラインなしのSOTA議論は、ほぼノイズになります。
</p>
</div>
</section>

<section class="section" id="l0-done">
<h2 class="section-title">ここまでできたら L0 完了とみなせる目安</h2>
<table class="data-table">
<thead>
<tr>
<th>確認項目</th>
<th>最低ライン</th>
<th>まだ不足なら次にやること</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>入力の形</strong></td>
<td>BIDS の骨格があり、最低限のメタデータが置かれていること。</td>
<td>ディレクトリ構造と `dataset_description.json`、`channels.tsv` などの雛形を先に埋めます。</td>
</tr>
<tr>
<td><strong>規格確認</strong></td>
<td>BIDS Validator を通し、共有不能な規格違反が残っていないこと。</td>
<td>Validator のエラーを一つずつ潰し、警告は理由つきで残します。</td>
</tr>
<tr>
<td><strong>QCの証跡</strong></td>
<td>欠損、ノイズ、アーティファクト、除外理由の数値ログが残っていること。</td>
<td>人の記憶ではなく、再実行できるログ形式へ落とします。</td>
</tr>
<tr>
<td><strong>ベースライン</strong></td>
<td>単純でもよいので、1本の再現可能な指標が計算できること。</td>
<td>複雑なモデルを増やす前に、単純な分類や要約指標を固定します。</td>
</tr>
<tr>
<td><strong>再実行性</strong></td>
<td>他の人に渡せる手順として、コマンド、前処理条件、失敗例が残っていること。</td>
<td>README 相当の短い実行手順と、既知のつまずきどころを追記します。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="tie-to-verification">
<h2 class="section-title">このハンズオンがVerificationに繋がる点</h2>
<p>
ここまでできると、次は「同じ物差しで比較できる」方向へ進めます。つまり、ベンチマーク化です。
</p>
<div class="cta-box">
<h4>Next</h4>
<p>L0を“公共財”にして積み上げる設計図。</p>
<a href="verification.html">検証基盤を見る →</a>
</div>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>Related</h4>
<ul>
<li><a href="datasets.html">データ&ベンチ →</a></li>
<li><a href="eeg_101.html">EEG入門 →</a></li>
<li><a href="tech_roadmap.html#definition">前進の定義 →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>External</h4>
<ul>
<li><a href="https://bids.neuroimaging.io/" target="_blank">BIDS</a></li>
<li><a href="https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/03-electroencephalography.html" target="_blank">BIDS EEG Spec</a></li>
</ul>
</div>

</aside>
</main>
