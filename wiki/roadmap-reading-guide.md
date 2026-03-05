---
layout: default
title: "Wiki：ロードマップの読み方"
description: "P/M/R/I/V/D の記号が何を意味し、どういう順で読むと迷いにくいかを説明する補助ページです。"
article_type: Wiki
subtitle: "技術ロードマップを『長い一覧』ではなく『依存関係の地図』として読む"
author: Mind Uploading Research Project
last_updated: "2026-03-06"
note: "Reading guide"
audience: "技術ロードマップの記号が多くて迷う人、読む順番を知りたい人"
reading_time: "8〜12分"
page_intro: "このページは、技術ロードマップの P/M/R/I/V/D が何を意味し、どこから読むと迷いにくいかを説明する補助ページです。ロードマップ本文を要約し直すのではなく、『地図の読み方』そのものを整理します。"
accuracy_note: "このページは読み方の補助です。正式な論点一覧や現時点の整理は、必ず技術ロードマップ本文へ戻って確認してください。"
page_highlights:
  - "P/M/R/I/V/D を、ただの記号ではなく『問いの種類』として説明します。"
  - "どの順番で詰まりやすいか、なぜ前の層を飛ばせないかを示します。"
  - "興味別に読む入り口も分けています。"
known_points:
  - "P は前進の定義、M は計測、R は再構成、I は実装、V は検証、D は社会実装という役割分担です。"
  - "強い主張ほど後ろにあり、前の層の未整理を飛ばして進めません。"
  - "ロードマップは結論集ではなく依存関係の地図として読むのが適切です。"
unknown_points:
  - "どの経路が最短で有効かは、今後のデータ・ベンチ整備で変わり得ます。"
  - "V と D の最終条件は、まだ未解決問題を多く含みます。"
wiki_links:
  - label: "Wiki: WBEの基本"
    url: "/wiki/mind-upload-basics.html"
    description: "この地図が何のために要るのか、全体像から見たい人向けです。"
  - label: "Wiki: 検証基盤の基本"
    url: "/wiki/verification-basics.html"
    description: "V 系列で何を固定したいのかを補います。"
  - label: "Wiki Home"
    url: "/wiki/"
    description: "他の基礎ページへ戻れます。"
recommended_pages:
  - label: "技術ロードマップ"
    url: "/tech_roadmap.html"
  - label: "WBE入門"
    url: "/wbe_101.html"
  - label: "検証基盤"
    url: "/verification.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>まず一言でいうと</h2>
<p>
技術ロードマップは「何を先に解かないと、その先の話が崩れるか」を並べた地図です。長い一覧に見えても、実際には「前提 → 計測 → 推定 → 実装 → 検証 → 社会実装」という依存関係を表しています。
</p>
</div>

<section class="section" id="letters">
<h2 class="section-title">P/M/R/I/V/D を日常語にする</h2>
<table class="data-table">
<thead>
<tr>
<th>記号</th>
<th>何の問いか</th>
<th>これが抜けると何が困るか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>P</strong></td>
<td>何を成功と呼ぶか</td>
<td>目標が定まらず、後から都合よく勝利条件を変えられてしまいます。</td>
</tr>
<tr>
<td><strong>M</strong></td>
<td>何をどの精度で測れるか</td>
<td>そもそも入力に何が入っているか分かりません。</td>
</tr>
<tr>
<td><strong>R</strong></td>
<td>観測から何を推定できるか</td>
<td>測れた信号を、必要以上に強い意味へ読み替えてしまいます。</td>
</tr>
<tr>
<td><strong>I</strong></td>
<td>そのモデルをどう動かすか</td>
<td>紙の上ではよく見えても、実際には回らない可能性があります。</td>
</tr>
<tr>
<td><strong>V</strong></td>
<td>何をどう確かめるか</td>
<td>前進したのか、見かけだけなのかを区別できません。</td>
</tr>
<tr>
<td><strong>D</strong></td>
<td>社会でどう扱うか</td>
<td>技術が動いても、権利や安全の面で運用できません。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="routes">
<h2 class="section-title">興味別の読み順</h2>
<table class="data-table">
<thead>
<tr>
<th>いま気になること</th>
<th>まず読む記号</th>
<th>次に追う記号</th>
</tr>
</thead>
<tbody>
<tr>
<td>何を達成したら前進か知りたい</td>
<td><strong>P</strong></td>
<td><strong>V</strong></td>
</tr>
<tr>
<td>EEG や fMRI の限界から入りたい</td>
<td><strong>M</strong></td>
<td><strong>R</strong></td>
</tr>
<tr>
<td>モデルがどう動くか知りたい</td>
<td><strong>R</strong></td>
<td><strong>I</strong></td>
</tr>
<tr>
<td>本人性や社会制度まで見たい</td>
<td><strong>V</strong></td>
<td><strong>D</strong></td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="not-timeline">
<h2 class="section-title">これは年表ではなく依存関係です</h2>
<p>
P → M → R → I → V → D と並んでいても、「必ずこの年にここまで行く」という意味ではありません。大事なのは、後ろの主張ほど前の層の失敗に弱いということです。たとえば、M と R が曖昧なまま V で強い本人性主張へ進むと、入力の限界や推定の不確実性がそのまま残ります。
</p>
<div class="cta-box">
<h4>Next</h4>
<p>正式な論点一覧と索引は、技術ロードマップ本文で確認してください。</p>
<a href="../tech_roadmap.html">技術ロードマップへ →</a>
</div>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="mind-upload-basics.html">WBEの基本 →</a></li>
<li><a href="verification-basics.html">検証基盤の基本 →</a></li>
<li><a href="eeg-preprocessing-and-qc.html">EEG前処理とQC →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../tech_roadmap.html">技術ロードマップ →</a></li>
<li><a href="../verification.html">検証基盤 →</a></li>
<li><a href="../wbe_101.html">WBE 101 →</a></li>
</ul>
</div>
</aside>
</main>
