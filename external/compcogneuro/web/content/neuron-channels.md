---
layout: default
title: "compcogneuro/web: neuron-channels"
description: "compcogneuro/web: neuron-channels.md の日本語訳"
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
<p>原典: <a href="https://github.com/compcogneuro/web/blob/main/content/neuron-channels.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/web/blob/main/content/neuron-channels.md</a></p>
<p>ライセンス: Text: CC BY 4.0; code: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
+++
Categories = ["Activation", "Neuroscience"]
bibfile = "ccnlab.json"
+++
このページでは、特定のニューロン タイプで生物学に基づいた機能的に重要な動作を駆動するために、[[Axon]] [[neuron]] で利用可能なチャネル タイプの全範囲について詳細を説明します。すべてのニューロンは、[[neuron]] および [[neuron electrophysiology]] ページで詳細に説明されている基本的な興奮性チャネル、抑制性チャネル、およびリーク チャネルを使用します。また、次のチャネルの一部は他のほとんどのニューロンで使用されますが、一部は特に重要な特定のニューロン タイプでのみ使用されます。

これらの生物学的に根拠のあるチャネルは、以下に挙げる情報源に基づいて、実際のニューロンの詳細な電気生理学的特性に正確に適合します。これにより、[[abstract neural network]] の単位に比べて多数のパラメータが生成されますが、明確な生物学的または機能的な動機がない限り、これらのパラメータをデフォルト値から変更することはほとんどありません。さらに、幅広いモデルにわたる広範なテストにより、これらの生物学的に根拠のあるメカニズムとパラメーター値が実際に最良の機能結果を生み出すことが示されました。

これらのチャネルのソース コードは、[軸索チャンス](https://github.com/emer/axon/tree/main/chans) ディレクトリにあります。これらのチャネルのほとんどは、以下の [[#table_taus]] に示す時定数パラメータによって制御される [[exponential integration]] を使用します。これらのチャネルのいくつかの実装は、[[@^MiglioreHoffmanMageeEtAl99]]、[[@^PoiraziBrannonMel03]]、[[@^UrakuboHondaFroemkeEtAl08]] などの標準生物物理学的詳細モデルに基づいています。 [AdEx](https://nest-simulator.readthedocs.io/en/stable/models/aeif_cond_exp.html)、[トラウブ HH](https://nest-simulator.readthedocs.io/en/stable/models/hh_cond_exp_traub.html) などの文書化された例については、[[@^BretteRudolphCarnevaleEtAl07]] および [NEST モデル ディレクトリ](https://nest-simulator.readthedocs.io/en/stable/models/index.html) も参照してください。  [ブライアンの例](https://brian2.readthedocs.io/en/stable/examples/index.html) には、[ブルネルとワン、2001](https://brian2.readthedocs.io/en/stable/examples/frompapers.Brunel_Wang_2001.html) を含むさまざまな標準モデルの読みやすい完全な方程式が含まれています。また、優れた概要については [ウィキペディア: 生物学的ニューロン モデル](https://en.wikipedia.org/wiki/Biological_neuron_model) を参照してください。また、NEURON および関連ソフトウェアで作成された生物物理モデルに含まれる電流の標準化されたリストについては、[ModelDB の現在](https://modeldb.science/NeuronDB/NeuronalCurrents)、[ModelDB の現在の検索](https://modeldb.science/ModelDB/FindByCurrent)、および [イオンチャネル系統学](https://icg.neurotheory.ox.ac.uk) を参照してください。

## パラメータ

ここで説明する各チャネル タイプのデフォルト パラメータは、[[neuron#units and parameters|standard units]] を使用して次の表に示されています。

{id="table_taus" title="時間定数"}
|パラメータ |値 |
|---------------------------------|----------|
| AMPA 減衰 $\tau_d$ | 5ミリ秒 |
| GABA-A 崩壊 $\tau_d$ | 7ミリ秒 |
| NMDA 減衰 $\tau_d$ | 100ミリ秒 |
| GABA-B 上昇 $\tau_r$ | 45ミリ秒 |
| GABA-B 崩壊 $\tau_d$ | 50ミリ秒 |
| mAHP、sAHP 最大 $\tau_{max}$ | 1秒 |
| KNa_m 上昇 $\tau_r$ | 50ミリ秒 |
| KNa_m 減衰 $\tau_d$ | 100ミリ秒 |
| KNa_s 上昇 $\tau_r$ | 1秒 |
| KNa_s の減衰 $\tau_d$ | 1秒 |
|キールライズ $\tau_r$ | 14ミリ秒 |
| Kir 崩壊 $\tau_d$ | 23ミリ秒 |
| SKCa上昇$\tau_r$ | 15ミリ秒 |
| SKCa 減衰 $\tau_d$ | 30ミリ秒 |

さまざまなチャネルの [[exponential integration]] 時定数パラメータは [[#table_taus]] に示されています。

{id="table_gs" title="コンダクタンスのスケーリング係数"}
|パラメータ |値 |
|-------|-------|
| NMDA | 0.006 |
|ギャバ-B | 0.015 |
| VGCC | 0.02 |
| A型K | 0.1 |
| mAHP | 0.02 |
| sAPH | 0.05 |
| KNa | 0.2 |
|キル (デフォルト 0) | 10 |
| SKCa (デフォルト 0) | 2 |

上記の [[#table_gs]] は、各チャネルのコンダクタンス スケーリング係数です。これらのチャネルは、全体的な時間変化する `Ge(t)` または `Gk(t)` コンダクタンスにこれらのチャネルを追加し、最終的に g バー係数 (デフォルトでは 100 nS に設定されます) で乗算されるため、大まかに正規化された時間変化するコンダクタンス値を最終的な nS コンダクタンス値に変換する全体的な g バー係数と同じ単位ではありません。さらに、これらのスケーリング係数は、それ自体が正規化された量ではない値を乗算するため、直接解釈することはできず、標準パラメーターの完全なセットを文書化するためにのみここに含まれています。コンダクタンスの全体的な相対的な大きさをよりよく理解できる値については、次の表を参照してください。

{id="table_max-gs" title="典型的な最大コンダクタンス"}
|パラメータ |値 |
|--------------------------|---------------|
|アンパ | 1-200ns |
|ギャバA | 3-400ns |
| NMDA後皮質 | 50ns |
|ギャバ-B | 50ns |
| VGCC | 4ns |
| aK | 10ns |
|マップ | 2ns |
|サップ | 5ns |
| KNa メッド | 3ns |
| KNa遅い | 1ns |

上記の [[#table_max-gs]] は、最終的な時間変化するコンダクタンス値の計算に必要なさまざまな要素をすべて含む、各タイプのチャネルの典型的な最大コンダクタンスを示しています。これらはすべて近似値であり、さまざまなネットワーク レベルのパラメーターとダイナミクス (特に AMPA、GABA-A 阻害、NMDA) に依存するため、相対的な大きさの全体的な感覚を得るためにのみ使用されます。

{id="table_gs-refs" title="他のモデルのコンダクタンス"}
|パラメータ |値 |
|--------------------------------------|------|
| NMDA PFC (ブルネルとワン、2001) | 1 シンセあたり 0.327 ns |
| VGCC 遠位 (Urakubo et al., 2008) | 146ns |
| VGCC 近位 (Urakubo et al., 2008) | 3.2ns |
| VGCC ソーマ (浦久保ら、2008) | 93ns |
| aK 遠位 (Urakubo et al., 2008) | 49ns |
| aK 近位 (Urakubo et al., 2008) | 7.5ns |


## アンパ

AMPA (α-アミノ-3-ヒドロキシ-5-メチル-4-イソオキサゾールプロピオン酸) チャネルは、[[neuron]] で広く議論されている主要な興奮性シナプス入力チャネルです。チャネルは神経伝達物質 **グルタミン酸**の結合によって開き、これによりチャネル構造がねじれて開き、主に $Na^+$ イオンが細胞内に侵入できるようになり、電位が上昇します (興奮)。

AMPA 受容体のコンダクタンスは、_double-exponential_ 関数を使用してモデル化できます。ここで、_t_ はグルタミン酸が受容体に結合してからの時間です。

{id="eq_double_e" title="二重指数関数"}
$$
g(t) = e^{-t / \tau_r} - e^{-t / \tau_d}
$$

$\tau_r$ は、グルタミン酸が最初に AMPA 受容体に結合するときのコンダクタンスの増加の速い _rise_ 時定数 ([[@HestrinNicollPerkelEtAl90]] によると 1 ms 未満)、$\tau_d$ は時間の経過による AMPA 受容体の不活化を反映する遅い _decay_ 時定数であり、によって 4.4 ms と推定されます。 [[@^HestrinNicollPerkelEtAl90]]。

[[@^Rall67]] によって導入された _alpha_ 関数は、単一の時定数を使用して比較的高速なコンダクタンスをモデル化するためにも使用されています。

{id="eq_alpha" title="アルファ関数"}
$$
g(t) = \frac{t}{\tau} e^{-t / \tau}
$$

[[Axon]] モデルでは、[[neuron]] レベル方程式のすべてを統合するために 1 ミリ秒のタイム ステップを使用するため、比較的速い立ち上がり時定数はあまりに早く発生してしまい、関連性がありません。したがって、AMPA コンダクタンスは 1 ms の時間ステップで離散的に増加し、時定数 5 ms の単一の指数関数的減衰関数を使用します。これは、単純なオンライン [[exponential integration]] を使用して計算できます。

{id="eq_ampa_g" title="AMPA コンダクタンス"}
$$
g_{ampa}(t) = g_{e-raw}(t) + g_{ampa}(t-1) \left(1 - \frac{1}{\tau_d} \right)
$$

すべてのチャネルと同様に、このコンダクタンスは、AMPA の反転電位 ($E_{ampa}$) の関数として対応する電流を駆動します。これは 0 mV と推定されます。

{id="eq_ampa_i" title="AMPA 現在"}
$$
I_{ampa} = g_{ampa} \left(E_{ampa} - V_m\right)
$$

## ギャバ-A

GABA-A チャネルは、[[neuron]] および [[inhibition]] で説明されている標準的な抑制性シナプス入力チャネルです。これは、抑制性介在ニューロンの特別な集団によって放出される、GABA (ガンマ-アミノ酪酸) 神経伝達物質の結合によって開きます。これは主に、負に帯電した塩化物イオン $Cl^-$ がセルに流入することを可能にし、電位を負に保つように作用します。

AMPA と同じ方法で、単一の指数関数的減衰関数 ([[#eq_ampa_g]]、減衰時定数 $\tau_d$ 7 ms [[@XiangHuguenardPrince98]] を使用) を使用して GABA-A コンダクタンスをモデル化します。GABA-A の反転電位 ($E_{gaba_a}$) は -75 mV です。

## K リーク

$K^+$ リーク チャネルは常に開いているため、$\overline{g}_{gaba_a}$ でパラメータ化された一定のコンダクタンスと -75 mV の反転電位 ($E_{leak}$) を持ちます。

## NMDA

{id="plot_nmda" title="NMDA チャネル" Collapsed="true"}
「ゴール」
pl := &chanplots.NMDAPlot{}
ルート、_ := tensorfs.NewDir("ルート")
br := egui.NewGUIBody(b, pl, root, "NMDA", "NMDA チャネル", "NMDA チャネル方程式")
pl.Config(root, br.Tabs)
br.FinalizeGUI(false)
br.Splits.Styler(func(s *styles.Style) {
	s.Min.Y.Em(25)
})
pl.GVRun()
「」

NMDA (N-メチル-D-アスパラギン酸) チャネルは脳全体に存在し、[[Axon]] で使用される [[kinase algorithm]] でキャプチャされるように、学習において重要な役割を果たします。 NMDA チャネルの開口部は、膜電位が静止電位に近い場合、通常、正に帯電したマグネシウム イオン ($Mg^{++}$) によってブロックされます。この静止電位を超える膜脱分極の結果としてのこのブロックの除去 ($Mg^{++}$ イオンが細胞の外側にあるため、「外方整流」として知られています) は、このチャネルの 2 つの重要な機能的特徴のうちの 1 つです。このブロック解除のダイナミクスは、学習にとっても、ニューロンの活性化ダイナミクスへの重要な貢献にとっても重要です。

NMDA チャネルのもう 1 つの重要な機能特性は、$Mg^{++}$ のブロック解除に加えて、グルタミン酸神経伝達物質の結合を開く必要があることです。したがって、ゲート要素を 1 つだけ持つ (またはまったく持たない) 他の多くのチャネルとは異なり、NMDA ではこれらの要素の両方が必要です。さらに、$Mg^{++}$ 因子はシナプス後活動 (脱分極) の関数ですが、グルタミン酸はシナプス前ニューロンによって放出されます。したがって、NMDA は、シナプス前とシナプス後の両方の活動の結合に応答する独自の位置にあります。

ブロック解除の動作を確認するには、上の [[#plot_nmda:GV run]] ボタンを押します。これにより、プロットの左側に示されているパラメーターを使用して、コンダクタンス (_g_) (および電流 _I_) 対電圧 (_v_) のプロットが生成されます。ただし、周囲にグルタミン酸が十分に存在するため、その要因は関係ないと仮定します。電圧が -90 度の過分極開始点を超えて増加すると、コンダクタンスは着実に増加します。これは、$Mg^{++}$ イオンがチャネル開口部をブロックしない可能性が徐々に増加することを反映しています。 NMDA チャネルの_反転電位_は約 0 mV であるため、電圧がこの点に近づくと、チャネルを通してイオンを引っ張る正味の力は徐々に弱くなり ([[neuron]] の綱引きの例えで説明されているように)、電圧が 0 に近づくと電流_I_ は減少します。

NMDA チャネルは主に、_カルシウム_ イオン ($Ca^{++}$) が細胞に流入することを可能にし、このチャネルの学習効果は、さまざまなシナプス後化学反応を引き起こすカルシウムの能力によるものです ([[synaptic plasticity]] を参照)。活性化効果はこのイオンの正電荷によるものであり、したがって細胞に対して正味の興奮性 (脱分極) 効果をもたらします。

[[#plot_nmda:Time run]] は、NMDA チャネルのもう 1 つの重要な特徴を示しています。それは、$\tau_d$ 減衰時定数パラメータ ([[#eq_ampa_g]] を参照) が他のほとんどのチャネルよりもはるかに長く、100 ミリ秒以上のオーダーであることです (AMPA と同様、NMDA の立ち上がり時間は無視できるほど十分に速いです)。この比較的長い時定数は、時間の経過とともに [[stable activation]] パターンを作成するため、NMDA チャネルの活性化に寄与するために重要です (詳細な説明とデモンストレーションについては、そのページを参照してください)。

電圧ゲート コンダクタンスに使用する式は [[@JahrStevens90]] によるもので、広く引用されている [[@BrunelWang01]] モデルで使用されています。

{id="eq_nmda_g" title="NMDA 電圧ゲート コンダクタンス"}
$$
g_{nmda}(t) = \frac{g_{e-raw}(t) \overline{g}_{nmda}}{1 + \frac{[Mg^{++}]}{3.57} e^{-0.062 V_d}} - \frac{1}{\tau_d} g_{nmda}(t-1)
$$

ここで、$\overline{g}_{nmda}$ は NMDA 固有の乗数 ([[#table_gs]] を参照)、$[Mg^{++}]$ は細胞外マグネシウム濃度 (通常は 1 ～ 1.5)、$g_{e-raw}(t)$ は [[neuron#Computing input conductances]] で説明されている生の興奮性シナプス入力です。 NMDA 受容体は主に入力を受け取る樹状突起に位置するため、この式では _dendritic_ Vm 膜電位値 $V_d$ を使用します (詳細については、[[neuron dendrites]] を参照)。

この関数はシグモイド、「S 字型」の形をしており、電圧が増加するにつれて漸近値まで増加します。 [[#plot_nmda:GV run]] でわかるように、この関数の関連部分はシグモイドの左側にあります。電圧が増加するにつれて _I_ で見られる減少は、すべてのチャネル コンダクタンス ([[#eq_ampa_i]]) に適用される標準の綱引きオームの法則乗数によるものです。

## ギャバ-B

{id="plot_gabab" title="GABA-B チャネル" Collapsed="true"}
「ゴール」
pl := &chanplots.GABABPlot{}
ルート、_ := tensorfs.NewDir("ルート")
br := egui.NewGUIBody(b, pl, root, "GABA-B", "GABA-B チャネル", "GABA-B チャネル方程式")
pl.Config(root, br.Tabs)
br.FinalizeGUI(false)
br.Splits.Styler(func(s *styles.Style) {
	s.Min.Y.Em(25)
})
pl.GVRun()
「」

GABA-B チャネルは、GIRK チャネル (_G タンパク質結合内向き整流カリウム (K) チャネル_) に結合しているため、標準的な GABA-A 阻害チャネルと比較して減衰時定数がはるかに遅くなります。これは脳内に遍在しており、基本的な神経機能に不可欠であると考えられます。 「内向き整流」は、ニューロンの「内部」からの $Mg^{++}$ イオン ブロックによって引き起こされます。これは、ニューロンが過分極している (非アクティブな) ときにこれらのチャネルが最も開くことを意味し、したがって、非アクティブなニューロンを非アクティブに保つ役割を果たします。これは NMDA チャネルの効果を補完しており、[[@^SandersBerendsMajorEtAl13]] は、[[stable activation]] パターンを生成する際のこれら 2 つのチャネルの相乗的な性質を強調しています。NMDA は活性ニューロンを活性に保ち、GABA-B は不活性ニューロンを不活性に保ちます。

上の [[#plot_gabab:GV run]] ボタンを押すと、プロットの左側に表示されているパラメーターを使用してコンダクタンス (_g_) (および電流 _I_) 対電圧 (_v_) のプロットが表示されます。比較可能な NMDA プロットと比較すると、GABA-B と NMDA が互いに鏡像であることがわかります。さらに、ここでプロットされた _I_ 値は絶対値 (正) ですが、その反転電位 $E_{gaba_b}$ がカリウム (-90 mV) であるため、実際の電流は NMDA と逆の符号を持ちます。

GABA-B チャネルの実装は、[[@^SandersBerendsMajorEtAl13]] および [[@^ThomsonDestexhe99]] に基づいており、[[@^YamadaInanobeKurachi98]] からの次のシグモイド電圧ゲート コンダクタンス関数が使用されます。

{id="eq_gabab_gv" title="GABA-B 電位依存性コンダクタンス"}
$$
g_{gaba_b}(V) = \overline{g}_{gaba_b} \frac{1}{1 + e^{0.1(V-E_{gaba_b}+10)}}
$$

時間の経過に伴う抑制性入力スパイクからの GABA 結合の関数として GABA-B コンダクタンスの時間ダイナミクスを計算するために必要な追加のシグモイド関数があります ([[@ThomsonDestexhe99]] の図 16)。

{id="eq_gabab_x" title="GABA-B スパイク率の統合"}
$$
X = \frac{1}{1 + e^{-(s - 7.1) / 1.4}}
$$

ここで、_s_ は最近の時間枠でのスパイク率であり、[[Axon]] で使用される [[inhibition]] 関数からの $g_i$ 阻害係数に基づいて計算されます。_X_ は、別個の上昇を伴う次の二重指数更新方程式に従って、GABA-B 活性化 (_M_ とラベル付け) の増加を促進します。 ($\tau_r$) 係数と減衰係数 ($\tau_d$) (それぞれ 45 ミリ秒と 50 ミリ秒。[[@ThomsonDestexhe99]] からの時間経過データによく適合します。[[#table_taus]]):

{id="eq_gabab_m" title="GABA-B 活性化 M の経時的"}
$$
M(t) = \frac{1}{\tau_r} \left( \left[(\tau_d / \tau_r)^{(\tau_r / (\tau_d - \tau_r))} \right] X(t) - M(t-1) \right)
$$

$$
X(t) = \left( \frac{1}{1 + e^{-(s - 7.1) / 1.4}} - X(t-1) \right) - \tau_d X(t-1)
$$

最終的な GABA-B コンダクタンスは、上記の [[#eq_gabab_m]] に示されている M 活性化係数と、[[#eq_gabab_gv]] に示されている電圧ゲート係数の積です。

{id="eq_gabab_tg" title="GABA-B 正味コンダクタンスの経時変化"}
$$
g_{gaba_b}(t) = g_{gaba_b}(V) M(t)
$$

[[#plot_gabab:Time run]] を実行すると、これらの時間ダイナミクスが開始時に入力パルスとともに 500 ミリ秒のウィンドウにわたって再生されることを確認できます。

### キル

{id="plot_kir" title="キール チャネル" Collapsed="true"}
「ゴール」
pl := &chanplots.KirPlot{}
ルート、_ := tensorfs.NewDir("ルート")
br := egui.NewGUIBody(b, pl, root, "Kir", "Kir チャネル", "Kir チャネル方程式")
pl.Config(root, br.Tabs)
br.FinalizeGUI(false)
br.Splits.Styler(func(s *styles.Style) {
	s.Min.Y.Em(25)
})
pl.GVRun()
「」

GABA-B が結合する _Kir_ チャネルは、同じ形式の内向き整流電圧依存性を使用して、別個のスタンドアロン チャネルとしても利用できますが、持続的にアクティブな形式です。これらのチャネルはデフォルトでは使用されませんが、特定の細胞タイプにとっては重要です。内向きの整流により、閾値のような双安定動作が追加されます。休止電位を大きく超えて活性化されていないニューロンは、この Kir チャネルから追加のリーク コンダクタンスを取得しますが、一旦活性化され始めると、Kir は不活性化され、より容易に発火できるようになります。これは、大脳基底核の線条体の中型有棘ニューロン (MSN) の動作にとって重要です。MSN は非常に静かである傾向がありますが、十分に活性化されると別個のバーストで発火します。

MSN ニューロン用にパラメータ化された [[@^LindroosDorstDuEtAl18]] の方程式を使用し、活性化因子 M を使用します。これは、[[#plot_kir:GV run]] および [[#plot_kir:Time run]] に見られます。

{id="eq_kir_m" title="Kir 電位依存性活性化 M"}
$$
M_{\infty} = \frac{1}{1 + e^{(V+102)/13}}
$$

{id="eq_kir_tau" title="Kir 変数時定数"}
$$
A = 0.1 e^{-(V+60)/14}
$$

$$
B = \frac{0.27}{1 + e^{-(V+31)/23}}
$$

$$
\tau = \frac{1}{A + B}
$$

{id="eq_kir_dm" title="Kir M アップデート"}
$$
M(t) = M(t-1) + \frac{1}{3 \tau(t)} \left(M_{\infty} - M(t-1) \right)
$$

{id="eq_kir_g" title="Kir コンダクタンス"}
$$
g_{kir} = \overline{g}_{kir} M(t)
$$

## VGCC

電位依存性カルシウム チャネル (VGCC) は、$Ca^{++}$ へのコンダクタンスが電位依存性を持つという点で NMDA チャネルと似ていますが、神経伝達物質結合特性を「持たず」、その電位依存性は通常 NMDA よりも高い閾値にあります (そして、$Mg^{++}$ ブロックによって引き起こされるものではありません)。この閾値が高いため、VGCC チャネルは通常、活動電位の逆伝播中にのみ開きます (詳細については [[neuron dendrites]] を参照)。したがって、VGCC チャネルはシナプス後スパイクと密接に関係するカルシウム信号を提供します。このプロパティを [[kinase algorithm]] 学習ルールで利用します。 VGCC もスパイクが終わるとすぐに閉じるため、活性化ダイナミクスに大きな影響を与えません。VGCC は主に学習にとって重要です。

多数の VGCC タイプ ([[@Dolphin18]]; [[@CainSnutch12]]) があり、活性化の電圧しきい値の降順に文字で示されます: L、PQ、N、R、T で、対応する Ca_v 名: Ca_v1.1、1.2、1.3 があります。 1.4 はすべて L タイプ、2.1、2.2、2.3 はそれぞれ PQ、N、R で、T タイプ（低閾値）は 3.1、3.2、3.3 で構成されます。各チャネルは、電圧依存性と不活性化機能によって特徴付けられます。

{id="table_vgcc" title="VGCC チャネル タイプ"}
|手紙 | Ca_v | V しきい値 |不活性化 |場所 |機能 |
| ------ | ------- | ------------ | ------------ | -------- | --------------------- |
|  Ｌ | 1.1-1.4 |高い (-40mV) |速い |コーテックス + |スパイクを厳密に追跡 |
|  PQ | 2.1 |高い | ?            |小脳 (プルク、グラン) | ?      |
|  N | 2.2 |高い | ?            |どこでも？ | ?                  |
|  R | 2.3 |医学 | ?            |小脳グラン | ?              |
|  た | 3.1-.3 |低い | ?            | 5IB、皮質下 |低周波オシレータ |

* L タイプは、錐体細胞の樹状突起スパインの典型的な「VGCC」であり、以下にプロットします。

* PQ と R は [[cerebellum]] に固有です。

* T タイプは低周波振動にとって最も重要であり、主要なバースト タイプである 5IB 層 5 ニューロン以外の錐体ニューロンには存在しません。これは、TRN などの皮質下ニューロンにとって最も重要です。実装については、[Destexhe 他、BRIAN の 1998 年モデル](https://brian2.readthedocs.io/en/stable/examples/frompapers.Destexhe_et_al_1998.html) を参照してください。

{id="plot_vgcc" title="VGCC L 型チャネル" Collapsed="true"}
「ゴール」
pl := &chanplots.VGCCPlot{}
ルート、_ := tensorfs.NewDir("ルート")
br := egui.NewGUIBody(b, pl, root, "VGCC", "VGCC チャネル", "VGCC L タイプ チャネル方程式")
pl.Config(root, br.Tabs)
br.FinalizeGUI(false)
br.Splits.Styler(func(s *styles.Style) {
	s.Min.Y.Em(25)
})
pl.GVRun()
「」

L タイプ VGCC の実装は [[@UrakuboHondaFroemkeEtAl08]] に基づいており、この [リンク](http://kurodalab.bs.s.u-tokyo.ac.jp/info/STDP/Urakubo2008.tar.gz) で入手可能なソース コードを使用します。

まず、電圧ゲートには、上記と同様のシグモイド関数によって定義される、時間的に不変な側面があります。

{id="eq_vgcc_gv" title="VGCC L 電圧ゲート コンダクタンス"}
$$
g_{vgcc}(V) = -\overline{g}_{vgcc} \frac{1}{1 - e^{0.0756 V}}
$$

さらに、強い時間依存性を持つ _M_ (アクティブ化) と _H_ (非アクティブ化) で示される 2 つの追加の反対側ゲート要素があり、次のようなシグモイド駆動機能があります。

{id="eq_vgcc_m" title="VGCC M ゲート電圧ベースの最大値"}
$$
M_{max}(V) = \frac{1}{1 + e^{-(V + 37)}}
$$

{id="eq_vgcc_h" title="VGCC H ゲート電圧ベースの最大値"}
$$
H_{max}(V) = \frac{1}{1 + e^{2(V + 41)}}
$$

更新方程式は、関連する時定数を使用してこれらの最大値に向かって移動するだけです。

{id="eq_vgcc_dm" title="VGCC M ゲート更新"}
$$
M(t) = M(t-1) + \frac{1}{3.6} \left( M_{max}(V) - M(t-1) \right)
$$

{id="eq_vgcc_dh" title="VGCC H ゲート更新"}
$$
H(t) = H(t-1) + \frac{1}{29} \left( H_{max}(V) - H(t-1) \right)
$$

時間の経過に伴う最終的なコンダクタンスは、結合部位の活性化と不活化を 3 対 1 の比率で反映します。

{id="eq_vgcc_gt" title="VGCC L コンダクタンスの経時変化"}
$$
g_{vgcc}(t) = g_{vgcc}(V) M^3(t) H(t)
$$

静的電圧ゲート シグモイド関数を確認するには、[[#plot_vgcc:GV run]] を実行します。離散スパイク入力に対する M および H チャネルの応答を確認するには、[[#plot_vgcc:Time run]] を実行します。どちらの場合も、より狭い範囲の値を表示できるようにするには、変数の選択を解除する必要があります。 M 活性化チャネルは、3.6 ミリ秒の時定数と一致して、あらゆる活動電位で急速に上昇し、すぐに下降することが観察されるはずです。対照的に、H 不活化因子は時間の経過とともに蓄積し、全体のコンダクタンス値をゆっくりと減少させます。

## A型K

{id="plot_ak" title="A タイプ K チャネル" Collapsed="true"}
「ゴール」
pl := &chanplots.AKPlot{}
ルート、_ := tensorfs.NewDir("ルート")
br := egui.NewGUIBody(b, pl, root, "AK", "A タイプ K チャネル", "A タイプ K チャネル方程式")
pl.Config(root, br.Tabs)
br.FinalizeGUI(false)
br.Splits.Styler(func(s *styles.Style) {
	s.Min.Y.Em(25)
})
pl.GVRun()
「」

A タイプ K チャネルは電圧ゲート型で、最大活性化は約 -37 mV ([[@HoffmanMageeColbertEtAl97]]) です。これは、暴走興奮性電流を駆動する可能性がある VGCC L 型チャネル (共局在している) の興奮性効果を中和するために特に重要です。これは「緊急ブレーキ」と考えてください。このため、VGCC をモデルに追加するときは常に必要になります。

これには、M (V ゲートの開き) と H (V ゲートの閉じ) という 2 つの状態変数があり、それぞれ高速時定数と低速時定数を統合します。 H は、持続的な活動パターンの不活性化の漸近レベルに比較的早く到達するため、最小限の結果で実際に無視できます。また、高速ホジキン-ハクスリー スパイク チャネルを実装していないため、より高速な時間ダイナミクスの一部を単純化することもできます。したがって、シミュレーションでは、より複雑な関数の立ち上がり部分に適合するパラメーターを使用して、M アクティブ化コンポーネントに単一のシグモイド関数を使用するだけです。

{id="eq_ak_m" title="AタイプMの活性化"}
$$
M = \frac{0.076}{1 + e^{0.075(V + 2)}}
$$

この関数には、-37 mV ピークを超える減少値が欠落していますが、スパイクのダイナミクスと積分の 1 ms タイム ステップを考慮すると、これは関係ありません。この単純化されたコンダクタンスと、[[@^HoffmanMageeColbertEtAl97]] および [[@^MiglioreHoffmanMageeEtAl99]] の完全なモデルとの比較は、[[#plot_ak:GV run]] プロットで確認できます。 [[#plot_ak:Time run]] プロットで時間のダイナミクスを確認することもできます。

## 適応チャネル

さまざまな時間スケールにわたって、さまざまな活動信号に応答して、ニューロンの [[adaptation]] 効果 (_調節_ または _神経疲労_ とも呼ばれます) を引き起こすさまざまなチャネルが多数あります。これらのチャネルは、ニューロンの活動状態に応じて、時間の経過とともにその応答性を低下させます。その結果、進行中の活動パターンに対する反応が全体的に抑制され、新しいパターンに対する反応が相対的に強化されます (つまり、_新規フィルター_)。これらのチャネルはすべて、リーク チャネルと同様に $K^+$ イオンを伝導し、それらのコンダクタンスを合計して全体の `Gk(t)` 値となります。

機能的には、これらは「過分極後 (AHP)」チャネルとしても知られています。これは、高速 (fAHP; 2 ～ 5 ミリ秒)、中程度 (mAHP; 50 ～ 100 ミリ秒)、低速 (sAHP; 0.1 ～ 2 秒) までのさまざまな時間枠で、ニューロンがさらなる興奮性入力に対して不応性 (反応性が低下) になるためです。

生物学的には、非常に多様な K チャネルがあり、通常 4 つの異なる α (アルファ) サブユニットから構成されており、その中には電位依存性 (Kv)、内向き整流子 (Kir)、カルシウム (KCa)、およびナトリウム (KNa) タイプがあります。 [[@^BendaMalerLongtin10]] は、ホジキン・ハクスリー活動電位スパイク自体を駆動する Na チャネルに基づく別の適応メカニズムに関連して、これらの異なるタイプのいくつかの詳細な計算比較を提供します。彼らは、K ベースの適応チャネルとスパイク閾値適応の間に重要な定性的な違いを発見しました。

### M タイプ チャネル

ウシガエルの交感神経節細胞におけるムスカリン性アセチルコリン (ACh) 応答により、歴史的に「M 型」と呼ばれるさまざまな K チャネルが多数存在します。これらは現在、Kv7 KCNQ チャネルとして分類されており、広範囲の異なる神経伝達物質やその他の因子に反応することが脳全体で確認されています ([[@GreeneHoshi17]])。 1 つのよく特徴付けられた M 型チャネルが mAHP K 電流に大きく寄与しており、以下で説明するように Axon で使用します。電圧に敏感ですが、低電圧 (-60 mV) で開き始め、さまざまな神経伝達物質やその他の要因によって閉じる可能性があります。一般に、アクティブ化には時間がかかり、その時定数は約 50 ミリ秒程度で、非アクティブ化も同じタイムスケールで行われます。

機能的には、これらの M 型チャネルに結合する神経伝達物質は、通常、チャネルをオンではなくオフにし、本質的に本質的に調節的または乗算的な脱抑制効果を生み出します。余分な K リーク コンダクタンスを除去しても、ニューロンは直接活性化されませんが、他の入力に対する反応性が高まり、適応効果の影響を受けにくくなります。

### maHP

{id="plot_mahp" title="mAHP M タイプ チャネル" Collapsed="true"}
「ゴール」
pl := &chanplots.MahpPlot{}
ルート、_ := tensorfs.NewDir("ルート")
br := egui.NewGUIBody(b, pl, root, "mAHP", "mAHP チャネル", "mAHP M 型方程式")
pl.Config(root, br.Tabs)
br.FinalizeGUI(false)
br.Splits.Styler(func(s *styles.Style) {
	s.Min.Y.Em(25)
})
pl.GVRun()
「」

スパイクからの $Na^+$ 流入に応答する、以下に説明する KNA チャネルと比較して、M 型 mAHP チャネルの広範囲に調整された電圧感度は、スパイクの前により強力な「予測」コンダクタンスを生成します。したがって、KNa チャネルとは異なる方法で、初期のスパイクを「ヘッドオフ」します。

ほとんどのモデルにおける M タイプ電流の元の特性評価は、[[@^MainenSejnowski96]] によって NEURON に実装されている [[@^GutfreundYaromSegev95]] から派生しています。このコードの広範な使用については、ModelDB エントリの [2488](https://modeldb.science/2488?tab=2&file=cells/km.mod)、[[@CutsuridisPoirazi15]] からの [181967](https://modeldb.science/181967?tab=2&file=CutsuridisPoirazi2015/km.mod)、および [ICジェネロジー](https://icg.neurotheory.ox.ac.uk/viewer/?family=1&channel=1706) を参照してください。

漸近的な駆動値 ($N_{\infty}$) と時間依存の時定数 $\tau$ を持つ電圧ゲート係数 _N_ (他のチャネルでは _M_ とラベル付けされることが多い) があり、どちらも -30 mV を中心とし、9 mV の傾きを持つ電位 V の 2 つのシグモイド関数から構成されます。

{id="eq_mahp_ab" title="mAHP 関数"}
$$
V_o = V + 30
$$

$$
A = \frac{V_o}{\tau_{max} \left(1 - e^{-V_o/9} \right)}
$$

$$
B = \frac{-V_o}{\tau_{max} \left(1 - e^{V_o/9} \right)}
$$

$$
N_{\infty} = \frac{A}{A + B}
$$

$$
\tau = \frac{1}{A + B}
$$

{id="eq_mahp_dn" title="mAHP N アップデート"}
$$
N(t) = N(t-1) + \frac{1}{\tau} \left( N_{\infty} - N(t-1) \right)
$$

$$
g_{mahp} = \overline{g}_{mahp} 2.3^{(37-23)/10} N(t)
$$

これらの関数は [[#plot_mahp:GV run]] で、時間経過のダイナミクスは [[#plot_mahp:Time run]] で確認できます。

### sAHP

{id="plot_sahp" title="sAHP M タイプ チャネル" Collapsed="true"}
「ゴール」
pl := &chanplots.SahpPlot{}
ルート、_ := tensorfs.NewDir("ルート")
br := egui.NewGUIBody(b, pl, root, "sAHP", "sAHP チャネル", "sAHP M タイプ方程式")
pl.Config(root, br.Tabs)
br.FinalizeGUI(false)
br.Splits.Styler(func(s *styles.Style) {
	s.Min.Y.Em(25)
})
pl.GCaRun()
「」

海馬や他のニューロンで観察されている、ゆっくりと長く続く sAHP 電流 ([[@Larsson13]]) の起源を特定することは困難です。これは、より長い時定数を持つカルシウムセンサー経路によって駆動される、M 型チャネル上のさらに別のモジュレーターであると考えられます。ここではさらに研究する必要がありますが、K+ チャネルを活性化する前に構築するのに長い時間がかかり、その後減衰するのにも長い時間がかかるメカニズムを安全に使用できます。

上記の方程式 ([[#eq_mahp_ab]]) は sAHP に使用され、オフセット 0.8 および傾き 0.02 で正規化された統合 Ca 値によって駆動されます。標準の 1 ミリ秒のタイム ステップで更新される mAHP とは異なり、sAHP はシータ サイクル間隔 (200 ミリ秒ごと) で更新され、時間ダイナミクスが自動的に拡張されます。 [[#plot_sahp:G ca run]] および [[#plot_sahp:Time run]] は関数を示します。

### KNa

適応のもう 1 つの源は、ナトリウム (Na) ゲート カリウム (K) 電流のファミリー、_KNa_ です。ニューロンがスパイクして Na の流入を促進すると、K チャネルが活性化されます。 AMPA チャネルからのシナプス Na もこのようなチャネルを活性化する可能性がありますが、さまざまな考察により、これらのチャネルは体細胞の軸索丘の周囲に局在しており、主にスパイクによって生成された Na ([[@Sanchez-VivesNowakMcCormick00a]]; [[@WangLiuHaditschEtAl03]]) に応答することが示唆されています。したがって、上記の電位依存性 mAHP M 型チャネルとは対照的に、これらの KNa チャネルは閾値を超えるスパイクに応答するため、予測的というよりも活性に対して「反応性」が高くなります。 _Slick_ (中)、_Slack_ (低速) など、複数の異なる時定数が特定されています ([[@Kaczmarek13]]; [[@Kohn07]]; [[@Sanchez-VivesNowakMcCormick00a]]; [[@WangLiuHaditschEtAl03]]; [[@BendaMalerLongtin10]])。

スパイクの離散的な性質と更新の 1 ミリ秒の時間スケールにより、スパイクの関数として単純化された指数更新ダイナミックを使用できます。
「行く」
	スパイクの場合{
		gKNa += 1/上昇 * (最大 - gKNa)
	} それ以外の場合は {
		gKNa -= 1/減衰 * gKNa
	}
「」

### SKCa

{id="plot_skca" title="SKCa チャネル" Collapsed="true"}
「ゴール」
pl := &chanplots.SKCaPlot{}
ルート、_ := tensorfs.NewDir("ルート")
br := egui.NewGUIBody(b, pl, root, "SKCa", "SKCa チャネル", "SKCa 方程式")
pl.Config(root, br.Tabs)
br.FinalizeGUI(false)
br.Splits.Styler(func(s *styles.Style) {
	s.Min.Y.Em(25)
})
pl.GCaRun()
「」

Ca 依存性 K チャネルには、「小さい」 K (SK、SKCa) と「大きい」 K (BK、BKCa) の 2 つの主要なタイプがあります。 BK チャネルは、高速ダイナミクスを備えた高いコンダクタンスであり、活動電位の形成に役割を果たします。したがって、AdEx 近似と 1 ms タイム ステップを使用するため、活動電位は無視されます ([モデルDB](https://modeldb.science/modellist/243504) によると、これらは生物物理学モデルには広く実装されていません)。

SK チャネルはデフォルトではオンになっていませんが、視床下核のモデル ([[STN]]) にとって重要です。このモデルは、最初のバースト発火後に活動の明確な休止パターンを示し、SKCa がこれに寄与しています ([[@HallworthWilsonBevan03]])。 SKCaは、発火の最初のバースト中に放出される細胞内Ca貯蔵によって活性化され、その後の追加のKコンダクタンスによって誘発される発火の一時停止により、これらのCaが再緩衝され、それによってSKCa電流が非活性化されます。

私たちの実装は [[@^FujitaFukaiKitano12]] に基づいており、さらに [[@^GunayEdgertonJaeger08]] に基づいており、次の形式をとる単純なヒル方程式を使用しています。

{eq="eq_hill" title="ヒル方程式"}
$$
Y = \frac{X}{X + C_{50}} = \frac{\frac{X}{C_{50}}}{1 + \frac{X}{C_{50}}}
$$

ここで、$C_{50}$ は、値が 50% となる濃度です。このヒル方程式は、複数の要素が同じ場所および状態にあるという要件を反映してさまざまな力率に引き上げられ、さまざまな化学プロセスをモデル化するために使用でき、上記で使用したさまざまな方程式を導出するために舞台裏で使用されます。視床下核 (STN) 細胞のモデルの [[@^GilliesWillshaw06]] では、別のシグモイド指数方程式が与えられました。 [[@^AdelmanMaylieSah12]] および [[@^DwivediBhalla21]] は、SKCa に対して 5 ～ 15 ミリ秒の活性化時定数と約 30 ミリ秒の減衰定数を与えます。

いつものように、正規化された細胞内 Ca 濃度係数 $[Ca]_i$ に作用する、漸近ヒル方程式によって支配される M 活性化係数を使用します。

{eq="eq_skca_m" title="SKCa M 活性化因子"}
$$
M_{\infty} = \frac{([Ca]_i / C_{50})^4}{1 + ([Ca]_i / C_{50})^4}
$$

$M_{\infty}$ が現在の M アクティベーション値より大きい場合、M は 15 ms の立ち上がり時定数で増加し、それ以外の場合は 30 ms の時定数で減衰します。プロットについては、[[#plot_skca:G ca run]] および [[#plot_skca:Time run]] を参照してください。




</section>

</article>
</main>
