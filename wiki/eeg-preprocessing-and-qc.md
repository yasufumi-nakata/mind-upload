---
layout: default
title: "Wiki：EEG前処理とQC"
description: "参照法、フィルタ、アーティファクト処理、除外基準など、EEG の前処理と品質管理の基本を整理します。"
article_type: Wiki
subtitle: "結果が変わるのは、信号が繊細だからです"
author: Mind Uploading Research Project
last_updated: "2026-03-14"
note: "Practical guide"
audience: "EEG の前処理や QC がなぜ重要か知りたい人、Hands-on 前後でつまずいた人"
reading_time: "10〜15分"
page_intro: "このページは、EEG の前処理と QC がなぜ結果に大きく効くのかを初歩から説明する wiki です。難しいアルゴリズム一覧より先に、『どこで結果が変わりやすいか』『何をログに残すべきか』を理解することを目標にします。"
accuracy_note: "ここで挙げるのは典型的な論点です。最適な処理は課題やデータに依存するため、万能の1手順を示すページではありません。"
page_highlights:
  - "参照法、フィルタ、アーティファクト処理、除外基準が結果を変えます。"
  - "きれいな図だけでなく、何をどう処理したかを残すことが重要です。"
  - "QC は面倒な前処理ではなく、再現性の一部です。"
known_points:
  - "EEG はノイズの影響を受けやすく、前処理の違いで結果が変わりやすいです。"
  - "参照法、フィルタ、アーティファクト除去、除外基準は最低限残すべき情報です。"
  - "QC ログがない結果は、見た目がよくても追試しにくくなります。"
unknown_points:
  - "どの処理がどの課題で最も良いかは、データと目的に依存します。"
  - "EEG だけでどこまで因果構造の推定に迫れるかは、前処理だけでは解決しません。"
wiki_links:
  - label: "Wiki: EEGの基本"
    url: "/wiki/eeg-basics.html"
    description: "信号そのものの性質から戻りたいときはこちらです。"
  - label: "Wiki: 検証基盤の基本"
    url: "/wiki/verification-basics.html"
    description: "なぜ QC が再現性に直結するかを、運用の側から補います。"
  - label: "Wiki Home"
    url: "/wiki/"
    description: "他の基礎ページへ戻れます。"
recommended_pages:
  - label: "EEG入門"
    url: "/eeg_101.html"
  - label: "ハンズオン"
    url: "/datasets.html#l0-practice"
  - label: "データ&ベンチ"
    url: "/datasets.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>前処理で何が起きるのか</h2>
<p>
EEG は、脳の信号だけでなく、まばたき、筋電、体動、電源ノイズ、電極接触の問題なども一緒に入ってきます。だから、前処理は「見栄えを整える作業」ではなく、<strong>何を信号として扱うかを決める作業</strong>です。
</p>
</div>

<section class="section" id="four-points">
<h2 class="section-title">まず意識したい4点</h2>
<table class="data-table">
<thead>
<tr>
<th>論点</th>
<th>何が変わるか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>参照法</strong></td>
<td>どの基準と比べるかで、見える波形の形が変わります。</td>
</tr>
<tr>
<td><strong>フィルタ</strong></td>
<td>残す周波数帯を変えると、強調される情報と消える情報が変わります。</td>
</tr>
<tr>
<td><strong>アーティファクト処理</strong></td>
<td>眼球や筋電をどこまで除くかで、残る信号の解釈が変わります。</td>
</tr>
<tr>
<td><strong>除外基準</strong></td>
<td>どのデータを外したかで、最終結果の分布や難しさが変わります。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-log">
<h2 class="section-title">なぜログを残すのか</h2>
<p>
同じデータでも、前処理が違えば結果が変わることがあります。そのため、「この条件で、この結果になった」という再現可能な記録が必要です。最低限、参照法、フィルタ設定、アーティファクト処理、除外基準、失敗例は残すべきです。
</p>
<div class="key-points">
<h4>最低限残したい項目</h4>
<ul>
<li><strong>参照法：</strong>平均参照か、特定電極参照か。</li>
<li><strong>フィルタ：</strong>高域・低域・ノッチの設定。</li>
<li><strong>アーティファクト処理：</strong>ICA などを使ったか、どの成分を除いたか。</li>
<li><strong>除外基準：</strong>どの閾値で、どのチャンネルや区間を外したか。</li>
</ul>
</div>
</section>

<section class="section" id="what-not-do">
<h2 class="section-title">やりがちな誤解</h2>
<table class="data-table">
<thead>
<tr>
<th>誤解</th>
<th>実際には</th>
</tr>
</thead>
<tbody>
<tr>
<td>きれいな図が出たから十分</td>
<td>見た目がきれいでも、どう処理したかが残っていなければ再現性は弱いです。</td>
</tr>
<tr>
<td>1つの前処理が常に最適</td>
<td>課題やデータの性質で、よい設定は変わります。</td>
</tr>
<tr>
<td>QC は最後に見るもの</td>
<td>QC は最初から最後まで、入力の信頼性を支える作業です。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="next-step">
<h2 class="section-title">次にどこへ戻るか</h2>
<p>
EEG の信号そのものをもう一度確認したい場合は <a href="eeg-basics.html">EEGの基本</a>、実際の作業手順へ戻りたい場合は <a href="../datasets.html#l0-practice">Hands-on</a>、公開データ選びへ戻りたい場合は <a href="../datasets.html">Datasets</a> が自然です。
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="eeg-basics.html">EEGの基本 →</a></li>
<li><a href="verification-basics.html">検証基盤の基本 →</a></li>
<li><a href="roadmap-reading-guide.html">ロードマップの読み方 →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../eeg_101.html">EEG 101 →</a></li>
<li><a href="../datasets.html#l0-practice">ハンズオン →</a></li>
<li><a href="../datasets.html">データ&ベンチ →</a></li>
</ul>
</div>
</aside>
</main>
