---
layout: default
title: "OpenSourceBrain Documentation: シミュレーター"
description: "OpenSourceBrain/Documentation: source/OSBv1/Simulators.md の日本語訳"
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
<p>原典: <a href="https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv1/Simulators.md" target="_blank" rel="noopener noreferrer">https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv1/Simulators.md</a></p>
<p>ライセンス: CC BY 4.0。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
<a id="v1:simulators"></a>
<a id="simulators"></a>
# シミュレーター

OSB のモデルの主なターゲット シミュレーターの概要

**注意: すべてのシミュレータがすべてのモデルを実行できるわけではありません。** OSB の各モデルでサポートされているシミュレータの詳細については、[ここ](https://v1.opensourcebrain.org/status) を参照してください。

OSB 上のモデルの NeuroML 要素を処理できるその他のツール (モデルの視覚化、分析など) については、[ここ](https://docs.neuroml.org/Userdocs/Software/SupportingTools.html) を参照してください。

<a id="brian"></a>
## ブライアン

Brian は [ここ](http://briansimulator.org) からダウンロードできます。 OSB には [ブライアン・ショーケース](http://www.opensourcebrain.org/projects/brianshowcase) プロジェクトがあります。

NeuroML のモデルを Brian との間で変換するためのネイティブ サポートの強化は、[NeuroML v2.0](http:///www.neuroml.org/neuroml2) で開発中です。 [ここ](https://github.com/NeuroML/org.neuroml.export/blob/development/src/main/java/org/neuroml/export/brian/BrianWriter.java) を参照してください。

Brian は現在、NeuroML モデルの [ぴんん](http://neuralensemble.org/trac/PyNN) への変換によってもサポートされています。 [ここ](http://www.neuroml.org/pynn) を参照してください。

<a id="genesis-2"></a>
## ジェネシス 2

GENESIS 2 は [ここ](http://genesis-sim.org/project/genesis) からダウンロードできます。

GENESIS 2 で NeuroML モデルを実行するためのサポートは、主に [ニューロコンストラクト](http://www.opensourcebrain.org/docs#Using_neuroConstruct_Based_Projects) によるスクリプトの生成によって有効になりますが、[ここ](http://www.neuroml.org/tool_support.php#GENESIS) も参照してください。

<a id="genesis-3neurospaces"></a>
## ジェネシス 3/ニューロスペース

GENESIS 3/ニューロスペースは [ここ](http://neurospaces.sourceforge.net) で入手可能です。

GENESIS 3 は現在、NeuroML 形式 (形態学 + パッシブ パラメーター) でのパッシブ モデルのネイティブ読み取りをサポートしています。

最近の [GENESIS 3 を使用した計算神経科学におけるマルチスケール モデリングに関するワークショップ](http://www.gradschool.uni-luebeck.de/index.php?id=377) の参加者は、neuroConstruct が生成した GENESIS 2 スクリプトを GENESIS 3 上で実行することに成功したと報告しました。

<a id="moose"></a>
## ムース

MOOSE は [ここ](http://moose.sourceforge.net) で入手可能です。

MOOSE における NeuroML (バージョン 1 および 2) のネイティブ サポートは現在開発中ですが、[ニューロコンストラクト](http://www.opensourcebrain.org/docs#Using_neuroConstruct_Based_Projects) を使用して NeuroML モデルから MOOSE コードを生成することもできます。

MOOSE [ここ](http://moose.svn.sourceforge.net/viewvc/moose/moose) の最新の開発状況をフォローしてください。

[モーグリ](http://moose.ncbs.res.in/moogli/) は MOOSE の姉妹プロジェクトであり、ニューラル シミュレーション用のシミュレーターに依存しない OpenGL ベースの視覚化ツールです。

<a id="neuron"></a>
## ニューロン

NEURON は [ここ](http://www.neuron.yale.edu/neuron) で入手可能です。 OSB には [NEURONショーケース](http://www.opensourcebrain.org/projects/neuronshowcase) プロジェクトがあります。

NEURON では NeuroML セルの読み取り/書き込みがネイティブでサポートされています。[ここ](http://www.neuroml.org/neuron_tools.php) を参照してください。

[ニューロコンストラクト](http://www.opensourcebrain.org/docs#Using_neuroConstruct_Based_Projects) を使用して、NeuroML モデルから NEURON コード (Parallel NEURON を含む) を生成することもできます。

<a id="nest"></a>
## 巣

NEST は [ここ](http://www.nest-initiative.org) からダウンロードできます。

NEST は現在、NeuroML モデルを [ぴんん](http://neuralensemble.org/trac/PyNN) に変換することでサポートされています。 [ここ](http://www.neuroml.org/pynn) を参照してください。

NEST のネイティブ サポートの強化は [NeuroML v2.0](http:///www.neuroml.org/neuroml2) で計画されています ([ここ](https://github.com/NeuroML/org.neuroml.export/blob/development/src/main/java/org/neuroml/export/nest/NestWriter.java) を参照)。

<a id="psics"></a>
## PSICS

PSICS は [ここ](http://www.psics.org) で利用可能です。

PSICS には NeuroML 用の [ネイティブサポート](http://www.psics.org/neuroml/index.html) がありますが、[ニューロコンストラクト](http://www.opensourcebrain.org/docs#Using_neuroConstruct_Based_Projects) を使用して NeuroML モデルから PSICS コードを生成することもできます。
</section>

</article>
</main>
