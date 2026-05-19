---
layout: default
title: "OpenSourceBrain Documentation: モデルを NeuroML 2 に変換する必要があるのはなぜですか?"
description: "OpenSourceBrain/Documentation: source/OSBv1/Converting_To_NeuroML2.md の日本語訳"
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
<p>原典: <a href="https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv1/Converting_To_NeuroML2.md" target="_blank" rel="noopener noreferrer">https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv1/Converting_To_NeuroML2.md</a></p>
<p>ライセンス: CC BY 4.0。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
<a id="v1:convert_nml"></a>
<a id="why-should-you-convert-your-model-to-neuroml-2"></a>
# モデルを NeuroML 2 に変換する必要があるのはなぜですか?

<div class="note-box" markdown="1">
<strong>**注:** 最新情報については、NeuroML ドキュメントを参照してください。</strong>

[NeuroML ドキュメント](https://docs.neuroml.org) は最近徹底的に更新されており、モデルを NeuroML 2 に変換する理由と方法についての主要なガイドとして使用する必要があります。
</div>

モデルをシミュレータに依存しない形式 [ニューロML2](https://docs.neuroml.org/Userdocs/NeuroMLv2.html) に変換すると、モデルを [多くの異なる形式](https://docs.neuroml.org/Userdocs/Software/SupportingTools.html) に変換できるほか、OSB の高度な機能の多くをモデルで使用できるようになります (例: [細胞の3D可視化](http://v1.opensourcebrain.org/projects/l5bpyrcellhayetal2011?explorer=https%3A%2F%2Fraw.github.com%2FOpenSourceBrain%2FL5bPyrCellHayEtAl2011%2Fmaster%2FneuroConstruct%2FgeneratedNeuroML2%2FL5PC.cell.nml) および [ネットワーク](http://v1.opensourcebrain.org/projects/acnet2?explorer=https%3A%2F%2Fraw.github.com%2FOpenSourceBrain%2FACnet2%2Fmaster%2FneuroConstruct%2FgeneratedNeuroML2%2FMediumNet.net.nml)、[チャネル動力学](http://v1.opensourcebrain.org/projects/acnet2?explorer=https%3A%2F%2Fraw.github.com%2FOpenSourceBrain%2FACnet2%2Fmaster%2FneuroConstruct%2FgeneratedNeuroML2%2FNa_pyr.channel.nml) に関する情報の抽出)。

![OSBの機能](https://raw.githubusercontent.com/OpenSourceBrain/OSB_Documentation/master/resources/images/OSBfeatures.jpg)

現時点では、モデルを有効な NeuroML 2 にエクスポートするためにシミュレータで押す「魔法のボタン」はありません。現時点での最良のアプローチは、[NeuroML 2 のコア例](https://github.com/NeuroML/NeuroML2/tree/master/examples) や [NeuroML 2 に変換される OSB プロジェクト](https://github.com/OpenSourceBrain/.github/blob/main/testsheet/README.md) の一部を確認し、そこにある XML サンプルを確認し、これらに基づいてモデルの手動変換を開始することです。

**ステップバイステップのガイドがあります: _コンダクタンスベースの細胞モデルを NeuroML2 に変換_ [ここ](https://docs.neuroml.org/Userdocs/CreatingNeuroMLModels.html#converting-cell-models-to-neuroml-and-sharing-them-on-open-source-brain)!**

このプロセスで使用するツールについては、以下にいくつかの提案があります。

**jNeuroML を使用して NeuroML 2 ファイルを検証/実行/変換/表示します**

[jNeuroML](https://github.com/NeuroML/jNeuroML) は、NeuroML2 ファイルの検証に使用できます。

     jnml -validate MyNeuroML2.nml

これにより、最新の XSD スキーマ ドキュメントに対してファイルが検証されるだけでなく、モデルの構造に関してその他の多くのチェックが実行されます。

LEMS シミュレーション ファイルを作成して、シミュレーションの実行時間、タイムステップ、プロット/保存する内容などを指定すると、モデルを jNeuroML で実行できるようになります。例を参照してください。[ここ](https://github.com/NeuroML/NeuroML2/tree/master/LEMSexamples) とほとんどの [これらの OSB プロジェクト](https://github.com/OpenSourceBrain/redmine/issues/125) にも、少なくとも 1 つの LEMS シミュレーション ファイルがあります。

NeuroML 2 でセルとネットワークをすばやく視覚化するために (neuroConstruct にロードしたり OSB で表示したりするのではなく)、モデルを SVG 形式に変換できます (Web ブラウザーなどで表示するため)。

     jnml MyNeuron.cell.nml -svg
     jnml MyCircuit.net.nml -svg

jNeuroML の最新機能を入手するには、[ここ](https://github.com/NeuroML/jNeuroML/blob/master/README.md) で説明されているように **ソースから最新の開発バージョン**をインストールすることを**強くお勧めします**。

**pyNeuroML を使用して NEURON から NeuroML2 形態をエクスポートします**

[pyNeuroML](https://github.com/NeuroML/pyNeuroML) は、jNeuroML jar ファイルをバンドルし、そのパッケージの機能を使用することで、[jNeuroML](https://github.com/NeuroML/jNeuroML) の多くの機能に Python スクリプトでアクセスできるようにする Python パッケージです。

jNeuroML の機能に加えて、pyNeuroML には、NEURON から NeuroML2 への更新されたエクスポーターなど、多数の Python 固有の機能が追加されています。これは現在、ニューロン形態のエクスポートのみに限定されています ([ここ](https://github.com/NeuroML/pyNeuroML/blob/master/examples/export_neuroml2.py) の例を参照) が、接続性 (およびチャネル、シナプスなどの NeuroML2 でのテンプレートの生成) などの他の機能の抽出が可能になるようにさらに開発される予定です。

この機能は、[3D嗅球モデル](http://v1.opensourcebrain.org/projects/miglioreetal14_olfactorybulb3d) の元の NEURON コードから多数のセル モデルを抽出するために使用されました ([このスクリプト](https://github.com/OpenSourceBrain/MiglioreEtAl14_OlfactoryBulb3D/blob/master/NeuroML2/export_mitral.py) を参照)。

![30セル](https://raw.githubusercontent.com/OpenSourceBrain/MiglioreEtAl14_OlfactoryBulb3D/master/images/30cells.jpg)

**pyNeuroML を使用してチャネルを NeuroML 2 に変換します**

取り組んでいるもう 1 つの機能は、イオン チャネル モデル (NEURON の NMODL 形式など) を NeuroML 2 に変換するのに役立つ一連のスクリプトです。これらのスクリプトは、pyNeuroML がインストールされた後に以下を使用してアクセスできます。

    pynml-channelanalysis NaConductance.channel.nml   # Analyse a NeuroML 2 channel
    pynml-modchananalysis NaConductance               # Analyse a NEURON channel e.g. from NaConductance.mod

これらのスクリプトは、アクティブ化/非アクティブ化変数のトレースを生成するために異なるアプローチを採用していますが、同等のプロットを生成します。

![ピンミリ](https://raw.githubusercontent.com/OpenSourceBrain/OSB_Documentation/master/resources/images/pynml_analyse.png)

左側は NeuroML ファイルから生成されたプロット ([ここ](https://github.com/NeuroML/pyNeuroML/blob/master/examples/analyseNaNml2.sh) を参照)、右側は NMODL バージョンから生成されたプロット ([ここ](https://github.com/NeuroML/pyNeuroML/blob/master/examples/analyseNaMod.sh) を参照) です。

明確にしておきますが、これらのスクリプトは (現時点では) NMODL ファイルから方程式を抽出して NeuroML ファイル内の正しい場所に配置するのには役立ちません。単に 2 チャネル形式の動作を比較して手動変換でのエラーをチェックするのに役立つだけです。


**NeuroConstruct を使用して NeuroML v1/2 への変換を支援します**

OSB 上の多くのプロジェクトは元々、neuroConstruct を使用して元の形式 (NEURON、GENESIS など) から NeuroML v1.8.1 に変換されました (これらのリストについては [ここ](http://www.opensourcebrain.org/search_custom_field?f[]=43&op[43]=~&v[43][]=neuroConstruct) を参照)。そこから、neuroConstruct 内での NeuroML2 への変換は簡単でした。 neoConstruct [ここ](http://www.opensourcebrain.org/docs#Using_neuroConstruct_Based_Projects) の使用方法の詳細と、NeuroML v1 [ここ](http://www.neuroconstruct.org/docs/importneuron.html#Converting+mod+file%2FGENESIS+script+channels+into+ChannelML) へのモデルの変換の詳細。
</section>

</article>
</main>
