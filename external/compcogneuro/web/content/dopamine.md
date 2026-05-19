---
layout: default
title: "compcogneuro/web: dopamine"
description: "compcogneuro/web: dopamine.md の日本語訳"
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
<p>原典: <a href="https://github.com/compcogneuro/web/blob/main/content/dopamine.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/web/blob/main/content/dopamine.md</a></p>
<p>ライセンス: Text: CC BY 4.0; code: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
+++
Categories = ["Rubicon"]
bibfile = "ccnlab.json"
+++
**ドーパミン**は、脳全体の学習を調節する [[neuromodulator]] です。これは主に、脳幹内の 2 つの隣接する脳領域、**腹側被蓋野 (VTA)** と **黒質緻密部 (SNc)** から分泌されます。計算の観点から見ると、これらのドーパミン ニューロンの活動は、_報酬予測誤差_ (RPE; 予測された報酬と実際に受け取った報酬の差) を計算する TD (_時間差_) [[reinforcement learning]] アルゴリズムの動作とよく一致します。

生物学的な観点から見ると、多くの異なる神経経路が VTA と SNc に集中してドーパミン ニューロンの発火を駆動します。 [[PVLV]] モデルは、これらのさまざまな経路のそれぞれがどのような寄与をしているかを理解するための十分に検証されたフレームワークを提供し、目標主導型で動機付けられた行動のためのより広範な [[Rubicon]] フレームワークの中核要素です。

{id="figure_da-schultz" style="高さ:30em"}
![単純な条件付けタスクにおける腹側被蓋野 (VTA) および黒質緻密部 (SNc) におけるドーパミン作動性ニューロンの神経発火の特徴的なパターン (Schultz et al、1997)。条件付けの前に、報酬が与えられると、ドーパミン ニューロンは活動を爆発させます (上のパネル --- 上のヒストグラムは、以下に示す繰り返し記録トレースにわたるニューラル スパイクの合計を示しています。各行は異なる記録試行です)。動物が条件刺激（CS）（音など）を報酬と関連付けることを学習した後、ドーパミンニューロンは報酬そのものではなく、CSの開始に合わせて発火するようになります。 CS 後に報酬が保留された場合、ドーパミンの発火に低下または一時停止があり、報酬について何らかの予測があったことを示し、報酬が到着しなかった場合には負の予測エラーがあったことを示します。この全体的な条件間での発火パターンは、報酬予測誤差に基づく強化学習モデルと非常に一致しています。 Schultz et al、1997 より転載](media/fig_schultz97_vta_td.png)


</section>

</article>
</main>
