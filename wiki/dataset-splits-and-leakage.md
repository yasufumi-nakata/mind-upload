---
layout: default
title: "Wiki：データ分割とデータリーク"
description: "train/test の分け方、被験者分割、時間分割、patient/session/report leakage を初歩から説明します。"
article_type: Wiki
subtitle: "高い精度でも、分け方が甘いと評価は壊れます"
author: Mind Uploading Research Project
last_updated: "2026-03-15"
note: "Practical guide"
audience: "公開データで最初の評価を作る人、リークや分割で混乱しやすい人"
reading_time: "10〜15分"
page_intro: "このページは、データセットをどう分けるか、なぜデータリークが危険かを初歩から説明する wiki です。『精度が高いのに信用できない』という事故を減らすために、最小限どこを見ればよいかを整理します。"
accuracy_note: "ここで示すのは基本原則です。最適な分割方法は課題やデータの構造に依存するため、万能の 1 ルールではありません。"
page_highlights:
  - "被験者、セッション、時間のどれを単位に分けるかで、難しさは大きく変わります。"
  - "リークは『不正行為』だけでなく、善意の前処理や分割でも起きます。"
  - "スターターデータ 4 件でも、独立単位は subject / case / night / session で違います。"
  - "まず見るべきなのは、精度そのものより分割ルールとリーク対策です。"
known_points:
  - "train/test の分け方が甘いと、精度は簡単に過大評価されます。"
  - "同じ被験者、同じセッション、近い時刻の断片が両側に入ると、見かけ上の性能が上がりやすいです。"
  - "臨床 EEG では、report text や report-derived label も leakage source になりえます。"
  - "前処理、正規化、特徴選択も、全データを見てから行うとリーク源になりえます。"
unknown_points:
  - "どの分割が最も将来の実運用に近いかは、課題設定と利用場面に依存します。"
  - "リークを完全にゼロにしたと言い切るには、データ構造の深い理解と監査が必要です。"
  - "report-derived label を signal-only benchmark からどう標準的に切り分けるかは、運用設計の途上です。"
wiki_links:
  - label: "Wiki: EEG前処理とQC"
    url: "/wiki/eeg-preprocessing-and-qc.html"
    description: "前処理そのものがどこで結果を変えるかを補います。"
  - label: "Wiki: 検証基盤の基本"
    url: "/wiki/verification-basics.html"
    description: "なぜリーク対策が『運用の一部』なのかを確認できます。"
  - label: "Wiki Home"
    url: "/wiki/"
    description: "学習用ページの全体マップへ戻れます。"
recommended_pages:
  - label: "データ&ベンチ"
    url: "/datasets.html"
  - label: "ハンズオン"
    url: "/datasets.html#l0-practice"
  - label: "検証基盤"
    url: "/verification.html"
---

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>いちばん短い説明</h2>
<p>
データ分割は「答え合わせの前に、どこまで見てよいかを先に決める」作業です。データリークは、その境界をうっかり越えてしまい、<strong>本番では使えない情報を学習や調整に混ぜてしまうこと</strong>です。
</p>
</div>

<section class="section" id="why-split-matters">
<h2 class="section-title">なぜ分割がそんなに大事なのか</h2>
<p>
学校のテストで、答えを見ながら練習した問題をそのまま本番に出せば、点数は高くなります。ですが、その点数は「本当に新しい問題を解ける力」とは言えません。機械学習でも同じで、<strong>学習時に見た情報が test 側へにじむ</strong>と、数字だけ良く見えてしまいます。
</p>
</section>

<section class="section" id="split-units">
<h2 class="section-title">まず分ける単位を意識する</h2>
<table class="data-table">
<thead>
<tr>
<th>分ける単位</th>
<th>どういう場面か</th>
<th>注意点</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>被験者単位</strong></td>
<td>新しい人に一般化できるかを見たいとき。</td>
<td>同じ人の断片が train と test に両方入ると、見かけより簡単になります。</td>
</tr>
<tr>
<td><strong>セッション単位</strong></td>
<td>同じ人でも別日に安定するかを見たいとき。</td>
<td>同日記録だけで分けると、日差や電極状態の違いを見落とします。</td>
</tr>
<tr>
<td><strong>時間単位</strong></td>
<td>未来予測や連続運用を想定するとき。</td>
<td>近い時刻の窓が両側に入ると、ほぼ同じ断片を見てしまうことがあります。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="dataset-specific-units">
<h2 class="section-title">スターターデータ 4 件で、独立単位は同じではありません</h2>
<div class="note-box">
<strong>最後の 2 列は、本サイトの運用推論です</strong>
<p>
下の表の <strong>なぜ漏れるか</strong> と <strong>安全側の分け方</strong> は、各データセットの公式説明と一次文献が示す階層構造から、本サイトが引く運用上のルールでございます。
</p>
</div>
<table class="data-table">
<thead>
<tr>
<th>データセット</th>
<th>独立単位として優先するもの</th>
<th>ありがちな誤分割</th>
<th>なぜ漏れるか</th>
<th>安全側の分け方</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG Motor Movement/Imagery</strong></td>
<td>subject、必要なら run</td>
<td>epoch / trial のランダム分割</td>
<td>同一 subject・同一 session の信号特性と cue 構造が train / test にまたがります。</td>
<td>まず subject 単位、同一 subject 内評価でも run 単位を分けます。</td>
</tr>
<tr>
<td><strong>CHB-MIT</strong></td>
<td>subject と case chronology</td>
<td>file 単位のランダム分割</td>
<td><code>chb21</code> は <code>chb01</code> と同一被験者で、file 間 gap も文脈を持つためです。</td>
<td>case ではなく subject 対応を確認し、連続順と gap を保ったまま split します。</td>
</tr>
<tr>
<td><strong>Sleep-EDF</strong></td>
<td>subject-night</td>
<td>epoch のランダム分割</td>
<td>同一夜の連続 hypnogram と subject 固有の睡眠構造が train / test にまたがります。</td>
<td>night ごと保持し、subject をまたいだ generalization か within-subject かを先に宣言します。</td>
</tr>
<tr>
<td><strong>TUH EEG / TUSZ</strong></td>
<td>patient / session</td>
<td>segment / file のランダム分割、report 併用のまま signal-only 評価</td>
<td>同一患者の複数 session と de-identified report が、ラベルへ近い情報を持つからです。</td>
<td>patient / session 単位 split と <strong>report usage flag</strong> を必須にします。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="common-leaks">
<h2 class="section-title">ありがちなリーク 5 パターン</h2>
<table class="data-table">
<thead>
<tr>
<th>ありがちな事故</th>
<th>何が起きているか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>同じ被験者の断片が両側に入る</strong></td>
<td>個人固有の癖を覚えてしまい、新しい人への一般化性能より高く見えます。</td>
</tr>
<tr>
<td><strong>近接した時間窓を混ぜる</strong></td>
<td>ほぼ同じ波形の切れ端を train/test に分けてしまい、未来予測の難しさを過小評価します。</td>
</tr>
<tr>
<td><strong>全データで正規化や特徴選択をする</strong></td>
<td>test 側の統計量を学習時に使ってしまい、情報が逆流します。</td>
</tr>
<tr>
<td><strong>モデル選択を test で繰り返す</strong></td>
<td>test が実質的に validation の役割を持ち、最後の点数が楽観的になります。</td>
</tr>
<tr>
<td><strong>重複サンプルや派生サンプルを見逃す</strong></td>
<td>元は同じ記録から切ったデータが両側に入り、独立試料でない比較になります。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="dataset-specific-traps">
<h2 class="section-title">今回追加する dataset 固有のリーク注意</h2>
<table class="data-table">
<thead>
<tr>
<th>dataset</th>
<th>今回固定する注意点</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG Motor Movement/Imagery</strong></td>
<td>cue-locked motor task なので、split を厳しくしても視覚 cue / 眼球 / 筋電寄与の監査を別に残します。</td>
</tr>
<tr>
<td><strong>CHB-MIT</strong></td>
<td>subject 数と case 数を混同しません。file をシャッフルせず、gap と chronology を runbook に固定します。</td>
</tr>
<tr>
<td><strong>Sleep-EDF</strong></td>
<td>R&amp;K hypnogram を AASM 相当として無言で混ぜません。label mapping を書かずに cross-dataset 比較しません。</td>
</tr>
<tr>
<td><strong>TUH EEG / TUSZ</strong></td>
<td>report text、report keyword 由来の triage、session metadata を、signal-only benchmark の入力へ混ぜません。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="what-to-report">
<h2 class="section-title">最低限これだけは報告したい</h2>
<div class="key-points">
<h4>Report Items</h4>
<ul>
<li><strong>分割単位：</strong>被験者、セッション、時間のどれで分けたか。</li>
<li><strong>分割規則：</strong>何件を train/validation/test に置いたか。</li>
<li><strong>独立 ID：</strong>subject / case / night / session のどれを独立単位とみなしたか。</li>
<li><strong>report 使用：</strong>signal-only か、report / metadata を併用した multimodal 評価か。</li>
<li><strong>label manual：</strong>manual scoring や mapping rule がある場合は、その基準。</li>
<li><strong>前処理の境界：</strong>正規化や特徴選択を、train のみで fit したか。</li>
<li><strong>ベースライン：</strong>単純な手法と比べてどこが改善したか。</li>
<li><strong>失敗例：</strong>どの条件で崩れたか、除外理由は何か。</li>
</ul>
</div>
</section>

<section class="section" id="references">
<h2 class="section-title">参考文献</h2>
<ul>
<li><a href="https://physionet.org/content/eegmmidb/1.0.0/" target="_blank">PhysioNet: EEG Motor Movement/Imagery Dataset</a></li>
<li><a href="https://physionet.org/content/chbmit/1.0.0/" target="_blank">PhysioNet: CHB-MIT Scalp EEG Database</a></li>
<li><a href="https://physionet.org/content/sleep-edfx/1.0.0/" target="_blank">PhysioNet: Sleep-EDF Database Expanded</a></li>
<li><a href="https://doi.org/10.3389/fnins.2016.00196" target="_blank">Obeid &amp; Picone (2016), The Temple University Hospital EEG Data Corpus</a></li>
<li><a href="https://doi.org/10.3389/fninf.2018.00083" target="_blank">Shah et al. (2018), The Temple University Hospital Seizure Detection Corpus</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/19238800/" target="_blank">Moser et al. (2009), Sleep classification according to AASM and Rechtschaffen &amp; Kales</a></li>
</ul>
</section>

<section class="section" id="beginner-rule">
<h2 class="section-title">最初の 1 本で迷ったときの安全策</h2>
<p>
迷ったら、<strong>被験者単位で train/test を分ける</strong>、<strong>test は最後まで触らない</strong>、<strong>正規化や特徴選択は train だけで fit する</strong>、この 3 点を守るのが安全です。厳しすぎるように見えても、信用できる精度の方が、派手な数字より価値があります。
</p>
</section>

<section class="section" id="return">
<h2 class="section-title">次にどこへ戻るか</h2>
<p>
実際のスターターデータを見直したい場合は <a href="../datasets.html">データ&ベンチ</a>、最小ループを作る作業へ戻りたい場合は <a href="../datasets.html#l0-practice">ハンズオン</a>、なぜこれが検証基盤の一部なのかを確認したい場合は <a href="../verification.html">検証基盤</a> へ戻ってください。
</p>
</section>

</article>

<aside class="sidebar-column">
<div class="sidebar-box">
<h4>Related Wiki</h4>
<ul>
<li><a href="eeg-preprocessing-and-qc.html">EEG前処理とQC →</a></li>
<li><a href="verification-basics.html">検証基盤の基本 →</a></li>
<li><a href="claims-and-evidence.html">主張と証拠の読み方 →</a></li>
</ul>
</div>
<div class="sidebar-box">
<h4>公開ページ</h4>
<ul>
<li><a href="../datasets.html">データ&ベンチ →</a></li>
<li><a href="../datasets.html#l0-practice">ハンズオン →</a></li>
<li><a href="../verification.html">検証基盤 →</a></li>
</ul>
</div>
</aside>
</main>
