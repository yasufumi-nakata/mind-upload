---
layout: default
title: "compcogneuro/web: error-driven-learning"
description: "compcogneuro/web: error-driven-learning.md の日本語訳"
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
<p>原典: <a href="https://github.com/compcogneuro/web/blob/main/content/error-driven-learning.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/web/blob/main/content/error-driven-learning.md</a></p>
<p>ライセンス: Text: CC BY 4.0; code: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
+++
Name = "Error-driven learning"
Categories = ["Learning", "Computation"]
bibfile = "ccnlab.json"
+++
**エラー駆動学習** は、シナプスの重みの変更を促進して_エラー_を削減する強力な学習形式です。 [[Axon]] では、これらのエラーは通常、_予測エラー_、つまり予測と実際に起こることの違いです ([[predictive learning]] を参照)。予測エラー駆動学習は、ChatGPT および関連モデルを強化する [[large language models]] (LLM) での学習を推進します。

エラー駆動学習には、これらのエラー信号がシナプス変化を引き起こすメカニズムが必要です。 LLM およびその他の現在の [[abstract neural network]] モデルでは、[[error backpropagation]] はシナプス学習を駆動するために使用されます。ただし、このメカニズムは、既知の神経生物学的メカニズムと直接互換性がありません。したがって、Axon は、[[bidirectional connectivity]] のコンテキストで生物学に基づくメカニズムを使用してローカルに計算できる [[temporal derivative]] を使用して、[[kinase algorithm]] を使用したエラー駆動学習を推進します。

エラー駆動学習は、特定のタスクのパフォーマンス エラーを最小限に抑えるために数学的に導出されるため、非常に一般的で柔軟な形式の学習を提供します。対照的に、既知の [[synaptic plasticity]] メカニズムによってより明確にサポートされている [[Hebbian learning]] は、[[principal components analysis]] と数学的に関連しており、一般に、その入力に存在する強い相関構造をエンコードすることを学習します。経験的に、任意のタスクを解決する方法を学習するわけではないため、[[neocortex]] の汎用学習メカニズムの妥当な基礎とはなりません。

エラー駆動学習におけるトレードオフの分析については、[[combinatorial vs conjunctive]] を参照してください。これは、ヘビアン学習との関係を明確にするのに役立ちます。



</section>

</article>
</main>
