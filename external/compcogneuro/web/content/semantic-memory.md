---
layout: default
title: "compcogneuro/web: semantic-memory"
description: "compcogneuro/web: semantic-memory.md の日本語訳"
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
<p>原典: <a href="https://github.com/compcogneuro/web/blob/main/content/semantic-memory.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/web/blob/main/content/semantic-memory.md</a></p>
<p>ライセンス: Text: CC BY 4.0; code: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
+++
Categories = ["Cognition", "Learning"]
bibfile = "ccnlab.json"
+++
**意味記憶** は、[[neocortex]] の後方領域で人間が世界について獲得する「常識的な」一般知識のすべてを表す認知用語です。これは、個々の具体的な経験エピソードについて学ぶことを指す [[episodic memory]] とは対照的です。 [[complementary learning systems]] (CLS) フレームワークでは、[[hippocampus]] はエピソード記憶 (高速学習とまばらなパターン分離表現) をサポートする神経特殊化を備えていますが、新皮質は [[distributed representations]] に対して低速のインターリーブ学習を実行して、世界についてより効率的かつ体系的に推論できる [[categorization|categorical]] 抽象化を開発します。新しい状況への [[generalization|generalize]]。

[[combinatorial vs conjunctive]] 表現間の基本的なトレードオフ (それぞれ新皮質と海馬における) により、これらの異なるタイプの表現をサポートする個別の神経システムの必要性が生じます。対照的に、[[large language models]] (LLM) で使用される [[transformer]] アーキテクチャには、各層に単一のニューラル ネットワーク コンポーネントがあり、一般的により結合的な表現を好む特性があり、1 つのネットワークでエピソード記憶と意味記憶の両方の組み合わせをサポートします。

これらの LLM モデルは、柔軟な推論と体系的で生成的な行動をサポートするために、人間の本質的にすべての知識に基づいて訓練された意味記憶の力の人間の脳の外での最良の例を提供します。この「結晶化した知能」は、[[prefrontal cortex]] によってサポートされる「流動的な知能」と対比することができます。[[prefrontal cortex]] は、人間にとって、特に困難な新規領域における戦略的で目標に向けた問題解決をサポートするために重要です。

LLM でこれらの「推論」能力を開発するために現在多くの努力が行われていますが、最終的にこれらのモデルを特定の問題の解決に集中させ続けるのは、人間のプロンプトと制御信号です。 [[Rubicon]] モデルは、これらの目標主導型メカニズムが人間の脳内でどのように機能するかを理解するという私たちの試みを表しています。


</section>

</article>
</main>
