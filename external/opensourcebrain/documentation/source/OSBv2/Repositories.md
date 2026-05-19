---
layout: default
title: "OpenSourceBrain Documentation: Repositories"
description: "OpenSourceBrain/Documentation: source/OSBv2/Repositories.md の日本語訳"
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
<p>原典: <a href="https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv2/Repositories.md" target="_blank" rel="noopener noreferrer">https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv2/Repositories.md</a></p>
<p>ライセンス: CC BY 4.0。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
<a id="osbv2:repositories"></a>
<a id="repositories"></a>
リポジトリの数

リポジトリは、[GitHub](/external/opensourcebrain/documentation/source/OSBv2/GitHub.html#osbv2:github) や [DANDIアーカイブ](/external/opensourcebrain/documentation/source/OSBv2/DANDI.html#osbv2:dandi) などの公開リソース内のファイルとデータのビューです。
ソースの **現在の内容** が表示されます。
現在、[GitHub](/external/opensourcebrain/documentation/source/OSBv2/GitHub.html#osbv2:github)、[フィグシェア](/external/opensourcebrain/documentation/source/OSBv2/Figshare.html#osbv2:figshare)、および [ダンディ](/external/opensourcebrain/documentation/source/OSBv2/DANDI.html#osbv2:dandi) がサポートされており、さらに多くのソースのサポートも計画されています。

現在、リポジトリは公開されているため、すべてのユーザーが OSBv2 に追加されたリポジトリを参照できます。

<a id="osbv2:repositories:viewing"></a>
<a id="viewing-available-repositories"></a>
## 利用可能なリポジトリの表示

ユーザーは、[リポジトリリスト](https://v2.opensourcebrain.org/repositories) ページで、OSBv2 上に現在作成されているすべてのリポジトリを表示できます。
[リポジトリの表示] ボタンをクリックするか、右上隅の [リポジトリ] ドロップダウンをクリックして、リポジトリ リスト ページを表示します。

![リポジトリリストへのアクセス方法を示す図](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/osbv2-main-page-repositories-link-with-text.png)

*ダッシュボードの [リポジトリ] ボタンをクリックしてすべてのリポジトリを表示するか、[作成] ドロップダウン ボタンを使用して新しいリポジトリを作成します。*

ユーザーはリポジトリを表示するために署名する必要はありません。
ただし、それらを使用するには [サインイン](/external/opensourcebrain/documentation/source/OSBv2/User_Accounts.html#osbv2:useraccounts:signin) する必要があります。 [ワークスペース](/external/opensourcebrain/documentation/source/OSBv2/Workspaces.html#osbv2:workspaces) にそれらからのデータを設定します。

リポジトリ リスト ページにアクセスすると、関心のあるリポジトリを検索/フィルタリングして情報を表示したり、自分のリポジトリを表示したり、リポジトリを新規追加または編集したりできます。

![リポジトリ一覧ページを示す図](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/osbv2-repositories-page-with-text.png)

*リポジトリ リスト ページを使用して、新しいリポジトリを表示、編集、追加できます。*

リポジトリ リスト ページのエントリをクリックすると、リポジトリの詳細ページが開きます。
ここでは、その時点でのリポジトリのプレビューを確認できます。

![リポジトリの詳細ページを示す図](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/osbv2-repository-detail-page-with-text.png)

*ここでリポジトリに関する情報を表示し、ワークスペースに追加するファイルを選択できます。*

右側のファイル セレクターを使用して、既存の [ワークスペース](/external/opensourcebrain/documentation/source/OSBv2/Workspaces.html#osbv2:workspaces) に追加するファイルを選択したり、それらのファイルを使用してまったく新しいワークスペースを作成したりすることもできます。

<a id="osbv2:repositories:adding"></a>
<a id="adding-new-and-editing-repositories"></a>
## 新しいリポジトリの追加と編集

すべてのユーザーは、次の手順に従って OSBv2 にリポジトリを追加できます。

- [OSBv2にログインする](/external/opensourcebrain/documentation/source/OSBv2/User_Accounts.html#osbv2:useraccounts:signin)
- 上に示すように、リポジトリ リスト ページに移動します。
- 「新しいリポジトリを追加」ボタンをクリックします

これにより、[新しいリポジトリの追加] ダイアログ ボックスが表示されます。
ここで、リポジトリを OSBv2 に追加するために必要な情報を入力できます。

![「新しいリポジトリの追加」ダイアログボックス](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/osbv2-add-repository-with-text.png)

*「新しいリポジトリの追加」ダイアログボックスに入力します。*

リポジトリのメタデータは、作成後に変更することもできます。
上に示すように、ポップアップの [編集] オプションをクリックすると、[新しいリポジトリの追加] ダイアログが再度開きます。
</section>

</article>
</main>
