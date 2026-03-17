---
layout: default
title: "Mind-Upload"
description: "マインドアップロード/WBEを「進歩を測れる科学」に寄せるための検証基盤（Verification Commons）。"
article_type: Start Here
subtitle: "勝利条件・標準・ベンチマーク・事前登録を先に作る"
author: Mind Uploading Research Project
last_updated: "2026-03-17"
note: "Human-friendly landing page"
audience: "はじめて来た人、全体像だけ先に知りたい人、読む順番で迷いたくない人"
reading_time: "5〜10分"
page_intro: "このページは、Mind-Upload 全体の入口です。『このサイトは何を目指しているか』『どこから読むと迷いにくいか』『今すぐ見に行くべきページはどれか』を最短で把握できるようにしています。"
accuracy_note: "ここでは入口に必要なことだけを先に示します。細かい根拠や技術的な条件は、各リンク先で確認してください。"
page_highlights:
  - "Mind-Uploadの中心は、派手な結論を出すことではなく、前進を測れる検証基盤を作ることです。"
  - "迷ったら Verification → Roadmap → WBE/EEG入門 の順で読むと、話の軸を保ちやすいです。"
  - "配線図や cell type だけでは長期ダイナミクスは決まらず、sleep/homeostasis・髄鞘・グリア代謝も別変数として残ります。"
  - "brain-to-text や speech demo では、Neural Contribution Card で神経寄与と task / language prior を切り分けます。"
  - "same-day の成功を cross-day / long-term claim へ読み替えないため、Temporal Validity Card を公開運用へ追加しました。"
  - "用語や前提で止まったときに戻れる入口として、FAQ と用語集も近くに置いています。"
known_points:
  - "公開データ、標準、ベンチマーク、監査をそろえると、L0〜L2 の前進は比較可能な形で積み上げられます。"
  - "EEGやデコーディング研究は、条件を限定すれば測定可能な前進を作れます。"
  - "connectome-complete は emulation-complete を意味せず、maintenance-state の不足を別に監査する必要があります。"
  - "本人性や意識の強い主張は、入口ページではなく後段の検証設計として扱う必要があります。"
unknown_points:
  - "どの条件を満たせば L4 の本人性を認めるかについて、分野横断の合意はまだありません。"
  - "非侵襲計測だけで WBE に十分な内部情報が取れるかは未解決です。"
  - "L5 の社会実装に必要な制度設計は、技術問題だけでは決まりません。"
wiki_links:
  - label: "Wiki Home"
    url: "/wiki/"
    description: "初歩から学ぶための全体マップです。"
  - label: "Wiki: 公開ページ冒頭ブロックの読み方"
    url: "/wiki/page-header-reading-guide.html"
    description: "各ページ上部の案内、既知/未知、wiki導線をどう読むかを整理します。"
  - label: "Wiki: 公開ページの読み分けガイド"
    url: "/wiki/public-page-reading-guide.html"
    description: "Verification、Roadmap、WBE 101、Datasets などの役割差を整理します。"
  - label: "Wiki: WBEの基本"
    url: "/wiki/mind-upload-basics.html"
    description: "マインドアップロードと WBE の最初の一歩を丁寧に説明します。"
  - label: "Wiki: 主張の読み方"
    url: "/wiki/claims-and-evidence.html"
    description: "ニュースや研究発表を、証拠の強さで読み分ける練習用ページです。"
recommended_pages:
  - label: "検証基盤"
    url: "/verification.html"
  - label: "WBE入門"
    url: "/wbe_101.html"
  - label: "FAQ"
    url: "/faq.html"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>What This Is</h2>
<p>
Mind-Uploadは、「心をコンピュータで再現できるのか？」という大きな問いを、<strong>検証できる小さな課題</strong>に分けて進めるサイトです。大きな結論を急がず、まずは<strong>何を達成したら前進か</strong>と、<strong>他の人が同じ結果を確認できるか</strong>を先に決めます。
</p>
</div>

<div class="key-points">
<h4>このページで先に分かること</h4>
<ul>
<li><strong>このサイトの中心：</strong>「本当にできるのか」をすぐ断言するのではなく、まず確かめ方を揃えることです。</li>
<li><strong>最短の読み方：</strong>全体像だけ知りたい場合は、下の「読む順番」から 1〜3 を見れば十分です。</li>
<li><strong>このページでしないこと：</strong>本人性や意識の最終結論を、入口ページだけで決めることはしません。</li>
</ul>
</div>

<div class="note-box">
<strong>入口で先に防ぐ誤読</strong>
<p>
このサイトは 2026年3月の一次文献再監査を受けて、<strong>「配線図と cell type があれば、残りはほぼ埋まる」</strong>という読み方を入口ページでも採りません。sleep / wake に依存した再正規化、髄鞘 / オリゴデンドロサイト support、グリア代謝、分子ターンオーバー下の active maintenance が別変数として残るためです。今回の追補ではこの不足を、<strong>fast execution state</strong>、<strong>controller state</strong>、<strong>slow maintenance state</strong> の 3 層と timescale ごとの claim ceiling へ分け、same-day の fit から cross-day / long-term claim へ飛ばさない運用にそろえました。したがって、本サイトでは <strong>connectome-complete</strong> をそのまま <strong>emulation-complete</strong> と読み替えません。短い説明は <a href="wbe_101.html#state-completeness">WBE入門の hidden state 節</a>、根拠の整理は <a href="wiki/connectome-is-not-enough.html#timescale-matrix">Wiki: 配線図だけでは足りない理由の timescale matrix</a> と <a href="wiki/homeostatic-plasticity-and-maintenance-state.html">Wiki: 恒常性可塑性と維持状態</a> に集約しています。
</p>
</div>

<div class="note-box">
<strong>『どこまで直接見えているか』を先に確認したいとき</strong>
<p>
2026年3月の更新では、measurement stack ごとの主張上限を本文運用へ落とすため、<a href="verification.html#observability-budget">Verification の Observability Budget</a> を追加しました。multimodal という言葉だけで state-complete と読まないため、<a href="wiki/measurement-stack-and-claim-ceiling.html">Wiki: 計測スタックごとの observability と claim ceiling</a> では <strong>stack 別の整理表</strong>に加えて、<strong>state variable × timescale × direct / proxy / inferred</strong> の行列も公開しています。
</p>
</div>

<div class="note-box">
<strong>multimodal を見たときに、何が本当に増えたか先に切り分けたいとき</strong>
<p>
2026年3月の再監査では、<strong>同時計測 + 共有時計</strong>、<strong>同一個体の幾何統合</strong>、<strong>coverage-limited な侵襲校正</strong>、<strong>atlas / transcriptomic prior</strong> を、同じ <code>multimodal</code> の 1 語で読まない方針にそろえました。特に EEG-fMRI では、shared clock があっても BOLD は hemodynamic proxy であり、<strong>2025年12月16日公開の Epp et al.</strong> が示したように cortex の有意 voxel の約40%で BOLD と酸素代謝変化が逆向きになりえます。さらに今回の更新では、<strong>baseline vascular state / CVR</strong> を別監査しない限り、BOLD の群差や縦断差をそのまま neural difference と読みません。したがって本サイトでは、<code>multimodal = mechanistic truth</code> と読まず、<a href="verification.html#fusion-card">Verification の Fusion Card</a> と <a href="wiki/multimodal-integration-basics.html#hemodynamic-gate">Wiki: hemodynamic proxy gate</a> を先に確認してください。
</p>
</div>

<div class="note-box">
<strong>『何がまだ claim を止めているか』まで見たいとき</strong>
<p>
Observability Budget で「何を直接見たか」を確認したら、次は <a href="verification.html#latent-state-error-budget">Verification の latent-state error budget</a> で、<strong>どの未観測状態がいまの誤差をまだ支配しているか</strong>を確認してください。ここでは、内在興奮性、現在のシナプス効率、遅延 / 髄鞘、神経修飾の specificity、glial / slow-state、chronic unit identity を別々の error source として監査し、connectome-only baseline と augmentation claim をどう読み分けるかまで固定しています。
</p>
</div>
<div class="note-box">
<strong>same-day の成功を cross-day / long-term claim へ上げる前に見たいとき</strong>
<p>
2026年3月の更新では、縦断主張の誤読を止めるため <a href="verification.html#temporal-validity-card">Verification の Temporal Validity Card</a> を追加しました。ここでは <strong>fixed decoder interval</strong>、<strong>state annotation</strong>、<strong>interface / decoder drift</strong>、<strong>recalibration burden</strong>、<strong>transfer ceiling</strong> を独立に出し、same-day の fit を別日安定性や長期 deployability へそのまま延長しません。背景は <a href="wiki/state-trait-and-drift.html">Wiki: state・trait・ドリフト</a> に集約しています。
</p>
</div>
<div class="note-box">
<strong>cross-day の score だけで maintenance-consistent claim へ上げたくないとき</strong>
<p>
今回の追補では、時間軸の成功と maintenance route の証跡を分けるため <a href="verification.html#maintenance-state-error-budget">Verification の maintenance-state error budget</a> を追加しました。ここでは <strong>controller state</strong>、<strong>sleep / wake history</strong>、<strong>timing-support</strong>、<strong>bioenergetic / glial / clearance proxy</strong> を別欄で出し、same-day の fit や cross-day の hold を、そのまま <strong>maintenance-consistent</strong> や <strong>remote-memory relevant</strong> と読まないようにします。背景は <a href="wiki/homeostatic-plasticity-and-maintenance-state.html">Wiki: 恒常性可塑性と維持状態</a> に集約しています。
</p>
</div>
<div class="note-box">
<strong>『文字列や音声が出た』ときに、何が脳由来か先に見たいとき</strong>
<p>
2026年3月の更新では、brain-to-text / speech decode の過大解釈を止めるため <a href="verification.html#neural-contribution-card">Verification の Neural Contribution Card</a> を追加しました。ここでは <strong>task constraint</strong>、<strong>language model / prompt / candidate set</strong>、<strong>no-brain / no-LM / shuffle baseline</strong>、<strong>subject cooperation / calibration burden</strong>、<strong>online / offline</strong> を固定し、「文字列が出た」をそのまま neural reconstruction と読み替えません。入口Q&amp;Aなら <a href="faq.html#brain-to-text">FAQ: brain-to-text の見方</a> が近道です。
</p>
</div>

<div class="note-box">
<strong>公開ページと wiki の役割分担</strong>
<p>
このトップページを含む公開ページは、まず「いま何が分かっていて、何がまだ未解決か」を早く把握するための<strong>情報ポータル</strong>です。背景から順に学びたい場合は、各ページ上部の <strong>wiki</strong> 導線から学習用ページへ進んでください。
</p>
</div>
<div class="note-box">
<strong>このサイトをどう使うかで迷ったとき</strong>
<p>
全体像をつかむ、初歩から学ぶ、実際に直す・参加する、の 3 モードでサイト全体の使い方を見たい場合は <a href="wiki/site-usage-modes.html">Wiki: このサイトの3つの使い方</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>A4 要約冊子で先に全体像だけ見たいとき</strong>
<p>
公開ページの要点を短く束ねた版として <a href="summary_booklet.html">Summary Booklet</a> を追加しています。GitHub Actions ではこのページから A4 PDF も生成いたします。
</p>
</div>
<div class="note-box">
<strong>公開ページどうしの違いで迷ったとき</strong>
<p>
Verification、Roadmap、Perspective、WBE 101、Datasets などは、似た説明をしているようで役割が違います。まずどの公開ページから入るべきかを整理したい場合は <a href="wiki/public-page-reading-guide.html">Wiki: 公開ページの読み分けガイド</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>『分かっていること / 分かっていないこと』の意味で迷ったとき</strong>
<p>
このサイトの公開ページは、断言できる範囲と保留すべき範囲を先に分けています。既知/未知、正確さの前提、外部依存をどう読むかを 1 枚で見たい場合は <a href="wiki/known-unknown-and-status-reading.html">Wiki: 『分かっていること / 分かっていないこと』の読み方</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>ページ上部の案内ブロック自体の使い方で迷ったとき</strong>
<p>
公開ページの冒頭には「このページの読み方」「向いている人」「正確さの前提」「いま分かっていること」「wiki で基礎から確認する」が並びます。この順番でどう読むと迷いにくいかを 1 枚で見たい場合は <a href="wiki/page-header-reading-guide.html">Wiki: 公開ページ冒頭ブロックの読み方</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>理論から入りたいとき</strong>
<p>
WBE 101、Perspective、Framework、Roadmap の違いだけを理論系に絞って整理したい場合は <a href="wiki/theory-pages-reading-guide.html">Wiki: 理論系ページの読み分けガイド</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>手を動かす側から入りたいとき</strong>
<p>
Verification、Datasets、Datasets内のL0実践節、Verification内のケースワーク節、Issue内の提案統合節の違いだけを実務系に絞って整理したい場合は <a href="wiki/practical-pages-reading-guide.html">Wiki: 実務系ページの読み分けガイド</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>最初の30分で何を見るかだけ決めたいとき</strong>
<p>
全体像、理論、実務、文献、参加のどこから入るかで、最初の 3〜4 ページを固定したい場合は <a href="wiki/first-30-minutes-by-goal.html">Wiki: 目的別の最初の30分ルート</a> をご覧ください。
</p>
</div>

<table class="data-table">
<thead>
<tr>
<th>こんな人に向く入口</th>
<th>最初の1ページ</th>
<th>次に進むページ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>全体像だけ先に知りたい</strong></td>
<td><a href="verification.html">Verification</a></td>
<td><a href="tech_roadmap.html">Roadmap</a> で、何を解けば前進かを見ます。</td>
</tr>
<tr>
<td><strong>まず短く入門したい</strong></td>
<td><a href="wbe_101.html">WBE 101</a></td>
<td><a href="eeg_101.html">EEG 101</a> で、現実に何が測れるかを押さえます。</td>
</tr>
<tr>
<td><strong>用語や理論名で止まりやすい</strong></td>
<td><a href="glossary.html">Glossary</a></td>
<td><a href="faq.html">FAQ</a> で、よくある誤解を先に潰します。</td>
</tr>
<tr>
<td><strong>本当に初歩から順番に学びたい</strong></td>
<td><a href="wiki/">Wiki</a></td>
<td><a href="wbe_101.html">WBE 101</a> や <a href="eeg_101.html">EEG 101</a> へ戻ると、公開ページの要点が読みやすくなります。</td>
</tr>
<tr>
<td><strong>公開データで手を動かしたい</strong></td>
<td><a href="datasets.html">Datasets</a></td>
<td><a href="datasets.html#l0-practice">Datasets内のL0実践節</a> で、最小ループへそのまま進みます。</td>
</tr>
<tr>
<td><strong>Issue対応や参加方法を見たい</strong></td>
<td><a href="issue.html">Issue Guide</a></td>
<td><a href="content_hub.html">Content Hub</a> で、どこへ追記するかを確認します。</td>
</tr>
</tbody>
</table>

<table class="data-table">
<thead>
<tr>
<th>このサイトが今やること</th>
<th>この入口ページではまだ主張しないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td>L0〜L2 を中心に、再現可能な解析、比較可能な評価、介入を含む検証条件を整えることです。</td>
<td>L4〜L5 に当たる本人性の最終判定や社会実装の成立を、入口だけで断言することはしません。</td>
</tr>
<tr>
<td>データ、コード、ログ、評価ルールをそろえ、他の人が追える形にすることです。</td>
<td>「雰囲気として人っぽい」「会話が自然」といった印象だけで、WBE成立とみなすことはしません。</td>
</tr>
</tbody>
</table>

<section class="section" id="start">
<h2 class="section-title">読む順番（迷ったらこれ）</h2>
<div class="stage-list">
<div class="stage-item">
<div class="stage-number">01</div>
<div class="stage-body">
<h4>検証基盤（Verification）</h4>
<p>このサイトが「何を作るのか」を1ページで把握できます（勝利条件・標準・ベンチ・登録）。</p>
<a href="verification.html" class="btn-action">Open Verification</a>
</div>
</div>
<div class="stage-item">
<div class="stage-number">02</div>
<div class="stage-body">
<h4>技術ロードマップ（Roadmap）</h4>
<p>WBEを「計測→再構成→実装→検証」の問いの木に分解して、何を解けば前進かを整理します。</p>
<a href="tech_roadmap.html" class="btn-action">Open Roadmap</a>
</div>
</div>
<div class="stage-item">
<div class="stage-number">03</div>
<div class="stage-body">
<h4>研究ノート（Perspective）</h4>
<p>理論・技術・批判点を含めて、現状と論点をまとめた長文ノートです。</p>
<a href="perspective.html" class="btn-action">Open Perspective</a>
</div>
</div>
<div class="stage-item">
<div class="stage-number">04</div>
<div class="stage-body">
<h4>理論フレーム（Framework）</h4>
<p>「静的コピーではなく動的プロセスとしての意識」という立場から、設計要件へ落とすためのノートです。</p>
<a href="perspective.html#design-principles" class="btn-action">Open Framework In Perspective</a>
</div>
</div>
<div class="stage-item">
<div class="stage-number">05</div>
<div class="stage-body">
<h4>論文集（Papers）</h4>
<p>過去10年のMind Uploading関連論文を収集・整理したアーカイブです。</p>
<a href="mind_uploading_papers.html" class="btn-action">Open Papers</a>
</div>
</div>
<div class="stage-item">
<div class="stage-number">06</div>
<div class="stage-body">
<h4>技術提案統合（All Issues）</h4>
<p>Issue #46/#47/#48/#56/#58/#61/#62 の提案・対応状況・根拠節を1ページ本文に統合しています。</p>
<a href="issue.html#proposal-integration" class="btn-action">Open Integrated Proposals</a>
</div>
</div>
<div class="stage-item">
<div class="stage-number">07</div>
<div class="stage-body">
<h4>外部依存・協業候補</h4>
<p>検証基盤に接続可能な研究機関・プロジェクト・企業・助成制度を優先度付きで整理。</p>
<a href="issue.html#external-collaboration" class="btn-action">Open External Collaboration Plan</a>
</div>
</div>
</div>
</section>

<section class="section" id="beginner">
<h2 class="section-title">はじめての人向け（15分コース）</h2>
<p>いきなり長文（Perspective/Roadmap）に入ると大変なので、まずは“入門ページ”を用意しました。</p>
<div class="stage-list">
<div class="stage-item">
<div class="stage-number">A</div>
<div class="stage-body">
<h4>WBE入門</h4>
<p>マインドアップロードを「測れる問題」にするための考え方（勝利条件・反証条件）を短く整理。</p>
<a href="wbe_101.html" class="btn-action">Open WBE 101</a>
</div>
</div>
<div class="stage-item">
<div class="stage-number">B</div>
<div class="stage-body">
<h4>EEG入門</h4>
<p>EEGで何ができて何ができないか、解析の流れ、Mind-Uploadでの位置づけ。</p>
<a href="eeg_101.html" class="btn-action">Open EEG 101</a>
</div>
</div>
<div class="stage-item">
<div class="stage-number">C</div>
<div class="stage-body">
<h4>用語集</h4>
<p>頻出用語の“すり替え”を防ぐための最短辞書。</p>
<a href="glossary.html" class="btn-action">Open Glossary</a>
</div>
</div>
<div class="stage-item">
<div class="stage-number">D</div>
<div class="stage-body">
<h4>データ&ベンチ</h4>
<p>まず何で検証するか（公開データ、置き場、チェックリスト）を実務として整理。</p>
<a href="datasets.html" class="btn-action">Open Datasets</a>
</div>
</div>
<div class="stage-item">
<div class="stage-number">E</div>
<div class="stage-body">
<h4>Wiki（基礎学習）</h4>
<p>本当にゼロから学ぶ人向けに、用語、主張の読み方、EEGの基礎、検証基盤の考え方を順番に説明します。</p>
<a href="wiki/" class="btn-action">Open Wiki</a>
</div>
</div>
</div>
</section>

<div class="cta-box">
<h4>L0実践（Datasets内）</h4>
<p>「再現可能な解析（L0）」を最短で作る手順。</p>
<a href="datasets.html#l0-practice">L0実践を見る →</a>
</div>

<section class="section" id="cases">
<h2 class="section-title">歴史のケースワーク（Verification内）</h2>
<p>
PDB、BIDS+OpenNeuro、PhysioNet、ImageNet、MLPerf、OSFで築かれた検証手法を整理し、Mind-Uploadに転用するための参照ページです。過去の成功例を型として提示し、必要な要素を即座に確認できます。
</p>
<div class="cta-box">
<h4>Verification内ケースワーク</h4>
<p>標準化・ベンチマーク・事前登録が、どう“前進を測れる状態”を作ったか。</p>
<a href="verification.html#casework">ケースワーク集を見る →</a>
</div>
</section>

<section class="section" id="contribute">
<h2 class="section-title">参加（今できること）</h2>
<div class="key-points">
<h4>Ways To Help</h4>
<ul>
<li><strong>提案：</strong>「達成条件」と「反証条件」が書けるIssueは特に価値が高い</li>
<li><strong>レビュー：</strong>既存ページの“すり替え”や“定義の曖昧さ”を指摘する</li>
<li><strong>実装：</strong>まずL0〜L2（再現可能な解析・ベースライン・評価スイート）を積み上げる</li>
</ul>
</div>
<div class="cta-box">
<h4>Contribute</h4>
<p>議論はGitHub Issueから始められます。</p>
<a href="issue.html">貢献ガイドを見る →</a>
</div>
<div class="cta-box">
<h4>Issue対応状況</h4>
<p>Technical Proposal 系 Issue の対応内容と根拠リンクを確認できます。</p>
<a href="issue.html#technical-issue-tracker">Issueトラッカーを見る →</a>
</div>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>Quick Links</h4>
<ul>
<li><a href="verification.html">検証基盤（Verification）→</a></li>
<li><a href="research_harvest_50.html">未解決問題×文献地図（50ワーカー）→</a></li>
<li><a href="wbe_101.html">WBE入門 →</a></li>
<li><a href="eeg_101.html">EEG入門 →</a></li>
<li><a href="datasets.html">データ&ベンチ →</a></li>
<li><a href="glossary.html">用語集 →</a></li>
<li><a href="faq.html">FAQ →</a></li>
<li><a href="datasets.html#l0-practice">L0実践（Datasets内）→</a></li>
<li><a href="verification.html#casework">Verification内ケースワーク →</a></li>
<li><a href="issue.html#proposal-integration">Issue内の提案統合 →</a></li>
<li><a href="mind_uploading_papers.html">論文集（Papers）→</a></li>
<li><a href="issue.html#technical-issue-tracker">Issue対応トラッカー →</a></li>
<li><a href="content_hub.html">公開コンテンツ統合ハブ →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Content Governance</h4>
<ul>
<li><a href="content_hub.html">公開コンテンツ統合ハブ →</a></li>
<li><a href="https://github.com/yasufumi-nakata/mind-upload/blob/main/README.md" target="_blank">README.md ↗</a></li>
<li><a href="https://github.com/yasufumi-nakata/mind-upload/tree/main/.agent" target="_blank">.agent/ ↗</a></li>
<li><a href="https://github.com/yasufumi-nakata/mind-upload/tree/main/automation" target="_blank">automation/ ↗</a></li>
</ul>
</div>

<div class="note-box">
<strong>Rule</strong>
<p>
このサイトでは、強い主張ほど、先に“小さく反証できる形”に分解します。読み物としても使えますが、最終的には検証可能な成果物（データ・コード・評価）に接続することを目的とします。
</p>
</div>

</aside>
</main>
