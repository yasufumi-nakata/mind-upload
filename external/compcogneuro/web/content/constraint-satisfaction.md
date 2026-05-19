---
layout: default
title: "compcogneuro/web: constraint-satisfaction"
description: "compcogneuro/web: constraint-satisfaction.md の日本語訳"
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
<p>原典: <a href="https://github.com/compcogneuro/web/blob/main/content/constraint-satisfaction.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/web/blob/main/content/constraint-satisfaction.md</a></p>
<p>ライセンス: Text: CC BY 4.0; code: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
+++
Categories = ["Computation", "Activation"]
bibfile = "ccnlab.json"
+++
**制約充足**は、[[neocortex]] における [[bidirectional connectivity]] の能力を理解するための最も重要な概念の 1 つであり、[[Axon]] アプローチの約束の中心となります。これは、多くの利点を維持しながら野生的な側面を飼いならす方法で広範な双方向接続を組み込んだ数少ないニューラル ネットワーク モデルの 1 つです。

{id="figure_hopfield" style="高さ:30em"}
![Hopfield & Tank (1985) の双方向接続ネットワークは、巡回セールスマン問題 (TSP) を解決します。都市は行 (A ～ J) で表され、パス内の各都市の位置は列で表されます。パネル **(d)** のネットワークの解決策は、都市順序 DHIFGEAJCB です (つまり、都市 D がアクティブな最初の位置を持ち、H が次など)。ネットワーク内のシナプスの重みは、各都市が他の都市にどれだけ近いかをエンコードしており、同じ列と行内に抑制的な接続があるため、各都市は 1 回だけ表され、各位置には 1 つの都市だけが含まれます。反復的な「設定」プロセスにより、パネル a ～ d にわたってニューロンのアクティビティ (正方形のサイズで示される) が更新されます。このプロセスには、他のユニットに対する各ユニットの勾配を計算することが含まれ、効率的な検索が行われます。](media/fig_hopfield_tank_85_tsp.png)

制約満足問題 (CSP) は、N 個の変数に対して定義された一連の制約を満たす一連の値を見つけることとして定義されます ([[@Tsang14]])。古典的な例は、N クイーン問題です。この問題では、2 つのクイーンが互いに脅し合わないように、N 個のチェスのクイーンをボード上に配置する必要があります。このような問題のもう 1 つは、_巡回セールスマン問題_ (TSP) で、双方向接続のホップフィールド ネットワークを使用して [[@^HopfieldTank85]] によって分析されます。これには、_N_ 都市間の最短距離のルートを見つけることが含まれます ([[#figure_hopfield]])。

したがって、CSP は本質的に、すべての可能な状態に対して [[search]] を実行して、課せられた一連の制約に最もよく適合する状態を見つけるという問題です。状態の数が増加すると、可能な状態の数は [[curse of dimensionality]] により指数関数的に増加します。

双方向接続されたニューラル ネットワークは、_専用並列_ 表現に対する単一の勾配ベースの計算ステップですべての制約を統合し、考えられる解の状態に対して_確率的勾配降下_ プロセスを効果的に実行することにより、この検索プロセスを非常に効率的な方法で実装できます。これは、[[search]] で説明したように、可能な表現の高次元空間を検索するために [[error-backpropagation]] 学習で使用される戦略と本質的に同じです。数学的には、これは実質的に [[error backpropagation#backpropagation to activations]] のプロセスです。

純粋なフィードフォワード ネットワークは、現在の入力セットを処理するときに表現を動的に適応させず、学習した重みに基づいて 1 回のスイープで表現を生成するだけです。したがって、彼らは現在の状況を解釈する最も_満足のいく_方法を見つけるためにこれらの表現を最適化しているわけではありません。対照的に、双方向に接続されたニューロン間の反復的な往復の相互作用により、最終的に能動表現が最適化され、その後の学習の基礎が提供されます。



</section>

</article>
</main>
