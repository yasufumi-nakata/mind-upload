---
layout: default
title: "compcogneuro/web: neuron-equilibrium-potential"
description: "compcogneuro/web: neuron-equilibrium-potential.md の日本語訳"
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
<p>原典: <a href="https://github.com/compcogneuro/web/blob/main/content/neuron-equilibrium-potential.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/web/blob/main/content/neuron-equilibrium-potential.md</a></p>
<p>ライセンス: Text: CC BY 4.0; code: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
+++
Categories = ["Activation", "Neuroscience"]
bibfile = "ccnlab.json"
+++
検出プロセスの最終ステップ (出力の生成) を完了する前に、**平衡膜電位** の概念を使用する必要があります。これは、*興奮性入力コンダクタンスと抑制性入力コンダクタンスの固定セットを仮定した場合*、ニューロンが安定してそこに留まる $V_m$ の値です (これらが安定していない場合、$V_m$ は変化に応じて常に変化する可能性があります)。この平衡値は、ニューロン内の綱引きプロセスが実際に最終的にどのようにバランスをとるかをより明確に示すため、興味深いものです。また、これが数学的に役立つことも次のセクションで説明します。

平衡膜電位 ($V_m^{eq}$) を計算するには、重要な数学的手法を使用できます。つまり、膜電位の変化 (上記の反復 $V_m$ 更新式に従って) を 0 に設定し、この条件下で $V_m$ の値の方程式を解きます。言い換えれば、平衡状態が何であるかを知りたい場合は、$V_m$ が変化しなくなる (つまり、変化率が 0 になる) ために必要な数値を計算するだけです。これを行う数学的手順は次のとおりです。

{id="eq_vm_updt" title="Vm アップデート"}
$$
V_m(t) = V_m(t-1) + dt_{vm} \left[ g_e (E_e-V_m) + g_i (E_i-V_m) + g_l (E_l-V_m) \right]
$$

これは変化を引き起こす部分です (平衡を求めているため時定数は省略しています)。

{id="eq_delta_vm" title="デルタ Vm"}
$$
\デルタ V_m = g_e \left(E_e-V_m\right) + g_i (E_i-V_m) + g_l (E_l-V_m)
$$

変化が止まった時点を見つけるためにこれをゼロに設定します。

$$
0 = g_e \left(E_e-V_m\right) + g_i (E_i-V_m) + g_l (E_l-V_m)
$$

次に、代数を実行して $V_m$ を解決します。

{id="eq_vm_eq" title="平衡 Vm"}
$$
V_m = \frac{g_e}{g_e + g_i + g_l} E_e + \frac{g_i}{g_e + g_i + g_l} E_i + \frac{g_l}{g_e + g_i + g_l} E_l
$$

詳細な計算は、以下の [[#Derivation]] に示されています。

言い換えれば、これは、興奮性ドライブ $E_e$ が、すべてのコンダクタンスの合計 ($g_e + g_i + g_l$) に対する興奮性コンダクタンス $g_e$ の割合の関数として、全体の $V_m$ に寄与していることを示しています。他のそれぞれについても同様です (阻害、漏れ)。これはまさに綱引きの図から予想されることです。$g_l$ を無視すると、$V_m$ の「フラグ」は、$g_e$ と $g_i$ の間の相対的なバランスの関数として配置されます --- それらが等しい場合、$g_e / (g_e + g_i)$ は .5 になります (たとえば、各 g について --- 1/2 = .5)、これは、$V_m$ フラグが $E_i$ と $E_e$ の中間にあることを意味します。

つまり、この計算はすべて、私たちがすでに直感的に知っていたことを再発見するためだけに行われたのです。 (実際、これが数学を行うための最良の方法です。適切な絵を描けば、すべての代数を行う前に答えがわかるはずです)。しかし、この計算が次に役立つことがわかります。

以下は、コンダクタンス項が「g-bar」定数と時間変化する「g(t)」部分に明示的に分割されたバージョンです。

{id="eq_vm_eq" title="Equilibrium Vm フル"}
$$
V_m = \frac{\overline{g}_e g_e(t)}{\overline{g}_e g_e(t) + \overline{g}_i g_i(t) + \overline{g}_l} E_e \frac{\overline{g}_i g_i(t)}{\overline{g}_e g_e(t) + \overline{g}_i g_i(t) + \overline{g}_l} E_i + \frac{\overline{g}_l}{\overline{g}_e g_e(t) + \overline{g}_i g_i(t) + \overline{g}_l} E_l
$$

数学が本当に好きな人にとって、平衡膜電位方程式は [[neuron bayesian|Bayesian optimal detector]] として示すことができます。

## 導出

これは、更新方程式から平衡膜電位を導出するすべての代数を示しています。PDF バージョンでのみ表示されます。

反復 Vm 更新式:

$$
V_m(t) = V_m(t-1) + dt_{vm} \left[ g_e (E_e-V_m) + g_i (E_i-V_m) + g_l (E_l-V_m) \right] $$

変更部分だけ:

$$
\デルタ Vm = g_e \left(E_e-V_m\right) + g_i (E_i-V_m) + g_l (E_l-V_m)
$$

それをゼロに設定します。

$$
0 = g_e \left(E_e-V_m\right) + g_i (E_i-V_m) + g_l (E_l-V_m)
$$

Vm を解く: (すべての g を乗算します)

$$
0 = g_e E_e - g_e V_m + g_i E_i - g_i V_m + g_l E_l - g_l V_m
$$

Vm を解く: (反対側の Vm 項を収集)

$$
g_e V_m + g_i V_m + g_l V_m = g_e E_e + g_i E_i + g_l E_l
$$

Vm を解きます: (Vm ガイを 1 つだけ取得し、各辺を g で割って取得します。)

$$
V_m (g_e + g_i + g_l ) = g_e E_e + g_i E_i + g_l E_l
$$

解決！

$$
V_m = \frac{g_e E_e + g_i E_i + g_l E_l}{g_e + g_i + g_l}
$$

このソリューションを別の方法で記述すると、その意味がもう少し明確になります。

$$
V_m = \frac{g_e}{g_e + g_i + g_l} E_e + \frac{g_i}{g_e + g_i + g_l} E_i + \frac{g_l}{g_e + g_i + g_l} E_l
$$

適応指数関数には、膜更新方程式に入る適応係数 $\omega$ (ギリシャ語オメガ) があり、これを平衡計算に含めることができます。

反復 Vm 更新式:

$$
V_m(t) = V_m(t-1) + dt_{vm} \left[ g_e (E_e-V_m) + g_i (E_i-V_m) + g_l (E_l-V_m) - \omega \right]
$$

変更部分だけ:

$$
\Delta Vm = g_e \left(E_e-V_m\right) + g_i (E_i-V_m) + g_l (E_l-V_m) - \omega
$$

それをゼロに設定します。

$$
0 = g_e \left(E_e-V_m\right) + g_i (E_i-V_m) + g_l (E_l-V_m) - \omega
$$

Vm を解く: (すべての g を乗算します)

$$
0 = g_e E_e - g_e V_m + g_i E_i - g_i V_m + g_l E_l - g_l V_m - \omega
$$

Vm を解く: (反対側の Vm 項を収集)

$$
g_e V_m + g_i V_m + g_l V_m = g_e E_e + g_i E_i + g_l E_l - \omega
$$

Vm を解きます: (Vm ガイを 1 つだけ取得し、各辺を g で割って取得します。)

$$
V_m (g_e + g_i + g_l ) = g_e E_e + g_i E_i + g_l E_l - \omega
$$

解決：

$$
V_m = \frac{g_e E_e + g_i E_i + g_l E_l - \omega}{g_e + g_i + g_l}
$$

$g_e^{\Theta}$ の方程式の導出は次のとおりです。

閾値における平衡 Vm:

$$
\Theta = \frac{g_e^{\Theta} E_e + g_i E_i + g_l E_l}{g_e^{\Theta} + g_i + g_l}
$$

g_e を解く：

$$
\シータ (g_e^{\シータ} + g_i + g_l) = g_e^{\シータ} E_e + g_i E_i + g_l E_l
$$

(両辺に g を掛けます)、g_e を求めます。

$$
\Theta g_e^{\Theta} = g_e^{\Theta} E_e + g_i E_i + g_l E_l - \Theta g_i - \Theta g_l
$$

(非 g_e を反対側に戻して)、g_e を解きます。

$$
g_e^{\Theta} \Theta - g_e^{\Theta} E_e = g_i (E_i - \Theta) + g_l (E_l - \Theta)
$$

(他の g_e を持ってきて反対側を統合し、次に両側を分割して g_e を分離して取得します)、解決策:

$$
g_e^{\Theta} = \frac{g_i (E_i - \Theta) + g_l (E_l - \Theta)}{\Theta - E_e}
$$

AdEx 関数には、膜更新方程式に入る適応係数 $\omega$ (ギリシャ語のオメガ) があり、上記のように平衡計算に含めることができます。

閾値における平衡 Vm:

$$
\Theta = \frac{g_e^{\Theta} E_e + g_i E_i + g_l E_l - \omega}{g_e^{\Theta} + g_i + g_l}
$$

g_e を解く：

$$
\シータ (g_e^{\シータ} + g_i + g_l) = g_e^{\シータ} E_e + g_i E_i + g_l E_l - \omega
$$

(両辺に g を掛けます)、g_e を求めます。

$$
\Theta g_e^{\Theta} = g_e^{\Theta} E_e + g_i E_i + g_l E_l - \Theta g_i - \Theta g_l - \omega$$

(非 g_e を反対側に戻して)、g_e を解きます。

$$
g_e^{\Theta} \Theta - g_e^{\Theta} E_e = g_i (E_i - \Theta) + g_l (E_l - \Theta) - \omega
$$

(他の g_e を持ってきて反対側を統合し、次に両側を分割して g_e を分離して取得します)、解決策:

$$
g_e^{\Theta} = \frac{g_i (E_i - \Theta) + g_l (E_l - \Theta) - \omega}{\Theta - E_e}
$$


</section>

</article>
</main>
