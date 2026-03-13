---
layout: default
title: "検証基盤：Mind Uploading Verification Commons"
description: "マインドアップロード/WBEを「進歩を測れる科学」に寄せるための、標準・ベンチマーク・登録・監査の設計図。"
article_type: Platform
subtitle: "PDB×BIDS×PhysioNet×OSFの発想で、WBEの“勝利条件”と“再現可能な前進”を作る"
author: Mind Uploading Research Project
last_updated: "2026-03-14"
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
  - label: "Wiki: 公開ページ冒頭ブロックの読み方"
    url: "/wiki/page-header-reading-guide.html"
    description: "このページ上部の案内、既知/未知、wiki導線をどう使うかを整理します。"
  - label: "Wiki: L0〜L5ごとの読み進め方"
    url: "/wiki/claim-level-reading-routes.html"
    description: "L0〜L5 のどの主張を追うかで、次にどのページへ行くかを整理します。"
  - label: "Wiki: L0で最低限そろえる成果物パック"
    url: "/wiki/l0-minimum-artifact-pack.html"
    description: "BIDS、QC、分割、ベースライン、実行手順、失敗例の最小セットを整理します。"
  - label: "Wiki: 部分解決・探索段階・未整備の読み方"
    url: "/wiki/progress-labels-and-open-problem-status.html"
    description: "設計済み、未実装、不足、未整備の違いを整理します。"
  - label: "Wiki: 主張と証拠の読み方"
    url: "/wiki/claims-and-evidence.html"
    description: "L0〜L5 を証拠の強さで読み分ける練習用ページです。"
  - label: "Wiki: データ分割とリーク"
    url: "/wiki/dataset-splits-and-leakage.html"
    description: "精度を見る前に確認すべき、分割単位とリーク事故を整理します。"
  - label: "Wiki: 観測から推定へ"
    url: "/wiki/observation-to-estimation.html"
    description: "ESI、DCM、SCM、因果同値類を、観測と推定の違いから整理します。"
  - label: "Wiki: 配線図だけでは足りない理由"
    url: "/wiki/connectome-is-not-enough.html"
    description: "connectome だけで落ちる状態変数を、シナプス・遅延・神経修飾・グリアから整理します。"
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
  - label: "Wiki: 規格・置き場・Validator・ベンチマーク"
    url: "/wiki/standards-repositories-validators-and-benchmarks.html"
    description: "標準、共有基盤、形式点検、比較ルールの役割差を整理します。"
  - label: "Wiki: 閉ループ・遅延・ジッタ・安全停止"
    url: "/wiki/closed-loop-latency-jitter-and-safety-stops.html"
    description: "L3 で必要な遅延、ジッタ、安全停止、棄権の違いを整理します。"
  - label: "Wiki: 熱力学的接地の基本"
    url: "/wiki/thermodynamic-grounding-basics.html"
    description: "Landauer、散逸、NESS、EPR の入口を初歩から整理します。"
recommended_pages:
  - label: "技術ロードマップ"
    url: "/tech_roadmap.html"
  - label: "データ&ベンチ"
    url: "/datasets.html"
  - label: "貢献ガイド"
    url: "/issue.html"
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

<div class="note-box">
<strong>『不足』『未実装』『未完成』の違いで止まったとき</strong>
<p>
このページでは、設計済みのもの、公開運用が未整備のもの、ベンチや監査が不足しているものを分けて書いています。進み具合の言葉を 1 枚で確認したい場合は <a href="wiki/progress-labels-and-open-problem-status.html">Wiki: 部分解決・探索段階・未整備の読み方</a> を先に見ると誤読しにくくなります。
</p>
</div>
<div class="note-box">
<strong>『分かっていること / 分かっていないこと』の意味で止まったとき</strong>
<p>
このページの冒頭にある既知/未知や正確さの前提は、断言の境界を示しています。その意味を公開ページ全体に共通する読み方として整理したい場合は <a href="wiki/known-unknown-and-status-reading.html">Wiki: 『分かっていること / 分かっていないこと』の読み方</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>このページ上部の案内をどう使うかで止まったとき</strong>
<p>
Verification は長い設計図なので、本文へ入る前に上部の「このページの読み方」「向いている人」「正確さの前提」「wiki で基礎から確認する」を使って読む範囲を決めるのが有効です。その共通ルールを見たい場合は <a href="wiki/page-header-reading-guide.html">Wiki: 公開ページ冒頭ブロックの読み方</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>いま見たい主張レベルで次ページを決めたいとき</strong>
<p>
このページは全レベルの設計図なので、L0 実務へ行くのか、L3 閉ループへ行くのか、L4 本人性へ行くのかで次ページが変わります。レベルごとの導線を 1 枚で見たい場合は <a href="wiki/claim-level-reading-routes.html">Wiki: L0〜L5ごとの読み進め方</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>実務系ページの役割差で迷ったとき</strong>
<p>
Verification は勝利条件と反証条件の設計図です。入口データと L0 の最小ループは <a href="datasets.html">データ & ハンズオン</a>、参照事例はこのページ内の <a href="#casework">ケースワーク節</a>、提案整理と外部依存の切り分けは <a href="issue.html#proposal-integration">貢献ガイド内の統合提案節</a> が担当します。実務系だけの読み分けを 1 枚で見たい場合は <a href="wiki/practical-pages-reading-guide.html">Wiki: 実務系ページの読み分けガイド</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>EEGからL0までの実務ルートを一本道で見たいとき</strong>
<p>
EEG 入門から公開データ選定、Datasets内のL0実践節での L0 作成を経て、このページで何が満たせたかを確認するまでの流れを一本道で見たい場合は <a href="wiki/eeg-to-l0-route.html">Wiki: EEGからL0までの一本道</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>このページのあとに次の1ページを決めたいとき</strong>
<p>
Verification を読んだあとに、L0 実装へ戻るのか、L2 の介入検証へ進むのか、L3 の閉ループを見るのか、L4 の本人性を見るのかを 1 枚で整理したい場合は <a href="wiki/verification-next-routes.html">Wiki: Verificationのあとに進む4つの道</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>意味は分かったが、次に行動へ進めるか迷ったとき</strong>
<p>
要約を読んだだけなのか、条件や修正位置まで確認できたのかを段階で整理したい場合は <a href="wiki/understanding-vs-action-readiness.html">Wiki: 『分かった』と『次に進める』の違い</a> をご覧ください。
</p>
</div>

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
<div class="note-box">
<strong>L3 の入口で止まったとき</strong>
<p>
閉ループでは、オフライン精度だけでなく、end-to-end 遅延、ジッタ、ドリフト、安全停止の設計が必要です。この切り分けを初歩から整理したい場合は <a href="wiki/closed-loop-latency-jitter-and-safety-stops.html">Wiki: 閉ループ・遅延・ジッタ・安全停止</a> を先にご覧ください。
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
<div class="note-box">
<strong>規格と置き場と Validator の違いで止まったとき</strong>
<p>
BIDS、OpenNeuro、PhysioNet、BIDS Validator、benchmark は全部「研究基盤」ですが、やっている仕事は別です。この役割差を初歩から整理したい場合は <a href="wiki/standards-repositories-validators-and-benchmarks.html">Wiki: 規格・置き場・Validator・ベンチマーク</a> を先にご覧ください。
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
<strong>L0 の最低提出物だけ先に見たいとき</strong>
<p>
このページは公共財全体の設計図です。BIDS、Validator、QC、分割、ベースライン、実行手順、失敗例を 1 パックとして見たい場合は <a href="wiki/l0-minimum-artifact-pack.html">Wiki: L0で最低限そろえる成果物パック</a> が近道です。
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
Mind-Uploadの設計は“新規発明”ではなく、他分野が既に解いてきた「検証の型」の移植です。旧 <code>casework.md</code> の要点は本節へ統合し、ここでそのまま比較できるようにしました。
</p>
<div class="note-box">
<strong>移植のコツ</strong>
<p>
PDB（単一アーカイブ）やBIDS+OpenNeuro（規格＋置き場）、PhysioNet（データ＋評価）、OSF/PROSPERO（事前登録）などの型は、分野が違っても「前進を測れる」構造を作ります。WBEは特に、<strong>達成条件</strong>と<strong>反証条件</strong>を先に固定する必要があります。
</p>
</div>

<table class="data-table">
<thead>
<tr>
<th>先例</th>
<th>その分野で解いた問題</th>
<th>Mind-Upload が借りる設計</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>PDB / INSDC</strong></td>
<td>参照先が分散し、同じデータを見ているつもりでも比較が崩れる問題を抑えました。</td>
<td>単一参照先、安定ID、版管理、提出時の最低バリデーションを先に置きます。</td>
</tr>
<tr>
<td><strong>BIDS + OpenNeuro</strong></td>
<td>脳計測データの形式差とメタデータ欠落で、追試が難しかった問題を抑えました。</td>
<td>「どう置くか」と「どこへ置くか」を分けず、BIDS と共有基盤をセットで設計します。</td>
</tr>
<tr>
<td><strong>PhysioNet / ImageNet / MLPerf</strong></td>
<td>タスクや指標がばらばらで、前進を年単位で比較できない問題を抑えました。</td>
<td>ベースライン、提出形式、比較指標、リーク監査を固定し、改善を測れるようにします。</td>
</tr>
<tr>
<td><strong>OSF / PROSPERO</strong></td>
<td>探索と検証が混ざり、都合のよい報告だけが残る問題を抑えました。</td>
<td>事前登録、停止条件、失敗例、保留理由を成果物の一部として残します。</td>
</tr>
<tr>
<td><strong>W3C / IETF / Unicode</strong></td>
<td>別システム同士がつながらず、意味の取り違えで壊れる問題を抑えました。</td>
<td>用語、メタデータ語彙、同期ログ、監査語彙の相互運用を先に揃えます。</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>歴史事例をそのまま真似しない理由</strong>
<p>
WBE は本人性や因果同値のような強い論点を含むため、データ共有だけで完了にはなりません。ただし、標準、置き場、ベンチマーク、登録、監査を先に揃えるという順番自体は、他分野の成功例からかなり強く借りられます。
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

<section class="section" id="state-completeness-gate">
<h2 class="section-title">状態変数の完全性ゲート</h2>
<p>
2026年3月の一次文献監査では、<strong>「配線図がある」こと</strong>と<strong>「生成的に振る舞える」こと</strong>の間に、少なくとも 5 種類の抜けやすい状態変数があることを再確認しました。Dorkenwald et al. (2024)、Holler et al. (2021)、Matsuzaki et al. (2004)、Reimer et al. (2016)、Adamsky et al. (2018)、Micheva et al. (2021)、Gamlin et al. (2025) などを踏まえ、本サイトでは <strong>edge list だけの提出物を L2 以上の合格条件に使いません</strong>。
</p>
<table class="data-table">
<thead>
<tr>
<th>状態クラス</th>
<th>なぜ配線図だけでは不足か</th>
<th>欠けている場合に言える範囲</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>細胞型ラベル</strong></td>
<td>同じ隣接関係でも、転写型ごとに結合モチーフ、シナプス特性、髄鞘化の傾向が変わります。</td>
<td>構造アトラスや候補 scaffold としては有用ですが、機能再現の十分条件とは言えません。</td>
</tr>
<tr>
<td><strong>シナプス効率・短期状態</strong></td>
<td>辺の有無だけでは重み、放出確率、可塑的変化を決められません。</td>
<td>静的配線の記述までは可能ですが、L2 の介入予測や L3 の安定制御は主張できません。</td>
</tr>
<tr>
<td><strong>遅延・髄鞘</strong></td>
<td>同じグラフでも伝導速度が違えば同期と位相が変わります。</td>
<td>閉ループや時間整合性の主張を止め、遅延不確実性を明示します。</td>
</tr>
<tr>
<td><strong>神経修飾場</strong></td>
<td>覚醒度や学習率の状態は静的配線から復元できず、瞳孔径や HRV は coarse proxy にとどまります。</td>
<td>トランスミッタ特異的な内部状態は主張せず、共変量や層別化因子として扱います。</td>
</tr>
<tr>
<td><strong>グリア・代謝結合状態</strong></td>
<td>アストロサイト等は可塑性と記憶想起に因果的に関与し、単なる支持組織ではありません。</td>
<td>可塑性や長期安定性は部分モデルとして扱い、適用範囲を限定します。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>ここでの実務ルール</strong>
<p>
connectome-complete は <strong>emulation-complete を意味しません</strong>。詳細な一次文献と、どの状態変数を最低提出物に入れるべきかの技術的根拠は <a href="wiki/connectome-is-not-enough.html">Wiki: 配線図だけでは足りない理由</a> に集約します。
</p>
</div>
</section>

<section class="section" id="verification-rigor">
<h2 class="section-title">検証の厳密性要件（2026-03 科学監査で再整理）</h2>
<p>
2026年3月の一次文献監査に基づき、この節は「現時点で標準に近い要件」と「有望だが探索段階の要件」を分けて書き直しました。主な修正点は、<strong>特定ツール名を一律に義務化しない</strong>、<strong>source imaging の主張には外部妥当化を必須にする</strong>、<strong>TMS-EEG と熱力学指標は適用条件つきに下げる</strong>、の3点です。
</p>
<div class="note-box">
<strong>監査で見えた弱点</strong>
<p>
従来の本文では、ASR、ZapLine-plus、PCI-ST、Effective Information、EPR など、性質の違う手法が同じ「必須要件」として並んでいました。しかし、COBIDAS-MEEG や EEG-BIDS が強調するのは、まず<strong>透明な報告</strong>、<strong>共有可能なメタデータ</strong>、<strong>比較可能なベースライン</strong>です。したがって本ページでは、<strong>再現性の土台</strong>を必須、<strong>方法論の選択</strong>を推奨、<strong>理論駆動の追加指標</strong>を探索へ再配置します。
</p>
</div>
<div class="key-points">
<h4>必須要件（現時点で標準に近いもの）</h4>
<ul>
<li><strong>共有可能な入力：</strong>BIDS / EEG-BIDS に準拠し、<code>events.tsv</code> と JSON sidecar、電極座標、座標系、課題説明、指示文、主要アーティファクト要因を残します。イベント意味づけは HED や CogAtlasID など機械可読な語彙で補うことを強く推奨します。</li>
<li><strong>透明な報告：</strong>COBIDAS-MEEG に沿って、取得条件、参照法、フィルタ、bad channel 処理、除外試行、ICA/回帰/補間の順序とパラメータを公開します。再現できない「自動前処理」は採用しません。</li>
<li><strong>ESI主張の外部妥当化：</strong>EEG source imaging の改善を主張する場合は、個体別 MRI・座標・forward model を可能な限り明示し、さらにシミュレーション、ファントム、同時侵襲記録、頭蓋内刺激のいずれかで誤差を検証します。高密度 EEG や MRI の導入だけで深部精度を主張してはなりません。</li>
<li><strong>比較の設計：</strong>評価は単一データセットの精度で完結させず、被験者単位またはセッション単位で分割し、既存ベースラインと比較し、失敗例・棄権条件・不確実性を公開します。単独データセットでの改善は外部一般化を保証しません。</li>
</ul>
</div>
<div class="key-points">
<h4>推奨要件（課題依存だが再現性を上げるもの）</h4>
<ul>
<li><strong>前処理の感度分析：</strong>ASR、Autoreject、ICA、ZapLine-plus、リーマン幾何系などは候補であり、万能な正解ではありません。少なくとも 1 つの代替設定または感度分析を残し、どの処理が結果を動かしたかを確認します。</li>
<li><strong>信号保存の監査：</strong>前後スペクトル、除外率、補間率、主要指標の変化量を記録し、「ノイズが減った」だけでなく「目的信号を壊していないか」を確認します。</li>
<li><strong>TMS-EEG/PCI の条件明示：</strong>摂動複雑性を使う場合は、刺激部位、強度、コイル角度、聴覚マスキング、筋電・刺激アーチファクト窓、再現性評価を報告し、TMS-EEG の推奨事項に従います。</li>
</ul>
</div>
<div class="key-points">
<h4>探索要件（有望だが現時点ではゲート条件にしないもの）</h4>
<ul>
<li><strong>PCI-ST空間分布、Effective Information、Causal Density、Transfer Entropy：</strong>これらは研究上有用であり得ますが、課題依存性と実装依存性が大きく、現時点では共通ベンチの必須コア指標には置きません。</li>
<li><strong>パーシステンス図、Bottleneck distance、Fisher情報量距離：</strong>構造比較の補助指標としては有望ですが、解釈と安定性の標準化が不足しています。補助解析として提出し、一次判定はより単純で監査しやすい指標に置きます。</li>
<li><strong>熱力学的不可逆性・EPR：</strong>脳ダイナミクスの非平衡性を捉える研究は進んでいますが、現状の主証拠は fMRI や ECoG、理論モデルに強く依存します。WBE 検証の pass/fail を決める必須KPIとしてはまだ早いです。</li>
</ul>
</div>
</section>

<section class="section" id="causal-perturbation-suite">
<h2 class="section-title">因果的摂動スイート（段階導入版）</h2>
<p>
Issues #251・#254 を踏まえ、この節では「標準的な行動テストを超える」方向性を維持しつつ、<strong>いま実行できる検証</strong>と<strong>外部依存の強い検証</strong>を分離します。単なる出力一致ではなく、条件を変えたときの応答構造まで比較する発想は重要ですが、現時点では段階導入が妥当です。
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
<h4>三段階の導入</h4>
<ul>
<li><strong>Stage A / いま実行できる検証：</strong>公開 EEG データで、被験者外一般化、未学習条件、条件シフト、棄権、キャリブレーションを事前登録して比較します。まずは再現可能な L0〜L1 ループを固めます。</li>
<li><strong>Stage B / 外部基準つき中間検証：</strong>シミュレーション、ファントム、頭蓋内刺激など ground truth のあるデータで、応答誤差と不確実性を測ります。source imaging や摂動応答の改善主張は、この段階を通さない限り強く言いません。</li>
<li><strong>Stage C / 実介入：</strong>TMS-EEG、tDCS、薬理学的介入は強い検証力を持つ一方、IRB、機材、被験者運用が前提です。本リポジトリでは要求仕様と公開ログ形式を先行整備し、実験実施自体は外部依存タスクとして分離します。</li>
</ul>
</div>
<div class="note-box">
<strong>評価指標</strong>
<p>
一次判定では、事前登録した effect size、OOD 条件での頑健性、校正誤差、棄権率、不確実性の幅を優先します。PCI-ST 空間分布、パーシステンス図の Bottleneck distance、生成モデル間距離の Fisher Information Metric (FIM) は補助解析として残し、主要な合否判定を一手法へ依存させません。
</p>
</div>
</section>

<section class="section" id="verification-rigor-2026-02">
<h2 class="section-title">追加監査ログ（適用条件つき）</h2>
<p>
2026年2月後半に提出された技術批判（Issue #257–#260）に対応し、追加ログの位置づけを整理します。目的は「全部を必須にする」ことではなく、<strong>その解析を行ったなら何を一緒に出すべきか</strong>を明確にすることです。
</p>
<div class="key-points">
<h4>適用条件つきログ</h4>
<ul>
<li><strong>ESI / HBM ログ：</strong>解剖学的な source claim を行う場合に限り、頭蓋導電率や forward model の感度分析、あるいは階層ベイズ推定による不確実性マップを添付します。</li>
<li><strong>代替モデルログ：</strong>推定モデルが唯一解であるとは主張せず、同一観測統計量を説明しうる代替モデル群や同値類の存在を報告します。</li>
<li><strong>前処理忠実度ログ：</strong>ASR の有無に限らず、前後スペクトル、除外/補間率、主要指標の変化量、少なくとも 1 つの課題整合的な信号保存指標を記録します。</li>
<li><strong>イベント意味論ログ：</strong>BIDS メタデータに HED を付与し、必要に応じて CogAtlas / CogPO / NIF / SCORE 等へ写像します。特定オントロジーへの固定を共通必須にはしません。</li>
<li><strong>摂動ログ：</strong>局所介入や刺激を使った場合は、刺激部位、強度、アーチファクト窓、マスキング、安全停止条件、再試行条件を公開します。使っていない場合は「摂動証拠なし」と明記します。</li>
<li><strong>補助的熱力学ログ：</strong>不可逆性や EPR を報告する場合は、粗視化、モダリティ、サンプリング、推定器、下界なのか本体推定なのか、ハードウェア電力と計算コストの切り分けを明記します。</li>
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
<h2 class="section-title">熱力学指標（探索トラック）</h2>
<p>
NESS（非平衡定常状態）や time irreversibility を使って脳ダイナミクスを調べる研究は重要ですが、本サイトでは 2026-03 時点で<strong>補助的な研究トラック</strong>と位置づけます。不可逆性指標の有用性は示されつつある一方、WBE 検証の共通受け入れ基準としては、まだモダリティ依存性と推定仮定の影響が大きいためです。
</p>
<div class="key-points">
<h4>現時点で言えること</h4>
<ul>
<li><strong>詳細釣り合いの破れは観測されうる：</strong>脳活動から entropy production の下界を推定する研究はあり、不可逆性が神経ダイナミクスの情報を持つこと自体は支持されています。</li>
<li><strong>ただし解釈はモダリティ依存です：</strong>意識状態と不可逆性の関連は fMRI や ECoG などでも報告されていますが、粗視化、時間分解能、前処理で見え方が変わります。</li>
<li><strong>したがってゲート条件にはしません：</strong>現段階では、熱力学指標だけで WBE 的同一性や妥当性の合否を決めません。</li>
</ul>
</div>
<div class="key-points">
<h4>採用する場合の最低条件</h4>
<ul>
<li><strong>推定条件の開示：</strong>粗視化、サンプリング周期、状態空間再構成、Markov 仮定、下界推定かどうかを必ず書きます。</li>
<li><strong>コストの切り分け：</strong>ハードウェア電力、wall-clock energy、FLOPs、通信コストを分離して報告し、生物学的脳の約20Wは比較の背景値としてのみ扱います。</li>
<li><strong>補助指標として提出：</strong>既存の再現性指標、source 妥当化、摂動応答、ベースライン比較と並べて読み、単独で結論を出しません。</li>
</ul>
</div>
<div class="note-box">
<strong>本リポジトリで今やること</strong>
<p>
本リポジトリでは、熱力学指標を「必須提出物」にするのではなく、ログ形式と文献監視を整える段階に留めます。実データでの安定運用と推定誤差の監査が固まるまでは、探索的補助解析として扱います。
</p>
</div>
</section>

<section class="section" id="references">
<h2 class="section-title">参考文献（主要）</h2>
<ol>
<li>Gorgolewski, K. J., et al. (2016). The brain imaging data structure. <a href="https://doi.org/10.1038/sdata.2016.44" target="_blank">doi:10.1038/sdata.2016.44</a></li>
<li><a href="https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html" target="_blank">BIDS EEG Specification</a>（official documentation）</li>
<li>Pernet, C. R., et al. (2019). EEG-BIDS. <a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">doi:10.1038/s41597-019-0104-8</a></li>
<li>Bigdely-Shamlo, N., et al. (2016). Hierarchical Event Descriptors (HED). <a href="https://doi.org/10.3389/fninf.2016.00042" target="_blank">doi:10.3389/fninf.2016.00042</a></li>
<li>Hermes, D., et al. (2025). HED library schema for EEG data annotation. <a href="https://doi.org/10.1038/s41597-025-05791-2" target="_blank">doi:10.1038/s41597-025-05791-2</a></li>
<li>Pernet, C., et al. (2020). COBIDAS-MEEG recommendations. <a href="https://doi.org/10.1038/s41593-020-00709-0" target="_blank">doi:10.1038/s41593-020-00709-0</a></li>
<li>Markiewicz, C. J., et al. (2021). OpenNeuro resource paper. <a href="https://doi.org/10.7554/eLife.71774" target="_blank">doi:10.7554/eLife.71774</a></li>
<li>Goldberger, A. L., et al. (2000). PhysioBank / PhysioNet. <a href="https://doi.org/10.1161/01.CIR.101.23.e215" target="_blank">doi:10.1161/01.CIR.101.23.e215</a></li>
<li>Jayaram, V., &amp; Barachant, A. (2018). MOABB: trustworthy algorithm benchmarking for BCIs. <a href="https://doi.org/10.1088/1741-2552/aadea0" target="_blank">doi:10.1088/1741-2552/aadea0</a></li>
<li>Michel, C. M., &amp; Brunet, D. (2019). EEG source imaging: a practical review. <a href="https://doi.org/10.3389/fneur.2019.00325" target="_blank">doi:10.3389/fneur.2019.00325</a></li>
<li>Unnwongse, K., et al. (2022). Validating EEG source imaging using intracranial electrical stimulation. <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">doi:10.1093/braincomms/fcad023</a></li>
<li>Delorme, A. (2023). EEG is better left alone. <a href="https://doi.org/10.1038/s41598-023-27528-0" target="_blank">doi:10.1038/s41598-023-27528-0</a></li>
<li>Klug, M., &amp; Kloosterman, N. A. (2022). Zapline-plus. <a href="https://doi.org/10.1002/hbm.25832" target="_blank">doi:10.1002/hbm.25832</a></li>
<li>Hernandez-Pavon, J. C., et al. (2023). TMS combined with EEG: recommendations and open issues. <a href="https://doi.org/10.1016/j.brs.2023.02.009" target="_blank">doi:10.1016/j.brs.2023.02.009</a></li>
<li>Casali, A. G., et al. (2013). A theoretically based index of consciousness independent of sensory processing and behavior. <a href="https://doi.org/10.1126/scitranslmed.3006294" target="_blank">doi:10.1126/scitranslmed.3006294</a></li>
<li>Comolatti, R., et al. (2019). A fast and general method to empirically estimate the complexity of brain responses to transcranial and intracranial stimulations. <a href="https://doi.org/10.1016/j.brs.2019.05.013" target="_blank">doi:10.1016/j.brs.2019.05.013</a></li>
<li>Lynn, C. W., et al. (2021). Broken detailed balance and entropy production in the human brain. <a href="https://doi.org/10.1073/pnas.2109889118" target="_blank">doi:10.1073/pnas.2109889118</a></li>
<li>de la Fuente, L. A., et al. (2022). Temporal irreversibility of neural dynamics as a signature of consciousness. <a href="https://doi.org/10.1093/cercor/bhac177" target="_blank">doi:10.1093/cercor/bhac177</a></li>
<li>Nosek, B. A., et al. (2015). Promoting an open research culture. <a href="https://doi.org/10.1126/science.aab2374" target="_blank">doi:10.1126/science.aab2374</a></li>
<li>Wilkinson, M. D., et al. (2016). The FAIR Guiding Principles. <a href="https://doi.org/10.1038/sdata.2016.18" target="_blank">doi:10.1038/sdata.2016.18</a></li>
</ol>
</section>




</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>Start Here</h4>
<ul>
<li><a href="tech_roadmap.html#definition">前進の定義（Roadmap）→</a></li>
<li><a href="verification.html#casework">ケースワーク（歴史の型）→</a></li>
<li><a href="research_harvest_50.html">50ワーカー文献地図（未解決問題分解）→</a></li>
<li><a href="issue.html#proposal-integration">技術提案の一覧（Issue連動）→</a></li>
<li><a href="glossary.html">用語集（Glossary）→</a></li>
<li><a href="datasets.html">データ&ベンチ（Datasets）→</a></li>
<li><a href="faq.html">FAQ →</a></li>
<li><a href="datasets.html#l0-practice">L0実践（Datasets内）→</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Related Pages</h4>
<ul>
<li><a href="perspective.html#design-principles">Framework（理論）→</a></li>
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
