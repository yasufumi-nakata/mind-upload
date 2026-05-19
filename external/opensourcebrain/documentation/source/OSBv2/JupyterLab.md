---
layout: default
title: "OpenSourceBrain Documentation: JupyterLab"
description: "OpenSourceBrain/Documentation: source/OSBv2/JupyterLab.md の日本語訳"
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
<p>原典: <a href="https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv2/JupyterLab.md" target="_blank" rel="noopener noreferrer">https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv2/JupyterLab.md</a></p>
<p>ライセンス: CC BY 4.0。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
<a id="osbv2:applications:jupyterlab"></a>
<a id="jupyterlab"></a>
#ジュピターラボ

OSBv2 は、[ジュピターラボ](https://jupyterlab.readthedocs.io/en/latest/user/index.html) インスタンスを [アプリケーション](/external/opensourcebrain/documentation/source/OSBv2/Applications.html#osbv2:applications) の 1 つとしてホストします。当社の JupyterLab アプリケーションは、主に Python で対話型の探索的コンピューティングのための Web インターフェイスを提供し、多数の神経科学モデリングおよびデータ分析パッケージがプリインストールされています。

![OSBv2 上の JupyterLab](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/jlab.png)

*JupyterLab のインスタンスは OSBv2 でホストされています。*

OSBv2 上の JupyterLab アプリケーションで [ワークスペース](/external/opensourcebrain/documentation/source/OSBv2/Workspaces.html#osbv2:workspaces) (もともと [NWB エクスプローラー](/external/opensourcebrain/documentation/source/OSBv2/NWBE.html#osbv2:applications:nwbe) または [NetPyNE](/external/opensourcebrain/documentation/source/OSBv2/NetPyNE.html#osbv2:applications:netpyne) 用に作成された可能性があります) を開くには、サインインする必要があります。

<a id="osbv2:applications:jupyterlab:features"></a>
<a id="features"></a>
## 特徴

<a id="file-management"></a>
### ファイル管理
JupyterLab アプリケーションの重要な機能は、[ワークスペースストレージ](/external/opensourcebrain/documentation/source/OSBv2/User_Accounts.html#osbv2:useraccounts:storage) と [ファイルをアップロードしたり、既存のファイルをダウンロードしたりできます](/external/opensourcebrain/documentation/source/OSBv2/Workspaces.html#osbv2:workspaces:addingmore) を表示できるファイル ブラウザです。

<a id="osbv2:applications:jupyterlab:configuration"></a>
<a id="configuration"></a>
## 構成

JupyterLab 環境ではどのような Python パッケージが利用できますか?現在のパッケージのセットを確認するには、ターミナルで `pip list` を試してください。

これらは、JupyterLab アプリケーションの Dockerfile ([マスターバージョン](https://github.com/OpenSourceBrain/OSBv2/blob/master/applications/jupyterlab/Dockerfile)、[最新の開発バージョン](https://github.com/OpenSourceBrain/OSBv2/blob/develop/applications/jupyterlab/Dockerfile)) で設定されます。ここにパッケージを追加したい場合は、[問題を開く](https://github.com/OpenSourceBrain/OSBv2/issues) または Dockerfile のプル リクエストを送信してください。
</section>

</article>
</main>
