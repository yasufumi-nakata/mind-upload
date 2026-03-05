---
layout: default
title: "Wiki：規格・置き場・Validator・ベンチマーク"
description: "BIDS のような規格、OpenNeuro のような置き場、Validator、Benchmark の役割差を初歩から整理します。"
article_type: Wiki
subtitle: "似て見える4つの役割は、やっている仕事が違います"
author: Mind Uploading Research Project
last_updated: "2026-03-06"
note: "Learning guide"
audience: "BIDS、OpenNeuro、PhysioNet、Validator、Benchmark が同じ種類のものに見える人"
reading_time: "10〜15分"
page_intro: "このページは、Mind-Upload で何度も出てくる『規格』『置き場』『Validator』『ベンチマーク』の役割差を、初歩から整理する wiki です。名前だけ覚えるのではなく、『何をそろえる道具なのか』を分けて理解することを目標にします。"
accuracy_note: "ここで説明するのは役割の基本整理です。どの規格やどのベンチマークが最終的に WBE に十分かの結論を与えるページではありません。"
page_highlights:
  - "BIDS は規格、OpenNeuro や PhysioNet は置き場、Validator は機械検査、Benchmark は比較ルールです。"
  - "raw ファイルを置いただけでは、比較可能な前進にはなりません。"
  - "この 4 つがそろうと、他人が追試しやすくなります。"
known_points:
  - "研究を比較可能にするには、データの形、公開先、検査手段、評価ルールを分けて整える必要があります。"
  - "BIDS と EEG-BIDS は『どう置くか』の規格であり、採点ルールそのものではありません。"
  - "OpenNeuro や PhysioNet は公開基盤ですが、入力形式や評価手順を自動で全部保証するわけではありません。"
unknown_points:
  - "WBE 向けの最終的な共通 benchmark がどの粒度であるべきかは未確定です。"
  - "どの validator や監査項目を最終標準にするかは、今後の運用設計に依存します。"
wiki_links:
  - label: "Wiki: 検証基盤の基本"
    url: "/wiki/verification-basics.html"
    description: "標準、ベンチ、登録、監査の大きな地図へ戻れます。"
  - label: "Wiki: ベースライン・事前登録・モデルカード"
    url: "/wiki/baselines-prereg-and-model-cards.html"
    description: "Benchmark の先にある運用語の違いを補います。"
  - label: "Wiki: イベント同期と観測ログ"
    url: "/wiki/event-sync-and-measurement-logs.html"
    description: "規格に入れたいログ情報の具体例を補います。"
  - label: "Wiki Home"
    url: "/wiki/"
    description: "他の補助ページへ戻れます。"
recommended_pages:
  - label: "データ&ベンチ"
    url: "/datasets.html"
  - label: "検証基盤"
    url: "/verification.html"
  - label: "ケースワーク"
    url: "/casework.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>いちばん短い区別</h2>
<p>
<strong>規格</strong>は「どういう形でそろえるか」、<strong>置き場</strong>は「どこへ公開するか」、<strong>Validator</strong>は「規格どおりかを機械で確かめる道具」、<strong>ベンチマーク</strong>は「何で比べるか」のルールです。同じ『研究基盤』でも役割は別です。
</p>
</div>

<section class="section" id="why-separate">
<h2 class="section-title">なぜ分けて考えるのか</h2>
<p>
この 4 つを混同すると、「OpenNeuro に上げたから benchmark がある」「BIDS だから比較まで済んでいる」といった読み違いが起きます。実際には、データの形をそろえる仕事と、比較のルールを作る仕事は別です。
</p>
</section>

<section class="section" id="terms">
<h2 class="section-title">まず用語を分ける</h2>
<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>何をするものか</th>
<th>例</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>規格（standard）</strong></td>
<td>ファイルの置き方、名前、メタデータの書き方をそろえます。</td>
<td>BIDS、EEG-BIDS です。</td>
</tr>
<tr>
<td><strong>置き場 / 共有基盤（repository）</strong></td>
<td>データを公開し、他の人が取得できるようにします。</td>
<td>OpenNeuro、PhysioNet、PDB などです。</td>
</tr>
<tr>
<td><strong>Validator</strong></td>
<td>規格違反や不足メタデータを機械で点検します。</td>
<td>BIDS Validator です。</td>
</tr>
<tr>
<td><strong>ベンチマーク（benchmark）</strong></td>
<td>課題、分割、指標、禁止事項を固定して比較可能にします。</td>
<td>MOABB、MLPerf、ImageNet 型の運用です。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="eeg-example">
<h2 class="section-title">EEG の例で見ると</h2>
<table class="data-table">
<thead>
<tr>
<th>段階</th>
<th>そこでやること</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. 規格へそろえる</strong></td>
<td>EEG ファイル、events.tsv、channels.tsv、メタデータを BIDS 形へそろえます。</td>
</tr>
<tr>
<td><strong>2. Validator で点検する</strong></td>
<td>規格違反や不足項目を機械的に洗い出します。</td>
</tr>
<tr>
<td><strong>3. 置き場へ公開する</strong></td>
<td>OpenNeuro や PhysioNet のような共有基盤に載せ、第三者が取得できるようにします。</td>
</tr>
<tr>
<td><strong>4. ベンチマークで比べる</strong></td>
<td>同じ train/test 分割、同じ指標、同じベースラインでモデルを比較します。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>ここが重要です</strong>
<p>
規格にそろえただけでは、まだ「比べるルール」はありません。逆に benchmark だけあっても、入力の形がバラバラなら比較が崩れます。両方必要です。
</p>
</div>
</section>

<section class="section" id="missing-piece">
<h2 class="section-title">何が欠けると何が困るか</h2>
<table class="data-table">
<thead>
<tr>
<th>欠けるもの</th>
<th>起きやすい問題</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>規格</strong></td>
<td>ファイル名やメタデータが人ごとに違い、追試の入口で止まります。</td>
</tr>
<tr>
<td><strong>置き場</strong></td>
<td>存在を知っても入手や再利用ができず、比較の輪が広がりません。</td>
</tr>
<tr>
<td><strong>Validator</strong></td>
<td>規格違反に気づくのが遅れ、共有直前や再解析時に事故が出ます。</td>
</tr>
<tr>
<td><strong>ベンチマーク</strong></td>
<td>各自が違う分割や指標で評価し、「勝った」の意味が揺れます。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="raw-is-not-enough">
<h2 class="section-title">raw ファイルだけでは足りない理由</h2>
<p>
波形ファイルを置いただけでは、規格も benchmark も十分ではありません。少なくとも、イベント定義、刺激ログ、同期情報、QC ログ、除外理由がないと、同じ課題として追試しにくくなります。
</p>
<div class="note-box">
<strong>安全な読み方</strong>
<p>
「公開されている」ことと「比較可能である」ことは別です。公開は入口、比較可能性はその次の設計です。
</p>
</div>
</section>

<section class="section" id="common-confusions">
<h2 class="section-title">ありがちな混同</h2>
<table class="data-table">
<thead>
<tr>
<th>言いがちなこと</th>
<th>より正確な言い換え</th>
</tr>
</thead>
<tbody>
<tr>
<td>「BIDS にしたので benchmark がある」</td>
<td>BIDS は入力形式の規格であり、比較ルールそのものではありません。</td>
</tr>
<tr>
<td>「OpenNeuro に置いたので標準化された」</td>
<td>置き場に載せても、規格やメタデータが十分とは限りません。</td>
</tr>
<tr>
<td>「Validator が通ったので研究として十分」</td>
<td>Validator は形式点検であり、研究の妥当性や benchmark の強さまでは保証しません。</td>
</tr>
<tr>
<td>「ベンチマークに勝ったので実運用も十分」</td>
<td>benchmark は比較の物差しであり、実運用や L4/L5 の成立を自動では保証しません。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="how-to-read">
<h2 class="section-title">強い主張を読むときの 3 問</h2>
<ol>
<li><strong>入力の規格は何か：</strong>BIDS などで形がそろっているかを確認します。</li>
<li><strong>どこに置かれているか：</strong>第三者が取得し直せる repository があるかを見ます。</li>
<li><strong>何で比べているか：</strong>benchmark、分割、指標、禁止事項が固定されているかを見ます。</li>
</ol>
</section>

<section class="section" id="return">
<h2 class="section-title">次にどこへ戻るか</h2>
<p>
実務の入口へ戻るなら <a href="../datasets.html">データ&ベンチ</a>、全体設計へ戻るなら <a href="../verification.html">検証基盤</a>、他分野の実例へ戻るなら <a href="../casework.html">ケースワーク</a> をご利用ください。
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="verification-basics.html">検証基盤の基本 →</a></li>
<li><a href="baselines-prereg-and-model-cards.html">ベースライン・事前登録・モデルカード →</a></li>
<li><a href="event-sync-and-measurement-logs.html">イベント同期と観測ログ →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../datasets.html">データ&ベンチ →</a></li>
<li><a href="../verification.html">検証基盤 →</a></li>
<li><a href="../casework.html">ケースワーク →</a></li>
</ul>
</div>
</aside>
</main>
