---
layout: default
title: "BIDS / EEG-BIDS"
description: "BIDSとEEG-BIDSを、最低限のフォルダ構造、メタデータ、Validator、未解決点まで含めて整理します。"
article_type: Wiki
subtitle: "『共有できるデータ』を作るための最低限"
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
BIDS は、脳計測データを<strong>他の人が読める形</strong>で置くための規約です。EEG-BIDS はその EEG 拡張です。重要なのは、単にファイル名を整えることではなく、<strong>メタデータと QC を一緒に残す</strong>ことです。
</p>
</div>

<section class="section" id="minimum">
<h2 class="section-title">最低限なにが必要か</h2>
<div class="key-points">
<h4>Minimum Set</h4>
<ul>
<li><strong>`dataset_description.json`：</strong>データセットの説明。</li>
<li><strong>`participants.tsv`：</strong>参加者情報。</li>
<li><strong>`sub-xx/eeg/`：</strong>EEG本体と sidecar JSON。</li>
<li><strong>`channels.tsv` / `electrodes.tsv`：</strong>チャンネルと電極位置。</li>
<li><strong>イベント情報：</strong>刺激時刻、課題条件、反応など。</li>
<li><strong>QC と監査ログ：</strong>欠損、ノイズ、同期誤差、除外区間の記録。</li>
</ul>
</div>
</section>

<section class="section" id="skeleton">
<h2 class="section-title">最小フォルダ骨格</h2>
<pre><code>dataset/
  dataset_description.json
  participants.tsv
  sub-01/
    eeg/
      sub-01_task-rest_eeg.edf
      sub-01_task-rest_eeg.json
      sub-01_task-rest_channels.tsv
      sub-01_task-rest_events.tsv
</code></pre>
<p>
実務では、ここに <code>derivatives/</code> を追加して、前処理結果や監査ログを残します。Mind-Upload では、BIDS 準拠そのものだけでなく、<strong>何を削除し、何を残したか</strong>の監査性も重視します。
</p>
</section>

<section class="section" id="validator">
<h2 class="section-title">Validator は何を保証し、何を保証しないか</h2>
<table class="data-table">
<thead>
<tr>
<th>できること</th>
<th>できないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td>ファイル名や必須メタデータの形式確認</td>
<td>データの科学的妥当性の保証</td>
</tr>
<tr>
<td>不足ファイルや構文エラーの検出</td>
<td>同期精度やアーティファクト除去の品質保証</td>
</tr>
<tr>
<td>共有時の最低限の互換性確保</td>
<td>課題設計やラベル定義の妥当性判断</td>
</tr>
</tbody>
</table>
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
<td><strong>認知文脈のメタデータ</strong><br>何をどこまで標準化すべきか。</td>
<td>刺激、主観報告、課題意図の記述がまだばらつくからです。</td>
<td>同じ課題名でも意味がずれることがあります。</td>
<td>高レベル比較の再現性が上がります。</td>
</tr>
<tr>
<td><strong>Derivatives の監査規約</strong><br>前処理や除去の証跡をどこまで残すか。</td>
<td>解析手法が多様で、統一文化がまだ弱いからです。</td>
<td>再解析時に前処理の影響を追えません。</td>
<td>同じ生データから別の結論が出た理由を監査できます。</td>
</tr>
<tr>
<td><strong>マルチモーダル同期</strong><br>EEG, fMRI, motion, 刺激ログをどう一貫記述するか。</td>
<td>時間軸も座標系も機器ごとに異なるからです。</td>
<td>介入や閉ループの比較で詰まります。</td>
<td>複数モダリティの統合解析がしやすくなります。</td>
</tr>
<tr>
<td><strong>公開と秘匿の境界</strong><br>神経データをどこまで安全に共有できるか。</td>
<td>個人識別性や機微情報の扱いが難しいからです。</td>
<td>オープン共有の範囲設定が難しいです。</td>
<td>安全に比較可能なデータ基盤を広げられます。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-it-matters">
<h2 class="section-title">このページが分かると何が進むか</h2>
<div class="key-points">
<h4>Practical Gain</h4>
<ul>
<li>「BIDS準拠」と「本当に追試可能」を分けて評価できます。</li>
<li>データ共有の最初の実装単位が具体的になります。</li>
<li>QC とメタデータが、モデル性能より先に必要な理由が明確になります。</li>
</ul>
</div>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>関連Wiki</h4>
<ul>
<li><a href="{{ '/wiki/measurement-basics.html' | relative_url }}">計測とデータ →</a></li>
<li><a href="{{ '/wiki/reproducibility-basics.html' | relative_url }}">再現性とベンチ →</a></li>
<li><a href="{{ '/wiki/inverse-problem-and-esi.html' | relative_url }}">逆問題とESI →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>元ページ</h4>
<ul>
<li><a href="{{ '/datasets.html#bids' | relative_url }}">Datasets: BIDS →</a></li>
<li><a href="{{ '/hands_on.html#bids-skeleton' | relative_url }}">Hands-on: BIDS骨格 →</a></li>
<li><a href="{{ '/tech_roadmap.html#qa-m9' | relative_url }}">Roadmap: M9 →</a></li>
</ul>
</div>

</aside>
</main>
