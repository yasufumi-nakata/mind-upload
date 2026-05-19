---
layout: default
title: "compcogneuro/web: adaptation"
description: "compcogneuro/web: adaptation.md の日本語訳"
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
<p>原典: <a href="https://github.com/compcogneuro/web/blob/main/content/adaptation.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/web/blob/main/content/adaptation.md</a></p>
<p>ライセンス: Text: CC BY 4.0; code: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
+++
Categories = ["Activation", "Neuroscience"]
bibfile = "ccnlab.json"
+++
**適応** (**順応**または**神経疲労**としても知られています) は、ニューロンの活動性の関数として、時間の経過とともにニューロンの反応性を低下させるプロセスです。これは、異なる時間にわたって動作するいくつかの異なる [[neuron channels#adaptation channels]] によって生物学的に駆動され、そのほとんどがカリウム (K) チャネルのコンダクタンスに影響を与えます。

適応の機能的利点は、**新規フィルター** ダイナミックを生成することです。「新しい」非適応ニューロンに当たる新規入力は、すでに処理されている進行中の入力と比べてより強力な応答を生成し、その結果、適応されたニューロンを駆動します ([[@Benda21]])。さまざまな適応チャネルの状態を切り替えることで、個々の [[neuron simulation]] でこの動作を調べることができます。

さまざまな K チャネルに加えて、**シナプス抑制** ([[@AbbottVarelaSenEtAl97]]) がシナプス特異的適応の重要なメカニズムとして提案されており、これはニューロンレベルの適応メカニズムよりも大幅に選択的である可能性があります。しかし、覚醒している非麻酔動物での研究では、進行中の神経活動の自発的レベルは、ほとんどのシナプスを効果的に強直性抑制状態にするのに十分であり、したがって、このメカニズムの機能的寄与が制限されることが示されている（[[@BoudreauFerster05]]、[[@Borst10]]、[[@BuchholzGuilabertEhretEtAl23]]）。

[[@^Borst10]] は入手可能な文献を特に徹底的に検討し、覚醒している動物の神経計算においてシナプス抑制が重要な役割を果たす可能性は低いと結論付けています。彼は、ニューロンのスライスまたは培養物（_in vitro_）で行われた研究と、麻酔をかけられた動物を含む_in vivo_とは異なる、覚醒した無傷の動物（[[in activo]]と名付けた）で行われた研究との区別にも一般的に当てはまる多くの点を挙げています。 [[@^Borst10]] が指摘するように、一般に、覚醒中の脳の動作は全体的により直線的になる傾向があり、短期的な可塑性やバースト性は低くなります。

シナプス抑制に関するもう 1 つの問題は、シナプス抑制が主にシナプス前ニューロンのスパイクによって引き起こされ、シナプス後ニューロン ([[@NeherSakaba08]]) の活動状態にはほとんど依存しないことです。したがって、実際には、シナプス前ニューロン全体に作用する適応メカニズム以上の特異性を提供するものではありません。計算上、これは便利です。なぜなら、ニューロン レベルで動作するメカニズムと比較して、シナプスでメカニズムをシミュレートする方がはるかにコストがかかるからです。




</section>

</article>
</main>
