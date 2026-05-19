---
layout: default
title: "compcogneuro/web: neuromodulator"
description: "compcogneuro/web: neuromodulator.md の日本語訳"
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
<p>原典: <a href="https://github.com/compcogneuro/web/blob/main/content/neuromodulator.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/web/blob/main/content/neuromodulator.md</a></p>
<p>ライセンス: Text: CC BY 4.0; code: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
+++
Categories = ["Neuroscience", "Rubicon"]
bibfile = "ccnlab.json"
+++
**神経調節物質** は、ニューロンの学習と活動に「調節」効果をもたらす神経伝達物質の一種です。神経調節物質は通常、脳全体に非常に広範な影響を与えるため、最も重要な生存に関連する信号を伝達し、覚醒-睡眠サイクル全体の覚醒レベルを調節するためにも重要です。 [[Rubicon]] フレームワークは、これらの神経調節物質の一部の生物学に基づいた実装を提供し、目標主導型の動機付けられた行動において中心的な役割を果たします。

このような神経調節物質はいくつかあり、それらはすべて脳全体に重複しながらも区別可能な効果をもたらします。

* [[Dopamine]] (DA)。これは、[[TD#reward prediction error]] (RPE; 予測報酬と実際の報酬の差) をエンコードすることで学習を調整するのに特に重要です。大衆文化ではドーパミンが「快楽」を意味するものとして使われてきましたが、RPE は生の報酬信号そのものではなく、「差」の尺度であるため、実際には学習信号の方がはるかに多いのです。

* [[Acetylcholine]] (ACh)。これも学習にとって重要ですが、[[basal ganglia]] およびその他の領域のニューロンの興奮性を大幅に調節します。 [[Rubicon]] モデルでは、ACh は明確な「顕著性」信号であり、報酬イベントと報酬予測イベントの両方、および新しい刺激の開始を反映します。ドーパミンとは異なり、ACh はエラー (RPE のような) 信号ではなく、「生の」報酬または報酬の予測を表します。これにより、RPE 差異特性が重要であるドーパミンの学習固有の役割とは対照的に、新しい目標状態に取り組むことに関与するニューロンの興奮性を調節することができます。



</section>

</article>
</main>
