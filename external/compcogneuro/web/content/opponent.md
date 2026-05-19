---
layout: default
title: "compcogneuro/web: opponent"
description: "compcogneuro/web: opponent.md の日本語訳"
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
<p>原典: <a href="https://github.com/compcogneuro/web/blob/main/content/opponent.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/web/blob/main/content/opponent.md</a></p>
<p>ライセンス: Text: CC BY 4.0; code: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
+++
Categories = ["Neuroscience", "Computation"]
bibfile = "ccnlab.json"
+++
脳は、学習の形成、ダイナミック レンジの維持、脳システム間の調節的相互作用の可能化など、計算上の重要な利点があるため、さまざまな脳構造にわたるさまざまな形で**相手**の処理に依存しています。

* [[Neocortex]] はプールされたサラウンド [[inhibition]] ダイナミクスに完全に依存しており、競合が発生し、[[attention]] やその他の効果が生じます。その結果、特定の領域内の 2 つの表現は、他の領域に影響を与える能力を巡って効果的に互いに競合し、[[constraint satisfaction]] の重要な要素である「適者生存」の選択圧力と、現在の状況を表現する良い方法を見つける広範な [[search]] プロセスを提供します。

* [[Basal ganglia]] には、この脳システムの出力を制御するために互いに競合する_直接_経路と_間接_経路が十分に文書化されています。 [[BG ventral simulation]] に示されているように、これらの個別の競合する経路があることで、モデルは、相対的な差異に対する適切な感度を維持しながら、広範囲の絶対値にわたって賛成と反対 (賛否両論) の値を重み付けすることができ、これにより、ニューラル スパイキング信号の限られたダイナミック レンジをさらに拡張することができます ([[@CollinsFrank14]])。

* [[motor]] 制御では、筋肉は収縮によってのみ力を発揮するため、筋肉は相手の経路に編成されます。内部の神経経路は、この敵の組織を反映し、敵の経路の両側に励起を適用することで動的利得変調を提供します。これは、[[cerebellum]] が運動動作に影響を与える重要な方法の 1 つです。これにより、脳システム間の一種の「乗算的」な調節的相互作用が可能になり、より効率的に、上位レベルのシステムが下位レベルのシステムに対してより単純で低次元の制御を実行できるようになります。


</section>

</article>
</main>
