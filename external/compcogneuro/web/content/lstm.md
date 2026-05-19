---
layout: default
title: "compcogneuro/web: lstm"
description: "compcogneuro/web: lstm.md の日本語訳"
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
<p>原典: <a href="https://github.com/compcogneuro/web/blob/main/content/lstm.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/web/blob/main/content/lstm.md</a></p>
<p>ライセンス: Text: CC BY 4.0; code: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
+++
Name = "LSTM"
Categories = ["Computation"]
bibfile = "ccnlab.json"
+++
[[@^HochreiterSchmidhuber97]] の **LSTM** (長短期記憶) モデルは、複数形式の乗算 **ゲーティング**を使用して、[[error backpropagation]] でトレーニングされた [[abstract neural network]] に、特に堅牢かつ柔軟な形式の活性化ベースの作業記憶を実装します。

{id="figure_lstm" style="高さ:10em"}
![定エラー カルーセル (CEC; 対角線のある円) を備えた LSTM メモリ セル (長方形)。メンテナンス ゲート g (左側) は新しい情報を更新およびエンコードするタイミングを乗算的に決定し、出力ゲート (右側) は動作を駆動するためにメモリ セルから情報を読み出すタイミングを決定します。 Hochreiter & Schmidhuber、1997 年、図 1 より。](media/fig_hochreiter_schmidhuber_97_lstm.png)

モデルの動機となった重要な洞察は、神経活動信号の形で情報の痕跡を経時的に堅牢に維持するには、経時的な指数関数的な増加または減衰を回避する正確にバランスのとれた形式の再発性神経活動が必要であるということでした。これは、_定数エラー カルーセル_ (CEC) ([[#figure_lstm]]) と呼ばれていました。

このような堅牢なメンテナンス メカニズムを構築すると、定義上、新しい情報がいつ更新されるか既存の情報が維持されるかを決定する可能性のある内部ダイナミクスがなくなります。そこで、CEC メモリに新しい情報をいつ更新するかを決定する「入力ゲート」と、応答またはその他のプロセスを駆動するためにメモリから情報を読み出す時期を決定する「出力ゲート」を導入しました。

方程式形式では、メモリ状態を更新するための入力ゲートは次のようになります。

{id="eq_in" title="入力ゲーティング"}
$$
s_{c_j}(t) = s_{c_j}(t-1) + g(net_{c_j})(t) y^{in_j}(t)
$$

ここで、$s_{c_j}(t)$ は、タイムステップ $t$ における CEC のアクティビティ状態です。 $g(net_{c_j}(t))$ は、0..1 の範囲の値を生成する非線形のスカッシング アクティベーション関数であり、$y^{in_j}(t)$ は入力ゲート関数 $in_j$ のアクティベーションです。

メモリセルからの出力は次のとおりです。

{id="eq_out" title="出力ゲーティング"}
$$
y^{c_j}(t) = y^{out_j}(t) h(s_{c_j})(t)
$$

ここで、$y^{c_j}(t)$ は各タイムステップでのメモリ セルの出力です。 $y^{out_j}(t)$ は出力ゲートユニット $out_j$ のアクティビティです。 $h(s_{c_j}(t))$ は、CEC の現在の状態値 $s_{c_j}$ の非線形関数です。

他の形式のゲートが [[@^GersSchmidhuberCummins00]] および [[@^SchmidhuberGersEck02]] (クリア ゲートおよびメンテナンス ゲート) で導入されました。

[[PBWM]] (前頭前皮質、大脳基底核ワーキングメモリ) モデル ([[@OReillyFrank06]]) は、[[thalamus]] と [[prefrontal cortex]] の間の興奮性ループに対する [[basal ganglia]] の脱抑制性 (調節的、乗法的) 影響からこれらのゲート機構がどのように生じるかを示しています。


</section>

</article>
</main>
