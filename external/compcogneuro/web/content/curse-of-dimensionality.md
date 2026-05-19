---
layout: default
title: "compcogneuro/web: curse-of-dimensionality"
description: "compcogneuro/web: curse-of-dimensionality.md の日本語訳"
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
<p>原典: <a href="https://github.com/compcogneuro/web/blob/main/content/curse-of-dimensionality.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/web/blob/main/content/curse-of-dimensionality.md</a></p>
<p>ライセンス: Text: CC BY 4.0; code: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
+++
Categories = ["Computation"]
bibfile = "ccnlab.json"
+++
**次元の呪い** ([[@Bellman57]]) はニューラル計算の多くの側面で発生し、計算アルゴリズムの相対的な長所と短所を理解するための重要なツールとなります。これらの問題に関して人間の直観は一般に (かなり) 不正確であるため、たとえある程度複雑な問題空間であっても、シリアル アルゴリズムが成功することが事実上妨げられます。

したがって、ここでの主な結論は、統合計算フレームワークとしての [[search]] の議論で詳述されているように、次元が増加するにつれて _多項式 _ の計算複雑性を示す、_専用並列、勾配ベース_ アルゴリズムのみが現実世界の問題に対して実行可能であるということです。これが、ニューラル ネットワークが、たとえば [[artificial intelligence]] に対する記号的アプローチよりもはるかに役立つ理由です。 [[Reinforcement learning]]、つまり試行錯誤による検索は、次元の呪いによって深刻な影響を受けます。

## 組み合わせ爆発

この呪いは、空間の次元が増加するにつれて驚くほど早く発生する [組み合わせ爆発](https://en.wikipedia.org/wiki/Combinatorial_explosion) (wikipedia リンク) から発生します。この組み合わせ爆発は、ピクセル密度が増加するにつれて、たとえば 2D モニターのピクセル数など、非常に低い次元ですでに存在しています。メーカーが宣伝する印象的なメガピクセルの増加は、実際には 1D 線形密度の比較的穏やかな増加に相当します (たとえば、1,280 x 720 はほぼ 1 メガピクセルですが、1,920 x 1,080 はすでに 2 メガピクセルです)。

3D ボリューム レベルに移行すると、動物の線形体サイズの増加に伴う質量の増加は、物体がどれだけ大きくなるか、またどれだけ簡単に飛ぶことができるかを制限するという現実世界に大きな影響を及ぼします (たとえば、大きくなったミツバチは単純に飛べません)。

次元ごとに 2 つの値を持つ単純なバイナリ空間では、一意の組み合わせの総数は次のようになります。

{id="eq_exp" title="指数関数的な爆発"}
$$
N = 2^d
$$

この無邪気に見える表情は欺瞞的である可能性があり、人々はその成長の速さを理解するのが難しいです。伝説的な話には、チェス盤メーカーが [チェス盤](https://en.wikipedia.org/wiki/Wheat_and_chessboard_problem) の各マス目にある小麦粒の数を 2 倍にするだけで報酬を要求するというものがあります。この無害に聞こえる要求の結果、合計 18,446,744,073,709,551,615 グレインが得られます。

もう 1 つの楽しい現実のデモンストレーションは、紙の厚さが指数関数的に増加するため、紙を 8 回以上徐々に半分に折るのが難しいことです。世界記録は明らかに 13 で、これには [54,000フィートのトイレットペーパー](https://www.npr.org/sections/thetwo-way/2011/12/05/143150449/record-folders-54-000-feet-of-paper-13-folds-one-new-standard) (NPR リンク) が必要でした。

計算の領域では、比較的単純なゲームでも問題空間のサイズが指数関数的に増大し、この問題空間を通じて単純な総当たり [[search]] アルゴリズムを適用して優れた戦略を見つける能力が制限されます。たとえば、チェスのゲームで問題の空間を完全に探索することは、駒が 7 つある場合にのみ可能ですが、これでも膨大な量の計算とストレージが必要でした。


</section>

</article>
</main>
