---
layout: default
title: "compcogneuro/web: vor-simulation"
description: "compcogneuro/web: vor-simulation.md の日本語訳"
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
<p>原典: <a href="https://github.com/compcogneuro/web/blob/main/content/vor-simulation.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/web/blob/main/content/vor-simulation.md</a></p>
<p>ライセンス: Text: CC BY 4.0; code: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
+++
Name = "VOR simulation"
Categories = ["Neuroscience", "Simulations"]
bibfile = "ccnlab.json"
+++
<!--- <sim-vor> -->

<div>

＃＃ 導入

このシミュレーションは、[[cerebellum#vestibulo-ocular reflex]] (VOR) の対話型モデルと、[[cerebellum]] **フォワード モデル** 学習の寄与を提供します。このモデルに進む前に、重要な背景情報については、これらのリンクを参照してください。

### 既存の計算モデル

#### リスバーガー 1994

最も初期のモデルの 1 つは、**HGVP** (水平注視速度プルキンエ) 細胞を特徴としており、この細胞は **FTN** (前庭核内の綿状標的ニューロン) に抑制を投射し、その後眼球運動系に投射し、前庭系の小脳核ニューロンと機能的に同等です。これらのニューロンは、高い緊張レベルの活動を持ち、興奮性 ([[@MatsunoKudohWatakabeEtAl16]]) で、2 つの異なるサブタイプが反対方向に反応します: E_i = 同側、E_c = 対側の眼球運動関連活動 ()。

通常の条件下では、同側のニューロンは同側方向への頭部の動きに反応して発火を増加させるが、対側のニューロンは逆のパターンを示し、典型的な敵によって組織化されたシステムを提供する。 VOR トレーニングでは、VOR ゲインの増加は主に E_c 相手の速度感度の大幅な低下と関連し、E_i 同側方向の感度の小さな増加 (つまり、抑制が大幅に減少し、励起がわずかに増加) に関連していました。対照的に、VOR 利得の減少は、E_c 対戦相手の活動および E_i 活動の増加と関連していました。

* E_i -> Ipsi = 頭が回転するイプシ、*目* が回転するコントラ!!
* E_c -> contra = 頭の回転コントラ、*目* 回転のイプシ

GAIN = この 2 つのバランス!どちらか一方だけではありません。さらにゲイン -> E_i+、E_c-;ゲインが小さい -> E_i-、E_c+

全体として、HGVP プルキンエ細胞のほとんどは、VOR の最初の修飾成分を駆動するには反応が遅すぎるため、FTN への脳幹前庭入力の変化によって駆動される必要があります。HGVP は可塑性に寄与している可能性がありますが、FTN ニューロンが重要な学習のほとんどの場所であることは明らかです。


</section>

</article>
</main>
