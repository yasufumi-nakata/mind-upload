---
layout: default
title: "用語集（Glossary）"
description: "Mind-Uploadで頻出する用語を、人間が迷子にならない粒度でまとめます。厳密定義はRoadmapにリンクします。"
article_type: Reference
subtitle: "まずは“言葉のすり替え”を止める"
author: Mind Uploading Research Project
last_updated: "2026-03-16"
note: "Living document"
audience: "用語で止まりたくない人、言葉のすり替えを防ぎたい人"
reading_time: "必要な項目だけなら3〜10分"
page_intro: "このページは、Mind-Upload でよく出る言葉を『まず日常語で理解し、そのあと必要なら厳密に戻る』ための用語集です。議論で迷子にならないように、難しい単語を測定や検証の話に結び付けて説明します。"
accuracy_note: "ここに書く説明は入口用の短い定義です。厳密な使い方は、リンク先の本文や元論文で確認してください。"
page_highlights:
  - "用語を短く説明しつつ、どこで使う概念かも一緒に示します。"
  - "『似ているが違う』語を分けることで、話のすり替えを防ぎます。特に observability / identifiability / direct validation を混ぜないことを重視します。"
  - "detectable / localized / identified / validated / deployable は別レベルの主張であり、同じ成功ではありません。"
  - "brain signal / language prior / Neural Contribution Card を分けることで、decode 系デモの過大解釈を防ぎます。"
  - "分からない言葉が出たら、このページに戻れば最低限の足場を作れます。"
known_points:
  - "用語の混同を減らすだけで、議論の多くのすれ違いは防げます。"
  - "特に decode / emulate、相関 / 因果、observability / identifiability、モデル適合 / direct validation、brain signal / language prior の区別は重要です。"
  - "connectivity、calibration、abstention、recalibration burden も、2026-03 時点では独立に監査すべき語です。"
  - "このページは短い定義の入口であり、本文への戻り先を作る役割を持ちます。"
unknown_points:
  - "意識理論まわりの用語は、論文や立場で意味の置き方が少しずつ異なります。"
  - "短い定義だけで、研究上の争点まで完全に片づくわけではありません。"
  - "calibration / abstention / deployability の共通 pass/fail を site-wide にどこまで固定するかはまだ検討中です。"
wiki_links:
  - label: "Wiki: WBEの基本"
    url: "/wiki/mind-upload-basics.html"
    description: "用語が使われる全体像を先に見たいときの入口です。"
  - label: "Wiki: 公開ページの読み分けガイド"
    url: "/wiki/public-page-reading-guide.html"
    description: "用語確認のあとに、どの公開ページへ戻るかを整理します。"
  - label: "Wiki: 意識理論マップ"
    url: "/wiki/consciousness-theory-map.html"
    description: "IIT、GNWT、FEP、PCI の違いを表で整理した補助ページです。"
  - label: "Wiki: EEGの基本"
    url: "/wiki/eeg-basics.html"
    description: "EEG 関連語を、測定の流れに沿って理解したい人向けです。"
  - label: "Wiki: 計測からモデル化まで"
    url: "/wiki/measurement-and-modeling-terms.html"
    description: "EEG、QC、BIDS、ESI、DCM、SCM を 1 本の流れで整理します。"
  - label: "Wiki: 観測から推定へ"
    url: "/wiki/observation-to-estimation.html"
    description: "逆問題、ESI、DCM、SCM、因果同値類をもう一段ていねいに整理します。"
  - label: "Wiki: 不確実性・校正・棄権"
    url: "/wiki/uncertainty-confidence-and-abstention.html"
    description: "点推定と区間の違い、不確実性伝播、低信頼時の棄権を整理します。"
  - label: "Wiki: マルチモーダル統合の基本"
    url: "/wiki/multimodal-integration-basics.html"
    description: "EEG、MEG、fMRI、ECoG、MRI の役割差を初歩から整理します。"
  - label: "Wiki: ベースライン・事前登録・モデルカード"
    url: "/wiki/baselines-prereg-and-model-cards.html"
    description: "研究運用の言葉の役割差を、初歩から整理します。"
  - label: "Wiki: 熱力学的接地の基本"
    url: "/wiki/thermodynamic-grounding-basics.html"
    description: "Landauer、散逸、NESS、EPR の入口を初歩から整理します。"
recommended_pages:
  - label: "WBE入門"
    url: "/wbe_101.html"
  - label: "EEG入門"
    url: "/eeg_101.html"
  - label: "FAQ"
    url: "/faq.html"
---
<!-- IMPORTANT: Do not delete or overwrite this information. It serves as the project's permanent knowledge base. -->

<main class="main-container">
<article class="content-column">

<div class="abstract-box">
<h2>How To Use</h2>
<p>
この用語集は、用語の意味をすぐ確認するためのリファレンスです。まず日常語の説明で把握し、必要なときだけ厳密な定義に進む構成とし、議論を測定と扱い方に結び付けます。WBEの議論は言葉のズレで混乱しやすいため、ここでは<strong>実際にどう測って扱うか</strong>を重視します。
</p>
</div>

<div class="note-box">
<strong>このページの見方</strong>
<p>
一語一句を暗記する必要はありません。本文で止まった単語をここで確認し、「ざっくり意味が分かったら元のページに戻る」という使い方で十分です。
</p>
</div>
<div class="note-box">
<strong>どの本文へ戻るか迷ったとき</strong>
<p>
用語だけ分かっても、次に Verification、Roadmap、WBE 101、EEG 101 のどこへ戻るかで迷うことがあります。公開ページどうしの役割差を先に整理したい場合は <a href="wiki/public-page-reading-guide.html">Wiki: 公開ページの読み分けガイド</a> をご覧ください。
</p>
</div>
<div class="note-box">
<strong>理論系か実務系かで戻り先を絞りたいとき</strong>
<p>
WBE 101、Perspective、Perspective内の理論フレーム節、Roadmap のような理論系ページへ戻りたい場合は <a href="wiki/theory-pages-reading-guide.html">Wiki: 理論系ページの読み分けガイド</a>、Verification、Datasets、Datasets内のL0実践節のような実務系ページへ戻りたい場合は <a href="wiki/practical-pages-reading-guide.html">Wiki: 実務系ページの読み分けガイド</a> をご覧ください。
</p>
</div>

<section class="section" id="where-to-look">
<h2 class="section-title">迷った言葉の種類ごとの引き方</h2>
<table class="data-table">
<thead>
<tr>
<th>こういう言葉で止まったら</th>
<th>まず見る節</th>
<th>ここで分かること</th>
</tr>
</thead>
<tbody>
<tr>
<td>Mind-Upload、WBE、クレーム階段のような「このサイトの土台の言葉」</td>
<td><a href="#core">コア概念</a></td>
<td>このサイトが何を目標にし、どの強さの主張を区別しているかが分かります。</td>
</tr>
<tr>
<td>decode、emulate、counterfactual のような「できることの違い」を示す言葉</td>
<td><a href="#decode-emulate">Decode と Emulate</a></td>
<td>観測の翻訳と、内部の仕組みを動かすことが別だと分かります。</td>
</tr>
<tr>
<td>IIT、GNWT、FEP、PCI のような「意識理論や意識指標」の言葉</td>
<td><a href="#consciousness-theories">意識理論</a></td>
<td>どの理論や指標が、何を説明しようとしているかを短くつかめます。</td>
</tr>
<tr>
<td>EEG、MEG、fMRI、ECoG、QC のような「計測方法」の言葉</td>
<td><a href="#measurement">計測</a></td>
<td>何を測る手法か、どこが得意でどこが弱いかを確認できます。</td>
</tr>
<tr>
<td>逆問題、ESI、因果、同定可能性のような「推定やモデル化」の言葉</td>
<td><a href="#modeling">モデル化</a></td>
<td>観測から中身を推定するときに、なぜ一意に決まらないことがあるのかを追えます。</td>
</tr>
<tr>
<td>BIDS、ベンチマーク、再現性、事前登録のような「研究運用」の言葉</td>
<td><a href="#open-science">標準化・再現性</a></td>
<td>比較可能な前進を作るために、なぜ運用ルールが必要かが分かります。</td>
</tr>
<tr>
<td>confidence、calibration、coverage、abstention、recalibration burden のような「運用上限」を決める言葉</td>
<td><a href="#uncertainty-deployment">不確実性と運用</a></td>
<td>高い score がそのまま安全な deployability を意味しない理由が分かります。</td>
</tr>
</tbody>
</table>
</section>

<div class="note-box">
<strong>読み方のコツ</strong>
<p>
似た言葉が並んだときは、まず「何を観測している言葉か」「その言葉だけで強い主張をしていないか」「条件を変えたときの反応まで含むか」を見ると混同しにくくなります。特に、相関の説明をそのまま因果や本人性の説明へ広げないことが重要です。
</p>
</div>

<div class="note-box">
<strong>理論名が並んで苦しくなったとき</strong>
<p>
IIT、GNWT、FEP、PCI の違いは、短い定義だけでは頭に入りにくいことがあります。その場合は <a href="wiki/consciousness-theory-map.html">Wiki: 意識理論マップ</a> を先に見て、何を説明したい理論なのかを表で掴んでから戻ると読みやすくなります。
</p>
</div>

<div class="note-box">
<strong>計測語とモデル語が混ざって苦しくなったとき</strong>
<p>
EEG、QC、BIDS、逆問題、ESI、DCM、SCM は、全部同じ種類の言葉ではありません。観測、整理、推定、検証のどの段階で使う語かを流れで見たい場合は <a href="wiki/measurement-and-modeling-terms.html">Wiki: 計測からモデル化までの用語ガイド</a> を先に見ると戻りやすくなります。
</p>
</div>

<div class="note-box">
<strong>逆問題や因果モデルで止まったとき</strong>
<p>
「頭皮で見えた信号」と「脳内で本当に起きていたこと」と「因果が分かったこと」は別です。この差を順問題、逆問題、ESI、DCM、SCM の順に整理したい場合は <a href="wiki/observation-to-estimation.html">Wiki: 観測から推定へ</a> を先にご覧ください。
</p>
</div>

<div class="note-box">
<strong>数字の幅や低信頼時の扱いで止まったとき</strong>
<p>
信用区間、信頼区間、不確実性の伝播、棄権は、全部「1つの数字だけで断言しない」ための仕組みです。ここを初歩から整理したい場合は <a href="wiki/uncertainty-confidence-and-abstention.html">Wiki: 不確実性・校正・棄権</a> を先にご覧ください。
</p>
</div>

<div class="note-box">
<strong>計測装置の役割差で止まったとき</strong>
<p>
EEG、MEG、fMRI、ECoG、MRI は全部「脳を測るもの」ですが、得意不得意が違います。どれを何のために組み合わせるのかを初歩から整理したい場合は <a href="wiki/multimodal-integration-basics.html">Wiki: マルチモーダル統合の基本</a> を先にご覧ください。
</p>
</div>

<div class="note-box">
<strong>研究運用の言葉で止まったとき</strong>
<p>
ベースライン、ベンチマーク、事前登録、モデルカード、失敗例は、全部「再現性に大事なもの」ですが役割が違います。その差を初歩から整理したい場合は <a href="wiki/baselines-prereg-and-model-cards.html">Wiki: ベースライン・事前登録・モデルカード</a> を先にご覧ください。
</p>
</div>

<div class="note-box">
<strong>2026-03 用語監査の要点</strong>
<p>
今回の更新では、最近の公開ページで強化した境界を、この用語集にも下ろしました。特に <strong>detectability / localization / identifiability / direct validation / deployability</strong> を 1 つの「性能」にまとめないこと、そして <strong>confidence / calibration / abstention / recalibration burden</strong> を別指標として読むことを、用語レベルでも固定いたします。
</p>
</div>

<section class="section" id="core">
<h2 class="section-title">コア概念</h2>
<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>Mind-Uploadでの意味（ざっくり）</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>マインドアップロード</strong></td>
<td>「意識や記憶をデジタルに移す」一般呼称。Mind-Uploadでは主張レベルをクレーム階段で分けて扱う。</td>
</tr>
<tr>
<td><strong>WBE（Whole Brain Emulation）</strong></td>
<td>脳の機能を別基盤で再現すること。何を再現したら“成功”かは定義依存なので、先に評価を固定する。</td>
</tr>
<tr>
<td><strong>クレーム階段（L0〜L5）</strong></td>
<td>成果の言い方を揃える枠組み。L1（デコーディング）をL4（本人性）と混同しないためのガードレール。</td>
</tr>
<tr>
<td><strong>検証基盤（Verification Commons）</strong></td>
<td>標準・データ・評価・登録・監査をまとめて提供し、「比較可能な前進」を積み上げる公共財。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="decode-emulate">
<h2 class="section-title">Decode と Emulate</h2>
<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>違い</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>デコーディング（Decoding）</strong></td>
<td>観測された信号から、状態・刺激・文章などを予測する（相関ベースになりやすい）。</td>
</tr>
<tr>
<td><strong>エミュレーション（Emulation）</strong></td>
<td>内部状態が時間発展し、介入に反応し、将来の出力を生成する（因果・生成の要求が強い）。</td>
</tr>
<tr>
<td><strong>反事実（Counterfactual）</strong></td>
<td>「もし条件Xを変えたら？」という分岐に対する予測。decode→emulateのギャップを埋める検証の中心。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="easy-confusions">
<h2 class="section-title">よく混同する言葉</h2>
<table class="data-table">
<thead>
<tr>
<th>混同しやすい組</th>
<th>違いを一言で言うと</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>マインドアップロード / WBE</strong></td>
<td>マインドアップロードは広い一般呼称、WBE は脳機能を別基盤で再現する技術寄りの言い方です。</td>
</tr>
<tr>
<td><strong>デコーディング / エミュレーション</strong></td>
<td>デコーディングは「観測の翻訳」、エミュレーションは「中の仕組みごと動かすこと」です。</td>
</tr>
<tr>
<td><strong>相関 / 因果</strong></td>
<td>相関は一緒に変わる関係、因果は片方を変えるともう片方も変わる関係です。</td>
</tr>
<tr>
<td><strong>観測可能性 / 同定可能性</strong></td>
<td>観測可能性は「見分けられるか」、同定可能性は「一意に決まるか」です。前者があっても後者は成立しません。</td>
</tr>
<tr>
<td><strong>検出可能性 / 局在化</strong></td>
<td>検出可能性は「何かが見えている」こと、局在化は「どこから来たかを絞る」ことです。前者だけで source claim にはなりません。</td>
</tr>
<tr>
<td><strong>局在化 / 同定可能性</strong></td>
<td>局在化は候補領域を推定すること、同定可能性は代替モデル族を除外して唯一性へ近づくことです。</td>
</tr>
<tr>
<td><strong>同定可能性 / 直接妥当化</strong></td>
<td>同定可能性は理論上どこまで絞れるか、直接妥当化は SEEG や intracranial stimulation などの外部 ground truth と照合したかです。</td>
</tr>
<tr>
<td><strong>モデル適合 / 直接妥当化</strong></td>
<td>モデル適合は観測データに合うこと、直接妥当化は外部の ground truth と照合することです。後者のほうが強い証拠です。</td>
</tr>
<tr>
<td><strong>脳信号 / language prior</strong></td>
<td>脳信号は計測由来の情報、language prior は語彙・文脈・LLM が補う統計的手掛かりです。出力の流暢さだけでは寄与を分けられません。</td>
</tr>
<tr>
<td><strong>confidence / calibration</strong></td>
<td>confidence はモデルの自己評価、calibration はその自己評価が経験的頻度と合っているかです。</td>
</tr>
<tr>
<td><strong>calibration / deployability</strong></td>
<td>校正が良いことは必要条件ですが、deployability には abstention、tail latency、drift、recalibration burden も要ります。</td>
</tr>
<tr>
<td><strong>lagged connectivity / leakage control</strong></td>
<td>wPLI や imaginary coherence は leakage を減らす候補ですが、reference 依存性や ghost interaction を自動では消しません。</td>
</tr>
<tr>
<td><strong>ベンチマーク / リーダーボード</strong></td>
<td>ベンチマークは比べるための課題と指標、リーダーボードはその結果を並べる運用画面です。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="consciousness-theories">
<h2 class="section-title">意識理論（Theories of Consciousness）</h2>
<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>Mind-Uploadでの意味</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>IIT（統合情報理論）</strong></td>
<td>意識を「統合された情報量（Φ）」で測る理論。IIT 4.0（Albantakis et al., 2023）では公理系を刷新し、Φ構造（cause-effect structure）で意識を特定する。WBEでは因果構造の保存要件に直結する。</td>
</tr>
<tr>
<td><strong>GNWT（グローバル神経ワークスペース理論）</strong></td>
<td>情報が前頭-頭頂ネットワークで「イグニッション」し広域共有されることで意識が成立するとする理論。IITとの実験的対立はCogitate Consortium（2025）で検証された。</td>
</tr>
<tr>
<td><strong>FEP（自由エネルギー原理）</strong></td>
<td>生物が環境との境界を維持するために、感覚入力の「驚き」を最小化するという包括的枠組み（Friston, 2010）。WBEでは実装原理として採用。</td>
</tr>
<tr>
<td><strong>能動的推論（Active Inference）</strong></td>
<td>FEPの行動側面。環境を能動的に変えて予測誤差を最小化する。エミュレータの自律性の基盤。</td>
</tr>
<tr>
<td><strong>PCI / PCI-ST（摂動複雑性指標）</strong></td>
<td>TMS刺激に対するEEG応答の複雑性で意識レベルを定量する。理論に依存しない経験的指標としてWBEの検証基盤に位置づける（Casali et al., 2013）。</td>
</tr>
<tr>
<td><strong>マルコフブランケット（Markov Blanket）</strong></td>
<td>システムと環境の統計的境界。FEPにおける「自己」の定義に使われるが、意識の境界への適用には批判もある（Bruineberg et al., 2022）。</td>
</tr>
<tr>
<td><strong>Unfolding Argument</strong></td>
<td>任意のリカレントネットワークは機能的に等価なフィードフォワード網で置換でき、IITではΦ=0となるという批判（Doerig et al., 2019）。WBEでは因果構造保存の必要性を支持する論拠。</td>
</tr>
<tr>
<td><strong>HOT（高次理論）</strong></td>
<td>意識は一次表象に対する高次の表象（「自分が知覚していることを知っている」）によって成立するとする理論群。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="measurement">
<h2 class="section-title">計測（Measurement）</h2>
<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>メモ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG</strong></td>
<td>頭皮上の電位差を高時間分解能で測る。空間分解能は弱いので不確実性の扱いが重要。</td>
</tr>
<tr>
<td><strong>MEG</strong></td>
<td>磁場を測る。EEGとは異なる感度分布で補完関係があるが、装置は高価。</td>
</tr>
<tr>
<td><strong>fMRI</strong></td>
<td>血流（BOLD）を測る。空間分解能は良いが時間分解能は遅い。</td>
</tr>
<tr>
<td><strong>ECoG / 侵襲計測</strong></td>
<td>因果介入や高SNRの可能性がある一方、倫理・適用範囲の制約が大きい。</td>
</tr>
<tr>
<td><strong>QC（Quality Control）</strong></td>
<td>インピーダンス、ノイズ、欠損、アーティファクトなどを定量化し、ログとして残すこと。</td>
</tr>
<tr>
<td><strong>Observability Budget</strong></td>
<td>選んだ計測スタックで、何が直接見えていて何が latent のまま残るかを先に固定する考え方です。</td>
</tr>
<tr>
<td><strong>Claim Ceiling</strong></td>
<td>その計測で無理なく言える主張の上限です。観測量が増えても、state-complete と自動では読みません。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="implementation">
<h2 class="section-title">実装基盤（Implementation）</h2>
<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>Mind-Uploadでの意味</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>ニューロモルフィック・ハードウェア</strong></td>
<td>生物学的ニューロンの動態を電子回路で模倣する専用チップ（Intel Loihi 2, SpiNNaker 2等）。IITの因果構造要件への対応候補。</td>
</tr>
<tr>
<td><strong>Slow Continuous Mind Uploading</strong></td>
<td>一括コピーではなく、生体脳とデジタル基盤を段階的に統合する移行戦略（Clowes, 2021）。本人性保存の工学的アプローチ。</td>
</tr>
<tr>
<td><strong>コネクトーム（Connectome）</strong></td>
<td>脳内の神経結合の完全地図。ショウジョウバエ全脳コネクトーム（FlyWire, Dorkenwald et al., 2024）が完成し、マウス脳が次の目標。</td>
</tr>
<tr>
<td><strong>NMM（Neural Mass Model）</strong></td>
<td>大規模ニューロン群の平均活動を記述するモデル。DCMの基盤となり、E/Iバランスの推定に使用。</td>
</tr>
<tr>
<td><strong>E/Iバランス（興奮/抑制バランス）</strong></td>
<td>神経回路の興奮性と抑制性の動的均衡。意識の質やレベルの変化に関与する。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="modeling">
<h2 class="section-title">モデル化（Modeling）</h2>
<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>Mind-Uploadでの使いどころ</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>逆問題（Inverse Problem）</strong></td>
<td>観測（頭皮EEG）から原因（脳内活動）を推定する問題。一般に解が一意に定まらない。</td>
</tr>
<tr>
<td><strong>観測可能性（Observability）</strong></td>
<td>選んだ観測だけで latent state の違いを区別できるか。見えていることと、一意に分かることは別です。</td>
</tr>
<tr>
<td><strong>検出可能性（Detectability）</strong></td>
<td>source や条件差の存在を「ある程度見つけられるか」です。deep activity が detectable でも state-complete reconstruction とは別です。</td>
</tr>
<tr>
<td><strong>局在化（Localization）</strong></td>
<td>推定 source を空間的にどこへ置くかです。fit が良いだけでは強い source claim にはなりません。</td>
</tr>
<tr>
<td><strong>同定可能性（Identifiability）</strong></td>
<td>異なる内部モデルや状態が、同じ観測を説明してしまわないか。予測精度が高くても唯一解とは限りません。</td>
</tr>
<tr>
<td><strong>ESI（EEG Source Imaging）</strong></td>
<td>逆問題を解いて、脳内ソースを推定する。推定値だけでなく“不確実性”も一緒に扱うのが重要。</td>
</tr>
<tr>
<td><strong>Ghost Interaction</strong></td>
<td>source reconstruction 後にも残りうる見かけの結合です。connectivity を localization の延長と読まないための警告語です。</td>
</tr>
<tr>
<td><strong>直接妥当化（Direct Validation）</strong></td>
<td>推定 source やモデル出力を、intracranial stimulation / SEEG / 外部 ground truth と照合すること。fit が良いだけでは代用できません。</td>
</tr>
<tr>
<td><strong>Family Comparison</strong></td>
<td>DCM などで候補モデル族を比較し、どの構造仮説が data に相対的に強いかを見る手続きです。単一モデルだけで断言しません。</td>
</tr>
<tr>
<td><strong>Parameter Degeneracy</strong></td>
<td>異なる内部パラメータ群が、ほぼ同じ出力を作れてしまうことです。出力一致だけで唯一の機序だと言えない理由になります。</td>
</tr>
<tr>
<td><strong>Language Prior</strong></td>
<td>decoder が語彙・文脈・LLM から借りる統計的先験情報。文章を滑らかにできる一方、brain-derived information の寄与を見えにくくします。</td>
</tr>
<tr>
<td><strong>Neural Contribution Card</strong></td>
<td>brain-to-text / speech decode で、task constraint、LM / prompt / candidate set、<code>no-brain</code> / <code>LM-only</code> / shuffle baseline、subject cooperation、online / offline、claim ceiling を固定し、流暢な出力をそのまま neural reconstruction と読まないための提出物です。</td>
</tr>
<tr>
<td><strong>DCM</strong></td>
<td>神経回路モデルを仮定し、結合を推定する枠組みの一種。介入設計と相性が良い。</td>
</tr>
<tr>
<td><strong>SCM（構造的因果モデル）</strong></td>
<td>因果関係を明示するモデル。反事実や介入予測を定義しやすい。</td>
</tr>
</tbody>
</table>
</section>

<div class="note-box">
<strong>2026-03 の補足</strong>
<p>
non-invasive decoding や ESI は着実に前進していますが、成功した decoder や source estimate がそのまま内部状態の一意復元を意味するわけではありません。Seeber et al. (2019)、Mikulan et al. (2020)、Unnwongse et al. (2023)、Hao et al. (2025) を読むときは、<strong>detectability</strong>、<strong>localization</strong>、<strong>identifiability</strong>、<strong>direct validation</strong> を分けて見てください。さらに connectivity claim では Haufe et al. (2013) と Palva et al. (2018) が示した source mixing / ghost interaction を別監査に残します。
</p>
</div>

<section class="section" id="uncertainty-deployment">
<h2 class="section-title">不確実性と運用（Uncertainty & Deployment）</h2>
<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>意味</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>校正（Calibration）</strong></td>
<td>たとえば confidence 80% の予測が、長期的に本当に約 80% 当たる状態です。score の大きさと正しさをそろえます。</td>
</tr>
<tr>
<td><strong>Coverage</strong></td>
<td>モデルが判定を返した割合です。棄権を増やすと risk は下げられますが、coverage は下がります。</td>
</tr>
<tr>
<td><strong>棄権（Abstention / Reject Option）</strong></td>
<td>低信頼・外挿・外れ値のときに「分からない」と返す運用です。過大主張を防ぐための技術的な安全弁です。</td>
</tr>
<tr>
<td><strong>Tail Latency</strong></td>
<td>P95 / P99 のような遅い側の応答時間です。closed loop では平均遅延だけでは安全性を読み切れません。</td>
</tr>
<tr>
<td><strong>Recalibration Burden</strong></td>
<td>decoder や BCI を使い続けるために、どれだけ再較正が必要かです。長期運用可能性の主要指標です。</td>
</tr>
</tbody>
</table>
<div class="note-box">
<strong>運用で起きやすい誤読</strong>
<p>
高い accuracy や confidence は、すぐには deployability を意味しません。Segal et al. (2023) は false alarm rate を制御する calibration の必要性を示し、Wilson et al. (2025) は長期 iBCI で <strong>recalibration burden</strong> が臨床運用の主要障壁であることを示しました。したがって本サイトでは、<strong>confidence</strong>、<strong>calibration</strong>、<strong>abstention</strong>、<strong>tail latency</strong>、<strong>recalibration burden</strong> を別々に記録します。
</p>
</div>
</section>

<section class="section" id="open-science">
<h2 class="section-title">標準化・再現性（Open Science）</h2>
<table class="data-table">
<thead>
<tr>
<th>用語</th>
<th>意味</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>BIDS / EEG-BIDS</strong></td>
<td>神経計測データの整理規約。共有と再現の“最初の壁”を下げる。</td>
</tr>
<tr>
<td><strong>ベンチマーク</strong></td>
<td>タスク・データ・指標を固定して比較可能にする仕組み。</td>
</tr>
<tr>
<td><strong>ベースライン</strong></td>
<td>比較の出発点。改善を主張するならベースラインとの差分が必要。</td>
</tr>
<tr>
<td><strong>事前登録（Preregistration）</strong></td>
<td>“やる前”に計画を固定し、探索と検証を区別する。報告バイアスを減らす。</td>
</tr>
<tr>
<td><strong>モデルカード</strong></td>
<td>スコアだけでなく、学習データ、計算資源、既知の弱点、失敗例を公開するフォーマット。</td>
</tr>
</tbody>
</table>
</section>

<section class="section" id="references">
<h2 class="section-title">参考文献（用語定義）</h2>
<ol>
<li>Michel, C. M., &amp; Brunet, D. (2019). EEG source imaging review. <a href="https://doi.org/10.3389/fneur.2019.00325" target="_blank">doi:10.3389/fneur.2019.00325</a></li>
<li>Wipf, D., &amp; Nagarajan, S. (2009). Unified Bayesian framework for MEG/EEG source imaging. <a href="https://doi.org/10.1016/j.neuroimage.2008.02.059" target="_blank">doi:10.1016/j.neuroimage.2008.02.059</a></li>
<li>Seeber, M., Cantonas, L.-M., Hoevels, M., et al. (2019). Subcortical electrophysiological activity is detectable with high-density EEG source imaging. <a href="https://doi.org/10.1038/s41467-019-08725-w" target="_blank">doi:10.1038/s41467-019-08725-w</a></li>
<li>Mikulan, E., Russo, S., Parmigiani, S., et al. (2020). Simultaneous human intracerebral stimulation and HD-EEG, ground-truth for source localization methods. <a href="https://doi.org/10.1038/s41597-020-0467-x" target="_blank">doi:10.1038/s41597-020-0467-x</a></li>
<li>Unnwongse, K., Achakulvisut, T., Wu, J. Y., et al. (2023). Validating EEG source imaging using intracranial electrical stimulation in focal epilepsy. <a href="https://doi.org/10.1093/braincomms/fcad023" target="_blank">doi:10.1093/braincomms/fcad023</a></li>
<li>Hao, S., Zhao, H., Feng, Z., et al. (2025). HD-EEG source imaging with simultaneous SEEG recording in drug-resistant epilepsy. <a href="https://doi.org/10.1111/epi.18552" target="_blank">doi:10.1111/epi.18552</a></li>
<li>Aydin, U., Vorwerk, J., Küpper, P., et al. (2019). Influence of head tissue conductivity uncertainties on EEG dipole reconstruction. <a href="https://doi.org/10.3389/fnins.2019.00531" target="_blank">doi:10.3389/fnins.2019.00531</a></li>
<li>Haufe, S., Nikulin, V. V., Müller, K.-R., &amp; Nolte, G. (2013). A critical assessment of connectivity measures for EEG data: a simulation study. <a href="https://doi.org/10.1016/j.neuroimage.2012.09.036" target="_blank">doi:10.1016/j.neuroimage.2012.09.036</a></li>
<li>Palva, J. M., Wang, S. H., Palva, S., et al. (2018). Ghost interactions in MEG/EEG source space: A note of caution on inter-areal coupling measures. <a href="https://doi.org/10.1016/j.neuroimage.2018.02.032" target="_blank">doi:10.1016/j.neuroimage.2018.02.032</a></li>
<li>Penny, W. D., Stephan, K. E., Mechelli, A., &amp; Friston, K. J. (2004). Comparing dynamic causal models. <a href="https://doi.org/10.1016/j.neuroimage.2004.03.026" target="_blank">doi:10.1016/j.neuroimage.2004.03.026</a></li>
<li>Hauser, A., &amp; Bühlmann, P. (2012). Characterization and Greedy Learning of Interventional Markov Equivalence Classes of Directed Acyclic Graphs. <a href="https://jmlr.csail.mit.edu/papers/v13/hauser12a.html" target="_blank">JMLR 13:2409-2464</a></li>
<li>Vink, J. J. T., Klooster, D. C. W., Ozdemir, R. A., et al. (2020). EEG Functional Connectivity is a Weak Predictor of Causal Brain Interactions. <a href="https://doi.org/10.1007/s10548-020-00757-6" target="_blank">doi:10.1007/s10548-020-00757-6</a></li>
<li>Tang, J., LeBel, A., Jain, S., &amp; Huth, A. G. (2023). Semantic reconstruction of continuous language from non-invasive brain recordings. <a href="https://doi.org/10.1038/s41593-023-01304-9" target="_blank">doi:10.1038/s41593-023-01304-9</a></li>
<li>d'Ascoli, S., Bel, C., Rapin, J., et al. (2025). Towards decoding individual words from non-invasive brain recordings. <a href="https://doi.org/10.1038/s41467-025-65499-0" target="_blank">doi:10.1038/s41467-025-65499-0</a></li>
<li>Friston, K. J., Harrison, L., &amp; Penny, W. (2003). Dynamic causal modelling. <a href="https://doi.org/10.1016/S1053-8119(03)00202-7" target="_blank">doi:10.1016/S1053-8119(03)00202-7</a></li>
<li>Vinck, M., et al. (2011). Weighted Phase Lag Index (wPLI). <a href="https://doi.org/10.1016/j.neuroimage.2011.01.055" target="_blank">doi:10.1016/j.neuroimage.2011.01.055</a></li>
<li>Staniek, M., &amp; Lehnertz, K. (2008). Symbolic Transfer Entropy. <a href="https://doi.org/10.1103/PhysRevLett.100.158101" target="_blank">doi:10.1103/PhysRevLett.100.158101</a></li>
<li>Gorgolewski, K. J., et al. (2016). BIDS. <a href="https://doi.org/10.1038/sdata.2016.44" target="_blank">doi:10.1038/sdata.2016.44</a></li>
<li>Pernet, C. R., et al. (2019). EEG-BIDS. <a href="https://doi.org/10.1038/s41597-019-0104-8" target="_blank">doi:10.1038/s41597-019-0104-8</a></li>
<li>Pernet, C. R., et al. (2020). Best practices in data analysis and sharing in neuroimaging using MEEG. <a href="https://doi.org/10.1038/s41593-020-00709-0" target="_blank">doi:10.1038/s41593-020-00709-0</a></li>
<li>Guo, C., Pleiss, G., Sun, Y., &amp; Weinberger, K. Q. (2017). On Calibration of Modern Neural Networks. <a href="https://proceedings.mlr.press/v70/guo17a.html" target="_blank">PMLR 70:1321-1330</a></li>
<li>Geifman, Y., &amp; El-Yaniv, R. (2017). Selective Classification for Deep Neural Networks. <a href="https://papers.neurips.cc/paper/7073-selective-classification-for-deep-neural-networks" target="_blank">NeurIPS 2017</a></li>
<li>Segal, G., Keidar, N., Lotan, R. M., et al. (2023). Utilizing risk-controlling prediction calibration to reduce false alarm rates in epileptic seizure prediction. <a href="https://doi.org/10.3389/fnins.2023.1184990" target="_blank">doi:10.3389/fnins.2023.1184990</a></li>
<li>Wilson, G. H., Stein, E. A., Kamdar, F., et al. (2025). Long-term unsupervised recalibration of cursor-based intracortical brain-computer interfaces using a hidden Markov model. <a href="https://doi.org/10.1038/s41551-025-01536-z" target="_blank">doi:10.1038/s41551-025-01536-z</a></li>
<li>Prinz, A. A., Bucher, D., &amp; Marder, E. (2004). Similar network activity from disparate circuit parameters. <a href="https://doi.org/10.1038/nn1352" target="_blank">doi:10.1038/nn1352</a></li>
<li>Albantakis, L., et al. (2023). Integrated Information Theory (IIT) 4.0. <a href="https://doi.org/10.1371/journal.pcbi.1011465" target="_blank">doi:10.1371/journal.pcbi.1011465</a></li>
<li>Friston, K. (2010). The free-energy principle. <a href="https://doi.org/10.1038/nrn2787" target="_blank">doi:10.1038/nrn2787</a></li>
<li>Casali, A. G., et al. (2013). PCI. <a href="https://doi.org/10.1126/scitranslmed.3006294" target="_blank">doi:10.1126/scitranslmed.3006294</a></li>
<li>Doerig, A., et al. (2019). Unfolding Argument. <a href="https://doi.org/10.1016/j.concog.2019.04.002" target="_blank">doi:10.1016/j.concog.2019.04.002</a></li>
<li>Tononi, G., et al. (2016). IIT: from the phenomenology to the mechanisms of consciousness. <a href="https://doi.org/10.1038/nrn.2016.44" target="_blank">doi:10.1038/nrn.2016.44</a></li>
</ol>
</section>

</article>

<aside class="sidebar-column">

<div class="sidebar-box">
<h4>Related</h4>
<ul>
<li><a href="wbe_101.html">WBE入門 →</a></li>
<li><a href="eeg_101.html">EEG入門 →</a></li>
<li><a href="verification.html">検証基盤 →</a></li>
<li><a href="tech_roadmap.html#definition">前進の定義 →</a></li>
</ul>
</div>

<div class="note-box">
<strong>Note</strong>
<p>
この用語集は「統一のための暫定」です。曖昧な語は、Roadmap側で“測れる定義”に固定していきます。
</p>
</div>

</aside>
</main>
