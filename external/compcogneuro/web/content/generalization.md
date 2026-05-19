---
layout: default
title: "compcogneuro/web: generalization"
description: "compcogneuro/web: generalization.md の日本語訳"
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
<p>原典: <a href="https://github.com/compcogneuro/web/blob/main/content/generalization.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/web/blob/main/content/generalization.md</a></p>
<p>ライセンス: Text: CC BY 4.0; code: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
+++
Categories = ["Computation", "Cognition", "Learning"]
bibfile = "ccnlab.json"
+++
**一般化** は、[[computation]] と [[cognition]] の両方で最も重要な概念の 1 つであり、事前学習を新しい状況に適用する能力を指します。これは、心理学の文献では学習の**転移**としても知られており、ここで説明する**生成性** (新しい行動や出力を生成する能力) および**体系性** (ルールに似た方法で行動する能力、たとえば、文法規則を他の方法では意味をなさない文に適用する能力) と密接に関連しています。

一般化する能力がなければ、現実世界の動物は生存することがはるかに困難になるでしょう。なぜなら、世界は常に変化する一連の状況や課題を私たちに提示するからです。人間は、ある種の一般化に特に優れており、私たちと現存する [[artificial intelligence]] モデルとの間の「一般化ギャップ」が、[[artificial intelligence#artificial general intelligence]] (AGI) (例: [[@Chollet19]]) の探求の動機となります。この記事の執筆時点では、人類はまだ、広く認知されている AGI システムの唯一の例です。

## 一般化の種類

{id="figure_generalizations" style="height:15em"}
![一般化の領域。トレーニング データが凸型の部分空間 (島など) に存在する地理的な用語で視覚化されます。近似転送は補間によって発生する可能性があり、テスト項目の周囲に十分なデータがあり、近くのトレーニング項目の加重平均で十分です。これは独立同一分散 (iid) テスト データとして知られており、トレーニング データを作成したのと同じ確率分布から得られます。地理的には、トレーニング データに囲まれた島の小さな湖のようなものです。トレーニング データの領域 (凸包) の完全に外側の点 (つまり、島を越えた「海」) で表される遠方への移動には、ある種の外挿が必要であり、はるかに困難です。島の端 (トレーニング データの端) にある小さな入り江または湾は、中間の「エッジ」ケースを表します。フィギュアのコンセプトはアレックス・ペトロフによる。](media/fig_generalization_iid_ood_lake_ocean.png)

[[#figure_generalizations]] は、より大きな高次元空間内のある種の全体的な「境界」内にあると想定される、特定のトレーニング データのセットに関する 3 つの異なるタイプの一般化を示します。一般化の比較的簡単な形式には、この境界内にしっかりと収まるテスト ケースが含まれます。これらのテスト ケースは、統計文献では「i.i.d.」 = 「独立しており、同一に分散された」テスト項目として特徴付けられています。これらは、たとえば、近いトレーニングのサンプル間で補間することで解決できます。

より困難で興味深い一般化形式には、トレーニング データの「島」を越えた「海」にある「ドメイン外」 (_o.o.d_) テスト ケースが含まれます。これは心理学の文献では**遠方転移**として知られており、学習およびトレーニング技術の一般化に関する多くの研究の焦点となってきました。一般に、ここでの結果は、多くの領域、特に [[executive function]] の領域で期待外れであり、遠距離転送は研究によって大きく異なり、かなりの論争の的となっています ([[@KarbachKray21]])。

一般に、AI モデルは遠距離転送を実行する能力も非常に限られていることが示されており、多くの場合、妥当なレベルの近距離転送を行うにも大量のトレーニングが必要です (例: [[@AlbrechtFettermanFogelmanEtAl22]]、[[@Chollet19]])。 [[large language models]] (LLM) における一般化の程度の評価は、これらのモデルがトレーニングされる膨大なデータセットによって大幅に複雑になります。また、トレーニング セットの真の外側にある汎化テストを見つけようとする試みは、それらの遠方転送能力が、広範なトレーニング セット (例: [マサレナ.ai](https://matharena.ai/)) 内の要素を柔軟に組み合わせる能力よりも制限されていることを示唆しています。

一般化のタイプにおけるこれらのドメインベースの区別に加えて、_生成性_ に関係する重要な側面があります。それは、一般化テストに新しい応答が含まれるかどうかです。新しい歌や詩を作らなければならない場合、それは、すでにコンセプトを持っている、奇妙な見た目の犬を犬 [[categorization|category]] の一員として認識することとは大きく異なります。

一般に、生成性には、[[combinatorial vs conjunctive]] 表現で説明されているように、既存の表現要素の新しい組み合わせ、つまり「組み合わせコード」を形成する必要があります。

## 一般化の根拠

ニューロンのネットワークが学習を一般化できるのはなぜでしょうか?以下に、確立されたメカニズムをいくつか示します。

* **補間**は、トレーニング セットから学習した近くの表現からの「投票」の加重平均を取ることによって機能します。これは、テスト項目がトレーニング項目によって十分に密に囲まれている場合 (つまり、[[#figure_generalization]] の「海」ではなく「湖」) に通常はうまく機能します。

* **抽象化**: [[categorization]] ページで詳しく説明されているように、ますます抽象化された検出器の階層を形成すると、新しい入力を既存のカテゴリのメンバーとして認識できるようになります。一度分類されると、そのカテゴリと適切な行動やその他の精神的表象との間の既存の関連付けをアクティブにすることができます。

* **組み合わせコード**: [[Distributed representations]] は、独立した表現機能を使用してさまざまな分離可能な側面をエンコードできます。これにより、新しい入力は、これらの既存の表現の新しい組み合わせを使用してエンコードされます。たとえば、視覚システムには、色と形状の特徴を個別に表すニューロンがあり、形状と色の新しい組み合わせに自動的に一般化できます。これが可能となるのは、これらの次元が個別の方法で容易に抽出され、自然界がこれらの次元の相対的な独立性の重要な例を提供しているためです。ただし、組み合わせコードには [[binding problem]] という問題があり、[[combinatorial vs conjunctive]] で説明されているように別の課題が生じます。

* **リレーショナル** 一般化はエンティティ間の関係の抽象化に依存するため、これらの関係は、_systematicity_ ([[@OReillyRanganathRussin22]]; [[@WebbFranklandAltabaaEtAl24]]) とも呼ばれる新しいドメインに適用できます。広く研究されている例の 1 つは [[analogical reasoning]] です。この場合、「ソース」ドメインの関係が新しい「ターゲット」ドメインの関係に適用されます ([[@Gentner83]]; [[@Holyoak12]])。たとえば、ソース ドメインを恒星を周回する惑星とし、原子核を周回する電子のターゲット ドメインに適用することができます ([[#figure_structural]])。

	These kinds of abstract relational representations are also known as _structure sensitive_ representations or processes, and are a central feature of symbolic AI models, in the form of _propositional_ representations ([[@FodorPylyshyn88]]; [[@AndersonLebiere98]]). These representations form the basis of _rule-based_ generalization, where a generalizable rule captures necessary relationships among entities in abstract terms. Relational representations are known to exist in the [[parietal]] lobe ([[@OReillyRanganathRussin22]]; [[@SummerfieldLuyckxSheahan20]]).

{id="figure_structural" style="高さ:20em"}
![O.O.Dへの遠方転送ケースは、トレーニング セットのはるか外にあるエンティティによく知られた関係を適用できるようにする「ブリッジング」概念に基づく構造的外挿によって発生する可能性があります。  この図では、軌道の類似した構造により、より馴染みのある概念を使用して、原子核を周回する電子の目に見えない原子の世界を推定することができます。](media/fig_generalization_bridge_ood.png)

[[#figure_structural]] で概念的に説明されているように、遠隔転送を成功させるには多くの認知作業が必要です。まず、既存の知識の範囲内で関連する構造表現 (「リレーショナル ブリッジ」) を構築する必要があります。次に、構造マッピング プロセス ([[@Gentner83]]) を実行して、この橋を横断して、既存の知識の島の安全を超えて、野生の未知の「海」に到達する必要があります。次に、それがどこにもない橋なのか、それとも本当にこの新しい領域への強固な入り口を提供するのかを判断する必要があります。原子系の場合、単純な軌道モデルは部分的にしか適用されず、代わりに、この神秘的で目に見えない微視的な領域で物事がどのように機能するかを正確に理解するには、量子力学の多くの奇妙で新しい概念が必要となります。

したがって、汎用の [[abstract neural network]] がアクティビティの 1 つのフィードフォワード パスで魔法のように遠隔転送の実行を開始することを期待するのは信じがたいことのように思えます。その代わりに、LLM の最近の進歩と一致して、より洗練されたタイプの系統的一般化をサポートするには、かなりの構造化された反復処理 (「推論」) が必要になります。 [[Rubicon]] モデルの目標主導型メカニズムは、この時間的に拡張されるタイプの処理の足場となるように設計されています。

## 数学は一般化をサポートします

科学の場合、大小のあらゆる種類のシステムを理解することを可能にする主要な基礎的な橋渡し構造としての数学の開発には、膨大な量の累積的な文化的努力が費やされてきました。 Math には、一般化をサポートする上記のプロパティがすべてあります。

* 数値は究極の抽象化であり、_quantity_ の抽象プロパティのみを保持し、他のすべてを破棄します。

* 数学的演算を無限の方法で組み合わせて、新しい問題に取り組むことができます。

* 数学の多くの側面は、関係 (より大きい、より小さい、等しい、集合論など) を捉える正確かつ一般的な方法を提供します。

認知神経科学の研究では、頭頂葉の領域が人間や他の動物の脳におけるこれらの表現の多くをサポートしていることが示されています。たとえば、ある種の「精神数線」は、ヒトから霊長類、げっ歯類に至るまでの複数の種の頭頂葉で特徴付けられています ([[@DehaeneDehaene-LambertzCohen98]]; [[@NiederMiller04]]; [[@NiederDehaene09]])。より一般的には、数学的推論は、頭頂葉で発達する広範な空間表現を活用すると考えられています ([[@UngerleiderMishkin82]]; [[@OReilly10]])。

したがって、はるかな一般化をサポートするために数学を使用する能力は、性質（頭頂葉の特別な接続性およびその他の特性を持つ）と育成（教育を通じて蓄積された文化的な数学的知識にさらされる）の両方に依存すると考えられます。現在進行中の主な研究目標は、この種の空間化された関係表現をサポートする頭頂葉の特性の観点から、この方程式の本質部分をより深く理解することです。

<!--- TODO: point to models of spatial learning here -->

## プログラミングは一般化をサポートします

コンピューター プログラムは、一般化のためのもう 1 つの重要なソース ドメインであり、体系的で一般化可能な動作の実装を直接可能にする外部ツールを提供します。実際、コンピューター プログラムを使用した脳の計算シミュレーションが、ここで行われる取り組みの基礎全体です。こうしたシミュレーションは、誰にとっても紙の上で実行することは不可能であり、ましてや頭の中で実行することは不可能です。

すべてのプログラミング言語は、型、関数、および構造の形式で強力なリレーショナル抽象化を提供し、強力に体系化された一般化された機能をサポートします。たとえば、関数は、型システムによって課される制約に従って、任意の値を取ることができる引数を指定します。

```Go
Add := func(a, b int) int {
    sum := a + b
    fmt.Printf("%d + %d = %d\n", a, b, sum)
    return sum
}

Add(2, 3)
Add(5, 7)
```

Thus, this one function can operate on any two arguments, providing massive levels of systematicity and generalization. The types can be further qualified and specified to more strongly constrain the relationships among variables, etc.

Consistent with these properties, we argue that the ability to be [[self-programmable]] at least to some extent is an essential property for supporting systematic out-of-domain generalization abilities in the human brain. We can use our [[language]] capacities to talk ourselves through extended sequences of actions, and remember key intermediate values, enabling us to solve complex novel problems that otherwise would be impossible in a single parallel step of standard neural processing.



</section>

</article>
</main>
