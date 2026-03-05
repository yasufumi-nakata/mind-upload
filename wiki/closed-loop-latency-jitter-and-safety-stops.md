---
layout: default
title: "Wiki：閉ループ・遅延・ジッタ・安全停止"
description: "閉ループ評価で重要になる遅延、ジッタ、ドリフト、安全停止、棄権の違いを初歩から整理します。"
article_type: Wiki
subtitle: "オフライン精度が高くても、リアルタイムで安定とは限りません"
author: Mind Uploading Research Project
last_updated: "2026-03-06"
note: "Learning guide"
audience: "L3 の閉ループ評価やリアルタイム運用の意味が曖昧な人"
reading_time: "10〜15分"
page_intro: "このページは、Mind-Upload の L3『閉ループ』で重要になる遅延、ジッタ、ドリフト、安全停止、棄権の違いを初歩から整理する wiki です。オフラインで高精度だったモデルが、なぜそのままリアルタイム系では強い主張にならないのかを分けて理解することを目標にします。"
accuracy_note: "ここで示すのは閉ループ評価の基本整理です。許容遅延や安全停止の閾値は課題依存であり、固定値を与えるページではありません。"
page_highlights:
  - "オフライン精度と閉ループ安定性は別の話です。"
  - "遅延、ジッタ、ドリフトは似ていますが、壊し方が違います。"
  - "棄権、freeze、緊急停止は、全部『止める』でも役割が違います。"
known_points:
  - "閉ループでは、出力が環境を変え、その結果がまた次の入力に戻ってきます。"
  - "遅延やジッタが大きいと、オフラインでは見えない不安定さが出ます。"
  - "安全停止は、性能評価とは別に事前設計しておく必要があります。"
unknown_points:
  - "どの課題で何 ms の遅延やどの程度のジッタまで許容できるかは未確定です。"
  - "閉ループの安定性が、どこまで本人性や意識の主張に必要十分かは未解決です。"
wiki_links:
  - label: "Wiki: イベント同期と観測ログ"
    url: "/wiki/event-sync-and-measurement-logs.html"
    description: "遅延、ジッタ、ドリフトの記録方法を補います。"
  - label: "Wiki: 不確実性・信頼区間・棄権"
    url: "/wiki/uncertainty-confidence-and-abstention.html"
    description: "低信頼時に何もしない設計の考え方を補います。"
  - label: "Wiki: 更新・分岐・停止規則"
    url: "/wiki/update-branching-and-stop-rules.html"
    description: "停止規則やキルスイッチの運用語を補います。"
  - label: "Wiki Home"
    url: "/wiki/"
    description: "他の補助ページへ戻れます。"
recommended_pages:
  - label: "検証基盤"
    url: "/verification.html"
  - label: "EEG入門"
    url: "/eeg_101.html"
  - label: "技術ロードマップ"
    url: "/tech_roadmap.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>いちばん短い区別</h2>
<p>
<strong>閉ループ</strong>は「出力が次の入力を変える系」です。ここでは、<strong>遅延</strong>は毎回のずれ、<strong>ジッタ</strong>はそのずれの揺れ、<strong>ドリフト</strong>は長時間での時計ずれです。さらに、<strong>棄権</strong>は低信頼時に何もしないこと、<strong>安全停止</strong>は危険時に止めることです。
</p>
</div>

<section class="section" id="why-offline-is-not-enough">
<h2 class="section-title">なぜオフライン精度だけでは足りないのか</h2>
<p>
オフライン評価では、すでに記録されたデータをあとから処理します。これに対して閉ループでは、モデルの出力が環境や次の入力を変えます。したがって、同じモデルでも、遅延やジッタが入るだけで挙動が崩れることがあります。
</p>
<div class="note-box">
<strong>安全な読み方</strong>
<p>
「オフラインで 95% 出た」ことと、「リアルタイムで安定に動く」ことは別の主張です。前者が L1/L2 の入口でも、後者は L3 の追加課題です。
</p>
</div>
</section>

<section class="section" id="terms">
<h2 class="section-title">まず 4 つを分ける</h2>
<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>意味</th>
<th>起きやすい問題</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>遅延</strong></td>
<td>入力から出力まで、平均して何 ms かかるかです。</td>
<td>反応が遅れて、制御や同期がずれます。</td>
</tr>
<tr>
<td><strong>ジッタ</strong></td>
<td>その遅延が毎回どれくらい揺れるかです。</td>
<td>同じ条件でも応答時刻がぶれ、安定性が落ちます。</td>
</tr>
<tr>
<td><strong>ドリフト</strong></td>
<td>長時間で時計やタイミングのずれが積み重なることです。</td>
<td>前半と後半で同期誤差が変わり、比較が崩れます。</td>
</tr>
<tr>
<td><strong>再較正（recalibration）</strong></td>
<td>条件変化や劣化に応じて、設定やモデルを調整することです。</td>
<td>頻繁に必要なら、その系は安定に動いていない可能性があります。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="end-to-end">
<h2 class="section-title">何を end-to-end で測るのか</h2>
<table class="data-table">
<thead>
<tr>
<th>区間</th>
<th>最低限知りたいこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>観測</strong></td>
<td>センサーや取得系が、いつ信号を受け取ったか。</td>
</tr>
<tr>
<td><strong>処理</strong></td>
<td>前処理、推定、意思決定にどれだけ時間がかかったか。</td>
</tr>
<tr>
<td><strong>出力</strong></td>
<td>表示、刺激、制御信号がいつ実際に出たか。</td>
</tr>
<tr>
<td><strong>戻り</strong></td>
<td>その出力の影響が、いつ次の入力へ返ってきたか。</td>
</tr>
</tbody>
</table>
<p>
閉ループでは、途中の平均時間だけでなく、<strong>全経路の end-to-end 遅延</strong>を見る必要があります。処理が速くても、表示遅延や通信遅延で全体が遅ければ、系としては遅いままです。
</p>
</section>

<section class="section" id="stops">
<h2 class="section-title">棄権と freeze と安全停止は別物</h2>
<table class="data-table">
<thead>
<tr>
<th>仕組み</th>
<th>主目的</th>
<th>例</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>棄権</strong></td>
<td>低信頼のとき、無理に出力しないためです。</td>
<td>分類確信度が低いときに「不明」と返すことです。</td>
</tr>
<tr>
<td><strong>freeze / 一時停止</strong></td>
<td>再較正や原因確認のために、挙動を一時保留するためです。</td>
<td>同期異常を検出して、更新を止めてログ確認へ入ることです。</td>
</tr>
<tr>
<td><strong>安全停止 / containment</strong></td>
<td>危険な動作や逸脱を防ぐためです。</td>
<td>上限遅延や異常振幅を超えたときに即停止することです。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>ここが重要です</strong>
<p>
低信頼なので出さない、壊れたかもしれないので保留する、危険なので止める、は全部違います。全部まとめて「止めた」で済ませると、性能問題と安全問題が混ざります。
</p>
</div>
</section>

<section class="section" id="logs">
<h2 class="section-title">最低限残したいログ</h2>
<div class="key-points">
<h4>Checklist</h4>
<ul>
<li><strong>end-to-end 遅延：</strong>平均だけでなく分布も残します。</li>
<li><strong>ジッタ：</strong>毎回のばらつきがどれくらいあるか。</li>
<li><strong>ドロップや欠損：</strong>フレーム落ち、試行落ち、同期失敗。</li>
<li><strong>再較正イベント：</strong>いつ調整を入れたか、なぜ入れたか。</li>
<li><strong>棄権率：</strong>低信頼でどれだけ何もしなかったか。</li>
<li><strong>停止トリガー：</strong>どの条件で freeze や安全停止が発動したか。</li>
</ul>
</div>
</section>

<section class="section" id="how-to-read">
<h2 class="section-title">L3 の主張を読むときの 3 問</h2>
<ol>
<li><strong>オフライン精度と閉ループ安定性を分けて報告しているか：</strong>片方だけで両方を言っていないかを見ます。</li>
<li><strong>遅延、ジッタ、ドリフトを end-to-end で測っているか：</strong>途中の一部だけで安心していないかを確認します。</li>
<li><strong>棄権、freeze、安全停止の条件が書かれているか：</strong>危険時の扱いが曖昧でないかを見ます。</li>
</ol>
</section>

<section class="section" id="return">
<h2 class="section-title">次にどこへ戻るか</h2>
<p>
L3 の全体設計へ戻るなら <a href="../verification.html">検証基盤</a>、EEG と同期の実務へ戻るなら <a href="../eeg_101.html">EEG入門</a>、Roadmap の I1 / I8 へ戻るなら <a href="../tech_roadmap.html">技術ロードマップ</a> をご利用ください。
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="event-sync-and-measurement-logs.html">イベント同期と観測ログ →</a></li>
<li><a href="uncertainty-confidence-and-abstention.html">不確実性・信頼区間・棄権 →</a></li>
<li><a href="update-branching-and-stop-rules.html">更新・分岐・停止規則 →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../verification.html">検証基盤 →</a></li>
<li><a href="../eeg_101.html">EEG入門 →</a></li>
<li><a href="../tech_roadmap.html">技術ロードマップ →</a></li>
</ul>
</div>
</aside>
</main>
