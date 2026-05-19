---
layout: default
title: "OpenSourceBrain Documentation: NWBE"
description: "OpenSourceBrain/Documentation: source/OSBv2/NWBE.md の日本語訳"
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
<p>原典: <a href="https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv2/NWBE.md" target="_blank" rel="noopener noreferrer">https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv2/NWBE.md</a></p>
<p>ライセンス: CC BY 4.0。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
<a id="osbv2:applications:nwbe"></a>
<a id="nwb-explorer"></a>
#NWBエクスプローラー

NWB Explorer は、科学者が NWB:N 2 ファイルの内容を読み取り、視覚化し、探索するために使用できる Web アプリケーションです。

![OSBv2 の NWB エクスプローラー](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/nwbe.png)

*NWB Explorer のインスタンスは OSBv2 でホストされています。*

複数の NWB ファイルを視覚化し、ノートブックを作成してファイルに含まれるデータを分析し、作業内容を保存/共有できるようにするには、OSBv2 で [応用](/external/opensourcebrain/documentation/source/OSBv2/Applications.html#osbv2:applications) として NWB エクスプローラーを開くことができます。これを行うには登録/ログインする必要があります。

<a id="quick-access-to-nwb-explorer"></a>
## NWB Explorer へのクイック アクセス

NWBE は OSBv2 に統合されており、NWB ファイルを含む [ワークスペース](/external/opensourcebrain/documentation/source/OSBv2/Workspaces.html#osbv2:workspaces) を開くための [応用](/external/opensourcebrain/documentation/source/OSBv2/Applications.html#osbv2:applications) として使用できますが、このアプリケーションの **スタンドアロン バージョン** には (ログインせずに) http://nwbexplorer.opensourcebrain.org. でアクセスできます。

これには、多数のサンプル NWB ファイルへのリンクが含まれており、公的にアクセス可能な NWB ファイルへの URL を入力して、その内容を視覚化できます。

![NWB Explorerへのメインインターフェイス](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/NWBE_home.png)

*サンプル ファイルと、外部でホストされている NWB ファイルへの URL を貼り付けるオプションを備えた NWB エクスプローラーへのメイン インターフェイス。*


<a id="osbv2:applications:nwbe:links"></a>
<a id="constructing-direct-links-urls-to-open-nwb-files-in-nwbe"></a>
## NWBE で NWB ファイルを開くための直接リンク (URL) の構築

ドキュメントで使用するために、NWBE で NWB ファイルを開くための直接リンク (URL) を構築することができます。
URL の形式は次のとおりです。

{% raw %}
```
http://nwbexplorer.opensourcebrain.org/nwbfile=<path to file>
```
{% endraw %}


<a id="osbv2:applications:nwbe:links:github"></a>
<a id="file-hosted-on-github"></a>
### GitHub でホストされているファイル

たとえば、GitHub でホストされているファイルの場合、これは次のようになります。

{% raw %}
```
http://nwbexplorer.opensourcebrain.org/nwbfile=https://github.com/openworm/WormsenseLab_ASH/raw/main/test_data/07-06-25-1.nwb
```
{% endraw %}

NWBE がファイルをダウンロードできるように、ファイルの URL は「生」の URL である必要があることに注意してください。

これを使用したバッジの例: <a href="http://nwbexplorer.opensourcebrain.org/nwbfile=https://github.com/openworm/WormsenseLab_ASH/raw/main/test_data/07-06-25-1.nwb">![静的バッジ](https://img.shields.io/badge/NWB-Open_in_OSB-orange)</a>


<a id="osbv2:applications:nwbe:links:dandi"></a>
<a id="file-hosted-on-dandi"></a>
### DANDI でホストされているファイル

DANDI でホストされている NWB ファイルの場合、「ダウンロード」ボタンを右クリックして取得したファイルへの直接 URL を使用できます。例:

{% raw %}
```
http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/0acc0d47-a8c6-4971-8130-32b0b331c838/download/
```
{% endraw %}
これを使用したバッジの例: <a href="http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/0acc0d47-a8c6-4971-8130-32b0b331c838/download/">![静的バッジ](https://img.shields.io/badge/NWB-Open_in_OSB-orange)</a>

<a id="osbv2:applications:nwbe:links:figshare"></a>
<a id="file-hosted-on-figshare"></a>
### Figshare でホストされているファイル

Figshare でホストされている NWB ファイルの場合、「ダウンロード」ボタンを右クリックして取得したファイルへの直接 URL を使用できます。例:
{% raw %}
```
http://nwbexplorer.opensourcebrain.org/nwbfile=https://figshare.com/ndownloader/files/34273955
```
{% endraw %}
これを使用したバッジの例: <a href="http://nwbexplorer.opensourcebrain.org/nwbfile=https://figshare.com/ndownloader/files/34273955">![静的バッジ](https://img.shields.io/badge/NWB-Open_in_OSB-orange)</a>


</section>

</article>
</main>
