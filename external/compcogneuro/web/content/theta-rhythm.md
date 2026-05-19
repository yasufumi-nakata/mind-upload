---
layout: default
title: "compcogneuro/web: theta-rhythm"
description: "compcogneuro/web: theta-rhythm.md の日本語訳"
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
<p>原典: <a href="https://github.com/compcogneuro/web/blob/main/content/theta-rhythm.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/web/blob/main/content/theta-rhythm.md</a></p>
<p>ライセンス: Text: CC BY 4.0; code: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
+++
Categories = ["Neuroscience"]
bibfile = "ccnlab.json"
+++
**シータ リズム**は、脳のさまざまな領域で見られるおよそ 5 Hz の振動で、その特徴的な周期は 200 ms (1000 ms / 5 Hz = 200 ms) です。さまざまな哺乳類種にわたって、このタイムスケールでの処理を中心に特に組織化された神経機構が存在することを示唆する神経科学の証拠の多様な情報源が数多くあります。その中には次の 2 つの著名な例があります。

* 人間を含む霊長類では、固視持続時間の中央値は約 200 ミリ秒で非常にピークに達します ([[@DevillezGuyaderCurranEtAl20]])。私たちは一度に約 200 ミリ秒の間ものを見る傾向があります (引用)。

* げっ歯類 [[hippocampus]] のシータサイクルは広範囲に研究されており、海馬形成全体にわたって複雑な一連のダイナミクスを駆動します (引用)。

このタイムスケールは、[[Axon]] フレームワークにおいて、[[predictive learning]] および [[kinase algorithm]] 学習メカニズムのプロセスを組織するために重要な役割を果たします。シータ サイクルの生物学的性質はかなりの柔軟性を示し、環境内で発生する顕著なイベントと継続的に同期させることができますが、私たちは通常、モデルのトレーニングとテストに使用するシミュレートされた環境にこの 200 ミリ秒の時間枠を単純に課すという非常に簡単な点を利用します。

<!--- TODO: more? -->

## 脳幹の起源: VTN、MMB

（グッデンの）腹側被蓋核（VTN）_には、本質的にシータリズム振動を生成する細胞内電流を持つニューロンが含まれており、海馬に集まる内側側頭葉経路にこのリズムの源を提供している可能性があります。これらの VTN ニューロンは内側乳頭体 (MMB) に投射し、MMB は [[thalamus]] の前腹側 (AV) 核に強力な駆動入力を提供し、その後海馬の海馬台に投射します。

<!--- TODO: figure, more details about MMB contributions, top-down vs. bottom-up reset etc. -->


</section>

</article>
</main>
