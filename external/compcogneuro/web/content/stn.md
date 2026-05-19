---
layout: default
title: "compcogneuro/web: stn"
description: "compcogneuro/web: stn.md の日本語訳"
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
<p>原典: <a href="https://github.com/compcogneuro/web/blob/main/content/stn.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/web/blob/main/content/stn.md</a></p>
<p>ライセンス: Text: CC BY 4.0; code: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
+++
Categories = ["Rubicon", "Neuroscience"]
Name = "STN"
bibfile = "ccnlab.json"
+++
**視床下核** (STN) は、[[basal ganglia]] 回路の一部であり、[[neocortex]] から直接入力を受け取り、外淡蒼球 (GPe) と双方向に接続され、出力核 (SNr、GPi) に興奮を投影します。 PCore モデルでは、STN は、これらの出力核を励起することによって BG 脱抑制の初期ブレーキを駆動する役割を果たし、次に GPePr (プロトタイプ GPe) ニューロンからリバウンド抑制シグナルを受け取ります。これにより、活動が長期間停止し、BG が意思決定機能を実行するための短い時間枠が開かれます。これは、BG ニューロンの段階的発火の背後にあるメカニズムを提供します。

このページでは、STN が回路内で非常に重要でやや物議を醸す役割を果たすことを考慮して、STN の機能をよりよく理解するために、STN 上のニューラル データについてより詳細に説明します。

[[basal ganglia]] でレビューされているように、BG の発火に関する入手可能なデータの多くは、個々のニューロンの活動の短い周期的なウィンドウと一致しており、これらの短いウィンドウの外側にある線条体ニューロンは著しく沈黙しています。これは、仮説どおりの STN の貢献と全体的に一致しています。

{id="figure_Fujimoto-kita93" style="高さ:20em"}
![STN ニューロンからの神経記録。最初に 2 回の活動のバーストとその後の長期間の抑制が示され、その後回復します。上のパネルは 2 つの最初のバーストのより詳細なタイムスケールのズームインを示し、下のパネルは約 150 ミリ秒のより長いタイムスケールの抑制ウィンドウを示しています。藤本＆喜多著、1993年](media/fig_stn_pause_fujimoto_kita_93_fig3.png)

{id="figure_magill04" style="高さ:20em"}
![異なる応答プロファイルによる STN ニューロンからの神経記録。パネル A と B は、最初に 2 回の活動バーストと、それに続く長期間の抑制を示し、その後回復します。回復ウィンドウについては特に示されていませんが、論文で説明されています。マギルら、2004 年より](media/fig_stn_pause_magill_etal_04.png)

さらに、STN における神経活動の直接記録は、[[@^FujimotoKita93]] および [[@^MagillSharottBevanEtAl04]] からそれぞれ [[#figure_fujimoto-kita93]] および [[#figure_magill04]] に示されているように、一時停止動作を明確に示しています。 STN ニューロンが最初のバースト後に持続的な抑制を受ける期間は約 150 ミリ秒です。

この阻害の原因は上記の論文の著者には不明であり、残念なことに、一般にこの分野で集中的に研究される重要なテーマではありませんでした。既存の電気生理学文献からは 2 つの主要な候補があります。

* 小さなコンダクタンスのカルシウム活性化 K チャネル ([[neuron channels#SKCa]])。[[@^HallworthWilsonBevan03]] によって説明され、現在の PCore モデルに含まれるメカニズムです。最初のバースト活動パターンの結果として入ってくる Ca++ イオンは、その後、さらなる発火を抑制する比較的長時間持続する K+ 電流をオンにします。

* 高い持続プラトー電位による Na+ スパイク駆動チャネルの不活性化 ([[@KassMintz06]])。 [[@BeurrierBioulacAudinEtAl01]])。この不活性化は樹状カルシウムスパイクによって逆転する可能性があり ([[@Kass09]])、STN ニューロンへの他の興奮性シナプス入力が休止を終了できる可能性があることを示唆しています ([[@ChopekHultbornBrownstone19]])。

バーストでは NMDA チャネルにも役割があり、SKCa チャネル ([[@ZhuMunhallShenEtAl04]]) に結合する可能性があります。他の論文では、STN ニューロンのさまざまな電気生理学的特性を調査しています ([[@NakanishiKitaKitai87]]、[[@OtsukaAbeTsukagawaEtAl04]]、[[@KumaraveluBrockerGrill16), and [[@^ChopekHultbornBrownstone19]] では、発火の一時停止など、これらのニューロンの複雑な電気生理学的特性について説明しています。

## STN における異質性

{id="figure_stn-neurons" style="高さ:20em"}
![分子マーカーに基づく STN 内のさまざまな細胞タイプの分布。腹内側から背外側への強い勾配を示し、DL のみが相性バーストに関連する PV+ タイプを持ちます。 Wallen-Mackenzie 他、2020 年より](media/fig_stn_neurons_wallen_etal_2020.png)

STN 内の複数の細胞タイプ ([[@JeonLeeKwonEtAl22]]; [[@Wallen-MackenzieDumasPapathanouEtAl20]]) および STN ニューロンからの異なるタイプの投射経路 ([[@SatoParentLevesqueEtAl00]]; [[@KoshimizuFujiyamaNakamuraEtAl13]]) についてはかなりの証拠があるため、STN 機能の上記の特徴付けはおそらく話の一部にすぎません。 [[@^Wallen-MackenzieDumasPapathanouEtAl20]] からの [[#figure_stn-neurons]] は、PV+ タイプが STN の背外側部分にのみ存在し、BG の残りの部分の DL 部分と相​​互接続していることを示しています。この PV+ タイプはバーストを示しますが、PV- タイプはバーストを示しません ([[@JeonLeeKwonEtAl22]])。

{id="figure_mirzaei" style="高さ:10em"}
![STN ニューロンからの神経記録。いくつかのニューロンは三相性のバーストと一時停止の活動パターンを示しますが、そうでないニューロンは、不均一なニューロン タイプの集団と一致します。これらのニューロンは、Go キューの前に負のランプ活動レベルを示しました。正のランプを示した他のニューロンは、バースト一時停止活動を示さなかったのです。ミルザエイら、2017 年より](media/fig_stn_burst_pause_mirzaei_etal_17.png)

したがって、[[basal ganglia]] の [[basal ganglia#figure_ds-actions]] に示される DLS ニューロンの活動の厳密な位相窓は PV+ タイプに限定されている可能性がありますが、VMS ニューロン ([[basal ganglia#figure_vs-maze]]) で見られるやや幅広く、より多様な活動プロファイルは PV-STN ニューロンに関連している可能性があります。 [[#figure_mirzaei]] は、手がかり選択課題中のラット STN からの記録データを示しています。記録されたニューロンのいくつかはバースト - 一時停止 - 発火の三相性活動を示しますが、他のニューロンは示さず、代わりに約 400 ミリ秒後に発火します。この論文には、GPe 神経発火パターンに関する [[basal ganglia]] でレビューされた他の論文と一致する関連データも含まれています。

<!--- ## Hold-your-horses vs pause models -->



</section>

</article>
</main>
