---
layout: default
title: "compcogneuro/web: abstract-neural-network"
description: "compcogneuro/web: abstract-neural-network.md の日本語訳"
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
<p>原典: <a href="https://github.com/compcogneuro/web/blob/main/content/abstract-neural-network.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/web/blob/main/content/abstract-neural-network.md</a></p>
<p>ライセンス: Text: CC BY 4.0; code: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
+++
Categories = ["Learning", "Computation"]
bibfile = "ccnlab.json"
+++
**抽象ニューラル ネットワーク** (_ANN_) モデルは、_人工ニューラル ネットワーク_、_接続主義_、_並列分散処理_ (PDP)、_パーセプトロン_、_バックプロパゲーション ネットワーク_、_ディープ ネットワーク_、_AI_ ([[artificial intelligence]]) モデル、および _ML (機械学習)_ などさまざまな名前で知られており、実行される分散処理のコア メカニズムを含む大規模なモデル クラスを表します。相互接続されたニューロンのような処理要素 (_units_) によって。

おそらく、すべての ANN モデルに共通する最も基本的な特徴は、[[activation]] と [[weights]] の区別です。ここで、活性化は、重み付けされたシナプス接続を介して他のニューロンに伝達されるニューロン活動を表す動的状態変数です。 [[Learning]] は、通常は局所的な活性化状態の影響下で、これらのシナプスの重みの強度を変更することによって発生します。

これらのモデルの概要を説明した後、それらが一般に神経科学、より具体的には [[Axon]] にどのように関連するかを検討します。要約すると、Axon には、多くの ANN モデルとは大きく異なる、神経生物学的に動機付けられた特性が多数あり、機能的に重要な意味を持つ可能性があります。

歴史的には、初期の開発には Frank Rosenblatt の 2 層パーセプトロン モデル ([[@Rosenblatt59]]; [[@Rosenblatt62]]) が含まれていましたが、これは [[@^MinskyPapert69]] によって批判され、このフレームワークの広範な拒否につながりました (振り返ってみると、これは明らかに見当違いでした)。 [[@^RumelhartHintonWilliams86]] によって開発された [[error-backpropagation]] フレームワークを介して「隠しレイヤー」を使用できるようになったことで、これらのモデルへの関心が再び高まりました。しかし、その後の関心の低下（そしてより厳密な統計に基づくフレームワークに注目）の後、[[GPU]] 上で実行される [[@^KrizhevskySutskeverHinton12]] 「AlexNet」ディープ ニューラル ネットワークの驚くべきパフォーマンスが関心の復活を引き起こし、今日まで指数関数的に成長しています。歴史的なレビューについては [[@^LeCunBengioHinton15]] および [[@^Schmidhuber15a]] を参照し、今日に至るまで関連性の高い基本的な洞察については [[@^RumelhartMcClelland86]] を参照してください。

現在広く使用されている [[large language models]] (LLM) は、この一連の作業の最も影響力のある結果を表しており、ChatGPT やその他のさまざまな関連モデルの形で何百万もの人々によって毎日使用されています。興味深いことに、このモデルのコア メカニズムは 1980 年代の [[error-backpropagagion]] モデルに直接遡ることができ、[[GPU]] テクノロジーの大幅な改善の結果、両方のモデルのサイズとトレーニングできるデータ量が大幅に向上したことに大きな進歩が見られます。

インターネット上で人間が生成したテキストの基本的にコーパス全体で LLM をトレーニングできる機能 (つまり、「ビッグ データ」アプローチ) は、LLM が [[predictive learning]] に基づいているという事実に由来します。[[predictive learning]] は、[[Axon]] モデルの中核機能であり、仮説によれば、哺乳類の [[neocortex]] です。対照的に、AlexNet モデルでは、そのモデルや他の多くの誤差逆伝播モデルで誤差信号を駆動するカテゴリ ラベルを提供するために、人間がラベル付けした画像の大規模なコーパス (_ImageNet_ コーパス; [[@DengDongSocherEtAl09]]) が必要でした。具体的には、LLM は、言語入力ストリーム内の次の単語を予測しようとすることによって生成されるエラー信号から学習します。この単純な原理がそのようなモデルの驚くべき能力につながる可能性があることは注目に値します。

一般に、ANN モデルの進歩は、Rich Sutton が明確に述べた [苦い教訓](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) と一致しています。これは本質的に、比較的単純な汎用モデルによって消費される「ビッグ データ」が、より複雑なオーダーメイドのアルゴリズムと表現を開発する試みよりも最終的に優先されるということです。これは、[[bias-variance tradeoff]] のインスタンスです。これは、学習システムに強力なバイアスを組み込むことと、より汎用的な不偏モデルを使用することとの間のトレードオフを制御する基本的な統計原則です。データが不足している場合、学習結果の分散量を減らすために、より強いバイアスが有益です (これは、新しい入力に一般化するモデルの能力に直接関係します)。しかし、データが豊富であれば、バイアスは不要であり、有害ですらあります。

この文脈では、Axon はその中間に位置します。軸索の新皮質 [[error-driven learning]] メカニズムは、事実上、ほとんどの ANN モデルにおける主要な汎用学習メカニズムの生物学に基づいたバージョンです。ただし、[[Rubicon]] モデルは、より強くバイアスされた形式の目標駆動型学習を推進する、[[evolution|evolutionarily]] 形状の強い皮質下脳領域のセットを表しています。このシステムにより、シミュレートされた生物は、より強いバイアスと一致して、大幅に少ない学習試行で新しいスキルを学習できるようになります。

Axon フレームワークと大多数の ANN モデルの最も重要な違いの 1 つは、これらのモデルが厳密に [[feedforward connections]] を使用し、情報がネットワーク全体で一方向 (「順方向」) にのみ流れることです。この制約により、誤差勾配を効率的に計算できるようになり、モデルの活性化ダイナミクスも大幅に簡素化されます。 Axon の中核機能である [[bidirectional connectivity]] をネットワークに組み込むと、その結果生じる「正のフィードバック ループ」により、エラー逆伝播とネットワーク全体の動作の両方に重大な問題が発生します。

したがって、この研究の動機となる主要な科学的疑問は、なぜ脳が双方向接続に基づいているのか、そしてそれによってフィードフォワード ANN と比較して実行される計算の性質がどのように変化するのかを理解することです。中心的な仮説の 1 つは、双方向接続が [[conscious awareness]] にとって重要であるというもので、これにより、厳密なフィードフォワード モデルでは不可能な方法で、システムが独自の知識状態にアクセスできるようになります。したがって、意識の計算上の利点は、この質問に対する 1 つの潜在的な答えを表しており、LLM やその他のモデルを悩ませ続けている「敵対的攻撃」によって明らかにされる作話や「不自然な」失敗の問題を制限できる可能性があります。

## 神経科学に関連した ANN の重要な進歩

以下は、1980 年代のオリジナルのバックプロップ ネットと比べて、最新の ANN モデルの主な進歩の一部です。これらの進歩の中には、軸索の生物学的特性と一致するものもありますが、一致しないものもあります。

* **ReLu 線形化活性化関数。** AlexNet モデルの主な進歩は、以前のモデルで使用されていた _saturating_ シグモイド (S 字型) 活性化関数と比較して、_rectified Linear Unit_ (ReLU) 活性化関数を使用したことでした。この関数の線形的な性質により、ディープ ニューラル ネットワークの複数の隠れ層にわたるエラー信号の指数関数的減衰の問題が解決されます。また、各ユニットにはるかに広い有効ダイナミック レンジを与えるという追加のボーナスもあり、1 つのユニットで多数のシグモイド関数の仕事を実行できるようになります。

	This is _not_ consistent with the known biology, where individual neurons in the cortex have strong saturation properties and a relatively limited dynamic range of activation signaling. This saturating nonlinearity is critical for bidirectional excitatory networks, providing a built-in damping limit on potentially runaway positive feedback dynamics.

    Interestingly, the exponential decay phenomenon is at least partially mitigated in the brain despite the presence of saturating nonlinearities, by virtue of robust [[inhibition]] that keeps most neurons well below the saturation levels of activity. Indeed, neurons in awake behaving [[neocortex]] are characterized as being precisely balanced between inhibition and excitation ([[@ShadlenNewsome98]]; [[@OkunLampl08]]; [[@IsaacsonScanziani11]]; [[@RubinAbbottSompolinsky17]]). This balance right around the threshold of firing also makes them more chaotic and contributes to the Poisson noise observed in spiking neurons, which could also potentially amplify responses to the temporal differences that drive learning in the [[GeneRec]] and [[kinase algorithm]]s.

* **ショートカット接続と _residual_error の重要性。** _residual_error_ 信号に焦点を当てて学習すること (平均値を減算するなど) の重要性に関する [[@^Schraudolph98]] の元の洞察は、深い層間の広範な _shortcut_ 接続を含む [[@^HeZhangRenEtAl15]] の _ResNet_ アーキテクチャで増幅され、詳しく説明されました。重要なアイデアは、これらのショートカット接続により、上位層が下位層で表されるすべての知識から自動的に恩恵を受けることができるため、このより「基本的な」レベルを超えた「残りの」情報の学習に集中できるということです。これらの方向に沿った初期の影響力のあるアイデアは、[[@^FahlmanLebiere89]] の「カスケード相関」アルゴリズムであり、これには、残差の関数として新しいユニットを段階的に追加することが含まれていました。他の広く使用されている正規化メカニズム (「バッチ ノルム」など) も、センタリングと残差誤差に焦点を当てています。

	Shortcut connections are a prominent feature of the brain and are often used in Axon models. Furthermore, the ubiquitous pooled [[inhibition]] in the brain, which is also essential for Axon, provides a form of normalization and dynamic range centering.

* **トランスフォーマーのようなアテンション メカニズム。** オリジナルのバックプロパゲーション ネットワークと比較して最も劇的な最近の革新は、おそらく、LLM で使用される [[transformer]] アーキテクチャへの「アテンション」メカニズムの導入です。確かに、[[attention]] は人間の認知の重要な側面ですが、トランスフォーマーのアーキテクチャは、脳内で動作する際の注意よりも、[[hippocampus]] の [[episodic memory]] 機能をより多く捉えている可能性があります。



</section>

</article>
</main>
