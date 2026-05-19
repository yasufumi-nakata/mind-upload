---
layout: default
title: "compcogneuro/web: acetylcholine"
description: "compcogneuro/web: acetylcholine.md の日本語訳"
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
<p>原典: <a href="https://github.com/compcogneuro/web/blob/main/content/acetylcholine.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/web/blob/main/content/acetylcholine.md</a></p>
<p>ライセンス: Text: CC BY 4.0; code: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
+++
Categories = ["Rubicon", "Neuroscience"]
bibfile = "ccnlab.json"
+++
**アセチルコリン** (**ACh**) は脳全体にわたる重要な神経調節物質であり、[[Rubicon]] 目標駆動モデルにおいて [[dopamine]] とともに重要な役割を果たします。これら 2 つの神経調節物質の基本的な違いは、ドーパミンは報酬予測誤差 (RPE) を反映し、_error_、つまり予測との関係に重点を置いているのに対し、ACh はエラー信号成分を含まないむしろ _raw_ 報酬信号であり、新規の予期せぬ刺激に対しても強力に発火することです。

ルビコン フレームワークでは、ACh は、回路の興奮性と学習を調整するために重要です。回路は、目標選択時にのみ関与し、その後、目標の結果で再び関与する必要がありますが、その間では関与しません。この機能と一致して、ACh は将来の報酬を通知する CS と、報酬自体である US に対して起動されます。したがって、CS の開始はゴール選択の機会を提供し、対応する ACh のアクティブ化によってゴール選択回路がより興奮し、実際に発火してゴールを狙うことができるようになります。目標が達成されると、ACh の活動が抑制されるため、目標の追求中にシステムの気が散りすぎなくなります。

中脳の解剖学的に局在する 2 つの核から放出されるドーパミンとは異なり、[[basal ganglia]] を含め、脳全体に多数の異なる ACh 放出部位が存在します。しかし、これらの異なる部位のほとんどは、後背被蓋核 (LDT) と脚橋核 (PPN) という 2 つの中脳核 ([[@Huerta-OcampoDautanGutEtAl21]]) の活動を介して連携しているようです。したがって、計算の観点からは、少なくとも開始点としては、それらを 1 つの調整された信号として扱うことができます。

BFCN = 前脳基底部コリン作動性ニューロン

## 生物学的データ

一般に、ACh システムは生物学的レベルで非常に複雑であり、複数の異なるタイプのムスカリン受容体とニコチン受容体が ACh 結合に対して相反する反応を示し、多くの ACh 放出ニューロンが他の神経伝達物質も同時に放出します ([[@AnanthRajebhosaleKimEtAl23]]; [[@AbudukeyoumuHernandez-FloresGarcia-MunozEtAl19]])。これは、さまざまな方法で動作を最適化するために既存の神経経路を常に微調整する [[evolution|evolutionary]] プロセスと一致しています。明確に定義された計算機能を達成するための学習と変調をサポートする、より一般化されたメカニズムへの関心を考えると、必然的にこれらの詳細の多くを単純化しすぎて省略しています。

### ボリューム送信

[[dopamine]] などの他の神経調節物質と同様に、ACh は通常、広範な神経領域にわたる体積伝達を介して放出され、神経組織の体積内のすべてのニューロンに ACh シグナルを伝達し、ニューロンごとに膨大な数の放出部位が存在します。さらに、個々のニューロンは機能的に関連した多様な標的に投射し、共通の神経調節シグナルの下で遠位神経領域を効果的に結合します ([[@AnanthRajebhosaleKimEtAl23]])。

### 迅速な段階的反応

ほとんどの神経調節薬と同様に、ACh 放出には持続性と位相性の両方の側面があります。ルビコンモデルと一致する、BFCN ([[@LaszlovszkySchlingloffHegedusEtAl20]]) における急速で位相的な行動相関発火の明確な証拠があります。

### 顕著性エンコーディング

* [[@LaszlovszkySchlingloffHegedusEtAl20]]、[[@HangyaRanadeLorencEtAl15]] -- 正と負の両方の価数に応答します。



</section>

</article>
</main>
