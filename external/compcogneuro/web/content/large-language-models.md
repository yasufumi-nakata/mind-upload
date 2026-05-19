---
layout: default
title: "compcogneuro/web: large-language-models"
description: "compcogneuro/web: large-language-models.md の日本語訳"
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
<p>原典: <a href="https://github.com/compcogneuro/web/blob/main/content/large-language-models.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/web/blob/main/content/large-language-models.md</a></p>
<p>ライセンス: Text: CC BY 4.0; code: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
+++
Categories = ["Learning", "Computation"]
bibfile = "ccnlab.json"
+++
**大規模言語モデル** (LLM) は、広く使用されている ChatGPT および関連製品の背後にあるテクノロジーであり、何百万人もの人々が日常的に使用しているため、ほとんどの読者には馴染みのあるものになっているでしょう。何年にもわたる過大な期待を経て、これらの製品は [[artificial intelligence]] (AI) が完全に主流になった時点を表しており、人類文明の終焉などについての際限のない議論を必然的に刺激する一方、少なくともすべての人にとって仕事と教育の性質を変える能力を備えていることは明らかです。

LLM の背後にある基礎となる計算フレームワークは [[transformer]] です。これは、非常に標準的な [[abstract neural network]] コンポーネントと新しい _self-attention_ メカニズムを組み合わせたもので、システムが入力ストリームの他の要素の活性化強度を、それらの入力の学習された変換に基づいて動的に調整できるようにします ([[@VaswaniShazeerParmarEtAl17]])。ネットワーク全体は、インターネット上で利用可能な「すべて」の合理的な部分を表す真に膨大なテキストのコレクションを使用して、テキスト本文内の次の単語を予測するという [[predictive learning]] 目標に基づいてエンドツーエンドの [[error backpropagation]] でトレーニングされます。

LLM は、比較的大きなテキストのチャンクを _Parallel_ で処理し、新しいモデルの一時的な _context_ サイズ (GPT-3 では 2k、GPT-4 では 4k) がますます大きくなります。これにより、バックプロパゲーション メカニズムの [[credit assignment]] プロセスが、多くの積み重ねられた層にわたってあらゆる種類の複雑な回路を開発し、生の入力をこのテキスト チャンク内の次の予測単語に変換することが可能になります。次に、その単語が入力に追加され、このプロセスが繰り返され、プロンプトに基づいて長く印象に残るテキストの一節が生成されます。

[[transformer]] ページで詳しく説明されているように、このシステムは、[[Axon]] および [[Rubicon]] フレームワークの生物学に基づくメカニズムとは大きく異なるメカニズムを使用して、系統的な [[generalization]]、[[semantic memory]]、および [[episodic memory]] の認知プロセスを捕捉します。

これらのメカニズムの違いにもかかわらず、LLM 変換モデルは、これらの重要な認知機能が人間の脳の外側の人工システムでどのように機能するかを示す唯一の実例を提供します。広範な研究により、人間の脳が同様の偉業をどのように達成するかをより深く理解するためにこの驚くべきツールを活用することを困難にしている不透明な「ブラックボックス」の不可解性が徐々に剥がされつつあります（[[@YangCampbellHuangEtAl25]]、[[@McGrathRussinPavlickEtAl24]]、[[@ElhageNandaOlssonEtAl21]]）。最初の一般的な洞察は [[transformer]] ページで説明されており、その他の関連する洞察は本文全体で説明されています。

重要な洞察の例は次のとおりです。

* [[Combinatorial vs conjunctive]] は、学習の一般的な計算原理の文脈で LLM を分析し、LLM は論理積検索テーブルのように機能することを学習することが多く、非常に大きなコーパスによって形成された場合にのみ、より体系的な [[generalization]] を示すと主張しています。

* LLM は、[[self-programmable]] [[Turing machine]] のように機能することを学習し、望ましい目標に向けて動作を推進するために組み立てられた一連の処理ステップに従う能力を与えます。


</section>

</article>
</main>
