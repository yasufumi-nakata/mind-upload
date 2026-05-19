---
layout: default
title: "OpenSourceBrain Documentation: オープンソース ブレイン v2"
description: "OpenSourceBrain/Documentation: source/OSBv2/Overview.md の日本語訳"
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
<p>原典: <a href="https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv2/Overview.md" target="_blank" rel="noopener noreferrer">https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv2/Overview.md</a></p>
<p>ライセンス: CC BY 4.0。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
<a id="osbv2"></a>
<a id="open-source-brain-v2"></a>
# オープンソース ブレイン v2

<div class="note-box" markdown="1">
<strong>OSBv2 が公開されました!</strong>

OSBv2 の最新リリースは **https://v2.opensourcebrain.org**. で入手できます。質問がある場合、またはユーザー テストを支援したい場合は、[連絡する](/external/opensourcebrain/documentation/source/General/Contacts.html#contact) を実行してください。
</div>

Open Source Brain (OSB) v2 は、[OSBv1](/external/opensourcebrain/documentation/source/OSBv1/Getting_Started.html#v1:getting_started) の機能に基づいて構築された新しい統合研究プラットフォームです。
現在鋭意開発中ですが、ユーザーが研究で使い始めるのに十分安定しています。

OSBv2 は、**リポジトリ**、**ワークスペース**、**アプリケーション**という 3 つの主要な概念を中心に構成されています。

![OSBv2の概要](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/OSBv2Overview.png)

*OSBv2 上のリポジトリ、ワークスペース、アプリケーション間の関係*

<a id="repositories"></a>
<a id="repositories"></a>
## リポジトリ

リポジトリは、[GitHub](/external/opensourcebrain/documentation/source/OSBv2/GitHub.html#osbv2:github)、[フィグシェア](/external/opensourcebrain/documentation/source/OSBv2/Figshare.html#osbv2:figshare)、[DANDIアーカイブ](/external/opensourcebrain/documentation/source/OSBv2/DANDI.html#osbv2:dandi) などの公開リソース内のファイルとデータのセットのビューです。

- OSBv2 のリポジトリ ページには、リモート リソース (GitHub リポジトリ、FigShare プロジェクトなど) の **現在のコンテンツ** がリストされます。
- OSB リポジトリはパブリックです。すべてのユーザーは OSBv2 に追加された [リポジトリを参照する](https://v2.opensourcebrain.org/repositories) を実行できます。
- プライベートリポジトリ、および他の神経情報学リソースへのインターフェースも計画されています

リポジトリの詳細については、[ここ](/external/opensourcebrain/documentation/source/OSBv2/Repositories.html#osbv2:repositories) を参照してください。

<a id="workspaces"></a>
<a id="workspaces"></a>
## ワークスペース

ワークスペースは、ユーザーが作業を実行するための永続的なスペースです。

- 空のワークスペースを作成したり、その時点でリポジトリ内のファイルの一部またはすべてを使用して OSBv2 [リポジトリ](/external/opensourcebrain/documentation/source/OSBv2/Repositories.html#osbv2:repositories) からシードしたりできます。
- 各ワークスペースは [永続的なクラウド ボリューム](/external/opensourcebrain/documentation/source/OSBv2/User_Accounts.html#osbv2:useraccounts:storage) に保存されるため、ユーザーは作業を保存して後で再開できます。
- ワークスペースは任意の [OSBv2アプリケーション](/external/opensourcebrain/documentation/source/OSBv2/Applications.html#osbv2:applications) で開くことができ、生成されたファイル (解析出力、シミュレーション結果など) もワークスペースに保存され、他のファイル [アップロードできます](/external/opensourcebrain/documentation/source/OSBv2/Workspaces.html#osbv2:workspaces:addingmore)
- ユーザーは自分のワークスペースをプライベートのままにすることも、パブリックにしてコミュニティと共有することもできます

ワークスペースの詳細については、[ここ](/external/opensourcebrain/documentation/source/OSBv2/Workspaces.html#osbv2:workspaces) を参照してください。

<a id="applications"></a>
<a id="applications"></a>
## アプリケーション

OSBv2 は研究者が使用できる多数のアプリケーションを統合しており、サポートされている OSBv2 アプリケーションのいずれかでワークスペースを開くことができます。

- [NWB エクスプローラー](/external/opensourcebrain/documentation/source/OSBv2/NWBE.html#osbv2:applications:nwbe): [国境なきニューロデータ](https://nwb.org) ファイルの内容の対話型の探索/視覚化用
- [NetPyNE](/external/opensourcebrain/documentation/source/OSBv2/NetPyNE.html#osbv2:applications:netpyne): 神経科学モデルの構築とシミュレーションのためのグラフィカル ユーザー インターフェイス
- [ジュピターラボ](/external/opensourcebrain/documentation/source/OSBv2/JupyterLab.html#osbv2:applications:jupyterlab): Python プログラミング言語の完全な開発環境

[NWB エクスプローラー](/external/opensourcebrain/documentation/source/OSBv2/NWBE.html#osbv2:applications:nwbe) と [NetPyNE](/external/opensourcebrain/documentation/source/OSBv2/NetPyNE.html#osbv2:applications:netpyne) の両方には、アドホック スクリプト作成と分析用の組み込み Python コンソールも含まれており、便宜上、多数の Python ライブラリが [ジュピターラボ](/external/opensourcebrain/documentation/source/OSBv2/JupyterLab.html#osbv2:applications:jupyterlab) アプリケーションにプリロードされています。

OSBv2 アプリケーションの詳細については、[ここ](/external/opensourcebrain/documentation/source/OSBv2/Applications.html#osbv2:applications) を参照してください。
</section>

</article>
</main>
