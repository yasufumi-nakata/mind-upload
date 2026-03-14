---
layout: default
title: "マインドアップロード実現への道：技術・理論の統合アプローチ"
description: "マインドアップロード実現のための中核となるコアサイト。意識や記憶の交換・複製を可能とする技術の研究とコミュニティの中心的ハブ。"
article_type: Perspective
subtitle: "脳の情報処理を別の基盤で再現し、心的機能を移植・複製するという研究仮説の現状と展望"
author: Mind Uploading Research Project
last_updated: "2026-03-14"
note: "研究ノート (2026年1月改訂)"
audience: "理論と実装のつながりまで追いたい人、限界や反論も含めて全体を知りたい人"
reading_time: "30〜45分"
page_intro: "このページは、マインドアップロードをめぐる理論・計測・実装の論点を、一次文献と限界を並べながら追う長い研究ノートです。楽観論だけでも悲観論だけでもなく、『どこまでは言えて、どこから先は未解決か』をはっきり分けて読めるようにしています。"
accuracy_note: "特定の意識理論がすでに正しいと確定した前提では書いていません。支持点と未解決点を分けて扱います。"
page_highlights:
  - "理論の紹介だけで終わらず、実装へ落としたときの制約まで一緒に追います。"
  - "強い主張ほど、反証条件や代替説明を並べて確認します。"
  - "長文ですが、導入と注意書きだけでも全体の立場が分かる構成にしています。"
known_points:
  - "主要理論のどれも、現時点では単独で決定打になっていません。"
  - "EEG 単体には逆問題や空間分解能の限界があり、強い主張の土台としては不足があります。"
  - "因果的摂動、追試可能性、代替説明の排除を抜いた強い主張は危うい、という点はかなりはっきりしています。"
unknown_points:
  - "どの理論の組み合わせが最終的に十分条件になるかは未確定です。"
  - "どこまで多モダリティ統合で EEG の限界を埋められるかは研究途中です。"
  - "本人性や現象的意識の最終判定を、理論と工学でどう接続するかは未解決です。"
wiki_links:
  - label: "Wiki: 意識理論マップ"
    url: "/wiki/consciousness-theory-map.html"
    description: "IIT、GNWT、FEP、PCI の違いと役割分担を初歩から整理します。"
  - label: "Wiki: 部分解決・探索段階・未整備の読み方"
    url: "/wiki/progress-labels-and-open-problem-status.html"
    description: "このページで出る『不足』『未確定』『未解決』の読み方を整理します。"
  - label: "Wiki: 本人性とコピー問題"
    url: "/wiki/personhood-and-copy-problem.html"
    description: "このページで出る哲学寄りの論点を、初歩から整理します。"
  - label: "Wiki: EEG前処理とQC"
    url: "/wiki/eeg-preprocessing-and-qc.html"
    description: "EEG の限界がどこから来るのかを、処理の流れから説明します。"
  - label: "Wiki: 主張と証拠の読み方"
    url: "/wiki/claims-and-evidence.html"
    description: "理論の話を、どの強さの主張かで整理しながら読む補助ページです。"
  - label: "Wiki: 閉ループ・遅延・ジッタ・安全停止"
    url: "/wiki/closed-loop-latency-jitter-and-safety-stops.html"
    description: "閉ループ実装で問題になる遅延、ジッタ、安全停止の基本を補います。"
  - label: "Wiki: 熱力学的接地の基本"
    url: "/wiki/thermodynamic-grounding-basics.html"
    description: "Landauer、散逸、NESS、EPR の入口を初歩から整理します。"
recommended_pages:
  - label: "検証基盤"
    url: "/verification.html"
  - label: "技術ロードマップ"
    url: "/tech_roadmap.html"
  - label: "WBE入門"
    url: "/wbe_101.html"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<!-- Abstract -->
<div class="abstract-box">
<h2>Abstract</h2>
<p>このページは、マインドアップロード（WBE）を「本当に検証できる研究」にするための長い研究ノートです。内容は、<strong>どう測るか</strong>、<strong>どう読み取るか</strong>、<strong>どう実装するか</strong>の3段階で整理しています。最新研究の成果だけでなく、うまくいっていない点や限界も同じ重みで扱い、「どこまで言えて、どこから言えないか」をはっきり分ける構成にしています。</p>
</div>

<div class="cta-box">
<h4>Start Here: Verification Commons</h4>
<p>Mind-Uploadの中心は「前進の定義」と「比較可能な検証基盤」を先に作ることです。</p>
<a href="verification.html">検証基盤（Platform）を見る →</a>
</div>

<div class="note-box">
<strong>新しく来た人へ</strong>
<p>
このページは長い研究ノートです。まずは <a href="wbe_101.html">WBE入門</a> と <a href="eeg_101.html">EEG入門</a>、必要なら <a href="glossary.html">用語集</a> を先に読むと迷子になりにくいです。
</p>
</div>

<div class="note-box">
<strong>背景説明がほしいとき</strong>
<p>
理論名の違いで止まった場合は <a href="wiki/consciousness-theory-map.html">Wiki: 意識理論マップ</a>、コピー問題や本人性の話で止まった場合は <a href="wiki/personhood-and-copy-problem.html">Wiki: 本人性とコピー問題</a>、EEG の限界が気になる場合は <a href="wiki/eeg-preprocessing-and-qc.html">Wiki: EEG前処理とQC</a>、計測語とモデル語のつながりで止まった場合は <a href="wiki/measurement-and-modeling-terms.html">Wiki: 計測からモデル化までの用語ガイド</a>、不確実性や棄権の設計で止まった場合は <a href="wiki/uncertainty-confidence-and-abstention.html">Wiki: 不確実性・信頼区間・棄権</a>、マルチモーダル統合の意味で止まった場合は <a href="wiki/multimodal-integration-basics.html">Wiki: マルチモーダル統合の基本</a>、縦断評価やドリフトで止まった場合は <a href="wiki/state-trait-and-drift.html">Wiki: state・trait・ドリフト</a>、閉ループ実装の遅延や安全停止で止まった場合は <a href="wiki/closed-loop-latency-jitter-and-safety-stops.html">Wiki: 閉ループ・遅延・ジッタ・安全停止</a>、熱力学や散逸の話で止まった場合は <a href="wiki/thermodynamic-grounding-basics.html">Wiki: 熱力学的接地の基本</a> を先に見ると、本文へ戻りやすくなります。
</p>
</div>
<div class="note-box">
<strong>理論系ページの役割差で迷ったとき</strong>
<p>
Perspective は理論、計測、反論、限界に加え、採用する設計原理までまとめて追う長文ノートです。主張レベルを先にそろえる入口は <a href="wbe_101.html">WBE 101</a>、依存関係の地図は <a href="tech_roadmap.html">技術ロードマップ</a> です。理論系だけの読み分けを 1 枚で見たい場合は <a href="wiki/theory-pages-reading-guide.html">Wiki: 理論系ページの読み分けガイド</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>研究ノート、理論フレーム、提案、Issue の違いで迷ったとき</strong>
<p>
このページは観察と限界を並べる長文ノートであり、提案一覧や実行タスクそのものではありません。事実・仮説・提案・実行タスクの違いを 1 枚で見たい場合は <a href="wiki/facts-hypotheses-proposals-and-tasks.html">Wiki: 事実・仮説・提案・実行タスクの違い</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>WBE入門からここへ来るまでの理論ルートを見たいとき</strong>
<p>
WBE 101 のあとに、なぜこの長文ノートへ進むのか、誤解整理や設計原理との違いも含めて一本道で見たい場合は <a href="wiki/wbe-to-theory-route.html">Wiki: WBE入門から理論を深掘る4ルート</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>『不足』『未確定』『未解決』の重さを分けたいとき</strong>
<p>
このページは限界や反論を多く扱うため、何が<strong>部分解決</strong>で、何が<strong>探索段階</strong>で、何が<strong>未整備</strong>なのかを分けて読む必要があります。進み具合の言葉を 1 枚で整理したい場合は <a href="wiki/progress-labels-and-open-problem-status.html">Wiki: 部分解決・探索段階・未整備の読み方</a> を先にご覧ください。
</p>
</div>

<div class="key-points">
<h4>読む前に確認したいこと</h4>
<ul>
<li><strong>このページの役割：</strong>賛成意見だけを並べることではなく、根拠と限界を同時に追うことです。</li>
<li><strong>このページで言えること：</strong>主要理論が何を説明し、どこでつまずいているかを整理できます。</li>
<li><strong>このページだけでは言えないこと：</strong>「これで意識を完全に説明できた」という最終結論までは出していません。</li>
</ul>
</div>

<div class="note-box">
<strong>迷ったときの読み順</strong>
<p>
まず導入部で立場を把握し、次に <a href="#design-principles">設計原理</a> で「コピーではなく移行としてどう考えるか」を確認し、その後に計測・モデル化・実装の節へ進んでください。哲学寄りの論点で詰まった場合は <a href="faq.html">FAQ</a> を挟むと戻りやすくなります。
</p>
</div>

<table class="data-table">
<thead>
<tr>
<th>いま気になる論点</th>
<th>先に読む節</th>
<th>そこで分かること</th>
</tr>
</thead>
<tbody>
<tr>
<td>主要理論がどこでつまずいているか知りたい</td>
<td><a href="#introduction">Introduction</a></td>
<td>IIT、GNWT、FEP をどう位置づけ直しているかを最初に確認できます。</td>
</tr>
<tr>
<td>計測から実装までの全体設計を見たい</td>
<td><a href="#technical-framework">Technical Framework</a></td>
<td>計測、解読、実装の3段階が、どの前提でつながるかを追えます。</td>
</tr>
<tr>
<td>decode と emulate の間に何が足りないか知りたい</td>
<td><a href="#decoding-to-emulation-gap">Decoding to Emulation Gap</a></td>
<td>相関ベースの読み出しから、因果的検証へ進むための不足分が分かります。</td>
</tr>
<tr>
<td>どんな研究計画に落ちるのか知りたい</td>
<td><a href="#research-program">Research Program</a> / <a href="#eeg-consciousness-roadmap">EEG Consciousness Roadmap</a></td>
<td>実際に何を積み上げるのかを、研究計画として確認できます。</td>
</tr>
<tr>
<td>このページの限界を先に知りたい</td>
<td><a href="#limitations">Limitations</a></td>
<td>理論的限界、工学的限界、運営上の限界を切り分けて読めます。</td>
</tr>
</tbody>
</table>

<table class="data-table">
<thead>
<tr>
<th>このページで比較的強く言えること</th>
<th>このページでまだ仮説として扱うこと</th>
</tr>
</thead>
<tbody>
<tr>
<td>主要理論のどれも、現時点では単独で決定打になっていないことです。</td>
<td>どの理論の組み合わせが最終的に WBE の十分条件になるかは未確定です。</td>
</tr>
<tr>
<td>EEG 単体では逆問題や空間分解能に根本的な限界があることです。</td>
<td>どこまで他モダリティ統合でその限界を埋められるかは、まだ研究課題です。</td>
</tr>
<tr>
<td>因果的摂動、追試可能性、熱力学制約を抜いた強い主張は危ういことです。</td>
<td>それらをどの閾値で「十分」と判定するかは、今後のベンチ設計に依存します。</td>
</tr>
</tbody>
</table>

<section class="section" id="design-principles">
<h2 class="section-title">Design Principles: コピーではなく移行として設計する</h2>
<p>
ここでは、旧 <code>idea.md</code> で独立していた理論フレームを、本研究ノートの設計原理として統合しております。狙いは、哲学的立場を増やすことではなく、<strong>どの前提を設計条件へ落とすのか</strong>を本文の中で切り離さずに読めるようにすることです。
</p>

<div class="key-points">
<h4>採用する設計原理</h4>
<ul>
<li><strong>静的コピーではなく動的移行：</strong> 脳の情報を保存するだけでなく、更新し続ける過程をどう引き継ぐかを問います。</li>
<li><strong>理論は作業仮説として使う：</strong> IIT、FEP、予測符号化は真理宣言ではなく、要件定義へ落とすための補助線として扱います。</li>
<li><strong>本人性は設計条件へ戻す：</strong> コピー問題は抽象論で止めず、連続性テスト、介入応答、因果保存、熱力学制約へ分解します。</li>
</ul>
</div>

<table class="data-table">
<thead>
<tr>
<th>設計で先に固定したいこと</th>
<th>このページの立場</th>
<th>まだ未解決なこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>本人性</strong></td>
<td>「同じデータがあるか」ではなく、「更新し続ける過程が連続しているか」を重く見ます。</td>
<td>どの連続性指標を十分条件とみなすかは未確定です。</td>
</tr>
<tr>
<td><strong>意識理論の使い方</strong></td>
<td>IIT、GNWT、FEP を競わせるより、測定・摂動・統合指標へ変換して使います。</td>
<td>理論横断で安定して使える共通仕様はまだ不足しています。</td>
</tr>
<tr>
<td><strong>熱力学</strong></td>
<td>動的過程を保つなら、論理コストだけでなく散逸や非平衡性も監査対象に入れます。</td>
<td>どの熱力学 KPI が本人性や意識の質に直結するかは未解決です。</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>日常語で言うと</strong>
<p>
写真1枚を保存するのと、動画を同じ動きのまま引き継ぐのは別問題でございます。Mind-Upload を前者ではなく後者に近いものとして扱うなら、必要なのは「構造の複製」だけでなく、「遷移の連続」「介入への応答」「維持コスト」の3点でございます。
</p>
</div>

<div class="note-box">
<strong>この立場が実装へ落ちる場所</strong>
<p>
計測では BIDS、同期、QC、摂動ログが必要になり、モデル化では ESI / DCM / SCM の不確実性管理が必要になり、実装では閉ループ安定性と熱力学的制約が必要になります。したがって、この節は抽象的な宣言ではなく、後続節の要件を束ねる入口として読むのが正しい使い方です。
</p>
</div>
</section>

<!-- Introduction -->
<section class="section" id="introduction">
<h2 class="section-title">Introduction: Theoretical Foundations Revisited</h2>

<h3>1.1. 意識の科学：理論的基盤の再検討と「Adversarial Collaboration」の衝撃</h3>
<div class="note-box">
<strong>この節で決めたいこと</strong>
<p>
ここで決めたいのは、「どの理論が勝ちか」を宣言することではありません。むしろ、主要理論を並べて見たときに、<strong>どの理論にも共通して必要な検証条件は何か</strong>を先に取り出すことが目的です。
</p>
</div>
<p>マインドアップロード（WBE）が再現すべき「意識」とは何か。この問いに対し、本プロジェクトは従来、統合情報理論（IIT）とグローバル神経ワークスペース理論（GNWT）の統合可能性を強めに見積もっていました。しかし、2025年に公開された事前登録型の敵対的共同研究は、IIT / GNWT / RPT の主要予測を部分的には支持しつつ、鍵予測のいくつかを反証し、単一理論を勝者にしませんでした<sup><a href="#ref-54">[54]</a></sup>。さらに、意識内容の候補マーカーと thought-to-report / task relevance のマーカーが分離され、理論選択より先に confound control を固定すべきことが明確になりました<sup><a href="#ref-54">[54]</a></sup>。したがって本サイトでは、理論を採択するのではなく、理論を<strong>事前登録された予測集合</strong>として競わせ、no-report 条件、摂動 benchmark、外部一般化へ翻訳する立場を取ります。FEP / 予測符号化はその候補の一つですが、既定路線とはしません。</p>

<table class="data-table">
<thead>
<tr>
<th>理論</th>
<th>主に説明したいこと</th>
<th>弱点・つまずきやすい点</th>
<th>Mind-Uploadでの使い方</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>IIT</strong></td>
<td>意識の「統合された質」や因果構造を説明したい。</td>
<td>計算量が重く、機能的に同じでも意識なしと判定しうる Unfolding Argument が問題になる。</td>
<td>意識の質や統合性を測る<strong>ものさし候補</strong>として参照し、実装上は PCI 系など近似可能な指標へ落とします。</td>
</tr>
<tr>
<td><strong>GNWT</strong></td>
<td>情報が広域共有されるとき、なぜ意識的アクセスが起こるのかを説明したい。</td>
<td>前頭前野イグニッションが報告動作と切り分けにくく、意識そのものとの対応が揺れやすい。</td>
<td>「広域共有」「報告可能性」がどの条件で成立するかを見る<strong>作業仮説</strong>として使います。</td>
</tr>
<tr>
<td><strong>FEP / 予測符号化</strong></td>
<td>システムが環境とやり取りしながら、どう安定して推論し続けるかを説明したい。</td>
<td>それ自体で現象的意識まで説明しきれるわけではなく、抽象度が高いため何でも説明したように見えやすい。</td>
<td>閉ループ・予測誤差・適応を記述する<strong>候補モデル族</strong>として使い、DCM / SCM / 状態空間モデルと競わせます。</td>
</tr>
</tbody>
</table>

<div class="question-box">
<h4>中心的課題: 理論選好ではなく prediction competition をどう設計するか</h4>
<p>Nature 2025 の adversarial test は、意識内容に関わる信号が occipital / temporal / frontal の複数領域に分布し、同時に一部マーカーが task relevance や report requirements を追うことを示しました<sup><a href="#ref-54">[54]</a></sup>。したがって、どの理論名を掲げるかよりも、どの予測をどの条件で落とすかを先に固定する方が科学的でございます。</p>
<div class="resolution-box">
<h5>解決の方向性: 理論を「勝者」ではなく「予測源」に戻す</h5>
<p>本サイトでは、IIT / GNWT / RPT / FEP を、互いに競争する<strong>予測生成器</strong>として扱います。採否は、no-report 条件、摂動条件、task-relevance 統制、cross-dataset / cross-center 一般化を通ったかで決めます。</p>
<ul style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 6px;"><strong>理論層：</strong>各理論は、どの時空間パターン・どの条件差・どの失敗条件を予測するかを事前登録します。</li>
<li style="margin-bottom: 6px;"><strong>指標層：</strong>PCI/PCI-ST、複雑性、臨界性は理論そのものではなく、予測を落とすための benchmark 候補として扱います。</li>
<li style="margin-bottom: 6px;"><strong>設計層：</strong>no-report、アーチファクト管理、遅延/ジッタ監査、外部妥当化を満たさない限り、理論の当否は繰り上げません。</li>
</ul>
<p>また、閉ループ系の時間要件や反実仮想的等価性は、単一閾値や単一理論で決めるのではなく、課題別 latency budget と failure mode を先に公開し、その上で検証課題として扱います<sup><a href="#ref-76">[76]</a></sup>。</p>
</div>
</div>

<h3>1.2. 理論から実装へ：技術的・哲学的課題</h3>
<p><strong>IITのデジタル基盤への移植課題：</strong> IIT 4.0<sup><a
href="#ref-17">[17]</a></sup>をWBEに応用するには、その公理系をデジタル基盤上でいかに満たすかという問題が残る。特に、物理的な実在を問う「内因的実在（Intrinsic
Existence）」の公理<sup><a
href="#ref-44">[44]</a></sup>は、離散的な計算システム（標準的なノイマン型コンピュータ）では原理的に満たされない可能性が高い（Unfolding Argument）。本プロジェクトでは、デジタルエミュレーションでの「近似」という表現を避け、<strong>ニューロモルフィック・ハードウェアによる因果構造の物理的写像</strong>へのシフトを明記する。あるいは、Albantakis et al. (2023)<sup><a href="#ref-17">[17]</a></sup>が示唆するように、生物学的ニューロンとデジタル素子を組み合わせた<strong>ハイブリッド・システム（Hybrid Systems）</strong>による段階的遷移を主軸に据え、単なる計算上の出力一致ではなく、物理的レベルでの因果力の保存を目指す。</p>

<p><strong>心理的連続性とコピー問題：</strong> デレク・パーフィットの心理的連続性理論<sup><a
href="#ref-4">[4]</a></sup>は、記憶や性格の連続性を本人性の根拠とする。これは、単なる静的なデータコピーではなく、「動的なプロセス」の維持をWBEに要求する。この理論が提起する「コピー問題（分身のパラドックス）」に対し、我々は「段階的な神経置換」や「ハイブリッド脳システム」といった思考実験を、検証可能な工学的プロトコルへと落とし込むことを目指す。
</p>
<p><strong>プロセス哲学への転回：</strong>
意識を静的な「モノ」ではなく、環境との相互作用の中で絶えず更新される「プロセス」として捉える視点は、Whiteheadのプロセス哲学<sup><a
href="#ref-32">[32]</a></sup>や、Fristonの自由エネルギー原理<sup><a
href="#ref-14">[14]</a></sup>／能動的推論<sup><a
href="#ref-45">[45]</a></sup>とも共鳴する。本プロジェクトは、この動的な実在性を計算機上で維持するための技術的要件（例：Slow
Continuous Mind Uploading）を具体化する<sup><a href="#ref-59">[59]</a></sup>。</p>
<div class="note-box">
<strong>研究としての約束</strong>
<p>以下を「最低限のガードレール」として運用する：主要な主張には一次/総説などの出典を付す・仮説と事実、価値判断を区別し不確実性を併記する・評価指標や手順を先に定義し再現可能性を優先する。</p>
</div>
</section>


<!-- Technical Framework -->
<section class="section" id="technical-framework">
<h2 class="section-title">Technical Framework</h2>

<p>マインドアップロードの実現に向けた技術的ロードマップは、「計測」「解読」「実装」の3段階で構想される。これは古典的なWBEロードマップ<sup><a
href="#ref-8">[8]</a></sup>に加え、近年の全脳アーキテクチャ構築ロードマップ<sup><a
href="#ref-7">[7]</a></sup>や大規模シミュレーション計画（Blue Brain等）<sup><a
href="#ref-16">[16]</a></sup>の知見を踏まえた整理である。</p>

<div class="note-box">
<strong>2026-03 文献監査で、この節の書き方を改めた理由</strong>
<p>従来の本文では、Block-Champagne、Active Inference、PCI、TDA、熱力学ログのように性質の異なる要素を、やや近い重みで並べていました。しかし、EEG source imaging の直接妥当化研究、TMS-EEG の推奨事項、理論論文を突き合わせると、現時点で共通コアに置けるのは <strong>透明な報告</strong>、<strong>forward model と電極幾何の開示</strong>、<strong>外部基準つき妥当化</strong>、<strong>OOD/摂動/棄権の設計</strong> でございます。特定 solver、特定理論、熱力学指標は、条件付きまたは探索トラックとして扱うのが妥当です<sup><a href="#ref-78">[78]</a></sup><sup><a href="#ref-79">[79]</a></sup><sup><a href="#ref-90">[90]</a></sup><sup><a href="#ref-100">[100]</a></sup>。</p>
</div>

<table class="data-table">
<thead>
<tr>
<th>論点</th>
<th>修正前に弱かった点</th>
<th>2026-03 時点で妥当な整理</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG source imaging</strong></td>
<td>アルゴリズム名を前面に出しすぎていました。</td>
<td>コア要件は外部妥当化・不確実性報告・導電率感度分析であり、Block-Champagne 等は有望候補です<sup><a href="#ref-78">[78]</a></sup><sup><a href="#ref-79">[79]</a></sup><sup><a href="#ref-101">[101]</a></sup>。</td>
</tr>
<tr>
<td><strong>Perturbation / PCI</strong></td>
<td>PCI を ground truth に近く書いていました。</td>
<td>PCI/PCI-ST は強い外部 benchmark 候補ですが、TMS-EEG の厳密な刺激・アーチファクト管理が前提で、普遍 KPI ではありません<sup><a href="#ref-90">[90]</a></sup><sup><a href="#ref-100">[100]</a></sup>。</td>
</tr>
<tr>
<td><strong>Active Inference / Counterfactual Equivalence</strong></td>
<td>検証済み中心指標のように読める書き方でした。</td>
<td>現時点では理論駆動の仮説源・モデル族として使い、OOD 一般化、介入、モデル競争で絞る段階です<sup><a href="#ref-76">[76]</a></sup><sup><a href="#ref-80">[80]</a></sup>。</td>
</tr>
<tr>
<td><strong>Criticality / TDA / Irreversibility</strong></td>
<td>コア指標に近い扱いが残っていました。</td>
<td>複雑性や臨界性は promising ですが、現時点では補助解析として提出し、主要判定はより監査しやすい指標束で行います<sup><a href="#ref-52">[52]</a></sup><sup><a href="#ref-56">[56]</a></sup><sup><a href="#ref-92">[92]</a></sup>。</td>
</tr>
</tbody>
</table>

<div class="stage-list">
<div class="stage-item" id="proposal-46">
<div class="stage-number"></div>
<div class="stage-body">
<h4>1. 計測（Sensing）：脳活動の精密な読み取りと不確実性の定量化</h4>
<p>高時間分解能を持つ脳波（EEG）はWBEの有力な入力信号ですが、その空間分解能の低さは根本的な課題です。脳波源推定（ESI）は、この課題を解決する計算論的アプローチですが、これは本質的に解が一意に定まらない<strong>不良設定問題（ill-posed problem）</strong>です<sup><a href="#ref-5">[5]</a></sup>。WBEのような極めて高い信頼性が求められる工学的目標において、従来の最小ノルム法（MNE）やdSPMのような点推定（Point Estimate）に依存することは、推定誤差をシステム全体に伝播させるリスクがあります。</p>
<p>この問題に対して、現時点で固定すべきなのは <strong>solver 名</strong> ではなく <strong>証拠鎖</strong> でございます。経験ベイズ系<sup><a href="#ref-78">[78]</a></sup>や高密度 EEG は有力な改善候補ですが、EEG-BIDS に沿った報告<sup><a href="#ref-26">[26]</a></sup>、電極座標と forward model の開示、導電率不確実性の感度分析<sup><a href="#ref-79">[79]</a></sup>、外部基準つき妥当化が先に満たされなければ、特定手法を「標準」とは呼びません。</p>
<ul
style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;">
<strong>高密度EEGとベイズ推定の位置づけ：</strong>Block-Champagne Framework<sup><a href="#ref-78">[78]</a></sup>、高密度 EEG、個体別 MRI に基づく FEM/BEM フォワードモデルは、推定条件を改善する重要な要素です。ただし、頭蓋骨による空間平滑化と逆問題の非一意性は残るため、センサー密度を上げても source uniqueness は保証されません<sup><a href="#ref-101">[101]</a></sup>。したがって本プロジェクトでは、これらを<strong>保証の根拠</strong>ではなく、<strong>誤差源を狭めるための前提条件</strong>として扱います。
</li>
<li style="margin-bottom: 8px;">
<strong>不確実性の可視化と外部妥当化：</strong>推定された脳活動マップには、振幅だけでなく<strong>「信頼区間（Credible Intervals）」</strong>または事後分布の集中度を併記し、不確実性が高い領域を明示します。さらに、シミュレーション、ファントム、同時侵襲記録、頭蓋内刺激などの外部基準に対して、どの条件でどこまで誤差が減ったかを報告しない限り、「改善した」とは呼びません。
</li>
<li style="margin-bottom: 8px;">
<strong>順問題の不確実性と誤差伝播：</strong>頭部組織（特に頭蓋骨）の導電率や形状の誤差は定位誤差へ直接効くため<sup><a href="#ref-79">[79]</a></sup>、少なくとも感度分析または範囲評価を提出物へ含めます。フル確率モデリングは有力ですが、2026-03 時点では共通必須ではなく、まずは誤差範囲を第三者が監査できることを優先します。
</li>
</ul>
<div class="tag-list" style="margin-top: 12px;">
<span class="tag">External Validation</span>
<span class="tag">Forward Model Audit</span>
<span class="tag">Sensitivity Analysis</span>
<span class="tag">Uncertainty Quantification</span>
</div>
</div>
</div>
<div class="stage-item">
<div class="stage-number"></div>
<div class="stage-body">
<h4>2. 解読（Decoding）：能動的推論と反実仮想的等価性の導入</h4>
<p>「解読」のセクションにおいて、従来のデコーディング技術（Mind Captioning等）は「相関」に基づくマッピングに過ぎません。WBE に近い主張へ進むには、単なる入出力模倣ではなく、未学習条件、介入条件、失敗条件を含む<strong>生成的な予測性能</strong>を示す必要があります。ただし、ここで必要なのは一つの理論を正解として固定することではなく、複数の生成モデルを比較可能な形で並べることでございます。</p>
<p>Laukkonen らの<strong>「反実仮想的等価性（Counterfactual Equivalence）」</strong><sup><a href="#ref-76">[76]</a></sup>や、active inference 系の議論<sup><a href="#ref-80">[80]</a></sup>は、何を test すべきかを設計するうえで有用です。しかし 2026-03 時点では、これ自体が共通の受け入れ基準になったわけではありません。本ページでは、OOD 一般化、摂動応答、校正、棄権、代替モデル報告を束ねる<strong>設計仮説</strong>として扱います。</p>
<ul
style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;">
<strong>能動的推論（Active Inference）の位置づけ：</strong>脳を受動的デコーダーではなく、環境に働きかける生成モデルとして捉える枠組みは有力です<sup><a href="#ref-80">[80]</a></sup>。ただし本プロジェクトでは、これを唯一の実装原理とはせず、DCM、状態空間モデル、SCM を含む <strong>model competition</strong> の一候補として扱います。
</li>
<li style="margin-bottom: 8px;">
<strong>チューリング・テストの拡張（因果的摂動プロトコル）：</strong>静的な反実仮想の検証は不可能であるため、「チューリング・テストを拡張した因果的摂動プロトコル（Causal Perturbation Protocol）」を具体化します。TMS 等による物理的摂動に対する生物学的脳の反応と、エミュレーション上の仮想的摂動に対する反応分布を比較しますが、PCI はその際の <strong>外部 benchmark の一つ</strong> であり、ground truth そのものではありません<sup><a href="#ref-90">[90]</a></sup><sup><a href="#ref-100">[100]</a></sup>。
</li>
</ul>
<div class="tag-list" style="margin-top: 12px;">
<span class="tag">Model Competition</span>
<span class="tag">OOD Generalization</span>
<span class="tag">Perturbation</span>
<span class="tag">Causal Structure</span>
</div>
</div>
</div>
<div class="stage-item">
<div class="stage-number"></div>
<div class="stage-body">
<h4>3. 実装（Implementation）：IIT 4.0 の計算論的限界と代替指標の検討</h4>
<p>本プロジェクトは従来、統合情報理論（IIT 4.0）を主要な理論基盤としてきましたが、その最大の問題である<strong>計算量の爆発（NP困難）</strong>と、デジタル基盤における「内因的実在」の定義の曖昧さに対処する必要があります。IIT を教条的に支持するのではなく、2025 年の<strong>「Adversarial Collaboration」の結果</strong><sup><a href="#ref-54">[54]</a></sup>を踏まえ、<strong>主判定</strong> と <strong>補助解析</strong> を分けた実装指標へ整理します。</p>
<ul
style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;">
<strong>計算可能な近似指標の位置づけ：</strong>Φ（統合情報量）の直接計算はシステム規模に対して指数関数的に困難です。そのため、PCI-ST や低次元埋め込みによる近似手法<sup><a href="#ref-81">[81]</a></sup>は<strong>工学的 proxy</strong>としては有用ですが、意識や同一性の直接代用としては扱いません。
</li>
<li style="margin-bottom: 8px;">
<strong>神経活動多様体の幾何学的比較（Neural Manifold Geometry）：</strong>PCI 等のスカラー値だけでは見えない構造差を拾うため、グラフ指標や TDA、パーシステント・ホモロジーを<strong>補助解析</strong>として導入します。ただし、解釈の一貫性とノイズ安定性はまだ十分標準化されていないため、主要な合否判定はより単純で監査しやすい指標へ置きます。
</li>
<li style="margin-bottom: 8px;">
<strong>熱力学的制約の導入：</strong>計算コストと物理コストを分けて監査する発想は維持しますが、不可逆性や entropy production は現時点では<strong>探索的補助ログ</strong>でございます。粗視化 neural data から得る量を、そのまま微視的散逸や意識の必要条件と同一視してはなりません<sup><a href="#ref-92">[92]</a></sup>。
</li>
</ul>
<div class="tag-list" style="margin-top: 12px;">
<span class="tag">IIT 4.0 Limits</span>
<span class="tag">Evidence Tiers</span>
<span class="tag">Exploratory Metrics</span>
<span class="tag">Resource Audits</span>
</div>
</div>
</div>
</div>
</section>

<!-- Decoding vs Emulation -->
<section class="section" id="decoding-to-emulation-gap">
<h2 class="section-title">デコーディングからエミュレーションへ：論理的ギャップの明示と検証設計</h2>

<div class="note-box">
<strong>TL;DR</strong>
<p>脳活動から文章を「読み出す」デコーディングは強力だが、それは基本的に<strong>観測された結果の翻訳</strong>であり、WBEが要求する<strong>脳ダイナミクスの生成（自律的な因果モデル）</strong>とは別物である<sup><a
href="#ref-8">[8]</a></sup>。このギャップを埋めるには、生成モデル（何が入力で、内部で何が起き、何が出力か）を明示し、介入（摂動）に対する予測で検証する必要がある<sup><a
href="#ref-13">[13]</a></sup><sup><a href="#ref-45">[45]</a></sup>。</p>
</div>

<h3>ギャップの中身（高校生にもわかる言い換え）</h3>
<p>たとえば「テストの答案」を読めても、<strong>その人が普段どう考えているか</strong>（新しい問題にどう対応するか）が再現できるとは限らない。同様に、brain-to-textは「今この瞬間の脳活動」を言葉にできても、WBEが必要とする「環境と相互作用しながら状態を更新し続けるプロセス」まで保証しない。</p>

<div class="visual-diagram diagram-decoding-gap">
  <div class="diagram-side decoding">
    <div class="diagram-icon">🧠</div>
    <div class="arrow-box">Decoding<br><span style="font-size:10px; font-weight:400; opacity:0.8;">(Translation)</span></div>
    <div class="diagram-icon">📝</div>
    <p class="diagram-caption">Output: Text/Media<br>(Static)</p>
  </div>
  <div class="diagram-divider">VS</div>
  <div class="diagram-side emulation">
    <div class="diagram-icon">🧠</div>
    <div class="arrow-box active">Emulation<br><span style="font-size:10px; font-weight:400; opacity:0.8;">(Causal Model)</span></div>
    <div class="diagram-icon">⚙️</div>
    <p class="diagram-caption">Output: Dynamics<br>(Process)</p>
  </div>
</div>

<h3>学術的に問題になるポイント（何を追加で示すべきか）</h3>
<ul style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;">
<strong>相関（decode）と生成（emulate）の違い：</strong>Mind Captioning<sup><a
href="#ref-11">[11]</a></sup>や連続言語復元<sup><a href="#ref-30">[30]</a></sup>は、脳信号から意味・文章を再構成できることを示した。しかしWBEは、同じ入力（感覚）を与えたときに内部状態がどう遷移し、将来の出力（行動・思考・自己モデル）がどう生成されるか、という因果過程そのものの再現を要求する<sup><a
href="#ref-8">[8]</a></sup>。
</li>
<li style="margin-bottom: 8px;">
<strong>言語事前分布（LLM）が勝ってしまう問題：</strong>LLMは流暢さゆえに、根拠が弱いときほど「それっぽい文章」を作れてしまう（hallucination）<sup><a
href="#ref-28">[28]</a></sup>。したがって、脳信号の情報量がどれだけ出力に寄与したかを、反事実入力（シャッフル等）でベースライン化し、棄権（abstention）設計を先に定義する必要がある（本ページのLLM節を参照）。
</li>
<li style="margin-bottom: 8px;">
<strong>多対一（同じ観測を説明する別モデル）の問題：</strong>EEG源推定が不良設定問題であるのと同様に<sup><a
href="#ref-5">[5]</a></sup>、「観測されたデータに合う説明」は複数あり得る。IITでも定義上の非一意性が議論されている<sup><a
href="#ref-3">[3]</a></sup>。WBEでは、<strong>観測一致だけでなく介入予測</strong>でモデルを絞り込む必要がある。
</li>
<li style="margin-bottom: 8px;">
<strong>意識・本人性の保存の検証：</strong>本人性を心理的連続性で捉える立場は、コピー問題（多重性）を含む<sup><a
href="#ref-4">[4]</a></sup><sup><a href="#ref-58">[58]</a></sup>。Slow Continuous Mind Uploading<sup><a
href="#ref-59">[59]</a></sup>のような「連続的移行」仮説を採る場合でも、少なくとも行動非依存の指標（PCI系）で「意識能力」が保存されるかを監査する必要がある<sup><a
href="#ref-47">[47]</a></sup>。
</li>
</ul>

<h3>ギャップを埋める実証プラン（最低限）</h3>
<ol style="margin: 0; padding-left: 20px; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;"><strong>生成モデルを明示する：</strong>DCMなどで、何が状態で何がパラメータかを明確化し、モデル比較可能な形で提示する<sup><a
href="#ref-13">[13]</a></sup>。</li>
<li style="margin-bottom: 8px;"><strong>介入（摂動）予測を事前登録する：</strong>PCI/PCI-STのように、摂動に対する反応の伝播・複雑性を評価軸に組み込む<sup><a
href="#ref-47">[47]</a></sup><sup><a href="#ref-51">[51]</a></sup>。</li>
<li style="margin-bottom: 8px;"><strong>反事実ベースラインを必須化する：</strong>入力シャッフル・試行入れ替え・モデルの温度固定などで、言語事前分布だけで出る出力を定量化し、効果量として報告する<sup><a
href="#ref-28">[28]</a></sup>。</li>
</ol>

<h3>因果構造・状態完全性・物理制約の検証境界（2026-03 監査で更新）</h3>
<p>上記の実証プランを具体化するにあたり、GitHub Issues #64–#70 で出た論点は、「何を共通必須にし、何を探索トラックに残すか」を分けて整理するのが妥当でございます。強い主張ほど、推定器依存性と coarse-graining の影響を先に明示いたします。</p>

<ol style="margin: 0; padding-left: 20px; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 12px;">
<strong>DCMの適用限界と対策：</strong>EEG-based Dynamic Causal Modelling（DCM）はモデル同定可能性（model identifiability）の問題を内在します。特に、EEG の空間分解能制約下では、類似した観測データを生成する複数のモデルが存在し得ます。この問題に対し、Bayesian Model Reduction（BMR; Friston &amp; Penny, 2011）によるモデル空間の効率的探索と、Causal Fingerprinting（Frässle et al., 2021）<sup><a href="#ref-96">[96]</a></sup>による test-retest 信頼性の定量化を優先します。Regression DCM は従来の DCM に比べ、計算コストを抑えつつモデル比較の精度を維持できるため、大規模データへのスケーラビリティ確保に有用です。
</li>
<li style="margin-bottom: 12px;">
<strong>因果指標は補助指標として扱います：</strong>反事実等価性（counterfactual equivalence）だけでは、エミュレーションの因果的忠実度を十分に評価できません。一方で、Effective Information、Causal Density、Symbolic Transfer Entropy（STE）<sup><a href="#ref-99">[99]</a></sup>は、課題依存性と実装依存性が大きく、単独で universal pass/fail を担えるほど標準化されていません。したがって本プロジェクトでは、これらを<strong>追加解析</strong>として用い、主要判定は事前登録した OOD 条件、摂動応答、不確実性、棄権条件、再テスト信頼性の束で行います。
</li>
<li style="margin-bottom: 12px;">
<strong>connectome は scaffold であって state-complete ではありません：</strong><a href="https://doi.org/10.1038/s41586-024-07558-y">Dorkenwald et al. (2024)</a> による成体ショウジョウバエ全脳 connectome、<a href="https://doi.org/10.1038/s41586-025-08790-w">MICrONS Consortium et al. (2025)</a> による機能計測つき皮質 connectomics、<a href="https://doi.org/10.1038/s41586-025-08805-6">Gamlin et al. (2025)</a> による transcriptomic type ごとの接続差、<a href="https://doi.org/10.1038/s41586-024-07311-5">Cahill et al. (2024)</a> による astrocyte network encoding は、配線図が強い scaffold になることを示しました。しかし同時に、細胞型、シナプス状態、遅延・髄鞘、神経修飾、グリア結合状態が落ちると、配線図だけでは動的再現の十分条件にならないことも示しております。したがって、L2 以上の主張には <strong>state-completeness gate</strong> を設け、欠測時は推定誤差または abstention を明示いたします。
</li>
<li style="margin-bottom: 12px;">
<strong>熱力学指標は探索トラックに下げます：</strong><a href="https://doi.org/10.1073/pnas.2109889118">Lynn et al. (2021)</a> と <a href="https://doi.org/10.1093/cercor/bhac177">de la Fuente et al. (2022)</a> は、粗視化した neural dynamics に不可逆性シグネチャが現れることを示しましたが、Lynn ら自身が扱っている量は microscopic physical dissipation そのものではなく、coarse-grained neural data から得る <strong>information entropy production の lower bound</strong> です。さらに <a href="https://doi.org/10.1038/s41467-025-66669-w">Ishihara &amp; Shimazaki (2025)</a> は、neuronal spiking から time asymmetry を直接安定に評価すること自体がなお難しいと述べています。したがって、EPR / time irreversibility は有望な補助ログではありますが、<strong>同一性要件</strong>や<strong>単独の検証KPI</strong>には昇格させません。
</li>
<li style="margin-bottom: 12px;">
<strong>最低限の証拠鎖を固定します：</strong>L2 以上の主張では、(a) 事前登録した hold-out / OOD 条件、(b) 摂動または外部基準つき妥当化、(c) 不確実性と棄権条件、(d) 代替モデルまたは同値類の報告、(e) 計算コストとハードウェア電力の切り分け、を最低ラインとします。熱力学ログはこの束に<strong>追加で添える補助解析</strong>であり、これだけで強い結論は出しません。
</li>
</ol>

</section>

<!-- Reproducibility -->
<section class="section" id="reproducibility">
<h2 class="section-title">プロジェクトの実体性と再現性 (Substance and Reproducibility)</h2>
<p>「Mind-Upload」というプロジェクト名が示す通り、本研究は計算論的手法に基づいている。しかし、現状のGitHubリポジトリはウェブサイト中心であり、研究プロジェクトとしての実体性・再現性が<strong>第三者に実行可能な形</strong>で十分提示されているとは言い難い。この重大な懸念に応えるため、本プロジェクトでは、データの整理規約としてBIDSおよびEEG-BIDS拡張<sup><a
href="#ref-25">[25]</a></sup><sup><a href="#ref-26">[26]</a></sup>を採用し、解析パイプライン・データスキーマ・実験条件ログを段階的に整備して、ウェブサイトの主張を裏付けるコードベースへ移行する。
</p>
<ul style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;">
<strong>データ処理パイプライン：</strong>BIDS/EEG-BIDS<sup><a href="#ref-25">[25]</a></sup><sup><a
href="#ref-26">[26]</a></sup>準拠の生データから、ESI、DCM解析に至るまでの最小限実行可能な処理スクリプト（Python/MNE-Python,
SPM, FieldTrip等のラッパー）を公開する。
</li>
<li style="margin-bottom: 8px;"><strong>デコーディングモデル：</strong>Mind
Captioningに類するTransformerベースのモデルアーキテクチャ定義と、ダミーデータを用いた学習・推論コードを公開する。</li>
<li style="margin-bottom: 8px;">
<strong>データスキーマの拡充：</strong>`dataset_description.json`に加え、EEGデータの具体的な構造（例：`sub-01/eeg/sub-01_task-rest_eeg.eeg`）や、計測プロトコルを記述した`eeg.json`のスキーマ例を公開し、BIDS標準の形式的遵守から実質的遵守へと移行する。
</li>
</ul>
</section>

<!-- Current Status -->
<section class="section" id="key-technical-challenges">
<h2 class="section-title">主要な技術的課題 (Key Technical Challenges)</h2>

<h3>コネクトームとダイナミクスのギャップ</h3>
<p>図1が示す構造的コネクトーム（神経配線図）の研究は、2024–2025 年に大きく前進しました。<a href="https://doi.org/10.1038/s41586-024-07558-y">Dorkenwald et al. (2024)</a> は成体ショウジョウバエ全脳の wiring diagram を示し、<a href="https://doi.org/10.1038/s41586-025-08790-w">MICrONS Consortium et al. (2025)</a> は同一個体の機能計測と connectomics を結びつけた局所 functional digital twin を提示しました。しかし、ここから直接言えるのは「配線図が強い scaffold になる」という点までであり、「配線図だけで全状態が決まる」という点ではございません。</p>
<p>少なくとも 5 つの状態クラスが残ります。第一に、<a href="https://doi.org/10.1038/s41586-025-08805-6">Gamlin et al. (2025)</a> が示すように、transcriptomic type によって接続モチーフやシナプス特性は系統的に異なります。第二に、シナプスは binary edge ではなく、ultrastructure・放出確率・可塑性履歴を伴います。第三に、遅延と髄鞘は timing state を規定し、同じグラフでも同期や位相を変えます。第四に、神経修飾は <strong>volume transmission</strong><sup><a href="#ref-19">[19]</a></sup> と動的機能結合の再編成<sup><a href="#ref-39">[39]</a></sup>を通じて働き、静的 wiring から一意に読めません。第五に、アストロサイトは広域の neurotransmitter input を network-level state に変換しうることが示されており<sup><a href="#ref-41">[41]</a></sup>、非神経細胞を後付け補正で済ませることはできません。</p>
<p>したがって、脳のエミュレーションは、単なるニューロン接続性（connectome）の再現に留まらず、細胞型、シナプス状態、遅延・髄鞘、神経修飾、グリア結合状態をどこまで取得・推定・棄権するかを第一級の設計変数として扱う必要があります。この静的構造と動的状態のギャップを埋めるには、トランスクリプトーム・コネクトミクス<sup><a href="#ref-33">[33]</a></sup>と、state-completeness gate を通した段階的検証が不可欠でございます。</p>

<!-- Figure: Connectome Progress -->
<div class="figure-box">
<div class="figure-content">
<div class="timeline-visual">
<div class="timeline-item">
<div class="timeline-dot done"></div>
<div class="timeline-label">線虫<br><strong>302</strong> neurons</div>
</div>
<div class="timeline-item">
<div class="timeline-dot done"></div>
<div class="timeline-label">ショウジョウバエ（FlyWire全脳）<br><strong>~139,000</strong> neurons<br><span style="font-size:10px; opacity:0.7;">Dorkenwald et al., Nature 2024</span></div>
</div>
<div class="timeline-item">
<div class="timeline-dot current"></div>
<div class="timeline-label">マウス<br><strong>~71M</strong> neurons</div>
</div>
<div class="timeline-item">
<div class="timeline-dot"></div>
<div class="timeline-label">ヒト<br><strong>~86B</strong> neurons</div>
</div>
</div>
</div>
<p class="figure-label">Figure 1</p>
<p class="figure-caption">コネクトーム研究の進展とスケール。線虫（<em>C.
elegans</em>）では全神経系のコネクトームが整備されつつあり<sup><a href="#ref-20">[20]</a></sup>、ショウジョウバエでは2024年にFlyWireプロジェクトにより成虫全脳コネクトーム（約139,000ニューロン）が完成した（Dorkenwald et al., 2024）<sup><a
href="#ref-21">[21]</a></sup>。一方で、機能的ダイナミクス（状態依存の結合変化）や、シナプス強度・神経修飾・グリアを含む力学の同定は依然課題である。マウスでは皮質の小体積で飽和再構成が達成されているが<sup><a
href="#ref-22">[22]</a></sup>、全脳規模の再構成は現在進行中である。ヒト脳は約860億ニューロンを有する<sup><a
href="#ref-57">[57]</a></sup>。
</p>
</div>

<!-- Figure: Verification Stack -->
<div class="figure-box">
<div class="figure-content">
<div class="flow-visual">
<div class="flow-step">
<div class="flow-title">計測</div>
<div class="flow-sub">HD-EEG / fMRI / MEG<br>品質保証・同期</div>
</div>
<div class="flow-step">
<div class="flow-title">逆問題</div>
<div class="flow-sub">ソース推定 / 不確実性<br>分布として保持</div>
</div>
<div class="flow-step">
<div class="flow-title">因果モデリング</div>
<div class="flow-sub">SCM / 介入設計<br>反実仮想の検証</div>
</div>
<div class="flow-step">
<div class="flow-title">同一性検証</div>
<div class="flow-sub">PCI / 構造保存<br>最小分岐セット</div>
</div>
</div>
</div>
<p class="figure-label">Figure 2</p>
<p class="figure-caption">WBE検証に必要な「計測→再構成→因果→検証」の連鎖。各段階の不確実性は次段階に引き継ぎ、介入により反実仮想的等価性を評価する。</p>
</div>
</section>

<!-- Research Program -->
<section class="section" id="research-program">
<h2 class="section-title">Research Program</h2>

<p>論文化を意識した実証プランでは、計測・解読・実装の各段階を統合的に示す。目標はマルチモーダル計測と神経解読を統合した「本人性維持」評価系の設計と論文化である。加えて、計測段階の柱として、EEGを中心とした<strong>行動非依存の意識指標</strong>（複雑性×摂動応答×臨界性）のロードマップも明示する。
</p>

<!-- Table: Roadmap -->
<table class="data-table">
<thead>
<tr>
<th>Phase</th>
<th>計測/データ</th>
<th>解読/解析</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>HD-EEG/fMRI同時計測セットアップ、再現性データ収集。IHM採用とBIDSメタデータ拡充。</td>
<td>brain-to-text 系で、<strong>brainなし / LMなし / shuffle / OOD / drift / latency</strong> を同時に監査する評価パックを固定し、言語事前分布と神経寄与を分離する。</td>
</tr>
<tr>
<td>2</td>
<td>ESI信号分離とMEGデータの融合。逆問題制約条件の妥当性検証。</td>
<td>Dynamic Causal Modeling (DCM) による部位間因果ダイナミクス解析と生成モデルの同定。</td>
</tr>
<tr>
<td>3</td>
<td>WBA統合フレームワークでの動作検証。非神経細胞（グリア）のモデル化。</td>
<td><strong>神経学的チューリングテスト（Neural Turing Test）</strong>：オリジナルの脳とエミュレーションの「摂動応答（PCI）」の統計的同一性を検証。</td>
</tr>
</tbody>
</table>
</section>

<!-- Brain-to-Text Update -->
<section class="section" id="llm-research-update">
<h2 class="section-title">Brain-to-Textアップデート：言語事前分布、streaming、evidence gate</h2>
<p>2026-03 時点の一次文献が強く示しているのは、「汎用LLM運用論」がそのまま脳解読の核心だ、ということではございません。むしろ重要なのは、<strong>どのモダリティで</strong>、<strong>どの課題で</strong>、<strong>どの一般化条件まで</strong>、<strong>言語事前分布を上回る神経寄与が確認できたか</strong>を切り分けることです。Tang らの non-invasive semantic reconstruction は被験者の協力が学習時にも適用時にも必要でした<sup><a href="#ref-30">[30]</a></sup>。Horikawa らの Mind Captioning は視覚内容の記述生成を前進させましたが<sup><a href="#ref-11">[11]</a></sup>、やはり「通信サブシステムでどこまで意味を復元できるか」の系です。さらに Défossez らの non-invasive speech perception decoding<sup><a href="#ref-106">[106]</a></sup>、d'Ascoli らの単語デコード<sup><a href="#ref-107">[107]</a></sup>、Willett ら / Littlejohn ら / Wairagkar らの invasive speech neuroprosthesis<sup><a href="#ref-108">[108]</a></sup><sup><a href="#ref-109">[109]</a></sup><sup><a href="#ref-110">[110]</a></sup>は、decode の到達点を押し上げました。しかし、ここから直ちに言えるのは <strong>language / communication route の局所的前進</strong>であって、WBE や self-model の再現ではありません。</p>

<div class="note-box">
<strong>2026-03 の site rule</strong>
<p>
この節では、RLHF、RAG、agent 化の一般論を主証拠にしません。主証拠は <strong>brain-to-text / speech neuroprosthesis / neural encoding</strong> の一次文献であり、汎用LLM論文は実装メモに留めます。
</p>
</div>

<h3>証拠階層を 4 つに分ける</h3>
<table class="data-table">
<thead>
<tr>
<th>トラック</th>
<th>一次文献が今支持すること</th>
<th>まだ言えないこと</th>
<th>このサイトでの扱い</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>非侵襲 semantic / caption decoding</strong></td>
<td>Tang らは fMRI から連続言語の意味再構成を示し、Horikawa らは脳活動から視覚内容の記述生成を示しました<sup><a href="#ref-30">[30]</a></sup><sup><a href="#ref-11">[11]</a></sup>。</td>
<td>subject-independent decode、日常対話の streaming、因果的内部状態の再現は示していません。Tang ら自身が、decoder の学習と適用に参加者の協力が必要だと報告しています<sup><a href="#ref-30">[30]</a></sup>。</td>
<td><strong>L1 相当の意味復元</strong></td>
</tr>
<tr>
<td><strong>非侵襲 word / speech decoding</strong></td>
<td>Défossez らは non-invasive 記録から 3 秒音声区間の識別を示し、d'Ascoli らは 723 人規模の単語デコードで、MEG・読字課題・データ量が性能を大きく左右すると示しました<sup><a href="#ref-106">[106]</a></sup><sup><a href="#ref-107">[107]</a></sup>。</td>
<td>open-vocabulary の安定通信、単発試行での高信頼 decode、長期 drift 耐性は示していません。</td>
<td><strong>L1 の強化候補</strong></td>
</tr>
<tr>
<td><strong>侵襲 streaming speech neuroprosthesis</strong></td>
<td>Willett らは 125,000 語語彙で高性能 speech BCI を示し、Littlejohn らは 48 words/min の streaming brain-to-voice、Wairagkar らは約 10 ms の instantaneous voice synthesis を示しました<sup><a href="#ref-108">[108]</a></sup><sup><a href="#ref-109">[109]</a></sup><sup><a href="#ref-110">[110]</a></sup>。</td>
<td>全脳WBE、branch-equivalence、再較正不要の長期安定運用は示していません。ここで実証されたのは communication subsystem の closed loop です。</td>
<td><strong>L2〜L3 の局所 benchmark</strong></td>
</tr>
<tr>
<td><strong>LLM 埋め込みによる neural encoding</strong></td>
<td>Zada らや Goldstein らは、文脈埋め込みや意味関係の表現が自然言語課題中の脳活動を予測しうることを示しました<sup><a href="#ref-111">[111]</a></sup><sup><a href="#ref-112">[112]</a></sup>。</td>
<td>これは thought reading でも decoder でもありません。LLM 埋め込みが脳反応をよく説明しても、それだけで「脳の中身を読んだ」ことにはなりません。</td>
<td><strong>measurement model / encoding benchmark</strong></td>
</tr>
</tbody>
</table>

<h3>最低限必要な評価パック</h3>
<ul style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;"><strong>神経寄与の切り分け：</strong><code>brainなし</code>、<code>time-shuffle</code>、<code>trial-shuffle</code>、<code>LM-only</code>、<code>no-LM</code> を並べ、候補集合からの検索なら candidate set size も明示します。</li>
<li style="margin-bottom: 8px;"><strong>一般化の境界：</strong>held-out 文・held-out story・held-out vocabulary・cross-day・cross-task・cross-subject を分けて報告し、被験者協力や個人適応が必要なら隠さず書きます<sup><a href="#ref-30">[30]</a></sup><sup><a href="#ref-107">[107]</a></sup>。</li>
<li style="margin-bottom: 8px;"><strong>real-time 指標：</strong>streaming を主張するなら、words/min だけでなく <strong>P50/P95/P99 latency</strong>、silence / abstention rate、dropout、recalibration burden、recovery time を出します<sup><a href="#ref-109">[109]</a></sup><sup><a href="#ref-110">[110]</a></sup>。</li>
<li style="margin-bottom: 8px;"><strong>再現ログ：</strong>brain encoder、language model、vocoder、context window、beam width、外部コーパス、prompt、キャリブレーション手順を固定し、モデル更新が評価を跨いだ場合は別 run として扱います。</li>
</ul>

<h3>Mind-Upload 側での運用ルール</h3>
<ol style="margin: 0; padding-left: 20px; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;"><strong>L1 を主張する条件：</strong>LM-only / shuffle baseline を上回る神経寄与を示し、candidate set や評価条件を隠さないこと。</li>
<li style="margin-bottom: 8px;"><strong>L2 を主張する条件：</strong>held-out 条件、cross-day ないし cross-task の一般化、低信頼時の abstention を含むこと。</li>
<li style="margin-bottom: 8px;"><strong>L3 を主張する条件：</strong>streaming log、tail latency、silence / freeze、recalibration burden を提出し、closed-loop の failure mode を公開すること。</li>
<li style="margin-bottom: 8px;"><strong>上位主張への禁止事項：</strong>decode 成功、embedding 類似、会話の自然さを、そのまま emulate / WBE / 本人性保存へ読み替えません。</li>
</ol>

<div class="tag-list" style="margin-top: 12px;">
<span class="tag">Brain-to-Text</span>
<span class="tag">Language Prior</span>
<span class="tag">Streaming BCI</span>
<span class="tag">Abstention</span>
<span class="tag">Drift</span>
</div>
</section>

<!-- EEG Consciousness Roadmap -->
<section class="section" id="eeg-consciousness-roadmap">
<h2 class="section-title">EEGで意識を測る：摂動指標を主軸に、安静時指標を補助で読む</h2>

<p>WBE の「計測」段階で意識関連情報を扱う場合、EEG は有力ですが、単独で「意識がある / ない」を裁定する装置ではありません。現時点の一次文献が強く支持するのは、(a) 摂動応答の複雑性は state-level の benchmark 候補であること、(b) no-report paradigms は report confound を減らす設計条件であること、(c) 安静時複雑性・臨界性は有望だが補助 readout に留まること、(d) 臨床運用では multimodal・multicentre 検証が必要であることです<sup><a href="#ref-47">[47]</a></sup><sup><a href="#ref-51">[51]</a></sup><sup><a href="#ref-52">[52]</a></sup><sup><a href="#ref-100">[100]</a></sup><sup><a href="#ref-102">[102]</a></sup><sup><a href="#ref-103">[103]</a></sup><sup><a href="#ref-104">[104]</a></sup><sup><a href="#ref-105">[105]</a></sup>。したがって本節では、EEG を「単独の意識メータ」ではなく、証拠強度の異なる指標束として扱います。</p>

<div class="note-box">
<strong>この節の site rule</strong><br>
no-report は <strong>confound control</strong>、PCI/PCI-ST は <strong>主 benchmark 候補</strong>、安静時複雑性・臨界性は <strong>補助 / 探索トラック</strong>、臨床主張は <strong>multimodal external validation</strong> が揃うまで繰り上げません。
</div>

<h3>この節で先に固定する4条件</h3>
<ol style="margin: 0; padding-left: 20px; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;"><strong>report confound を先に潰す</strong>：no-report paradigms は意識 readout そのものではなく、知覚と報告後処理を切り分けるための設計条件です<sup><a href="#ref-48">[48]</a></sup><sup><a href="#ref-102">[102]</a></sup><sup><a href="#ref-103">[103]</a></sup>。</li>
<li style="margin-bottom: 8px;"><strong>摂動 benchmark を主軸に置く</strong>：PCI/PCI-ST は altered states や disorders of consciousness をまたぐ有力 benchmark ですが、TMS-EEG の刺激条件とアーチファクト管理が前提です<sup><a href="#ref-47">[47]</a></sup><sup><a href="#ref-51">[51]</a></sup><sup><a href="#ref-100">[100]</a></sup>。</li>
<li style="margin-bottom: 8px;"><strong>安静時指標は外部較正つきで使う</strong>：LZ 複雑性や臨界性は有望ですが、摂動指標や臨床アウトカムと較正しない限り、単独での主判定には使いません<sup><a href="#ref-50">[50]</a></sup><sup><a href="#ref-52">[52]</a></sup><sup><a href="#ref-104">[104]</a></sup>。</li>
<li style="margin-bottom: 8px;"><strong>臨床主張は multimodal で外部妥当化する</strong>：単一指標の見栄えより、行動評価・画像・電気生理を束ねた incremental validity を重視します<sup><a href="#ref-55">[55]</a></sup><sup><a href="#ref-105">[105]</a></sup>。</li>
</ol>

<h3>証拠強度の違う4トラック</h3>
<table class="data-table">
<thead>
<tr>
<th>トラック</th>
<th>一次文献が今支持すること</th>
<th>まだ言えないこと</th>
<th>このサイトでの位置づけ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>PCI / PCI-ST</strong></td>
<td>摂動に対する複雑な応答は、麻酔・睡眠・DoC をまたぐ state-level benchmark 候補になります<sup><a href="#ref-47">[47]</a></sup><sup><a href="#ref-51">[51]</a></sup><sup><a href="#ref-55">[55]</a></sup>。</td>
<td>意識内容、本人性、理論の当否を単独で裁定するものではありません。TMS-EEG の厳密なアーチファクト管理を外すと比較不能になります<sup><a href="#ref-100">[100]</a></sup>。</td>
<td><strong>主 benchmark 候補</strong></td>
</tr>
<tr>
<td><strong>No-report paradigms</strong></td>
<td>visual / auditory の両方で、post-perceptual processing と conscious content の分離に効く設計条件であることが強まりました<sup><a href="#ref-48">[48]</a></sup><sup><a href="#ref-102">[102]</a></sup><sup><a href="#ref-103">[103]</a></sup>。</td>
<td>それ自体が bedside meter になるわけではなく、意識レベルの普遍 readout も自動的には与えません。</td>
<td><strong>confound control</strong></td>
</tr>
<tr>
<td><strong>安静時複雑性 / 臨界性</strong></td>
<td>麻酔に伴う変化や、特定 cohort における PCI との関連は報告されています<sup><a href="#ref-50">[50]</a></sup><sup><a href="#ref-52">[52]</a></sup><sup><a href="#ref-56">[56]</a></sup>。</td>
<td>摂動指標の置換ではありません。MCS では spontaneous marker と evoked marker が解離しうるため、同一視は危険です<sup><a href="#ref-104">[104]</a></sup>。</td>
<td><strong>補助 / 探索トラック</strong></td>
</tr>
<tr>
<td><strong>Multimodal clinical panel</strong></td>
<td>単一指標より、行動評価・EEG・画像・臨床変数を束ねた multicentre モデルの方が診断 / 予後に強い可能性があります<sup><a href="#ref-105">[105]</a></sup>。</td>
<td>まだ「世界標準の単独指標」はなく、施設間差・欠測・測定負荷を含む運用問題が残ります。</td>
<td><strong>deployability gate</strong></td>
</tr>
</tbody>
</table>

<h3>研究の優先順位（A→C）</h3>
<table class="data-table">
<thead>
<tr>
<th>Track</th>
<th>狙い</th>
<th>いま優先する理由</th>
<th>先へ進む条件</th>
</tr>
</thead>
<tbody>
<tr>
<td>A</td>
<td>摂動 benchmark を確立する</td>
<td>現時点で最も検証強度が高く、状態差をまたいだ比較がしやすいからです<sup><a href="#ref-47">[47]</a></sup><sup><a href="#ref-51">[51]</a></sup>。</td>
<td>TMS-EEG / 刺激系のログ、アーチファクト窓、再テスト信頼性を公開すること<sup><a href="#ref-100">[100]</a></sup>。</td>
</tr>
<tr>
<td>B</td>
<td>安静時 proxy を benchmark に較正する</td>
<td>装置負荷を下げられる一方、摂動指標との置換可能性はまだ示されていないからです<sup><a href="#ref-52">[52]</a></sup><sup><a href="#ref-104">[104]</a></sup>。</td>
<td>同一 cohort で PCI / 行動 / 臨床アウトカムとの外部較正を通すこと。</td>
</tr>
<tr>
<td>C</td>
<td>multimodal・multicentre で外部妥当化する</td>
<td>臨床価値は単一 lab の成功ではなく、増分予測力と施設外再現性で決まるからです<sup><a href="#ref-105">[105]</a></sup>。</td>
<td>behaviour-only baseline を上回ること、欠測に頑健であること、校正誤差を公開すること。</td>
</tr>
</tbody>
</table>

<h3>ロードマップ（大学院を想定）</h3>
<div class="stage-list">
<div class="stage-item">
<div class="stage-number"></div>
<div class="stage-body">
<h4>フェーズ0：基盤整備（〜1年）—「測れる」「再現できる」を固める</h4>
<p>EEG解析パイプラインを固定し、安静時指標と report confound 制御を同一データ上で再現できる状態にします。</p>
<ul
style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;">前処理・アーチファクト除去・ログまで含む再現可能な解析（BIDS等）</li>
<li style="margin-bottom: 8px;">公開データで、麻酔/鎮静に伴う<strong>複雑性・スペクトル・結合性</strong>の変化を再現する<sup><a href="#ref-23">[23]</a></sup><sup><a href="#ref-50">[50]</a></sup><sup><a href="#ref-53">[53]</a></sup></li>
<li style="margin-bottom: 8px;">report あり / なし条件を併走できる課題設計にし、visual / auditory の no-report 文献と整合させる<sup><a href="#ref-102">[102]</a></sup><sup><a href="#ref-103">[103]</a></sup></li>
<li style="margin-bottom: 8px;">同一データで LZ 複雑性・臨界性・スペクトル指標の再テスト信頼性を先に点検する</li>
</ul>
<div class="tag-list" style="margin-top: 12px;">
<span class="tag">Reproducible Pipeline</span>
<span class="tag">No-Report</span>
<span class="tag">Spontaneous Metrics</span>
<span class="tag">Reliability</span>
</div>
</div>
</div>

<div class="stage-item">
<div class="stage-number"></div>
<div class="stage-body">
<h4>フェーズ1：摂動 benchmark（1〜2年目相当）—「PCI/PCI-STライン」を監査可能にする</h4>
<p>摂動（TMSや感覚刺激等）に対する応答複雑性を主 benchmark として整備し、state-level comparison を可能にします。</p>
<ul
style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;">理想：TMS-EEG で PCI 系指標を扱い、刺激部位・強度・マスキング・アーチファクト窓まで公開する<sup><a href="#ref-47">[47]</a></sup><sup><a href="#ref-100">[100]</a></sup></li>
<li style="margin-bottom: 8px;">現実解：PCI-ST の思想を他の摂動へ移植する場合も、比較対象と failure mode を先に固定する<sup><a href="#ref-51">[51]</a></sup></li>
</ul>
<div class="tag-list" style="margin-top: 12px;">
<span class="tag">Perturbation</span>
<span class="tag">PCI / PCI-ST</span>
<span class="tag">Artifact Audit</span>
</div>
</div>
</div>

<div class="stage-item">
<div class="stage-number"></div>
<div class="stage-body">
<h4>フェーズ2：安静時 proxy の較正（2〜3年目相当）—「摂動なし」は代替ではなく補助として詰める</h4>
<p>安静時 EEG の複雑性や臨界性を、摂動指標・行動・臨床アウトカムに対して外部較正します。目的は PCI の置換ではなく、どこまで proxy として使えるかを定量化することです。</p>
<p style="margin-top: 8px;">Maschke らは麻酔誘導下で臨界性指標と PCI の関連を示しましたが<sup><a href="#ref-52">[52]</a></sup>、Adam らは MCS で spontaneous marker と evoked marker が解離しうることを報告しています<sup><a href="#ref-104">[104]</a></sup>。したがって、「摂動なしで十分」とは書かず、condition-specific な proxy 性能を監査します。</p>
<div class="tag-list" style="margin-top: 12px;">
<span class="tag">Resting-State EEG</span>
<span class="tag">Critical Dynamics</span>
<span class="tag">External Calibration</span>
</div>
</div>
</div>

<div class="stage-item">
<div class="stage-number"></div>
<div class="stage-body">
<h4>フェーズ3：外部妥当化（3〜4年目相当）—「単独指標」ではなく multimodal gain を示す</h4>
<p>最終段階では、EEG 指標を behaviour / imaging / clinical variables と束ね、診断・予後・欠測耐性の観点で incremental validity を評価します。</p>
<ul
style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;">単一指標の AUC ではなく、baseline をどれだけ上回るか、校正が保たれるかを報告する<sup><a href="#ref-105">[105]</a></sup></li>
<li style="margin-bottom: 8px;">施設差・測定負荷・欠測を含めて、deployability を評価する</li>
</ul>
<div class="tag-list" style="margin-top: 12px;">
<span class="tag">Multimodal</span>
<span class="tag">Calibration</span>
<span class="tag">External Validation</span>
</div>
</div>
</div>
</div>

<div class="resolution-box">
<h5>直近1〜3か月のToDo（最小で効く順）</h5>
<ul
style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 13px; line-height: 1.5; color: #d7e2cf;">
<li style="margin-bottom: 6px;">解析パイプラインとログ schema を固定し、安静時指標の再テスト信頼性を先に出す</li>
<li style="margin-bottom: 6px;">report あり / なし条件を visual / auditory の no-report 文献と対応づけて設計する<sup><a href="#ref-102">[102]</a></sup><sup><a href="#ref-103">[103]</a></sup></li>
<li style="margin-bottom: 6px;">公開データで、麻酔/鎮静に伴う変化を一度再現する<sup><a href="#ref-50">[50]</a></sup><sup><a href="#ref-52">[52]</a></sup></li>
<li style="margin-bottom: 6px;">摂動導入の可否に応じて、PCI/PCI-ST 路線の刺激ログとアーチファクト窓を事前登録する<sup><a href="#ref-51">[51]</a></sup><sup><a href="#ref-100">[100]</a></sup></li>
<li>安静時 proxy を bedside meter と誤読しないよう、multimodal validation の公開指標を先に決める<sup><a href="#ref-105">[105]</a></sup></li>
</ul>
</div>

<h3>技術的立ち位置と到達目標</h3>
<p>本ロードマップは、特定の意識理論の正しさを証明することではなく、摂動指標・no-report 制御・安静時 proxy・multimodal 臨床評価を、同じ監査スキーマで比較可能にすることを目指します。Ferrante らの adversarial test が示したのは「単一理論への収束」ではなく、理論と課題設計を分けて監査すべきだという点です<sup><a href="#ref-54">[54]</a></sup>。</p>
<p>したがって本節の到達目標は、「世界標準の単独意識メータ」を宣言することではありません。Ferreiro らの multicentre 研究が示す通り、診断・予後は behaviour 単独より multimodal 統合で改善しうる一方、各指標は互いに代替ではありません<sup><a href="#ref-105">[105]</a></sup>。本サイトが目指す成果は、事前登録・外部妥当化・校正・棄権を含む公開 benchmark を積み上げることです。</p>
</section>

<!-- Technical Proposals -->
<section class="section" id="technical-proposals">
<h2 class="section-title">Technical Proposals</h2>
<p>研究ロードマップを支える具体的な技術提案です。ここでは提案内容を本文に統合し、エビデンスと実装の焦点を一望できるように整理しています。</p>

<div class="stage-list">
<div class="stage-item">
<div class="stage-number">46</div>
<div class="stage-body">
<h4>計測QA・同期・BIDS準拠の統合</h4>
<p>計測品質の可視化（インピーダンス/ノイズフロア/CMRR）と同期の標準化を、BIDS-EEGのメタデータ構造に直接結び付ける。EEG-BIDSは <code>dataset_description.json</code> や <code>eeg.json</code>、<code>channels.tsv</code>、<code>electrodes.tsv</code> 等の明示的メタデータを要求し、再現性・可搬性を担保する枠組みを提供する。</p>
<ul>
<li>BIDS-EEGの構造・必須メタデータをQAログと連携し、再現可能な「計測の証跡」を残す<sup><a href="#ref-83">[83]</a></sup></li>
<li>マルチモーダル同期はLSLのサンプルタイムスタンプとジッタ補正を標準に据える<sup><a href="#ref-84">[84]</a></sup></li>
</ul>
<p><a href="issue.html#proposal-integration">→ 提案状態と外部依存の整理は貢献ガイドへ</a></p>
</div>
</div>

<div class="stage-item" id="proposal-47">
<div class="stage-number">47</div>
<div class="stage-body">
<h4>前処理の再現性強化とネットワーク指標</h4>
<p>ノイズ除去と接続性推定の「再現性」を担保することが重点。ASRの自動除去とZapLineの線雑音抑制を組み合わせ、wPLI/STEで体積伝導・方向性の問題に対処する。</p>
<ul>
<li>ASRは自動アーティファクト除去手法として評価が進んでおり、パラメータ範囲の指針が示されている<sup><a href="#ref-85">[85]</a></sup></li>
<li>ZapLineは線雑音除去のための実証済み手法で、EEG/MEGに適用可能<sup><a href="#ref-86">[86]</a></sup></li>
<li>wPLIは体積伝導とノイズの影響を抑えた位相同期指標<sup><a href="#ref-87">[87]</a></sup>、STEは方向性情報流の推定に有効<sup><a href="#ref-88">[88]</a></sup></li>
</ul>
<p><a href="issue.html#proposal-integration">→ 提案状態と外部依存の整理は貢献ガイドへ</a></p>
</div>
</div>

<div class="stage-item" id="proposal-48">
<div class="stage-number">48</div>
<div class="stage-body">
<h4>神経工学的拡張（OPM-MEG / Hyper-scanning）</h4>
<p>OPM-MEGの可搬性と動作自由度は、VRや自然行動下の計測を現実的にする。ウェアラブルMEGの実証は「動きながらの高時間分解能計測」を研究パイプラインに組み込む根拠となる。</p>
<ul>
<li>ウェアラブルMEGの実証により、自然な動きを伴う計測が可能になった<sup><a href="#ref-89">[89]</a></sup></li>
</ul>
<p><a href="issue.html#proposal-integration">→ 提案状態と外部依存の整理は貢献ガイドへ</a></p>
</div>
</div>

<div class="stage-item" id="proposal-56">
<div class="stage-number">56</div>
<div class="stage-body">
<h4>識別可能性と因果介入（PCI / do-calculus）</h4>
<p>反実仮想の検証は観測だけでは不可能であり、介入データが必要です。PCI（TMS-EEG に基づく摂動複雑性）は、そのときに使える<strong>外部 benchmark の一つ</strong>ですが、ground truth そのものではありません。刺激部位、強度、聴覚マスキング、筋電・刺激アーチファクト窓などの TMS-EEG 推奨事項を満たした場合に限り、介入に対する応答分布の比較基準として用います<sup><a href="#ref-90">[90]</a></sup><sup><a href="#ref-100">[100]</a></sup>。</p>
<ul>
<li>因果階層は「観測・介入・反実仮想」の3層で構成される<sup><a href="#ref-91">[91]</a></sup></li>
<li>PCIはTMS-EEG応答の複雑性を用いた意識指標として提案されているが、OOD 条件、校正、棄権条件と併用して読む必要があります<sup><a href="#ref-90">[90]</a></sup></li>
</ul>
<p><a href="issue.html#proposal-integration">→ 提案状態と外部依存の整理は貢献ガイドへ</a></p>
</div>
</div>

<div class="stage-item" id="proposal-58">
<div class="stage-number">58</div>
<div class="stage-body">
<h4>熱力学・因果・IIT計算量のギャップ対応</h4>
<p>「論理的コスト」だけでは不十分で、計算コストと物理コストを分けて監査する必要があります。ただし、不可逆性や EPR は現時点では探索的補助ログに留め、IIT や EPR を共通必須 KPI にしません。主判定は、摂動、OOD、妥当化、棄権条件の束で行います。</p>
<ul>
<li>非平衡系のエントロピー生成は不可逆性の定量指標として確立されている<sup><a href="#ref-92">[92]</a></sup></li>
<li>IITのMIP探索は系のサイズに対して指数的コストがかかるため、近似や計算戦略が必須<sup><a href="#ref-93">[93]</a></sup></li>
</ul>
<p><a href="issue.html#proposal-integration">→ 提案状態と外部依存の整理は貢献ガイドへ</a></p>
</div>
</div>

<div class="stage-item" id="proposal-61">
<div class="stage-number">61</div>
<div class="stage-body">
<h4>因果・熱力学の論理ギャップ補強</h4>
<p>因果構造保存の監査を主軸に置き、必要な場合のみ不可逆性ログを補助的に添えます。EPR<sup><a href="#ref-92">[92]</a></sup> は coarse-grained neural dynamics の探索的シグナルとして扱い、同一性要件には昇格させません。</p>
<p><a href="issue.html#proposal-integration">→ 提案状態と外部依存の整理は貢献ガイドへ</a></p>
</div>
</div>

<div class="stage-item" id="proposal-62">
<div class="stage-number">62</div>
<div class="stage-body">
<h4>熱力学的・因果的妥当性の強化</h4>
<p>PCI<sup><a href="#ref-90">[90]</a></sup> と SCM<sup><a href="#ref-91">[91]</a></sup> を主軸に、必要なら不可逆性ログと電力・通信ログを補助的に添えます。反実仮想と散逸の両方を見る発想は維持しますが、EPR<sup><a href="#ref-92">[92]</a></sup> を単独の合否指標には使いません。</p>
<p><a href="issue.html#proposal-integration">→ 提案状態と外部依存の整理は貢献ガイドへ</a></p>
</div>
</div>
</div>
</section>

<!-- Limitations -->
<section class="section" id="limitations">
<h2 class="section-title">Limitations and Epistemic Humility</h2>

<div class="note-box">
<strong>このページの限界を明示する</strong>
<p>
研究ノートとして、以下の構造的限界を認識し明記します。これらは「弱点」ではなく、科学的誠実さの要件です。
</p>
</div>

<h3>理論的限界</h3>
<ul style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;"><strong>ハードプロブレムの回避：</strong>本ページは機能的等価性を操作的定義として採用するが、現象的意識（phenomenal consciousness）の同一性は検証対象外である。機能的に完全なエミュレーションが「意識を持つ」ことの十分条件であるかは、本プロジェクトの枠組みでは判定不能である（Chalmers, 1995）。</li>
<li style="margin-bottom: 8px;"><strong>理論的中立性の限界：</strong>「理論に依存しない」と宣言しつつも、PCI等の指標選択自体がIIT寄りの暗黙的前提を含む可能性がある。この潜在的バイアスを完全に排除することはできない。</li>
<li style="margin-bottom: 8px;"><strong>FEPの反証可能性：</strong>自由エネルギー原理は包括的すぎて反証不可能との批判がある。本プロジェクトはFEPを「実装原理」として採用するが、その妥当性は経験的成果で別途検証する必要がある。</li>
<li style="margin-bottom: 8px;"><strong>Unfolding Argumentの含意：</strong>Doerig et al. (2019)<sup><a href="#ref-40">[40]</a></sup>の議論が正しければ、デジタルエミュレーションではIITの意味での意識（Φ>0）は原理的に生じない。ニューロモルフィック基盤への移行は必須となるが、その工学的実現可能性は未検証である。</li>
</ul>

<h3>工学的限界</h3>
<ul style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;"><strong>計測−再現ギャップ：</strong>非侵襲EEG（空間解像度~1-2cm）とWBEが要求する詳細度（シナプスレベル~nm）の間には約7桁のギャップがある。逆問題の不良設定性は原理的に解消されない。</li>
<li style="margin-bottom: 8px;"><strong>再現性の現状：</strong>本プロジェクトが掲げるL0（第三者再現可能性）は、現時点では達成されていない。リポジトリは主にウェブサイトコンテンツであり、実行可能なコード・データ・環境情報は未公開である。</li>
<li style="margin-bottom: 8px;"><strong>コネクトーム-ダイナミクスギャップの深刻さ：</strong>FlyWire（2024）やC. elegans（2019）のコネクトームが完成しても、それだけでは行動の予測に不十分であることが示されている。構造から機能への変換は、WBEの中核的未解決問題である。</li>
</ul>

<h3>プロジェクト運営の限界</h3>
<ul style="margin: 0; padding-left: 20px; list-style-type: disc; font-size: 14px; line-height: 1.6;">
<li style="margin-bottom: 8px;"><strong>個人プロジェクト：</strong>現時点では個人の研究ノートであり、ピアレビューを受けた研究ではない。外部検証と共同研究の拡大が必要である。</li>
<li style="margin-bottom: 8px;"><strong>設計と実装の乖離：</strong>本ページに記述された設計方針の多くは文書レベルに留まり、実装コード・テストデータ・評価結果として公開されていない。</li>
</ul>
</section>

<!-- About -->
<section class="section" id="about">
<h2 class="section-title">About</h2>
<p><strong>中田 康史 (Yasufumi Nakata)</strong><br>
慶應義塾大学 環境情報学部 / 青山敦研究室 所属。<br>
本サイトはマインドアップロード研究に関する公開研究ノートです。</p>
</section>

<!-- References -->
<section class="section references" id="references">
<h2 class="section-title">References</h2>
<ol>
<li id="ref-1" value="1">Fleming, S. M., et al. (2023). Open letter regarding "The integrated information
theory of consciousness". <em>Neuroscience of Consciousness</em>, 2023(1), niad001. <a
href="https://doi.org/10.31234/osf.io/zsr78">doi:10.31234/osf.io/zsr78</a></li>
<li id="ref-2" value="2">Tononi, G., et al. (2016). Integrated information theory: from consciousness to its
physical substrate. <em>Nat. Rev. Neurosci.</em>, 17, 450–461. <a
href="https://doi.org/10.1038/nrn.2016.44">doi:10.1038/nrn.2016.44</a></li>
<li id="ref-3" value="3">Hanson, J. R. (2023). On the non-uniqueness problem in integrated information theory.
<em>Neuroscience of Consciousness</em>, 2023(1), niad014. <a
href="https://doi.org/10.1093/nc/niad014">doi:10.1093/nc/niad014</a>
</li>
<li id="ref-4" value="4">Parfit, D. (1984). <em>Reasons and Persons</em>. Oxford University Press.</li>
<li id="ref-5" value="5">Michel, C. M., & Brunet, D. (2019). EEG source imaging: a practical review of the
methodology. <em>Frontiers in Neurology</em>, 10, 325. <a
href="https://doi.org/10.3389/fneur.2019.00325">doi:10.3389/fneur.2019.00325</a></li>
<li id="ref-6" value="6">Koch, C., Massimini, M., Boly, M., & Tononi, G. (2016). Neural correlates of consciousness: Progress and
problems. <em>Nature Reviews Neuroscience</em>, 17(5), 307–321. <a
href="https://doi.org/10.1038/nrn.2016.22">doi:10.1038/nrn.2016.22</a></li>
<li id="ref-7" value="7">Yamakawa, H., et al. (2024). Technology roadmap toward the completion of whole-brain
architecture with BRA-driven development. <em>Cognitive Systems Research</em>, 88, 101300. <a
href="https://doi.org/10.1016/j.cogsys.2024.101300">doi:10.1016/j.cogsys.2024.101300</a>
</li>
<li id="ref-8" value="8">Sandberg, A., & Bostrom, N. (2008). <em>Whole Brain Emulation: A Roadmap</em>. Future
of Humanity Institute, Oxford University. <a
href="https://www.philosophyofbrains.com/wp-content/uploads/2013/08/2008-3.pdf">Link</a>
</li>
<li id="ref-9" value="9">Logothetis, N. K. (2008). What we can do and what we cannot do with fMRI.
<em>Nature</em>, 453(7197), 869-878. <a
href="https://doi.org/10.1038/nature06976">doi:10.1038/nature06976</a>
</li>
<li id="ref-10" value="10">Yuste, R., et al. (2017). Four ethical priorities for neurotechnologies and AI.
<em>Nature</em>, 551(7679), 159-163. <a
href="https://doi.org/10.1038/551159a">doi:10.1038/551159a</a>
</li>
<li id="ref-11" value="11">Horikawa, T., et al. (2025). Mind captioning: Evolving descriptive text of mental
content from human brain activity. <em>Science Advances</em>, 11(45), eadw1464. <a
href="https://doi.org/10.1126/sciadv.adw1464">doi:10.1126/sciadv.adw1464</a></li>
<li id="ref-12" value="12">Kozlov, M. (2025). 'Mind-captioning' AI decodes brain activity to turn thoughts into
text. <em>Nature</em>, 647(8089), 297. <a
href="https://doi.org/10.1038/d41586-025-03624-1">doi:10.1038/d41586-025-03624-1</a>
(Note: ニュース記事。一次研究は[11]を参照)</li>
<li id="ref-13" value="13">Friston, K. J., Harrison, L., & Penny, W. (2003). Dynamic causal modelling.
<em>NeuroImage</em>, 19(4), 1177-1202. <a
href="https://doi.org/10.1016/S1053-8119(03)00202-7">doi:10.1016/S1053-8119(03)00202-7</a>
</li>
<li id="ref-14" value="14">Friston, K. (2010). The free-energy principle: a rough guide to the brain.
<em>Nature Reviews Neuroscience</em>, 11(2), 127–138. <a
href="https://doi.org/10.1038/nrn2787">doi:10.1038/nrn2787</a>
</li>
<li id="ref-15" value="15">Vorwerk, J., et al. (2014). A guideline for head volume conductor modeling in EEG and MEG.
<em>NeuroImage</em>, 100, 590–607. <a
href="https://doi.org/10.1016/j.neuroimage.2014.06.040">doi:10.1016/j.neuroimage.2014.06.040</a></li>
<li id="ref-16" value="16">Markram, H. (2006). The Blue Brain Project. <em>Nature Reviews Neuroscience</em>,
7(2), 153-160. <a href="https://doi.org/10.1038/nrn1860">doi:10.1038/nrn1860</a></li>
<li id="ref-17" value="17">Albantakis, L., et al. (2023). Integrated information theory (IIT) 4.0: Formulating
the properties of phenomenal existence in physical terms. <em>PLOS Computational Biology</em>,
19(10), e1011465. <a
href="https://doi.org/10.1371/journal.pcbi.1011465">doi:10.1371/journal.pcbi.1011465</a>
</li>
<li id="ref-18" value="18">Wipf, D., & Nagarajan, S. (2009). A unified Bayesian framework for MEG/EEG source imaging.
<em>NeuroImage</em>, 44(3), 947–966. <a
href="https://doi.org/10.1016/j.neuroimage.2008.02.059">doi:10.1016/j.neuroimage.2008.02.059</a></li>
<li id="ref-19" value="19">Özçete, Ö. D., et al. (2024). Mechanisms of neuromodulatory volume transmission.
<em>Molecular Psychiatry</em>. <a href="https://doi.org/10.1038/s41380-024-02608-3">doi:10.1038/s41380-024-02608-3</a></li>
<li id="ref-20" value="20">Cook, S. J., et al. (2019). Whole-animal connectomes of both <em>Caenorhabditis elegans</em> sexes.
<em>Nature</em>, 571(7763), 63–71. <a href="https://doi.org/10.1038/s41586-019-1352-7">doi:10.1038/s41586-019-1352-7</a></li>
<li id="ref-21" value="21">Scheffer, L. K., et al. (2020). A connectome and analysis of the adult <em>Drosophila</em> central
brain. <em>eLife</em>, 9. <a href="https://doi.org/10.7554/eLife.57443">doi:10.7554/eLife.57443</a></li>
<li id="ref-22" value="22">Kasthuri, N., et al. (2015). Saturated reconstruction of a volume of neocortex.
<em>Cell</em>, 162(3), 648–661. <a href="https://doi.org/10.1016/j.cell.2015.06.054">doi:10.1016/j.cell.2015.06.054</a></li>
<li id="ref-23" value="23">Purdon, P. L., et al. (2013). Electroencephalogram signatures of loss and recovery of consciousness from
propofol. <em>PNAS</em>, 110(12), E1142–E1151. <a href="https://doi.org/10.1073/pnas.1221180110">doi:10.1073/pnas.1221180110</a></li>
<li id="ref-24" value="24">Schumer, C., et al. (2025). <em>Management of Individuals' Neural Data (MIND) Act of
2025</em>. U.S. Senate Bill. (Note: Proposed bill as of Jan 12, 2026).</li>
<li id="ref-25" value="25">Gorgolewski, K. J., et al. (2016). The brain imaging data structure, a format for organizing and
describing outputs of neuroimaging experiments. <em>Scientific Data</em>, 3. <a
href="https://doi.org/10.1038/sdata.2016.44">doi:10.1038/sdata.2016.44</a></li>
<li id="ref-26" value="26">Pernet, C. R., et al. (2019). EEG-BIDS, an extension to the brain imaging data structure for
electroencephalography. <em>Scientific Data</em>, 6(1). <a
href="https://doi.org/10.1038/s41597-019-0104-8">doi:10.1038/s41597-019-0104-8</a></li>
<li id="ref-27" value="27">Ienca, M., & Andorno, R. (2017). Towards new human rights in neuroscience. <em>Life
Sciences, Society and Policy</em>, 13(1), 5. <a
href="https://doi.org/10.1186/s40504-017-0050-1">doi:10.1186/s40504-017-0050-1</a></li>
<li id="ref-28" value="28">Ji, Z., et al. (2023). Survey of Hallucination in Natural Language Generation. <em>ACM Computing
Surveys</em>, 55(12). <a href="https://doi.org/10.1145/3571730">doi:10.1145/3571730</a></li>
<li id="ref-29" value="29">Huth, A. G., et al. (2016). Natural speech reveals the semantic maps that tile human cerebral cortex.
<em>Nature</em>, 532(7600), 453–458. <a href="https://doi.org/10.1038/nature17637">doi:10.1038/nature17637</a></li>
<li id="ref-30" value="30">Tang, J., et al. (2023). Semantic reconstruction of continuous language from non-invasive brain
recordings. <em>Nature Neuroscience</em>, 26(5), 858–866. <a
href="https://doi.org/10.1038/s41593-023-01304-9">doi:10.1038/s41593-023-01304-9</a></li>
<li id="ref-31" value="31">Boly, M., et al. (2017). Are the neural correlates of consciousness in the front or in the back of the
cerebral cortex? Clinical and neuroimaging evidence. <em>Journal of Neuroscience</em>, 37(40),
9603–9613. <a href="https://doi.org/10.1523/JNEUROSCI.3218-16.2017">doi:10.1523/JNEUROSCI.3218-16.2017</a></li>
<li id="ref-32" value="32">Whitehead, A. N. (1929). <em>Process and Reality: An Essay in Cosmology</em>. Macmillan.
(Note: プロセス哲学の古典。版によって出版年・出版社表記が異なる)</li>
<li id="ref-33" value="33">Gamlin, C. R., et al. (2025). Connectomics of predicted Sst transcriptomic types in mouse visual
cortex. <em>Nature</em>, 640(8058), 497–505. <a
href="https://doi.org/10.1038/s41586-025-08805-6">doi:10.1038/s41586-025-08805-6</a></li>
<li id="ref-39" value="39">Jun, S., Altmann, A., Sadaghiani, S., et al. (2025). Modulatory Neurotransmitter Genotypes Shape Dynamic
Functional Connectome Reconfigurations. <em>Journal of Neuroscience</em>, 45(10). <a
href="https://doi.org/10.1523/JNEUROSCI.1939-24.2025">doi:10.1523/JNEUROSCI.1939-24.2025</a>
(Open Access: <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11884390/">PMC11884390</a>)</li>
<li id="ref-40" value="40">Doerig, A., et al. (2019). The unfolding argument: Why IIT and other causal
structure theories cannot explain consciousness. <em>Consciousness and Cognition</em>, 72, 49–59. <a
href="https://doi.org/10.1016/j.concog.2019.04.002">doi:10.1016/j.concog.2019.04.002</a>
</li>
<li id="ref-41" value="41">Santello, M., et al. (2019). Astrocyte-neuron interactions: from synapses to
networks and behavior. <em>Neuron</em>, 103(6), 985-1000. <a
href="https://doi.org/10.1016/j.neuron.2019.08.024">doi:10.1016/j.neuron.2019.08.024</a>
</li>
<li id="ref-42" value="42">Melloni, L., et al. (2023). An adversarial collaboration protocol for testing
contrasting predictions of global neuronal workspace and integrated information theory. <em>PLoS
ONE</em>, 18(3), e0282855. <a
href="https://doi.org/10.1371/journal.pone.0282855">doi:10.1371/journal.pone.0282855</a>
</li>
<li id="ref-43" value="43">Dehaene, S., Kerszberg, M., & Changeux, J. P. (1998). A neuronal model of a global
workspace in effortful cognitive tasks. <em>Proceedings of the National Academy of
Sciences</em>, 95(24), 14529-14534. <a
href="https://doi.org/10.1073/pnas.95.24.14529">doi:10.1073/pnas.95.24.14529</a></li>
<li id="ref-44" value="44">Tononi, G. (2015). Integrated information theory. <em>Scholarpedia</em>, 10(1),
4164. <a
href="http://www.scholarpedia.org/article/Integrated_information_theory">doi:10.4249/scholarpedia.4164</a>
(Note: IITの内因的実在(Intrinsic Existence)の公理に関する議論については、この総説および[17]を参照)</li>
<li id="ref-45" value="45">Friston, K. (2017). Active inference: a process theory. <em>Neural Computation</em>, 29(1), 1–49. <a
href="https://doi.org/10.1162/NECO_a_00912">doi:10.1162/NECO_a_00912</a></li>
<li id="ref-46" value="46">Parr, T., & Friston, K. J. (2019). Generalised free energy and active inference.
<em>Biological cybernetics</em>, 113(4), 495-513. <a
href="https://doi.org/10.1007/s00422-019-00803-8">doi:10.1007/s00422-019-00803-8</a>
</li>
<li id="ref-47" value="47">Casali, A. G., Gosseries, O., Rosanova, M., Boly, M., Sarasso, S., Casali, K. R.,
... & Massimini, M. (2013). A theoretically based index of consciousness independent of sensory
processing and
behavior. <em>Science Translational Medicine</em>, 5(198), 198ra105. <a
href="https://doi.org/10.1126/scitranslmed.3006294">doi:10.1126/scitranslmed.3006294</a>
</li>
<li id="ref-48" value="48">Tsuchiya, N., et al. (2015). No-Report Paradigms: Extracting the True Neural Correlates of
Consciousness. <em>Trends in Cognitive Sciences</em>, 19(12), 757–770. <a
href="https://doi.org/10.1016/j.tics.2015.10.002">doi:10.1016/j.tics.2015.10.002</a></li>
<li id="ref-49" value="49">Massimini, M., et al. (2005). Breakdown of cortical effective connectivity during sleep.
<em>Science</em>, 309(5744), 2228–2232. <a href="https://doi.org/10.1126/science.1117256">doi:10.1126/science.1117256</a>
(Open Access: <a href="https://air.unimi.it/handle/2434/15471">air.unimi.it</a>)</li>
<li id="ref-50" value="50">Schartner, M., et al. (2015). Complexity of multi-dimensional spontaneous EEG decreases during
propofol induced general anaesthesia. <em>PLOS ONE</em>, 10(8). <a
href="https://doi.org/10.1371/journal.pone.0133532">doi:10.1371/journal.pone.0133532</a>
(Open Access: <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4529106/">PMCID: PMC4529106</a>)</li>
<li id="ref-51" value="51">Comolatti, R., et al. (2019). A fast and general method to empirically estimate the complexity of
brain responses to transcranial and intracranial stimulations. <em>Brain Stimulation</em>, 12(5),
1280–1289. <a href="https://doi.org/10.1016/j.brs.2019.05.013">doi:10.1016/j.brs.2019.05.013</a></li>
<li id="ref-52" value="52">Maschke, C., et al. (2024). Critical dynamics in spontaneous EEG predict anesthetic-induced loss of
consciousness and perturbational complexity. <em>Communications Biology</em>, 7(1). <a
href="https://doi.org/10.1038/s42003-024-06613-8">doi:10.1038/s42003-024-06613-8</a></li>
<li id="ref-53" value="53">Anusha, A. S., et al. (2021). Brain Functional Connectivity as Biomarker for Propofol-Induced
Alterations of Consciousness. <em>Proceedings of the Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC)</em>, 1928–1931. <a
href="https://doi.org/10.1109/EMBC46164.2021.9629617">doi:10.1109/EMBC46164.2021.9629617</a></li>
<li id="ref-54" value="54">Ferrante, O., et al. (2025). Adversarial testing of global neuronal workspace and integrated
information theories of consciousness. <em>Nature</em>, 642(8066), 133–142. <a
href="https://doi.org/10.1038/s41586-025-08888-1">doi:10.1038/s41586-025-08888-1</a></li>
<li id="ref-55" value="55">Sinitsyn, D. O., et al. (2020). Detecting the potential for consciousness in unresponsive patients
using the perturbational complexity index. <em>Brain Sciences</em>, 10(12), 917. <a
href="https://doi.org/10.3390/brainsci10120917">doi:10.3390/brainsci10120917</a></li>
<li id="ref-56" value="56">Shew, W. L., & Plenz, D. (2013). The functional benefits of criticality in the cortex.
<em>The Neuroscientist</em>, 19(1), 88–100. <a
href="https://doi.org/10.1177/1073858412445487">doi:10.1177/1073858412445487</a></li>
<li id="ref-57" value="57">Azevedo, F. A., Carvalho, L. R., Grinberg, L. T., Farfel, J. M., Ferretti, R. E.,
Leite, R. E., ... & Herculano-Houzel, S. (2009). Equal numbers of neuronal and nonneuronal cells
make the human brain an isometrically scaled-up primate brain. <em>Journal of Comparative
Neurology</em>, 513(5), 532-541. <a
href="https://doi.org/10.1002/cne.21974">doi:10.1002/cne.21974</a></li>
<li id="ref-58" value="58">Weber, C. (2025). The multiplicity objection against uploading optimism.
<em>Synthese</em>, 205(6). <a href="https://doi.org/10.1007/s11229-025-05057-9">doi:10.1007/s11229-025-05057-9</a></li>
<li id="ref-59" value="59">Clowes, R. W. (2021). Slow Continuous Mind Uploading. <em>Studies in Brain and Mind</em>, 18,
161–183. <a href="https://doi.org/10.1007/978-3-030-72644-7_8">doi:10.1007/978-3-030-72644-7_8</a></li>
<li id="ref-60" value="60">Vaswani, A., et al. (2017). Attention Is All You Need. <em>Advances in Neural
Information Processing Systems (NeurIPS)</em>. <a
href="https://arxiv.org/abs/1706.03762">arXiv:1706.03762</a></li>
<li id="ref-61" value="61">Ouyang, L., et al. (2022). Training language models to follow instructions with
human feedback. <em>arXiv:2203.02155</em>. <a href="https://arxiv.org/abs/2203.02155">arXiv</a>
</li>
<li id="ref-62" value="62">Rafailov, R., et al. (2023). Direct Preference Optimization: Your Language Model is
Secretly a Reward Model. <em>arXiv:2305.18290</em>. <a
href="https://arxiv.org/abs/2305.18290">arXiv</a></li>
<li id="ref-63" value="63">Dettmers, T., et al. (2023). QLoRA: Efficient Finetuning of Quantized LLMs.
<em>arXiv:2305.14314</em>. <a href="https://arxiv.org/abs/2305.14314">arXiv</a></li>
<li id="ref-64" value="64">Lewis, P., et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP
Tasks. <em>arXiv:2005.11401</em>. <a href="https://arxiv.org/abs/2005.11401">arXiv</a></li>
<li id="ref-65" value="65">Yao, S., et al. (2022). ReAct: Synergizing Reasoning and Acting in Language Models.
<em>arXiv:2210.03629</em>. <a href="https://arxiv.org/abs/2210.03629">arXiv</a></li>
<li id="ref-66" value="66">Schick, T., et al. (2023). Toolformer: Language Models Can Teach Themselves to Use
Tools. <em>arXiv:2302.04761</em>. <a href="https://arxiv.org/abs/2302.04761">arXiv</a></li>
<li id="ref-67" value="67">Manakul, P., et al. (2023). SelfCheckGPT: Zero-Resource Black-Box Hallucination
Detection for Generative Large Language Models. <em>arXiv:2303.08896</em>. <a
href="https://arxiv.org/abs/2303.08896">arXiv</a></li>
<li id="ref-70" value="70">Friston, K. J., et al. (2017). Active inference, mathematical constitution, and pure consciousness. <em>Frontiers in Psychology</em>, 8, 1322.</li>
<li id="ref-71" value="71">Zanichelli, N., et al. (2025). State of Brain Emulation Report 2025. <em>arXiv:2510.15745</em>.</li>
<li id="ref-73" value="73">Koulouri, A. (2025). Bayesian model parameter learning in linear inverse problems. <em>Machine Learning: Science and Technology</em>.</li>
<li id="ref-74" value="74">Nzakuna, P. S., et al. (2025). Monte Carlo-based Strategy for Assessing the Impact of EEG Data Uncertainty. <em>IEEE Transactions on Instrumentation and Measurement</em>.</li>
<li id="ref-76" value="76">Laukkonen, R. E., Friston, K., & Chandaria, S. (2025). A beautiful loop: An active inference theory of consciousness. <em>Neuroscience & Biobehavioral Reviews</em>, 183, 106296. <a href="https://doi.org/10.1016/j.neubiorev.2025.106296">doi:10.1016/j.neubiorev.2025.106296</a></li>
<li id="ref-77" value="77">Clark, A. (2013). The Mark of the Mental: In Search of the Markov Blanket. In: <em>The Mark of the Mental</em>. Oxford University Press.</li>
<li id="ref-78" value="78">Feng, Z., et al. (2025). Block-Champagne: Imaging Extended E/MEG Source Activation with Empirical Bayesian Uncertainty Quantification. <em>IEEE Transactions on Medical Imaging</em>. <a href="https://doi.org/10.1109/TMI.2025.3642620">doi:10.1109/TMI.2025.3642620</a></li>
<li id="ref-79" value="79">Aydin, U., Vorwerk, J., Küpper, P., et al. (2019). Influence of Head Tissue Conductivity Uncertainties on EEG Dipole Reconstruction. <em>Frontiers in Neuroscience</em>, 13, 531. <a href="https://doi.org/10.3389/fnins.2019.00531">doi:10.3389/fnins.2019.00531</a></li>
<li id="ref-80" value="80">Whyte, C. J., Hohwy, J., Baltieri, M., et al. (2025). On the minimal theory of consciousness implicit in active inference. <em>Physics of Life Reviews</em>. <a href="https://doi.org/10.1016/j.plrev.2025.11.002">doi:10.1016/j.plrev.2025.11.002</a></li>
<li id="ref-81" value="81">Li, J., et al. (2025). Computational complexity reduction in Integrated Information Theory via low-dimensional embedding. <em>Chaos, Solitons & Fractals</em>.</li>
<li id="ref-82" value="82">Cai, C., et al. (2021). Robust estimation of noise for electromagnetic brain imaging with the Champagne algorithm. <em>NeuroImage</em>.</li>
<li id="ref-83" value="83">Pernet, C. R., Appelhoff, S., Gorgolewski, K. J., et al. (2019). EEG-BIDS, an extension to the brain imaging data structure for electroencephalography. <em>Scientific Data</em>, 6, 103. <a href="https://doi.org/10.1038/s41597-019-0104-8">doi:10.1038/s41597-019-0104-8</a></li>
<li id="ref-84" value="84">Kothe, C., Shirazi, S. Y., Stenner, T., et al. (2025). The lab streaming layer for synchronized multimodal recording. <em>Imaging Neuroscience</em>, 3, IMAG.a.136. <a href="https://doi.org/10.1162/IMAG.a.136">doi:10.1162/IMAG.a.136</a></li>
<li id="ref-85" value="85">Chang, C.-Y., Hsu, S.-H., Pion-Tonachini, L., & Jung, T.-P. (2018). Evaluation of Artifact Subspace Reconstruction for automatic EEG artifact removal. <em>Proc. IEEE EMBC</em>. <a href="https://doi.org/10.1109/EMBC.2018.8512547">doi:10.1109/EMBC.2018.8512547</a></li>
<li id="ref-86" value="86">de Cheveigne, A. (2020). ZapLine: A simple and effective method to remove power line artifacts. <em>NeuroImage</em>, 207, 116356. <a href="https://doi.org/10.1016/j.neuroimage.2019.116356">doi:10.1016/j.neuroimage.2019.116356</a></li>
<li id="ref-87" value="87">Vinck, M., Oostenveld, R., van Wingerden, M., Battaglia, F., & Pennartz, C. M. A. (2011). An improved index of phase-synchronization for electrophysiological data in the presence of volume-conduction, noise and sample-size bias. <em>NeuroImage</em>, 55(4), 1548–1565. <a href="https://doi.org/10.1016/j.neuroimage.2011.01.055">doi:10.1016/j.neuroimage.2011.01.055</a></li>
<li id="ref-88" value="88">Staniek, M., & Lehnertz, K. (2008). Symbolic Transfer Entropy. <em>Physical Review Letters</em>, 100, 158101. <a href="https://doi.org/10.1103/PhysRevLett.100.158101">doi:10.1103/PhysRevLett.100.158101</a></li>
<li id="ref-89" value="89">Boto, E., Holmes, N., Leggett, J., et al. (2018). Moving magnetoencephalography towards real-world applications with a wearable system. <em>Nature</em>, 555, 657–661. <a href="https://doi.org/10.1038/nature26147">doi:10.1038/nature26147</a></li>
<li id="ref-90" value="90">Casali, A. G., Gosseries, O., Rosanova, M., et al. (2013). A theoretically based index of consciousness independent of sensory processing and behavior. <em>Science Translational Medicine</em>, 5(198), 198ra105. <a href="https://doi.org/10.1126/scitranslmed.3006294">doi:10.1126/scitranslmed.3006294</a></li>
<li id="ref-91" value="91">Correa, J. D., Lee, S., & Bareinboim, E. (2021). Nested Counterfactual Identification from Arbitrary Surrogate Experiments. <em>arXiv:2107.03190</em>. <a href="https://arxiv.org/abs/2107.03190">arXiv</a></li>
<li id="ref-92" value="92">Seifert, U. (2012). Stochastic thermodynamics, fluctuation theorems and molecular machines. <em>Reports on Progress in Physics</em>, 75(12), 126001. <a href="https://doi.org/10.1088/0034-4885/75/12/126001">doi:10.1088/0034-4885/75/12/126001</a></li>
<li id="ref-93" value="93">Kitazono, J., Kanai, R., & Oizumi, M. (2018). Efficient Algorithms for Searching the Minimum Information Partition in Integrated Information Theory. <em>Entropy</em>, 20(3), 173. <a href="https://doi.org/10.3390/e20030173">doi:10.3390/e20030173</a></li>
<li id="ref-94" value="94">Dorkenwald, S., et al. (2024). Neuronal wiring diagram of an adult brain. <em>Nature</em>, 634, 124–138. <a href="https://doi.org/10.1038/s41586-024-07558-y">doi:10.1038/s41586-024-07558-y</a></li>
<li id="ref-95" value="95">Chalmers, D. J. (1995). Facing up to the problem of consciousness. <em>Journal of Consciousness Studies</em>, 2(3), 200-219.</li>
<li id="ref-96" value="96">Frässle, S., et al. (2021). Regression DCMs for fMRI. <em>NeuroImage</em>, 227, 117566. <a href="https://doi.org/10.1016/j.neuroimage.2020.117566">doi:10.1016/j.neuroimage.2020.117566</a></li>
<li id="ref-97" value="97">Hoel, E., Albantakis, L., & Tononi, G. (2016). Can the macro beat the micro? Integrated information across spatiotemporal scales. <em>Neuroscience</em>, 311, 393–401. <a href="https://doi.org/10.1016/j.neuroscience.2016.09.049">doi:10.1016/j.neuroscience.2016.09.049</a></li>
<li id="ref-98" value="98">Seifert, U. (2012). Stochastic thermodynamics, fluctuation theorems and molecular machines. <em>Reports on Progress in Physics</em>, 75(12), 126001. <a href="https://doi.org/10.1088/0034-4885/75/12/126001">doi:10.1088/0034-4885/75/12/126001</a></li>
<li id="ref-99" value="99">Staniek, M. & Lehnertz, K. (2008). Symbolic Transfer Entropy. <em>Physical Review Letters</em>, 100(15), 158101. <a href="https://doi.org/10.1103/PhysRevLett.100.158101">doi:10.1103/PhysRevLett.100.158101</a></li>
<li id="ref-100" value="100">Hernandez-Pavon, J. C., Metsomaa, J., Mutanen, T. P., et al. (2023). TMS combined with EEG: Recommendations and open issues. <em>Brain Stimulation</em>, 16(2), 350–366. <a href="https://doi.org/10.1016/j.brs.2023.02.009">doi:10.1016/j.brs.2023.02.009</a></li>
<li id="ref-101" value="101">Srinivasan, R., Nunez, P. L., Tucker, D. M., Silberstein, R. B., & Cadusch, P. J. (1996). Spatial sampling and filtering of EEG with spline Laplacians to estimate cortical potentials. <em>Brain Topography</em>, 8(4), 355–366. <a href="https://doi.org/10.1007/BF01186911">doi:10.1007/BF01186911</a></li>
<li id="ref-102" value="102">Cohen, M. A., et al. (2024). Neural signatures of visual awareness independent of postperceptual processing. <em>Cerebral Cortex</em>, 34(11), bhae415. <a href="https://doi.org/10.1093/cercor/bhae415">doi:10.1093/cercor/bhae415</a></li>
<li id="ref-103" value="103">Dellert, T., et al. (2025). Neural correlates of auditory awareness under no-report conditions. <em>Current Biology</em>, 35(12), 2790–2804.e5. <a href="https://doi.org/10.1016/j.cub.2025.03.031">doi:10.1016/j.cub.2025.03.031</a></li>
<li id="ref-104" value="104">Adam, E., et al. (2025). A dissociation between spontaneous and evoked EEG markers of consciousness in the minimally conscious state. <em>Brain</em>, 148(11), 3490–3505. <a href="https://doi.org/10.1093/brain/awaf332">doi:10.1093/brain/awaf332</a></li>
<li id="ref-105" value="105">Ferreiro, D., et al. (2025). Multimodal multicentre investigation of diagnostic and prognostic markers in disorders of consciousness. <em>Brain</em>. <a href="https://doi.org/10.1093/brain/awaf287">doi:10.1093/brain/awaf287</a></li>
<li id="ref-106" value="106">Défossez, A., Caucheteux, C., Rapin, J., Kabeli, O., & King, J.-R. (2023). Decoding speech perception from non-invasive brain recordings. <em>Nature Machine Intelligence</em>, 5, 1097–1107. <a href="https://doi.org/10.1038/s42256-023-00714-5">doi:10.1038/s42256-023-00714-5</a></li>
<li id="ref-107" value="107">d'Ascoli, S., Ferrante, O., et al. (2025). Towards decoding individual words from non-invasive brain recordings. <em>Nature Communications</em>, 16, 1117. <a href="https://doi.org/10.1038/s41467-025-56165-8">doi:10.1038/s41467-025-56165-8</a></li>
<li id="ref-108" value="108">Willett, F. R., Kunz, E. M., Fan, C., et al. (2023). A high-performance speech neuroprosthesis. <em>Nature</em>, 620, 1031–1036. <a href="https://doi.org/10.1038/s41586-023-06377-x">doi:10.1038/s41586-023-06377-x</a></li>
<li id="ref-109" value="109">Littlejohn, K. T., Dabagia, M., Ladwig, A., et al. (2025). A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. <em>Nature Neuroscience</em>, 28, 1711–1719. <a href="https://doi.org/10.1038/s41593-025-01905-6">doi:10.1038/s41593-025-01905-6</a></li>
<li id="ref-110" value="110">Wairagkar, M., Card, N. S., Singer-Clark, T., et al. (2025). An instantaneous voice-synthesis neuroprosthesis. <em>Nature</em>, 644, 145–152. <a href="https://doi.org/10.1038/s41586-025-09127-3">doi:10.1038/s41586-025-09127-3</a></li>
<li id="ref-111" value="111">Zada, Z., Goldstein, A., et al. (2024). Contextual embeddings from deep language models predict fMRI responses to naturalistic language. <em>Neuron</em>, 112(22), 3725–3740.e9. <a href="https://doi.org/10.1016/j.neuron.2024.09.018">doi:10.1016/j.neuron.2024.09.018</a></li>
<li id="ref-112" value="112">Goldstein, A., Bar, A., et al. (2025). Connecting concepts in the brain by mapping cortical representations of semantic relations. <em>Nature Neuroscience</em>, 28, 1841–1848. <a href="https://doi.org/10.1038/s41593-025-01903-8">doi:10.1038/s41593-025-01903-8</a></li>
</ol>
</section>

</article>

<!-- Sidebar -->
<aside class="sidebar-column">

<div class="sidebar-box">
<h4>Start Here</h4>
<ul>
<li><a href="verification.html">検証基盤（Verification Commons）→</a></li>
<li><a href="verification.html#casework">ケースワーク（歴史の型）→</a></li>
<li><a href="tech_roadmap.html#definition">前進の定義（Roadmap）→</a></li>
<li><a href="perspective.html#design-principles">理論フレーム節（Framework）→</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Contents</h4>
<ul>
<li><a href="#introduction">Introduction</a></li>
<li><a href="#technical-framework">Technical Framework</a></li>
<li><a href="#decoding-to-emulation-gap">Decoding → Emulation</a></li>
<li><a href="#reproducibility">Reproducibility</a></li>
<li><a href="#key-technical-challenges">Key Technical Challenges</a></li>
<li><a href="#research-program">Research Program</a></li>
<li><a href="#llm-research-update">Brain-to-Text Update</a></li>
<li><a href="#eeg-consciousness-roadmap">EEG Consciousness Roadmap</a></li>
<li><a href="#technical-proposals">Technical Proposals</a></li>
<li><a href="#about">About</a></li>
<li><a href="#references">References</a></li>
</ul>
</div>

<div class="key-points">
<h4>Highlights</h4>
<ul>
<li>IIT/GNWTなどの理論対立を実装要件に落とす</li>
<li>ESI逆問題の克服策（IHM・不確実性定量化）を明記</li>
<li>DCM/能動的推論でデコーディング→生成モデルへ拡張</li>
<li>EEG複雑性×摂動応答×臨界性で行動非依存の意識指標をロードマップ化</li>
</ul>
</div>

<div class="sidebar-box">
<h4>Study Overview</h4>
<p><strong>Objective:</strong> マルチモーダル計測と神経解読を統合した「本人性維持」評価系の設計</p>
<p style="margin-top:8px;"><strong>Design:</strong> 課題ベース＋安静時の縦断収集、侵襲/非侵襲データの比較</p>
</div>

<div class="sidebar-box">
<h4>Focus Areas</h4>
<ul>
<li>脳活動の計測（HD-EEG, ESI, fMRI）</li>
<li>計算論的神経科学（DCM, Transformer）</li>
<li>意識の理論（IIT, 心理的連続性）</li>
</ul>
</div>

<div class="sidebar-box">
<h4>Technical Proposals</h4>
<ul>
<li><a href="#proposal-46">Issue #46: Measurement QA & BIDS</a></li>
<li><a href="#proposal-47">Issue #47: Strategic Extension</a></li>
<li><a href="#proposal-48">Issue #48: Neuroengineering & IIT</a></li>
<li><a href="#proposal-56">Issue #56: Identifiability & Intervention</a></li>
<li><a href="#proposal-58">Issue #58: Irreversibility & IIT Scaling</a></li>
<li><a href="#proposal-61">Issue #61: Causal & Thermodynamic Critique</a></li>
<li><a href="#proposal-62">Issue #62: Thermodynamic/Causal Validity</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Roadmaps</h4>
<ul>
<li><a href="tech_roadmap.html">技術ロードマップ（学習）→</a></li>
<li><a href="#eeg-consciousness-roadmap">Consciousness Metrics (EEG) →</a>
<ul style="padding-left: 15px; margin-top: 4px; list-style-type: '— ';">
<li>摂動 benchmark（PCI/PCI-ST）<sup><a href="#ref-47">[47]</a></sup></li>
<li>no-report設計でreport confoundを分離<sup><a href="#ref-48">[48]</a></sup></li>
<li>安静時指標は補助トラックとして較正<sup><a href="#ref-50">[50]</a></sup><sup><a href="#ref-52">[52]</a></sup></li>
<li>multimodal 一般化を重視<sup><a href="#ref-105">[105]</a></sup></li>
</ul>
</li>
</ul>
</div>

<div class="sidebar-box">
<h4>Data Standards</h4>
<ul>
<li>BIDS/EEG-BIDS標準への準拠<sup><a href="#ref-25">[25]</a></sup><sup><a href="#ref-26">[26]</a></sup>（<strong>課題:</strong> メタデータ拡充が急務）</li>
<li>データ構造とスキーマ例の公開</li>
<li>多施設間相互運用性の確保</li>
</ul>
</div>

<div class="sidebar-box">
<h4>Resources</h4>
<ul>
<li><a href="brain_science_dictionary.html">脳科学辞典 (Brain Science Dictionary) →</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Research Notes</h4>
<ul>
<li><a href="perspective.html#design-principles">理論フレーム節</a></li>
<li><a href="issue.html#external-collaboration">外部依存・協業節</a></li>
<li><a href="issue.html">貢献ガイド（Research Community）</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Paper Collection</h4>
<p>過去10年間の「Mind Uploading」に関する学術論文を収集・翻訳した資料を公開しています。</p>
<a href="mind_uploading_papers.html"
style="display: inline-block; margin-top: 10px; font-weight: bold; color: var(--color-accent);">論文集を見る
(HTML) →</a>
</div>

<div class="cta-box">
<h4>Contribute</h4>
<p>このプロジェクトに参加しませんか？</p>
<a href="https://github.com/yasufumi-nakata/mind-upload/issues" target="_blank">Issue を立てる</a>
</div>

</aside>
</main>
