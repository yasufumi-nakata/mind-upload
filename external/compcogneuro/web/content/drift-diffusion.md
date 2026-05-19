---
layout: default
title: "compcogneuro/web: drift-diffusion"
description: "compcogneuro/web: drift-diffusion.md の日本語訳"
article_type: 翻訳資料
last_updated: '2026-05-20'
audience: 外部資料を日本語で原文順に読みたい読者
reading_time: 原文量に依存
page_intro: "このページは外部資料の日本語訳です。原文の見出し順と本文順を保ち、コード・URL・出典表記はできるだけ原形のまま残しています。"
accuracy_note: "機械翻訳をベースにした日本語訳です。実装手順や引用は必ず原典も確認してください。"
---

<main class="main-container">
<article class="content-column">

<div class="note-box">
<strong>出典とライセンス</strong>
<p>原典: <a href="https://github.com/compcogneuro/web/blob/main/content/drift-diffusion.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/web/blob/main/content/drift-diffusion.md</a></p>
<p>ライセンス: Text: CC BY 4.0; code: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
+++
Categories = ["Computation", "Cognition"]
bibfile = "ccnlab.json"
+++
**ドリフト拡散** モデル (DDM) は、2 択強制選択 (2AFC) 決定の抽象的で数学的に単純なモデルであり、一定の時間内で最も正確な結果が得られるという意味で、時間の経過に伴う情報の最適な統合を提供します。逆に、所定の精度では、時間内で最も短い量の結果が得られます ([[@BogaczBrownMoehlisEtAl06]])。これは、連続確率比テスト (SPRT) の連続バージョンであり、同様に離散プロセスに最適であることが証明されています ([[@Wald47]]; [[@WaldWolfowitz48]])。

DDM モデルは、広範囲の 2AFC タスク ([[@Laming68]]; [[@Ratcliff78]]; [[@Stone60]]; [[@RatcliffRouder98]]) にわたる人間の反応時間分布 (RT) の正確な測定を提供し、DDM における中心蓄積プロセスの神経相関がさまざまな脳領域で特定されています ([[@ShadlenNewsome01]]; [[@ShadlenNewsome01]]; [[@GoldShadlen02]]; [[@DingGold13]])、[[basal ganglia]] ([[@YartsevHanksYoonEtAl18]]; [[@DunovanLynchMolesworthEtAl15]]; [[@DoiFanGoldEtAl20]]) を含みます。

{id="figure_ddm" style="高さ:20em"}
![ドリフト拡散モデルには、2 つの力によって駆動される蓄積プロセスが含まれます。1 つは、基礎となる信号の強度 (刺激をどれだけ明確に知覚するかなど) を反映する系統的なドリフトで、もう 1 つはノイズ (拡散) プロセスです。上限と下限の 2 つの境界があり、累積値が境界を越えるたびに、決定がカウントされます。境界通過時間の分布は、幅広い研究にわたって人間と動物の反応時間によく適合します。](media/fig_drift_diffusion_wiecki_etal_13.png)

[[#figure_ddm]] は、DDM の主要な要素を示します。通常、ドリフト レートは正であり、上限は正しい応答を表し、下限はエラーを表します。 DDM モデルの重要な長所の 1 つは、エラー反応時間の分布を適切に説明できることです。

DDM モデルは、関連する情報が本質的に弱い、および/または確率的であるタスクに適用されることがよくあります。たとえば、ドットがほぼランダムな方向に移動するものの、特定のターゲット方向に移動する潜在的な確率が存在するディスプレイなどです。これは、DDM での時間的に拡張された蓄積プロセスに適切に適合します。この蓄積プロセスは、ノイズの多い離散スパイク ニューロン上のあらゆるニューラル統合プロセスにもよく適合し、信号を統合する時間が長ければ長いほど、より高い精度が得られます。

[[BG ventral simulation]] は、[[basal ganglia]] 内のアキュムレータのようなプロセスが、DDM モデルの分布と同様の RT 分布をどのように示すことができるかを示しており、これは、これが DDM のようなインテグレータ プロセス ([[@YartsevHanksYoonEtAl18]]) の神経軌跡であるという証拠と一致しています。この統合プロセスの基礎となるメカニズムは、特に DDM に似ているわけではありませんが、おそらく [[@^BogaczMoraudAbdiEtAl16]] の分析により、それがどのように関係しているのかについての適切な洞察が得られる可能性があります。
</section>

</article>
</main>
