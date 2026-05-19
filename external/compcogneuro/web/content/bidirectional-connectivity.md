---
layout: default
title: "compcogneuro/web: bidirectional-connectivity"
description: "compcogneuro/web: bidirectional-connectivity.md の日本語訳"
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
<p>原典: <a href="https://github.com/compcogneuro/web/blob/main/content/bidirectional-connectivity.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/web/blob/main/content/bidirectional-connectivity.md</a></p>
<p>ライセンス: Text: CC BY 4.0; code: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
+++
Categories = ["Learning", "Activation", "Neuroscience", "Computation"]
bibfile = "ccnlab.json"
+++
双方向の興奮性接続は、[[constraint satisfaction]]、[[attractor dynamics]]、[[top-down attention]]、画像などの複数の重要な機能特性をサポートします。最も広いレベルでは、[[conscious awareness]] のほとんどの理論は、全対全の方法で情報を直接共有できるかどうかにかかっており、これは双方向接続に直接依存するか ([[@Lamme06]])、またはグローバル ワークスペースや関連する構成要素 (例: [[@Baars02]]、[[@DehaeneLauKouider17]]; [[@DehaeneKerszbergChangeux98]]; [[@SethBayne22]])。

ほとんどの [[abstract neural network]] (ANN) モデルと比較して、[[Axon]] は完全な双方向接続を直接組み込んでいる点で独特であり、そのため、この接続によってもたらされる計算上および機能上の利点を得ることができます。ただし、双方向の興奮性接続に伴う実用上の重大な問題もあります。たとえば、複雑な活性化ダイナミクスを生成する傾向があり、正のフィードバック ループの暴走を容易に引き起こす可能性がありますが、残念ながら人間の脳でもてんかん発作の形で発生します。これらのフィードバック ループを制御するには、[[inhibition]] の堅牢な形式が重要です。

複雑な活性化ダイナミクスのコンテキストでは学習もはるかに困難であり、興味深いことに、双方向に接続されたネットワーク内での学習を完全に回避し、代わりに単純なフィードフォワード [[error-driven learning]] メカニズムを介して信号をデコードできる複雑な動的アクティビティ状態の「貯蔵庫」としてネットワークを使用する [[reservoir computing]] ネットワークからは驚くほど印象的な結果が得られます。

対照的に、[[Axon]] の学習形式は、ネットワーク全体にエラー信号を伝播するための双方向の興奮性接続に大きく依存しており、[[temporal derivative]] に基づく学習の原理を活用して、大規模で複雑な双方向ネットワークを調整して環境の効果的な [[predictive learning]] 表現を開発できます。現在、新皮質全体に存在する皮質錐体ニューロンとシナプス機構が関与する、広く研究されている少なくとも 1 つの特定の経路において、この形式の学習と一致する実験的証拠が存在しています ([[Jang et al (2026)]])。

計算コストの観点から見ると、双方向接続はシナプス接続の数が 2 倍になり、単一の入力を処理するのにネットワーク経由で約 200 回の反復が必要になるため、非常に高価です。これにより、現在のフィードフォワード ANN モデルの優れた計算パフォーマンスの主な原動力となっているモデルをスケールアップする能力が大幅に制限されます。それにも関わらず、並列計算ハードウェアが改良され続けるにつれて、この制限は克服されることが期待されます (そして、[[Axon]] の現在のバージョンは、WebGPU を使用して任意の GPU 上で効率的に実行されるため、ブラウザー経由でも動作します)。当面、モデルは、スケーリングに伴う生のパフォーマンスの向上ではなく、原則を捉えることに重点を置いています (詳細については、[[bias-variance tradeoff]] を参照してください)。

## 双方向の興奮性結合の生物学

新皮質における双方向の興奮性結合の生物学の詳細については、[[neocortex#biology of the neocortex]] を参照してください。

接続の基本パターンには、より周辺的な感覚領域からより高いレベルのより抽象的な領域への **ボトムアップ** または **フィードフォワード** 接続が含まれます。これらの経路は、[[categorization]] の主要なプロセスをサポートします。上位層からの **トップダウン** または **フィードバック** 接続により、接続の双方向の側面が提供されます。

直感的には、これらのトップダウン接続は、より高いレベルの知識をより低いレベルの処理段階にもたらすことによって、あいまいな入力を解決する機能をサポートします (例: [[@AngelucciBressloff06]]、[[@BarKassamGhumanEtAl06]]、[[@OReillyWyatteHerdEtAl13]])。たとえば、大勢の人が集まる中で (スポーツ イベントやショッピング モールなどで) 仲間を検索しようとしている場合、探しているもののイメージ (赤いジャケットなど) を保持しておくと、下位レベルの段階で関連する処理を促進するのに役立ちます。

したがって、大脳新皮質の複数の層を通る興奮のフィードフォワード フローは、より高いレベルの抽象化を開発することで私たちを知的にすることができますが、逆方向の興奮のフィードバック フローは、私たちをより「堅牢」、「柔軟」、「適応性」にするのに役立ちます。このフィードバック経路がなければ、システムは、フィードフォワード、ボトムアップの情報の流れの中でシステムを最も強く駆動するために何が起こったとしても、それに基づいて応答することしかできません。しかし、多くの場合、私たちの第一印象は間違っているか、少なくとも不完全です。

同じ処理レベルでニューロンを相互接続する **側方** 興奮性結合もあり、一貫した活動パターンを相互にサポートするのに役立ちます。これは [[necker cube simulation]] に示されており、さまざまな視覚的特徴が横方向の接続を通じてどのように相互にサポートし、曖昧な視覚入力の一貫した全体的な解釈を推進できるかを示しています。これは、[[attractor dynamics]] のより広範なカテゴリの特定の例であり、双方向接続の計算機能のより抽象的で高レベルの特徴付けを提供します。

## フィードフォワード展開

双方向接続されたネットワークで発生するのと同じダイナミクスは、原則として、複数の層のカスケードにわたってネットワークを「展開」することによってキャプチャできます。このような各層は、特定の瞬間におけるネットワークの状態を表します。これは、コンピューター プログラムで `for` ループを展開するのに似ています。

```Go
for i := range 3 {
	fmt.Println(i)
}
// unrolled:
fmt.Println(0)
fmt.Println(1)
fmt.Println(2)
```

However, given the small-world connectivity dynamics of the neocortex, where each individual neuron is only a few synapses away from any other, it would therefore in principle require replicating the entire neocortex at each of these levels. This is analogous to in the above programming case to the amount of code contained within the for loop. When that code is just a few statements, it isn't a problem to unroll it (and it will actually be faster). But if that code is a giant complex algorithm, then replicating all that code is impractical.

Therefore, this unrolling approach cannot capture the full extent of a bidirectionally-connected neocortex. Nevertheless, it is likely that the [[transformer]] architecture that powers [[large language models]] is capturing some key elements of this bidirectional dynamic in the cortex.

Another critical difference for the relevance of bidirectional connectivity in [[conscious awareness]] is that the unrolling approach operates across _different neurons_ for each iteration, whereas the biological case is "re-using" the same neurons over time. Given that our subjective conscious state is effectively what it feels like to be this big bidirectionally connected network, it would presumably be quite different if this dynamic was instead happening across a bunch of different neural populations, instead of a smaller set of mutually interacting ones.

## Simulations

* [[faces simulation]] (Part II) demonstrates how top-down and bottom-up processing interact to produce imagery and help resolve ambiguous inputs (partially occluded faces).

* [[necker cube simulation]] demonstrates how lateral excitatory connections can produce attractor dynamics in the case of a classic ambiguous visual stimulus.

* [[cats and dogs simulation]] demonstrates bottom-up and top-down dynamics in a semantic network representing different levels of information about cats and dogs.


</section>

</article>
</main>
