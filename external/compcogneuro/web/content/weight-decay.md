---
layout: default
title: "compcogneuro/web: weight-decay"
description: "compcogneuro/web: weight-decay.md の日本語訳"
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
<p>原典: <a href="https://github.com/compcogneuro/web/blob/main/content/weight-decay.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/web/blob/main/content/weight-decay.md</a></p>
<p>ライセンス: Text: CC BY 4.0; code: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
+++
Categories = ["Learning", "Computation"]
bibfile = "ccnlab.json"
+++
多くの [[abstract neural network]] モデルでは、**重み減衰** が [[error backpropagation learning]] に事前に制約やバイアスを課す正則化要因としてよく使用されます。 [[bias-variance tradeoff]] のコンテキストでは、重み減衰バイアスはさまざまな学習結果間の分散を低減し、問題を解決するのに十分な重み値を維持しながら、一般に重み値が可能な限り小さいソリューションを優先します。

重み減衰は統計回帰でも長い間使用されてきました。これは数学的には線形活性化関数を備えた 2 層ニューラル ネットワークと同等です。具体的には、[なげなわ](https://en.wikipedia.org/wiki/Lasso_(statistics)) 回帰では L1 ノルム (重みの絶対値) に基づく重み減衰が使用され、[リッジ](https://en.wikipedia.org/wiki/Ridge_regression) 回帰では L2 ノルム (重みの 2 乗値) に基づく重み減衰が使用されます (wikipedia リンク)。

[[Leabra]] モデルでは、[[Hebbian learning]] は重み減衰と同様に正則化バイアスとして使用されます。


</section>

</article>
</main>
