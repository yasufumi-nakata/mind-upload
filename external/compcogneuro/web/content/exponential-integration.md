---
layout: default
title: "compcogneuro/web: exponential-integration"
description: "compcogneuro/web: exponential-integration.md の日本語訳"
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
<p>原典: <a href="https://github.com/compcogneuro/web/blob/main/content/exponential-integration.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/web/blob/main/content/exponential-integration.md</a></p>
<p>ライセンス: Text: CC BY 4.0; code: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
+++
Categories = ["Computation"]
bibfile = "ccnlab.json"
+++
{id="sim_tau" title="タウ指数積分時定数" Collapsed="true"}
「ゴール」
tau := 10.0 // 時定数
ドライブ:= 50.0
初期化:= 0.0
val := 初期化
var tauStr、driveStr、initStr、valAtTauStr 文字列

##
合計時間 := 100
driver := zeros(totalTime) // ドライバーは値を駆動するものです
vals := zeros(totalTime) // 値
exps := zeros(totalTime) // 指数関数の値
##

関数 valUpdate() {
    tauStr = fmt.Sprintf("タウ: %g", タウ)
    driveStr = fmt.Sprintf("ドライバー: %g", ドライブ)
    initStr = fmt.Sprintf("初期化: %g", init)
    ##
    d := array(drive) // 現在のドライブ
    iv := 配列(初期化)
    dv := d - iv
    v := array(init) // 現在の
    タウ := 配列(タウ)
    ##
    for t := 範囲 100 {
        ##
        テレビ := 配列(t)
        ドライバー[t] = d
        vals[t] = v
        v += (1.0 / ttau) * (d - v) // v は d に向かって移動します
        exps[t] = iv + dv * (1 - exp(-tv / ttau))
        ##
    }
    色合い := int(タウ)
    tval := vals.Float(int)
    dist := ドライブ - 初期化
    pdist := 100.0
    if dist != 0 {
        pdist = 100 * (tval-init) / dist
    }
    valAtTauStr = fmt.Sprintf("<b>タウの値 (%d) = %7.3g = %7.3g %% ドライブまでの道のり、%7.3g %% go</b> まで残り", tiny, tval, pdist, 100 - pdist)
}

valUpdate()

プロットスタイル := func(s *plot.Style) {
    s.Range.SetMax(100).SetMin(0)
    s.Plot.XAxis.Label = "時間"
    s.Plot.XAxis.Range.SetMax(100).SetMin(0)
	s.Plot.Legend.Position.Left = true
}
プロット.SetStyler(ドライバー, プロットスタイラー)

fig1, pw := lab.NewPlotWidget(b)
dl := プロット.NewLine(fig1, ドライバー)
vl := プロット.NewLine(fig1, vals)
el := プロット.NewLine(fig1, exps)
fig1.Legend.Add("ドライバー", dl)
fig1.Legend.Add("値", vl)
fig1.Legend.Add("Exp", el)

valAtTauTx := core.NewText(b)
valAtTauTx.Styler(func(s *styles.Style) {
    s.Min.X.Ch(80) // 可変幅コンテンツによるクリーンなレンダリング
})
core.Bind(&valAtTauStr, valAtTauTx)

関数 updt() {
    valUpdate()
    dl.SetData(ドライバー)
    vl.SetData(vals)
    el.SetData(exps)
    valAtTauTx.UpdateRender()
    pw.NeedsRender()
}

func addSlider(label *string, val *float64, mxVal float32) {
    tx := core.NewText(b)
    tx.Styler(func(s *styles.Style) {
        s.Min.X.Ch(40) // 可変幅コンテンツによるクリーンなレンダリング
    })
    core.Bind(ラベル、tx)
	sld := core.NewSlider(b).SetMin(1).SetMax(mxVal).SetStep(1).SetEnforceStep(true)
	sld.SendChangeOnInput()
	sld.OnChange(func(e events.Event) {
		updt()
		tx.UpdateRender()
	})
	core.Bind(val, sld)
}

addSlider(&tauStr, &tau, 50)
addSlider(&initStr, &init, 100)
addSlider(&driveStr, &drive, 100)
「」

[[#sim_tau]] は、**時定数** `tau` ($\tau$) によって制御されるオンライン **指数積分**のプロセスを示しています。ここで、指定された値は各タイム ステップで更新され、「駆動」値に向かって一定の割合が移動します。この割合は $\frac{1}{\tau}$ です。

{id="eq_tau" title="指数積分"}
$$
v(t+1) = v(t) + \frac{1}{\tau} (d - v(t))
$$

このタイプの方程式は、[[Axon]] のほぼあらゆる場所で使用されており、[[neuron]] のモデルを駆動する核となる方程式である、電位に対する電流の影響に関するオームの法則を含む、さまざまなタイプの物理プロセスの基本的な結果です。

化学反応も同様の関数に従い、化学反応の速度を表すタウ因子によって支配されます。たとえば、2 つの最初の「成分」_A_、_B_ は、_順速度定数 $K_f$ による化学反応によって _化合物_ _AB_ に結合できます。

{id="eq_chem" title="順化学反応"}
$$
A + B \; {K_f \atop \rightarrow} AB
$$

反応が進行するにつれて、利用できる原材料が少なくなるため、利用可能な原材料の量に応じて反応速度が自然に遅くなり、結果として [[#eq_tau]] と同じ動きになります。

## タウの値

[[#eq_tau]] でさまざまな `Tau`、`Init`、および `Driver` 値を試してみるとわかるように、更新の Tau タイム ステップ後には、ドライバーまでの距離が常に約 64% になります。これは、任意のタイム ステップで値を直接計算できる指数関数から直接計算できます ([[#sim_tau]] の `Exp` としてプロットされます)。

{id="eq_exp" title="指数関数"}
$$
v(t) = v(0) + (d - v(0)) \left(1 - e^{-t/\tau} \right)
$$

ここで、$v(0)$ は、タイム ステップ 0 での `Init` 初期値です。これを 0 に設定し、$t=\tau$ で評価すると、次のようになります。

{id="eq_exp-tau" title="t = タウの値"}
$$
v(\tau) = d \left(1 - e^{-1} \right) \約 1 - 1/2.72 \約 0.632..
$$

報告される値に小さな差異があるのは、離散時間間隔で更新方程式 ([[#eq_tau]]) を反復する場合と、(微積分などによる) 指数関数によって計算される完全に連続的な更新による数値の違いによるものです。

最も簡単に言うと、$\tau$ は、駆動値までのおよそ 2/3 に到達するのにかかる時間と考えることができます。

＃＃ 人生の半分

おそらく聞いたことがあるもう 1 つの値は、指数関数的過程 (放射性崩壊もこれと同じ関数に従います) の「半減期」です。これは、値が駆動値までの 50% に達するときです。これは、$t = ln(2) \tau$ またはおおよそ $t = 0.7 \tau$ のときに発生します。$v(t) = \frac{1}{2}d$ を設定して _t_ を解くとわかります。

{id="eq_hl-tau" title="半減期"}
$$
\frac{1}{2} d = d \left(1 - e^{-t/\tau} \right)
$$

$$
\left(1 - e^{-t/\tau} \right) = \frac{1}{2}
$$

両側の自然対数を取る：

$$
\frac{-t}{\tau} = ln(1) - ln(2)
$$

$$
t = ln(2) \tau
$$

詳細については、この [ウィキペディアのページ](https://en.wikipedia.org/wiki/Time_constant) を参照してください。
</section>

</article>
</main>
