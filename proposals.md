---
layout: default
title: "技術提案（統合本文）"
description: "Issue #46/#47/#48/#56/#58/#61/#62/#64–#70/#257–#260 に対応する Technical Proposal を1ページ本文に統合した根拠付きサマリー。"
article_type: Index
subtitle: "Issue対応・実装方針・根拠リンクを1ページで追跡"
author: Mind Uploading Research Project
last_updated: "2026-03-06"
note: "Integrated Compendium"
audience: "Issue対応の根拠を追いたい人、提案の状態と実装影響をまとめて確認したい人"
reading_time: "15〜25分"
page_intro: "このページは、Technical Proposal をバラバラのIssueのままではなく、1本の本文として追えるようにまとめたページです。『何が提案で、何が反映済みで、何がまだ根拠確認中か』を見失わないようにするための索引兼本文として使います。"
accuracy_note: "ここは統合サマリーです。採否や妥当性は、必ず原文節と Issue 履歴へ戻って確認してください。"
page_highlights:
  - "提案ごとの状態、主眼、根拠節を同じ表で追えます。"
  - "一覧だけでなく本文もまとめているため、背景を切り落とさず確認できます。"
  - "『提案済み』『実装方針反映』『外部依存』を混ぜない読み方を前提にしています。"
known_points:
  - "このページは、提案の状態、主眼、根拠節を1か所で追うための統合サマリーです。"
  - "提案受理や文書反映は、コード実装や外部合意の完了を自動的には意味しません。"
  - "要約だけで判断せず、原文節や Issue 履歴へ戻る前提で使うのが正しい読み方です。"
unknown_points:
  - "どの提案が今後どこまで実装や共同研究へ進むかは、まだ固定していません。"
  - "外部依存が残る提案は、相手先や条件次第で進み方が変わります。"
wiki_links:
  - label: "Wiki: 提案と状態ラベルの読み方"
    url: "/wiki/proposal-status-reading.html"
    description: "『提案』『受理』『反映済み』の違いを初歩から整理します。"
  - label: "Wiki: ロードマップの読み方"
    url: "/wiki/roadmap-reading-guide.html"
    description: "各ストリームが技術ロードマップのどこに対応するかを見失いにくくします。"
  - label: "Wiki: 検証基盤の基本"
    url: "/wiki/verification-basics.html"
    description: "達成条件や反証条件を先に置く理由を補います。"
  - label: "Wiki: 熱力学的接地の基本"
    url: "/wiki/thermodynamic-grounding-basics.html"
    description: "Stream D で出る Landauer、散逸、NESS、EPR の入口を補います。"
recommended_pages:
  - label: "貢献ガイド"
    url: "/issue.html"
  - label: "検証基盤"
    url: "/verification.html"
  - label: "技術ロードマップ"
    url: "/tech_roadmap.html"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Purpose</h2>
<p>
このページは、Technical Proposal 群（Issue #46/#47/#48/#56/#58/#61/#62/#257–#260）を「一覧」ではなく<strong>本文として統合</strong>したページです。
各提案の主張、対応状況、実装影響、根拠節へのリンクを1か所にまとめ、検証と更新を容易にします。
</p>
</div>

<div class="note-box">
<strong>このページで言えること／言えないこと</strong>
<p>
ここで言えるのは「どの提案が何を目指し、どの根拠に支えられているか」です。一方で、ここだけ読んで提案の妥当性が最終確定したとは言えません。判断が必要な場合は、必ず原文節と Issue のやり取りまで戻ってください。
</p>
</div>
<div class="note-box">
<strong>要約・原文・Issue 履歴のどこまで見ればよいか迷ったとき</strong>
<p>
このページは統合サマリーなので、全体像をつかむ入口としては有効ですが、採否判断や修正提案には原文節と Issue 履歴まで戻る必要があります。使い分けを 1 枚で見たい場合は <a href="wiki/summary-vs-source-reading.html">Wiki: 要約・原文・Issue履歴の使い分け</a> をご覧ください。
</p>
</div>

<div class="note-box">
<strong>状態ラベルで迷ったとき</strong>
<p>
このページは「提案の整理表」なので、状態ラベルの意味を読み違えると全体を誤読しやすくなります。まずラベルの意味を噛み砕いて押さえたい場合は、<a href="wiki/proposal-status-reading.html">Wiki: 提案と状態ラベルの読み方</a> を先に見ると安全です。
</p>
</div>
<div class="note-box">
<strong>実務系ページの中での位置づけを知りたいとき</strong>
<p>
このページは、提案群の状態と根拠を整理する本文です。勝利条件の設計は <a href="verification.html">検証基盤</a>、入口データは <a href="datasets.html">データ&ベンチ</a>、実作業の手順は <a href="hands_on.html">ハンズオン</a>、他分野から借りる型は <a href="casework.html">ケースワーク</a> が担当します。実務系ページだけの読み分けを 1 枚で見たい場合は <a href="wiki/practical-pages-reading-guide.html">Wiki: 実務系ページの読み分けガイド</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>研究ノート、理論フレーム、提案、Issue の違いで迷ったとき</strong>
<p>
このページは提案と状態の整理表であり、観察ノートや今すぐ実行するタスクとは役割が違います。事実・仮説・提案・実行タスクの違いをまとめて見たい場合は <a href="wiki/facts-hypotheses-proposals-and-tasks.html">Wiki: 事実・仮説・提案・実行タスクの違い</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>提案から Issue や外部依存へどう流すか見たいとき</strong>
<p>
読んだ内容や提案を、どの段階で Issue、Hands-on、Collaborations へ戻すかを一本道で見たい場合は <a href="wiki/reading-to-change-workflow.html">Wiki: 読んだ内容を変更へつなぐ流れ</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>Stream D の熱力学語で止まったとき</strong>
<p>
Landauer、散逸、NESS、EPR は、このページでは提案の論点として短く出てきます。まず入口だけ初歩から整理したい場合は <a href="wiki/thermodynamic-grounding-basics.html">Wiki: 熱力学的接地の基本</a> を先にご覧ください。
</p>
</div>

<section class="section" id="reading-guide">
<h2 class="section-title">読み方（根拠ベース）</h2>
<div class="key-points">
<h4>Rule</h4>
<ul>
<li><strong>要約だけで判断しない：</strong> 各項目の「根拠」リンクから原文節に戻って確認してください。</li>
<li><strong>主張レベルを分離：</strong> 「提案」「実装済み」「外部依存」を混同せずに読む運用にしています。</li>
<li><strong>更新点を追う：</strong> `last_updated` が新しい順に、変更理由を `issue.html` でも確認できます。</li>
</ul>
</div>

<div class="note-box">
<strong>迷ったときの最短手順</strong>
<p>
まず下のマトリクスで <strong>Issue番号</strong> と <strong>状態</strong> を確認し、次に自分に関係する技術ストリームだけを読み、最後に必要なときだけ原本へ戻ってください。最初から全文を追うより、「どの話か」を先に固定した方が読みやすくなります。
</p>
</div>

<table class="data-table">
<thead>
<tr>
<th>読みたいこと</th>
<th>先に見る場所</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>どの Issue が何を扱うか知りたい</strong></td>
<td>「Issue対応マトリクス（統合版）」を先に見ます。</td>
</tr>
<tr>
<td><strong>中身の要点だけ知りたい</strong></td>
<td>「統合本文（技術ストリーム別）」から該当ストリームへ進みます。</td>
</tr>
<tr>
<td><strong>本当にそう書いてあるか確認したい</strong></td>
<td>「原本（全文）インデックス」から各 technical proposal の原文節へ戻ります。</td>
</tr>
</tbody>
</table>

<table class="data-table">
<thead>
<tr>
<th>自分の立場</th>
<th>先に見る場所</th>
<th>そこで見たいこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>実装したい人</strong></td>
<td>「統合本文（技術ストリーム別）」</td>
<td>どのストリームが入力、前処理、因果検証、熱力学に対応するかを見ます。</td>
</tr>
<tr>
<td><strong>レビューしたい人</strong></td>
<td>「Issue対応マトリクス（統合版）」と「状態ラベルの意味」</td>
<td>提案段階なのか、方針反映済みなのかを切り分けて確認します。</td>
</tr>
<tr>
<td><strong>根拠の真偽を確かめたい人</strong></td>
<td>「原本（全文）インデックス」</td>
<td>要約を経由せず、元の proposal 節へ戻って文脈を確認します。</td>
</tr>
<tr>
<td><strong>いま何が未実装か知りたい人</strong></td>
<td><a href="issue.html">issue.html</a> と合わせて読む</td>
<td>文書反映と、コード・実験・外部依存の差を見分けます。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="status-meaning">
<h2 class="section-title">状態ラベルの意味</h2>
<table class="data-table">
<thead>
<tr>
<th>ラベル</th>
<th>意味</th>
<th>まだ残る確認</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>提案公開</strong></td>
<td>本文として公開され、議論にかけられる状態です。</td>
<td>妥当性や優先順位の精査が残ります。</td>
</tr>
<tr>
<td><strong>提案受理</strong></td>
<td>方針として取り込む価値が高いと判断した状態です。</td>
<td>実装方法や検証条件の具体化が必要です。</td>
</tr>
<tr>
<td><strong>実装方針反映</strong></td>
<td>サイト本文や設計へ考え方が反映された状態です。</td>
<td>コードや運用の実装が完了したとは限りません。</td>
</tr>
<tr>
<td><strong>外部依存</strong></td>
<td>実験・機材・審査など、リポジトリ外の条件が必要な状態です。</td>
<td>ここでは要求仕様やログ形式までを先に整えます。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="issue-matrix">
<h2 class="section-title">Issue対応マトリクス（統合版）</h2>
<table class="data-table">
<thead>
<tr>
<th>Issue</th>
<th>状態</th>
<th>主眼</th>
<th>根拠（原文節）</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>#46</strong></td>
<td>提案公開</td>
<td>計測QA・同期・モーション除去・BIDS/Motion-BIDS</td>
<td><a href="technical_proposal_46.html#qa">#qa</a> / <a href="technical_proposal_46.html#sync">#sync</a> / <a href="technical_proposal_46.html#bids">#bids</a></td>
</tr>
<tr>
<td><strong>#47</strong></td>
<td>提案受理</td>
<td>BIDS標準化、ASR/ZapLine、wPLI/STE、LSL同期</td>
<td><a href="technical_proposal_47.html#bids">#bids</a> / <a href="technical_proposal_47.html#preprocessing">#preprocessing</a> / <a href="technical_proposal_47.html#connectivity">#connectivity</a> / <a href="technical_proposal_47.html#multimodal">#multimodal</a></td>
</tr>
<tr>
<td><strong>#48</strong></td>
<td>審査中提案</td>
<td>OPM-MEG、転移学習、Team Flow因果、IIT実装拡張</td>
<td><a href="technical_proposal_48.html#measurement">#measurement</a> / <a href="technical_proposal_48.html#teamflow">#teamflow</a> / <a href="technical_proposal_48.html#iit-implementation">#iit-implementation</a></td>
</tr>
<tr>
<td><strong>#56</strong></td>
<td>提案公開</td>
<td>反実仮想の識別不能性に対する介入設計（PCI + do演算）</td>
<td><a href="technical_proposal_56.html#problem-statement">#problem-statement</a> / <a href="technical_proposal_56.html#proposal">#proposal</a></td>
</tr>
<tr>
<td><strong>#58</strong></td>
<td>提案公開</td>
<td>NESS散逸・反実仮想識別可能性・IIT近似計算</td>
<td><a href="technical_proposal_58.html#thermo">#thermo</a> / <a href="technical_proposal_58.html#counterfactual">#counterfactual</a> / <a href="technical_proposal_58.html#iit">#iit</a></td>
</tr>
<tr>
<td><strong>#61</strong></td>
<td>実装方針反映（提案文書）</td>
<td>Unfolding論点、熱力学コスト2層化、SCM厳密化、多モデル推論</td>
<td><a href="technical_proposal_61.html#causal-structure">#causal-structure</a> / <a href="technical_proposal_61.html#thermodynamics">#thermodynamics</a> / <a href="technical_proposal_61.html#scm-identifiability">#scm-identifiability</a> / <a href="technical_proposal_61.html#multi-model-inference">#multi-model-inference</a></td>
</tr>
<tr>
<td><strong>#62</strong></td>
<td>#58応答として実装計画化</td>
<td>NESS・同値類警告・IIT近似（ヒューリスティクス）</td>
<td><a href="technical_proposal_62.html#thermodynamics">#thermodynamics</a> / <a href="technical_proposal_62.html#identifiability">#identifiability</a> / <a href="technical_proposal_62.html#complexity">#complexity</a></td>
</tr>
<tr>
<td><strong>#257</strong></td>
<td>提案受理（本文追記）</td>
<td>HBMでの導電率同時推定・因果同値類の明示・NESS要件の実装化</td>
<td><a href="#stream-e-rigor">#stream-e-rigor</a> / <a href="verification.html#verification-rigor-2026-02">verification</a></td>
</tr>
<tr>
<td><strong>#258</strong></td>
<td>提案受理（本文追記）</td>
<td>IIT計算量制約の実務化（PCI-ST中心）と熱力学KPIの強化</td>
<td><a href="#stream-e-rigor">#stream-e-rigor</a> / <a href="verification.html#thermodynamic-verification">thermodynamic-verification</a></td>
</tr>
<tr>
<td><strong>#259</strong></td>
<td>提案受理（本文追記）</td>
<td>ASR前後の忠実度監査、BIDSセマンティック拡張（CogPO/NIF）を要件化</td>
<td><a href="#stream-e-rigor">#stream-e-rigor</a> / <a href="verification.html#verification-rigor-2026-02">verification</a></td>
</tr>
<tr>
<td><strong>#260</strong></td>
<td>提案受理（本文追記）</td>
<td>逆問題不確実性伝播・因果識別限界・熱力学整合性を統合追記</td>
<td><a href="#stream-e-rigor">#stream-e-rigor</a> / <a href="verification.html#causal-perturbation-suite">causal-perturbation-suite</a></td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="integrated-streams">
<h2 class="section-title">統合本文（技術ストリーム別）</h2>

<table class="data-table">
<thead>
<tr>
<th>ストリーム</th>
<th>ひとことで言うと</th>
<th>こんなときに読む</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>A</strong></td>
<td>まず計測をきれいにそろえる話です。</td>
<td>ノイズ、同期ずれ、BIDS など「入力の土台」が気になるときに読みます。</td>
</tr>
<tr>
<td><strong>B</strong></td>
<td>前処理と接続性解析を、比較可能な形にそろえる話です。</td>
<td>ASR、ZapLine、wPLI など、解析パイプラインの妥当性を見たいときに読みます。</td>
</tr>
<tr>
<td><strong>C</strong></td>
<td>観測が似ているだけでなく、介入への反応まで比べる話です。</td>
<td>WBE の同一性や因果検証が、どこまで言えるかを確認したいときに読みます。</td>
</tr>
<tr>
<td><strong>D</strong></td>
<td>計算量と熱力学の制約を、都合よく省略しないための話です。</td>
<td>「理論上できそう」だけでなく、実装コストや散逸まで含めて見たいときに読みます。</td>
</tr>
<tr>
<td><strong>E</strong></td>
<td>見落としやすい厳密化ポイントを、上位ルールとして締め直す話です。</td>
<td>逆問題不確実性、因果同値類、BIDS セマンティクス不足などの抜け漏れを確認したいときに読みます。</td>
</tr>
</tbody>
</table>

<div class="stage-list">
<div class="stage-item">
<div class="stage-number">A</div>
<div class="stage-body">
<h4>計測品質・同期・標準化ストリーム</h4>
<p>
計測品質の定量化・同期誤差（遅延/ジッタ/ドリフト）補正・BIDS準拠を再現可能性の最低条件として固定し、Issue #46/#47 共通の計測品質・同期・標準化ストリームとして扱います。
</p>
<div class="tag-list">
<span class="tag">QA</span><span class="tag">LSL</span><span class="tag">BIDS</span><span class="tag">Motion-BIDS</span>
</div>
<p><strong>根拠:</strong> <a href="technical_proposal_46.html#qa">#46: 計測QA</a> / <a href="technical_proposal_46.html#sync">#46: 同期補正</a> / <a href="technical_proposal_47.html#bids">#47: BIDS標準化</a></p>
</div>
</div>

<div class="stage-item">
<div class="stage-number">B</div>
<div class="stage-body">
<h4>信号前処理・接続性解析ストリーム</h4>
<p>
ASR/ZapLine 系の適応的デノイジングと、体積伝導に頑健な接続性指標（wPLI/STE）を組み合わせ、比較可能な解析パイプラインを構成します。
</p>
<div class="tag-list">
<span class="tag">ASR</span><span class="tag">ZapLine-plus</span><span class="tag">wPLI</span><span class="tag">STE</span>
</div>
<p><strong>根拠:</strong> <a href="technical_proposal_47.html#preprocessing">#47: 前処理</a> / <a href="technical_proposal_47.html#connectivity">#47: 接続性</a></p>
<p>
<strong>適応的前処理の拡張要件（Issue #64–#70）：</strong>
ASR のパラメータ選択においては、静的閾値ではなく Riemannian geometry に基づく外れ値検出（Riemannian Potato; Barachant et al., 2013）を採用し、共分散行列のリーマン距離を用いたデータ駆動型の適応閾値を標準とします。
周波数追従型デノイジングには ZapLine-plus（Klug &amp; Kloosterman, 2022）を標準パイプラインに組み込み、線スペクトルノイズの自動検出・除去を行います。
また、ICA/ASR 等で除去されたコンポーネントのトポグラフィは、再現性・監査可能性の観点から BIDS 監査ログ（derivatives 内 audit/ ディレクトリ）に必ず記録する運用とします。
</p>
<p>
<strong>信号忠実度の追加要件（Issue #259）：</strong>
ASR 適用前後で、相互情報量（Mutual Information）および位相同期指標（PLV/wPLI）の保存率を監査指標として記録します。
さらに、ASR 単独での除去性能に偏らないよう、深層学習ベースのBSS（ICA-U-Net 等）を比較対象に含め、タスク別に副作用（高周波成分の過抑制）を評価します。
</p>
</div>
</div>

<div class="stage-item">
<div class="stage-number">C</div>
<div class="stage-body">
<h4>WBE同一性検証（因果介入）ストリーム</h4>
<p>
Issue #56/#58/#61/#62 の統合論点です。観測一致だけでなく、介入に対する分岐構造一致を検証し、識別可能性の限界を明示します。
</p>
<div class="tag-list">
<span class="tag">Counterfactual</span><span class="tag">do-calculus</span><span class="tag">SCM</span><span class="tag">Identifiability</span>
</div>
<p><strong>根拠:</strong> <a href="technical_proposal_56.html#proposal">#56: 介入提案</a> / <a href="technical_proposal_58.html#counterfactual">#58: 識別可能性</a> / <a href="technical_proposal_61.html#scm-identifiability">#61: 厳密化</a> / <a href="technical_proposal_62.html#identifiability">#62: 同値類警告</a></p>
<p>
<strong>定量的因果メトリクスの導入（Issue #64–#70）：</strong>
WBE 同一性検証の形式要件として、Effective Information（EI）および Causal Density を定量的検証指標に採用します。EI はシステムの因果的影響力を情報量として測定し、Causal Density は接続パターン全体の因果的豊かさを評価します。
DCM モデル空間の効率的探索には Bayesian Model Reduction（BMR; Frässle et al., 2021）を適用し、フルモデルの事後分布から縮約モデル群のエビデンスを解析的に近似することで、計算コストを大幅に低減します。
さらに、接続性推定値が安定した個人特性であることを確認するため Causal Fingerprinting（テスト−リテスト間の因果的接続プロファイルの個人識別精度）を検証基準に組み込みます。
</p>
</div>
</div>

<div class="stage-item">
<div class="stage-number">D</div>
<div class="stage-body">
<h4>熱力学・計算量制約ストリーム</h4>
<p>
「論理コストだけで十分」という誤解を避け、非平衡散逸（NESS）と IIT 近似計算の制約を実装要件として分離します。
</p>
<div class="tag-list">
<span class="tag">NESS</span><span class="tag">EPR</span><span class="tag">Metabolic Flux</span><span class="tag">IIT Approximation</span>
</div>
<p><strong>根拠:</strong> <a href="technical_proposal_58.html#thermo">#58: 散逸制約</a> / <a href="technical_proposal_61.html#thermodynamics">#61: 2層コスト</a> / <a href="technical_proposal_62.html#complexity">#62: 計算量対応</a></p>
</div>
</div>

<div class="stage-item">
<div class="stage-number">E</div>
<div class="stage-body">
<h4 id="stream-e-rigor">2026年2月 追加厳密化ストリーム（Issue #257–#260）</h4>
<p>
Issue #257–#260 で提示された技術批判を、既存ストリームの上位制約として統合します。ここでは「提案の追加」ではなく、公開済み要件の判定条件を厳密化し、検証時に欠落しやすい論点を明示します。
</p>
<ul>
<li><strong>逆問題不確実性：</strong>導電率・ノイズ・逆問題不良設定性を分離し、HBMでの同時推定結果とモンテカルロ感度分析を提出必須にします。</li>
<li><strong>因果同値類の警告：</strong>観測一致のみでは同一性を主張しない運用とし、推定モデルが同値類の一要素であることを明記します。</li>
<li><strong>介入設計の実務化：</strong>PCI-STの単独報告ではなく、局所摂動（TMS/tDCS相当）に対する因果応答不一致の検出を評価契約に組み込みます。</li>
<li><strong>熱力学制約：</strong>論理コスト（FLOPs）と散逸コスト（EPR）を分離し、通信対計算のエネルギー比をKPIとして記録します。</li>
<li><strong>BIDSセマンティック拡張：</strong>CogPO/NIF と主観報告メタデータ（ESM等）を併用し、実験文脈の欠落を防ぎます。</li>
</ul>
<p><strong>根拠:</strong> <a href="verification.html#verification-rigor-2026-02">検証要件（#257–#260）</a> / <a href="verification.html#causal-perturbation-suite">因果的摂動スイート</a> / <a href="verification.html#thermodynamic-verification">熱力学的検証要件</a></p>
</div>
</div>
</div>
</section>

<section class="section" id="full-index">
<h2 class="section-title">原本（全文）インデックス</h2>
<table class="data-table">
<thead>
<tr>
<th>提案</th>
<th>Issue</th>
<th>更新日</th>
<th>リンク</th>
</tr>
</thead>
<tbody>
<tr><td>計測品質・同期・BIDS統合強化</td><td>#46</td><td>2026-02-01</td><td><a href="technical_proposal_46.html">Open</a></td></tr>
<tr><td>標準化と計算論的拡張</td><td>#47</td><td>2026-01-25</td><td><a href="technical_proposal_47.html">Open</a></td></tr>
<tr><td>神経工学的・計算論的枠組み拡張</td><td>#48</td><td>2026-01-25</td><td><a href="technical_proposal_48.html">Open</a></td></tr>
<tr><td>識別可能性と因果介入</td><td>#56</td><td>2026-01-30</td><td><a href="technical_proposal_56.html">Open</a></td></tr>
<tr><td>熱力学・因果整合性</td><td>#58</td><td>2026-02-01</td><td><a href="technical_proposal_58.html">Open</a></td></tr>
<tr><td>因果モデリング論理ギャップ対応</td><td>#61</td><td>2026-02-01</td><td><a href="technical_proposal_61.html">Open</a></td></tr>
<tr><td>#58批判への補強提案</td><td>#62（#58応答）</td><td>2026-02-01</td><td><a href="technical_proposal_62.html">Open</a></td></tr>
</tbody>
</table>

<div class="cta-box">
<h4>Issue対応の確認</h4>
<p>Issueごとの対応状況は `issue.html` に集約しています。</p>
<a href="issue.html">Issue対応ページを見る →</a>
</div>
</section>

<section class="section" id="evidence-gaps">
<h2 class="section-title">エビデンスギャップ（未解決課題）</h2>
<p>
各提案ストリームについて、文献的裏付けが不足している領域を明示します。
</p>
<div class="key-points">
<h4>Stream A: 計測品質</h4>
<ul>
<li><strong>ASR のパラメータ選択根拠：</strong>ASR（Artifact Subspace Reconstruction）の閾値設定は経験的であり、WBE用途での最適パラメータの理論的根拠は未確立。</li>
<li><strong>OPM-MEGとの統合：</strong>OPM-MEG（Optically Pumped Magnetometer）は動き耐性を改善するが、EEGとのマルチモーダル統合プロトコルは標準化されていない（Boto et al., 2018）。</li>
</ul>
</div>
<div class="key-points">
<h4>Stream C: WBE同一性検証</h4>
<ul>
<li><strong>do-calculusの実装可能性：</strong>Pearl のdo-calculusは理論的に強力だが、神経データに対する観測変数の選択と介入変数の特定が実験設計上の最大のボトルネック。</li>
<li><strong>SCMのサイクル問題：</strong>脳の再帰的接続ではDAG仮定が成り立たず、cyclic SCM（動的因果モデルとの接続）の理論的整備が必要。</li>
</ul>
</div>
<div class="key-points">
<h4>Stream D: 熱力学</h4>
<ul>
<li><strong>NESS測定の実現性：</strong>非平衡定常状態のエントロピー生成速度を神経系で直接測定する手法は確立されていない。代理指標（代謝率、ATP消費量等）との対応関係の検証が必要。</li>
</ul>
</div>
</section>

<section class="section" id="references">
<h2 class="section-title">参考文献（横断）</h2>
<ol>
<li>Chang, C.-Y., et al. (2018). ASR evaluation. <a href="https://doi.org/10.1109/EMBC.2018.8512547" target="_blank">doi:10.1109/EMBC.2018.8512547</a></li>
<li>de Cheveigne, A. (2020). ZapLine. <a href="https://doi.org/10.1016/j.neuroimage.2019.116356" target="_blank">doi:10.1016/j.neuroimage.2019.116356</a></li>
<li>Vinck, M., et al. (2011). wPLI. <a href="https://doi.org/10.1016/j.neuroimage.2011.01.055" target="_blank">doi:10.1016/j.neuroimage.2011.01.055</a></li>
<li>Staniek, M., &amp; Lehnertz, K. (2008). Symbolic Transfer Entropy. <a href="https://doi.org/10.1103/PhysRevLett.100.158101" target="_blank">doi:10.1103/PhysRevLett.100.158101</a></li>
<li>Correa, J. D., Lee, S., &amp; Bareinboim, E. (2021). Nested Counterfactual Identification. <a href="https://arxiv.org/abs/2107.03190" target="_blank">arXiv:2107.03190</a></li>
<li>Seifert, U. (2012). Stochastic thermodynamics. <a href="https://doi.org/10.1088/0034-4885/75/12/126001" target="_blank">doi:10.1088/0034-4885/75/12/126001</a></li>
<li>Kitazono, J., Kanai, R., &amp; Oizumi, M. (2018). Efficient MIP search in IIT. <a href="https://doi.org/10.3390/e20030173" target="_blank">doi:10.3390/e20030173</a></li>
<li>Kothe, C., et al. (2025). Lab Streaming Layer. <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">doi:10.1162/IMAG.a.136</a></li>
<li>Boto, E., et al. (2018). Moving magnetoencephalography towards real-world applications with wearable OPM-MEG. <a href="https://doi.org/10.1038/nature26147" target="_blank">doi:10.1038/nature26147</a></li>
<li>Pearl, J. (2009). <em>Causality: Models, Reasoning, and Inference</em> (2nd ed.). Cambridge University Press.</li>
<li>Friston, K. J., Harrison, L., &amp; Penny, W. (2003). Dynamic causal modelling. <a href="https://doi.org/10.1016/S1053-8119(03)00202-7" target="_blank">doi:10.1016/S1053-8119(03)00202-7</a></li>
<li>Barachant, A., et al. (2013). Classification of covariance matrices using a Riemannian-based kernel for BCI applications. <a href="https://doi.org/10.1016/j.neucom.2013.04.027" target="_blank">doi:10.1016/j.neucom.2013.04.027</a></li>
<li>Klug, M. &amp; Kloosterman, N. A. (2022). ZapLine-plus: A flexible and accurate removal of line noise. <a href="https://doi.org/10.1016/j.neuroimage.2022.119265" target="_blank">doi:10.1016/j.neuroimage.2022.119265</a></li>
<li>Frässle, S., et al. (2021). Regression DCMs for group studies. <a href="https://doi.org/10.1016/j.neuroimage.2020.117566" target="_blank">doi:10.1016/j.neuroimage.2020.117566</a></li>
<li>Mullen, T. R., et al. (2015). Real-time neuroimaging and cognitive monitoring using wearable EEG. <a href="https://doi.org/10.1109/TBME.2015.2437932" target="_blank">doi:10.1109/TBME.2015.2437932</a></li>
<li>Turner, B. O., et al. (2016). The Cognitive Paradigm Ontology (CogPO). <a href="https://doi.org/10.1007/s12021-016-9297-2" target="_blank">doi:10.1007/s12021-016-9297-2</a></li>
<li>Bug, W. J., et al. (2008). The Neuroscience Information Framework (NIF). <a href="https://doi.org/10.1007/s12021-008-9006-y" target="_blank">doi:10.1007/s12021-008-9006-y</a></li>
</ol>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>Related</h4>
<ul>
<li><a href="verification.html">検証基盤（Verification）→</a></li>
<li><a href="tech_roadmap.html">技術ロードマップ（学習）→</a></li>
<li><a href="issue.html">Issue対応状況（集約）→</a></li>
<li><a href="index.html">Start（トップ）→</a></li>
</ul>
</div>

<div class="note-box">
<strong>Rule of Thumb</strong>
<p>
提案は「主張」ではなく、<strong>検証条件</strong>・<strong>反証条件</strong>・<strong>根拠リンク</strong>の3点セットで管理します。
</p>
</div>

</aside>
</main>
