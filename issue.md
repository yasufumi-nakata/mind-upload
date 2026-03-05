---
layout: default
title: "貢献ガイド"
description: "Mind-Uploadプロジェクトへの参加方法と、Issue対応状況（根拠リンク付き）"
article_type: Guide
subtitle: "Join the Research Community + Issue Tracker"
author: Mind Uploading Research Project
last_updated: "2026-03-06"
note: "Contribution + Issue tracker"
audience: "初めて参加する人、Issueの状態を確認したい人、実行可能な貢献から入りたい人"
reading_time: "10〜20分"
page_intro: "このページは、Mind-Uploadにどう参加できるかを、Issue運用と対応状況ごとに整理した入口です。専門家だけの場所ではなく、『どの作業なら今すぐ役に立つか』が見えるようにしています。"
accuracy_note: "ここにある項目は、すべてが実装済みという意味ではありません。提案中・設計完了・外部依存を分けて読めるようにしています。"
page_highlights:
  - "文章改善や用語整理のような、小さくても価値の高い参加方法を明示しています。"
  - "Issueの状態と、どこまで実装済みかを切り分けて追えます。"
  - "強い主張より、達成条件と反証条件が明確なIssueを重視する方針です。"
known_points:
  - "文章改善、用語整理、リンク修正のような小さな変更も、このサイトでは重要な貢献です。"
  - "Issue の状態ラベルは、実装状況や公開状況を読むためのもので、科学的確定を意味しません。"
  - "外部依存タスクは、今ここで実行できる変更とは分けて扱う必要があります。"
unknown_points:
  - "どの提案が将来どこまで実装や共同研究へ進むかは、Issue 段階ではまだ確定しません。"
  - "外部依存タスクの完了時期や相手先の合意は、このページだけでは保証できません。"
wiki_links:
  - label: "Wiki Home"
    url: "/wiki/"
    description: "分野の前提知識を先に補いたい人向けの入口です。"
  - label: "Wiki: 内製で先にやることと外部依存"
    url: "/wiki/internal-prework-and-external-dependencies.html"
    description: "今このリポジトリで進められることと、外部依存になることを分けます。"
  - label: "Wiki: WBEの基本"
    url: "/wiki/mind-upload-basics.html"
    description: "何の話を改善しているのかを先に把握できます。"
  - label: "Wiki: 検証基盤の基本"
    url: "/wiki/verification-basics.html"
    description: "『達成条件』『反証条件』がなぜ重要かを初歩から説明します。"
recommended_pages:
  - label: "スタートページ"
    url: "/index.html"
  - label: "検証基盤"
    url: "/verification.html"
  - label: "用語集"
    url: "/glossary.html"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<!-- Intro -->
<div class="abstract-box">
<h2>Welcome</h2>
<p>
Mind-Uploadは、マインドアップロードを検証可能な研究へ進めるオープンコミュニティです。分野や経験を問わず、文章改善や用語整理、誤解の指摘など再現性向上に直結する作業からすぐに参加いただけます。
</p>
</div>

<div class="key-points">
<h4>はじめての人へ</h4>
<ul>
<li><strong>迷ったら：</strong><a href="index.html">Start</a> → <a href="verification.html">Verification</a> → <a href="tech_roadmap.html#definition">前進の定義</a></li>
<li><strong>用語で詰まったら：</strong><a href="glossary.html">Glossary</a> と <a href="faq.html">FAQ</a></li>
<li><strong>最初に価値が出やすい貢献：</strong>「達成条件」と「反証条件」が書けるIssue</li>
</ul>
</div>

<div class="note-box">
<strong>参加の考え方</strong>
<p>
最初から大きな実装を担う必要はありません。曖昧な言い回しの修正、用語の定義確認、リンク切れや根拠不足の指摘も、このサイトでは重要な貢献です。むしろ、再現性を上げる小さな修正の積み上げを重視しています。
</p>
</div>

<div class="note-box">
<strong>前提知識が足りないと感じたとき</strong>
<p>
無理に Issue を書き始めるより、先に <a href="wiki/">wiki</a> で WBE や検証基盤の基礎を押さえる方が安全です。用語の前提がそろうと、どこで止まったかをより正確に報告できます。
</p>
</div>
<div class="note-box">
<strong>Issue の書き方自体を初歩から見たいとき</strong>
<p>
「分からない」をどう書けば価値ある Issue になるか、前進条件や反証条件をどう置くかを初歩から見たい場合は <a href="wiki/issue-writing-basics.html">Wiki: はじめての Issue の書き方</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>外部依存の切り分けで止まったとき</strong>
<p>
IRB、実験、機材、法務が絡むときでも、要求仕様、判定条件、公開ログ形式などは先に内製できます。<a href="wiki/internal-prework-and-external-dependencies.html">Wiki: 内製で先にやることと外部依存の切り分け</a> に、今このリポジトリで進められることを整理しています。
</p>
</div>
<div class="note-box">
<strong>文献を読んだあとに Issue へ落とす流れを見たいとき</strong>
<p>
論文や文献地図を見たあとに、どの未解決問題へ戻し、どの条件で Issue に落とすかを一本道で見たい場合は <a href="wiki/literature-to-action-route.html">Wiki: 文献から実装・参加へ戻る一本道</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>このページのあとに次の1ページを決めたいとき</strong>
<p>
参加したい気持ちはあるが、次に小さな修正を切るのか、条件設計へ進むのか、外部依存を分解するのかで迷う場合は <a href="wiki/participation-next-routes.html">Wiki: 参加・協業ページのあとに進む5つの道</a> をご覧ください。
</p>
</div>

<section class="section" id="first-contribution-guide">
<h2 class="section-title">最初の一歩を決める早見表</h2>
<table class="data-table">
<thead>
<tr>
<th>こんなとき</th>
<th>まずやること</th>
<th>次に見るページ</th>
</tr>
</thead>
<tbody>
<tr>
<td>文章が難しく、どこで止まったかは分かる</td>
<td>「どの段落の、どの言葉で止まったか」を1つに絞って Issue に書く</td>
<td><a href="glossary.html">Glossary</a> / <a href="faq.html">FAQ</a></td>
</tr>
<tr>
<td>主張はあるが、合格条件や反証条件が見えない</td>
<td>「何を満たせば前進と言えるか」「何が出たら否定されるか」を分けて指摘する</td>
<td><a href="verification.html">Verification</a> / <a href="tech_roadmap.html">Roadmap</a></td>
</tr>
<tr>
<td>新しい論文・記事・データを見つけた</td>
<td>内容を要約する前に、既存ページのどこへ統合する話かを決める</td>
<td><a href="research_harvest_50.html">Research Harvest</a> / <a href="datasets.html">Datasets</a></td>
</tr>
<tr>
<td>小さくても今すぐ直せる誤字・リンク切れ・表記ゆれがある</td>
<td>そのまま修正案を Pull Request にし、必要なら対象ページの意味も一文で補足する</td>
<td><a href="content_hub.html">Content Hub</a></td>
</tr>
<tr>
<td>実験、IRB、機材、法務が必要な話を進めたい</td>
<td>このページでは「今すぐ実行できる準備作業」と「外部依存」を分けて整理する</td>
<td><a href="collaborations.html">Collaborations</a></td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="status-label-guide">
<h2 class="section-title">状態ラベルの読み方</h2>
<table class="data-table">
<thead>
<tr>
<th>ラベル</th>
<th>日常語で言うと</th>
<th>まだ確認すべきこと</th>
</tr>
</thead>
<tbody>
<tr>
<td>反映済み（文書）</td>
<td>サイト本文には書かれている状態です。</td>
<td>コード、公開データ、評価ログまで揃っているとは限りません。</td>
</tr>
<tr>
<td>提案化済み</td>
<td>どう直すかの設計は文章になっています。</td>
<td>実装や第三者検証がまだ無い場合があります。</td>
</tr>
<tr>
<td>提案受理（文書）</td>
<td>提案は採用され、本文に取り込まれています。</td>
<td>採用済みでも、再現可能性の基準を満たす公開物は別途必要です。</td>
</tr>
<tr>
<td>審査中提案</td>
<td>有力な案として置かれているが、まだ確定ではありません。</td>
<td>反論、代替案、実装可能性の確認で内容が変わる余地があります。</td>
</tr>
<tr>
<td>実装方針反映（文書） / 実装計画化（文書）</td>
<td>実装の方向や段取りは文章で整理されています。</td>
<td>実際に動くコードと検証結果の公開は別作業です。</td>
</tr>
<tr>
<td>設計完了（実装コード未公開）</td>
<td>考え方は固まっているが、外から追試できる形ではまだ不足があります。</td>
<td>L0再現可能性を満たすには、コード・データ・手順の公開が必要です。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="good-issue-minimum">
<h2 class="section-title">価値が高い Issue に最低限ほしい項目</h2>
<table class="data-table">
<thead>
<tr>
<th>項目</th>
<th>短くても入れてほしい内容</th>
<th>なぜ重要か</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>どこで止まったか</strong></td>
<td>対象ページ、節、段落、用語など、読む人が実際に止まった位置。</td>
<td>抽象的な「分かりにくい」より、直す位置がすぐ特定できるためです。</td>
</tr>
<tr>
<td><strong>何が不足しているか</strong></td>
<td>定義不足、根拠不足、導線不足、状態ラベル不明などの種類。</td>
<td>修正の種類が分かると、文章追加か構造修正かを切り分けやすいためです。</td>
</tr>
<tr>
<td><strong>前進条件</strong></td>
<td>何が足されれば「改善した」と言えるかを一文で書く。</td>
<td>終わりが定まらない Issue を減らし、修正完了の判断をしやすくするためです。</td>
</tr>
<tr>
<td><strong>反証条件</strong></td>
<td>何が確認されたら、その主張や提案は採らないかを書く。</td>
<td>このサイトでは、強い提案ほど「間違いと判定する条件」を先に持つことが重要だからです。</td>
</tr>
<tr>
<td><strong>外部依存かどうか</strong></td>
<td>この場で修正できるのか、IRB・実験・機材・合意が要るのかを分ける。</td>
<td>今すぐ動ける変更と、別トラック管理すべき課題を混同しないためです。</td>
</tr>
</tbody>
</table>
</section>

<!-- Contribution Methods -->
<section class="section">
<h2 class="section-title">How to Contribute</h2>

<div class="stage-list">
<div class="stage-item">
<div class="stage-number">01</div>
<div class="stage-body">
<h4>Issueを立てる (Discussion)</h4>
<p>新しいアイデアの提案、バグの報告、あるいは理論に関する議論は、すべて GitHub Issues から始まります。</p>
<div class="tag-list">
<span class="tag">Bug Report</span>
<span class="tag">Feature Request</span>
<span class="tag">Question</span>
</div>
</div>
</div>

<div class="stage-item">
<div class="stage-number">02</div>
<div class="stage-body">
<h4>Pull Requestを送る (Implementation)</h4>
<p>コードの修正やドキュメントの改善は Pull Request を通じて受け付けています。フォークしてブランチを作成し、変更を提案してください。</p>
</div>
</div>
</div>

<div class="cta-box">
<h4>Start Contributing</h4>
<p>GitHub Issue を作成して、議論に参加しましょう。</p>
<a href="https://github.com/yasufumi-nakata/mind-upload/issues" target="_blank">Open an Issue</a>
</div>
</section>

<!-- Resolved Issues -->
<section class="section">
<h2 class="section-title">Resolved Milestones</h2>
<p>コミュニティの貢献により解決された主要な課題です。</p>

<div class="key-points">
<h4>設計完了（実装コード未公開）</h4>
<ul>
<li><strong>Issue #10:</strong> MUとLLMシミュレーションの判別基準（予測不可能性・自己更新性・因果反応性）の3軸ベンチマーク — <em>設計文書は完了。再現可能な実装コード・テストデータ・評価結果は未公開。</em></li>
<li><strong>Issue #12:</strong> Boundary Problem に対するグリア・代謝指標を含むハイブリッド計測プロトコル — <em>概念設計は完了。プロトコル詳細・必要機材リスト・パイロットデータは未整備。</em></li>
<li><strong>Issue #34:</strong> M8品質管理 (QC) メトリクスのJSONログ出力機能 — <em>スキーマ設計は完了。実装コードはリポジトリに未反映。</em></li>
<li><strong>Issue #43:</strong> R2経験的ベイズによるソース推定と不確実性定量化（信頼区間） — <em>理論的枠組みは文書化済み。<code>02_source_imaging.py</code>の実装コードは未公開。</em></li>
</ul>
</div>
<div class="note-box">
<strong>透明性に関する注記</strong>
<p>
上記のIssueは、サイト内の文書レベルでは対応が完了していますが、第三者が再現・検証できる形（実行可能コード、テストデータ、評価結果）での公開には至っていません。本プロジェクトが掲げる再現性の基準（L0: 第三者による再現可能性）を満たすためには、これらの実装の公開が必要です。
</p>
</div>
</section>

<section class="section" id="technical-issue-tracker">
<h2 class="section-title">Technical Issue Tracker（本文統合済み）</h2>
<p>
以下は、Technical Proposal 系 Issue の対応状況です。判断根拠は、各 Proposal の該当節へ直接リンクしています。
</p>

<table class="data-table">
<thead>
<tr>
<th>Issue</th>
<th>対応内容（要約）</th>
<th>状態</th>
<th>根拠リンク</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>#46</strong></td>
<td>計測QA、同期補正、アーティファクト除去、BIDS/Motion-BIDSの統合方針を整理</td>
<td>提案化済み</td>
<td><a href="technical_proposal_46.html#qa">#qa</a> / <a href="technical_proposal_46.html#sync">#sync</a> / <a href="technical_proposal_46.html#bids">#bids</a></td>
</tr>
<tr>
<td><strong>#47</strong></td>
<td>BIDS標準化、ASR/ZapLine、wPLI/STE、LSL同期の実装方針を拡張</td>
<td>提案受理（文書）</td>
<td><a href="technical_proposal_47.html#bids">#bids</a> / <a href="technical_proposal_47.html#preprocessing">#preprocessing</a> / <a href="technical_proposal_47.html#connectivity">#connectivity</a></td>
</tr>
<tr>
<td><strong>#48</strong></td>
<td>OPM-MEG、転移学習、Team Flow因果、IIT実装の拡張案を提出</td>
<td>審査中提案</td>
<td><a href="technical_proposal_48.html#measurement">#measurement</a> / <a href="technical_proposal_48.html#teamflow">#teamflow</a> / <a href="technical_proposal_48.html#iit-implementation">#iit-implementation</a></td>
</tr>
<tr>
<td><strong>#56</strong></td>
<td>反実仮想の識別不能性に対して PCI と do-calculus を導入する検証設計へ変更</td>
<td>提案化済み</td>
<td><a href="technical_proposal_56.html#problem-statement">#problem-statement</a> / <a href="technical_proposal_56.html#proposal">#proposal</a></td>
</tr>
<tr>
<td><strong>#58</strong></td>
<td>NESS散逸・因果識別可能性・IIT近似計算の3課題に対する設計方針を明文化</td>
<td>提案化済み</td>
<td><a href="technical_proposal_58.html#thermo">#thermo</a> / <a href="technical_proposal_58.html#counterfactual">#counterfactual</a> / <a href="technical_proposal_58.html#iit">#iit</a></td>
</tr>
<tr>
<td><strong>#61</strong></td>
<td>Unfolding論点・熱力学コスト2層化・SCM厳密化・多モデル推論への修正を提示</td>
<td>実装方針反映（文書）</td>
<td><a href="technical_proposal_61.html#causal-structure">#causal-structure</a> / <a href="technical_proposal_61.html#thermodynamics">#thermodynamics</a> / <a href="technical_proposal_61.html#multi-model-inference">#multi-model-inference</a></td>
</tr>
<tr>
<td><strong>#62</strong></td>
<td>#58批判に対し、同値類警告とIIT近似の実装計画を追加補強</td>
<td>実装計画化（文書）</td>
<td><a href="technical_proposal_62.html#thermodynamics">#thermodynamics</a> / <a href="technical_proposal_62.html#identifiability">#identifiability</a> / <a href="technical_proposal_62.html#complexity">#complexity</a></td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>運用ルール</strong>
<p>
このトラッカーは「サイト内で確認可能な証跡」を基準に更新します。外部実装（実験・法務・機材調達等）は外部依存として分離し、本ページでは主張しません。
</p>
</div>

<div class="cta-box">
<h4>統合本文</h4>
<p>Technical Proposal 全体の統合本文は `proposals.html` に集約しています。</p>
<a href="proposals.html">統合本文を見る →</a>
</div>
</section>

<section class="section" id="recent-issue-responses">
<h2 class="section-title">最新Issue対応（#257–#263）</h2>
<p>
以下は 2026年2月後半に追加された Issue への反映結果です。今回は「今回実行する変更」と「外部依存で保留」を明確に分離して記録します。
</p>

<table class="data-table">
<thead>
<tr>
<th>Issue</th>
<th>要求</th>
<th>今回実行する変更</th>
<th>状態</th>
<th>根拠</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>#257</strong></td>
<td>逆問題不確実性・因果同値性・熱力学整合性の厳密化</td>
<td>HBM不確実性マップ、因果同値類の明示、NESS/EPR要件を本文基準へ追記</td>
<td>反映済み（文書）</td>
<td><a href="proposals.html#stream-e-rigor">proposals#stream-e-rigor</a> / <a href="verification.html#verification-rigor-2026-02">verification#verification-rigor-2026-02</a></td>
</tr>
<tr>
<td><strong>#258</strong></td>
<td>IIT計算量制約と熱力学的検証要件の明確化</td>
<td>PCI-ST中心運用と熱力学KPI（論理コスト/散逸コスト分離）を追加</td>
<td>反映済み（文書）</td>
<td><a href="proposals.html#stream-e-rigor">proposals#stream-e-rigor</a> / <a href="verification.html#thermodynamic-verification">verification#thermodynamic-verification</a></td>
</tr>
<tr>
<td><strong>#259</strong></td>
<td>ASR副作用・BIDSセマンティック不足への対応</td>
<td>ASR前後のMI/PLV監査とCogPO/NIF/主観報告メタデータ要件を追加</td>
<td>反映済み（文書）</td>
<td><a href="proposals.html#stream-e-rigor">proposals#stream-e-rigor</a> / <a href="verification.html#verification-rigor-2026-02">verification#verification-rigor-2026-02</a></td>
</tr>
<tr>
<td><strong>#260</strong></td>
<td>逆問題・反実仮想・熱力学の統合強化</td>
<td>#257〜#259の追記を統合要件として束ね、検証条件を再定義</td>
<td>反映済み（文書）</td>
<td><a href="proposals.html#stream-e-rigor">proposals#stream-e-rigor</a> / <a href="verification.html#causal-perturbation-suite">verification#causal-perturbation-suite</a></td>
</tr>
<tr>
<td><strong>#261</strong></td>
<td>外部記事URLの内容追加</td>
<td>収集済み文献導線へ追記し、参照URLをEvidence Bankに登録</td>
<td>反映済み（文書）</td>
<td><a href="research_harvest_50.html#recent-intake-2026-02">research_harvest_50#recent-intake-2026-02</a></td>
</tr>
<tr>
<td><strong>#262</strong></td>
<td>ScienceDirect/arXiv URLの内容追加</td>
<td>2件のURLをEvidence Bankの新規受け入れログへ追加</td>
<td>反映済み（文書）</td>
<td><a href="research_harvest_50.html#recent-intake-2026-02">research_harvest_50#recent-intake-2026-02</a></td>
</tr>
<tr>
<td><strong>#263</strong></td>
<td>arXiv URLの内容追加</td>
<td>arXiv文献を受け入れログに追加し、要確認ステータスを明示</td>
<td>反映済み（文書）</td>
<td><a href="research_harvest_50.html#recent-intake-2026-02">research_harvest_50#recent-intake-2026-02</a></td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>外部依存で保留</strong>
<ul>
<li><strong>タスク:</strong> 実被験者を対象としたTMS/tDCS介入実験 <strong>担当:</strong> 実験担当PI <strong>前提条件:</strong> IRB承認・機材確保・被験者募集 <strong>完了条件:</strong> 事前登録済みプロトコルで取得した公開可能データと監査ログが揃うこと</li>
</ul>
</div>
</section>

<!-- Verification Audit -->
<section class="section" id="verification-audit">
<h2 class="section-title">Verification Audit（180件の検証監査）</h2>
<p>
2026年2月に実施した全サイトコンテンツの体系的検証監査の結果です。4カテゴリ・180件のGitHub Issueとして登録し、サイト修正を通じて対応しています。
</p>

<table class="data-table">
<thead>
<tr>
<th>カテゴリ</th>
<th>Issue範囲</th>
<th>件数</th>
<th>対応状況</th>
<th>主な修正内容</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>LIT（文献検証）</strong></td>
<td>#71–#110</td>
<td>40件</td>
<td>文書修正済み</td>
<td>DOI検証、重複参照の除去（ref-68/69/72/75）、FlyWire 2024追加、未検証引用の明示</td>
</tr>
<tr>
<td><strong>THEO（理論的ギャップ）</strong></td>
<td>#111–#145</td>
<td>35件</td>
<td>文書修正済み</td>
<td>ハードプロブレムの立場明示、Unfolding Argument対応、FEP批判の認知、哲学的前提の表化</td>
</tr>
<tr>
<td><strong>IMPL（実装ギャップ）</strong></td>
<td>#146–#195</td>
<td>50件</td>
<td>文書修正済み</td>
<td>実装ステータス透明性報告、L0未達成の明示、エビデンスギャップ分析、Deployment節追加</td>
</tr>
<tr>
<td><strong>METH（方法論・最新研究）</strong></td>
<td>#196–#250</td>
<td>55件</td>
<td>文書修正済み</td>
<td>コネクトーム進捗更新、代替アプローチ比較表、倫理FAQ追加、用語集拡充（13用語追加）</td>
</tr>
</tbody>
</table>

<div class="key-points">
<h4>主要な修正（サイト横断）</h4>
<ul>
<li><strong>perspective.md：</strong>重複参照4件除去、Limitations節追加、FlyWireコネクトーム更新、Chalmers 1995追加</li>
<li><strong>idea.md：</strong>Limitations and Open Questions節追加、Weber 2025にDOIリンク付与、参考文献5件追加</li>
<li><strong>verification.md：</strong>実装ステータス透明性報告表追加、科学的ギャップ分析節追加、MOABB/FAIR参照追加</li>
<li><strong>glossary.md：</strong>意識理論セクション（IIT/GNWT/FEP/PCI/マルコフブランケット等8用語）と実装基盤セクション（5用語）を追加</li>
<li><strong>faq.md：</strong>ハードプロブレム、コピー問題、Cogitate結果、倫理、他プロジェクト比較の5問を追加</li>
<li><strong>wbe_101.md：</strong>哲学的前提の比較表、代替アプローチ比較表を追加</li>
<li><strong>proposals.md：</strong>エビデンスギャップ節追加（ASR/OPM-MEG/do-calculus/NESS課題の明示）</li>
<li><strong>tech_roadmap.md：</strong>I8/I9構造バグ修正、Deployment & Governance節（D0-D3）追加</li>
</ul>
</div>

<div class="note-box">
<strong>透明性に関する注記</strong>
<p>
上記の修正はすべて「文書レベル」です。実行可能コード、テストデータ、評価結果としての公開（L0達成）は別途必要であり、本監査ではその乖離を明示することを優先しました。
</p>
</div>
</section>

<!-- Technical Critique Response -->
<section class="section" id="technical-critique">
<h2 class="section-title">Technical Critique対応（#64–#70）</h2>
<p>
2026年2月に提出された7件の技術的・科学的批判（Issues #64–#70）への対応です。共通テーマをまとめて各ファイルに反映しています。
</p>

<table class="data-table">
<thead>
<tr>
<th>テーマ</th>
<th>対応Issue</th>
<th>修正内容</th>
<th>反映先</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>IIT 4.0計算量・Unfolding Argument</strong></td>
<td>#64, #65, #68, #69</td>
<td>哲学的ゾンビリスクの明示、ニューロモルフィック必要性の強調、階層的粗視化の導入</td>
<td><a href="perspective.html#decoding-to-emulation-gap">perspective</a></td>
</tr>
<tr>
<td><strong>EEG空間解像度の限界</strong></td>
<td>#64, #66, #67, #70</td>
<td>情報理論的限界の明示（7桁ギャップ）、WBEでの現実的役割の再定義</td>
<td><a href="eeg_101.html#information-theoretic-limits">eeg_101</a></td>
</tr>
<tr>
<td><strong>反実仮想的等価性の不十分さ</strong></td>
<td>#65, #66, #69, #70</td>
<td>EI・Causal Density・STEの3指標追加、Pearlの因果梯子による評価枠組み</td>
<td><a href="perspective.html#decoding-to-emulation-gap">perspective</a> / <a href="verification.html#verification-rigor">verification</a></td>
</tr>
<tr>
<td><strong>NESS熱力学的接地</strong></td>
<td>#68</td>
<td>Landauer限界を超えるEPR要件、Fisher Informationとの結合</td>
<td><a href="perspective.html#decoding-to-emulation-gap">perspective</a></td>
</tr>
<tr>
<td><strong>DCM/ベイズ法の限界</strong></td>
<td>#64, #65, #67, #70</td>
<td>BMR・Causal Fingerprinting・適応的前処理（Riemannian Potato）の導入</td>
<td><a href="proposals.html#integrated-streams">proposals</a></td>
</tr>
<tr>
<td><strong>ESI不確実性定量化</strong></td>
<td>#67, #69, #70</td>
<td>信頼区間義務化、適応的ASR/ZapLine-plus、順問題誤差伝播</td>
<td><a href="eeg_101.html#esi-uncertainty">eeg_101</a> / <a href="verification.html#verification-rigor">verification</a></td>
</tr>
</tbody>
</table>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>Resources</h4>
<ul>
<li><a href="https://github.com/yasufumi-nakata/mind-upload" target="_blank">GitHub Repository →</a></li>
<li><a href="idea.html">Theoretical Framework →</a></li>
<li><a href="tech_roadmap.html">Technical Roadmap →</a></li>
</ul>
</div>

<div class="note-box">
<strong>Code of Conduct</strong>
<p>
すべての参加者が快適に議論できるよう、互いに敬意を持って接してください。科学的な批判は歓迎されますが、攻撃的な言動は容認されません。
</p>
</div>

</aside>
</main>
