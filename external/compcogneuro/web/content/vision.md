---
layout: default
title: "compcogneuro/web: vision"
description: "compcogneuro/web: vision.md の日本語訳"
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
<p>原典: <a href="https://github.com/compcogneuro/web/blob/main/content/vision.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/web/blob/main/content/vision.md</a></p>
<p>ライセンス: Text: CC BY 4.0; code: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
+++
Categories = ["Neuroscience"]
bibfile = "ccnlab.json"
+++
**視覚**は、霊長類、特に人間にとって支配的な感覚様式です。しかし、げっ歯類やその他のほとんどの種では比較的未発達であり、[[olfaction]] (匂い) が支配的な感覚です。夜行性と昼行性のライフスタイルも、げっ歯類の視覚の有効性に大きな違いをもたらします。ラットとマウスは夜行性です ([[@KrubitzerCampiCooke11]])。霊長類では、視覚は遠方の世界の特性に即時かつ詳細にアクセスできるようにするのに特に役立ち、それ自体が [[motor]] の行動を計画し制御するための主要な基盤です。

霊長類以外のほとんどの種では、視覚入力から計算された [[#motion]] 信号が最も重要であり、潜在的な捕食者に警告し、[[vestibular]] システムとともに [[cerebellum]] への入力を駆動して行動の感覚的結果を表現します。前庭入力と運動入力のこの収束は、[[parietal]] 皮質における [[space]] の表現を固定する一連の中脳および視床経路を介して「頭部方向」システムを駆動します。これは、[[hippocampus]] における [[navigation]] および [[episodic memory]] にとって不可欠です。

げっ歯類と霊長類の頭頂経路は質的に類似しており、それに応じて、それらのナビゲーション能力も多くの点で同等です ([[@GrievesJeffery17]])。実際、視覚のこれらの空間的およびナビゲーション的側面は、多くの非哺乳類脊椎動物に共通しており、広範囲にわたる真に驚くべきナビゲーション能力をサポートしています ([[@GrievesJeffery17]])。

空間的に不変な方法 (すなわち、[[#object recognition]]) で物体を認識する能力には、低レベルの網膜トピック入力信号からより安定したより複雑な特徴を段階的に抽出する、比較的大きな皮質領域の 階層的に組織されたシーケンス が必要です。これは、霊長類の [[neocortex]] の一次視覚 **後頭葉**から**側頭葉**までの経路で発生し、霊長類の脳の神経ハードウェアへの多額の投資を表します。対照的に、げっ歯類の視覚野は比較的平坦で不均一であるため ([[@KrubitzerCampiCooke11]])、ラットはパターンに反応できますが、物体そのものを安定して表現する能力がありません。

## 網膜

視覚処理は明らかに目の**網膜**で始まり、そこには光を電気信号に変換する**光受容体**があり、最終的に**網膜神経節**ニューロンのスパイク出力を駆動し、脳のさまざまな部分に広く投影されます。これには、[[thalamus]]への主要な投影が含まれ、その後[[neocortex]]に続きます。

しかし、網膜は受動的な伝達システムとは程遠いものです。網膜は、[[evolution]] を通じて設計された複雑な回路に従って多数の重要な「信号処理」機能を実行し、その後の他の領域での処理のために視覚入力の最も関連性の高い特徴を抽出します。計算レベルでは、網膜は主に **圧縮**、**コントラスト強調**、および [[#motion]] 抽出を実行するため、出力信号は最大限に「効率的」かつ「有益」になります。

## モーション

ほとんどの動物の網膜では運動処理が堅牢に計算されており、**スターバースト アマクリン細胞 (SAC)** が網膜の方向に敏感な信号の検出に重要な役割を果たしています ([[@Wei18]]; [[@MorrieFeller18]]; [[@BrombasKalita-deCroftCooper-WilliamsEtAl17]]; [[@JainMurphy-BaumdeRosenrollEtAl20]]; [[@GreeneKimSeung16]])。これらの細胞は放射状に対称な樹状突起を持ち、中心から外側への運動感度（遠心力場）を示すため、中心のRFから外側に伝播する視覚信号がニューロンを最大限に活性化します。したがって、最大の活性化刺激は、環状に迫り来るような刺激、例えば、中央のＲＦ点を中心とするリング状の刺激にズームインすることになる。

放射対称 DoG セルと同様に、このような放射対称検出器を組み合わせて、異なる SAC 入力の優先領域とヌル領域をオフセットすることにより、全体的な方向固有の検出器を生成することもできます。

遠位樹状枝は、異なる時間的ダイナミクスで双極細胞から入力を受け取り、各遠位枝内で独立した統合ダイナミクスを持ちます。したがって、SAC セルの全体的な応答は、より小さなサブ領域の独立した動き信号の空間統合です。 [[@^WuKimDaceyEtAl23]] は、文献における SAC 機能の 2 つの主な理論を特定します。樹状突起統合特性に基づく_形態学的_ (例: [[@EncisoRempeDmitrievEtAl10]]; [[@TukkerTaylorSmith04]])、および [[@^KimGreeneZlateskiEtAl14]] からの_時空_メカニズムです。

> 体細胞から外側への動きにより、近位 BC が活性化され、続いて遠位 BC が活性化されます。刺激速度が時間差に対して適切であれば、両方の BC グループからの信号が同時に SAC 樹状突起に到達し、合計して大きな脱分極が生じます。体細胞に向かう内側への動きの場合、BC シグナルは非同期的に SAC 樹状突起に到達し、わずかな脱分極のみを引き起こします。したがって、実験的に観察されたように、樹状突起は外側への動きを「優先」します。

これらは相互に互換性がないわけではなく、正確にどのように機能するかについては、現時点で最終的な合意はありません。 [[Axon]] モデルでは、信頼性が高く正確な運動方向と速度 (つまり、速度) 信号を生成する、別の非常に堅牢な運動メカニズムを使用します。これは、SAC ニューロンの特性とも互換性があります。このメカニズムは [[temporal derivative]] 原理に基づいており、以下で説明するように、「高速」と「低速」の時間統合プロセスの差に基づいて計算されます。

この時間微分メカニズムには、目の動きに依存する「ヘビ」のような運動錯視 ([[@ConwayKitaokaYazdanbakhshEtAl05]]) によって活用される、静的コントラスト パターンに基づいて運動アーティファクトを説明できる可能性があるという利点があり、ショウジョウバエでも実証されています ([[@AgrochaoTanakaSalazar-GatzimasEtAl20]])。ショウジョウバエのシステムには、提案されたメカニズムと一致して、速い減衰と遅い減衰、および抑制と興奮の異なる速度も含まれます。

### 時間微分メカニズム

_fast -- low_ 時間導関数の背後にある重要な考え方は、より最近の変更は高速プロセスに反映され、古い変更は低速プロセスに反映されるということです。特に、運動メカニズムは 2 つの異なる _decay_ 速度に依存します。

```
  O o-o O
+||-   -||+
 O       O
```

In the above diagram, the receiving neurons at the top receive balanced fast excitatory + connections and slow inhibitory connections, with the same net synaptic strength. Two receiving neurons from spatially adjacent locations mutually inhibit each other. When there is no motion, the excitation and inhibition cancel out.

When visual input is moving from the right to the left, the right neuron experiences a net inhibitory signal because the slower inhibition persists longer than the fast excitation, while the opposite is true of the left neuron. The opposite pattern holds for motion in the opposite direction. Thus, the relative balance between these paired neurons provides a readout of the motion direction.

Critically, when there is a uniform onset of a novel input, both neurons receive the same initial excitatory transient, which then is balanced by the slower inhibition. Their mutual inhibition cancels this out. The circuit also needs to multiply by the min activity of any input, so that it doesn't just respond to edges where there is nothing and then something. This however does contribute to the static contrast motion illusions.

To ensure zero responding for static elements, it is critical that the temporal integration has a quick (immediate) rise and the difference is in the decay times, so anything that is still is always equalized at the same values. Thus, motion is registered in the immediate trail of a moving element, where the fast trace decays away faster than the slow one. It is therefore always a net inhibitory signal, with the direction of motion experiencing less inhibition than the other.

The ability to capture not only direction but also speed at a fine-grained level is critical, and is a major limitation of the space-time mechanism, which requires different spacing to capture different speeds. In the temporal derivative version, speed correlates directly with the length of the _fast -- slow_ trace, because a more quickly moving object leaves a longer trace. Thus, speed is naturally and accurately computed by the simple summation of these differences, which the dendritic arbor of the SAC is well-configured to do. This speed value needs to be normalized by the instantaneous size of the visual input to be properly calibrated, so that differences in raw visual filter activity are controlled for.

## Color

{id="figure_cone_rod" style="height:35em"}
![Light wavelength (color) sensitivity of human cone and rod photoreceptors. From Bowmaker & Dartnall (1980).](media/fig_retina_cone_rod_color_tuning.png)

The ability to perceive color depends on the presence of photoreceptors in the retina that are sensitive to different wavelengths of light. In humans, we have three **cones** that are maximally sensitive to long (L = Red), medium (M = Green) and short (S = Blue) wavelengths ([[#figure_cone_rod]]; [[@BowmakerDartnall80]]). In addition most vertebrates have **rod** receptors that have a blue-green color tuning, but are much more sensitive to low light and moving (short duration) stimuli.

### Color opponency

To provide an even more compact representation of color, the visual system computes two **opponent** color contrasts, Red -- Green (i.e., L -- M) and Blue -- Yellow (i.e., S - (LM), where Yellow is represented as a combination of red and green) ([[@Conway01]]; [[@Gegenfurtner03]]; [[@SolomonLennie07]]; [[@FieldGauthierSherEtAl10]]; [[@ShapleyHawken11]]; [[@ZhangBarhomiSerre12]]; [[@YangGaoLiEtAl13]])

* Double-opponent are most common, and define an edge in color space (e.g., R-G edge) by having offset opposing lobes of a gabor (e.g., one lobe is R+G- and the other lobe is G+R-) – this gives the usual zero response for uniform illumination, but a nice contrast response. We should probably turn on color responses in general in our V1 pathway, esp if it is just RG and BY instead of all those other guys. Can also have the color just be summarized in the PI polarity independent pathway.

* Single-opponent which are similar-sized gaussians with opponent R-G and B-Y tuning. These are much fewer, and more concentrated in these CO-blob regions, that go to the “thin” V2 stripes. But the divisions are not perfect..

### Computational color

To more accurately represent how humans perceive color as inputs to vision models, we can take advantage of decades of detailed psychophysics research that has developed progressively more accurate perceptual models. These models allow a standard RGB image to be transformed into the corresponding _LMS_ (long, medium, short) responses of the three different cone types ([[@MoroneyFairchildHuntEtAl02]]; [Wikipedia](https://en.wikipedia.org/wiki/LMS_color_space)).

We use the HPE (_Hunt-Pointer-Estevez_) version of the LMS transforms, which start by converting sRGB (s = standard) images into the [XYZ](https://en.wikipedia.org/wiki/CIE_1931_color_space) color space, and from there, using different weights to produce L, M, S outputs.



</section>

</article>
</main>
