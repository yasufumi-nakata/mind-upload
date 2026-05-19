---
layout: default
title: "compcogneuro/sims: ClusterPlot"
description: "compcogneuro/sims: ClusterPlot.md の日本語訳"
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
<p>原典: <a href="https://github.com/compcogneuro/sims/blob/main/ch3/faces/ClusterPlot.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/sims/blob/main/ch3/faces/ClusterPlot.md</a></p>
<p>ライセンス: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
**クラスター プロット**は、階層的にクラスター化された樹形図内の一連のパターン間の類似関係を表示します。多くの場合、これは高次元の類似構造を視覚化する最も便利な方法です。クラスター プロットを生成する方法については、taDataAnal ページを参照してください。

クラスター プロットを作成するアルゴリズムは、最も類似したパターンをグループ化し、次にパターンのグループを高次のクラスターにグループ化する再帰的なプロセスです。これは、最も近いアイテムまたはグループのみをグループ化することに「貪欲」であり、まだグループ化されていないものが何も残らなくなるまで続行されます。

プロットを読むには、ツリー内で最も類似した「葉」が含まれる右側から始めます。共通の垂直バーを共有し、その共通の垂直バーに水平線で接続されているアイテムは、すべて同じレベルの類似性でグループ化されます。多くの場合、これはアイテムのペアですが、複数のアイテム間の類似性が同じレベルである場合は、それらをすべてグループ化できます。 1 レベル左に戻ると、それ自体がクラスター内にグループ化されているグループは、他のそのようなグループ化と比較して、それぞれの項目間で共有される類似性が高くなります。等々..

水平線の長さは、グループ内の項目間の距離を示します。通常、これは *ユークリッド* 距離メトリック (つまり、差の二乗和の平方根) を使用して計算されますが、他にも多くの距離メトリックが利用可能です。

葉に垂直線のみが表示され、水平線セグメントが表示されない場合は、それらのアイテム間の距離がゼロであることを意味します。

切断されたクラスター間のクラスターの水平位置の長さに絶対的な意味はありません。距離は、共有クラスター内の項目についてのみ正確です。


</section>

</article>
</main>
