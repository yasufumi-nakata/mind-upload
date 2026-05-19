---
layout: default
title: "compcogneuro/web: boltzmann-machine"
description: "compcogneuro/web: boltzmann-machine.md の日本語訳"
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
<p>原典: <a href="https://github.com/compcogneuro/web/blob/main/content/boltzmann-machine.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/web/blob/main/content/boltzmann-machine.md</a></p>
<p>ライセンス: Text: CC BY 4.0; code: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
+++
Categories = ["Learning", "Computation"]
bibfile = "ccnlab.json"
+++
**ボルツマン マシン** (BM) は、1980 年代の先駆的なニューラル ネットワーク学習アルゴリズムであり、初めて [[temporal derivative]] を使用して [[error driven learning]] ([[@AckleyHintonSejnowski85]]; [[@HintonSejnowski86]]) を実行しました。これは、ボルツマン方程式という統計物理学のフレームワークから導出され、相互作用する要素の集合に対する全体的な「エネルギー関数」を定義します。これらの要素は通常、統計物理学では原子であり、この定式化ではニューロンです。このフレームワークは **ホップフィールド ネットワーク** ([[@Hopfield82]]; [[@Hopfield84]]) に非常に似ています。

BM での学習は、**プラス フェーズ**と**マイナス フェーズ**で計算された統計の差の関数です。プラス フェーズは「正しい答え」が存在するネットワークの状態ですが、マイナス フェーズには入力パターンのみがあり、ネットワークは正しい答えを生成しようとします。 BM は完全に双方向に接続されたネットワークに基づいているため、ニューロンの任意のサブセットを使用して入力パターンを表すことができ、他のサブセットは目的の出力パターンを表すことができます。したがって、BM は [[temporal derivative]] 学習フレームワークの汎用性と堅牢性をうまく捉えています。

ただし、実際には、BM は 2 つのフェーズのそれぞれで長期間の統計サンプリングを必要とし、複数の異なる隠れ層 (**ディープ ネットワーク**) を追加する場合にはあまり学習しません。実際、誤差曲面全体の **極小値** に陥る可能性が非常に高くなります。

これらの制限は、[[Axon]] フレームワークで、プールされた [[inhibition]] (フェーズ間の差に応答するためにニューロンを感知範囲内に維持する) やスパース表現、フィードバック接続とフィードフォワード接続の差分重み強度の使用など、さまざまな方法で克服されています。 [[GeneRec]] および [[kinase algorithm]] 学習メカニズムは、もともと BM で開発されたプラス フェーズとマイナス フェーズの基本原理に基づいて構築されています。

## 対照ヘビアン学習 (CHL)

BM の学習ルールの具体的な形式は、**対照ヘビアン学習 (CHL)** 方程式 ([[@MovellanMcClelland93]]) です。

{id="eq_chl" title="対照的ヘブ学習 (CHL)"}
$$
\デルタ w = \left(x^+ y^+\right) - \left(x^- y^-\right)
$$

ここで、最初の項は結果 (_プラス フェーズ_) 中の送信ユニットと受信ユニットのアクティビティであり、第 2 項は予測中 (_マイナス フェーズ_) のアクティビティです。 CHL は、[[Hebbian learning#Hebbian]] に似た 2 つの用語の対比または相違に関係するため、このように名付けられました。

[[GeneRec]] アルゴリズム ([[@OReilly96]]) は、他のいくつかの仮定とともに、これと同じ CHL 方程式を [[error backpropagation]] から直接導出します。


</section>

</article>
</main>
