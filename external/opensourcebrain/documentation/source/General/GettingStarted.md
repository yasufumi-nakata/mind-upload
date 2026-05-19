---
layout: default
title: "OpenSourceBrain Documentation: OSB を始める"
description: "OpenSourceBrain/Documentation: source/General/GettingStarted.md の日本語訳"
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
<p>原典: <a href="https://github.com/OpenSourceBrain/Documentation/blob/main/source/General/GettingStarted.md" target="_blank" rel="noopener noreferrer">https://github.com/OpenSourceBrain/Documentation/blob/main/source/General/GettingStarted.md</a></p>
<p>ライセンス: CC BY 4.0。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
<a id="getting_started_osb"></a>
<a id="getting-started-with-osb"></a>
# OSB を始める

現在、OSB には OSBv1 と現在開発中の新しいバージョンである OSBv2 の 2 つのバージョンがあります。

- **[OSBv1](/external/opensourcebrain/documentation/source/OSBv1/Getting_Started.html#v1:getting_started)** は、さまざまな脳領域および種から [ニューロML2](https://docs.neuroml.org) 形式で標準化されたモデルを共有、表示、分析、およびシミュレーションするための Web プラットフォームです。これは、[グリーソンら。 2019年](https://www.cell.com/neuron/fulltext/S0896-6273(19)30444-1) で詳しく説明されているバージョンです。
- **[OSBv2](/external/opensourcebrain/documentation/source/OSBv2/Overview.html#osbv2)** は、OSBv1 の機能に基づいて構築された新しい統合研究プラットフォームです。
  これは、神経科学者が実験データとデータ駆動型の計算/理論モデリングの間のループを閉じるのを支援することを目的としています。
  以下を統合します。

- [NWB エクスプローラー](/external/opensourcebrain/documentation/source/OSBv2/NWBE.html#osbv2:applications:nwbe) (NWB) 形式のデータの視覚化と分析用
  - 計算モデリングおよびシミュレーション用の [NetPyNE](/external/opensourcebrain/documentation/source/OSBv2/NetPyNE.html#osbv2:applications:netpyne)
  - [ジュピターラボ](/external/opensourcebrain/documentation/source/OSBv2/JupyterLab.html#osbv2:applications:jupyterlab) (一般的な Python ワークフロー用)

強力なクラウドベースの Web アプリケーションで。
  研究者は、OSBv2 上のワークスペースに作業内容を保存し、それを日々の研究に使用できます。

<a id="getting_started_osb:which"></a>
<a id="which-version-of-osb-should-i-use"></a>
## OSB のどのバージョンを使用すればよいですか?

**[OSBv1](/external/opensourcebrain/documentation/source/OSBv1/Getting_Started.html#v1:getting_started)** を使用してください:

- [グリーソンら。 2019年](https://www.cell.com/neuron/fulltext/S0896-6273(19)30444-1) [グリーソン2019](#Gleeson2019) で説明されているモデルを調べたい場合
- Web ブラウザで [ニューロML2](https://docs.neuroml.org) モデルを視覚化、分析、シミュレーションしたい場合

**[OSBv2](/external/opensourcebrain/documentation/source/OSBv2/Overview.html#osbv2)** を使用してください:

- 標準化された [NWB](/external/opensourcebrain/documentation/source/OSBv2/NWBE.html#osbv2:applications:nwbe) 形式で神経科学データを共有、視覚化、分析したい場合
- [NetPyNE](/external/opensourcebrain/documentation/source/OSBv2/NetPyNE.html#osbv2:applications:netpyne) プラットフォームを使用して計算モデルを作成、シミュレーション、共有したい場合
- [Python エコシステム](/external/opensourcebrain/documentation/source/OSBv2/JupyterLab.html#osbv2:applications:jupyterlab) ([ニューロML2](https://docs.neuroml.org) を含む) のパッケージを使用して、一般的な Python ベースのワークフローを作成および共有したい場合

OSBv2 はクラウド ベースのインフラストラクチャを使用するため、提供されたクラウド ストレージ自体に作業とデータを保存し、後で中断したところから続行できます。


OSBv2 は現在鋭意開発中であり、OSBv1 のすべての機能は時間の経過とともに OSBv2 に移行される予定です。
</section>

</article>
</main>
