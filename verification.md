---
layout: default
title: "検証基盤：Mind Uploading Verification Commons"
description: "マインドアップロード/WBEを「進歩を測れる科学」に寄せるための、標準・ベンチマーク・登録・監査の設計図。"
article_type: Platform
subtitle: "PDB×BIDS×PhysioNet×OSFの発想で、WBEの“勝利条件”と“再現可能な前進”を作る"
author: Mind Uploading Research Project
last_updated: "2026-03-16"
note: "Operational Specification"
audience: "このサイトの中心方針を知りたい人、何を揃えれば『前進』になるかを確認したい人"
reading_time: "15〜25分"
page_intro: "このページは、Mind-Upload の中心となる設計図です。データ、評価、失敗判定、再現手順を先にそろえることで、『何を達成したら前進か』を後付けではなく事前に決める考え方を説明します。"
accuracy_note: "このページは『WBEが可能だ』と断言するページではありません。可能かどうかを確かめられる土台を作るページです。"
page_highlights:
  - "標準、置き場、ベンチマーク、監査をセットでそろえる必要があります。"
  - "デコーディングとエミュレーションを混同しないために、主張レベルと失敗条件を先に固定します。"
  - "ここを読むと、なぜデータだけ集めても前進にならないのかが分かります。"
  - "multimodal や atlas prior を使う結果では、Observability Budget に加えて Fusion Card で取得関係・同期・融合モデル・外部妥当化を固定します。"
  - "L2 以上では、Observability Budget に加えて latent-state error budget も付け、どの未観測状態がまだ claim を止めるかまで公開します。"
  - "L2 以上の介入・閉ループ結果では、Intervention Card で trigger rule・timing audit・control/sham・安全停止・再較正負荷を固定します。"
  - "cross-day / longitudinal claim では、Temporal Validity Card で fixed decoder interval・state 注釈・recalibration burden・transfer ceiling を独立監査します。"
  - "確率・区間・予測集合・棄権を出す結果では、Calibration & Abstention Card で fit/calibration/test 分離・evaluation family・coverage-risk・fallback を固定します。"
known_points:
  - "標準、共有基盤、評価、監査をセットでそろえないと、比較可能な前進は作れません。"
  - "L0〜L2 では、再現性と反証条件を事前に設計することができます。"
  - "decode と emulate は別の主張であり、必要な証拠も別です。"
  - "multimodal result は 1 種類ではなく、同時取得、幾何統合、侵襲校正、atlas prior を分けて監査する必要があります。"
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
  - label: "Wiki: 計測スタックごとの observability と claim ceiling"
    url: "/wiki/measurement-stack-and-claim-ceiling.html"
    description: "どの measurement stack が何を直接観測し、どこで主張上限に当たるかを整理します。"
  - label: "Wiki: 反事実・介入・摂動"
    url: "/wiki/counterfactual-and-perturbation-verification.html"
    description: "held-out 精度と因果的摂動検証の差を、初歩から整理します。"
  - label: "Wiki: 不確実性・校正・棄権"
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
<td><a href="#observability-budget">Observability Budget</a> / <a href="#verification-rigor">検証の厳密性要件</a></td>
<td>どこまで直接観測していて、どこから推定か、さらに不確実性や前処理忠実度まで確認できます。</td>
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
<p>スコアだけでなく、データリーク対策、失敗例、計算資源、既知の弱点、さらに leaderboard / challenge 結果では <strong>どの split・hidden test・submission budget・checkpoint policy で score を出したか</strong> を示す <strong>Benchmark Governance Card</strong> を、L1 以上では <strong>どこまで直接観測し、どこから先が latent state か</strong> を示す <strong>Observability Budget</strong> を、確率・区間・予測集合・棄権を出す結果では <strong>fit / calibration / test の分離、evaluation family、coverage-risk、fallback policy</strong> を示す <strong>Calibration &amp; Abstention Card</strong> を、multimodal / atlas prior を使う結果では <strong>どう結び付け、どこまで較正したか</strong> を示す <strong>Fusion Card</strong> を、cross-day / longitudinal claim では <strong>same-day score をどこまで外挿してよいか</strong> を示す <strong>Temporal Validity Card</strong> を、L2 以上では <strong>どの latent state がまだ誤差を支配するか</strong> を示す <strong>latent-state error budget</strong> を、因果・閉ループ結果では <strong>trigger rule・timing audit・control/sham・安全停止・再較正負荷</strong> を示す <strong>Intervention Card</strong> を併記して公開し、再現性と安全性を担保する。</p>
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
<strong>L1 以上では『何を直接見たのか』も成果物に含めます</strong>
<p>
今回の再監査で見えた弱点は、hidden state を列挙できても、<strong>どの measurement stack がどの変数を直接観測しているか</strong>が提出物として固定されていなかった点でございます。したがって L1 以上の結果では、通常の model card に加えて <a href="#observability-budget">Observability Budget</a> を添付し、claim ceiling と abstention 条件まで残します。
</p>
</div>
<div class="note-box">
<strong>multimodal や atlas prior を使う結果では『どう結び付けたか』も成果物に含めます</strong>
<p>
今回さらに見えた弱点は、EEG 入門と multimodal wiki では止めていた論点が、<strong>検証基盤の提出物仕様</strong>にはまだ十分に落ちていなかったことです。したがって、<strong>複数モダリティを束ねた結果</strong>や<strong>atlas / transcriptomic prior を加えた結果</strong>では、通常の model card に加えて <a href="#fusion-card">Fusion Card</a> を添付し、取得関係、時計系、登録誤差、融合モデル、外部妥当化、coverage boundary まで残します。
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
Verification では、観測信号からの推定結果をそのまま唯一の真実として扱いません。逆問題、ESI、DCM、SCM、因果同値類の関係を先に整理したい場合は <a href="wiki/observation-to-estimation.html">Wiki: 観測から推定へ</a>、点推定と区間、低信頼時の棄権まで含めて読みたい場合は <a href="wiki/uncertainty-confidence-and-abstention.html">Wiki: 不確実性・校正・棄権</a> が補講になります。
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

<section class="section" id="observability-budget">
<h2 class="section-title">2026-03 追補：Observability Budget を必須提出物にする</h2>
<p>
今回もっとも深く更新すべきだった点は、<strong>「重要な hidden state が残る」</strong>という批判が、まだ<strong>提出物の形式</strong>にまで落ち切っていなかったことでございます。<a href="https://doi.org/10.1038/s41586-023-06812-z" target="_blank">Yao et al. (2023)</a> は whole-brain atlas が cell-type taxonomy と空間配置を強くする一方で current state を直接は与えず、<a href="https://doi.org/10.1038/s41586-024-07558-y" target="_blank">Dorkenwald et al. (2024)</a> は volume EM が structural scaffold を強くする一方で synaptic efficacy や neuromodulatory context を直接は与えず、<a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONS Consortium et al. (2025)</a> は same-brain structure-function link を大きく前進させつつも local conditional prediction の域に留まります。さらに、<a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">Unnwongse et al. (2023)</a> と <a href="https://doi.org/10.1111/epi.18552" target="_blank">Hao et al. (2025)</a> が示すように、HD-EEG / ESI は外部妥当化があっても source depth や頭部モデルに依存し、一般的一意復元を与えるわけではありません。したがって本サイトでは、<strong>L1 以上の提出物に Observability Budget を必須化</strong>し、何を直接見て何をまだ推定しているのかを先に固定します。
</p>
<table class="data-table">
<thead>
<tr>
<th>Observability Budget の欄</th>
<th>最低限書くこと</th>
<th>これが無いと何が起きるか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>measurement stack</strong></td>
<td>EEG / MEG / fMRI、high-density extracellular probe、whole-brain atlas、Patch-seq、volume EM、same-brain function、local transmitter / glia imaging のどれを使ったか。</td>
<td>「multimodal」「atlas」「same-brain」という言葉だけが独り歩きし、直接観測量の違いが消えます。</td>
</tr>
<tr>
<td><strong>direct observables</strong></td>
<td>その stack が直接測った変数だけを書きます。BOLD、field potential、spike waveform / threshold crossings、cell-type label、EM synapse、local ACh dynamics などです。</td>
<td>推定した latent state を、最初から観測済みだったかのように誤読しやすくなります。</td>
</tr>
<tr>
<td><strong>remaining latent state</strong></td>
<td>weights、delay / myelin、intrinsic excitability / homeostatic set point、neuromodulation、glia / metabolic support、sleep-history に加え、chronic probe 系では stable single-unit identity、sorting / matching error、tissue response も列挙します。</td>
<td>state-complete ではない結果を、emulation-complete や内部状態の唯一解へ繰り上げやすくなります。</td>
</tr>
<tr>
<td><strong>state-variable coverage と timescale class</strong></td>
<td>cell identity、synaptic efficacy / plastic history、intrinsic excitability、delay / myelin、neuromodulation、glia / slow-state、sleep / recovery、chronic unit identity の各行を、direct / proxy / inferred / absent のどれかでラベルし、dominant timescale を添えます。</td>
<td>multimodal の結果を 1 本の強さとして圧縮してしまい、same-day の fit を cross-day stability や maintenance-state claim へ不当に延長しやすくなります。</td>
</tr>
<tr>
<td><strong>external calibration route</strong></td>
<td>phantom、intracranial stimulation、同時侵襲記録、same-brain co-registration、Patch-seq bridge など、外部妥当化の経路を書きます。</td>
<td>精度や可視化の改善を、そのまま ground truth への接近と取り違えやすくなります。</td>
</tr>
<tr>
<td><strong>validity horizon</strong></td>
<td>within-session、cross-state、cross-day、perturbation、recovery のどこまで検証したかを書きます。</td>
<td>same-day の fit を長期 stability や memory claim へ不当に延長しやすくなります。</td>
</tr>
<tr>
<td><strong>unit identity audit</strong></td>
<td>chronic extracellular 記録なら、sorting version、drift correction、unit-match method / probability、dropout / new-unit rate、implant age と tissue-response proxy を書きます。</td>
<td>「same neuron across days」や single-unit level の長期安定性を、channel 番号だけで誤読しやすくなります。</td>
</tr>
<tr>
<td><strong>claim ceiling と abstention</strong></td>
<td>「macro state tracking」「structural scaffold」「local conditional prediction」など、その結果が到達してよい上限と、超えたら棄権する条件を書きます。</td>
<td>論文の前進を過大に翻訳し、L1 の結果を L2/L3/L4 へ誤昇格させやすくなります。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>最低運用ルール</strong>
<p>
このカードが無い場合、本サイトでは結果を <strong>L0/L1 の再現可能解析または限定つき decode</strong> として扱い、L2 以上へ上げません。たとえば、<strong>EEG / HD-EEG + MRI だけ</strong>なら default ceiling は macro state tracking、<strong>high-density extracellular probe だけ</strong>なら implant-region の local population window、<strong>volume EM だけ</strong>なら structural scaffold、<strong>whole-brain atlas だけ</strong>なら molecular / spatial prior、<strong>same-brain calcium + EM</strong> でも local conditional prediction までです。chronic probe 系で unit identity audit が無い場合、single-unit longitudinal claim は受理しません。詳細な stack 別 ceiling と <strong>state variable × timescale</strong> の行列は <a href="wiki/measurement-stack-and-claim-ceiling.html#state-variable-matrix">Wiki: 計測スタックごとの observability と claim ceiling</a> に集約しています。
</p>
</div>
</section>

<section class="section" id="fusion-card">
<h2 class="section-title">2026-03 追補：multimodal 結果には Fusion Card を添付する</h2>
<p>
今回もっとも深く修正すべきだった次の弱点は、<strong>multimodal の厳しさが局所ページに閉じ、Verification Commons の提出物仕様へまだ十分に入っていなかった</strong>ことです。<a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">Pernet et al. (2019)</a> と <a href="https://doi.org/10.1038/s41597-024-03559-8" target="_blank">Burns et al. (2024)</a> が与えるのは、EEG や motion metadata を共有可能にする<strong>器</strong>であり、<a href="https://doi.org/10.1162/imag.a.136" target="_blank">Kothe et al. (2025)</a> は LSL が synchronized recording を助けても device-side delay / jitter の ground truth を自動で与えないことを示しました。さらに、<a href="https://doi.org/10.1016/j.neuroimage.2019.116595" target="_blank">Wei et al. (2020)</a> は EEG-fMRI fusion が shared latent model を明示して初めて解釈可能になることを示し、<a href="https://doi.org/10.1016/j.neuroimage.2014.10.055" target="_blank">Jorge et al. (2015)</a> と <a href="https://doi.org/10.1371/journal.pone.0093154" target="_blank">Aydin et al. (2014)</a> は safety / artifact management と calibrated head model が成立条件であることを示しました。加えて、<a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">Mikulan et al. (2020)</a> と <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">Unnwongse et al. (2023)</a> は direct validation が強い一方で coverage-limited であることも示しています。今回の再監査ではさらに、fMRI / fNIRS を含む統合では <strong>shared clock や co-registration だけでは不十分で、HRF・task-related haemodynamics・venous bias を別に監査しないと BOLD を direct neural truth と誤読しやすい</strong>ことも見えました。したがって本サイトでは、<strong>multimodal / atlas prior 結果には Observability Budget だけでなく Fusion Card を必須化</strong>し、「何を直接見たか」だけでなく「どう結び付け、その結び付けがどこまで妥当化されたか」まで提出物化します。
</p>
<table class="data-table">
<thead>
<tr>
<th>Fusion Card の欄</th>
<th>最低限書くこと</th>
<th>これが無いと何が起きるか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>acquisition relation</strong></td>
<td>simultaneous、same-subject non-simultaneous、coverage-limited validation、atlas / bridge / prior のどれかを書きます。</td>
<td>「multimodal」という 1 語の下で、時計共有と prior 付与が同じ強さの証拠に見えてしまいます。</td>
</tr>
<tr>
<td><strong>clock and timing audit</strong></td>
<td>clock domain、offset / delay / jitter / drift、LSL / TTL / photodiode などの validation method、resync policy を書きます。</td>
<td>shared clock が無い統合を trial-level alignment や causal order と誤読しやすくなります。</td>
</tr>
<tr>
<td><strong>geometry and registration</strong></td>
<td>individual MRI、sensor / electrode coordinates、co-registration error、head model、conductivity assumptions を書きます。</td>
<td>幾何の改善と localizability の改善が、根拠なしに混ざります。</td>
</tr>
<tr>
<td><strong>fusion model and uncertainty</strong></td>
<td>late fusion か shared latent model か、loss、weights、priors、posterior / uncertainty representation、感度分析を書きます。</td>
<td>fused map を raw truth と読み替え、比較不能な黒箱を受理しやすくなります。</td>
</tr>
<tr>
<td><strong>hemodynamic proxy audit<br>(when fMRI / fNIRS is included)</strong></td>
<td>BOLD / CBF / fNIRS のどの proxy を使ったか、target neural claim、HRF model granularity、task / physiology nuisance、venous / depth diagnostic、mechanistic validator を書きます。</td>
<td>shared clock や geometry が揃っただけの結果を、そのまま direct neural truth や fine-grained mechanism と誤読しやすくなります。</td>
</tr>
<tr>
<td><strong>incremental evidence</strong></td>
<td>single-modality baseline、missing-modality ablation、behaviour-only / anatomy-only baseline との差分を残します。</td>
<td>本当に modality を足した価値なのか、強い prior や task shortcut なのかを切り分けられません。</td>
</tr>
<tr>
<td><strong>external validator</strong></td>
<td>phantom、intracranial stimulation、simultaneous invasive recording、same-brain co-registration、post-op outcome などの較正経路を書きます。</td>
<td>見た目の改善や相関上昇を、そのまま external validity と誤読しやすくなります。</td>
</tr>
<tr>
<td><strong>coverage boundary and raw retention</strong></td>
<td>何を still latent に残したかと、各 modality の raw / QC / BIDS metadata / artifact correction 前後の所在を書きます。</td>
<td>coverage-limited validation や atlas prior を whole-brain state coverage と誤昇格させやすくなります。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Observability Budget との役割差</strong>
<p>
Observability Budget は <strong>各 measurement stack が何を直接観測したか</strong> を固定するカードで、Fusion Card は <strong>複数モダリティや prior をどう結び付け、どこまで較正したか</strong> を固定するカードでございます。前者だけでは acquisition relation と fusion model が消え、後者だけでは direct observable と claim ceiling が消えます。したがって本サイトでは、<strong>multimodal / atlas prior 結果では両方を同時提出</strong>します。
</p>
</div>
<div class="note-box">
<strong>最低運用ルール</strong>
<p>
Fusion Card が無い場合、本サイトではその結果を原則として <strong>single-modality result に prior を足した推定</strong>、または <strong>限定つきの cross-modal concordance</strong> として扱い、L2 以上へ昇格させません。shared clock が無い場合は trial-level state alignment を書かず、coverage-limited validation しか無い場合は whole-brain ground truth を書かず、single-modality baseline が無い場合は multimodal gain を書きません。さらに <strong>fMRI / fNIRS を含む結果で hemodynamic proxy audit が無い場合</strong>、本サイトではその ceiling を <strong>macro concordance</strong> までに留め、fast causal order や fine-grained mechanism を書きません。
</p>
</div>
</section>

<section class="section" id="latent-state-error-budget">
<h2 class="section-title">2026-03 追補：latent-state error budget を加える</h2>
<p>
今回さらに深掘りして見えた弱点は、<strong>Observability Budget だけでは「何が直接見えていないか」は書けても、どの latent state がいまの claim をどれだけ止めているか</strong>までは固定しきれないことでした。<a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">Beiran &amp; Litwin-Kumar (2025)</a> は connectome 制約を入れても dynamics の縮退が残ることを示し、<a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONS Consortium et al. (2025)</a> は same-brain structure-function link が local conditional prediction を強くする一方で全脳 state-complete を与えないことを示しました。さらに、<a href="https://doi.org/10.1038/s41586-025-08805-6" target="_blank">Gamlin et al. (2025)</a>、<a href="https://doi.org/10.1038/s41592-024-02440-1" target="_blank">van Beest et al. (2024)</a>、<a href="https://doi.org/10.1016/j.celrep.2024.114808" target="_blank">Neyhart et al. (2024)</a>、<a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">Cahill et al. (2024)</a>、<a href="https://doi.org/10.1038/s41467-025-66975-3" target="_blank">Hadzibegovic et al. (2026)</a> に加え、<a href="https://doi.org/10.1016/j.cell.2016.01.046" target="_blank">Hengen et al. (2016)</a>、<a href="https://doi.org/10.1016/j.neuron.2021.04.004" target="_blank">Torrado Pacheco et al. (2021)</a>、<a href="https://doi.org/10.1038/s41593-023-01558-3" target="_blank">Looser et al. (2024)</a> は、cell-type bridge、chronic unit identity、transmitter specificity、glial slow-state、intrinsic excitability、sleep-dependent recovery、axonal support が別々の誤差源として残ることを裏づけます。今回の再監査ではさらに、<strong>各 latent-state 行に dominant timescale、evidence tier、transfer ceiling を持たせないと、same-day fit を cross-day stability へ、rodent local causal result を human whole-brain sufficient condition へ読み替えやすい</strong>ことも見えました。したがって本サイトでは、<strong>L2 以上の提出物に Observability Budget と latent-state error budget の両方</strong>を要求し、未観測状態を「列挙」ではなく「どの誤差項をまだ支配しているか」で管理します。
</p>
<table class="data-table">
<thead>
<tr>
<th>latent-state error source</th>
<th>最低限残す監査ログ</th>
<th>比較・較正</th>
<th>棄権条件</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>intrinsic excitability / homeostatic controller</strong></td>
<td>cross-day / cross-perturbation の held-out 劣化、recovery time、可能なら excitability proxy または allocation proxy。</td>
<td>fixed connectome / fixed decoder と、excitability・homeostasis 項を足した条件を同じ split で比べます。</td>
<td>within-session の gain しか無い、または recovery を記録していない場合、長期安定性・記憶配分の claim を止めます。</td>
</tr>
<tr>
<td><strong>synaptic efficacy / plastic history</strong></td>
<td>connectome-only baseline と weight / plasticity 項を足したモデルの held-out perturbation 誤差、ablation、drift 曲線。</td>
<td>edge count / EM synapse だけの条件と、現在の有効結合を持たせた条件を同一課題・同一 horizon で較正します。</td>
<td>edge list だけで gain を主張している場合、L2 の介入予測と L3 の安定制御を保留します。</td>
</tr>
<tr>
<td><strong>delay / myelin / axonal support</strong></td>
<td>phase error、latency degradation curve、timing-sensitive task での失敗率、delay を固定定数で近似した箇所。</td>
<td>timing-sensitive 条件で、delay fixed と delay-aware 条件の差を出し、cell-type / region 依存の caveat も併記します。</td>
<td>delay を定数へ押し込んだだけなら、位相同期・閉ループ時間整合性・cross-day timing claim を止めます。</td>
</tr>
<tr>
<td><strong>neuromodulatory specificity</strong></td>
<td>proxy specificity 表、compartment（pupil / axon / sensor / receptor）、spatial spread / clearance、receptor family / cell-type target、cross-state calibration、missing-modality 時の abstention。</td>
<td>mixed arousal proxy、local transmitter sensor、receptor atlas / pharmacology を同じ cohort または外部基準で分けて較正します。</td>
<td>compartment、spatial scope、receptor family のいずれかが無い場合、内部状態を neuromodulator ground truth と書きません。</td>
</tr>
<tr>
<td><strong>glial / slow-state support</strong></td>
<td>分オーダー以上の recovery、再想起後の restabilization window、slow-state covariate、neuron-only と glia-inclusive 条件の gain、適用時定数。</td>
<td>fast neural feature だけの条件と、glial / metabolic covariate または astrocyte ensemble state を足した条件を same split で比較します。</td>
<td>fast activity fit しか無い、または restabilization を見ていない場合、memory consolidation、long-term recall stabilization、slow-state、長期回復の claim を止めます。</td>
</tr>
<tr>
<td><strong>chronic unit identity / tissue response</strong></td>
<td>unit-match probability、dropout / new-unit rate、sorting version、drift correction、implant age、tissue-response proxy。</td>
<td>cross-day decoding と single-unit longitudinal claim を分け、population readout と unit identity を別監査にします。</td>
<td>matching probability と dropout が無い場合、same neuron across days や single-unit memory trace claim を止めます。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>2026-03 追補：neuromodulatory proxy も 1 本ではありません</strong>
<p>
<a href="https://doi.org/10.1038/ncomms13289" target="_blank">Reimer et al. (2016)</a> は pupil が adrenergic / cholinergic の mixed proxy であることを示し、<a href="https://doi.org/10.1038/s41593-022-01202-6" target="_blank">Lohani et al. (2022)</a> と <a href="https://doi.org/10.7554/eLife.86800.2" target="_blank">Collins et al. (2023)</a> は cortex-wide の共通信号と局所独立成分が共存することを示しました。さらに <a href="https://doi.org/10.1016/j.celrep.2024.114808" target="_blank">Neyhart et al. (2024)</a> は local ACh signal が axon distance と clearance kinetics に依存することを示し、<a href="https://doi.org/10.1038/s41593-022-01186-3" target="_blank">Hansen et al. (2022)</a> と <a href="https://doi.org/10.1038/ncomms12826" target="_blank">Verhoog et al. (2016)</a> は receptor distribution と effect が region / layer 依存であることを示しました。したがって本サイトでは、neuromodulatory proxy について <strong>compartment</strong>、<strong>spatial scope</strong>、<strong>receptor family</strong> を独立欄として残します。
</p>
</div>
<div class="note-box">
<strong>2026-03 で追加した必須列</strong>
<p>
latent-state error budget は、誤差源の名前だけでなく、<strong>どの時間スケールで止まるのか</strong>、<strong>どの証拠階層に依拠しているのか</strong>、<strong>どこまで human へ持ち込めるのか</strong>を同時に固定して初めて、過大な昇格を防げます。
</p>
</div>
<table class="data-table">
<thead>
<tr>
<th>追記列</th>
<th>最低限の書き方</th>
<th>この列が無いと起きる誤読</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>dominant timescale</strong></td>
<td>trial / within-session / within-day / cross-day / multiday のどこで誤差が支配的かを書きます。</td>
<td>same-day の gain を、そのまま overnight recovery や長期安定性へ読み替えやすくなります。</td>
</tr>
<tr>
<td><strong>evidence tier</strong></td>
<td>direct human / same-brain mammal / causal rodent / model / proxy-only のどれかでラベルします。</td>
<td>構造推定、proxy、rodent local intervention を同じ強さの ground truth と誤読しやすくなります。</td>
</tr>
<tr>
<td><strong>transfer ceiling</strong></td>
<td>local circuit、region-limited、species-limited、macro scaffold など、外挿の上限を書きます。</td>
<td>rodent 局所回路の成功を human whole-brain sufficient condition へ、macro-biochemical scaffold を local transmitter ground truth へ誤昇格させやすくなります。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Observability Budget との役割差</strong>
<p>
Observability Budget は <strong>何を直接観測したか</strong> を固定するカードで、latent-state error budget は <strong>未観測状態のうち、どれがいまの claim をまだ支配しているか</strong> を固定するカードでございます。前者だけでは「latent state が残る」としか書けず、後者だけでは measurement ceiling が消えます。したがって、本サイトでは <strong>L2 以上で両方を同時提出</strong>し、どちらかが欠ける場合は強い claim へ昇格させません。
</p>
</div>
<div class="note-box">
<strong>最低運用ルール</strong>
<p>
error budget が無い場合、本サイトでは結果を <strong>state-partial</strong> として扱い、augmentation claim は <strong>annotation</strong>、<strong>covariate</strong>、<strong>post hoc explanation</strong> のいずれかへ降格します。逆に、connectome-only baseline との比較、cross-day / perturbation / recovery の held-out gain、proxy specificity、abstention 条件まで出ていれば、「どの latent state をどこまで削ったか」を限定つきで一段強く読めます。
</p>
</div>
</section>

<section class="section" id="temporal-validity-card">
<h2 class="section-title">2026-03 追補：cross-day / longitudinal claim には Temporal Validity Card を添付する</h2>
<p>
今回の再監査で、サイト全体としてまだ最も改善余地が大きかった弱点は、<strong>same-day の score や短時間の closed-loop 成功を、cross-day stability や long-term deployability へ読み替える事故</strong>を、提出物仕様としてはまだ独立に止め切れていなかった点でございます。<a href="https://doi.org/10.1038/s41593-019-0502-4" target="_blank">Musall et al. (2019)</a> と <a href="https://doi.org/10.1038/s41593-023-01498-y" target="_blank">Benisty et al. (2024)</a> は、同一日内でも state fluctuation と自発行動が neural readout を大きく動かすことを示しました。<a href="https://doi.org/10.1038/s41593-019-0555-4" target="_blank">Gallego et al. (2020)</a>、<a href="https://doi.org/10.1038/s41467-023-40144-w" target="_blank">Roth &amp; Merriam (2023)</a>、<a href="https://doi.org/10.1038/s41593-025-01982-7" target="_blank">Noda et al. (2025)</a> は、population backbone の比較的安定性と unit / voxel レベルの drift が同時に起こりうることを示しました。さらに <a href="https://doi.org/10.1038/s41592-024-02440-1" target="_blank">van Beest et al. (2024)</a>、<a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">Wilson et al. (2025)</a>、<a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairagkar et al. (2025)</a> は、same-neuron claim、fixed decoder の保持期間、recalibration burden、silence / fallback を別々に監査しない限り、長期運用を読めないことを示しています。したがって本サイトでは、<strong>cross-day / longitudinal / deployable</strong> を名乗る結果に <strong>Temporal Validity Card</strong> を必須化し、時間軸の外挿を 1 行の注意書きではなく独立カードとして管理します。
</p>
<table class="data-table">
<thead>
<tr>
<th>Temporal Validity Card の欄</th>
<th>最低限書くこと</th>
<th>これが無いと起きる誤読</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>evaluation family と horizon</strong></td>
<td>within-session、cross-session、cross-subject、cross-state、multiday、closed-loop のどれかと、評価した日数 / セッション間隔を書きます。</td>
<td>same-day score を、そのまま別日耐性や長期運用へ読み替えやすくなります。</td>
</tr>
<tr>
<td><strong>fixed-model interval</strong></td>
<td>再学習なし decoder / controller を何日・何セッション hold したか、各 interval の劣化曲線を書きます。</td>
<td>高 score が fixed decoder の安定性から来たのか、頻繁な再較正から来たのかを切り分けられません。</td>
</tr>
<tr>
<td><strong>state annotation と maintenance covariate</strong></td>
<td>覚醒、睡眠 / wake 履歴、無意図運動、薬理状態、task engagement、recording context を、少なくとも長期比較で必要な粒度で残します。</td>
<td>state fluctuation や recovery history を、trait drift や decoder failure と誤認しやすくなります。</td>
</tr>
<tr>
<td><strong>interface / decoder drift audit</strong></td>
<td>再装着、impedance、channel dropout、probe drift、sorting version、drift correction、unit-match probability、feature shift を書きます。</td>
<td>biological drift と interface / decoder drift が混ざり、same-neuron claim や single-unit longitudinal claim を過大評価しやすくなります。</td>
</tr>
<tr>
<td><strong>population backbone / biological drift metric</strong></td>
<td>latent dynamics、representational similarity、cross-session identification、map homeostasis 指標など、骨格の安定性を示す metric を別列で残します。</td>
<td>unit-level の変化だけで「trait は無い」と読んだり、逆に population-level backbone だけで「全部安定」と読み過ぎたりします。</td>
</tr>
<tr>
<td><strong>recalibration burden と recovery route</strong></td>
<td>再較正頻度、所要時間、supervised / unsupervised の別、human intervention time、recovery time、失敗時 fallback を書きます。</td>
<td>accuracy や WER が維持された理由が、実際には heavy recalibration 依存だったことを隠しやすくなります。</td>
</tr>
<tr>
<td><strong>abstention / silence / tail risk</strong></td>
<td>abstention rate、silence / fallback rate、dropout、P50 / P95 / P99 latency、誤出力率を残します。</td>
<td>low-confidence 条件で止まる設計と、たまたま成功した high-confidence 条件を区別できません。</td>
</tr>
<tr>
<td><strong>transfer ceiling と abstention</strong></td>
<td>same-day only、same-subject cross-day、device-limited、clinic-only、local subsystem など、時間軸と運用環境の外挿上限を書きます。</td>
<td>限定つき decode や subsystem loop を、一般的な long-term deployability へ誤昇格させやすくなります。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>Observability Budget / latent-state error budget / Intervention Card との役割差</strong>
<p>
Observability Budget は <strong>何を直接見たか</strong>、latent-state error budget は <strong>どの hidden state がまだ claim を止めているか</strong>、Intervention Card は <strong>何をどの trigger と timing で変えたか</strong> を固定するカードです。Temporal Validity Card はそのどれでもなく、<strong>いまの証拠が何日・何状態・どの運用条件まで外挿できるか</strong>を固定するカードでございます。したがって、本サイトでは <strong>cross-day / longitudinal claim で独立提出</strong>させ、validity horizon を 1 行の注釈へ押し込みません。
</p>
</div>
<div class="note-box">
<strong>最低運用ルール</strong>
<p>
このカードが無い場合、本サイトでは結果を原則として <strong>within-session result</strong>、<strong>limited cross-session decode</strong>、または <strong>short-horizon online demo</strong> として扱い、longitudinal / deployable / maintenance-consistent claim へは上げません。特に <strong>fixed-model interval</strong>、<strong>state annotation</strong>、<strong>recalibration burden</strong> のいずれかが欠ける場合、same-day から cross-day への読替えを止めます。詳しい背景は <a href="wiki/state-trait-and-drift.html">Wiki: state・trait・ドリフト</a> に集約しています。
</p>
</div>
</section>

<section class="section" id="state-completeness-gate">
<h2 class="section-title">状態変数の完全性ゲート</h2>
<p>
2026年3月の一次文献監査では、<strong>「配線図がある」こと</strong>と<strong>「生成的に振る舞える」こと</strong>の間に、少なくとも 6 種類の抜けやすい状態変数があることを再確認しました。既存の細胞型・シナプス・遅延・神経修飾・グリアに加えて、今回あらためて <strong>内在興奮性 / 恒常性 set point</strong> を独立クラスとして切り出しました。したがって本サイトでは <strong>edge list だけの提出物を L2 以上の合格条件に使いません</strong>。
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
<td><strong>内在興奮性・恒常性 / 維持状態</strong></td>
<td>同じ graph と cell type でも、threshold、gain、firing-rate の戻り先、sleep / wake に依存した renormalization、compensation の仕方が違えば、同じ入力への応答と長期回復は変わります。</td>
<td>短期の活動一致があっても、cross-day stability、長期安定性、記憶配分は latent state 付きに留めます。</td>
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
<td>覚醒度や学習率の状態は静的配線から復元できず、瞳孔径や HRV は mixed arousal proxy にとどまり、receptor atlas は region prior であって momentary release ではありません。</td>
<td>トランスミッタ特異的な内部状態は主張せず、共変量・局所 chemical proxy・regional receptor prior を分けて扱います。</td>
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
connectome-complete は <strong>emulation-complete を意味しません</strong>。詳細な一次文献と、どの状態変数を最低提出物に入れるべきかの技術的根拠は <a href="wiki/connectome-is-not-enough.html">Wiki: 配線図だけでは足りない理由</a> に集約します。今回追加した <strong>内在興奮性 / 恒常性 / 維持状態</strong> の論点は、<a href="wiki/homeostatic-plasticity-and-maintenance-state.html">Wiki: 恒常性可塑性と維持状態</a> に切り出してあります。
</p>
</div>
<div class="note-box">
<strong>2026-03 追補：列挙ではなく augmentation / ablation で出す</strong>
<p>
今回の再監査で見えた弱点は、状態変数を「抜けています」と列挙するだけでは、何を足したら一段強い claim になるのかが読者に伝わりにくいことでした。そこで本サイトでは、<strong>connectome-only baseline</strong> と <strong>追加変数つきモデル</strong> を同じ held-out 条件で比較し、どの augmentation がどの誤差項を減らしたのかを提出物として要求します。
</p>
</div>
<table class="data-table">
<thead>
<tr>
<th>augmentation claim</th>
<th>最低限ほしい比較</th>
<th>合格したときに一段強く言えること</th>
<th>不合格時の読み替え</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>+ same-brain function / behavior</strong></td>
<td>connectome-only baseline と、same-brain function / behavior を足したモデルを同じ split で比較すること。</td>
<td>構造 atlas が、同一個体内の state-dependent response prediction にどこまで効くかを限定して言えます。</td>
<td>構造 scaffold と annotation に留め、dynamical claim へは上げません。</td>
</tr>
<tr>
<td><strong>+ transcriptomic / cell-type label</strong></td>
<td>node label を外した条件との ablation、target specificity や held-out response の gain を出すこと。</td>
<td>cell-type 情報が target-specific connectivity や応答予測をどれだけ改善したかを言えます。</td>
<td>cell-type は記述的なタグに留め、threshold / gain / set point まで自動補完しません。</td>
</tr>
<tr>
<td><strong>+ neuromodulatory proxy</strong></td>
<td>cross-state 条件での predictive gain、proxy specificity、compartment、spatial scope、receptor family、abstention を出すこと。</td>
<td>覚醒度や transmitter-linked state を、限定つき covariate / local chemical proxy / regional receptor prior として使えると書けます。</td>
<td>mixed arousal covariate に留め、ground truth や region-general transmitter field と言い換えません。</td>
</tr>
<tr>
<td><strong>+ glial / slow-state</strong></td>
<td>分オーダーの recovery、plasticity、perturbation aftermath で gain を示し、種差と cell-type 依存性を併記すること。</td>
<td>slow network state や可塑性の一部を、glia を含む条件付きモデルとして読めます。</td>
<td>neuron-only 近似の適用範囲を限定し、長期安定性 claim は降格します。</td>
</tr>
<tr>
<td><strong>+ excitability / homeostatic recovery log</strong></td>
<td>cross-day / cross-perturbation の held-out 劣化、recovery time、memory allocation proxy を出すこと。</td>
<td>長期安定性や記憶配分に対して、controller 側の状態が効いたと一段強く言えます。</td>
<td>短期の activity fit に留め、長期 claim と memory claim は latent state 付きに戻します。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>2026-03 追補：augmentation claim には measurement stack を添える</strong>
<p>
同じ「transcriptomic label を足した」「same-brain function を足した」でも、whole-brain spatial atlas、Patch-seq、volume EM、same-brain calcium+EM、local transmitter sensor では直接観測している変数が違います。したがって本サイトでは、augmentation claim に <strong>どの measurement stack で得た追加情報か</strong> を必ず添え、stack ごとの claim ceiling も別に書きます。整理表は <a href="wiki/measurement-stack-and-claim-ceiling.html">Wiki: 計測スタックごとの observability と claim ceiling</a> を参照してください。
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

<section class="section" id="consciousness-readout-gate">
<h2 class="section-title">2026-03 追補：意識 readout は 4 ゲートで受理する</h2>
<p>
今回さらに深掘りすべきだった弱点は、EEG / DoC / 麻酔文献を「no-report」「PCI」「resting-state」「multimodal」に分類するだけでは、<strong>どの条件で claim を一段上げてよいか</strong>がまだ operational でなかった点でございます。Cohen et al. (2024) と Fahrenfort et al. (2025) は、report / post-perceptual confound と criterion placement を別々に潰さなければ construct validity が壊れることを示しました。Gogulski et al. (2024) と Biabani et al. (2024) は、TMS-EEG の reliability と sensory contamination が target と time window に依存することを示し、Breyton et al. (2025) と Casarotto et al. (2024) は、resting-state complexity が有望でも PCI の置換ではなく同一 cohort での較正が要ることを示します。さらに Rohaut et al. (2024)、Kawai et al. (2025)、Manasova et al. (2026) は multimodal panel の前進を示しましたが、同時に behaviour-only baseline と missing-modality 条件を超えなければ deployability を主張できないことも意味します。したがって本サイトでは、意識関連 readout を以下の 4 ゲートで受理します。
</p>
<table class="data-table">
<thead>
<tr>
<th>ゲート</th>
<th>最低限出すもの</th>
<th>通っていないときに止める主張</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Construct-validity gate</strong></td>
<td>no-report / report の切り分け、criterion placement の別ログ、失敗条件の事前固定、少なくとも task / report confound を潰す設計根拠。</td>
<td>「この neural marker は意識内容そのものを読んだ」と言うことです。現状は decision strategy や post-perceptual processing を拾った可能性を残します。</td>
</tr>
<tr>
<td><strong>Perturbational gate</strong></td>
<td>TMS-EEG / intracranial perturbation の刺激部位、強度、対照、auditory / somatosensory control、artifact 窓、target-specific reliability。</td>
<td>PCI / PCI-ST 風の値だけで、state-level benchmark と呼ぶことです。条件ログが無ければ比較自体が崩れます。</td>
</tr>
<tr>
<td><strong>Calibration gate</strong></td>
<td>同一 cohort で PCI、行動評価、臨床アウトカム、pipeline 感度分析、棄権閾値へ較正すること。</td>
<td>resting-state complexity、criticality、受動 EEG classifier を単独の bedside meter と呼ぶことです。外部較正前は補助 proxy に留めます。</td>
</tr>
<tr>
<td><strong>Incremental / deployability gate</strong></td>
<td>behaviour-only baseline との比較、施設外一般化、missing-modality 条件での頑健性、校正誤差、測定負荷の報告。</td>
<td>multimodal panel を ready-to-deploy と書くことです。平均精度だけでは臨床運用の根拠になりません。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>最低運用ルール</strong>
<p>
no-report / criterion placement は <strong>construct-validity gate</strong>、PCI / PCI-ST は <strong>perturbational gate</strong> を通ったときだけ主 benchmark 候補、resting-state 複雑性 / 臨界性は <strong>calibration gate</strong> を通るまで補助 proxy、multimodal clinical panel は <strong>incremental / deployability gate</strong> を通るまで exploratory panel として扱います。つまり本サイトでは、同じ「意識指標」でも gate が違えば claim ceiling も違います。
</p>
</div>
</section>

<section class="section" id="causal-perturbation-suite">
<h2 class="section-title">因果的摂動スイート（4ゲート制へ再編）</h2>
<p>
2026年3月の一次文献監査では、現行の BCI / neuromodulation 文献が示しているのは、一足飛びの「反事実同値」ではなく、<strong>段階ごとに強さの違う因果証拠</strong>であることを再確認しました。そこで本サイトでは、offline 精度、online human-in-the-loop、局所 causal intervention、長期閉ループを分けて扱い、<strong>精度が高いだけの結果</strong>を L2 / L3 に繰り上げません。
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
<table class="data-table">
<thead>
<tr>
<th>ゲート</th>
<th>最低限ほしい実証</th>
<th>いまの代表例</th>
<th>まだ言えないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Gate 1 / online decode</strong></td>
<td>被験者が出力を見ながら連続操作または会話し、offline ではなく online 指標で比較すること。</td>
<td>Forenzo et al. (2024), Willett et al. (2023), Littlejohn et al. (2025)</td>
<td>これだけで因果構造一致や反事実同値までは言えません。</td>
</tr>
<tr>
<td><strong>Gate 2 / bidirectional perturbation</strong></td>
<td>feedback や刺激が次の入力を変える双方向 loop を持ち、介入で行動が変わること。</td>
<td>Flesher et al. (2021)</td>
<td>局所サブシステムの causal gain は示せても、全脳WBEの成立は示しません。</td>
</tr>
<tr>
<td><strong>Gate 3 / state-dependent intervention</strong></td>
<td>検出した状態に応じて刺激や制御を切り替え、実生活ブロック比較まで含めて改善を示すこと。</td>
<td>Oehrn et al. (2024), Dixon et al. (2026)</td>
<td>課題特異的 controller の有効性であり、state completeness は未解決です。</td>
</tr>
<tr>
<td><strong>Gate 4 / longitudinal stability</strong></td>
<td>固定 decoder の劣化、再較正頻度、棄権率、停止条件を公開すること。</td>
<td>Wairagkar et al. (2025), Wilson et al. (2025), Cascino et al. (2026)</td>
<td>長く使えない系を、短いデモだけで L3 完了とは扱えません。</td>
</tr>
</tbody>
</table>
<div class="key-points">
<h4>三段階の導入</h4>
<ul>
<li><strong>Stage A / いま実行できる検証：</strong>公開 EEG や既存 BCI データで、被験者外一般化、未学習条件、online 指標、棄権、校正誤差を事前登録して比較します。Stage A を通っても、主張は L1〜弱い L2 に留めます。</li>
<li><strong>Stage B / 外部基準つき中間検証：</strong>シミュレーション、ファントム、頭蓋内刺激、同時侵襲記録など ground truth のある系で、応答誤差、不確実性、回復時間を測ります。source imaging や摂動応答の改善主張は、この段階を通さない限り強く言いません。</li>
<li><strong>Stage C / 実介入：</strong>TMS-EEG、adaptive stimulation、薬理学的介入は強い検証力を持つ一方、IRB、機材、被験者運用が前提です。本リポジトリでは要求仕様と公開ログ形式を先行整備し、実験実施自体は外部依存タスクとして分離します。</li>
</ul>
</div>
<div class="note-box">
<strong>評価指標</strong>
<p>
一次判定では、事前登録した effect size、OOD 条件での頑健性、校正誤差、棄権率、不確実性の幅に加え、<strong>end-to-end latency の P50 / P95 / P99</strong>、<strong>jitter</strong>、<strong>dropout</strong>、<strong>recalibration burden</strong>、<strong>recovery time after perturbation</strong> を優先します。PCI-ST 空間分布、パーシステンス図の Bottleneck distance、生成モデル間距離の Fisher Information Metric (FIM) は補助解析として残し、主要な合否判定を一手法へ依存させません。
</p>
</div>
<div class="note-box">
<strong>反事実という語を安売りしない</strong>
<p>
分岐条件、比較規則、失敗条件、刺激アーチファクト窓が事前固定されていない場合、本サイトではそれを「反事実同値」とは呼ばず、より弱い表現である <strong>介入応答テスト</strong> または <strong>摂動一般化テスト</strong> と表記します。
</p>
</div>
</section>

<section class="section" id="intervention-card">
<h2 class="section-title">2026-03 追補：L2 以上の介入・閉ループ結果には Intervention Card を添付する</h2>
<p>
今回もっとも改善余地が大きかった弱点は、<strong>因果・閉ループ結果に対して、Fusion Card や Pretraining Card に相当する標準提出物がまだ無かった</strong>ことです。<a href="https://doi.org/10.1016/j.brs.2017.11.016" target="_blank">Zrenner et al. (2018)</a> は EEG-triggered TMS が <strong>どの brain state を、どのタイミングで叩いたか</strong>で結果が変わることを示し、<a href="https://doi.org/10.1038/s41591-024-03196-z" target="_blank">Oehrn et al. (2024)</a> は adaptive DBS の有効性が <strong>どの neural marker を state estimate として選び、どの comparator と blinded block で比べたか</strong>に依存することを示しました。さらに <a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">Littlejohn et al. (2025)</a> は 80 ms 単位の streaming 音声合成と continuous decode を示し、<a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">Wilson et al. (2025)</a> は accumulating neural change に対して <strong>再較正をどう回したか</strong>が長期運用の本体だと示しました。加えて <a href="https://doi.org/10.1113/JP283986" target="_blank">Gordon et al. (2023)</a> は、TMS-EEG では optimized sham を置かないと <strong>TMS 本体の応答</strong>と<strong>感覚入力由来の応答</strong>を切り分けにくいことを示しています。したがって本サイトでは、<strong>「adaptive」「closed-loop」「perturbation」</strong>というラベルだけでは因果証拠を受理せず、比較可能性を保つための <strong>Intervention Card</strong> を必須化します。
</p>
<table class="data-table">
<thead>
<tr>
<th>Intervention Card の欄</th>
<th>最低限書くこと</th>
<th>これが無いと何が起きるか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>target / actuator / comparator</strong></td>
<td>刺激部位、記録部位、アクチュエータ、波形、強度、duty cycle、比較条件（continuous、sham、no-stim、fixed decoder など）を書きます。</td>
<td>同じ `adaptive` という語でも、何を実際に変えた研究なのか比較不能になります。</td>
</tr>
<tr>
<td><strong>state estimate / trigger rule</strong></td>
<td>使った biomarker、しきい値または decoder、calibration window、confidence / abstention、fallback rule を書きます。</td>
<td>state-dependent claim を、後付けの threshold tuning や operator judgment と切り分けられません。</td>
</tr>
<tr>
<td><strong>timing audit</strong></td>
<td>clock domain、sense→decode→decide→actuate の経路、update cadence、end-to-end latency の P50 / P95 / P99、jitter、resync policy を書きます。</td>
<td>ms-sensitive intervention を、実際には timing が合っていない系と区別できません。</td>
</tr>
<tr>
<td><strong>control / sham / artifact handling</strong></td>
<td>optimized sham、active control、artifact window、masking、除外試行、前処理 pipeline version、採用しなかった cleaning 条件を残します。</td>
<td>刺激応答を sensory confound や cleaning artifact と取り違えやすくなります。</td>
</tr>
<tr>
<td><strong>safety / stop rule</strong></td>
<td>intensity limit、manual override、kill switch、adverse event、resume 条件、在宅/臨床の監視条件を書きます。</td>
<td>動いたデモと安全に運用できる系が同じ強さの evidence に見えてしまいます。</td>
</tr>
<tr>
<td><strong>online stability / recovery</strong></td>
<td>dropout、abstention、fixed decoder interval、recalibration burden、human intervention time、recovery time after perturbation を書きます。</td>
<td>短時間デモを、そのまま deployable な closed loop と誤読しやすくなります。</td>
</tr>
<tr>
<td><strong>claim ceiling</strong></td>
<td>communication route、symptom control、local causal gain など、到達してよい上限を明示します。</td>
<td>局所サブシステムの成功を、全脳WBE や state completeness へ誤昇格させやすくなります。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>最低運用ルール</strong>
<p>
Intervention Card が無い場合、本サイトではその結果を原則として <strong>online demo</strong>、<strong>exploratory intervention</strong>、または <strong>limited subsystem casework</strong> として扱い、L2/L3 の強い因果主張へ上げません。とくに <strong>timing audit</strong>、<strong>control / sham</strong>、<strong>recalibration burden</strong> のいずれかが欠ける場合、state-dependent / deployable / longitudinal の読替えを止めます。
</p>
</div>
<div class="note-box">
<strong>既存カードとの役割差</strong>
<p>
Observability Budget は「何を直接見たか」、Fusion Card は「どう結び付けたか」、latent-state error budget は「どの hidden state がまだ誤差を支配するか」を固定します。Intervention Card はその外側で、<strong>何を、どの trigger と comparator で、どの timing / artifact / safety 条件の下に実際に変えたか</strong>を固定するカードでございます。したがって、因果・閉ループ結果では <strong>Intervention Card を追加提出</strong>します。
</p>
</div>
</section>

<section class="section" id="calibration-abstention-card">
<h2 class="section-title">2026-03 追補：確率・区間・予測集合・棄権を出す結果には Calibration &amp; Abstention Card を添付する</h2>
<p>
今回さらに改善余地が大きかった弱点は、<strong>confidence / posterior / prediction set / abstention</strong> を各ページで注意書きとしては扱えていても、Observability Budget や Temporal Validity Card のような <strong>独立した提出物仕様</strong> にまだ落とせていなかったことです。<a href="https://www.mdpi.com/2227-7390/11/7/1650" target="_blank">Shafiezadeh et al. (2023)</a> は patient-independent seizure prediction で split 設計そのものが generalization estimate を大きく動かすことを示し、<a href="https://doi.org/10.3390/s24092863" target="_blank">Shafiezadeh et al. (2024)</a> と <a href="https://doi.org/10.3389/fnins.2023.1184990" target="_blank">Segal et al. (2023)</a> は calibration / risk control が threshold 設計を直接変えることを示しました。さらに <a href="https://papers.nips.cc/paper_files/paper/2019/hash/8558cb408c1d76621371888657d2eb1d-Abstract.html" target="_blank">Ovadia et al. (2019)</a> は predictive uncertainty methods が dataset shift 下で広く劣化しうることを、<a href="https://proceedings.mlr.press/v235/han24d.html" target="_blank">Han et al. (2024)</a> は model assessment / selection 自体を temporal distribution shift に合わせて設計し直す必要を示しました。加えて <a href="https://doi.org/10.1080/01621459.2017.1307116" target="_blank">Lei et al. (2018)</a> と <a href="https://doi.org/10.1073/pnas.2107794118" target="_blank">Chernozhukov et al. (2021)</a> は calibration split を用いた conformal route を与え、<a href="https://proceedings.mlr.press/v105/eliades19a.html" target="_blank">Eliades &amp; Papadopoulos (2019)</a> は BCI / exoskeleton control で conformal prediction を safety design に組み込めることを示しました。したがって本サイトでは、確率や区間を出しただけでは「校正済み」「安全に棄権できる」「deployable threshold」とは読まず、<strong>Calibration &amp; Abstention Card</strong> で split、slice、coverage-risk、fallback を提出物化します。
</p>
<table class="data-table">
<thead>
<tr>
<th>Calibration &amp; Abstention Card の欄</th>
<th>最低限書くこと</th>
<th>これが無いと何が起きるか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>uncertainty target</strong></td>
<td>class probability、interval、prediction set、risk score、abstention flag のどれを出したかを書きます。</td>
<td>scalar confidence と set-valued output を同じ「信頼度」と誤読します。</td>
</tr>
<tr>
<td><strong>fit / calibration / test separation</strong></td>
<td>model fit、temperature scaling / conformal / threshold tuning、最終 test をどの split で分けたか、freeze date と再調整可否を書きます。</td>
<td>test を見ながら閾値や温度を触った結果を、校正済み evidence と誤読します。</td>
</tr>
<tr>
<td><strong>evaluation family / shift slices</strong></td>
<td>within-session、cross-session、cross-subject、cross-site、temporal、OOD のどれかと、device / state / cohort / time の slice を書きます。</td>
<td>same-day の ECE や coverage を、cross-day / cross-patient の reliability へ不当に読み替えます。</td>
</tr>
<tr>
<td><strong>metrics / validity statement</strong></td>
<td>ECE、Brier、NLL、empirical coverage、interval width、prediction-set size、false alarm rate、marginal / conditional / temporal validity のどれを保証したかを書きます。</td>
<td>よい calibration だと思っていたものが、実際には平均的な 1 指標だけだった可能性を見落とします。</td>
</tr>
<tr>
<td><strong>selective prediction / fallback policy</strong></td>
<td>abstention threshold、coverage-risk trade-off、silence / hold-last-output / remeasure / manual review の分岐、false alarm ceiling を書きます。</td>
<td>低信頼時に何が起きるか不明なまま、「安全な棄権がある」と書いてしまいます。</td>
</tr>
<tr>
<td><strong>recalibration policy</strong></td>
<td>online / longitudinal 系では、いつ再較正を許すか、誰が介入するか、state drift をどう検知するかを書きます。</td>
<td>calibration が固定モデルの性質なのか、人手更新込みの運用成績なのかが混ざります。</td>
</tr>
<tr>
<td><strong>claim ceiling</strong></td>
<td>calibrated probability、risk-controlled alarm、safe abstention、deployable threshold からまだ言えないことを 1 行で固定します。</td>
<td>単一 cohort や単一 horizon の calibration を、一般的な reliability と誤昇格させやすくなります。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>最低運用ルール</strong>
<p>
Calibration &amp; Abstention Card が無い場合、本サイトではその結果を原則として <strong>exploratory confidence output</strong>、<strong>uncalibrated score ranking</strong>、または <strong>local thresholded demo</strong> として扱い、calibrated probability、risk-controlled alarm、safe abstention、deployable threshold claim へ上げません。とくに <strong>fit / calibration / test separation</strong>、<strong>evaluation family / shift slices</strong>、<strong>fallback policy</strong> のいずれかが欠ける場合、confidence の読み替えを止めます。
</p>
</div>
<div class="note-box">
<strong>既存カードとの役割差</strong>
<p>
Model Card は <strong>モデルの弱点と失敗例</strong> を固定し、Benchmark Governance Card は <strong>score の露出条件</strong> を固定し、Temporal Validity Card は <strong>その結果を何日・何状態まで外挿できるか</strong> を固定します。Calibration &amp; Abstention Card はその中で、<strong>confidence / interval / set / fallback の意味</strong> を固定するカードでございます。したがって本サイトでは、確率や棄権を前面に出す結果に <strong>Calibration &amp; Abstention Card を別提出</strong> させ、model strength と reliability semantics を混ぜません。
</p>
</div>
</section>

<section class="section" id="benchmark-governance-card">
<h2 class="section-title">2026-03 追補：leaderboard / challenge 結果には Benchmark Governance Card を添付する</h2>
<p>
今回さらに改善余地が大きかった弱点は、<strong>benchmark の score を受け取る側の提出物仕様がまだ弱く、split と metric を知っていても、その score が adaptive に擦られたものか、hidden final test で確定したものか、checkpoint 選択込みでどこまで固定されているかが見えにくかった</strong>ことです。<a href="https://doi.org/10.1088/1741-2552/aadea0" target="_blank">Jayaram &amp; Barachant (2018)</a> と <a href="https://moabb.neurotechx.com/docs/index.html" target="_blank">MOABB Docs</a> は fair evaluation family を整えましたが、<a href="https://proceedings.mlr.press/v37/blum15.html" target="_blank">Blum &amp; Hardt (2015)</a> は leaderboard が repeated submission により adaptive hold-out になりうることを示しました。他方、<a href="https://papers.neurips.cc/paper_files/paper/2019/hash/ee39e503b6bedf0c98c388b7e8589aca-Abstract.html" target="_blank">Roelofs et al. (2019)</a> は、separate final test で最終順位を決める設計では public leaderboard overfitting が必ずしも大きくないことも示しています。歴史的にも <a href="https://www.bbci.de/competition/iv/" target="_blank">BCI Competition IV</a> は labeled calibration + unlabeled evaluation と 1 researcher 1 result を採り、<a href="https://eeg2025.github.io/rules/" target="_blank">EEG Challenge 2025 Rules</a> と <a href="https://eeg2025.github.io/submission/" target="_blank">Submission</a> は code submission、single-GPU inference、daily submission limit、extra dataset / pretrained model の明示を要求しています。さらに <a href="https://arxiv.org/abs/2508.17742" target="_blank">Xiong et al. (2025)</a> は standardized evaluation の欠如が比較を壊すと明示し、<a href="https://arxiv.org/abs/2603.02268" target="_blank">Lahiri et al. (2026)</a> は split construction、checkpoint selection、segment length、normalization など 6 要因の不整合で ranking が反転しうると報告しました。したがって本サイトでは、score だけでなく <strong>score の露出条件そのもの</strong>を提出物にします。
</p>
<table class="data-table">
<thead>
<tr>
<th>Benchmark Governance Card の欄</th>
<th>最低限書くこと</th>
<th>これが無いと何が起きるか</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>benchmark object</strong></td>
<td>benchmark 名、version、task 定義、metric、dataset snapshot / DOI、freeze date を書きます。</td>
<td>同名 benchmark の別 protocol を同一比較だと誤読します。</td>
</tr>
<tr>
<td><strong>split / hold-out unit</strong></td>
<td>subject / session / trial / site / device のどれを独立単位とし、validation と test をどう分けたかを書きます。</td>
<td>ranking 差を model 能力の差と読み、実際には split 差だった可能性を見落とします。</td>
</tr>
<tr>
<td><strong>evaluation surface</strong></td>
<td>public leaderboard、private leaderboard、unlabeled evaluation、code submission、prediction upload のどれかを書きます。</td>
<td>adaptive feedback 下の score を、one-shot final test と同じ強さの evidence と誤読します。</td>
</tr>
<tr>
<td><strong>submission budget</strong></td>
<td>submission cap、team 単位か個人単位か、再提出の回数、final ranking が別 hold-out かを書きます。</td>
<td>public score 最適化の余地を hidden にしたまま、公平比較だと書いてしまいます。</td>
</tr>
<tr>
<td><strong>model-selection policy</strong></td>
<td>checkpoint selection、ensemble 可否、validation で見てよい情報、post-hoc tuning の可否を書きます。</td>
<td>ranking 差を model の差と読み、実際には選択規則の差だった可能性を落とします。</td>
</tr>
<tr>
<td><strong>external data / pretraining disclosure</strong></td>
<td>追加 dataset、事前学習 corpus、既存 foundation model、metadata / report の外部利用を列挙します。</td>
<td>同じ benchmark score を、同じ情報条件で得た結果だと誤読します。</td>
</tr>
<tr>
<td><strong>runtime envelope</strong></td>
<td>推論 hardware、memory 上限、実行時間制約、主要 package version、determinism 条件を書きます。</td>
<td>engineering 上の実装差を、科学的優位と混同します。</td>
</tr>
<tr>
<td><strong>post-benchmark audit trail</strong></td>
<td>code release、inference log、rerun 手順、protocol 更新履歴、external hold-out の有無を書きます。</td>
<td>competition 後に再現不能な ranking が、そのまま frontier result として残ります。</td>
</tr>
<tr>
<td><strong>claim ceiling</strong></td>
<td>single benchmark win からまだ言えないことを 1 行で固定します。たとえば universal ranking、cross-site deployability、general decoder です。</td>
<td>単発の勝利を、そのまま broad generalization や production-ready 系と誤昇格させやすくなります。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>最低運用ルール</strong>
<p>
Benchmark Governance Card が無い場合、本サイトではその結果を原則として <strong>exploratory leaderboard result</strong>、<strong>single-protocol benchmark score</strong>、または <strong>local challenge outcome</strong> として扱い、cross-paper frontier ranking や deployable generalization claim へ上げません。とくに <strong>evaluation surface</strong>、<strong>submission budget</strong>、<strong>model-selection policy</strong> のいずれかが欠ける場合、public score の読み替えを止めます。
</p>
</div>
<div class="note-box">
<strong>既存カードとの役割差</strong>
<p>
Model Card は <strong>モデルの弱点と失敗例</strong>を固定し、Pretraining Card は <strong>事前学習 corpus と adaptation 条件</strong>を固定し、Benchmark Governance Card は <strong>score を比較可能にする評価面</strong>を固定します。Observability Budget や Intervention Card は、それぞれ measurement ceiling と causal evidence を扱います。したがって本サイトでは、leaderboard / challenge 結果を受け取るときに <strong>Benchmark Governance Card を別提出</strong>し、model 側と benchmark 側の責任を混ぜません。
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
NESS（非平衡定常状態）や time irreversibility を使って脳ダイナミクスを調べる研究は重要ですが、本サイトでは 2026-03 時点で<strong>補助的な研究トラック</strong>と位置づけます。不可逆性指標の有用性は示されつつある一方、WBE 検証の共通受け入れ基準としては、まだモダリティ依存性と推定仮定の影響が大きいためです。特に、粗視化した neural data から推定される entropy production は、しばしば <strong>information-theoretic lower bound</strong> であり、微視的な物理散逸そのものとは切り分けて読む必要があります。
</p>
<div class="key-points">
<h4>現時点で言えること</h4>
<ul>
<li><strong>詳細釣り合いの破れは観測されうる：</strong>脳活動から entropy production の下界を推定する研究はあり、不可逆性が神経ダイナミクスの情報を持つこと自体は支持されています。</li>
<li><strong>ただし解釈はモダリティ依存です：</strong>意識状態と不可逆性の関連は fMRI や ECoG などでも報告されていますが、粗視化、時間分解能、前処理、推定器で見え方が変わります。EEG/ECoG/fMRI の不可逆性を、代謝散逸や hardware power と同一視してはなりません。</li>
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
<li>Jeung, J., et al. (2024). Motion-BIDS. <a href="https://doi.org/10.1038/s41597-024-03559-8" target="_blank">doi:10.1038/s41597-024-03559-8</a></li>
<li>Bigdely-Shamlo, N., et al. (2016). Hierarchical Event Descriptors (HED). <a href="https://doi.org/10.3389/fninf.2016.00042" target="_blank">doi:10.3389/fninf.2016.00042</a></li>
<li>Hermes, D., et al. (2025). HED library schema for EEG data annotation. <a href="https://doi.org/10.1038/s41597-025-05791-2" target="_blank">doi:10.1038/s41597-025-05791-2</a></li>
<li>Pernet, C., et al. (2020). COBIDAS-MEEG recommendations. <a href="https://doi.org/10.1038/s41593-020-00709-0" target="_blank">doi:10.1038/s41593-020-00709-0</a></li>
<li>Kothe, C. A., et al. (2025). The lab streaming layer for synchronized multimodal recording. <a href="https://doi.org/10.1162/imag.a.136" target="_blank">doi:10.1162/imag.a.136</a></li>
<li>Markiewicz, C. J., et al. (2021). OpenNeuro resource paper. <a href="https://doi.org/10.7554/eLife.71774" target="_blank">doi:10.7554/eLife.71774</a></li>
<li>Goldberger, A. L., et al. (2000). PhysioBank / PhysioNet. <a href="https://doi.org/10.1161/01.CIR.101.23.e215" target="_blank">doi:10.1161/01.CIR.101.23.e215</a></li>
<li>Jayaram, V., &amp; Barachant, A. (2018). MOABB: trustworthy algorithm benchmarking for BCIs. <a href="https://doi.org/10.1088/1741-2552/aadea0" target="_blank">doi:10.1088/1741-2552/aadea0</a></li>
<li>Blum, A., &amp; Hardt, M. (2015). The Ladder: A Reliable Leaderboard for Machine Learning Competitions. <a href="https://proceedings.mlr.press/v37/blum15.html" target="_blank">PMLR 37</a></li>
<li>Roelofs, R., Shankar, V., Recht, B., Fridovich-Keil, S., Hardt, M., Miller, J., &amp; Schmidt, L. (2019). A Meta-Analysis of Overfitting in Machine Learning. <a href="https://papers.neurips.cc/paper_files/paper/2019/hash/ee39e503b6bedf0c98c388b7e8589aca-Abstract.html" target="_blank">NeurIPS 2019</a></li>
<li><a href="https://www.bbci.de/competition/iv/" target="_blank">BCI Competition IV</a>（official website）</li>
<li><a href="https://eeg2025.github.io/rules/" target="_blank">EEG Challenge (2025): Rules</a></li>
<li><a href="https://eeg2025.github.io/submission/" target="_blank">EEG Challenge (2025): Submission</a></li>
<li>Xiong, W., Li, J., Li, J., Zhu, K., &amp; Jiang, C. (2025). EEG-FM-Bench: A Comprehensive Benchmark for the Systematic Evaluation of EEG Foundation Models. <a href="https://arxiv.org/abs/2508.17742" target="_blank">arXiv:2508.17742</a></li>
<li>Lahiri, J. B., Runwal, P., Kulkarni, A., Jain, M., Mishra, A. R., Panwar, S., &amp; Singh, S. (2026). PRISM: Exploring Heterogeneous Pretrained EEG Foundation Model Transfer to Clinical Differential Diagnosis. <a href="https://arxiv.org/abs/2603.02268" target="_blank">arXiv:2603.02268</a></li>
<li>Wei, H., et al. (2020). Bayesian fusion and multimodal DCM for EEG and fMRI. <a href="https://doi.org/10.1016/j.neuroimage.2019.116595" target="_blank">doi:10.1016/j.neuroimage.2019.116595</a></li>
<li>Jorge, J., et al. (2015). Simultaneous EEG-fMRI at ultra-high field: artifact prevention and safety assessment. <a href="https://doi.org/10.1016/j.neuroimage.2014.10.055" target="_blank">doi:10.1016/j.neuroimage.2014.10.055</a></li>
<li>Aydin, U., et al. (2014). Combining EEG and MEG for the reconstruction of epileptic activity using a calibrated realistic volume conductor model. <a href="https://doi.org/10.1371/journal.pone.0093154" target="_blank">doi:10.1371/journal.pone.0093154</a></li>
<li>Michel, C. M., &amp; Brunet, D. (2019). EEG source imaging: a practical review. <a href="https://doi.org/10.3389/fneur.2019.00325" target="_blank">doi:10.3389/fneur.2019.00325</a></li>
<li>Mikulan, E., et al. (2020). Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. <a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">doi:10.1038/s41597-020-0467-x</a></li>
<li>Unnwongse, K., et al. (2023). Validating EEG source imaging using intracranial electrical stimulation. <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">doi:10.1093/braincomms/fcad023</a></li>
<li>Hao, S., et al. (2025). HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. <a href="https://doi.org/10.1111/epi.18552" target="_blank">doi:10.1111/epi.18552</a></li>
<li>Delorme, A. (2023). EEG is better left alone. <a href="https://doi.org/10.1038/s41598-023-27528-0" target="_blank">doi:10.1038/s41598-023-27528-0</a></li>
<li>Klug, M., &amp; Kloosterman, N. A. (2022). Zapline-plus. <a href="https://doi.org/10.1002/hbm.25832" target="_blank">doi:10.1002/hbm.25832</a></li>
<li>Hernandez-Pavon, J. C., et al. (2023). TMS combined with EEG: recommendations and open issues. <a href="https://doi.org/10.1016/j.brs.2023.02.009" target="_blank">doi:10.1016/j.brs.2023.02.009</a></li>
<li>Casali, A. G., et al. (2013). A theoretically based index of consciousness independent of sensory processing and behavior. <a href="https://doi.org/10.1126/scitranslmed.3006294" target="_blank">doi:10.1126/scitranslmed.3006294</a></li>
<li>Comolatti, R., et al. (2019). A fast and general method to empirically estimate the complexity of brain responses to transcranial and intracranial stimulations. <a href="https://doi.org/10.1016/j.brs.2019.05.013" target="_blank">doi:10.1016/j.brs.2019.05.013</a></li>
<li>Forenzo, D., et al. (2024). Continuous tracking using deep learning-based decoding for noninvasive brain-computer interface. <a href="https://doi.org/10.1093/pnasnexus/pgae145" target="_blank">doi:10.1093/pnasnexus/pgae145</a></li>
<li>Zrenner, C., Desideri, D., Belardinelli, P., &amp; Ziemann, U. (2018). Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. <a href="https://doi.org/10.1016/j.brs.2017.11.016" target="_blank">doi:10.1016/j.brs.2017.11.016</a></li>
<li>Gordon, P. C., Song, Y. F., Jovellar, D. B., Rostami, M., Belardinelli, P., &amp; Ziemann, U. (2023). Untangling TMS-EEG responses caused by TMS versus sensory input using optimized sham control and GABAergic challenge. <a href="https://doi.org/10.1113/JP283986" target="_blank">doi:10.1113/JP283986</a></li>
<li>Willett, F. R., et al. (2023). A high-performance speech neuroprosthesis. <a href="https://doi.org/10.1038/s41586-023-06377-x" target="_blank">doi:10.1038/s41586-023-06377-x</a></li>
<li>Littlejohn, K. T., et al. (2025). A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. <a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">doi:10.1038/s41593-025-01905-6</a></li>
<li>Wairagkar, M., et al. (2025). An instantaneous voice-synthesis neuroprosthesis. <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">doi:10.1038/s41586-025-09127-3</a></li>
<li>Flesher, S. N., et al. (2021). A brain-computer interface that evokes tactile sensations improves robotic arm control. <a href="https://doi.org/10.1126/science.abd0380" target="_blank">doi:10.1126/science.abd0380</a></li>
<li>Wilson, G. H., et al. (2025). Long-term unsupervised recalibration of intracortical brain-computer interfaces using a hidden Markov model. <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">doi:10.1038/s41551-025-01536-z</a></li>
<li>Steinmetz, N. A., Aydin, C., Lebedeva, A., et al. (2021). Neuropixels 2.0: A miniaturized high-density probe for stable, long-term brain recordings. <a href="https://doi.org/10.1126/science.abf4588" target="_blank">doi:10.1126/science.abf4588</a></li>
<li>Pachitariu, M., et al. (2024). Spike sorting with Kilosort4. <a href="https://doi.org/10.1038/s41592-024-02595-5" target="_blank">doi:10.1038/s41592-024-02595-5</a></li>
<li>Trautmann, E. M., Stavisky, S. D., Lahiri, S., et al. (2019). Accurate estimation of neural population dynamics without spike sorting. <a href="https://doi.org/10.1016/j.neuron.2019.05.003" target="_blank">doi:10.1016/j.neuron.2019.05.003</a></li>
<li>van Beest, E. H., Jia, X., Deng, X., et al. (2024). Tracking neurons across days with high-density probes. <a href="https://doi.org/10.1038/s41592-024-02440-1" target="_blank">doi:10.1038/s41592-024-02440-1</a></li>
<li>Gregory, N. S., et al. (2023). Structural and functional changes of deep layer pyramidal neurons surrounding implanted microelectrode arrays in rat motor cortex. <a href="https://doi.org/10.1088/1741-2552/ace8ac" target="_blank">doi:10.1088/1741-2552/ace8ac</a></li>
<li>Musall, S., Kaufman, M. T., Juavinett, A. L., Gluf, S., &amp; Churchland, A. K. (2019). Single-trial neural dynamics are dominated by richly varied movements. <a href="https://doi.org/10.1038/s41593-019-0502-4" target="_blank">doi:10.1038/s41593-019-0502-4</a></li>
<li>Gallego, J. A., Perich, M. G., Chowdhury, R. H., Solla, S. A., &amp; Miller, L. E. (2020). Long-term stability of cortical population dynamics underlying consistent behavior. <a href="https://doi.org/10.1038/s41593-019-0555-4" target="_blank">doi:10.1038/s41593-019-0555-4</a></li>
<li>Benisty, H., Barson, D., Moberly, A. H., Lohani, S., Tang, L., Coifman, R. R., Crair, M. C., Cardin, J. A., &amp; Higley, M. J. (2024). Rapid fluctuations in functional connectivity of cortical networks encode spontaneous behavior. <a href="https://doi.org/10.1038/s41593-023-01498-y" target="_blank">doi:10.1038/s41593-023-01498-y</a></li>
<li>Roth, Z. N., &amp; Merriam, E. P. (2023). Representations in human primary visual cortex drift over time. <a href="https://doi.org/10.1038/s41467-023-40144-w" target="_blank">doi:10.1038/s41467-023-40144-w</a></li>
<li>Noda, T., Kienle, E., Eppler, J.-B., Aschauer, D. F., Kaschube, M., Loewenstein, Y., &amp; Rumpel, S. (2025). Homeostasis of a representational map in the neocortex. <a href="https://doi.org/10.1038/s41593-025-01982-7" target="_blank">doi:10.1038/s41593-025-01982-7</a></li>
<li>Oehrn, C. R., et al. (2024). Chronic adaptive deep brain stimulation versus conventional stimulation in Parkinson's disease: a blinded randomized feasibility trial. <a href="https://doi.org/10.1038/s41591-024-03196-z" target="_blank">doi:10.1038/s41591-024-03196-z</a></li>
<li>Dixon, S., et al. (2026). Movement-responsive deep brain stimulation for Parkinson’s disease using a remotely optimized neural decoder. <a href="https://doi.org/10.1038/s41551-025-01592-5" target="_blank">doi:10.1038/s41551-025-01592-5</a></li>
<li>Cascino, S., et al. (2026). Chronic adaptive deep brain stimulation in Parkinson’s disease: ADAPT-START findings and programming principles. <a href="https://doi.org/10.1038/s41531-026-01269-z" target="_blank">doi:10.1038/s41531-026-01269-z</a></li>
<li>Lynn, C. W., et al. (2021). Broken detailed balance and entropy production in the human brain. <a href="https://doi.org/10.1073/pnas.2109889118" target="_blank">doi:10.1073/pnas.2109889118</a></li>
<li>de la Fuente, L. A., et al. (2022). Temporal irreversibility of neural dynamics as a signature of consciousness. <a href="https://doi.org/10.1093/cercor/bhac177" target="_blank">doi:10.1093/cercor/bhac177</a></li>
<li>Ishihara, K., &amp; Shimazaki, H. (2025). State-space kinetic Ising model reveals task-dependent entropy flow in sparsely active nonequilibrium neuronal dynamics. <a href="https://doi.org/10.1038/s41467-025-66669-w" target="_blank">doi:10.1038/s41467-025-66669-w</a></li>
<li>Cohen, M. A., et al. (2024). Neural signatures of visual awareness independent of postperceptual processing. <a href="https://doi.org/10.1093/cercor/bhae415" target="_blank">doi:10.1093/cercor/bhae415</a></li>
<li>Fahrenfort, J. J., et al. (2025). Criterion placement threatens the construct validity of neural measures of consciousness. <a href="https://doi.org/10.7554/eLife.102335" target="_blank">doi:10.7554/eLife.102335</a></li>
<li>Gogulski, J., et al. (2024). The reliability and variability of TMS-evoked potentials in the dorsolateral prefrontal cortex in healthy adults. <a href="https://doi.org/10.1016/j.brs.2024.06.001" target="_blank">doi:10.1016/j.brs.2024.06.001</a></li>
<li>Biabani, M., et al. (2024). Characterising the contribution of auditory and somatosensory inputs to TMS-evoked potentials following stimulation of prefrontal, premotor, and parietal cortex. <a href="https://doi.org/10.1162/imag_a_00349" target="_blank">doi:10.1162/imag_a_00349</a></li>
<li>Breyton, M., et al. (2025). Spatiotemporal brain complexity quantifies consciousness outside of perturbation paradigms. <a href="https://doi.org/10.7554/eLife.98920" target="_blank">doi:10.7554/eLife.98920</a></li>
<li>Rohaut, B., et al. (2024). Multimodal imaging reveals partially preserved semantic cognition in comatose patients after cardiac arrest. <a href="https://doi.org/10.1212/WNL.0000000000209439" target="_blank">doi:10.1212/WNL.0000000000209439</a></li>
<li>Kawai, R., et al. (2025). Multimodal assessment improves neuroprognosis performance after out-of-hospital cardiac arrest. <a href="https://doi.org/10.1038/s41591-024-03019-1" target="_blank">doi:10.1038/s41591-024-03019-1</a></li>
<li>Yao, Z., et al. (2023). A high-resolution transcriptomic and spatial atlas of cell types in the whole mouse brain. <a href="https://doi.org/10.1038/s41586-023-06812-z" target="_blank">doi:10.1038/s41586-023-06812-z</a></li>
<li>Dorkenwald, S., et al. (2024). Neuronal wiring diagram of an adult brain. <a href="https://doi.org/10.1038/s41586-024-07558-y" target="_blank">doi:10.1038/s41586-024-07558-y</a></li>
<li>Lappalainen, J. K., Tschopp, F. D., Prakhya, S., et al. (2024). Connectome-constrained networks predict neural activity across the fly visual system. <a href="https://doi.org/10.1038/s41586-024-07939-3" target="_blank">doi:10.1038/s41586-024-07939-3</a></li>
<li>MICrONS Consortium, et al. (2025). Functional connectomics spanning multiple areas of mouse visual cortex. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">doi:10.1038/s41586-025-08790-w</a></li>
<li>Gamlin, C. R., et al. (2025). Connectomics of predicted Sst transcriptomic types in mouse visual cortex. <a href="https://doi.org/10.1038/s41586-025-08805-6" target="_blank">doi:10.1038/s41586-025-08805-6</a></li>
<li>Beiran, M., &amp; Litwin-Kumar, A. (2025). Prediction of neural activity in connectome-constrained recurrent networks. <a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">doi:10.1038/s41593-025-02080-4</a></li>
<li>Hengen, K. B., Torrado Pacheco, A., McGregor, J. N., Van Hooser, S. D., &amp; Turrigiano, G. G. (2016). Neuronal firing rate homeostasis is inhibited by sleep and promoted by wake. <a href="https://doi.org/10.1016/j.cell.2016.01.046" target="_blank">doi:10.1016/j.cell.2016.01.046</a></li>
<li>Torrado Pacheco, A., et al. (2021). Sleep Promotes Downward Firing Rate Homeostasis. <a href="https://doi.org/10.1016/j.neuron.2021.04.004" target="_blank">doi:10.1016/j.neuron.2021.04.004</a></li>
<li>Looser, Z. J., et al. (2024). Oligodendrocyte-axon metabolic coupling is mediated by extracellular K<sup>+</sup> and maintains axonal health. <a href="https://doi.org/10.1038/s41593-023-01558-3" target="_blank">doi:10.1038/s41593-023-01558-3</a></li>
<li>Reimer, J., McGinley, M. J., Liu, Y., et al. (2016). Pupil fluctuations track rapid changes in adrenergic and cholinergic activity in cortex. <a href="https://doi.org/10.1038/ncomms13289" target="_blank">doi:10.1038/ncomms13289</a></li>
<li>Lohani, S., Moberly, A. H., Benisty, H., et al. (2022). Spatiotemporally heterogeneous coordination of cholinergic and neocortical activity. <a href="https://doi.org/10.1038/s41593-022-01202-6" target="_blank">doi:10.1038/s41593-022-01202-6</a></li>
<li>Collins, L., Reddy, C. B., Neal, S., et al. (2023). Cholinergic and noradrenergic axonal activity contains a behavioral-state signal that is coordinated across the dorsal cortex. <a href="https://doi.org/10.7554/eLife.86800.2" target="_blank">doi:10.7554/eLife.86800.2</a></li>
<li>Neyhart, E., Zhou, N., Munn, B. R., et al. (2024). Cortical acetylcholine dynamics are predicted by cholinergic axon activity and behavioral state. <a href="https://doi.org/10.1016/j.celrep.2024.114808" target="_blank">doi:10.1016/j.celrep.2024.114808</a></li>
<li>Hansen, J. Y., Shafiei, G., Markello, R. D., et al. (2022). Mapping neurotransmitter systems to the structural and functional organization of the human neocortex. <a href="https://doi.org/10.1038/s41593-022-01186-3" target="_blank">doi:10.1038/s41593-022-01186-3</a></li>
<li>Verhoog, M. B., Goriounova, N. A., Obermayer, J., et al. (2016). Mechanisms underlying the rules for associative plasticity at adult human neocortical synapses. <a href="https://doi.org/10.1038/ncomms12826" target="_blank">doi:10.1038/ncomms12826</a></li>
<li>Cahill, M. K., et al. (2024). Network-level encoding of local neurotransmitters in cortical astrocytes. <a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">doi:10.1038/s41586-024-07311-5</a></li>
<li>Williamson, N. R., et al. (2025). Learning-associated astrocyte ensembles regulate memory recall. <a href="https://doi.org/10.1038/s41586-024-08170-w" target="_blank">doi:10.1038/s41586-024-08170-w</a></li>
<li>Dewa, K., et al. (2025). The astrocytic ensemble acts as a multiday trace to stabilize memory. <a href="https://doi.org/10.1038/s41586-025-09619-2" target="_blank">doi:10.1038/s41586-025-09619-2</a></li>
<li>Bukalo, O., et al. (2026). Astrocytes enable amygdala neural representations supporting memory. <a href="https://doi.org/10.1038/s41586-025-10068-0" target="_blank">doi:10.1038/s41586-025-10068-0</a></li>
<li>Vadisiute, A., Meijer, E., Therpurakal, R. N., et al. (2024). Glial cells undergo rapid changes following acute chemogenetic manipulation of cortical layer 5 projection neurons. <a href="https://doi.org/10.1038/s42003-024-06994-w" target="_blank">doi:10.1038/s42003-024-06994-w</a></li>
<li>Hadzibegovic, N., et al. (2026). Early intrinsic excitability plasticity of neocortical engram neurons defines memory formation and precision. <a href="https://doi.org/10.1038/s41467-025-66975-3" target="_blank">doi:10.1038/s41467-025-66975-3</a></li>
<li>Ovadia, Y., Fertig, E., Ren, J., Nado, Z., Sculley, D., Nowozin, S., Dillon, J. V., Lakshminarayanan, B., &amp; Snoek, J. (2019). Can You Trust Your Model's Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift. <a href="https://papers.nips.cc/paper_files/paper/2019/hash/8558cb408c1d76621371888657d2eb1d-Abstract.html" target="_blank">NeurIPS 2019</a></li>
<li>Han, J., Huang, Y., &amp; Wang, Y. (2024). Model Assessment and Selection under Temporal Distribution Shift. <a href="https://proceedings.mlr.press/v235/han24d.html" target="_blank">PMLR 235</a></li>
<li>Shafiezadeh, S., Mento, G., &amp; Testolin, A. (2023). Methodological Issues in Evaluating Machine Learning Models for Patient-Independent Epileptic Seizure Prediction. <a href="https://doi.org/10.3390/math11071650" target="_blank">doi:10.3390/math11071650</a></li>
<li>Shafiezadeh, S., Duma, G. M., Mento, G., Danieli, A., Antoniazzi, L., Del Popolo Cristaldi, F., Bonanni, P., &amp; Testolin, A. (2024). Calibrating Deep Learning Classifiers for Patient-Independent Electroencephalogram Seizure Forecasting. <a href="https://doi.org/10.3390/s24092863" target="_blank">doi:10.3390/s24092863</a></li>
<li>Lei, J., G'Sell, M., Rinaldo, A., Tibshirani, R. J., &amp; Wasserman, L. (2018). Distribution-Free Predictive Inference for Regression. <a href="https://doi.org/10.1080/01621459.2017.1307116" target="_blank">doi:10.1080/01621459.2017.1307116</a></li>
<li>Chernozhukov, V., Wüthrich, K., &amp; Zhu, Y. (2021). Distributional conformal prediction. <a href="https://doi.org/10.1073/pnas.2107794118" target="_blank">doi:10.1073/pnas.2107794118</a></li>
<li>Segal, G., Keidar, N., Lotan, R. M., Romano, Y., Herskovitz, M., &amp; Yaniv, Y. (2023). Utilizing risk-controlling prediction calibration to reduce false alarm rates in epileptic seizure prediction. <a href="https://doi.org/10.3389/fnins.2023.1184990" target="_blank">doi:10.3389/fnins.2023.1184990</a></li>
<li>Eliades, G., &amp; Papadopoulos, H. (2019). Applying conformal prediction to control an exoskeleton. <a href="https://proceedings.mlr.press/v105/eliades19a.html" target="_blank">PMLR 105</a></li>
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
