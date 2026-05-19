---
layout: default
title: "計測とデータ"
description: "EEGを中心に、脳をどう測るか、どこに限界があるか、BIDSやQCがなぜ必要かを初歩から整理します。"
article_type: Wiki
subtitle: "『見えているもの』と『推定しているもの』を分ける"
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
脳計測は、脳をそのまま読んでいるのではなく、<strong>測れた信号から逆算している</strong>部分が多いです。だから Mind-Upload では、計測機器の性能だけでなく、QC、メタデータ、BIDS のような整理規約を研究の中心に置きます。
</p>
</div>

<section class="section" id="modalities">
<h2 class="section-title">まずは主要モダリティを区別する</h2>
<table class="data-table">
<thead>
<tr>
<th>モダリティ</th>
<th>何を測るか</th>
<th>得意</th>
<th>苦手</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG</strong></td>
<td>頭皮上の電位差</td>
<td>時間分解能、低コスト、反復計測</td>
<td>空間分解能、深部推定、ノイズ耐性</td>
</tr>
<tr>
<td><strong>MEG</strong></td>
<td>脳活動由来の磁場</td>
<td>時間分解能、EEGと補完的な感度</td>
<td>装置コスト、設置制約</td>
</tr>
<tr>
<td><strong>fMRI</strong></td>
<td>血流変化（BOLD）</td>
<td>空間分解能、全脳カバレッジ</td>
<td>時間分解能、因果解釈</td>
</tr>
<tr>
<td><strong>ECoG / 侵襲記録</strong></td>
<td>脳表や深部の電気活動</td>
<td>SNR、局所性、介入と組み合わせやすい</td>
<td>倫理、対象者制約、大規模化の難しさ</td>
</tr>
<tr>
<td><strong>コネクトーム</strong></td>
<td>神経結合の構造</td>
<td>配線情報、構造制約</td>
<td>動的状態や化学的変調を直接は与えない</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="core-concepts">
<h2 class="section-title">計測ページで頻出する基礎語</h2>
<div class="key-points">
<h4>Key Terms</h4>
<ul>
<li><strong>逆問題：</strong>観測された信号から脳内の原因を推定する問題です。一般に答えは一意に決まりません。</li>
<li><strong>ESI：</strong>EEG Source Imaging。EEGから皮質上の活動を推定する手法です。</li>
<li><strong>QC：</strong>Quality Control。欠損、ノイズ、同期ずれ、アーティファクトを数値で残すことです。</li>
<li><strong>BIDS / EEG-BIDS：</strong>データとメタデータの置き方をそろえる共通規約です。</li>
</ul>
</div>
</section>

<section class="section" id="why-bids">
<h2 class="section-title">なぜ BIDS と QC がそんなに重要か</h2>
<p>
同じ EEG データでも、参照法、前処理、欠損チャンネルの扱い、刺激同期の精度で結果が変わります。BIDS は「どのファイルをどこに置くか」を、QC は「そのデータがどれくらい信用できるか」を固定します。
</p>
<div class="note-box">
<strong>重要</strong>
<p>
機械学習モデルの性能が高く見えても、入力の品質が不明だと比較不能です。Mind-Upload がまず L0 を重視するのはこのためです。
</p>
</div>
<div class="cta-box">
<h4>Deep Dive</h4>
<p>標準化の実務は <a href="{{ '/wiki/bids-and-eeg-bids.html' | relative_url }}">BIDS / EEG-BIDS</a>、推定の限界は <a href="{{ '/wiki/inverse-problem-and-esi.html' | relative_url }}">逆問題とESI</a>、観測量の読み分けは <a href="{{ '/wiki/observables-and-proxies.html' | relative_url }}">観測量と代理指標</a>、構造側の限界は <a href="{{ '/wiki/connectome-and-dynamics.html' | relative_url }}">コネクトームとダイナミクス</a> で詳しく追えます。</p>
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
<td><strong>WBEに必要な最低解像度</strong><br>どの粒度まで測れば十分か。</td>
<td>必要な情報がシナプスレベルなのか、回路レベルなのか、まだ合意がありません。</td>
<td>計測戦略と予算配分がぶれます。</td>
<td>非侵襲、侵襲、構造計測の役割分担を現実的に決められます。</td>
</tr>
<tr>
<td><strong>逆問題の不確実性</strong><br>頭皮信号から原因をどこまで一意に復元できるか。</td>
<td>同じ頭皮パターンを複数の脳内源が作れるからです。</td>
<td>ソース推定を強く解釈しすぎる危険があります。</td>
<td>どこまでが観測で、どこからが仮定かを明示できます。</td>
</tr>
<tr>
<td><strong>マルチモーダル統合の最適化</strong><br>EEG, MEG, fMRI, 構造情報をどう統合すべきか。</td>
<td>各モダリティでノイズ構造も時間軸も異なるためです。</td>
<td>統合モデルの不確実性が増えます。</td>
<td>時間と空間の両方を少しずつ制約できます。</td>
</tr>
<tr>
<td><strong>縦断的に安定な個人特徴</strong><br>日ごとの揺らぎを超えて残る特徴は何か。</td>
<td>覚醒、疲労、環境、装着条件の変動が大きいからです。</td>
<td>本人性や長期トラッキングの材料が弱いです。</td>
<td>L4 に近い議論の足場を作れます。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-it-matters">
<h2 class="section-title">このページが分かると何が進むか</h2>
<div class="key-points">
<h4>Practical Gain</h4>
<ul>
<li>EEG の成果を過大評価せず、現実的な貢献場所を判断できます。</li>
<li>「とりあえずデータ収集」ではなく、「比較可能なデータ収集」に切り替えられます。</li>
<li>測定の限界と、後続のモデル化が担う役割を切り分けられます。</li>
</ul>
</div>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>関連Wiki</h4>
<ul>
<li><a href="{{ '/wiki/bids-and-eeg-bids.html' | relative_url }}">BIDS / EEG-BIDS →</a></li>
<li><a href="{{ '/wiki/inverse-problem-and-esi.html' | relative_url }}">逆問題とESI →</a></li>
<li><a href="{{ '/wiki/pci-and-perturbation.html' | relative_url }}">PCI と摂動応答 →</a></li>
<li><a href="{{ '/wiki/connectome-and-dynamics.html' | relative_url }}">コネクトームとダイナミクス →</a></li>
<li><a href="{{ '/wiki/observables-and-proxies.html' | relative_url }}">観測量と代理指標 →</a></li>
<li><a href="{{ '/wiki/modeling-basics.html' | relative_url }}">モデルと因果 →</a></li>
<li><a href="{{ '/wiki/reproducibility-basics.html' | relative_url }}">再現性とベンチ →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>元ページ</h4>
<ul>
<li><a href="{{ '/eeg_101.html' | relative_url }}">EEG入門 →</a></li>
<li><a href="{{ '/datasets.html' | relative_url }}">データ&ベンチ →</a></li>
<li><a href="{{ '/hands_on.html' | relative_url }}">ハンズオン →</a></li>
<li><a href="{{ '/tech_roadmap.html#measurement' | relative_url }}">Roadmap: 計測 →</a></li>
</ul>
</div>

</aside>
</main>
