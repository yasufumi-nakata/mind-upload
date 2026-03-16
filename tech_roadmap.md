---
layout: default
title: "技術ロードマップ：計測→再構成→実装でWBEを理解する"
description: "マインドアップロード（WBE）を技術面から俯瞰する学習ロードマップ。計測→再構成→実装→検証の問いの木で整理。"
article_type: "Roadmap (Definition #1)"
subtitle: "「何を解けたら前進か」を問いの木に分解し、読む順番と最低限の到達点を示す"
last_updated: "2026-03-17"
note: "暫定版（随時更新）"
audience: "全体像を知りたい人、学習順序を決めたい人、主張の強さを段階で整理したい人"
reading_time: "20〜30分（索引だけなら5分）"
page_intro: "このページは、WBEの論点を『計測』『再構成』『実装』『検証』『社会実装』に分けて並べた地図です。どの問題が土台で、どの問題がまだ未解決なのかを見失わないために使います。"
accuracy_note: "ここに書くのは研究全体の整理であり、各項目がすでに解決済みだという意味ではありません。"
page_highlights:
  - "まずP0〜P2で『何を成功と呼ぶか』を固定し、その後に計測や実装へ進みます。"
  - "索引を使えば、気になる論点だけ先に読むこともできます。"
  - "強い主張ほど後ろのレベルに置き、前のレベルを飛ばして語らない構造にしています。"
  - "R3/R5 では latent-state を evidence tier と timescale で分け、same-day fit と multiday maintenance を同じ成功にしません。"
known_points:
  - "P/M/R/I/V/D に分けると、どの問題が土台でどの問題が上位論点かを整理できます。"
  - "前の層を飛ばして強い主張へ進めない、という依存関係はかなりはっきりしています。"
  - "このページは解決済み一覧ではなく、依存関係の地図として使うのが正しい読み方です。"
  - "connectome や local activity の前進があっても、latent-state と maintenance-state の監査は別に要ります。"
unknown_points:
  - "どの計測粒度が最終的に WBE に十分かは、まだ決まっていません。"
  - "V5 の本人性や D 系列の社会実装条件は、依然として未解決です。"
  - "どのルートが最短かは、今後のデータとベンチの整備状況で変わり得ます。"
  - "どの latent-state augmentation が human whole-brain claim をどこまで押し上げるかも未確定です。"
wiki_links:
  - label: "Wiki: ロードマップの読み方"
    url: "/wiki/roadmap-reading-guide.html"
    description: "P/M/R/I/V/D を初歩から追うための補助ページです。"
  - label: "Wiki: L0〜L5ごとの読み進め方"
    url: "/wiki/claim-level-reading-routes.html"
    description: "クレーム階段の各レベルから、次にどのページへ進むかを整理します。"
  - label: "Wiki: 部分解決・探索段階・未整備の読み方"
    url: "/wiki/progress-labels-and-open-problem-status.html"
    description: "現状欄のラベルが、何の不足を指すかを整理します。"
  - label: "Wiki: 主張と証拠の読み方"
    url: "/wiki/claims-and-evidence.html"
    description: "なぜ前の層を飛ばして強い主張に行けないかを日常語で説明します。"
  - label: "Wiki: 配線図だけでは足りない理由"
    url: "/wiki/connectome-is-not-enough.html"
    description: "R 系列で抜けやすい状態変数を、シナプス・遅延・神経修飾・グリアから整理します。"
  - label: "Wiki: 計測スタックごとの observability と claim ceiling"
    url: "/wiki/measurement-stack-and-claim-ceiling.html"
    description: "どの modality が何を直接見て、どこで主張上限に当たるかを整理します。"
  - label: "Wiki: EEG前処理とQC"
    url: "/wiki/eeg-preprocessing-and-qc.html"
    description: "M 系列で出てくる前処理や品質管理の基礎を補います。"
  - label: "Wiki: 本人性評価と連続性テスト"
    url: "/wiki/identity-and-continuity-tests.html"
    description: "V5 の本人性を、記憶・価値観・学習・分岐・縦断の入口から整理します。"
  - label: "Wiki: state・trait・ドリフト"
    url: "/wiki/state-trait-and-drift.html"
    description: "M7 / V4 で重要な縦断評価を、state・trait・drift の違いから整理します。"
  - label: "Wiki: 更新・分岐・停止規則"
    url: "/wiki/update-branching-and-stop-rules.html"
    description: "I5 / I8 / V7 で必要になる更新運用、分岐管理、停止条件を補います。"
  - label: "Wiki: 閉ループ・遅延・ジッタ・安全停止"
    url: "/wiki/closed-loop-latency-jitter-and-safety-stops.html"
    description: "I1 / I8 で必要になる遅延、ジッタ、リアルタイム安定性を補います。"
recommended_pages:
  - label: "WBE入門"
    url: "/wbe_101.html"
  - label: "EEG入門"
    url: "/eeg_101.html"
  - label: "検証基盤"
    url: "/verification.html"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>Summary</h2>
<p>このページは、マインドアップロード研究の「地図」です。いきなり結論を目指すのではなく、<strong>何を測るか</strong>、<strong>何を再現するか</strong>、<strong>どう動かすか</strong>、<strong>どう確かめるか</strong>を順番に整理します。つまり、<strong>計測 → 再構成 → 実装 → 検証 → 社会実装</strong>の流れで「今どこまで進んだか」を見える化するページです。</p>
</div>

<div class="note-box">
<strong>新しく来た人へ</strong>
<p>
このページは情報量が多いので、先に <a href="wbe_101.html">WBE入門</a> と <a href="eeg_101.html">EEG入門</a>（必要なら <a href="glossary.html">用語集</a>）を読むと理解が早いです。
</p>
</div>

<div class="note-box">
<strong>索引の見方が分からないとき</strong>
<p>
P/M/R/I/V/D の記号や依存関係を初歩から追いたい場合は、先に <a href="wiki/roadmap-reading-guide.html">Wiki: ロードマップの読み方</a> を見てください。この本文は「辞書」より「地図」に近いので、補助説明を先に入れた方が読みやすいです。
</p>
</div>
<div class="note-box">
<strong>理論系ページの中でこのページの役割を知りたいとき</strong>
<p>
このページは理論本文そのものより、論点どうしの依存関係を並べる地図です。主張レベルの入口は <a href="wbe_101.html">WBE入門</a>、理論と限界の長文は <a href="perspective.html">研究ノート</a>、設計原理は <a href="perspective.html#design-principles">Perspective内の理論フレーム節</a> が担当します。理論系ページ全体の読み分けを 1 枚で見たい場合は <a href="wiki/theory-pages-reading-guide.html">Wiki: 理論系ページの読み分けガイド</a> をご覧ください。
</p>
</div>

<div class="note-box">
<strong>V5 本人性の入口だけ先に見たいとき</strong>
<p>
本人性の論点は、このロードマップでは V5、V7、M7、R5 などにまたがります。記憶、価値観、学習、分岐、縦断のどこをどう見たいかを先に整理したい場合は <a href="wiki/identity-and-continuity-tests.html">Wiki: 本人性評価と連続性テスト</a> を先に読むと追いやすくなります。
</p>
</div>

<div class="note-box">
<strong>M7 / V4 の縦断評価で止まったとき</strong>
<p>
その日の state、比較的安定した trait、学習や更新による drift は別物です。短期変動と長期連続性をどう切り分けるかを先に整理したい場合は <a href="wiki/state-trait-and-drift.html">Wiki: state・trait・ドリフト</a> を先にご覧ください。
</p>
</div>

<div class="note-box">
<strong>I5 / I8 / V7 の運用で止まったとき</strong>
<p>
安全な更新、branch の扱い、停止規則、キルスイッチの違いが曖昧な場合は、先に <a href="wiki/update-branching-and-stop-rules.html">Wiki: 更新・分岐・停止規則</a> をご覧ください。Roadmap 本文では何が論点かを示し、運用語の初歩は wiki 側で補います。
</p>
</div>

<div class="note-box">
<strong>I1 / L3 の閉ループで止まったとき</strong>
<p>
リアルタイムに動くと言っても、遅延、ジッタ、end-to-end の戻り、安全停止をどう測るかで難しさが変わります。この入口を初歩から整理したい場合は <a href="wiki/closed-loop-latency-jitter-and-safety-stops.html">Wiki: 閉ループ・遅延・ジッタ・安全停止</a> を先にご覧ください。
</p>
</div>
<div class="note-box">
<strong>『コネクトームが取れたら十分では？』で止まったとき</strong>
<p>
R 系列では、配線図だけでなく、細胞型、内在興奮性 / 恒常性 set point、シナプス効率、遅延と髄鞘、神経修飾、グリアをどう扱うかが分岐点になります。どの状態変数が抜けると何が主張できなくなるかを一次文献から整理したい場合は <a href="wiki/connectome-is-not-enough.html">Wiki: 配線図だけでは足りない理由</a> と <a href="wiki/homeostatic-plasticity-and-maintenance-state.html">Wiki: 恒常性可塑性と維持状態</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>不足・未整備・部分解決の言葉で止まったとき</strong>
<p>
このページの本文では、各ノードの不足点を短い言葉で書いています。<strong>部分解決</strong>、<strong>探索段階</strong>、<strong>未標準化</strong>、<strong>未整備</strong> が何の不足を指すかを先に整理したい場合は <a href="wiki/progress-labels-and-open-problem-status.html">Wiki: 部分解決・探索段階・未整備の読み方</a> を先にご覧ください。
</p>
</div>
<div class="note-box">
<strong>クレーム階段ごとに戻るページを整理したいとき</strong>
<p>
Roadmap では L0〜L5 の全部を扱うため、いま見たいレベルによって次に行く公開ページが変わります。主張レベルごとの導線を 1 枚で見たい場合は <a href="wiki/claim-level-reading-routes.html">Wiki: L0〜L5ごとの読み進め方</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>このページのあとに次の1ページを決めたいとき</strong>
<p>
Roadmap を読んだあとに、計測、再構成、実装、検証、社会実装のどこを次に深掘りするかを 1 枚で見たい場合は <a href="wiki/roadmap-next-routes.html">Wiki: ロードマップのあとに進む5つの道</a> をご覧ください。
</p>
</div>

<div class="key-points">
<h4>先に押さえる3点</h4>
<ul>
<li><strong>このページの役割：</strong>結論を断言することではなく、「どの論点がどこにあるか」を固定することです。</li>
<li><strong>このページで言えること：</strong>今の研究課題を、順序と依存関係つきで整理できます。</li>
<li><strong>このページだけでは言えないこと：</strong>本人性や意識の最終結論が、すでに証明されたとは言えません。</li>
</ul>
</div>

<table class="data-table">
<thead>
<tr>
<th>記号</th>
<th>何のまとまりか</th>
<th>こんなときに先に読む</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>P</strong></td>
<td>前進の定義です。何を成功と呼ぶかを決めます。</td>
<td>いきなり技術論に入る前に、何を目標にしているかをそろえたいときです。</td>
</tr>
<tr>
<td><strong>M</strong></td>
<td>計測です。何をどの精度で観測できるかを扱います。</td>
<td>EEG、fMRI、侵襲計測などの違いから入りたいときです。</td>
</tr>
<tr>
<td><strong>R</strong></td>
<td>再構成です。観測から何を推定できるかを扱います。</td>
<td>逆問題、潜在状態、因果モデル、不確実性が気になるときです。</td>
</tr>
<tr>
<td><strong>I</strong></td>
<td>実装です。モデルをどう動かすか、どこで壊れるかを扱います。</td>
<td>閉ループ、遅延、計算量、安全設計を見たいときです。</td>
</tr>
<tr>
<td><strong>V</strong></td>
<td>検証です。何を測れば前進か、何が出たら失敗かを扱います。</td>
<td>ベンチマーク、因果テスト、本人性、追試可能性を確認したいときです。</td>
</tr>
<tr>
<td><strong>D</strong></td>
<td>社会実装です。権利、同意、公正、安全保障を扱います。</td>
<td>技術だけでなく、運用や制度まで含めて読みたいときです。</td>
</tr>
</tbody>
</table>

<section class="section" id="howto">
<h2 class="section-title">How to Use</h2>
<p>このページは“本”ではなく、研究全体像の<strong>地図</strong>です。まず「問いの木」を通読し、次に「学習の順序」に沿って各ノードを深掘りしてください。重要な運用ルールは2つだけです：<strong>(1) 出典リンクを残す</strong>、<strong>(2) 暫定（不確実性）を明示する</strong>。</p>
</section>

<section class="section" id="measurement-identifiability-audit">
<h2 class="section-title">2026-03 文献監査：計測・潜在状態・同定・介入の4つの壁</h2>
<p>
今回の再監査では、このロードマップの中でも <strong>M3（空間粒度）</strong>、<strong>R3（潜在状態）</strong>、<strong>R5（可塑性 / maintenance-state）</strong>、<strong>R7（同定可能性）</strong>、<strong>V2（因果テスト）</strong> を重点更新しました。理由は単純で、WBE をめぐる技術議論で最も起きやすい誤読が、<strong>観測量の増加</strong>を<strong>状態完全性</strong>と読み替えること、<strong>same-day の予測成功</strong>を<strong>cross-day の維持機構一致</strong>と読み替えること、<strong>予測性能の上昇</strong>を<strong>唯一解の獲得</strong>と読み替えること、そして<strong>介入を1回入れた</strong>ことを<strong>因果検証が済んだ</strong>と読み替えることだからです。以下の4つは、2026年3月時点の一次文献が比較的一貫して支持している下限でございます。
</p>
<table class="data-table">
<thead>
<tr>
<th>壁</th>
<th>一次文献が今支持すること</th>
<th>このページでの修正方針</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>計測粒度の壁</strong></td>
<td>EEG/MEG は大域的電流場、fMRI は血行動態 proxy であり、人で非侵襲に得られるのは基本的にマクロ観測です。一方、Dorkenwald et al. (2024) や MICrONS Consortium et al. (2025) が押し上げたのは、モデル生物や局所皮質での構造・機能対応の前線であって、human whole-brain の state-complete 測定ではありません。</td>
<td>M3 では「何が直接見えて、何が潜在のまま残るか」を粒度ごとに固定し、構造 scaffold と状態完全性を分けて書きます。</td>
</tr>
<tr>
<td><strong>潜在状態 / maintenance-state の壁</strong></td>
<td>Gouwens et al. (2021)、Hengen et al. (2016)、Torrado Pacheco et al. (2021)、Xu et al. (2024)、Looser et al. (2024)、Cahill et al. (2024)、Dewa et al. (2025)、Hadzibegovic et al. (2026) が比較的強く支持するのは、morpho-electric heterogeneity、sleep-dependent recovery、delay / myelin / metabolic support、astrocyte / intrinsic excitability の各状態が別々の timescale で claim ceiling を作ることです。</td>
<td>R3/R5 では latent state を evidence tier と dominant timescale で分け、same-day fit を cross-day maintenance や remote-memory claim へは自動で上げません。</td>
</tr>
<tr>
<td><strong>同定可能性の壁</strong></td>
<td>HD-EEG / ESI の直接妥当化は進んでいますが、Seeber et al. (2019)、Unnwongse et al. (2023)、Hao et al. (2025) が示すのは、条件付き detectability や局在誤差の監査可能性であって、内部状態の一般的一意復元ではありません。source depth、導電率仮定、頭部モデル、刺激条件で結論は動きます。</td>
<td>R7 では predictability、localization、identifiability を別レベルとして定義し、family comparison と棄権条件を必須にします。</td>
</tr>
<tr>
<td><strong>介入検証の壁</strong></td>
<td>TMS-EEG、phase-locked stimulation、adaptive DBS、BCI 閉ループは強い証拠候補ですが、Hernandez-Pavon et al. (2023)、Zrenner et al. (2018)、Wilson et al. (2010) などが示す通り、刺激部位・強度・マスキング・アーチファクト窓・latency/jitter の計測まで固定しないと比較不能です。介入は binary ではなく、強さの異なる段階証拠です。</td>
<td>M6 と V2 では、受動観測、held-out perturbation、online loop、局所因果介入、長期閉ループを段階分けし、要求ログを明示します。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>この監査で明確にした批判点</strong>
<p>
したがって、このロードマップでは今後、<strong>「多モーダルだから十分」</strong>、<strong>「same-day の fit が出たから hidden state もかなり埋まった」</strong>、<strong>「精度が高いから一意」</strong>、<strong>「刺激を入れたから因果」</strong>という4つの短絡を許しません。WBE に近い強い主張ほど、<strong>計測粒度</strong>、<strong>latent-state の timescale</strong>、<strong>候補モデル空間</strong>、<strong>介入設計</strong>、<strong>失敗時の棄権</strong>を先に公開する必要があります。
</p>
</div>
</section>

<section class="section" id="roadmap-index">
<h2 class="section-title">索引（キーワード→QA）</h2>
<p>用語から該当QAへ直接ジャンプできます。括弧内はQA-IDです。本文側にも同じアンカーを付けています。</p>

<div class="note-box">
<strong>使い方</strong>
<p>まず「クイック索引」で目的語へ移動し、次に「カテゴリ別QA索引」で周辺ノードを横断してください。</p>
</div>

<h3>クイック索引</h3>
<ul>
<li><a href="#qa-p0">操作的定義（P0）</a></li>
<li><a href="#qa-p1">クレーム階段（P1）</a></li>
<li><a href="#qa-p2">成果物テンプレ（P2）</a></li>
<li><a href="#qa-m0">計測路線（非侵襲/侵襲/破壊）（M0）</a></li>
<li><a href="#qa-m2">時間解像度（M2）</a></li>
<li><a href="#qa-m3">空間解像度（M3）</a></li>
<li><a href="#qa-m9">BIDS/標準化（M9）</a></li>
<li><a href="#qa-r1">逆問題（R1）</a></li>
<li><a href="#qa-r3">潜在状態（R3）</a></li>
<li><a href="#qa-r4">因果モデル（R4）</a></li>
<li><a href="#qa-r7">同定可能性（R7）</a></li>
<li><a href="#qa-r8">圧縮と忠実度（R8）</a></li>
<li><a href="#qa-i1">閉ループ遅延（I1）</a></li>
<li><a href="#qa-i2">モデル粒度（I2）</a></li>
<li><a href="#qa-i3">計算量ボトルネック（I3）</a></li>
<li><a href="#qa-i5">安全な更新（I5）</a></li>
<li><a href="#qa-i8">containment / 停止（I8）</a></li>
<li><a href="#qa-v1">評価スイート（V1）</a></li>
<li><a href="#qa-v2">因果テスト（V2）</a></li>
<li><a href="#qa-v5">本人性（V5）</a></li>
<li><a href="#qa-v7">コピー/分岐（V7）</a></li>
<li><a href="#qa-v9">追試可能性（V9）</a></li>
<li><a href="#qa-d1">同意と撤回（D1）</a></li>
<li><a href="#qa-d2">アクセスと公正（D2）</a></li>
<li><a href="#qa-d3">安全保障（D3）</a></li>
</ul>

<h3>カテゴリ別QA索引（全件）</h3>
<details class="qa-index-group" open>
<summary><strong>Meta（前進の定義）</strong></summary>
<ul>
<li><a href="#qa-p0"><strong>P0</strong> 「マインドアップロード」の操作的定義は？（何を再現する？）</a></li>
<li><a href="#qa-p1"><strong>P1</strong> 主張レベル（クレーム階段）をどこに置く？</a></li>
<li><a href="#qa-p2"><strong>P2</strong> 最低限の成果物は何？（データ・コード・評価・監査）</a></li>
</ul>
</details>

<details class="qa-index-group" open>
<summary><strong>Measurement（計測）</strong></summary>
<ul>
<li><a href="#qa-m0"><strong>M0</strong> 計測の前提：in vivo / 侵襲 / 破壊スキャンのどれを想定？</a></li>
<li><a href="#qa-m1"><strong>M1</strong> 観測変数：電気（EEG）/血流（fMRI）/スパイク（侵襲）で何が違う？</a></li>
<li><a href="#qa-m2"><strong>M2</strong> 時間解像度の下限：どの時間スケールを“保存”すべき？</a></li>
<li><a href="#qa-m3"><strong>M3</strong> 空間解像度の下限：どの粒度（領域/カラム/ニューロン/シナプス）を目指す？</a></li>
<li><a href="#qa-m4"><strong>M4</strong> 全脳カバレッジ：どこまで“全体”を測る必要がある？</a></li>
<li><a href="#qa-m5"><strong>M5</strong> マルチモーダル統合：位置合わせ（MRI/EEG/fMRI）をどう保証する？</a></li>
<li><a href="#qa-m6"><strong>M6</strong> 介入・刺激：同定可能性を上げる“実験デザイン”は？</a></li>
<li><a href="#qa-m7"><strong>M7</strong> 縦断：日内/日間変動に対して“本人性特徴”は安定か？</a></li>
<li><a href="#qa-m8"><strong>M8</strong> 品質管理：アーチファクト/欠損/ノイズをどう“定量化”して扱う？</a></li>
<li><a href="#qa-m9"><strong>M9</strong> 標準化：BIDS/メタデータで“他人が追試できる”形にするには？</a></li>
</ul>
</details>

<details class="qa-index-group" open>
<summary><strong>Reconstruction（再構成）</strong></summary>
<ul>
<li><a href="#qa-r0"><strong>R0</strong> 復元対象の最小セットは？（構造/状態/学習則）</a></li>
<li><a href="#qa-r1"><strong>R1</strong> 逆問題：観測（M1）から何が一意に推定できる？</a></li>
<li><a href="#qa-r2"><strong>R2</strong> ソース推定：EEGから“どの表現”の脳活動が欲しい？</a></li>
<li><a href="#qa-r3"><strong>R3</strong> 状態推定：潜在状態（latent）をどう定義し、どう検証する？</a></li>
<li><a href="#qa-r4"><strong>R4</strong> 因果：介入に対する反応を予測できるモデルは何？</a></li>
<li><a href="#qa-r5"><strong>R5</strong> 可塑性：学習則を“入れる/入れない”の境界は？</a></li>
<li><a href="#qa-r6"><strong>R6</strong> 個人化：一般モデル＋個人パラメータ？それとも完全に個人別？</a></li>
<li><a href="#qa-r7"><strong>R7</strong> 同定可能性：推定は“唯一解”に近づく？不確実性は？</a></li>
<li><a href="#qa-r8"><strong>R8</strong> 圧縮：どの情報を捨てても“検証基準”は保てる？</a></li>
<li><a href="#qa-r9"><strong>R9</strong> 監査：モデル差分と失敗例を“残す仕組み”は？</a></li>
<li><a href="#qa-r10"><strong>R10</strong> 神経修飾：気分や覚醒度（Volume Transmission）をどう組み込む？</a></li>
</ul>
</details>

<details class="qa-index-group" open>
<summary><strong>Implementation（実装）</strong></summary>
<ul>
<li><a href="#qa-i0"><strong>I0</strong> 実行基盤：汎用計算/GPU/HPC/ニューロモーフィックのどれを狙う？</a></li>
<li><a href="#qa-i10"><strong>I10</strong> 時間連続性：離散時間(RNN)と連続時間(ODE)のどちらを選ぶ？</a></li>
<li><a href="#qa-i1"><strong>I1</strong> 閉ループ：リアルタイムに何msの遅延まで許される？</a></li>
<li><a href="#qa-i2"><strong>I2</strong> モデル粒度：スパイキング/レート/抽象のどこで戦う？</a></li>
<li><a href="#qa-i3"><strong>I3</strong> 計算量：メモリ/電力/並列化のボトルネックはどこ？</a></li>
<li><a href="#qa-i4"><strong>I4</strong> 初期化：モデルの“初期状態”をどう与える？</a></li>
<li><a href="#qa-i5"><strong>I5</strong> 学習とドリフト：学習させるなら“安全な更新”をどう設計する？</a></li>
<li><a href="#qa-i6"><strong>I6</strong> 身体性：入力/出力（センサー/運動/言語）をどこまで持たせる？</a></li>
<li><a href="#qa-i7"><strong>I7</strong> 再現性：実装差（言語/ハード）で結果が変わらない保証は？</a></li>
<li><a href="#qa-i8"><strong>I8</strong> 安全：隔離・監視・停止（containment）をどう作る？</a></li>
<li><a href="#qa-i9"><strong>I9</strong> 熱力学：デジタル基盤で“意識の物理的コスト”を払えるか？</a></li>
</ul>
</details>

<details class="qa-index-group" open>
<summary><strong>Verification（検証）</strong></summary>
<ul>
<li><a href="#qa-v0"><strong>V0</strong> 検証対象：同一性・意識・行動のどれを“工学的に”検証する？</a></li>
<li><a href="#qa-v1"><strong>V1</strong> 評価スイート：何を測れば“前進”と言える？（事前登録）</a></li>
<li><a href="#qa-v2"><strong>V2</strong> 因果テスト：刺激/介入で“同じ反応”を出せるか？</a></li>
<li><a href="#qa-v3"><strong>V3</strong> 一般化：分布外（OOD）でも“本人らしさ”は保てる？</a></li>
<li><a href="#qa-v4"><strong>V4</strong> 長期：学習・ドリフト・忘却の扱いをどう評価する？</a></li>
<li><a href="#qa-v5"><strong>V5</strong> 本人性：心理的連続性を超えた“因果的同一性”とは？</a></li>
<li><a href="#qa-v6"><strong>V6</strong> 意識：理論に依存した予測を、どこまで“検証可能”にできる？</a></li>
<li><a href="#qa-v7"><strong>V7</strong> コピー/分岐：複数インスタンスが走ったら“本人”はどう扱う？</a></li>
<li><a href="#qa-v8"><strong>V8</strong> LLM/模倣との区別：外形が似ていても“中身が違う”をどう判定する？</a></li>
<li><a href="#qa-v9"><strong>V9</strong> 追試：第三者が“同じ結論”に到達できる設計になっている？</a></li>
<li><a href="#qa-v10"><strong>V10</strong> モデル距離：生体脳とエミュレーションの“近さ”をどう測る？</a></li>
<li><a href="#qa-v11"><strong>V11</strong> トポロジー：意識の“構造”は保存されているか？</a></li>
</ul>
</details>

<details class="qa-index-group" open>
<summary><strong>Deployment（社会実装）</strong></summary>
<ul>
<li><a href="#qa-d0"><strong>D0</strong> 倫理的フレームワーク：エミュレートされた存在の権利は？</a></li>
<li><a href="#qa-d1"><strong>D1</strong> 同意と撤回：本人のインフォームドコンセントをどう設計する？</a></li>
<li><a href="#qa-d2"><strong>D2</strong> アクセスと公正：誰がWBEにアクセスできるべきか？</a></li>
<li><a href="#qa-d3"><strong>D3</strong> 安全保障：悪用リスクと制御をどう設計する？</a></li>
</ul>
</details>

</section>

<section class="section" id="definition" data-qa-group>
<h2 class="section-title">前進の定義（最初に固定する）</h2>
<p>“前進”を主張するには、<strong>何を再現できたら勝ちか</strong>（＝評価軸）と、<strong>何が起きたら負けか</strong>（＝反証条件）を先に決める必要があります。ここでは、その前提となる問いを3つに圧縮します。</p>

<details open class="qa" data-tags="meta" id="qa-p0">
<summary>
<span class="qa-id">P0</span>
<span class="qa-title">「マインドアップロード」の操作的定義は？（何を再現する？）</span>
<span class="qa-tags"><span class="tag">META</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>“mind uploading / WBE”を、このサイトでは何として扱うか？（外から見える行動だけか／内部の因果構造か／本人性や意識まで含むか）</p>
<p><strong>分岐（例）：</strong>(A) 行動・機能の再現（ブラックボックス同等） / (B) 神経ダイナミクスの再現（中身重視） / (C) 本人性・主観の継続まで含む（強い主張）</p>
<p><strong>反証可能性：</strong>定義が曖昧なまま成果を語ると、評価が“後付け”になり、進捗の比較が不可能になる</p>
<p><strong>次に必要：</strong>このページ内の「検証」ノードで、(A)(B)(C)それぞれの<strong>測れる基準</strong>と<strong>負け条件</strong>を確定する</p>
</div>
</details>

<details open class="qa" data-tags="meta" id="qa-p1">
<summary>
<span class="qa-id">P1</span>
<span class="qa-title">主張レベル（クレーム階段）をどこに置く？</span>
<span class="qa-tags"><span class="tag">META</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>研究成果を、どのレベルまで到達したら「前進」と言うか？</p>
<ul>
<li><strong>L0：</strong>データ収集と再現可能な解析（標準化・品質管理・追試可能性）</li>
<li><strong>L1：</strong>デコーディング/エンコーディング（神経→行動/刺激、または逆の予測）</li>
<li><strong>L2：</strong>生成モデル（未学習条件でも神経/行動を外挿し、介入予測ができる）</li>
<li><strong>L3：</strong>閉ループ実装（リアルタイムに環境と相互作用して安定に動く）</li>
<li><strong>L4：</strong>本人性の主張（記憶・価値観・学習の連続性を、事前登録した基準で評価）</li>
<li><strong>L5：</strong>社会実装（権利・安全・ガバナンスが技術と同時に成立）</li>
</ul>
<p><strong>反証可能性：</strong>“L1の達成”を“L4の達成”のように語る（スコープのすり替え）を防ぐ</p>
<p><strong>次に必要：</strong>各レベルの「必要データ」「必要モデル」「評価スイート」を、このページで対応づける</p>
</div>
</details>

<details open class="qa" data-tags="meta" id="qa-p2">
<summary>
<span class="qa-id">P2</span>
<span class="qa-title">最低限の成果物は何？（データ・コード・評価・監査）</span>
<span class="qa-tags"><span class="tag">META</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>“前進”を再現可能にするため、何を必ず残すべきか？</p>
<ul>
<li><strong>データ：</strong>生データ＋メタデータ（BIDS等）＋匿名化/同意ログ</li>
<li><strong>コード：</strong>固定バージョンの解析パイプライン（環境・依存関係込み）</li>
<li><strong>評価：</strong>事前登録した指標・テスト・ベースライン比較</li>
<li><strong>監査：</strong>モデル差分、再現実行ログ、失敗例（ネガティブ結果）</li>
</ul>
<p><strong>反証可能性：</strong>成果の“見せ方”だけが先行し、検証不能な主張になる</p>
<p><strong>次に必要：</strong>Mind-UploadでまずL0-L2の成果物テンプレ（データ構造・評価スクリプト）を固める</p>
</div>
</details>
</section>

<section class="section" id="tree">
<h2 class="section-title">問いの木（詳細版：1ページに集約）</h2>
<p>以下に、技術面の問いを「計測→再構成→実装→検証→社会実装」に分解して、<strong>1ページに全部</strong>まとめます。各項目は折りたたみ（クリックで展開）です。</p>
<div class="key-points">
<h4>迷った人向けの最短コース</h4>
<ul>
<li><strong>全体像だけ先に知りたい人：</strong><a href="#qa-p0">P0</a> → <a href="#qa-m0">M0</a> → <a href="#qa-r1">R1</a> → <a href="#qa-v1">V1</a> の順で読むと、「何を測り、何を復元し、何で検証するか」が一周で分かります。</li>
<li><strong>EEG から入りたい人：</strong><a href="#qa-m0">M0</a> → <a href="#qa-m2">M2</a> → <a href="#qa-m9">M9</a> → <a href="#qa-v1">V1</a> の順で読むと、計測条件から評価までを追いやすいです。</li>
<li><strong>本人性の話から入りたい人：</strong><a href="#qa-p1">P1</a> → <a href="#qa-v5">V5</a> → <a href="#qa-v7">V7</a> → <a href="#qa-d1">D1</a> の順で読むと、強い主張に必要な条件と制度面の壁が見えます。</li>
</ul>
</div>

<div class="node" id="measurement" data-qa-group>
<div class="node-kicker">1. Measurement</div>
<h3>計測：どの解像度が必要？</h3>
<p class="mini"><strong>中心問い：</strong>「脳の何を、どの時空間解像度で取れば、“復元すべき対象”が一意に近づくか？」</p>

<details open class="qa" data-tags="measurement" id="qa-m0">
<summary>
<span class="qa-id">M0</span>
<span class="qa-title">計測の前提：in vivo / 侵襲 / 破壊スキャンのどれを想定？</span>
<span class="qa-tags"><span class="tag">MEASUREMENT</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>安全・スケールの制約を踏まえ、どの計測路線で"何を目指すか"を固定する。</p>
<p><strong>分岐（例）：</strong>(A) 非侵襲（EEG/MEG/fMRI）でモデルを鍛える / (B) 侵襲（ECoG/深部/動物）で因果推論を強化 / (C) 破壊的・超高解像度で構造を取る（将来像）</p>
<p><strong>反証条件：</strong>目的（復元対象）が定義されないまま、計測だけ“高級化”しても同定不能になる</p>
<p><strong>次に必要：</strong>このページ内のR0（復元対象）とV0（検証基準）を先に確定する</p>
</div>
</details>

<details open class="qa" data-tags="measurement" id="qa-m1">
<summary>
<span class="qa-id">M1</span>
<span class="qa-title">観測変数：電気（EEG）/血流（fMRI）/スパイク（侵襲）で何が違う？</span>
<span class="qa-tags"><span class="tag">EEG</span><span class="tag">FMRI</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>観測が変わると「復元できる対象（構造/状態/学習則）」が変わる。どの観測で何が識別可能か？</p>
<p><strong>論点：</strong>時系列の速さ・空間分解能・因果介入のしやすさ・全脳カバレッジ・コスト</p>
<table class="data-table">
<thead>
<tr>
<th>観測路線</th>
<th>直接観測しているもの</th>
<th>ここまでなら比較的強く言えること</th>
<th>そのままでは残る潜在状態</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG / MEG</strong></td>
<td>大域的に同期した電流の混合場です。</td>
<td>ms スケールの状態遷移、周波数帯ごとの大域ダイナミクス、閉ループの時間制約を追えます。</td>
<td>深部源の一意性、細胞型、神経修飾、グリア状態、現在のシナプス効率は直接は決まりません。</td>
</tr>
<tr>
<td><strong>fMRI</strong></td>
<td>BOLD を中心とする血行動態の proxy です。</td>
<td>領域スケールの recruitment、比較的遅い network state、同一個体内の広域 coverage を見やすいです。</td>
<td>ms スケールの timing、興奮性/抑制性の分離、region-specific HRF、task-related haemodynamics、venous / depth bias、速い介入応答は直接は見えません。</td>
</tr>
<tr>
<td><strong>whole-brain spatial transcriptomics / cell atlas</strong></td>
<td>ex vivo の分子ラベルと空間配置です。</td>
<td>cell-type taxonomy、領域ごとの分布、構造 atlas 上の分子地図を強くできます。</td>
<td>現在の発火則、シナプス効率、neuromodulatory / glial state、sleep-history は直接は決まりません。</td>
</tr>
<tr>
<td><strong>Patch-seq / morpho-electric-transcriptomics</strong></td>
<td>単一細胞の transcriptome・形態・電気生理の対応です。</td>
<td>cell-type label と morpho-electric phenotype の橋渡し、局所回路の parameter prior を強くできます。</td>
<td>全脳 coverage、same-brain の回路文脈、現在の network state、縦断的 plastic history は残ります。</td>
</tr>
<tr>
<td><strong>ECoG / SEEG</strong></td>
<td>留置部位の局所 field potential と介入応答です。</td>
<td>被覆領域では局所ダイナミクス、刺激応答、比較的強い因果検証へ進めます。</td>
<td>未留置領域、全脳 coverage、長期の state completeness は残ります。</td>
</tr>
<tr>
<td><strong>high-density extracellular probe<br>(Neuropixels / Utah / microwire)</strong></td>
<td>implant 近傍の extracellular spike waveform、threshold crossing、multiunit / local field activity です。</td>
<td>implant region の local population dynamics、online decode、比較的強い局所 readout を前進させます。</td>
<td>未記録 neuron、stable single-unit identity across days、sorting / matching 誤差、probe drift、tissue response、全脳 coverage は残ります。</td>
</tr>
<tr>
<td><strong>connectomics + same-brain function</strong></td>
<td>構造 scaffold と、同一脳での機能応答の対応です。</td>
<td>局所回路の wiring rule、cell-type 依存の結線、構造と機能の局所対応を強くできます。</td>
<td>現在のシナプス効率、内在興奮性 / homeostatic set point、神経修飾場、グリア/代謝状態、縦断的 plastic history はまだ別変数です。</td>
</tr>
<tr>
<td><strong>local transmitter / astrocyte imaging</strong></td>
<td>局所 transmitter dynamics と astrocyte network response です。</td>
<td>coarse proxy が何を代表し、何を代表しないかの較正を強くできます。</td>
<td>全脳 coverage、受容体状態、long-timescale maintenance-state、stack 間の完全統合は残ります。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>2026-03 補足：multimodal は「全部見えた」の同義語ではありません</strong>
<p>
Mikulan et al. (2020)、Seeber et al. (2019)、Unnwongse et al. (2023)、Hao et al. (2025) は、HD-EEG と intracranial ground truth を組み合わせると何が監査できるかを一段前進させました。一方、Steinmetz et al. (2021)、Pachitariu et al. (2024)、van Beest et al. (2025) が示すように、高密度 extracellular probe でも <strong>local population readout</strong> と <strong>chronic same-neuron identity</strong> は別問題であり、sorting / matching / drift audit を抜いて unit-level 安定性を断言できません。さらに Yao et al. (2023) の whole-brain spatial atlas、Gouwens et al. (2021) と Gamlin et al. (2025) の Patch-seq bridge、Dorkenwald et al. (2024) と MICrONS Consortium et al. (2025) の connectomics、Neyhart et al. (2024) と Cahill et al. (2024) の local state imaging が示すのは、stack ごとに <strong>強くなる変数</strong> と <strong>依然として残る latent state</strong> が違う、という事実です。したがって、このページでは <strong>観測量が増えた</strong>ことと、<strong>WBE に必要な状態変数が十分に同定できた</strong>ことを分けて扱います。stack ごとの整理表は <a href="wiki/measurement-stack-and-claim-ceiling.html">Wiki: 計測スタックごとの observability と claim ceiling</a> を参照してください。
</p>
</div>
<div class="note-box">
<strong>2026-03 補足：fMRI の proxy ceiling を 1 段厳しく読む</strong>
<p>
<a href="https://doi.org/10.1038/35084005" target="_blank">Logothetis et al. (2001)</a> と <a href="https://doi.org/10.1038/nature09108" target="_blank">Lee et al. (2010)</a> は BOLD が cell-type / population-input 依存の neurovascular proxy であることを、<a href="https://doi.org/10.1038/nature07664" target="_blank">Sirotin &amp; Das (2009)</a> と <a href="https://doi.org/10.1038/nn.3170" target="_blank">Cardoso et al. (2012)</a> は task-related haemodynamics が local neuronal activity だけでは閉じないことを、<a href="https://doi.org/10.1016/j.neuroimage.2003.11.029" target="_blank">Handwerker et al. (2004)</a> と <a href="https://doi.org/10.7554/eLife.86453" target="_blank">Bailes et al. (2023)</a> は HRF timing が領域・個体で動くことを、<a href="https://doi.org/10.1016/j.neuroimage.2019.02.006" target="_blank">Kay et al. (2019)</a> と <a href="https://doi.org/10.1523/JNEUROSCI.2532-21.2022" target="_blank">Kurzawski et al. (2022)</a> は venous / non-neural factor が空間地図の振幅を歪めうることを示しました。したがってこのロードマップでは、fMRI を neural truth ではなく <strong>hemodynamic proxy</strong> として読み、EEG-fMRI 統合でも <a href="wiki/multimodal-integration-basics.html#hemodynamic-gate">hemodynamic proxy gate</a> を通らない限り fine-grained mechanism を主張しません。
</p>
</div>
<p><strong>次に必要：</strong>同一の課題・同一個体で、マルチモーダル同時計測（可能な範囲）＋位置合わせ（M5）</p>
</div>
</details>

<details open class="qa" data-tags="measurement" id="qa-m2">
<summary>
<span class="qa-id">M2</span>
<span class="qa-title">時間解像度の下限：どの時間スケールを“保存”すべき？</span>
<span class="qa-tags"><span class="tag">RESOLUTION</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>認知・学習・意識に関係する現象を壊さないために、必要な時間分解能はどこか？</p>
<ul>
<li><strong>候補：</strong>ms（スパイク/位相）・10-100ms（結合ダイナミクス）・秒（状態遷移）・分〜日（学習/可塑性）</li>
<li><strong>反証条件：</strong>粗すぎる時間分解能で、介入応答や閉ループ制御が再現できない</li>
<li><strong>次に必要：</strong>閉ループ課題（I1）で許容遅延を測り、必要サンプリングを逆算する</li>
</ul>
<div class="note-box">
<strong>閉ループ時間要件は 1 つではありません</strong>
<p>
2026年3月の再監査では、閉ループの timing 要件は <strong>loop class</strong> ごとに分けて扱うべきだと整理しました。slow neurofeedback、ERP/command BCI、phase-locked stimulation、adaptive DBS では、支配的な時間スケールが異なります。Wilson et al. (2010) は系全体の latency/jitter を hardware で実測する必要を示し、Belinskaia et al. (2020) は alpha neurofeedback で追加 250 / 500 ms 遅延が学習を悪化させると報告しました。一方、Mansouri et al. (2018) と Zrenner et al. (2018) の phase-targeting 系では、遅延は ms 値そのものではなく <strong>対象周波数に対する位相誤差</strong> として評価すべきです。
</p>
<ul>
<li><strong>共通ゲートを 1 ms に固定しません：</strong>ループ型ごとに end-to-end の中央値、P95/P99、worst-case を実測します。</li>
<li><strong>phase 系は位相誤差で読みます：</strong>対象周波数と推定位相の信頼度を添えて評価します。</li>
<li><strong>同期系は path ごとに分けます：</strong>LSL/TTL/photodiode/loopback のどこを実測したかを別々に残します。</li>
</ul>
<p>
したがって、このロードマップでは「単一閾値で全閉ループを裁く」よりも、「どの loop class を扱い、どの timing failure mode を監査したか」を先に固定します。入口の整理は <a href="wiki/closed-loop-latency-jitter-and-safety-stops.html">Wiki: 閉ループ・遅延・ジッタ・安全停止</a> を参照してください。
</p>
</div>
</div>
</details>

<details open class="qa" data-tags="measurement" id="qa-m3">
<summary>
<span class="qa-id">M3</span>
<span class="qa-title">空間解像度の下限：どの粒度（領域/カラム/ニューロン/シナプス）を目指す？</span>
<span class="qa-tags"><span class="tag">RESOLUTION</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>“本人の心的機能”に必要な情報が、どの空間粒度に宿ると仮定するか？</p>
<p><strong>分岐（例）：</strong>(A) 領域間結合＋状態で十分 / (B) 局所回路まで必要 / (C) シナプス結合まで必要</p>
<p><strong>一次文献が強く支持すること：</strong>人で非侵襲に得られる EEG / MEG / fMRI は、基本的に <strong>マクロな proxy</strong> です。EEG / MEG は大域的に同期した電流場、fMRI は血行動態であり、ニューロン単位やシナプス単位の状態を直接観測しているわけではありません。逆に、Dorkenwald et al. (2024) や MICrONS Consortium et al. (2025) が押し上げたのは、モデル生物や局所皮質における高密度 connectomics と same-brain function の接続であり、そこから直ちに「人の全脳で state-complete に測れた」とは言えません。</p>
<ul>
<li><strong>非侵襲ヒト計測の上限：</strong>領域〜ネットワーク水準の状態遷移、比較的大域な timing 制約、条件差の追跡です。</li>
<li><strong>connectomics 前線の上限：</strong>構造 scaffold、局所 functional twin、cell-type 依存結線の監査であって、現在のシナプス効率や神経修飾場までの完全観測ではありません。</li>
<li><strong>残る潜在状態：</strong>シナプス重み、受容体状態、intrinsic excitability / homeostatic set point、neuromodulatory field、glial / metabolic state、plastic history は別変数として残ります。</li>
</ul>
<p><strong>暫定判定規則：</strong>観測経路がマクロ proxy に留まる場合、このロードマップでは主張をまず <strong>L1〜弱い L2</strong> に留めます。局所回路やシナプス粒度の主張へ上げるには、同一脳での構造・機能対応、外部 ground truth、介入応答のいずれかを追加で要求します。</p>
<p><strong>次に必要：</strong>仮定(A)(B)(C)ごとに、観測可能性（M1）、同定可能性（R7）、計算可能性（I3）を束で評価し、どの粒度で何を棄権するかまで公開します。背景は <a href="wiki/connectome-is-not-enough.html">Wiki: 配線図だけでは足りない理由</a> と <a href="wiki/homeostatic-plasticity-and-maintenance-state.html">Wiki: 恒常性可塑性と維持状態</a> を参照してください。</p>
</div>
</details>

<details open class="qa" data-tags="measurement" id="qa-m4">
<summary>
<span class="qa-id">M4</span>
<span class="qa-title">全脳カバレッジ：どこまで“全体”を測る必要がある？</span>
<span class="qa-tags"><span class="tag">COVERAGE</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>限られた計測で、“境界（何が主体に含まれるか）”をどう扱うか？</p>
<p><strong>次に必要：</strong>検証（V0）で「主体の境界」を操作的に置き、必要領域と不要領域を明文化する</p>
</div>
</details>

<details open class="qa" data-tags="measurement" id="qa-m5">
<summary>
<span class="qa-id">M5</span>
<span class="qa-title">マルチモーダル統合：位置合わせ（MRI/EEG/fMRI）をどう保証する？</span>
<span class="qa-tags"><span class="tag">FUSION</span><span class="tag">MRI</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>異なる計測は座標系・遅延・ノイズ構造が違う。統合の誤差が“学習したい信号”を壊していないか？</p>
<p><strong>反証条件：</strong>位置合わせ誤差で再構成（R2）が不安定になり、再現性（P2）が落ちる</p>
<p><strong>次に必要：</strong>同一データに対し複数パイプラインで一致するか（解析差分監査）</p>
<div class="note-box">
<strong>fMRI を混ぜるときの追加監査</strong>
<p>
EEG-fMRI / MRI-fMRI の統合では、shared clock と geometry だけでは足りません。fMRI 側は hemodynamic proxy なので、少なくとも <strong>target neural claim</strong>、<strong>HRF model granularity</strong>、<strong>task / physiology nuisance</strong>、<strong>venous / depth diagnostic</strong> を <a href="verification.html#fusion-card">Fusion Card</a> に加えて残します。これが無い場合、このロードマップでは統合結果を <strong>macro concordance</strong> までに留めます。
</p>
</div>
</div>
</details>

<details open class="qa" data-tags="measurement" id="qa-m6">
<summary>
<span class="qa-id">M6</span>
<span class="qa-title">介入・刺激：同定可能性を上げる“実験デザイン”は？</span>
<span class="qa-tags"><span class="tag">CAUSAL</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>受動観測だけでは同定できない時、どんな介入（刺激/課題/環境変化）を入れると識別可能性が上がるか？</p>
<p><strong>一次文献が強く支持すること：</strong>介入は「入れれば因果が分かる」魔法ではありません。識別可能性が本当に上がるのは、<strong>どこに、いつ、どれだけ刺激したか</strong>、<strong>アーチファクト窓をどう切ったか</strong>、<strong>latency / jitter をどう実測したか</strong> が揃った設計だけです。</p>
<ul>
<li><strong>state-targeted stimulation：</strong>Zrenner et al. (2018) のように、刺激時刻を脳状態へ条件付けると、同じ刺激でも応答差を検出しやすくなります。</li>
<li><strong>ground-truth 付き介入：</strong>頭蓋内刺激、同時 SEEG / ECoG、ファントム、動物実験は、scalp 側の推定誤差を外部基準で較正できます。</li>
<li><strong>閉ループ介入：</strong>BCI や adaptive stimulation では、Wilson et al. (2010) が示すように mean latency だけでなく jitter と worst-case path を測らない限り、反応差を因果差と解釈できません。</li>
</ul>
<p><strong>介入として数えないもの：</strong>受動課題の条件差、post-hoc な cross-modal 相関、刺激ログのない offline 解析だけでは、このページでは強い因果証拠に数えません。</p>
<p><strong>外部依存タスク：</strong>TMS / DBS / 実被験者への侵襲介入は IRB、機材、臨床協力が前提です。本リポジトリで先に握るのは、<strong>介入 grammar</strong>、<strong>同期ログ形式</strong>、<strong>失敗時の停止条件</strong>、<strong>比較規則</strong>の整備です。</p>
<p><strong>次に必要：</strong>モデル（R4）側で「この介入があると family 間の識別が改善する」という設計逆算を行い、TTL / LSL / photodiode / loopback のどこを測ったかまで含む提出物パックを固定します。</p>
</div>
</details>

<details open class="qa" data-tags="measurement" id="qa-m7">
<summary>
<span class="qa-id">M7</span>
<span class="qa-title">縦断：日内/日間変動に対して“本人性特徴”は安定か？</span>
<span class="qa-tags"><span class="tag">LONGITUDINAL</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>同一個体でも脳状態は揺れる。どの特徴が“本人らしさ”として頑健か？</p>
<p><strong>反証条件：</strong>再現できるのが“その日の状態”に限られ、長期の同一性評価（V5）ができない</p>
<p><strong>2026-03 補足：</strong>慢性 invasive 記録では、same neuron across days は channel 番号から自動で与えられません。Steinmetz et al. (2021) は motion correction 付き長期記録を前進させましたが、Pachitariu et al. (2024) は drift / split / merge を sorting 問題の中心に置き、van Beest et al. (2025) は cross-day unit matching を確率的推定として扱いました。したがって M7 では、<strong>sorting version</strong>、<strong>drift correction</strong>、<strong>unit-match probability</strong>、<strong>dropout / new-unit rate</strong> を hidden にしません。</p>
<p><strong>次に必要：</strong>同一被験者の複数セッションで、事前定義の同定スコア（V1）に加えて、chronic probe 系では unit identity audit も追跡する</p>
</div>
</details>

<details open class="qa" data-tags="measurement" id="qa-m8">
<summary>
<span class="qa-id">M8</span>
<span class="qa-title">品質管理：アーチファクト/欠損/ノイズをどう“定量化”して扱う？</span>
<span class="qa-tags"><span class="tag">QC</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>“良いデータ”の定義を事前に置き、除外・補完・重み付けを透明にする。加えて、インピーダンス/CMRR・ノイズフロア・HMD干渉など、<strong>ハードウェア由来の品質劣化</strong>をどう定量化するか？</p>
<ul>
<li><strong>インピーダンス/CMRR:</strong> バランス崩壊を検出し、計測前に警告する。</li>
<li><strong>ノイズフロア/SNR:</strong> 周波数帯ごとの実効SNRを可視化する。</li>
<li><strong>VR干渉:</strong> HMDの電磁・機械ノイズをプロファイル化する。</li>
</ul>
</div>
</details>

<details open class="qa" data-tags="measurement" id="qa-m9">
<summary>
<span class="qa-id">M9</span>
<span class="qa-title">標準化：BIDS/メタデータで“他人が追試できる”形にするには？</span>
<span class="qa-tags"><span class="tag">BIDS</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>データが共有可能でも、メタデータが薄いと追試できない。何を最低限メタデータ化するか？</p>
<p><strong>補足 (Issue #46):</strong> VR/モーション計測を含む場合は<strong>Motion-BIDS</strong>に合わせ、座標系・時間同期・デバイス仕様を明記する。</p>
<p><strong>次に必要：</strong>プロトコル（課題・機器・前処理）を機械可読で残す（P2）</p>
</div>
</details>
</div>

<div class="node" id="reconstruction" data-qa-group>
<div class="node-kicker">2. Reconstruction</div>
<h3>再構成：何を復元する？（回路 / 状態 / 学習則）</h3>
<p class="mini"><strong>中心問い：</strong>「“本人の心的機能”に必要なのは、構造（結合）・動的状態（活動）・学習則（可塑性）のどこまでか？」</p>

<details open class="qa" data-tags="reconstruction" id="qa-r0">
<summary>
<span class="qa-id">R0</span>
<span class="qa-title">復元対象の最小セットは？（構造/状態/学習則）</span>
<span class="qa-tags"><span class="tag">RECONSTRUCTION</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>どこまで復元すれば、検証（V0）で勝ちに行けるか？</p>
<p><strong>分岐（例）：</strong>(A) 構造＋状態（固定） / (B) 構造＋状態＋一部可塑性 / (C) 可塑性まで含むフル動的</p>
<p><strong>反証条件：</strong>(A)で閉ループ学習（I5）が再現不能、(B)(C)で同定不能・過学習で破綻</p>
<p><strong>次に必要：</strong>同定可能性（R7）と計算可能性（I3）を同時に評価する</p>
</div>
</details>

<details open class="qa" data-tags="reconstruction" id="qa-r1">
<summary>
<span class="qa-id">R1</span>
<span class="qa-title">逆問題：観測（M1）から何が一意に推定できる？</span>
<span class="qa-tags"><span class="tag">INVERSE</span><span class="tag">BAYES</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>EEG ソース推定のような逆問題は、解が一意に定まらない“不良設定問題（ill-posed problem）”です。したがって重要なのは、<strong>どの solver を採用したか</strong>より、<strong>幾何・導電率・電極座標・事前仮定を変えたときに結論がどこまで保つか</strong>を監査できることです。</p>
<p><strong>方針：</strong>本プロジェクトでは、特定 solver を標準解として固定しません。受理条件は、(1) 事後分布・信用区間・bootstrap/ensemble など何らかの<strong>不確実性表現</strong>があること、(2) 個体別 MRI / FEM-BEM / 導電率仮定 / 電極幾何の<strong>感度分析</strong>があること、(3) シミュレーション、ファントム、同時侵襲記録、頭蓋内刺激のいずれかで<strong>外部妥当化</strong>していること、です。Bayesian / empirical Bayes は有力候補ですが、必須なのは名称ではなく監査可能性です。</p>
<p><strong>次に必要：</strong>R2 と R7 で、source depth・頭蓋導電率・候補モデル空間がどこまで誤差を支配するかを切り分け、重なった解を無理に 1 つへ潰さない棄権条件まで公開します。</p>
</div>
</details>

<details open class="qa" data-tags="reconstruction" id="qa-r2">
<summary>
<span class="qa-id">R2</span>
<span class="qa-title">ソース推定：EEGから“どの表現”の脳活動が欲しい？</span>
<span class="qa-tags"><span class="tag">EEG</span><span class="tag">ESI</span><span class="tag">BAYES</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>EEGソース推定は「領域×時間」の表現を得やすいが、ニューロン/シナプスは直接は見えない。復元対象（R0）に合わせて表現を選ぶ。</p>
<p><strong>課題：</strong>従来は「高密度EEG(128ch)化」が推奨されてきたが、近年の研究はチャンネル数だけでは不良設定性（ill-posedness）を解決できないことを示している。特に、dSPMのような点推定法は不確実性を無視してしまう。</p>
<p><strong>厳密化した方針：</strong>Block-Champagne系のような不確実性付き推定、<strong>高密度EEG</strong>、<strong>個体別MRIに基づくFEM/BEMフォワードモデル</strong>は、推定の条件を改善する有力な手段です。ただし、これらは<strong>深部脳活動の精度を保証するものではありません</strong>。採用条件は「深部まで見えると言えること」ではなく、<strong>どの誤差源がどこまで減ったかを監査できること</strong>です。したがって、提出物には、(1) 事後分布または信用区間、(2) 導電率・電極座標・頭部モデルの感度分析、(3) シミュレーション/ファントム/同時侵襲記録/頭蓋内刺激など外部基準に対する妥当化、(4) 深部源に関する主張の保留条件、を必須で添付します。</p>
<p><strong>次に必要：</strong>公開実装の有無を曖昧にせず、まず <strong>source imaging の検証仕様書</strong> と <strong>外部基準付きベンチマーク</strong> を先に固定する。実装はその後に、事後分布・感度分析・失敗例まで再現できる形で公開します。</p>
</div>
</details>

<details open class="qa" data-tags="reconstruction" id="qa-r3">
<summary>
<span class="qa-id">R3</span>
<span class="qa-title">状態推定：潜在状態（latent）をどう定義し、どう検証する？</span>
<span class="qa-tags"><span class="tag">STATE</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>観測ノイズと真の状態を分離し、状態が“予測に効いている”ことを示せるか？</p>
<p><strong>2026-03-17 追補：</strong>このページでは latent state を 1 本の隠れ変数として扱いません。一次文献が比較的強く支持するのは、<strong>どの latent state が、どの timescale で、どの claim ceiling を作るか</strong>を分けて監査する必要でございます。same-day の held-out prediction が上がっても、それだけで sleep-dependent recovery、multiday stabilization、timing-sensitive closed loop の hidden state が埋まったとは書きません。</p>
<table class="data-table">
<thead>
<tr>
<th>latent-state class</th>
<th>一次文献が比較的支持すること</th>
<th>この節で止める過大主張</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>morpho-electric / intrinsic excitability</strong></td>
<td><a href="https://doi.org/10.1038/s41586-020-2907-3" target="_blank">Gouwens et al. (2021)</a> と <a href="https://doi.org/10.1038/s41467-025-66975-3" target="_blank">Hadzibegovic et al. (2026)</a> は、cell type だけでは threshold / gain / early consolidation window が決まらないことを示しました。</td>
<td>cell type と connectome があれば node state もほぼ固定された、と読むことです。</td>
</tr>
<tr>
<td><strong>sleep / homeostasis / regime recovery</strong></td>
<td><a href="https://doi.org/10.1016/j.cell.2016.01.046" target="_blank">Hengen et al. (2016)</a>、<a href="https://doi.org/10.1016/j.neuron.2021.04.004" target="_blank">Torrado Pacheco et al. (2021)</a>、<a href="https://doi.org/10.1038/s41593-023-01536-9" target="_blank">Xu et al. (2024)</a> は、sleep / wake をまたぐ firing-rate homeostasis と cortical regime recovery を示しました。</td>
<td>same-day fit を overnight / cross-day stability へそのまま延長することです。</td>
</tr>
<tr>
<td><strong>delay / myelin / metabolic support</strong></td>
<td><a href="https://doi.org/10.1038/s41593-023-01558-3" target="_blank">Looser et al. (2024)</a> は、activity-dependent な oligodendrocyte-axon metabolic coupling が axonal health と recovery に重要だと示しました。</td>
<td>同じ graph なら timing と fatigue / recovery もほぼ同じ、と読むことです。</td>
</tr>
<tr>
<td><strong>astrocyte / slow-state / multiday stabilization</strong></td>
<td><a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">Cahill et al. (2024)</a>、<a href="https://doi.org/10.1038/s41586-024-08170-w" target="_blank">Williamson et al. (2025)</a>、<a href="https://doi.org/10.1038/s41586-025-09619-2" target="_blank">Dewa et al. (2025)</a> は、astrocyte ensemble と slow-state が minutes-to-days の memory-related state を支えることを示しました。</td>
<td>rodent の局所因果証拠を、そのまま human whole-brain の十分条件へ上げることです。</td>
</tr>
<tr>
<td><strong>connectome-constrained degeneracy</strong></td>
<td><a href="https://doi.org/10.1038/s41593-025-02080-4" target="_blank">Beiran &amp; Litwin-Kumar (2025)</a> は connectome 制約があっても dynamics の縮退が残ることを示し、<a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">MICrONS Consortium (2025)</a> は same-brain structure + function が local scaffold を強くすることを示しました。</td>
<td>connectome-constrained prediction を unique internal mechanism や state-complete reconstruction と読むことです。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>R3 で最低限ほしい提出物</strong>
<p>
少なくとも <strong>(1) 直接観測量と proxy</strong>、<strong>(2) latent-state class ごとの dominant timescale と evidence tier</strong>、<strong>(3) connectome-only baseline と augmentation 比較</strong>、<strong>(4) どの latent state がいまの誤差をまだ支配しているか</strong>、<strong>(5) cross-day claim なら fixed interval と state annotation</strong> を一緒に出します。これがない場合、本サイトでは結果をまず <strong>conditional prediction</strong> として扱い、maintenance-consistent model や emulation-ready state estimate へは上げません。
</p>
</div>
<p><strong>反証条件：</strong>潜在状態がデータ圧縮にしかなっておらず、candidate family を変えると結論が大きく揺れる、あるいは介入予測（R4）と temporal validity に寄与しない場合は、状態を捉えたとはみなしません。</p>
<p><strong>次に必要：</strong><a href="verification.html#latent-state-error-budget">Verification の latent-state error budget</a> と <a href="verification.html#temporal-validity-card">Temporal Validity Card</a> に接続し、未学習条件での外挿、介入応答の予測誤差、cross-day 劣化を束で評価します。</p>
</div>
</details>

<details open class="qa" data-tags="reconstruction" id="qa-r4">
<summary>
<span class="qa-id">R4</span>
<span class="qa-title">因果：介入に対する反応を予測できるモデルは何？</span>
<span class="qa-tags"><span class="tag">CAUSAL</span><span class="tag">MULTI-SCALE</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>相関の当てはめではなく、刺激や条件変更に対して“どう変わるはずか”を言えるか。デコーディング（相関）からエミュレーション（因果）への飛躍を、どの証拠鎖で埋めるか。</p>
<p><strong>方針：</strong>本プロジェクトでは、Active Inference、DCM、状態空間モデル、SCM、機械論的回路モデルを<strong>競争させる候補集合</strong>として扱います。DCM は候補生成モデルの比較、SCM は介入・反事実の記述に有用ですが、どちらも単独では自動的な因果発見器ではありません。観測データだけなら同値類が残るため、<strong>候補モデル空間の明示</strong>、<strong>family-level 比較</strong>、<strong>model recovery</strong>、<strong>held-out perturbation 予測</strong>を必須にします。</p>
<p><strong>改善策（Multi-scale の位置づけ）：</strong> マルチスケール統合は有力な拡張ルートですが、既定路線とはしません。EEG 由来のマクロ制約を回路モデルへ渡す場合でも、採否は「理論名」ではなく、刺激・病変・課題摂動に対する予測改善、OOD 一般化、棄権条件の透明性で判断します。</p>
<p><strong>実装の厳密化 (Issue #52):</strong> 逆問題（R1/R2）で得られた不確実性は、後段モデルへ明示的に伝播させます。ただし、ここで固定するのは Active Inference の precision 実装そのものではなく、<strong>上流の不確実性を下流で消さない</strong>ことです。候補理論ごとの実装差は、同一ベンチで比較します。</p>
<p><strong>次に必要：</strong>介入前提の評価タスク（V2）、モデル空間宣言、family comparison、外部妥当化つき摂動ベンチを 1 つの提出物パックへ統合します。</p>
</div>
</details>

<details open class="qa" data-tags="reconstruction" id="qa-r5">
<summary>
<span class="qa-id">R5</span>
<span class="qa-title">可塑性：学習則を“入れる/入れない”の境界は？</span>
<span class="qa-tags"><span class="tag">PLASTICITY</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>長期の本人性（V5）を扱うなら、学習（更新）を入れざるを得ない。だが更新を入れると検証が難しくなる。</p>
<p><strong>2026-03-17 追補：</strong>可塑性の境界は、単に「学習則を書いたかどうか」ではありません。一次文献が比較的強く支持する本当の境界は、<strong>same-day の固定 decode</strong>、<strong>cross-day の maintenance</strong>、<strong>remote-memory / consolidation</strong> のどこまでを claim するかでございます。したがって本サイトでは、plasticity を <strong>claim timescale ごとに必要提出物が変わる問題</strong>として扱います。</p>
<table class="data-table">
<thead>
<tr>
<th>ルート</th>
<th>ここまでなら比較的安全に読めること</th>
<th>最低限ほしい提出物</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>(A) 固定モデル + state annotation</strong></td>
<td>within-session / same-day の限定課題で、状態を固定した条件付き prediction や decode を比較できます。</td>
<td>evaluation family、state annotation、hold-out、abstention、same-day の範囲から出ない claim ceiling です。</td>
</tr>
<tr>
<td><strong>(B) 固定パラメータ + maintenance log</strong></td>
<td><a href="https://doi.org/10.1016/j.cell.2016.01.046" target="_blank">Hengen et al. (2016)</a>、<a href="https://doi.org/10.1016/j.neuron.2021.04.004" target="_blank">Torrado Pacheco et al. (2021)</a>、<a href="https://doi.org/10.1038/s41593-023-01536-9" target="_blank">Xu et al. (2024)</a> が示すように、cross-day claim では sleep / wake と recovery を別監査として扱えます。</td>
<td>fixed decoder interval、sleep / wake history、recalibration burden、transfer ceiling、maintenance-state の未観測項目です。</td>
</tr>
<tr>
<td><strong>(C) 明示的 plasticity / maintenance model</strong></td>
<td><a href="https://doi.org/10.1038/s41586-025-09619-2" target="_blank">Dewa et al. (2025)</a> と <a href="https://doi.org/10.1038/s41467-025-66975-3" target="_blank">Hadzibegovic et al. (2026)</a> が示すような multiday stabilization や early consolidation window を、候補機序として比較できます。</td>
<td>update rule の明示、intervention / perturbation、family comparison、失敗時の downgrade rule、rodent local causal result を human whole-brain に上げない注記です。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>この節の site rule</strong>
<p>
固定モデルを許すのは、まず <strong>same-day / short-window</strong> の claim まででございます。cross-day stability を語るなら <a href="verification.html#temporal-validity-card">Temporal Validity Card</a> を、どの maintenance-state がまだ誤差を支配しているかを語るなら <a href="verification.html#latent-state-error-budget">latent-state error budget</a> を添えます。remote-memory や enduring-personalization を語る場合は、少なくとも intrinsic excitability、sleep-dependent recovery、delay / myelin / metabolic support、astrocyte / slow-state のどれを explicit に入れたか、あるいはどれを未解決として保留したかを出します。
</p>
</div>
<p><strong>分岐（例）：</strong>(A) 学習しない（固定モデル） / (B) 制限付きで学習（安全な更新） / (C) 学習則まで推定、ではなく、<strong>どの timescale の claim を許すか</strong>で必要提出物を変えます。</p>
<p><strong>次に必要：</strong>学習を入れた時のドリフト監視（V4）と安全策（I8）に加えて、cross-day では temporal validity、remote-memory では intervention と maintenance-state の証跡を束ねて公開します。</p>
</div>
</details>

<details open class="qa" data-tags="reconstruction" id="qa-r6">
<summary>
<span class="qa-id">R6</span>
<span class="qa-title">個人化：一般モデル＋個人パラメータ？それとも完全に個人別？</span>
<span class="qa-tags"><span class="tag">PERSONALIZATION</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>“本人性”を議論するなら個人化は避けられない。一方で、個人化しすぎると過学習と再現性が壊れる。</p>
<p><strong>次に必要：</strong>個人内/個人間の性能分解（どこが個人差か）を評価指標に入れる</p>
</div>
</details>

<details open class="qa" data-tags="reconstruction" id="qa-r7">
<summary>
<span class="qa-id">R7</span>
<span class="qa-title">同定可能性：推定は“唯一解”に近づく？不確実性は？</span>
<span class="qa-tags"><span class="tag">IDENTIFIABILITY</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>同じ観測を説明する別モデルが多数あるとき、どの仮定でどこまで絞り込めるか。不確実性は、センサー幾何、導電率、前処理、候補モデル集合、介入設計のどこから来るのか。</p>
<p><strong>反証条件：</strong>小さな前処理差、導電率仮定、候補モデル空間の変更で結論が大きく反転する、あるいは held-out 摂動や外部基準で回収できない場合は、同定できたとはみなしません。</p>
<p><strong>次に必要：</strong>事前分布/正則化だけでなく、<strong>比較した family と除外した family</strong>、<strong>電極幾何・頭部モデル・導電率の感度分析</strong>、<strong>シミュレーション/ファントム/侵襲較正</strong>、<strong>モデルが重なるときの棄権条件</strong>をまとめて公開し、頑健な結論だけを採用します。</p>
<div class="note-box">
<strong>predictability・localization・identifiability を分けます</strong>
<p>
このページでは、<strong>held-out 予測が上がった</strong>、<strong>局在誤差が下がった</strong>、<strong>内部状態が唯一解へ近づいた</strong>、を同じ強さで扱いません。前二者は重要な前進ですが、第三者まで含む一意性の主張には追加条件が必要です。
</p>
<ul>
<li><strong>predictability：</strong>条件付きで次の観測を当てられることです。モデル圧縮や proxy 改善としては有用ですが、それだけで内部状態の唯一性は出ません。</li>
<li><strong>localization：</strong>特定条件下で source の位置誤差が下がることです。直接妥当化として重要ですが、深部・低振幅・未観測領域では別の不確実性が残ります。</li>
<li><strong>identifiability：</strong>候補 family と感度分析を含めても、結論が安定し、かつ held-out perturbation と外部基準で回収できることです。</li>
</ul>
</div>
<div class="note-box">
<strong>2026-03 補足：相関・予測・同定を同じ強さで扱いません</strong>
<p>
直接妥当化つき EEG 文献は、慎重に読むとむしろ限界を明確にしています。Seeber et al. (2019) は 256ch scalp EEG で subcortical signal が <strong>条件付きで detectable</strong> だと示しましたが、一般的一意復元を主張していません。Unnwongse et al. (2023) は intracranial stimulation を用いた直接検証で localization error が conductivity 仮定と source depth に依存することを示し、Hao et al. (2025) は simultaneous HD-EEG/SEEG の患者コホートで source power と source depth が誤差を大きく左右すると報告しました。したがって、cross-modal 相関や held-out 予測が出ても、それはまず <strong>predictability / localization の改善</strong>であり、<strong>内部状態の唯一解</strong>に直結するとは書きません。
</p>
</div>
</div>
</details>

<details open class="qa" data-tags="reconstruction" id="qa-r8">
<summary>
<span class="qa-id">R8</span>
<span class="qa-title">圧縮：どの情報を捨てても“検証基準”は保てる？</span>
<span class="qa-tags"><span class="tag">COMPRESSION</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>WBEは“全部保存”が理想だが現実的でない。評価（V0）を満たす最小表現を探せるか？</p>
<p><strong>次に必要：</strong>圧縮率を変えて、評価スイートの性能がどこで崩れるかを測る</p>
</div>
</details>

<details open class="qa" data-tags="reconstruction" id="qa-r9">
<summary>
<span class="qa-id">R9</span>
<span class="qa-title">監査：モデル差分と失敗例を“残す仕組み”は？</span>
<span class="qa-tags"><span class="tag">AUDIT</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>更新のたびに結論が変わる領域だからこそ、差分・失敗・ネガティブ結果を残す必要がある。</p>
<p><strong>次に必要：</strong>モデル/データ/評価のバージョンを結びつけ、再実行で再現できる形にする（P2）</p>
</div>
</details>

<details open class="qa" data-tags="reconstruction" id="qa-r10">
<summary>
<span class="qa-id">R10</span>
<span class="qa-title">神経修飾：気分や覚醒度（Volume Transmission）をどう組み込む？</span>
<span class="qa-tags"><span class="tag">NEUROMODULATION</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>シナプス結合（Wiring Transmission）だけでは、ドーパミンやセロトニンなどの状態依存的な調節を再現できない。さらに、瞳孔径や HRV は粗い proxy であり、トランスミッタ特異的・領域特異的な内部状態の ground truth にはならない。</p>
<p><strong>2026-03 再定義：</strong>神経修飾の観測は少なくとも <strong>(a) pupil / HRV などの mixed arousal proxy</strong>、<strong>(b) axon activity</strong>、<strong>(c) local transmitter sensor</strong>、<strong>(d) receptor atlas / autoradiography</strong>、<strong>(e) occupancy / release-sensitive PET</strong>、<strong>(f) receptor physiology / pharmacology</strong> の 6 段に分けて読む必要があります。後段ほど chemical / receptor specificity は上がりますが、coverage は狭くなりやすく、逆に前段は広域 covariate として有用でも transmitter ground truth にはなりません。</p>
<p><strong>暫定方針：</strong>神経修飾は「1つの気分スカラー」ではなく、<strong>compartment</strong>、<strong>spatial scope</strong>、<strong>時間スケール</strong>、<strong>受容体依存性</strong>に加えて、PET 系では <strong>ligand / challenge</strong> と <strong>temporal window</strong> を持つ潜在状態として扱います。人データでは瞳孔径や HRV を共変量や層別化に使えても、それだけで脳幹アミン系を同定したとは言いませんし、receptor atlas や occupancy / displacement PET が入っても、それだけで momentary whole-brain transmitter field を読んだとは書きません。</p>
<p><strong>次に必要：</strong>動物や侵襲系の transmitter sensor / receptor physiology / pharmacology / perturbation で proxy を較正し、ヒト側では receptor atlas、occupancy PET、release-sensitive PET のどれを使ったかを分けたうえで、不確実性つきの状態推定と棄権条件を公開します。背景は <a href="wiki/measurement-stack-and-claim-ceiling.html#neuromodulatory-proxy-ladder">Wiki: 計測スタックごとの observability と claim ceiling</a> と <a href="wiki/connectome-is-not-enough.html">Wiki: 配線図だけでは足りない理由</a> を参照してください。</p>
</div>
</details>
</div>

<div class="node" id="implementation" data-qa-group>
<div class="node-kicker">3. Implementation</div>
<h3>実装：どの基盤で？リアルタイム性は？</h3>
<p class="mini"><strong>中心問い：</strong>「復元したモデルを、どの計算基盤（HPC/クラウド/ニューロモーフィック/ハイブリッド）で動かすか？閉ループ（身体・環境）に入れられるか？」</p>

<details open class="qa" data-tags="implementation" id="qa-i0">
<summary>
<span class="qa-id">I0</span>
<span class="qa-title">実行基盤：汎用計算/GPU/HPC/ニューロモーフィックのどれを狙う？</span>
<span class="qa-tags"><span class="tag">IMPLEMENTATION</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>復元対象（R0）に対して、実装基盤は“十分な忠実度”と“現実的コスト”を両立できるか？</p>
<p><strong>次に必要：</strong>モデル粒度（I2）と計算量（I3）をセットで見積もる</p>
</div>
</details>

<details open class="qa" data-tags="implementation" id="qa-i10">
<summary>
<span class="qa-id">I10</span>
<span class="qa-title">時間連続性：離散時間(RNN)と連続時間(ODE)のどちらを選ぶ？</span>
<span class="qa-tags"><span class="tag">NEURAL-ODE</span><span class="tag">DYNAMICS</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>生物学的脳は連続時間で動作するが、標準的なRNN/Transformerは離散時間である。このギャップがダイナミクスの歪みを生む。</p>
<p><strong>提案：</strong>実装フレームワークとして<strong>Neural ODEs (Neural Ordinary Differential Equations)</strong> または <strong>CTRNNs</strong> を採用する。$\frac{dh(t)}{dt} = f(h(t), t, \theta)$ としてモデル化することで、任意の時間分解能でのサンプリングと、随伴変数法（Adjoint Method）によるメモリ効率の良い学習が可能になる。</p>
<p><strong>次に必要：</strong>EEG（ミリ秒）とfMRI（秒）の異なるタイムスケールを、同一の微分方程式系で統合する</p>
</div>
</details>

<details open class="qa" data-tags="implementation" id="qa-i1">
<summary>
<span class="qa-id">I1</span>
<span class="qa-title">閉ループ：リアルタイムに何msの遅延まで許される？</span>
<span class="qa-tags"><span class="tag">REALTIME</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>“本人らしさ”を評価するなら、環境との相互作用（遅延・ノイズ）が本質になる。許容遅延は課題依存。</p>
<p><strong>再定義 (2026-03):</strong> 許容遅延は 1 つの数字ではなく、少なくとも <strong>(a) state feedback / neurofeedback</strong>、<strong>(b) ERP / command BCI</strong>、<strong>(c) phase-locked stimulation</strong>、<strong>(d) burst/state-triggered neuromodulation</strong> に分けて監査します。phase-targeting では ms より位相誤差、adaptive DBS では biomarker burst 検出遅延と停止規則が中心です。</p>
<p><strong>補足 (Issue #46):</strong> CLET やフォトダイオード、loopback、TTL を使って <strong>end-to-end 遅延とジッタ</strong>を実測し、LSL の time_correction は software offset 補正として位置づけます。LSL 単独で actuation onset を保証したとは言いません。</p>
<p><strong>次に必要：</strong> 評価スイート（V1）側で、loop class の明示、中央値/P95/P99/worst-case latency、位相誤差または burst 検出遅延、棄権/freeze/停止回数、追加遅延に対する性能劣化曲線を残します。入口の整理は <a href="wiki/closed-loop-latency-jitter-and-safety-stops.html">Wiki: 閉ループ・遅延・ジッタ・安全停止</a> を参照してください。</p>
</div>
</details>

<details open class="qa" data-tags="implementation" id="qa-i2">
<summary>
<span class="qa-id">I2</span>
<span class="qa-title">モデル粒度：スパイキング/レート/抽象のどこで戦う？</span>
<span class="qa-tags"><span class="tag">GRANULARITY</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>粒度を上げるほど忠実度は上がる（仮）一方で、同定（R7）と計算（I3）が壊れる。勝てる粒度はどこか？</p>
<p><strong>次に必要：</strong>粒度ごとに「必要計測（M2/M3）」「必要計算（I3）」「通る評価（V0）」を対応づける</p>
</div>
</details>

<details open class="qa" data-tags="implementation" id="qa-i3">
<summary>
<span class="qa-id">I3</span>
<span class="qa-title">計算量：メモリ/電力/並列化のボトルネックはどこ？</span>
<span class="qa-tags"><span class="tag">SCALING</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>モデルの忠実度を上げると、計算資源が爆発する。どこで近似・圧縮（R8）するか？</p>
<p><strong>次に必要：</strong>評価スイートの性能を落とさずに圧縮できる境界を測る</p>
</div>
</details>

<details open class="qa" data-tags="implementation" id="qa-i4">
<summary>
<span class="qa-id">I4</span>
<span class="qa-title">初期化：モデルの“初期状態”をどう与える？</span>
<span class="qa-tags"><span class="tag">INITIALIZATION</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>同じ構造でも初期状態が違えば振る舞いが違う。計測（M7）のどの時点を“スタート”にする？</p>
<p><strong>反証条件：</strong>初期化の任意性で結果が揺れて、本人性評価（V5）が成立しない</p>
<p><strong>次に必要：</strong>初期化手順を固定し、初期化に対する感度（頑健性）を測る</p>
</div>
</details>

<details open class="qa" data-tags="implementation" id="qa-i5">
<summary>
<span class="qa-id">I5</span>
<span class="qa-title">学習とドリフト：学習させるなら“安全な更新”をどう設計する？</span>
<span class="qa-tags"><span class="tag">LEARNING</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>学習（R5）を許すと、本人性（V5）と安全（D2）が絡む。更新をどう監視し、どこで止めるか？</p>
<p><strong>次に必要：</strong>ドリフト指標（V4）＋キルスイッチ/隔離（I8）</p>
</div>
</details>

<details open class="qa" data-tags="implementation" id="qa-i6">
<summary>
<span class="qa-id">I6</span>
<span class="qa-title">身体性：入力/出力（センサー/運動/言語）をどこまで持たせる？</span>
<span class="qa-tags"><span class="tag">EMBODIMENT</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>閉ループ検証（I1/V1）には、環境と身体（あるいはその代替）が必要。最小の身体性は何か？</p>
<p><strong>次に必要：</strong>環境（VR/ゲーム/対話）を固定し、同一条件で追試可能な評価を設計する</p>
</div>
</details>

<details open class="qa" data-tags="implementation" id="qa-i7">
<summary>
<span class="qa-id">I7</span>
<span class="qa-title">再現性：実装差（言語/ハード）で結果が変わらない保証は？</span>
<span class="qa-tags"><span class="tag">REPRO</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>“同じモデル”でも数値誤差や並列順序で挙動が変わる。どこまで決定性を要求するか？</p>
<p><strong>次に必要：</strong>固定乱数・固定環境・差分テスト（P2）で、許容誤差内に収まるか検証する</p>
</div>
</details>

<details open class="qa" data-tags="implementation" id="qa-i8">
<summary>
<span class="qa-id">I8</span>
<span class="qa-title">安全：隔離・監視・停止（containment）をどう作る？</span>
<span class="qa-tags"><span class="tag">SAFETY</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>強い主張（P1のL4-L5）に近づくほど、安全が技術要件になる。</p>
<p><strong>次に必要：</strong>隔離環境、監視指標、停止プロトコルの3点セットを、L3以降の実装計画に含める</p>
</div>
</details>

<details open class="qa" data-tags="implementation" id="qa-i9">
<summary>
<span class="qa-id">I9</span>
<span class="qa-title">熱力学：実装コストと不可逆性をどう監査するか？</span>
<span class="qa-tags"><span class="tag">THERMODYNAMICS</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>WBE の実装比較で、熱力学の話をどこまで評価へ入れるべきか。ここで混ぜてはいけないのは、<strong>Landauer 下限</strong>、<strong>組織レベルのエネルギー予算</strong>、<strong>粗視化 neural dynamics の time irreversibility</strong>、<strong>model-based entropy flow</strong>です。問うべきなのは「これで同一性が証明できるか」ではなく、<strong>物理コストと nonequilibrium 指標を過大主張せず、どう監査するか</strong>でございます。</p>
<p><strong>2026-03 文献監査：</strong>B&eacute;rut et al. (2012) が実証したのは、論理的に不可逆な bit erasure の最小散逸下限であり、デジタル脳全体の wall-power や NESS 再現条件ではありません。Lynn et al. (2021)、de la Fuente et al. (2023)、Nartallo-Kaluarachchi et al. (2025) が示すのは、fMRI / ECoG / MEG などの粗視化時系列から broken detailed balance や time irreversibility を測る有用性であって、微視的な物理散逸や本人性の受理条件ではありません。Ishihara &amp; Shimazaki (2025) も、entropy flow 推定が state-space kinetic Ising model、pairwise coupling、mean-field approximation などの仮定を要する model-based quantity であることを示しています。</p>
<div class="key-points">
<h4>このページで固定する扱い</h4>
<ul>
<li><strong>必須ゲートにはしません：</strong>EPR &gt; 0 の維持、<code>Virtual Dissipation Protocol</code>、生体脳 20W 一致、通信:計算比一致を、現時点での受理条件には置きません。</li>
<li><strong>補助ログとして扱います：</strong>wall-plug power、FLOPs、time irreversibility、model-based entropy flow は分けて記録します。</li>
<li><strong>モダリティ依存を明示します：</strong>fMRI / MEG / ECoG / spike train で推定量の意味が違うため、相互にそのまま置換しません。</li>
<li><strong>下界と本体を分けます：</strong>観測時系列から得る irreversibility は、しばしば coarse-grained lower bound であり、微視的な physical dissipation そのものとは書きません。</li>
</ul>
</div>
<p><strong>次に必要：</strong>同一モダリティ・同一前処理内で再現できる irreversibility benchmark と、wall-plug power / FLOPs / simulated metabolic overhead を分離したログ schema を整備することです。最低限、粗視化、サンプリング周期、推定器、Markov/Ising/mean-field 仮定、lower bound か model-based quantity か、比較対象タスク、ハードウェア電力の定義を公開します。詳細は <a href="wiki/thermodynamic-grounding-basics.html">Wiki: 熱力学的接地の基本</a> を参照してください。</p>
</div>
</details>
</div>
</details>

<div class="node" id="verification" data-qa-group>
<div class="node-kicker">4. Verification</div>
<h3>検証：何を満たせば「同じ」と言える？</h3>
<p class="mini"><strong>中心問い：</strong>「同一性/意識/行動のうち、技術的に検証可能な基準をどう定義し、反証条件をどう置くか？」</p>

<details open class="qa" data-tags="verification" id="qa-v0">
<summary>
<span class="qa-id">V0</span>
<span class="qa-title">検証対象：同一性・意識・行動のどれを“工学的に”検証する？</span>
<span class="qa-tags"><span class="tag">VERIFICATION</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>検証できない（測れない）ものを、検証したことにはできない。何を“測れる成功条件”に落とすか？</p>
<p><strong>分岐（例）：</strong>(A) 行動・能力の同等性 / (B) 介入応答の同等性 / (C) 自伝的記憶や価値観の連続性（要注意）</p>
<p><strong>次に必要：</strong>V1で評価スイートを事前登録し、P1のクレーム階段と対応づける</p>
</div>
</details>

<details open class="qa" data-tags="verification" id="qa-v1">
<summary>
<span class="qa-id">V1</span>
<span class="qa-title">評価スイート：何を測れば“前進”と言える？（事前登録）</span>
<span class="qa-tags"><span class="tag">BENCHMARK</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>タスク・指標・ベースライン・統計・失敗条件を事前に固定する。</p>
<ul>
<li><strong>行動：</strong>未学習タスクでの一般化、反応時間/誤り、学習曲線</li>
<li><strong>神経：</strong>状態遷移、スペクトル特徴、ネットワーク指標、介入応答</li>
<li><strong>本人性（暫定）：</strong>自伝的記憶の整合、選好の安定、自己モデルの一貫性</li>
</ul>
<p><strong>次に必要：</strong>まずはL0-L2向けに“小さくても追試可能”なスイートを作る</p>
</div>
</details>

<details open class="qa" data-tags="verification" id="qa-v2">
<summary>
<span class="qa-id">V2</span>
<span class="qa-title">因果テスト：刺激/介入で“同じ反応”を出せるか？</span>
<span class="qa-tags"><span class="tag">CAUSAL</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>相関一致は“似せた”だけでも達成できる。介入に対して一致するかが強い検証になる。</p>
<p><strong>証拠の強さを4段で扱います：</strong>このロードマップでは、因果テストを 1 種類の pass / fail に潰しません。一次文献が今支えるのは、強さの異なる段階証拠です。</p>
<ul>
<li><strong>Gate 1 / held-out perturbation prediction：</strong>課題条件、刺激タイミング、環境変化を変えたときの応答を offline に予測できることです。</li>
<li><strong>Gate 2 / online human-in-the-loop：</strong>実時間入力と feedback を含む loop で、latency / jitter を監査しながら性能を保てることです。</li>
<li><strong>Gate 3 / local causal intervention：</strong>TMS-EEG、intracranial stimulation、adaptive DBS など、刺激部位・強度・アーチファクト処理・安全停止条件が公開された介入です。</li>
<li><strong>Gate 4 / long-run closed loop：</strong>複数セッションや長期運用で、再較正負荷、回復時間、失敗モードまで追跡できることです。</li>
</ul>
<p><strong>必須ログ：</strong>刺激部位、強度、マスキング、アーチファクト窓、同期経路、end-to-end latency の中央値 / P95 / P99、jitter、dropout、recovery time を残します。TMS-EEG は Hernandez-Pavon et al. (2023) の推奨事項を外した時点で、比較可能な因果テストとして扱いません。</p>
<p><strong>判定規則：</strong>Gate 1 の成功だけで L3 や「反事実同値」を主張しません。より強い主張へ進めるには、M6（介入設計）と R4（因果モデル）をつないだ評価項目、外部妥当化、棄権条件を束で提出する必要があります。詳細な運用側の判定は <a href="verification.html#causal-perturbation-suite">Verification の因果的摂動スイート</a> を参照してください。</p>
<p><strong>次に必要：</strong>M6（介入設計）とR4（因果モデル）を繋いだ評価項目を作り、少なくとも Gate 1 / Gate 2 を第三者が再実行できる仕様へ落とします。</p>
</div>
</details>

<details open class="qa" data-tags="verification" id="qa-v3">
<summary>
<span class="qa-id">V3</span>
<span class="qa-title">一般化：分布外（OOD）でも“本人らしさ”は保てる？</span>
<span class="qa-tags"><span class="tag">OOD</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>訓練と同じ条件でしか動かないなら、アップロードではなく“再生”に近い。新規状況での一貫性を測る。</p>
<p><strong>次に必要：</strong>未学習課題・環境変化・ノイズ条件での性能劣化曲線を定義する</p>
</div>
</details>

<details open class="qa" data-tags="verification" id="qa-v4">
<summary>
<span class="qa-id">V4</span>
<span class="qa-title">長期：学習・ドリフト・忘却の扱いをどう評価する？</span>
<span class="qa-tags"><span class="tag">LONGITUDINAL</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>学習させるほど、元の本人と乖離する可能性も増える。変化を“許容”する範囲を定義する。</p>
<p><strong>次に必要：</strong>セッション間の同一性指標（M7）＋更新ログ（P2）</p>
</div>
</details>

<details open class="qa" data-tags="verification" id="qa-v5">
<summary>
<span class="qa-id">V5</span>
<span class="qa-title">本人性：心理的連続性を超えた“因果的同一性”とは？</span>
<span class="qa-tags"><span class="tag">IDENTITY</span><span class="tag">LEGAL</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>記憶や性格の類似（心理的連続性）だけでは、コピーや模倣（LLM）と区別がつかない。より厳密な工学的定義が必要である。</p>
<ul>
<li><strong>新基準：因果的同一性（Causal Identity）：</strong>
パーフィットの心理説を拡張し、システムの「未来の予測能力（Active Inference の精度）」が生物学的脳と統計的に区別不能であることを同一性の条件とする。
</li>
<li><strong>指標：</strong>チューリング・テストを拡張した<strong>「因果的摂動プロトコル（Causal Perturbation Protocol）」</strong>を実行する。TMS等による物理的摂動に対する生物学的脳の反応と、エミュレーション上の仮想的摂動に対する反応の統計的同一性を検証する指標（例：Perturbational Complexity Index, PCI）を導入し、動的な因果構造の一致を確認する。</li>
<li><strong>反証条件：</strong>記憶は持っているが、新規環境に対する適応・予測パターンがオリジナルと乖離する（ゾンビ/模倣者）</li>
<li><strong>次に必要：</strong>V8の「模倣との区別」テストにおいて、予測精度をコア指標に据える</li>
</ul>                        </div>
</details>

<details open class="qa" data-tags="verification" id="qa-v6">
<summary>
<span class="qa-id">V6</span>
<span class="qa-title">意識：理論に依存した予測を、どこまで“検証可能”にできる？</span>
<span class="qa-tags"><span class="tag">CONSCIOUSNESS</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>意識は直接観測できない。したがって、理論（IIT / GNWT / FEP など）が出す予測差を、task/report confound を抑えたうえで benchmark 化できるかを問います。</p>
<ul>
<li><strong>理論は winner-take-all で採択しません：</strong> Ferrante et al. (2025) が示したのは、単一理論の勝利ではなく preregistered prediction competition の必要性です。したがって本サイトでは、IIT / GNWT / FEP を <strong>prediction family</strong> として競わせ、理論名そのものを pass/fail 指標にはしません。</li>
<li><strong>PCI / PCI-ST は perturbation benchmark です：</strong> Casali et al. (2013) と Comolatti et al. (2019) は強い benchmark 候補を与えましたが、universal meter を与えたわけではありません。刺激部位、強度、マスキング、artifact window、cohort 較正を公開した場合に限り、L2/L3 の補助指標として扱います。</li>
<li><strong>spontaneous complexity / criticality は calibration track です：</strong> Maschke et al. (2024) は spontaneous criticality と PCI の関連を示しましたが、Casarotto et al. (2024) は minimally conscious state で spontaneous feature と PCI の解離を示しました。したがって resting-state marker は PCI の置換ではなく、外部較正が必要な proxy として扱います。</li>
<li><strong>no-report / criterion placement を先に固定します：</strong> Cohen et al. (2024) と Fahrenfort et al. (2025) が示すように、post-perceptual processing や criterion placement を統制しないと、理論差より task/report confound を見ている可能性が残ります。</li>
</ul>
<p><strong>注意：</strong>理論はあくまで仮説生成のツールとして扱い、実装（WBE）の成否は「特定理論への適合」ではなく、V2（因果）、V3（OOD）、V4（長期安定性）と束で判断します。geometry や topology を使う場合も、主要な pass/fail は perturbation と generalization に置きます。</p>
</div>
</details>

<details open class="qa" data-tags="verification" id="qa-v7">
<summary>
<span class="qa-id">V7</span>
<span class="qa-title">コピー/分岐：複数インスタンスが走ったら“本人”はどう扱う？</span>
<span class="qa-tags"><span class="tag">BRANCHING</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>工学的には複製が容易。検証の設計も、分岐を前提にしないと破綻する。</p>
<p><strong>次に必要：</strong>個体ID・版管理（P2）を、本人性評価（V5）と結びつける</p>
</div>
</details>

<details open class="qa" data-tags="verification" id="qa-v8">
<summary>
<span class="qa-id">V8</span>
<span class="qa-title">LLM/模倣との区別：外形が似ていても“中身が違う”をどう判定する？</span>
<span class="qa-tags"><span class="tag">DISAMBIGUATION</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>会話や報告は模倣されやすく、language model の事前分布が強いほど「それっぽさ」は上がります。したがって、ここで区別したいのは抽象的な「AIらしさ」ではなく、<strong>神経信号が language prior をどこまで上回っているか</strong>、<strong>どのモダリティ・課題・時間スケールで成立しているか</strong>です。</p>

<table class="data-table">
<thead>
<tr>
<th>トラック</th>
<th>2026-03時点で比較的強く言えること</th>
<th>まだ言えないこと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>非侵襲 semantic / caption decoding</strong></td>
<td>Tang らや Horikawa は、fMRI を使って連続言語の意味再構成や動画内容の記述生成を前進させました。ここでの到達点は、<strong>意味表現の一部を外部文へ写す</strong>ことです。</td>
<td>被験者協力、課題条件、caption 候補空間への依存が残るため、これだけで self-model や WBE の再現とは言えません。</td>
</tr>
<tr>
<td><strong>非侵襲 word / speech decoding</strong></td>
<td>Défossez らと d'Ascoli らは、MEG/EEG からの speech / word decoding を前進させ、<strong>MEG と reading task が有利で、データ量が性能を強く支配する</strong>ことを示しました。</td>
<td>open-ended thought reading や強い cross-day / cross-task 一般化は、まだ別問題です。candidate set や device 依存を隠したまま強い主張へ上げられません。</td>
</tr>
<tr>
<td><strong>侵襲 streaming speech neuroprosthesis</strong></td>
<td>Willett、Littlejohn、Wairagkar は、局所的な communication subsystem としての speech BCI を大きく前進させました。大語彙、高速 decode、80 ms 更新、closed-loop own-voice synthesis は重要な達成です。</td>
<td>ここで示されたのは communication route の局所的前進であって、全脳 emulation や本人性保存ではありません。さらに Wilson らが示したように、長期 drift と recalibration burden は別の壁として残ります。</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>最低限ほしい評価パック</strong>
<ul>
<li><strong>神経寄与の切り分け：</strong><code>brainなし</code>、<code>time-shuffle</code>、<code>trial-shuffle</code>、<code>LM-only</code>、<code>no-LM</code> を並べ、検索型なら candidate set size も公開します。</li>
<li><strong>一般化の境界：</strong>held-out story、held-out vocabulary、cross-day、cross-task、cross-subject を分けて報告し、被験者協力や個人適応の必要性を隠しません。</li>
<li><strong>streaming 指標：</strong>words/min だけでなく <code>P50/P95/P99 latency</code>、silence / abstention、dropout、recalibration burden、recovery time を残します。</li>
<li><strong>読替え禁止：</strong>decode 成功、embedding 類似、会話の自然さを、そのまま emulate / WBE / 本人性保存へ昇格させません。</li>
</ul>
</div>

<p><strong>次に必要：</strong>V2（介入）＋I1（閉ループ）＋R4（因果）に、<code>LM-only / shuffle / OOD / cross-day / latency / abstention / recalibration</code> を束ねた評価パックを接続し、communication route の前進と WBE の主張を分離します。</p>
</div>
</details>

<details open class="qa" data-tags="verification" id="qa-v9">
<summary>
<span class="qa-id">V9</span>
<span class="qa-title">追試：第三者が“同じ結論”に到達できる設計になっている？</span>
<span class="qa-tags"><span class="tag">REPRO</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>研究の最短距離は“他人が追試できる”状態を作ること。本人性の議論ほど追試性が重要になる。</p>
<p><strong>次に必要：</strong>P2（成果物）を満たす範囲で、データ/コード/評価を公開可能に整える</p>
</div>
</details>

<details open class="qa" data-tags="verification" id="qa-v10">
<summary>
<span class="qa-id">V10</span>
<span class="qa-title">モデル距離：生体脳とエミュレーションの“近さ”をどう測る？</span>
<span class="qa-tags"><span class="tag">METRIC</span><span class="tag">MATH</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>パラメータ空間での単純なユークリッド距離は、モデルの機能的な振る舞いの違いを反映しないことが多い。より本質的な「振る舞いの近さ」をどう定量化するか？</p>
<p><strong>方針：</strong>単一の数理距離を標準解として採用しません。現時点で外部基準として強いのは、held-out perturbation 応答、OOD 劣化曲線、校正誤差、回復時間のような<strong>観測可能な振る舞い</strong>です。Fisher-Rao、representation distance、manifold separation などの距離は候補群として比較しますが、どれか 1 つを既定の合否指標にはしません。</p>
<p><strong>次に必要：</strong>候補距離が V2 / V3 / V4 の外部基準とどの程度整合するかを、同一ベンチ上で比較することです。前処理、標本数、状態差を変えても順位が安定するかを sensitivity analysis で公開します。</p>
</div>
</details>

<details open class="qa" data-tags="verification" id="qa-v11">
<summary>
<span class="qa-id">V11</span>
<span class="qa-title">トポロジー：意識の“構造”は保存されているか？</span>
<span class="qa-tags"><span class="tag">TDA</span><span class="tag">GEOMETRY</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>PCI（複雑性）などのスカラー値だけでは、意識の「質的な構造（Qualitative Structure）」が同じかどうかわからない。</p>
<p><strong>方針：</strong>位相的データ解析（TDA）や manifold geometry は、スカラー指標で落ちる構造差を<strong>補助的に</strong>記述する有望なトラックです。Yoon et al. (2024) は cross-population で topology を比較する数学的基盤を与えましたが、iScience 2024 の mouse V1 circular manifold 研究は truthful topology の回収に sampling 障害があることも示しました。したがって topology distance を、そのまま consciousness structure の保証や WBE 合否へ直結させません。</p>
<p><strong>次に必要：</strong>sampling、埋め込み次元、距離関数、前処理、session drift、perturbation responsiveness を振った sensitivity analysis を通し、そのうえで安定に残る位相特徴だけを補助指標として報告します。</p>
</div>
</details>
</div>

<div class="node" id="deployment" data-qa-group>
<div class="node-kicker">5. Deployment & Governance</div>
<h3>社会実装：技術を越えて何が必要か？</h3>
<p class="mini"><strong>中心問い：</strong>「L5（社会実装）に向けて、技術以外にどのような制度・倫理・法的基盤が必要か？」</p>

<details open class="qa" data-tags="deployment" id="qa-d0">
<summary>
<span class="qa-id">D0</span>
<span class="qa-title">倫理的フレームワーク：エミュレートされた存在の権利は？</span>
<span class="qa-tags"><span class="tag">ETHICS</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>WBEが成功した場合、エミュレーションは権利主体か？停止は「死」か？複製は「出生」か？</p>
<p><strong>現状：</strong>EU AI Act、米国MIND Act（2025提案）等で神経データ保護の枠組みが整備されつつあるが、WBE固有の課題（複製、停止、改変）には対応していない。</p>
<p><strong>次に必要：</strong>技術的検証（L0-L2）と並行して、倫理レビュー委員会の設計指針を策定する</p>
</div>
</details>

<details open class="qa" data-tags="deployment" id="qa-d1">
<summary>
<span class="qa-id">D1</span>
<span class="qa-title">同意と撤回：本人のインフォームドコンセントをどう設計する？</span>
<span class="qa-tags"><span class="tag">CONSENT</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>WBEプロセスへの同意は事前に与えられるが、プロセス中やプロセス後の撤回権をどう保証するか？</p>
<p><strong>次に必要：</strong>段階的同意モデル（各フェーズでの再同意）と、停止権の工学的実装を設計する</p>
</div>
</details>

<details open class="qa" data-tags="deployment" id="qa-d2">
<summary>
<span class="qa-id">D2</span>
<span class="qa-title">アクセスと公正：誰がWBEにアクセスできるべきか？</span>
<span class="qa-tags"><span class="tag">EQUITY</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>WBEが実現した場合、富裕層のみが「不死」にアクセスできる格差問題をどう扱うか？</p>
<p><strong>次に必要：</strong>検証基盤（Verification Commons）のオープンアクセス設計を、格差防止の第一歩として位置づける</p>
</div>
</details>

<details open class="qa" data-tags="deployment" id="qa-d3">
<summary>
<span class="qa-id">D3</span>
<span class="qa-title">安全保障：悪用リスクと制御をどう設計する？</span>
<span class="qa-tags"><span class="tag">SECURITY</span></span>
</summary>
<div class="qa-body">
<p><strong>問い：</strong>エミュレーションの改変、強制的な精神操作、軍事利用等のリスクにどう対処するか？</p>
<p><strong>次に必要：</strong>I8（containment）の設計と連動し、アクセス制御・改変監査・停止権の技術的保証を設計する</p>
</div>
</details>
</div>
</div>

</section>

<section class="section" id="unsolved">
<h2 class="section-title">未解決問題の定義カタログ（厳密版）</h2>
<p>
ここでは「未解決」を曖昧語にせず、<strong>何が入力で、何を出力し、どの条件で合格/失敗か</strong>を定義します。先行研究が厚くても、判定条件が曖昧なら研究は積み上がりません。逆に、定義が厳密なら小さな前進を確実に蓄積できます。
</p>

<table class="data-table">
<thead>
<tr>
<th>ID</th>
<th>未解決問題の定義（厳密化）</th>
<th>既存到達点</th>
<th>未解決境界（次に詰める点）</th>
</tr>
</thead>
<tbody>
<tr>
<td>U0</td>
<td><strong>操作的同一性</strong>: 介入集合Iと時間窓Tに対し、生体系とモデル系の条件付き分布差が閾値以下であることを「同一」と定義できるか。</td>
<td>V0/V5で枠組み定義あり。心理的連続性と因果同一性の区別を導入済み。</td>
<td>介入集合Iの最小完備条件、閾値設定、事前登録ルールが未確定。</td>
</tr>
<tr>
<td>U1</td>
<td><strong>逆問題の同定可能性</strong>: 観測yから潜在源xを推定する際、事後分布の集中度で「唯一解に近い」を定量化できるか。</td>
<td>R2で不確実性付き推定の方針を明文化済み。ただし公開実装と外部妥当化は未完。</td>
<td>前向きモデル誤差（導電率・形状）込みの全体同定可能性が未検証。</td>
</tr>
<tr>
<td>U2</td>
<td><strong>時空間解像度の下限</strong>: 認知・学習・介入応答を壊さない最小の時間/空間分解能を課題別に定義できるか。</td>
<td>M2/M3で論点整理済み。</td>
<td>閉ループ課題での実測境界（遅延許容量・粒度崩壊点）が不足。</td>
</tr>
<tr>
<td>U3</td>
<td><strong>主体境界（Boundary）</strong>: 主体に含める生理・神経・環境要素の最小集合を、検証可能な操作定義で固定できるか。</td>
<td>Issue #12でハイブリッド計測プロトコルを整備。</td>
<td>境界変更時にV5判定がどれだけ変動するかの感度分析が未了。</td>
</tr>
<tr>
<td>U4</td>
<td><strong>因果同値（Counterfactual Equivalence）</strong>: 観測一致ではなく介入分岐の予測一致で同値判定できるか。</td>
<td>R4/V2/V6で理論的方針を明示。</td>
<td>反実仮想生成器、偽介入ベースライン、停止規則の実装が不足。</td>
</tr>
<tr>
<td>U5</td>
<td><strong>学習則と本人性ドリフト</strong>: 学習更新を許した場合、どの程度の表現変化まで同一性を維持とみなすか。</td>
<td>R5/V4で問題提起済み。</td>
<td>更新規則ごとの許容ドリフト閾値とキルスイッチ条件が未定義。</td>
</tr>
<tr>
<td>U6</td>
<td><strong>個人化と汎化の分離</strong>: 個人固有パラメータと課題共通パラメータを同定し、過学習を回避できるか。</td>
<td>R6で評価方針を提示。</td>
<td>個人内/個人間分解を行う標準ベンチと検定計画が不足。</td>
</tr>
<tr>
<td>U7</td>
<td><strong>マルチモーダル整合</strong>: EEG/fMRI/行動/生理を統合したとき、座標・遅延・ノイズ差を監査可能に保てるか。</td>
<td>M5/M9で要件化、Motion-BIDS方針（Issue #46）。</td>
<td>同一データで複数統合パイプラインの一致率評価が未整備。</td>
</tr>
<tr>
<td>U8</td>
<td><strong>閉ループ安定性</strong>: 遅延・ノイズ・環境変動下で、モデルが破綻せず制御可能か。</td>
<td>I1/I6で要件整理。</td>
<td>遅延とジッタの実測に基づく安全運転領域の同定が不足。</td>
</tr>
<tr>
<td>U9</td>
<td><strong>OOD頑健性</strong>: 未学習環境・新規課題・雑音条件で同一性指標を維持できるか。</td>
<td>V3で問題を明確化。</td>
<td>劣化曲線の標準化（どの速度で崩れるか）が未確立。</td>
</tr>
<tr>
<td>U10</td>
<td><strong>熱力学的一貫性</strong>: 情報処理が物理的不可逆性・散逸制約を満たす実装条件を定式化できるか。</td>
<td>I9とIssue #58/#61/#62で理論整理が進展。</td>
<td>測定可能な実験指標（散逸率・因果密度・効率）の統一が未了。</td>
</tr>
<tr>
<td>U11</td>
<td><strong>摂動・自発・幾何 proxy の較正</strong>: PCI/PCI-ST、自発複雑性、criticality、manifold / topology 指標が、どの条件で整合しどの条件で解離するか。</td>
<td>V6 / V11 で benchmark hierarchy と補助解析の役割差を定義。</td>
<td>multicohort、no-report、perturbation 条件をまたぐ外部較正が不足。</td>
</tr>
<tr>
<td>U12</td>
<td><strong>分岐本人性（多重インスタンス）</strong>: 複数分岐後の個体ID・責任・評価帰属をどう扱うか。</td>
<td>V7で版管理の必要性を明示。</td>
<td>分岐時点と評価期間を固定した制度設計が未着手。</td>
</tr>
<tr>
<td>U13</td>
<td><strong>模倣分離テスト</strong>: 振る舞い模倣（LLM型）と因果構造保存を実験的に区別できるか。</td>
<td>Issue #10で3軸ベンチマーク、V8で統合方針。</td>
<td>介入・閉ループ・内部状態整合を同時に課すテスト群が不足。</td>
</tr>
<tr>
<td>U14</td>
<td><strong>追試可能性の実装</strong>: 第三者が同じデータ・手順で同一結論に到達できる運用を固定できるか。</td>
<td>P2/V9で必要条件は整理済み。</td>
<td>実行環境・差分ログ・失敗例公開の運用フローが不完全。</td>
</tr>
<tr>
<td>U15</td>
<td><strong>社会実装ガバナンス</strong>: 権利・同意・責任分配を技術評価と同期させて設計できるか。</td>
<td>D0-D2で論点抽出済み。</td>
<td>技術KPIと制度KPIの連動ルール（中止基準含む）が未定義。</td>
</tr>
</tbody>
</table>

<div class="note-box">
<strong>判定ルール</strong>
<p>
上のU0-U15は「良いアイデア」ではなく「反証可能な研究問題」です。各問題は、<strong>入力・出力・評価指標・失敗条件</strong>がそろって初めて「解いた」と判定します。
</p>
</div>

<h3>最重要3課題の追加分解（さらに深く）</h3>
<div class="stage-list">
<div class="stage-item">
<div class="stage-number">A</div>
<div class="stage-body">
<h4>U4 因果同値</h4>
<ul>
<li>介入辞書（刺激・課題・薬理）の最小完備集合をどう作るか。</li>
<li>反実仮想一致度（KL, JS, FIMなど）の閾値をどう校正するか。</li>
<li>偽介入・シャム条件で過大評価をどう抑えるか。</li>
<li>失敗時停止規則（Stop Rule）をどう事前登録するか。</li>
</ul>
</div>
</div>
<div class="stage-item">
<div class="stage-number">B</div>
<div class="stage-body">
<h4>U10 熱力学的一貫性</h4>
<ul>
<li>情報処理の散逸率をどの時間窓で測るか。</li>
<li>物理的不可逆性と計算論的不可逆性の差をどう扱うか。</li>
<li>実装基盤が変わっても比較可能な共通指標を作れるか。</li>
<li>エネルギー効率と因果性能のトレードオフをどう最適化するか。</li>
</ul>
</div>
</div>
<div class="stage-item">
<div class="stage-number">C</div>
<div class="stage-body">
<h4>U12 分岐本人性</h4>
<ul>
<li>分岐時点の定義（初期条件固定）をどこに置くか。</li>
<li>分岐後の評価帰属期間をどう設定するか。</li>
<li>複数分岐がある場合の責任分配と監査IDをどう管理するか。</li>
<li>法的主体性と技術的同一性の不一致をどう扱うか。</li>
</ul>
</div>
</div>
</div>
</section>

<section class="section" id="priorwork-map">
<h2 class="section-title">先行研究マップ（重点領域別）</h2>
<p>
未解決問題を解くために必要な先行研究を、分野別に整理します。目的は「文献の羅列」ではなく、<strong>どの問題に、どの証拠が効くか</strong>を明確にすることです。
</p>

<table class="data-table">
<thead>
<tr>
<th>領域</th>
<th>代表先行研究（抜粋）</th>
<th>U0-U15への寄与</th>
</tr>
</thead>
<tbody>
<tr>
<td>WBE基礎・本人性</td>
<td>Sandberg &amp; Bostrom (2008), Yamakawa et al. (2024), Parfit (1984), Clowes (2021), Weber (2025)</td>
<td>U0, U12, U15</td>
</tr>
<tr>
<td>意識理論と検証</td>
<td>Tononi (2015), Tononi et al. (2016), Albantakis et al. (2023), Doerig et al. (2019), Ferrante et al. (2025), Casali et al. (2013), Comolatti et al. (2019)</td>
<td>U0, U4, U11</td>
</tr>
<tr>
<td>EEG/MEG逆問題</td>
<td>Michel &amp; Brunet (2019), Wipf &amp; Nagarajan (2009), Cai et al. (2021), Sechet et al. (2025), Vorwerk et al. (2014), Medani et al. (2025)</td>
<td>U1, U2, U7</td>
</tr>
<tr>
<td>前処理・同期・接続性</td>
<td>Wilson et al. (2010), Thompson et al. (2013), Mowla et al. (2017), Belinskaia et al. (2020), Mansouri et al. (2018), Zrenner et al. (2018), Appelhoff &amp; Stenner (2021), Kothe et al. (2025)</td>
<td>U1, U7, U8, U14</td>
</tr>
<tr>
<td>デコーディング</td>
<td>Huth et al. (2016), Tang et al. (2023), D&eacute;fossez et al. (2023), Horikawa (2025), d'Ascoli et al. (2025), Willett et al. (2023), Littlejohn et al. (2025), Wairagkar et al. (2025), Wilson et al. (2025)</td>
<td>U4, U8, U9, U13</td>
</tr>
<tr>
<td>因果・能動的推論</td>
<td>Friston et al. (2003), Friston (2010), Friston (2017), Parr &amp; Friston (2019), Laukkonen et al. (2025), Correa et al. (2021)</td>
<td>U4, U5, U9</td>
</tr>
<tr>
<td>生物学的制約</td>
<td>Cook et al. (2019), Scheffer et al. (2020), Kasthuri et al. (2015), Santello et al. (2019), Ozcete et al. (2024), Gamlin et al. (2025)</td>
<td>U2, U3, U6, U7</td>
</tr>
<tr>
<td>計測拡張（OPM等）</td>
<td>Boto et al. (2018), Logothetis (2008), Purdon et al. (2013)</td>
<td>U2, U7, U8</td>
</tr>
<tr>
<td>標準化・再現性</td>
<td>Gorgolewski et al. (2016), Pernet et al. (2019), EEG-BIDS update, Open benchmark practices</td>
<td>U14</td>
</tr>
<tr>
<td>倫理・権利・法制度</td>
<td>Yuste et al. (2017), Ienca &amp; Andorno (2017), MIND Act discourse (2025)</td>
<td>U12, U15</td>
</tr>
<tr>
<td>熱力学・計算可能性</td>
<td>Seifert (2012), Kitazono et al. (2018), complexity reduction studies on IIT (2025)</td>
<td>U10, U11</td>
</tr>
</tbody>
</table>

<div class="key-points">
<h4>読む順序（実務向け）</h4>
<ul>
<li><strong>第1層:</strong> U1/U14（計測と再現性）を先に固める。ここが弱いと上位議論は全て不安定。</li>
<li><strong>第2層:</strong> U4/U9（因果と一般化）を介入ベースで検証し、模倣との差分を確立する。</li>
<li><strong>第3層:</strong> U10/U11/U12/U15（物理・同一性・制度）を、実証結果と接続して更新する。</li>
</ul>
</div>
</section>

<section class="section" id="template">
<h2 class="section-title">科学的中心問いページ用テンプレ（推奨）</h2>
<p>新しい技術提案や問いのページを作成する際は、以下のMarkdownテンプレートをコピーして使用することを推奨します。R0（復元対象）とV0（検証基準）を先に固定する思考フローを強制する構成になっています。</p>

<details>
<summary><strong>テンプレートを表示（クリックで展開）</strong></summary>
<pre style="background: #f6f8fa; padding: 16px; border-radius: 6px; white-space: pre-wrap; font-size: 0.85em; overflow-x: auto;">
## 科学的中心問いページ用テンプレ（全部入り・そのままコピペ可）

&gt; 目的：**「R0（復元対象）とV0（検証基準）を先に固定し、その上でM0（計測）とI0（同定可能性）を議論する」**順序を強制するテンプレです。
&gt; ※各セクションは“未確定なら未確定”と明記して進められる形にしてあります。

---

# 0. タイトル

* **ページ題名**：
* **一文要約（結論先出し）**：

  * 「本ページは、＿＿＿＿を＿＿＿＿の基準で復元可能にするために、必要な計測要件（時空間解像度・観測変数）を同定する。」

---

# 1. 中心問い（CQ）

* **中心問い**：

  * 「＿＿＿＿を、どの時空間解像度で取得すれば、“復元すべき対象（R0）”が一意に近づくか？」
* **問いの焦点**（どれを主戦場にするか）：

  * [ ] 観測変数の選定（何を測るか）
  * [ ] 解像度・カバレッジの下限（どの程度細かく/広く）
  * [ ] ノイズ・欠測・個体差の許容範囲
  * [ ] 因果（介入可能性）を含む同定

---

# 2. 用語・スコープ固定（曖昧さ潰し）

* **対象種**：ヒト／動物（種：＿＿＿）／シミュレーション
* **状態の範囲**：安静／課題中（課題：＿＿＿）／睡眠／薬理介入
* **時間スケール**：ミリ秒〜秒／分〜時／日〜年
* **空間スケール**：細胞／カラム／領域／全脳
* **「復元」の意味**（直観ではなく定義で）：＿＿＿＿

---

# 3. R0：復元対象（最重要・先に確定）

## 3.1 何を復元するのか（対象の定義）

* **復元対象 R0**：

  * 例）構造（結線）／ダイナミクス（状態遷移）／機能（入力→出力）／記憶・方略／主観報告を含む自己モデル など
* **R0の出力形式**（最終的に何が出てくれば“復元”と言えるか）：

  * 例）パラメータ集合、生成モデル、状態空間モデル、エージェント方策、シミュレータ など

## 3.2 同一性（同値関係）＝「成功」の定義

* **同値関係（何が同じなら成功か）**：

  * 「＿＿＿＿が一致すればR0は同一とみなす」
* **許容誤差**（どこまで違っても同一扱いか）：

  * 指標：＿＿＿＿、閾値：＿＿＿＿

## 3.3 前提（R0に暗黙に含めている仮定）

* 例）脳はマルコフ的／観測可能な潜在状態が存在／学習可能な関数クラスで表現可能 等
* **仮定一覧**：

  * A1：＿＿＿＿
  * A2：＿＿＿＿
  * A3：＿＿＿＿

---

# 4. V0：検証基準（合否テスト）

## 4.1 何をもって「復元できた」と言うか（テスト設計）

* **検証タスク**：＿＿＿＿
* **評価データ**：同一個体内／個体間一般化／条件外挿（反事実）
* **ベースライン**：＿＿＿＿（例：単純モデル、既存手法）

## 4.2 指標（定量）と合格ライン（閾値）

* **主要指標**：＿＿＿＿（例：予測精度、尤度、因果効果の一致、行動分布距離）
* **合格ライン**：＿＿＿＿（閾値 or 比率）
* **再現性要件**：n=＿＿＿、再現率＿＿＿、事前登録の有無＿＿＿

## 4.3 介入・因果を使う場合（推奨：可能なら入れる）

* **介入手段**：刺激／薬理／損傷／閉ループ制御
* **介入時の一致条件**：＿＿＿＿（“応答が一致”の定義）

---

# 5. M0：計測の前提（MEASUREMENT）

## 5.1 計測路線の前提（どれを想定するか）

* **想定**：

  * [ ] in vivo（非侵襲）
  * [ ] in vivo（侵襲）
  * [ ] 破壊スキャン（ex vivo / 将来像）
* **安全・倫理・スケール制約**：＿＿＿＿

## 5.2 観測対象（何を測るか）候補リスト

* 電気：EEG/MEG/ECoG/単一・多点
* 血流：fMRI/fNIRS
* 光学：Ca imaging 等
* 構造：MRI/DTI/EM など
* **このページで主に扱う観測量**：＿＿＿＿

## 5.3 期待する時空間解像度・カバレッジ

* **時間分解能**：＿＿＿＿
* **空間分解能**：＿＿＿＿
* **被覆範囲**：局所／広域／全脳
* **サンプリング制約（持続時間・回数）**：＿＿＿＿
* **ノイズ床・欠測**：＿＿＿＿

---

# 6. P0：推定モデル／表現（モデル仮定を明示）

* **推定したい潜在表現**：状態空間／因子モデル／生成モデル／エージェント方策／コネクトーム等
* **学習パラダイム**：教師あり／自己教師／同化（data assimilation）／シミュレータ併用
* **必要な帰納バイアス**：＿＿＿＿（例：低次元、スパース、対称性、解剖学制約）
* **計算資源・実装制約**：＿＿＿＿

---

# 7. I0：同定可能性（このページの“芯”）

## 7.1 主張（1〜2文で）

* **I0主張**：

  * 「R0を一意に近づけるには、観測量＿＿＿＿を、時間＿＿＿＿・空間＿＿＿＿以上で取得する必要がある（少なくとも＿＿＿＿が下限）。」

## 7.2 必要条件（下限：これが無いと無理）

* **必要条件（観測の最小セット）**：＿＿＿＿
* **直観／根拠**：未観測自由度が残る／多対一写像になる／ノイズで不可分になる 等
* **“同定不能”の具体例**：＿＿＿＿（同じ観測を生む別解が構成できる 等）

## 7.3 十分条件（上限：ここまで取れれば原理的に可能）

* **十分条件**：＿＿＿＿
* **現実性**：今は不可能／将来可能性／代替案

## 7.4 失敗モード（重要：先回りで列挙）

* [ ] 多対一（別R0が同じ観測を生む）
* [ ] モデルミススペ（P0が間違っている）
* [ ] 介入不足で因果が切り分けられない
* [ ] 個体差で一般化が破れる
* [ ] ノイズ床・欠測で識別不能
* **検出方法**：＿＿＿＿（どの指標で“失敗”と判定するか）

## 7.5 「一意に近づく」を測る尺度

* **一意性スコア**（候補）：事後分布の集中度／同値類サイズ／識別距離 など
* **採用する尺度**：＿＿＿＿

---

# 8. 戦略分岐（A/B/C）※例のまま使える形

&gt; 各分岐は「M0の違い」だけでなく、**V0に到達する経路**と**I0を満たす見込み**を必ずセットで書きます。

## A：非侵襲（EEG/MEG/fMRI等）でモデルを鍛える

* **狙い**：＿＿＿＿（例：大規模・長期データで汎化を稼ぐ）
* **M0**：＿＿＿＿（解像度・カバレッジ・制約）
* **P0**：＿＿＿＿（表現・学習）
* **V0への到達経路**：＿＿＿＿（どのテストに通すか）
* **I0上のボトルネック**：＿＿＿＿（何が同定不能になりやすいか）
* **この分岐で得る“判定情報”**：＿＿＿＿（次の分岐選択に効く情報）

## B：侵襲（ECoG/深部/動物）で因果推論を強化

* **狙い**：＿＿＿＿（例：介入で因果・同定を強める）
* **M0**：＿＿＿＿
* **P0**：＿＿＿＿
* **V0への到達経路**：＿＿＿＿
* **I0上の改善点**：＿＿＿＿（介入で多対一を潰す等）
* **外挿（ヒト一般化）の扱い**：＿＿＿＿

## C：破壊的・超高解像度で構造を取る（将来像）

* **狙い**：＿＿＿＿（例：十分条件側の上限を検討）
* **M0**：＿＿＿＿（取得可能な構造情報）
* **P0**：＿＿＿＿（構造→機能の写像仮定）
* **V0への到達経路**：＿＿＿＿
* **I0の結論**：＿＿＿＿（原理的に十分か／まだ不足か）

---

# 9. 反証条件・停止規則（Stop rule）

## 9.1 全体反証（ページの根本を否定する条件）

* **反証条件**：

  * 「R0（復元対象）が定義されないまま計測だけ高級化しても、同定不能が解消されない」
  * 具体的には：＿＿＿＿（同じ観測で別R0が構成できる、V0を通らない 等）

## 9.2 分岐別の停止規則（撤退ライン）

* Aの停止：＿＿＿＿
* Bの停止：＿＿＿＿
* Cの停止：＿＿＿＿
* **ピボット条件**：＿＿＿＿（A→Bへ、B→Cへ、等の判断基準）

---

# 10. 次アクション（このページ内の優先順位を固定）

* **まず確定する**：

  1. R0（復元対象・同値関係）
  2. V0（合否テスト）
  3. I0（必要条件の下限主張）
* **今週やること**：＿＿＿＿
* **次に書き足すセクション**：＿＿＿＿
* **未確定の論点（質問リスト）**：

  * Q1：＿＿＿＿
  * Q2：＿＿＿＿

---

## 付録：1ページで俯瞰する「要点サマリ」枠（任意）

* **R0**：＿＿＿＿
* **V0**：＿＿＿＿
* **M0**：＿＿＿＿
* **P0**：＿＿＿＿
* **I0結論（下限/上限）**：＿＿＿＿
* **採用する分岐**：A/B/C（理由：＿＿＿＿）
* **反証・停止**：＿＿＿＿

---
</pre>
</details>
</section>

<section class="section" id="learning">
<h2 class="section-title">学習の順序（最短で全体像）</h2>
<p>“順番”は重要です。計測に強くても、検証基準が曖昧だと前進を主張できません。逆に、検証だけが立派でも、復元対象が定義できていなければ実装が迷走します。</p>
<ol>
<li><strong>全体像：</strong>WBEロードマップ（大枠の工程・ボトルネック）</li>
<li><strong>計測：</strong>どの解像度で何が失われるか（EEG/fMRI/侵襲/コネクトーム）</li>
<li><strong>再構成：</strong>逆問題→状態推定→生成モデル→介入予測、の順で“反証可能な復元”へ</li>
<li><strong>実装：</strong>モデル粒度を固定し、実行基盤差の影響を監査可能にする</li>
<li><strong>検証：</strong>評価スイートと反証条件を先に書き、更新履歴を残す</li>
</ol>
</section>



<section class="section" id="sources">
<h2 class="section-title">先行研究リスト（拡張版）</h2>
<p>
以下は、U0-U15の未解決問題に直接関係する主要文献です。詳細な拡張一覧は <a href="mind_uploading_papers.html">Paper Collection</a> と <a href="perspective.html#references">PerspectiveのReferences</a> を併読してください。
</p>

<h3>A. WBE基礎・本人性・哲学</h3>
<ol>
<li>Sandberg, A., &amp; Bostrom, N. (2008). <em>Whole Brain Emulation: A Roadmap</em>.</li>
<li>Yamakawa, H., et al. (2024). Technology roadmap toward the completion of whole-brain architecture.</li>
<li>Parfit, D. (1984). <em>Reasons and Persons</em>.</li>
<li>Whitehead, A. N. (1929). <em>Process and Reality</em>.</li>
<li>Clowes, R. W. (2021). Slow Continuous Mind Uploading.</li>
<li>Weber, C. (2025). The multiplicity objection against uploading optimism.</li>
</ol>

<h3>B. 意識理論・検証指標</h3>
<ol>
<li>Tononi, G. (2015). Integrated information theory.</li>
<li>Tononi, G., et al. (2016). IIT: from consciousness to its physical substrate.</li>
<li>Albantakis, L., et al. (2023). IIT 4.0.</li>
<li>Doerig, A., et al. (2019). The unfolding argument.</li>
<li>Boly, M., et al. (2017). Front vs back NCC debate.</li>
<li>Tsuchiya, N., et al. (2015). No-report paradigms.</li>
<li>Casali, A. G., et al. (2013). PCI.</li>
<li>Comolatti, R., et al. (2019). PCI-ST.</li>
<li>Ferrante, O., et al. (2025). Adversarial testing of GNWT and IIT.</li>
<li>Cohen, M. A., et al. (2024). Neural signatures of visual awareness independent of postperceptual processing.</li>
<li>Fahrenfort, J. J., et al. (2025). Criterion placement threatens the construct validity of neural measures of conscious contents.</li>
<li>Casarotto, S., et al. (2024). Dissociations between spontaneous electroencephalographic features and perturbational complexity index in the minimally conscious state.</li>
<li>Maschke, C., et al. (2024). Critical dynamics in spontaneous EEG predict anesthetic-induced loss of consciousness and perturbational complexity.</li>
<li>Yoon, B., et al. (2024). Tracking the topology of neural manifolds across populations.</li>
<li>The topological structure of population activity in mouse visual cortex encodes visual stimuli. (2024).</li>
<li>Massimini, M., et al. (2005). Breakdown of effective connectivity during sleep.</li>
</ol>

<h3>C. 計測・逆問題・不確実性推定</h3>
<ol>
<li>Michel, C. M., &amp; Brunet, D. (2019). EEG source imaging review.</li>
<li>Wipf, D., &amp; Nagarajan, S. (2009). Unified Bayesian framework for MEG/EEG source imaging.</li>
<li>Cai, C., et al. (2021). Robust noise estimation with Champagne. <a href="https://doi.org/10.1016/j.neuroimage.2020.117411" target="_blank">doi:10.1016/j.neuroimage.2020.117411</a></li>
<li>Sechet, D., Kowalski, M., Mokhtari, S., &amp; Torrésani, B. (2025). Revisiting CHAMPAGNE: Sparse Bayesian Learning as Reweighted Sparse Coding. <a href="https://doi.org/10.1109/SAMPTA64769.2025.11133512" target="_blank">doi:10.1109/SAMPTA64769.2025.11133512</a></li>
<li>Feng, Z., Mishne, G., Hashemi, A., et al. (2025). Block-Champagne: Imaging Extended E/MEG Source Activation with Empirical Bayesian Uncertainty Quantification. <a href="https://doi.org/10.1109/TMI.2025.3642620" target="_blank">doi:10.1109/TMI.2025.3642620</a></li>
<li>Vorwerk, J., et al. (2014). Head volume conductor modeling guideline.</li>
<li>Aydin, U., Vorwerk, J., K&uuml;pper, P., et al. (2019). Influence of head tissue conductivity uncertainties on EEG dipole reconstruction. <a href="https://doi.org/10.3389/fnins.2019.00531" target="_blank">doi:10.3389/fnins.2019.00531</a></li>
<li>Mikulan, E., Russo, S., Bares, M., et al. (2020). Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. <a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">doi:10.1038/s41597-020-0467-x</a></li>
<li>Seeber, M., Cantonas, L.-M., Hoevels, M., et al. (2019). Subcortical electrophysiological activity is detectable with high-density EEG source imaging. <a href="https://doi.org/10.1038/s41467-019-08725-w" target="_blank">doi:10.1038/s41467-019-08725-w</a></li>
<li>Unnwongse, K., Achakulvisut, T., Wu, J. Y., et al. (2023). Direct validation of EEG source imaging by intracranial electric stimulation in human patients. <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">doi:10.1093/braincomms/fcad023</a></li>
<li>Hao, S., Zhao, H., Feng, Z., et al. (2025). HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. <a href="https://doi.org/10.1111/epi.18552" target="_blank">doi:10.1111/epi.18552</a></li>
<li>Logothetis, N. K., Pauls, J., Augath, M., Trinath, T., &amp; Oeltermann, A. (2001). Neurophysiological investigation of the basis of the fMRI signal. <a href="https://doi.org/10.1038/35084005" target="_blank">doi:10.1038/35084005</a></li>
<li>Lee, J. H., Durand, R., Gradinaru, V., et al. (2010). Global and local fMRI signals driven by neurons defined optogenetically by type and wiring. <a href="https://doi.org/10.1038/nature09108" target="_blank">doi:10.1038/nature09108</a></li>
<li>Sirotin, Y. B., &amp; Das, A. (2009). Anticipatory haemodynamic signals in sensory cortex not predicted by local neuronal activity. <a href="https://doi.org/10.1038/nature07664" target="_blank">doi:10.1038/nature07664</a></li>
<li>Cardoso, M. M. B. M., Sirotin, Y. B., Lima, B., Glushenkova, E., &amp; Das, A. (2012). The neuroimaging signal is a linear sum of neurally distinct stimulus- and task-related components. <a href="https://doi.org/10.1038/nn.3170" target="_blank">doi:10.1038/nn.3170</a></li>
<li>Handwerker, D. A., Ollinger, J. M., &amp; D'Esposito, M. (2004). Variation of BOLD hemodynamic responses across subjects and brain regions and their effects on statistical analyses. <a href="https://doi.org/10.1016/j.neuroimage.2003.11.029" target="_blank">doi:10.1016/j.neuroimage.2003.11.029</a></li>
<li>Bailes, J., Millman, R., Franklin, C., et al. (2023). Resting-state fMRI signals contain spectral signatures of local hemodynamic response timing. <a href="https://doi.org/10.7554/eLife.86453" target="_blank">doi:10.7554/eLife.86453</a></li>
<li>Kay, K. N., Jamison, K. W., Zhang, R. Y., &amp; Uğurbil, K. (2019). A critical assessment of data quality and venous effects in sub-millimeter fMRI. <a href="https://doi.org/10.1016/j.neuroimage.2019.02.006" target="_blank">doi:10.1016/j.neuroimage.2019.02.006</a></li>
<li>Kurzawski, J. W., Yablonskiy, D. A., Pointer, R., et al. (2022). Non-Neural Factors Influencing BOLD Response Magnitudes within Individual Subjects. <a href="https://doi.org/10.1523/JNEUROSCI.2532-21.2022" target="_blank">doi:10.1523/JNEUROSCI.2532-21.2022</a></li>
<li>Logothetis, N. K. (2008). What we can do and what we cannot do with fMRI. <a href="https://doi.org/10.1038/nature06976" target="_blank">doi:10.1038/nature06976</a></li>
<li>Purdon, P. L., et al. (2013). EEG signatures of loss/recovery of consciousness.</li>
<li>Boto, E., et al. (2018). Wearable OPM-MEG.</li>
<li>Steinmetz, N. A., Aydin, C., Lebedeva, A., et al. (2021). Neuropixels 2.0: A miniaturized high-density probe for stable, long-term brain recordings. <a href="https://doi.org/10.1126/science.abf4588" target="_blank">doi:10.1126/science.abf4588</a></li>
<li>Pachitariu, M., et al. (2024). Spike sorting with Kilosort4. <a href="https://doi.org/10.1038/s41592-024-02595-5" target="_blank">doi:10.1038/s41592-024-02595-5</a></li>
<li>Trautmann, E. M., Stavisky, S. D., Lahiri, S., et al. (2019). Accurate estimation of neural population dynamics without spike sorting. <a href="https://doi.org/10.1016/j.neuron.2019.05.003" target="_blank">doi:10.1016/j.neuron.2019.05.003</a></li>
<li>van Beest, E. H., Jia, X., Deng, X., et al. (2025). Tracking neurons across days with high-density probes. <a href="https://doi.org/10.1038/s41592-024-02440-1" target="_blank">doi:10.1038/s41592-024-02440-1</a></li>
</ol>

<h3>D. 前処理・同期・ネットワーク解析</h3>
<ol>
<li>Chang, C.-Y., et al. (2018). Evaluation of Artifact Subspace Reconstruction.</li>
<li>de Cheveigne, A. (2020). ZapLine.</li>
<li>Vinck, M., et al. (2011). Weighted Phase Lag Index (wPLI).</li>
<li>Staniek, M., &amp; Lehnertz, K. (2008). Symbolic Transfer Entropy.</li>
<li>Wilson, J. A., Mellinger, J., Schalk, G., &amp; Williams, J. C. (2010). A procedure for measuring latencies in brain-computer interfaces. <a href="https://doi.org/10.1109/TBME.2010.2047259" target="_blank">doi:10.1109/TBME.2010.2047259</a></li>
<li>Thompson, D. E., Warschausky, S. A., &amp; Huggins, J. E. (2013). Classifier-based latency estimation: a novel way to estimate and predict BCI accuracy. <a href="https://doi.org/10.1088/1741-2560/10/1/016006" target="_blank">doi:10.1088/1741-2560/10/1/016006</a></li>
<li>Mowla, M. R., Huggins, J. E., &amp; Thompson, D. E. (2017). Enhancing P300-BCI performance using latency estimation. <a href="https://doi.org/10.1080/2326263X.2017.1338010" target="_blank">doi:10.1080/2326263X.2017.1338010</a></li>
<li>Belinskaia, A., Smetanin, N., Lebedev, M., &amp; Ossadtchi, A. (2020). Short-delay neurofeedback facilitates training of the parietal alpha rhythm. <a href="https://doi.org/10.1088/1741-2552/abc8d7" target="_blank">doi:10.1088/1741-2552/abc8d7</a></li>
<li>Mansouri, F., Fettes, P., Schulze, L., et al. (2018). A real-time phase-locking system for non-invasive brain stimulation. <a href="https://doi.org/10.3389/fnins.2018.00877" target="_blank">doi:10.3389/fnins.2018.00877</a></li>
<li>Zrenner, C., Desideri, D., Belardinelli, P., &amp; Ziemann, U. (2018). Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in the human motor cortex. <a href="https://doi.org/10.1016/j.brs.2017.11.016" target="_blank">doi:10.1016/j.brs.2017.11.016</a></li>
<li>Little, S., Pogosyan, A., Neal, S., et al. (2013). Adaptive deep brain stimulation in advanced Parkinson disease. <a href="https://doi.org/10.1002/ana.23951" target="_blank">doi:10.1002/ana.23951</a></li>
<li>Tinkhauser, G., Pogosyan, A., Little, S., et al. (2017). The modulatory effect of adaptive deep brain stimulation on beta bursts in Parkinson's disease. <a href="https://doi.org/10.1093/brain/awx010" target="_blank">doi:10.1093/brain/awx010</a></li>
<li>Hernandez-Pavon, J. C., Metsomaa, J., Mutanen, T. P., et al. (2023). TMS combined with EEG: Recommendations and open issues. <a href="https://doi.org/10.1016/j.brs.2023.02.009" target="_blank">doi:10.1016/j.brs.2023.02.009</a></li>
<li>Appelhoff, S., &amp; Stenner, T. (2021). In COM we trust: Feasibility of USB-based event marking. <a href="https://doi.org/10.3758/s13428-021-01571-z" target="_blank">doi:10.3758/s13428-021-01571-z</a></li>
<li>Kothe, C., Shirazi, S. Y., Stenner, T., et al. (2025). The lab streaming layer for synchronized multimodal recording. <a href="https://doi.org/10.1162/IMAG.a.136" target="_blank">doi:10.1162/IMAG.a.136</a></li>
</ol>

<h3>E. デコーディング・生成モデル・模倣分離</h3>
<ol>
<li>Huth, A. G., de Heer, W. A., Griffiths, T. L., Theunissen, F. E., &amp; Gallant, J. L. (2016). Natural speech reveals the semantic maps that tile human cerebral cortex. <a href="https://doi.org/10.1038/nature17637" target="_blank">doi:10.1038/nature17637</a></li>
<li>Tang, J., LeBel, A., Jain, S., et al. (2023). Semantic reconstruction of continuous language from non-invasive brain recordings. <a href="https://doi.org/10.1038/s41593-023-01304-9" target="_blank">doi:10.1038/s41593-023-01304-9</a></li>
<li>D&eacute;fossez, A., Caucheteux, C., Rapin, J., Kabeli, O., &amp; King, J.-R. (2023). Decoding speech perception from non-invasive brain recordings. <a href="https://doi.org/10.1038/s42256-023-00714-5" target="_blank">doi:10.1038/s42256-023-00714-5</a></li>
<li>Horikawa, T. (2025). Mind captioning: Evolving descriptive text of mental content from human brain activity. <a href="https://doi.org/10.1126/sciadv.adw1464" target="_blank">doi:10.1126/sciadv.adw1464</a></li>
<li>d'Ascoli, S., Ferrante, O., et al. (2025). Towards decoding individual words from non-invasive brain recordings. <a href="https://doi.org/10.1038/s41467-025-65499-0" target="_blank">doi:10.1038/s41467-025-65499-0</a></li>
<li>Willett, F. R., Kunz, E. M., Fan, C., et al. (2023). A high-performance speech neuroprosthesis. <a href="https://doi.org/10.1038/s41586-023-06377-x" target="_blank">doi:10.1038/s41586-023-06377-x</a></li>
<li>Littlejohn, K. T., Dabagia, M., Ladwig, A., et al. (2025). A streaming brain-to-voice neuroprosthesis to restore naturalistic communication. <a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">doi:10.1038/s41593-025-01905-6</a></li>
<li>Wairagkar, M., Card, N. S., Singer-Clark, T., et al. (2025). An instantaneous voice-synthesis neuroprosthesis. <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">doi:10.1038/s41586-025-09127-3</a></li>
<li>Wilson, G. H., Stein, E. A., Kamdar, F., et al. (2025). Long-term unsupervised recalibration of cursor-based intracortical brain&ndash;computer interfaces using a hidden Markov model. <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">doi:10.1038/s41551-025-01536-z</a></li>
</ol>

<h3>F. 因果推論・能動的推論・反実仮想</h3>
<ol>
<li>Friston, K. J., Harrison, L., &amp; Penny, W. (2003). Dynamic causal modelling.</li>
<li>Penny, W. D., Stephan, K. E., Mechelli, A., &amp; Friston, K. J. (2004). Comparing dynamic causal models. <a href="https://doi.org/10.1016/j.neuroimage.2004.03.026" target="_blank">doi:10.1016/j.neuroimage.2004.03.026</a></li>
<li>Friston, K. (2010). Free-energy principle.</li>
<li>Friston, K. (2017). Active inference: a process theory.</li>
<li>Parr, T., &amp; Friston, K. J. (2019). Generalised free energy.</li>
<li>Lee, H.-L., Zahneisen, B., Hugger, T., et al. (2017). Tracking dynamic effective connectivity from fMRI using changes induced by anesthesia. <a href="https://doi.org/10.1016/j.neuroimage.2017.02.012" target="_blank">doi:10.1016/j.neuroimage.2017.02.012</a></li>
<li>Hauser, A., &amp; B&uuml;hlmann, P. (2012). Characterization and greedy learning of interventional Markov equivalence classes of directed acyclic graphs. <a href="https://jmlr.org/papers/v13/hauser12a.html" target="_blank">JMLR</a></li>
<li>Vink, J. J., Ramos-Nu&ntilde;ez, A. I., Bellesi, A., et al. (2020). The brain's functional connectome is a poor predictor of the brain's causal activity flow. <a href="https://doi.org/10.1371/journal.pcbi.1007866" target="_blank">doi:10.1371/journal.pcbi.1007866</a></li>
<li>Laukkonen, R., Friston, K., &amp; Chandaria, S. (2025). A beautiful loop.</li>
<li>Correa, J. D., Lee, S., &amp; Bareinboim, E. (2021). Nested counterfactual identification.</li>
</ol>

<h3>G. 生物学的制約（コネクトーム・神経修飾・グリア）</h3>
<ol>
<li>Cook, S. J., et al. (2019). Whole-animal connectomes of both <em>C. elegans</em> sexes.</li>
<li>Scheffer, L. K., et al. (2020). Adult <em>Drosophila</em> central brain connectome.</li>
<li>Kasthuri, N., et al. (2015). Saturated reconstruction of neocortex volume.</li>
<li>Santello, M., et al. (2019). Astrocyte-neuron interactions.</li>
<li>Ozcete, O. D., et al. (2024). Neuromodulatory volume transmission.</li>
<li>Dorkenwald, S., et al. (2024). Neuronal wiring diagram of an adult brain. <a href="https://doi.org/10.1038/s41586-024-07558-y" target="_blank">doi:10.1038/s41586-024-07558-y</a></li>
<li>MICrONS Consortium, et al. (2025). Functional connectomics spanning multiple areas of mouse visual cortex. <a href="https://doi.org/10.1038/s41586-025-08790-w" target="_blank">doi:10.1038/s41586-025-08790-w</a></li>
<li>Gamlin, C. R., et al. (2025). Connectomics of predicted Sst transcriptomic types in mouse visual cortex. <a href="https://doi.org/10.1038/s41586-025-08805-6" target="_blank">doi:10.1038/s41586-025-08805-6</a></li>
<li>Cahill, M. K., et al. (2024). Network-level encoding of local neurotransmitters in cortical astrocytes. <a href="https://doi.org/10.1038/s41586-024-07311-5" target="_blank">doi:10.1038/s41586-024-07311-5</a></li>
</ol>

<h3>H. 標準化・再現性・倫理・制度</h3>
<ol>
<li>Gorgolewski, K. J., et al. (2016). BIDS.</li>
<li>Pernet, C. R., et al. (2019). EEG-BIDS.</li>
<li>Fleming, S. M., et al. (2023). Open letter on IIT interpretability and testability.</li>
<li>Yuste, R., et al. (2017). Four ethical priorities for neurotechnologies and AI.</li>
<li>Ienca, M., &amp; Andorno, R. (2017). New human rights in neuroscience.</li>
<li>Schumer, C., et al. (2025). MIND Act discourse.</li>
</ol>

<h3>I. 熱力学・不可逆性・エネルギー予算</h3>
<ol>
<li>B&eacute;rut, A., Arakelyan, A., Petrosyan, A., et al. (2012). Experimental verification of Landauer&rsquo;s principle linking information and thermodynamics. <a href="https://doi.org/10.1038/nature10872" target="_blank">doi:10.1038/nature10872</a></li>
<li>Attwell, D., &amp; Laughlin, S. B. (2001). An energy budget for signaling in the grey matter of the brain. <a href="https://doi.org/10.1097/00004647-200110000-00001" target="_blank">doi:10.1097/00004647-200110000-00001</a></li>
<li>Lynn, C. W., Cornblath, E. J., Papadopoulos, L., et al. (2021). Broken detailed balance and entropy production in the human brain. <a href="https://doi.org/10.1073/pnas.2109889118" target="_blank">doi:10.1073/pnas.2109889118</a></li>
<li>de la Fuente, L. A., Perl, Y. S., Zamberlan, F., et al. (2023). Temporal irreversibility of neural dynamics as a signature of consciousness. <a href="https://doi.org/10.1093/cercor/bhac177" target="_blank">doi:10.1093/cercor/bhac177</a></li>
<li>Nartallo-Kaluarachchi, R., Bonetti, L., Fern&aacute;ndez-Rubio, G., et al. (2025). Multilevel irreversibility reveals higher-order organization of nonequilibrium interactions in human brain dynamics. <a href="https://doi.org/10.1073/pnas.2408791122" target="_blank">doi:10.1073/pnas.2408791122</a></li>
<li>Ishihara, K., &amp; Shimazaki, H. (2025). State-space kinetic Ising model reveals task-dependent entropy flow in sparsely active nonequilibrium neuronal dynamics. <a href="https://doi.org/10.1038/s41467-025-66669-w" target="_blank">doi:10.1038/s41467-025-66669-w</a></li>
</ol>
</section>

</article>

<aside class="sidebar-column">

<div class="key-points">
<h4>このページで得るもの</h4>
<ul>
<li>問いの木（詳細版）を1ページに集約</li>
<li>前進の定義（クレーム階段）の固定</li>
<li>折りたたみ＋絞り込みで探索</li>
<li>学習の順序（迷子にならない）</li>
<li>最初に当たる一次/総説リンク</li>
</ul>
</div>

<div class="sidebar-box">
<h4>Filter</h4>
<input id="qaSearch" class="filter-input" type="text" placeholder="キーワードで絞り込み（例: EEG, 因果, 本人性）">
<p class="small" style="margin-top: 10px;">カテゴリ</p>
<div class="checkbox-grid" style="margin-top: 8px;">
<label><input type="checkbox" name="qaTag" value="meta">Meta</label>
<label><input type="checkbox" name="qaTag" value="measurement">Measurement</label>
<label><input type="checkbox" name="qaTag" value="reconstruction">Reconstruction</label>
<label><input type="checkbox" name="qaTag" value="implementation">Implementation</label>
<label><input type="checkbox" name="qaTag" value="verification">Verification</label>
<label><input type="checkbox" name="qaTag" value="deployment">Deployment</label>
</div>
<div class="controls" style="margin-top: 12px;">
<button class="btn" id="qaClear" type="button">Clear</button>
<button class="btn" id="qaExpandAll" type="button">Expand</button>
<button class="btn" id="qaCollapseAll" type="button">Collapse</button>
</div>
<p class="small" id="qaStatus" style="margin-top: 10px;">表示: -/-</p>
</div>

<div class="sidebar-box">
<h4>On this page</h4>
<ul>
<li><a href="#howto">How to Use</a></li>
<li><a href="#measurement-identifiability-audit">2026-03 文献監査</a></li>
<li><a href="#definition">前進の定義</a></li>
<li><a href="#roadmap-index">索引</a></li>
<li><a href="#tree">問いの木</a></li>
<li><a href="#measurement">計測</a></li>
<li><a href="#reconstruction">再構成</a></li>
<li><a href="#implementation">実装</a></li>
<li><a href="#verification">検証</a></li>
<li><a href="#unsolved">未解決問題の定義</a></li>
<li><a href="#priorwork-map">先行研究マップ</a></li>
<li><a href="#deployment">社会実装</a></li>
<li><a href="#learning">学習の順序</a></li>
<li><a href="#mind-upload">Mind-Upload の現在地</a></li>
<li><a href="#sources">参考文献</a></li>
</ul>
</div>

<div class="sidebar-box">
<h4>Links</h4>
<ul>
<li><a href="index.html">Start</a></li>
<li><a href="issue.html#proposal-integration">Issue内の提案統合節</a></li>
<li><a href="mind_uploading_papers.html">Paper Collection</a></li>
<li><a href="brain_science_dictionary.html">Brain Science Dictionary</a></li>
<li><a href="https://github.com/yasufumi-nakata/mind-upload" target="_blank">GitHub Repository</a></li>
<li><a href="issue.html">Contribute Guide</a></li>
</ul>
</div>

</aside>
</main>

<footer>
<p>Mind-Upload · 技術ロードマップ（暫定）</p>
</footer>

<script>
(function () {
var searchInput = document.getElementById('qaSearch');
var clearBtn = document.getElementById('qaClear');
var expandBtn = document.getElementById('qaExpandAll');
var collapseBtn = document.getElementById('qaCollapseAll');
var statusEl = document.getElementById('qaStatus');

if (!searchInput || !statusEl) return;

function toArray(nodeList) {
return Array.prototype.slice.call(nodeList || []);
}

var checkboxes = toArray(document.querySelectorAll('input[name="qaTag"]'));
var qas = toArray(document.querySelectorAll('details.qa'));
var groups = toArray(document.querySelectorAll('[data-qa-group]'));

function selectedTags() {
return checkboxes
.filter(function (cb) { return cb.checked; })
.map(function (cb) { return cb.value; });
}

function matchesTags(qaTags, selected) {
if (!selected.length) return true;
for (var i = 0; i < selected.length; i++) {
if (qaTags.indexOf(selected[i]) !== -1) return true;
}
return false;
}

function matchesText(text, query) {
if (!query) return true;
return text.indexOf(query) !== -1;
}

function applyFilters() {
var query = (searchInput.value || '').trim().toLowerCase();
var selected = selectedTags();
var visibleCount = 0;

qas.forEach(function (qa) {
var qaTags = (qa.getAttribute('data-tags') || '')
.split(/\s+/)
.filter(Boolean);
var text = (qa.textContent || '').toLowerCase();
var show = matchesTags(qaTags, selected) && matchesText(text, query);
qa.style.display = show ? '' : 'none';
if (show) visibleCount += 1;
});

groups.forEach(function (g) {
var groupQas = toArray(g.querySelectorAll('details.qa'));
var anyVisible = groupQas.some(function (qa) { return qa.style.display !== 'none'; });
g.style.display = anyVisible ? '' : 'none';
});

statusEl.textContent = '表示: ' + visibleCount + '/' + qas.length;
}

function visibleQAs() {
return qas.filter(function (qa) { return qa.style.display !== 'none'; });
}

searchInput.addEventListener('input', applyFilters);
checkboxes.forEach(function (cb) { cb.addEventListener('change', applyFilters); });

if (clearBtn) {
clearBtn.addEventListener('click', function () {
searchInput.value = '';
checkboxes.forEach(function (cb) { cb.checked = false; });
applyFilters();
searchInput.focus();
});
}

if (expandBtn) {
expandBtn.addEventListener('click', function () {
visibleQAs().forEach(function (d) { d.open = true; });
});
}

if (collapseBtn) {
collapseBtn.addEventListener('click', function () {
visibleQAs().forEach(function (d) { d.open = false; });
});
}

applyFilters();
})();
</script>
