---
layout: default
title: "compcogneuro/web: eyeblink-simulation"
description: "compcogneuro/web: eyeblink-simulation.md の日本語訳"
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
<p>原典: <a href="https://github.com/compcogneuro/web/blob/main/content/eyeblink-simulation.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/web/blob/main/content/eyeblink-simulation.md</a></p>
<p>ライセンス: Text: CC BY 4.0; code: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
+++
Categories = ["Simulations"]
bibfile = "ccnlab.json"
+++
TODO: エアパフ瞬き条件付けパラダイムの [[cerebellum]] シミュレーション。

{id="figure_dec" style="高さ:25em"}
![まばたきの遅延条件付けとさまざまな小脳回路の機能的役割。 CS (条件刺激) は有害なエアパフ (US、無条件刺激) に確実に先行し、学習により CS に応じたまばたきの条件反応 (CR) の実行が可能になります。 CS (緊張) は橋核を介して小脳に入り、小脳皮質への苔状線維入力を生じます。この領域の小脳核 (CN) である間位核 (IP) にも側副核があります。エアパフは IO (下オリーブ核) を活性化しますが、これも IP からの抑制を受けます。 CRは、プルキンエ細胞からIPへの抑制入力によって活性化されます。 Cheng et al (2015) より。](media/fig_cerebellum_delay_eyeblink_conditioning.png)

小脳が一種の古典的条件付けをサポートしているという初期の発見 ([[@McCormickClarkLavondEtAl82]]; [[@McCormickThompson84]]; [[@YeoHardimanGlickstein85]]; [[@MaukSteinmetzThompson86]]) は、小脳系の特性の理解にかなりの進歩をもたらしました ([[@ChengJacobsonJacobsonEtAl15]] から [[#figure_dec]]) が、同時にかなりの混乱を永続させてきました。モーターの直接的な関与について。具体的には、小脳は、条件刺激(例えば、トーン)に応答して、有害なエアパフの無条件刺激(US)から目を保護する予防的まばたきの条件反応(CR)を直接駆動すると想定されている。

小脳出力からの推定される脱抑制性駆動を介した CR のこの直接的な活性化は、核モデルによって想定される純粋な感覚予測学習と明らかに互換性がありません。しかし、条件付け中に記録された PC および CN ニューロンの反応の多くは運動モデル ([[@McCormickThompson84a]]; [[@BerthierMoore86]]; [[@JirenhedBengtssonHesslow07]]; [[@GreenSteinmetz05]]) と互換性がなく、代わりに感覚予測モデルと一致していました。

具体的には、この条件付けパラダイムで記録されたほとんどの PC ニューロンは、脱抑制的な減少ではなく、行動的 CR の直前に単純なスパイク発火の「増加」を示しました。これは、条件付けタスクに適用される感覚適応フィルタリング モデルと一致しています。小脳の仕事は、感覚的な US および CS の開始を予測する方法を学習し、これらの刺激が予想されるようになったときに、それらの刺激に対する過渡応答をキャンセルすることです。したがって、予想されるエアパフの時点で、抑制性 PC 駆動のキャンセル活動の増加が予想されます。

その後の研究 ([[@HalversonKhilkevichMauk15]]) では、ニューロンのサブセットを具体的に調べました。

TODO: IN の記録 ([[@McCormickThompson84a]]; [[@McCormickThompson84]])、および [[@BoeleKoekkoekDeZeeuw10]] の結果が表示されます。




</section>

</article>
</main>
