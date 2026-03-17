---
layout: default
title: "Wiki：検証基盤の基本"
description: "なぜ WBE の話で標準、ベンチ、事前登録、監査が必要なのかを初歩から説明し、Observability Budget / maintenance-state error budget / Temporal Validity Card / Calibration & Abstention Card などの役割差も整理します。"
article_type: Wiki
subtitle: "派手な主張より先に、物差しと記録の置き場を作る"
author: Mind Uploading Research Project
last_updated: "2026-03-17"
note: "Beginner guide"
audience: "Verification Commons の考え方を初歩から理解したい人"
reading_time: "10〜15分"
page_intro: "このページは、Mind-Upload がなぜ『標準・ベンチ・登録・監査』を中心に据えているのかを初歩から説明する wiki です。技術の中身だけでなく、比較可能な前進を作るための運用面を学ぶことが目的です。"
accuracy_note: "ここで使うたとえは理解の補助です。たとえで分かった気にならず、実際の設計は公開ページの仕様へ戻って確認してください。"
page_highlights:
  - "データがあるだけでは、比較可能な前進になりません。"
  - "標準、ベンチ、事前登録、監査は、互いに役割が違います。"
  - "監査も 1 枚ではなく、何を直接見たか、何が未観測か、どの maintenance route を実際に見たか、何日持つか、低信頼時にどう止まるかで役割が分かれます。"
  - "WBE のように主張が大きい分野ほど、運用面の厳しさが重要になります。"
known_points:
  - "比較可能な前進には、入力、評価、ルール、記録の4つが必要です。"
  - "事前登録や監査がないと、あとから都合よく成功条件を変えられてしまいます。"
  - "Observation、latent state、maintenance route、time horizon、confidence semantics は別 failure mode なので、site-wide では別の card に分けて管理します。"
  - "PDB や BIDS など、他分野でも公共財の整備が進歩を加速してきました。"
unknown_points:
  - "WBE 専用の最終ベンチマークが、まだ完成した形で存在するわけではありません。"
  - "どの追加要件が L4 や L5 に十分かは、まだ研究と社会議論の途中です。"
wiki_links:
  - label: "Wiki: 主張と証拠の読み方"
    url: "/wiki/claims-and-evidence.html"
    description: "この基盤が、なぜ主張の読み分けに必要かを説明します。"
  - label: "Wiki: WBEの基本"
    url: "/wiki/mind-upload-basics.html"
    description: "全体像から戻って読みたい人向けです。"
  - label: "Wiki: ベースライン・事前登録・モデルカード"
    url: "/wiki/baselines-prereg-and-model-cards.html"
    description: "運用語の役割差を、初歩から整理します。"
  - label: "Wiki Home"
    url: "/wiki/"
    description: "他の基礎ページへ戻れます。"
recommended_pages:
  - label: "検証基盤"
    url: "/verification.html"
  - label: "ケースワーク"
    url: "/verification.html#casework"
  - label: "データ&ベンチ"
    url: "/datasets.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>なぜ「物差し」が先なのか</h2>
<p>
もし学校のテストで、答案用紙も採点基準も違うまま「こっちの方が賢い」と比べたら、結果は信用しにくくなります。WBE でも同じで、データ、評価、失敗条件、記録の置き場がそろわないと、「前進した」と言っても比べられません。
</p>
</div>

<section class="section" id="four-parts">
<h2 class="section-title">4つの部品を学校のテストでたとえる</h2>
<table class="data-table">
<thead>
<tr>
<th>部品</th>
<th>役割</th>
<th>たとえ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>標準（Data Standard）</strong></td>
<td>入力の形をそろえる</td>
<td>同じ答案用紙です。</td>
</tr>
<tr>
<td><strong>ベンチマーク（Benchmark）</strong></td>
<td>比べる課題と指標をそろえる</td>
<td>同じ採点基準です。</td>
</tr>
<tr>
<td><strong>事前登録（Registry / Prereg）</strong></td>
<td>やる前にルールを固定する</td>
<td>試験前に配られる実施要項です。</td>
</tr>
<tr>
<td><strong>監査（Audit / Model Card）</strong></td>
<td>失敗例や弱点まで残す</td>
<td>点数だけでなく、ミスや再試験条件も載った成績表です。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="site-cards">
<h2 class="section-title">監査は 1 枚では足りません</h2>
<p>
今回この入門ページで補うべきだった弱点は、<strong>監査</strong> を 1 箱にまとめすぎ、公開サイトで実際に使っている提出物の役割差が見えにくかった点でございます。Mind-Upload では、<strong>何を直接見たか</strong>、<strong>どう結び付けたか</strong>、<strong>何がまだ未観測か</strong>、<strong>どの maintenance route を実際に見たか</strong>、<strong>何日・何状態まで持つか</strong>、<strong>低信頼時にどう止まるか</strong> を別々に残します。
</p>
<table class="data-table">
<thead>
<tr>
<th>card / 仕様</th>
<th>何を固定するか</th>
<th>これが無いと起きる誤読</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="../verification.html#observability-budget"><strong>Observability Budget</strong></a></td>
<td>何が direct で、何が proxy で、何がまだ latent かを固定します。</td>
<td><code>multimodal だから全部見えた</code>、<code>proxy だから neural truth</code> と読みやすくなります。</td>
</tr>
<tr>
<td><a href="../verification.html#fusion-card"><strong>Fusion Card</strong></a></td>
<td>複数モダリティをどう結び付け、どの transfer assumption が残るかを固定します。</td>
<td><code>統合したから mechanism も分かった</code> と読みやすくなります。</td>
</tr>
<tr>
<td><a href="../verification.html#latent-state-error-budget"><strong>latent-state error budget</strong></a></td>
<td>どの hidden state が、いまの claim をまだ止めているかを固定します。</td>
<td><code>connectome-only でもかなり十分</code>、<code>same-day fit で hidden state も埋まった</code> と読みやすくなります。</td>
</tr>
<tr>
<td><a href="../verification.html#intervention-card"><strong>Intervention Card</strong></a></td>
<td>何を、どの trigger と comparator と timing で実際に変えたかを固定します。</td>
<td><code>よく当たったから causal</code> と読みやすくなります。</td>
</tr>
<tr>
<td><a href="../verification.html#temporal-validity-card"><strong>Temporal Validity Card</strong></a></td>
<td>その結果を何日・何状態・何回の再較正まで外挿できるかを固定します。</td>
<td><code>same-day high score = chronic deployable</code> と読みやすくなります。</td>
</tr>
<tr>
<td><a href="../verification.html#maintenance-state-error-budget"><strong>maintenance-state error budget</strong></a></td>
<td>controller state、sleep / wake history、support-state proxy のどこを direct / proxy / omitted で扱ったかを固定します。</td>
<td><code>cross-day で持った = maintenance も揃った</code>、<code>human proxy がある = cell-specific maintenance route も見えた</code> と読みやすくなります。</td>
</tr>
<tr>
<td><a href="../verification.html#calibration-abstention-card"><strong>Calibration &amp; Abstention Card</strong></a></td>
<td>confidence、interval、prediction set、fallback、abstention の意味を固定します。</td>
<td><code>high confidence = safe</code>、<code>threshold を付けたから reliable</code> と読みやすくなります。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>学校のテストの比喩で言うと</strong>
<p>
答案用紙と採点基準だけでは足りません。<strong>どの問題を直接見たか</strong>、<strong>カンニングになりうる補助線をどこまで使ったか</strong>、<strong>翌週も同じ点が取れるか</strong>、<strong>自信がないときに「分からない」と言えたか</strong>まで別々に記録して、初めて比較可能な成績表になります。
</p>
</div>
</section>

<section class="section" id="missing">
<h2 class="section-title">どれか1つ欠けると何が起こるか</h2>
<table class="data-table">
<thead>
<tr>
<th>欠けるもの</th>
<th>起こる問題</th>
</tr>
</thead>
<tbody>
<tr>
<td>標準</td>
<td>同じ入力を見ているのか分からなくなります。</td>
</tr>
<tr>
<td>ベンチマーク</td>
<td>誰もが別の物差しで勝ったと言えてしまいます。</td>
</tr>
<tr>
<td>事前登録</td>
<td>あとから都合のよい条件だけを選んで成功扱いしやすくなります。</td>
</tr>
<tr>
<td>監査</td>
<td>点数だけが独り歩きし、弱点やリークが見えなくなります。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="why-wbe-needs-this">
<h2 class="section-title">なぜ WBE では特に重要なのか</h2>
<p>
WBE は、話が大きい分だけ、レベルのすり替えが起きやすい分野です。L1 の結果を L4 のように語る、相関を因果のように見せる、部分的な成功を全体の成立のように扱う、といった事故が起きやすくなります。だからこそ、結果だけでなく<strong>どう評価したか</strong>を固定する必要があります。
</p>
</section>

<section class="section" id="site-link">
<h2 class="section-title">このサイトでの使われ方</h2>
<p>
Mind-Upload では、Verification ページが設計図、Hands-on が最小実装、Datasets が入口データ、Casework が他分野の先例です。wiki は、その前提知識を補うためにあります。
</p>
<p>ベースライン、事前登録、モデルカード、失敗例の役割差をもう一段ていねいに整理したい場合は <a href="baselines-prereg-and-model-cards.html">Wiki: ベースライン・事前登録・モデルカード</a>、計測から推定、妥当化、運用までの流れを用語ごとにつなげて見たい場合は <a href="measurement-and-modeling-terms.html">Wiki: 計測からモデル化までの用語ガイド</a> が補講になります。</p>
<div class="cta-box">
<h4>Next</h4>
<p>この基礎を読んだあとで、実際の設計図を見たい場合はこちらです。</p>
<a href="../verification.html">検証基盤ページへ →</a>
</div>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="mind-upload-basics.html">WBEの基本 →</a></li>
<li><a href="claims-and-evidence.html">主張と証拠の読み方 →</a></li>
<li><a href="eeg-basics.html">EEGの基本 →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../verification.html">Verification →</a></li>
<li><a href="../datasets.html">データ&ベンチ →</a></li>
<li><a href="../verification.html#casework">ケースワーク →</a></li>
</ul>
</div>
</aside>
</main>
