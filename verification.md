---
layout: default
title: "検証基盤：Mind Uploading Verification Commons"
description: "マインドアップロード/WBEを「進歩を測れる科学」に寄せるための、標準・ベンチマーク・登録・監査の設計図。"
article_type: Platform
subtitle: "PDB×BIDS×PhysioNet×OSFの発想で、WBEの“勝利条件”と“再現可能な前進”を作る"
author: Mind Uploading Research Project
last_updated: "2026-03-06"
note: "Operational Specification"
audience: "このサイトの中心方針を知りたい人、何を揃えれば『前進』になるかを確認したい人"
reading_time: "15〜25分"
page_intro: "このページは、Mind-Upload の中心となる設計図です。データ、評価、失敗判定、再現手順を先にそろえることで、『何を達成したら前進か』を後付けではなく事前に決める考え方を説明します。"
accuracy_note: "このページは『WBEが可能だ』と断言するページではありません。可能かどうかを確かめられる土台を作るページです。"
page_highlights:
  - "標準、置き場、ベンチマーク、監査をセットでそろえる必要があります。"
  - "デコーディングとエミュレーションを混同しないために、主張レベルと失敗条件を先に固定します。"
  - "ここを読むと、なぜデータだけ集めても前進にならないのかが分かります。"
known_points:
  - "標準、共有基盤、評価、監査をセットでそろえないと、比較可能な前進は作れません。"
  - "L0〜L2 では、再現性と反証条件を事前に設計することができます。"
  - "decode と emulate は別の主張であり、必要な証拠も別です。"
unknown_points:
  - "どの因果構造近似で L4 の本人性に十分と言えるかは、まだ決着していません。"
  - "熱力学、閉ループ、本人性をまとめた最終勝利条件は未完成です。"
  - "L5 の制度設計は、技術要件だけでは決まりません。"
wiki_links:
  - label: "Wiki: 検証基盤の基本"
    url: "/wiki/verification-basics.html"
    description: "標準、ベンチ、登録、監査がなぜ必要かを初歩から説明します。"
  - label: "Wiki: 主張と証拠の読み方"
    url: "/wiki/claims-and-evidence.html"
    description: "L0〜L5 を証拠の強さで読み分ける練習用ページです。"
  - label: "Wiki: データ分割とリーク"
    url: "/wiki/dataset-splits-and-leakage.html"
    description: "精度を見る前に確認すべき、分割単位とリーク事故を整理します。"
  - label: "Wiki: 観測から推定へ"
    url: "/wiki/observation-to-estimation.html"
    description: "ESI、DCM、SCM、因果同値類を、観測と推定の違いから整理します。"
  - label: "Wiki: 反事実・介入・摂動"
    url: "/wiki/counterfactual-and-perturbation-verification.html"
    description: "held-out 精度と因果的摂動検証の差を、初歩から整理します。"
  - label: "Wiki: 不確実性・信頼区間・棄権"
    url: "/wiki/uncertainty-confidence-and-abstention.html"
    description: "点推定、区間、伝播、低信頼時の棄権を初歩から整理します。"
  - label: "Wiki: 本人性評価と連続性テスト"
    url: "/wiki/identity-and-continuity-tests.html"
    description: "L4 で何をどこまでテストしたいのかを、連続性の観点から整理します。"
  - label: "Wiki: ベースライン・事前登録・モデルカード"
    url: "/wiki/baselines-prereg-and-model-cards.html"
    description: "出発点、事前ルール、結果記録、失敗例の役割差を整理します。"
  - label: "Wiki: 更新・分岐・停止規則"
    url: "/wiki/update-branching-and-stop-rules.html"
    description: "更新時の差分ログ、分岐 ID、停止条件の違いを初歩から整理します。"
recommended_pages:
  - label: "技術ロードマップ"
    url: "/tech_roadmap.html"
  - label: "データ&ベンチ"
    url: "/datasets.html"
  - label: "ケースワーク"
    url: "/casework.html"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>One Problem</h2>
<p>
マインドアップロード（WBE）を「夢の話」で終わらせないために、まず必要なのは<strong>共通のルール</strong>です。Mind-Uploadでは、データの置き方、評価のしかた、失敗の判定、再現手順を先にそろえて、誰でも同じ基準で確かめられる土台を作ります。
</p>
</div>

<div class="note-box">
<strong>このページで先に押さえるべきこと</strong>
<p>
ここで揃えたいのは、<strong>標準（どう置くか）</strong>、<strong>共有基盤（どこに置くか）</strong>、<strong>評価（何で比べるか）</strong>、<strong>監査（失敗や更新をどう残すか）</strong>の4点です。どれか1つだけでは、比較可能な前進になりません。
</p>
</div>

<table class="data-table">
<thead>
<tr>
<th>いま知りたいこと</th>
<th>先に読む節</th>
<th>そこで分かること</th>
</tr>
</thead>
<tbody>
<tr>
<td>このサイトが「前進」と呼ぶ条件を知りたい</td>
<td><a href="#definition">このサイトで解く「1問」</a></td>
<td>何を満たせば前進と言えるかを、主張レベルと再現条件で確認できます。</td>
</tr>
<tr>
<td>最低限そろえる公共財を知りたい</td>
<td><a href="#deliverables">Mind-Upload Commons の成果物</a></td>
<td>Data Standard、Benchmark、Registry、Leaderboard の役割分担が分かります。</td>
</tr>
<tr>
<td>現状どこまで実装済みか知りたい</td>
<td><a href="#current-status">実装ステータス</a></td>
<td>設計済みの部分と、まだ未公開・未実装の部分を分けて読めます。</td>
</tr>
<tr>
<td>厳しめの検証条件だけ知りたい</td>
<td><a href="#verification-rigor">検証の厳密性要件</a> / <a href="#verification-rigor-2026-02">追加更新</a></td>
<td>不確実性、因果同値類、前処理忠実度など、見落としやすい必須条件を確認できます。</td>
</tr>
<tr>
<td>普通の精度評価と何が違うか知りたい</td>
<td><a href="#causal-perturbation-suite">因果的摂動スイート</a></td>
<td>出力一致ではなく、条件変更への反応まで比べる理由を追えます。</td>
</tr>
<tr>
<td>熱力学の話がなぜ必要か知りたい</td>
<td><a href="#thermodynamic-verification">熱力学的検証要件</a></td>
<td>情報処理だけでなく、散逸やエネルギー制約も検証対象に入れる理由が分かります。</td>
</tr>
</tbody>
</table>

<section class="section" id="tldr">
<h2 class="section-title">TL;DR（人間向け）</h2>
<div class="key-points">
<h4>3つだけ覚える</h4>
<ul>
<li><strong>主張より先に物差し：</strong>「何を満たせば前進か」を固定しないと、成果が比較できない</li>
<li><strong>データだけでも不足：</strong>規格（標準）＋置き場（共有）＋評価（ベンチ）がセットで必要</li>
<li><strong>WBEは特に“すり替え”が起きる：</strong>decode（相関）を emulation（生成/因果）と混同しない</li>
</ul>
</div>
</section>

<section class="section" id="definition">
<h2 class="section-title">このサイトで解く「1問」</h2>
<p>
<strong>問い：</strong>「何を満たせば“前進”と言えるか？」を事前に固定し、第三者が同じ入力（データ）で同じ結論（評価）に到達できる状態を作る。
</p>
<div class="key-points">
<h4>Outcome</h4>
<ul>
<li><strong>勝利条件の固定：</strong>クレーム階段（L0〜L5）を明示し、L1をL4のように語る“すり替え”を防ぐ</li>
<li><strong>再現可能な入力：</strong>BIDS等の標準＋メタデータで、解析対象を第三者に渡せる</li>
<li><strong>比較可能な出力：</strong>スコア・ログ・失敗例まで含む評価スイートを公開する</li>
<li><strong>継続運用：</strong>ベンチマーク更新、バージョン管理、監査ログで公共財を積み上げる</li>
</ul>
</div>
</section>

<section class="section" id="claim-level-evidence">
<h2 class="section-title">主張レベルごとに最低限ほしい証拠</h2>
<table class="data-table">
<thead>
<tr>
<th>主張レベル</th>
<th>最低限ほしいもの</th>
<th>それだけではまだ足りないもの</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>L0</strong> 再現可能な解析</td>
<td>データ、コード、環境、実行ログが揃い、第三者が同じ結果を再現できること。</td>
<td>これだけで本人性や意識について強い主張はできません。</td>
</tr>
<tr>
<td><strong>L1</strong> デコーディング</td>
<td>ベースライン比較、リーク検査、OOD でない条件下の再現精度。</td>
<td>内部の因果構造や未学習条件での生成能力はまだ示せません。</td>
</tr>
<tr>
<td><strong>L2</strong> 生成・介入予測</td>
<td>未学習条件、反事実、条件変更に対する予測一致。</td>
<td>閉ループ安定性や長期運用まで成立したとは言えません。</td>
</tr>
<tr>
<td><strong>L3</strong> 閉ループ</td>
<td>リアルタイム運用での安定性、遅延管理、安全停止条件。</td>
<td>それでも本人性や権利問題は別に検証が必要です。</td>
</tr>
<tr>
<td><strong>L4</strong> 本人性</td>
<td>事前登録した連続性テスト、記憶・価値観・学習の分岐検証。</td>
<td>社会制度や長期ガバナンスまで含めた成立は別段階です。</td>
</tr>
<tr>
<td><strong>L5</strong> 社会実装</td>
<td>権利、同意、停止基準、監査体制を含む運用設計。</td>
<td>技術デモだけではこの段階には達しません。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>L4 はテスト設計そのものが難所です</strong>
<p>
本人性では、単に高スコアを出すより、何を連続していると見なすかを事前登録する方が重要です。記憶、価値観、学習、分岐、縦断の入口を初歩から整理したい場合は <a href="wiki/identity-and-continuity-tests.html">Wiki: 本人性評価と連続性テスト</a> が補講になります。
</p>
</div>
</section>

<div class="note-box">
<strong>スコアを見る前に 3 点だけ確認する</strong>
<p>
L1 の精度や L2 の予測一致を見る前に、<strong>何単位で train/test を分けたか</strong>、<strong>前処理や正規化が test を見ていないか</strong>、<strong>test をモデル選択に使っていないか</strong>を確認してください。ここが曖昧だと、主張レベル以前に評価の土台が崩れます。初歩から確認したい場合は <a href="wiki/dataset-splits-and-leakage.html">Wiki: データ分割とデータリーク</a> が最短です。
</p>
</div>

<section class="section" id="non-goals">
<h2 class="section-title">これは何ではないか（誤解防止）</h2>
<div class="note-box">
<strong>Non-goals</strong>
<p>
このページは「マインドアップロードが可能/不可能」を断言する場所ではありません。Mind-Uploadが作るのは、<strong>断言が可能になるための検証基盤</strong>です（測定・評価・反証のルール）。
</p>
</div>
</section>

<section class="section" id="deliverables">
<h2 class="section-title">Mind-Upload Commons の成果物（公共財）</h2>
<div class="note-box">
<strong>学校のテストでたとえると</strong>
<p>
この4要素は、学校のテストにたとえると役割が見えやすくなります。<strong>Data Standard</strong> は「同じ答案用紙」、<strong>Benchmark Suite</strong> は「同じ採点基準」、<strong>Registry &amp; Prereg</strong> は「試験前に配られる実施ルール」、<strong>Leaderboard &amp; Model Cards</strong> は「点数だけでなく、どう解いたかやミスも含めた成績表」に当たります。
</p>
</div>
<div class="stage-list">
<div class="stage-item">
<div class="stage-number">01</div>
<div class="stage-body">
<h4>Data Standard（入力の固定）</h4>
<p>BIDS/EEG-BIDSをベースに、課題・刺激・同期・QC・匿名化のメタデータを拡張し、「解析可能な形」で共有できる規格を整備する。</p>
<div class="tag-list">
<span class="tag">BIDS</span><span class="tag">EEG</span><span class="tag">Metadata</span><span class="tag">QC</span>
</div>
</div>
</div>
<div class="stage-item">
<div class="stage-number">02</div>
<div class="stage-body">
<h4>Benchmark Suite（出力の固定）</h4>
<p>デコーディング（相関）だけでなく、<strong>反事実・介入予測</strong>や<strong>閉ループ安定性</strong>まで含めたタスク群を定義し、同じ物差しで比較できる状態にする。</p>
<div class="tag-list">
<span class="tag">Counterfactual</span><span class="tag">Intervention</span><span class="tag">Closed-loop</span>
</div>
</div>
</div>
<div class="stage-item">
<div class="stage-number">03</div>
<div class="stage-body">
<h4>Registry & Prereg（“やる前”の固定）</h4>
<p>実験・解析計画を事前登録し、探索と検証を分離する。最初にテンプレート化した前提・評価指標・停止条件を提出し、更新時は差分付きで審査ログに追記して報告バイアスを下げる。</p>
<div class="tag-list">
<span class="tag">Preregistration</span><span class="tag">Protocol</span><span class="tag">Audit</span>
</div>
</div>
</div>
<div class="stage-item">
<div class="stage-number">04</div>
<div class="stage-body">
<h4>Leaderboard & Model Cards（比較の運用）</h4>
<p>スコアだけでなく、データリーク対策、失敗例、計算資源、既知の弱点を“カード”として公開し、再現性と安全性を担保する。</p>
<div class="tag-list">
<span class="tag">Leaderboard</span><span class="tag">Reproducibility</span><span class="tag">Safety</span>
</div>
</div>
</div>
</div>
<div class="note-box">
<strong>更新・分岐・停止で止まったとき</strong>
<p>
Registry を作っても、更新をどこまで許すか、branch をどう記録するか、停止規則とキルスイッチをどう分けるかで迷いやすいです。ここを初歩から整理したい場合は <a href="wiki/update-branching-and-stop-rules.html">Wiki: 更新・分岐・停止規則</a> を先にご覧ください。
</p>
</div>
<table class="data-table">
<thead>
<tr>
<th>欠ける要素</th>
<th>何が困るか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Data Standard がない</strong></td>
<td>入力の形式や条件がばらばらになり、同じ課題を解いているのかさえ比べにくくなります。</td>
</tr>
<tr>
<td><strong>Benchmark Suite がない</strong></td>
<td>評価の物差しが人ごとに変わり、「勝った」と言っても本当に前進したか判断できません。</td>
</tr>
<tr>
<td><strong>Registry &amp; Prereg がない</strong></td>
<td>あとから都合のよい指標や条件だけを選べてしまい、失敗と成功の区別が曖昧になります。</td>
</tr>
<tr>
<td><strong>Leaderboard &amp; Model Cards がない</strong></td>
<td>点数だけが独り歩きし、データリーク、弱点、再現手順の不足を見落としやすくなります。</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>raw EEG を置くだけでは Data Standard になりません</strong>
<p>
比較可能な入力にするには、波形ファイルだけでなく、<strong>イベントマーカー</strong>、<strong>刺激ログ</strong>、<strong>時刻同期</strong>、<strong>bad channel / bad segment の記録</strong>まで必要です。ここが曖昧だと、後から同じ課題として追試できません。初歩から整理したい場合は <a href="wiki/event-sync-and-measurement-logs.html">Wiki: イベント同期と観測ログの基本</a> をご利用ください。
</p>
</div>
</section>

<section class="section" id="example">
<h2 class="section-title">具体例：1つの「比較可能な前進」はこう見える</h2>
<p>たとえば「EEGから状態を推定するモデル」を例にすると、Commonsとして必要なのは次の4点です。</p>
<table class="data-table">
<thead>
<tr>
<th>要素</th>
<th>最低限の中身（例）</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>入力（Data）</strong></td>
<td>BIDS準拠のデータ一式、計測条件、同期ログ、QCログ、匿名化/同意の範囲</td>
</tr>
<tr>
<td><strong>手順（Code/Protocol）</strong></td>
<td>前処理→特徴→学習→評価の固定レシピ、環境情報、乱数シード</td>
</tr>
<tr>
<td><strong>出力（Metrics）</strong></td>
<td>スコア（精度/不確実性/頑健性）、失敗例、ベースラインとの差分</td>
</tr>
<tr>
<td><strong>反証（Falsification）</strong></td>
<td>データリーク検査、反事実テスト、刺激条件の変更に対する予測外れの記録</td>
</tr>
</tbody>
</table>
<p>これが揃うと「誰がやっても同じ条件で比較できる」ようになり、はじめて進捗が積み上がります。</p>

<div class="note-box">
<strong>抽象的に見えたら補講へ</strong>
<p>
この 4 要素が実際にどう噛み合うかを、EEG の小さな例で順番に見たい場合は <a href="wiki/verification-example-walkthrough.html">Wiki: Verification の具体例ウォークスルー</a> を参照してください。公開ページでは設計図を保ち、補講は wiki 側へ逃がしています。
</p>
</div>
<div class="note-box">
<strong>運用語の違いで止まったとき</strong>
<p>
ベースライン、ベンチマーク、事前登録、モデルカード、失敗例は全部重要ですが、役割は同じではありません。この差を初歩から整理したい場合は <a href="wiki/baselines-prereg-and-model-cards.html">Wiki: ベースライン・事前登録・モデルカード</a> を先にご覧ください。
</p>
</div>
</section>

<div class="note-box">
<strong>不確実性や因果同値類で止まったとき</strong>
<p>
Verification では、観測信号からの推定結果をそのまま唯一の真実として扱いません。逆問題、ESI、DCM、SCM、因果同値類の関係を先に整理したい場合は <a href="wiki/observation-to-estimation.html">Wiki: 観測から推定へ</a>、点推定と区間、低信頼時の棄権まで含めて読みたい場合は <a href="wiki/uncertainty-confidence-and-abstention.html">Wiki: 不確実性・信頼区間・棄権</a> が補講になります。
</p>
</div>

<section class="section" id="casework">
<h2 class="section-title">歴史のケースワークから借りる設計</h2>
<p>
Mind-Uploadの設計は“新規発明”ではなく、他分野が既に解いてきた「検証の型」の移植です。代表例は <a href="casework.html">ケースワーク集</a> に整理しています。
</p>
<div class="note-box">
<strong>移植のコツ</strong>
<p>
PDB（単一アーカイブ）やBIDS+OpenNeuro（規格＋置き場）、PhysioNet（データ＋評価）、OSF/PROSPERO（事前登録）などの型は、分野が違っても「前進を測れる」構造を作ります。WBEは特に、<strong>達成条件</strong>と<strong>反証条件</strong>を先に固定する必要があります。
</p>
</div>
</section>

<section class="section" id="current-status">
<h2 class="section-title">実装ステータス（透明性報告）</h2>
<div class="note-box">
<strong>率直な現状</strong>
<p>
科学的誠実さのため、各成果物の現在の実装状況を明記します。「設計文書の完成」と「実装の完了」を混同しないよう注意してください。
</p>
</div>

<table class="data-table">
<thead>
<tr>
<th>成果物</th>
<th>設計状態</th>
<th>実装状態</th>
<th>次のステップ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Data Standard</strong></td>
<td>BIDS/EEG-BIDS準拠の拡張仕様を文書化済み</td>
<td>サンプルデータセットは未公開。バリデータ未実装。</td>
<td>1データセット分のBIDS変換パイプラインと検証スクリプトの公開</td>
</tr>
<tr>
<td><strong>Benchmark Suite</strong></td>
<td>タスク定義・指標定義を文書化済み</td>
<td>ベンチマークコード・ベースライン結果は未公開。</td>
<td>L0/L1レベルの最小ベンチマーク1セットの実装と公開</td>
</tr>
<tr>
<td><strong>Registry & Prereg</strong></td>
<td>テンプレート設計済み</td>
<td>登録システム未構築。テンプレートのみ文書内に記載。</td>
<td>OSF連携またはGitHub Issueベースの簡易登録フローの構築</td>
</tr>
<tr>
<td><strong>Leaderboard</strong></td>
<td>Model Card形式を定義済み</td>
<td>実データによるエントリーなし。</td>
<td>ベンチマークの実装後に最初のエントリーを登録</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="gap-analysis">
<h2 class="section-title">科学的ギャップ分析</h2>
<p>
Verification Commonsが「科学に貢献する」ために、以下のギャップを認識し、優先的に対処します。
</p>
<div class="key-points">
<h4>優先対処事項</h4>
<ul>
<li><strong>L0の実現：</strong>第三者がコード・データ・環境を揃えて同じ結果を再現できる状態を最優先とする。現状、再現に必要な全構成要素を含むリポジトリは存在しない。</li>
<li><strong>反事実テストの操作化：</strong>「反事実」「介入予測」は概念として定義されているが、具体的な実験プロトコルとしてのテスト手順は未確定。</li>
<li><strong>既存ベンチマークとの接続：</strong>BCI Competition、MOABB等の既存ベンチマークとの互換性・差分を明確にし、車輪の再発明を避ける。</li>
<li><strong>失敗事例の体系化：</strong>Commonsの設計にはネガティブリザルトの収集と公開が含まれるが、収集のインセンティブ設計が未着手。</li>
</ul>
</div>
</section>

<section class="section" id="verification-rigor">
<h2 class="section-title">検証の厳密性要件（Technical Critique対応）</h2>
<p>
Issues #64–#70 で指摘された技術的批判を受け、Verification Commonsの検証基準を以下のとおり強化します。
</p>
<div class="key-points">
<h4>強化要件</h4>
<ul>
<li><strong>不確実性定量化の義務化：</strong>Benchmark Suiteに提出されるすべてのESI（EEG Source Imaging）結果には、信用区間（credible intervals）または事後分布の集中度指標を必ず含めること。点推定のみではWBEグレードの検証として不十分である。</li>
<li><strong>摂動ベース検証の標準化：</strong>同一性検証には、学習済みタスクを超えた摂動ベーステストを必須とする。
<ul>
<li>シミュレーションTMS応答が生体脳とエミュレーション間で一致すること</li>
<li>PCI-STの空間分布比較を複数の摂動部位で実施すること</li>
<li>未学習（新規）刺激に対する応答が統計的に区別不能であること</li>
</ul>
</li>
<li><strong>適応的前処理の要件：</strong>
<ul>
<li>ASRカットオフ閾値は静的ではなく適応的とし、リーマン幾何ベースの外れ値検出を用いること</li>
<li>周波数追従型ノイズ除去にはZapLine-plusを使用すること</li>
<li>除去されたコンポーネントの空間トポグラフィをBIDS監査証跡としてログに記録すること</li>
</ul>
</li>
<li><strong>因果指標の検証スイートへの統合：</strong>
<ul>
<li>Effective Information（EI）およびCausal Densityをコア検証指標とすること</li>
<li>有向非線形情報フローにはSymbolic Transfer Entropy（STE）を用いること</li>
<li>Pearlの因果階梯（観察→介入→反事実）を評価フレームワークとすること</li>
</ul>
</li>
  </ul>
  </div>
</section>

<section class="section" id="causal-perturbation-suite">
<h2 class="section-title">因果的摂動スイート（Causal Perturbation Suite）</h2>
<p>
Issues #251・#254 を踏まえ、標準的な行動テストを超えてWBE同一性を検証するベンチマークとして「因果的摂動スイート（Causal Perturbation Suite）」を定義します。単なる出力の一致ではなく、<strong>摂動に対する応答構造の等価性</strong>を検証するテスト群です。
</p>
<div class="note-box">
<strong>普通の精度評価と何が違うのか</strong>
<p>
普通の精度評価は、「同じ問題に同じ答えを返せたか」を見るテストです。因果的摂動スイートは、その一歩先で<strong>条件をわざと変えたときに、どう崩れ、どう持ち直すか</strong>まで比べます。つまり「答えが合うか」ではなく、「中の仕組みが同じように反応しているか」を見るテストです。
</p>
</div>
<div class="note-box">
<strong>入り口だけ先に整理したいとき</strong>
<p>
held-out 精度、介入、反事実、摂動ベース検証の違いを日常語で先に整理したい場合は <a href="wiki/counterfactual-and-perturbation-verification.html">Wiki: 反事実・介入・摂動の検証</a> を先に読むと、この節へ戻りやすくなります。
</p>
</div>
<div class="key-points">
<h4>三つのテストカテゴリ</h4>
<ul>
<li><strong>1. シミュレーションTMS応答の一致：</strong>仮想摂動（virtual perturbation）を印加し、生物学的脳とエミュレーション間のEEG応答パターンを比較する。複数摂動部位での応答伝播の統計的一致を検証する。</li>
<li><strong>2. 薬理学的介入シミュレーション：</strong>麻酔・薬物効果の伝播をモデル化し、生体脳における実測データと比較する。状態遷移（覚醒↔鎮静など）のパターン再現性を検証する。</li>
<li><strong>3. 新規・極端刺激応答：</strong>学習中に一度も見せていない新規・極端刺激に対する応答を比較し、KLダイバージェンスを用いた分岐パターンの違いを評価する。</li>
</ul>
</div>
<div class="note-box">
<strong>評価指標</strong>
<p>
PCI-ST空間分布比較、パーシステンス図のBottleneck distance、生成モデル間距離のFisher Information Metric (FIM) を採用する。反事実等価性については Laukkonen et al. (2025) を参照する。
</p>
</div>
</section>

<section class="section" id="verification-rigor-2026-02">
<h2 class="section-title">検証要件の追加更新（Issue #257–#260）</h2>
<p>
2026年2月後半に提出された技術批判（Issue #257–#260）に対応し、既存要件に不足していた判定ログを追加します。目的は「主張の強化」ではなく、第三者が反証可能な形で再現監査できることです。
</p>
<div class="key-points">
<h4>追加必須ログ</h4>
<ul>
<li><strong>HBM不確実性マップ：</strong>EEG逆問題では、頭蓋導電率を含む順問題パラメータとソース活動を同時推定し、モンテカルロ感度分析の空間マップを提出すること。</li>
<li><strong>因果同値類の明示：</strong>推定モデルが唯一解であるとは主張せず、同一観測統計量を説明しうる代替モデル群（causal equivalence class）の存在を報告すること。</li>
<li><strong>摂動一致の追加判定：</strong>PCI-STの値比較だけでなく、局所介入（TMS/tDCS相当）での応答分岐一致を必須とすること。</li>
<li><strong>前処理忠実度監査：</strong>ASR適用前後の相互情報量（MI）および位相同期（PLV/wPLI）の保存率を記録し、高周波成分の過抑制を検査すること。</li>
<li><strong>セマンティックメタデータ：</strong>BIDSメタデータにCogPO/NIF準拠タグと主観報告（ESM等）を追加し、認知文脈の欠落を防ぐこと。</li>
<li><strong>熱力学KPI：</strong>FLOPs系の論理コストとEPR系の散逸コストを分離し、通信対計算エネルギー比を併記すること。</li>
</ul>
</div>
<div class="note-box">
<strong>外部依存タスクの扱い</strong>
<p>
実被験者介入（TMS/tDCS）、IRB審査、機材調達を要する検証は外部依存タスクとして管理します。本リポジトリでは「要求仕様・判定条件・公開ログ形式」までを先行実装し、実験実施自体は別トラックで進めます。
</p>
</div>
</section>

<section class="section" id="thermodynamic-verification">
<h2 class="section-title">熱力学的検証要件（Thermodynamic Verification Requirements）</h2>
<p>
Issues #251・#254 に基づき、NESS（非平衡定常状態）およびEPR（エントロピー生成速度）の観点から熱力学指標を検証スイートに組み込みます。
</p>
<div class="key-points">
<h4>必須要件</h4>
<ul>
<li><strong>熱力学指標の報告義務：</strong>ベンチマークへのエミュレーション提出物は、必ず熱力学関連指標を報告すること。既存の情報論的指標を補完する。</li>
</ul>
</div>
<div class="key-points">
<h4>実証的EPR測定</h4>
<ul>
<li><strong>下界エントロピー生成速度：</strong>EEG時系列を用い、時間反転対称性の破れ（time-reversal asymmetry）に基づいてエントロピー生成速度の下界を推定する（Lynn et al., 2021, PNAS; Ishihara &amp; Shimazaki, 2025, Nature Communications）。</li>
</ul>
</div>
<div class="key-points">
<h4>エネルギー効率の比較</h4>
<ul>
<li><strong>仮想エネルギー流の比率：</strong>エミュレーションの仮想エネルギー流と、生物学的脳の約20Wとの比を算出し、効率性を比較する。</li>
<li><strong>通信 vs 計算のエネルギー比：</strong>Niven &amp; Laughlin (2008) に従い、大脳皮質において通信コストが計算コストの約35倍となる点を考慮し、エミュレーション設計の評価に反映する。</li>
</ul>
</div>
<div class="note-box">
<strong>位置づけ</strong>
<p>
これらの熱力学指標は、既存の情報論的指標（Effective Information、Causal Density 等）を補完する。同一性検証において、非平衡熱力学の観点を欠いた主張は不十分とみなす。
</p>
</div>
</section>

<section class="section" id="references">
<h2 class="section-title">参考文献（主要）</h2>
<ol>
<li>Gorgolewski, K. J., et al. (2016). BIDS. <a href="https://doi.org/10.1038/sdata.2016.44" target="_blank">doi:10.1038/sdata.2016.44</a></li>
<li>Pernet, C. R., et al. (2019). EEG-BIDS. <a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">doi:10.1038/s41597-019-0104-8</a></li>
<li>Markiewicz, C. J., et al. (2021). OpenNeuro resource paper. <a href="https://doi.org/10.7554/eLife.71774" target="_blank">doi:10.7554/eLife.71774</a></li>
<li>Goldberger, A. L., et al. (2000). PhysioBank/PhysioNet. <a href="https://doi.org/10.1161/01.CIR.101.23.e215" target="_blank">doi:10.1161/01.CIR.101.23.e215</a></li>
<li>Nosek, B. A., et al. (2015). Promoting an open research culture. <a href="https://doi.org/10.1126/science.aab2374" target="_blank">doi:10.1126/science.aab2374</a></li>
<li>Jayaram, V., &amp; Barachant, A. (2018). MOABB: BCI benchmark framework. <a href="https://doi.org/10.1088/1741-2552/aaddc8" target="_blank">doi:10.1088/1741-2552/aaddc8</a></li>
<li>Wilkinson, M. D., et al. (2016). The FAIR Guiding Principles. <a href="https://doi.org/10.1038/sdata.2016.18" target="_blank">doi:10.1038/sdata.2016.18</a></li>
</ol>
</section>




</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>Start Here</h4>
<ul>
<li><a href="tech_roadmap.html#definition">前進の定義（Roadmap）→</a></li>
<li><a href="casework.html">ケースワーク集（歴史の型）→</a></li>
<li><a href="research_harvest_50.html">50ワーカー文献地図（未解決問題分解）→</a></li>
<li><a href="proposals.html">技術提案の一覧（Issue連動）→</a></li>
<li><a href="glossary.html">用語集（Glossary）→</a></li>
<li><a href="datasets.html">データ&ベンチ（Datasets）→</a></li>
<li><a href="faq.html">FAQ →</a></li>
<li><a href="hands_on.html">ハンズオン（L0）→</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Related Pages</h4>
<ul>
<li><a href="idea.html">Framework（理論）→</a></li>
<li><a href="mind_uploading_papers.html">Papers（文献）→</a></li>
<li><a href="issue.html">Contribute（参加）→</a></li>
</ul>
</div>

<div class="note-box">
<strong>Scope</strong>
<p>
このページは「最終結論」を主張する場所ではなく、研究が積み上がるための<strong>ルールと成果物</strong>を置く場所です。大きな主張ほど、先に“小さく反証できる形”に分解します。
</p>
</div>

</aside>
</main>
