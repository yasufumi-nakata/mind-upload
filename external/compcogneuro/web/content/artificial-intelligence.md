---
layout: default
title: "compcogneuro/web: artificial-intelligence"
description: "compcogneuro/web: artificial-intelligence.md の日本語訳"
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
<p>原典: <a href="https://github.com/compcogneuro/web/blob/main/content/artificial-intelligence.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/web/blob/main/content/artificial-intelligence.md</a></p>
<p>ライセンス: Text: CC BY 4.0; code: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
+++
Categories = ["Computation", "Cognition"]
bibfile = "ccnlab.json"
+++
**人工知能** (AI) は、1950 年代から 1990 年代にかけて開発された記号推論システム (基本的にシリアル [[Turing machine]] の普遍的な計算能力に基づく) や、[[large language models]] を含む現在の [[abstract neural network]] (ANN) モデルなど、非常に広範囲にわたるさまざまな計算フレームワークを記述するために長年にわたって使用されてきました。 (LLM)。

何を「知性」とみなすかという問題は難しい。なぜなら、私たちは人間を唯一の利用可能な参照点として利用する一方で、自分自身の特定の知性のブランドの癖にあまり直接結び付けられることを望まないからである。何が知的であるかについての明確な基準を定義する試みは、難しいことで有名であり、チューリングテストは満足のいくものではない実用的なアプローチを提供します。つまり、人間との違いを見分けることができない場合、それは知的であるに違いありません。

AI における有用な区別の 1 つは、知能の「狭い」形式と「一般的な」形式との間であり、「新しい AI」モデルのほとんどはより狭い種類のものです。たとえば、1997 年に IBM によって作成された _Deep Blue_ チェス プレイ システムは明らかに非常に限定的であり、チェスをプレイすること専用に設計されていました。他のほとんどのゲームプレイ モデルも、ドメイン全般の学習メカニズム ([[@SilverHuangMaddisonEtAl16]] など) を使用している場合でも、同様に特定のゲーム用に最適化されています。同様に、他のほとんどのディープ ニューラル ネットワークは、画像認識などの特定のタスクのみに適しています。

したがって、AI の新しい目標は、人工汎用知能 (AGI) を達成することです。AGI では、システムは、広範囲の領域にわたって人間レベルの [[generalized|generalization]] 知能に近づくものを達成します。 LLM は AGI を達成したか、少なくともそれに非常に近いものであると主張する人もいます。しかし、これに対する反論は、彼らは実際には自分自身の「真の」知性をあまり持っておらず、代わりに彼らが訓練された人間の文章の集合的な出力に表されるように、かなりの量の人間の知性を吸収しているだけであるというものです。これらのモデルがトレーニングされた対象の範囲が膨大であることを考えると、トレーニング資料の単なる「再シャッフル」と、真に知的な認知の兆候であると考えられるものの違いを見分けるのは困難です。

この考え方は、_ドメイン外の一般化_ が AGI の必要な特徴であることを示唆しています (例: [[@Chollet19]]; [[@LakeBaroni17]]; [[@RussinJoOReillyEtAl19]])。ここで、訓練セットから潜在的な汚染を除去するために強力な措置が取られる場合、LLM の証拠はそれほど明確ではありません。たとえば、ある研究では、モデルのトレーニング データの収集後に行われた最近の数学コンテストのパフォーマンスを調査しましたが、パフォーマンスは全体的に比較的劣っています ([マサレナ.ai](https://matharena.ai/))。

非常に基本的なレベルでは、LLM には大きなオンライン学習能力が欠けているため、新しい領域でまったく新しい表現システムを形成できないという事実によって根本的に制限されています。対照的に、人間は実際には、新しい領域への「ゼロショット」一般化はあまり得意ではありませんが、その代わりに、新しい領域での「学習」と目標主導型の問題解決には優れています。

現在の LLM のもう 1 つの明らかな欠点は、動作を形成するのに人間からの外部入力にほぼ完全に依存していることです。彼らは、自分が知っていることすべてに基づいて興味深い考察について空想したり、考えたり答えを発見したりするための興味深い新しい問題を考案したりして、暇な時間を過ごすことはありません。基本的に、彼らは自分が何を知っていて、何を知らないのかを知らないため、問題を解決するために何を知る必要があるかを理解することに重点を置いた問題解決戦略を立てる能力がありません。彼らは人間の推論を模倣するように訓練されており、これによりパフォーマンスがある程度向上しますが、最終的には、LLM の場合と同様、真の人間の問題解決と知性の模倣にすぎません。

## 軸索の一般的な知能

[[Rubicon]] フレームワークは、全体的な軸索モデルに基づいて、相互作用する脳ネットワークを通じて目標主導の問題解決能力がどのように発現するかについての明確な仮説を提供します。このアプローチの主な特徴は次のとおりです。

* 一般知能は、2 つの主要なシステムの相互作用を通じて出現します。1 つは、世界に関するあらゆる種類の「常識」知識をさまざまな抽象レベル (LLM によって適切にキャプチャされます) でエンコードする、豊富で柔軟な [[semantic memory]] システムです。もう 1 つは、[[conscious awareness]] ([[bidirectional connectivity]] 経由) を使用してこの意味記憶の状態を検査および操作できる、目標駆動型の実行制御システムです。問題を推論して解決するためのシステム。

    These two systems depend on different brain areas organized by [[evolution]] and learning to optimize different functional properties, which have been studied by cognitive neuroscientists for many years. A particularly unimaginative but nevertheless influential terminology describes these as System 1 and System 2 ([[@Kahneman11]]). LLMs, and essentially any other ANN framework, are lacking a well-developed model of this executive control system ([[@RussinOReillyBengio20]]), which is the focus of the [[Rubicon]] model.

* 目標主導型の実行機能システムは、意味記憶システムを含む脳全体の学習を促進し、新しい領域の問題解決に役立つ新しい表現を学習します。何度も失敗に終わり、貴重な学習を推進するこの「根性」の能力は、人間の領域における真のイノベーションと最終的な成功のほとんどの例にとって重要な要素です ([[@DuckworthPetersonMatthewsEtAl07]]; [[@DuckworthGross14]])。このような性質は、既存の AI モデルにはまったく欠けています。

* セマンティック メモリと実行制御ネットワークはどちらも、膨大な知識の宝庫を効率的に検索して、当面のタスクに最も関連性の高い情報を見つけるために、双方向の [[constraint satisfaction]] 処理に大きく依存しています。 LLM はこの種の処理を近似できますが、フィードフォワード方向でのみ行うことができるため、トップダウンとボトムアップの制約を同時に統合して、現在の目標に従って感覚入力に従って意味のある解決策を見つけることは不可能です。

[ジョン・マッカーシー](http://jmc.stanford.edu/artificial-intelligence/what-is-ai/index.html) (自称「AI の父」) が主張するように要約すると、次のようになります。

> 知性とは、世界の目標を達成する能力の計算部分です。

しかし、既存の AI システムのほとんどには、重要な目標主導型の実行制御機能や学習機能が欠けているため、どのようにして「真の」インテリジェンスを実現できるのかは不明です。 Axon フレームワークもまだ真のインテリジェンスを実証していませんが、少なくとも必要な要素のいくつかを明確に認識しており、これらの側面をよりよく理解することに取り組むことができます。

要約すると、AGI 用の LLM やその他の現在の ANN テクノロジーを追求する人々の懸念は、「月に到達するために木に登っている」ということです。確かに、月に近づいていますが、使用されているメカニズムに根本的な制限がある場合、それは最終的には実際には機能しません。これらのモデルが示す知性の本当の基盤が、「真の」人間の情報源から吸収した既存のアイデアをリミックスする素晴らしい能力に過ぎないのであれば、彼らが真に自分で考えて真に斬新な問題を解決することは決してできないことは明らかだと思われます。


</section>

</article>
</main>
