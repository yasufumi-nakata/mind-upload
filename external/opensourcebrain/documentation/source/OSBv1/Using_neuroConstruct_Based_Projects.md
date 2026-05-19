---
layout: default
title: "OpenSourceBrain Documentation: neoConstruct ベースのプロジェクトの使用"
description: "OpenSourceBrain/Documentation: source/OSBv1/Using_neuroConstruct_Based_Projects.md の日本語訳"
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
<p>原典: <a href="https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv1/Using_neuroConstruct_Based_Projects.md" target="_blank" rel="noopener noreferrer">https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv1/Using_neuroConstruct_Based_Projects.md</a></p>
<p>ライセンス: CC BY 4.0。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
<a id="v1:using_neuroconstruct"></a>
<a id="using-neuroconstruct-based-projects"></a>
# neoConstruct ベースのプロジェクトの使用

OSB 上の多くのプロジェクトは、以下に基づいています。
[ニューロコンストラクト](http://www.neuroconstruct.org/) プロジェクト (「
[ここ](http://opensourcebrain.org/search_custom_field?f[]=43&op[43]=~&v[43][]=neuroConstruct))。
neoConstruct は、モデル要素を NeuroML にインポートするために使用されます (例:
シミュレーターまたは他のアプリケーション)、複数のシミュレーター用のコードを生成できます。
NeuroML をさまざまな形式でエクスポートできます。

<a id="install-the-latest-version-of-neuroconstruct"></a>
## 最新バージョンの NeuroConstruct をインストールします

まず、neuroConstruct の最新バージョンを入手します。
NeuroConstruct のダウンロード ページでバイナリ インストーラーを入手できますが、**GitHub からこのアプリケーションの最新バージョンを使用する**ことが最善です。これは、OSB 上のプロジェクトが最後に保存されたバージョンである可能性が高いためです。

最新バージョンの Git を入手します (Git の詳細については、[ここ](http://www.opensourcebrain.org/projects/gitintro/wiki/Wiki) を参照してください)。
ソースから NeuroConstruct をインストールする詳細な手順については、[ここ](https://github.com/NeuralEnsemble/neuroConstruct/blob/master/INSTALL.md) を参照してください。

<a id="install-your-simulators-of-choice"></a>
## 選択したシミュレータをインストールします

OSB でサポートされているシミュレーターの詳細については、[ここ](/external/opensourcebrain/documentation/source/OSBv1/Simulators.html#v1:simulators) を参照してください。

<a id="get-a-local-copy-of-one-of-the-neuroconstruct-based-projects"></a>
## NeuroConstruct ベースのプロジェクトの 1 つのローカル コピーを取得します。

いずれかのプロジェクトのローカル コピーをチェックアウトします。プロジェクト:顆粒セル

{% raw %}
```bash
git clone https://github.com/OpenSourceBrain/GranuleCell.git
```
{% endraw %}

インストール手順の説明に従って、neuroConstruct を実行します。

**ファイル**、**プロジェクトを開く…**に移動し、プロジェクトをインストールしたフォルダーに移動して**GranuleCell/neuroConstruct/GranuleCell.ncx**を選択します。
**生成**タブに移動し、**セルの位置と接続を生成**を押します。
[**エクスポート**] タブに移動し、選択したシミュレーター (例: NEURON) のタブに移動し、**[XXX ファイルの作成]** を押してから、[**XXX シミュレーションの実行**] を押します。
これらのシミュレータとneuroConstructの相互作用の詳細については、[ここ](http://www.neuroconstruct.org/docs/interact.html)を参照してください。

<a id="get-all-neuroconstruct-based-projects-on-osb"></a>
## OSB 上のすべての neoConstruct ベースのプロジェクトを取得する

neoConstruct プロジェクト (およびその他の多くのプロジェクト) を含む OSB 上のすべてのプロジェクトのクローンを作成するには、neuroConstruct ホーム ディレクトリの **osb** サブフォルダーにある **checkOSB** スクリプトを使用します。

{% raw %}
```bash
cd osb
./checkOsb.sh -u (Linux/Mac)
checkOsb.bat -u  (Windows)
```
{% endraw %}

これにより、\~70 のプロジェクトと、\~20 の NeuroConstruct プロジェクトが含まれるクローンが作成されます。これらのプロジェクトは、ファイル - オープンソース Brain プロジェクトでアクセスできるようになります。

<!-- TODO: missing image -->

![](http://www.opensourcebrain.org/attachments/download/51/nCmenu.png)
</section>

</article>
</main>
