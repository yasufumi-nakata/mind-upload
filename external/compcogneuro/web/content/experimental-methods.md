---
layout: default
title: "compcogneuro/web: experimental-methods"
description: "compcogneuro/web: experimental-methods.md の日本語訳"
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
<p>原典: <a href="https://github.com/compcogneuro/web/blob/main/content/experimental-methods.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/web/blob/main/content/experimental-methods.md</a></p>
<p>ライセンス: Text: CC BY 4.0; code: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
+++
Categories = ["Cognition", "Neuroscience"]
bibfile = "ccnlab.json"
+++
このページでは、[[neuroscience]] および [[cognition]] でよく使用される実験手法について、馴染みのない人のために簡単に説明します。

## 刺激周囲時間ヒストグラム (PSTH)

{id="figure_psth" style="高さ:20em"}
![Funabashi et al, 1988 のこのプロットのような刺激周囲時間ヒストグラム (PSTH) プロットは、神経発火データをプロットするのに広く使用されている方法であり、上部には個々の神経スパイクが「ラスター」プロットとして表示され、各行は個別の試行であり、重要な実験時点が垂直線で示されています。下部には、ラスター プロットに示されているよりも大きなデータ プールのヒストグラムが表示されます。バーの高さは、対応する時間ビン内の発火の相対頻度を示します。このプロットは、PFC ニューロンが時間 C でキューに応答し、遅延期間 D にわたって維持され、応答 R の開始直後に発火が突然終了することを示しています。](media/fig_psth_histogram_raster.png)

[[#figure_psth]] は、刺激周囲時間ヒストグラム (PSTH) プロットの例を示しています。これは、特定のタイプの反復試行にわたる個々の神経反応を示すために広く使用されています。これにより、対象の条件の前後のベースラインの発火レベルがよくわかり、ラベル付けされたタスク入力の関数としてアクティビティがどの程度信頼性が高く、強くまたは弱く調整されているかがわかります。

## 表現類似性分析 (RSA)

{id="figure_rsa" style="高さ:20em"}
![代表的類似性分析 (RSA) 類似性行列は、さまざまな実験条件にわたるアクティビティ パターンの類似性メトリックをプロットします。各セルは、横軸でラベル付けされた条件と縦軸でラベル付けされた条件におけるアクティビティ パターンの類似性または距離の値です。多くの場合、相関関係が使用されます。1 は同一性値、0 は相関関係がありません。距離が増加する距離メトリックも使用できます。このデータは、Hunt et al.、2018 によるものです。](media/fig_rsa_matrix.png)

[[#figure_rsa]] では、各セルが特定の条件の組み合わせの値を持つように、さまざまな条件にわたる応答の全体的なパターンを横軸と縦軸にラベル付けして示すために使用される類似度行列 (距離行列の場合もあります) について説明します。

このタイプのプロットは、[[distributed representations]] で説明されているように、集団レベルの反応をより多く伝えるため、通常、個々の神経発火を観察するよりも優れています。


</section>

</article>
</main>
