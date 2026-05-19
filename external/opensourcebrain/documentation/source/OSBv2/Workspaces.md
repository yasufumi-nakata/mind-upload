---
layout: default
title: "OpenSourceBrain Documentation: ワークスペース"
description: "OpenSourceBrain/Documentation: source/OSBv2/Workspaces.md の日本語訳"
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
<p>原典: <a href="https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv2/Workspaces.md" target="_blank" rel="noopener noreferrer">https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv2/Workspaces.md</a></p>
<p>ライセンス: CC BY 4.0。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
<a id="osbv2:workspaces"></a>
<a id="workspaces"></a>
# ワークスペース

ワークスペースは、ユーザーがさまざまな [OSBv2 アプリケーション](/external/opensourcebrain/documentation/source/OSBv2/Applications.html#osbv2:applications) を使用して作業するための永続的なスペースです。
各ワークスペースは [永続的なクラウド ボリューム](/external/opensourcebrain/documentation/source/OSBv2/User_Accounts.html#osbv2:useraccounts:storage) に保存されるため、ユーザーは作業内容を保存して、後で再開できます。
ユーザーは、[リポジトリ](/external/opensourcebrain/documentation/source/OSBv2/Repositories.html#osbv2:repositories) からワークスペースにファイルを追加したり、自分のコンピュータからファイルをアップロードしたりできます。
ワークスペースは、パブリック、プライベート、または特集のいずれかにすることができます。

- **プライベート ワークスペース**は、それを作成したユーザーのみに表示およびアクセスできます
- **パブリック ワークスペース**は全員に表示されますが、作成者のみが変更できます (他のユーザーは読み取り専用モードで開くことができます)
- **注目のワークスペース** は、OSBv2 管理者によって厳選されたパブリック ワークスペースです。

<a id="osbv2:workspaces:existing"></a>
<a id="working-with-existing-workspaces"></a>
## 既存のワークスペースの操作

これらのワークスペースはすべて、OSBv2 ホームページの右側のパネルに表示されます。
ユーザーは適切なタブを選択して、さまざまなタイプのワークスペースを切り替えることができます。

![OSBv2 ホームページにリストされているワークスペースを示す図](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/osbv2-workspaces-homepage-with-text.png)

*ワークスペースは OSBv2 ホームページでご覧いただけます。*

ワークスペースは、[OSBv2 アプリケーション](/external/opensourcebrain/documentation/source/OSBv2/Applications.html#osbv2:applications) のいずれかで開くことができます。
これは、リスト内の各ワークスペースのコンテキスト メニューを使用してホームページから直接行うことも、ワークスペース情報ページから行うこともできます。

![ワークスペース情報ページを示す図](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/osbv2-workspaces-page-with-text.png)

*ワークスペース情報ページには、ワークスペースに含まれるリソースなど、ワークスペースに関する詳細が表示されます。*
ワークスペースにはファイルが含まれており、その一部は **リソース** として識別されます。
リソースは、[OSBv2 アプリケーション](/external/opensourcebrain/documentation/source/OSBv2/Applications.html#osbv2:applications) のいずれかで開くことができると OSBv2 が認識している特別なファイルです。
これらは、ワークスペースとアプリケーションの左側のペインにあるリソース サイド バーに表示されます。

リソースをクリックすると、関連するアプリケーションでリソースが開きます。

- NWB ファイル (*.nwb ファイル) は [NWB エクスプローラー](/external/opensourcebrain/documentation/source/OSBv2/NWBE.html#osbv2:applications:nwbe) で開きます
- Jupyter Notebook (*.ipynb ファイル) [ジュピターラボ](/external/opensourcebrain/documentation/source/OSBv2/JupyterLab.html#osbv2:applications:jupyterlab) を開く
- NetPyNE ファイルは [NetPyNE](/external/opensourcebrain/documentation/source/OSBv2/NetPyNE.html#osbv2:applications:netpyne) ([近日公開...](https://github.com/OpenSourceBrain/OSBv2/issues/304)) で開きます。

<a id="osbv2:workspaces:creating"></a>
<a id="creating-a-new-workspace"></a>
## 新しいワークスペースの作成

OSBv2 でワークスペースを作成するには 2 つの方法があり、どちらも OSBv2 ホームページで利用できます。

![新しいワークスペースを作成するためのホームページ上のオプションを示す図。](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/osbv2-workspaces-homepage-create-with-text.png)

*ワークスペースは、OSBv2 ホームページのオプションを使用して作成できます。*
最初から開始したい場合は、ファイルやリソースを含まない **空白/空のワークスペース** を作成できます (インタラクティブ開発/JupyterLab をクリック)。

あるいは、アクセス権のある [リポジトリ](/external/opensourcebrain/documentation/source/OSBv2/Repositories.html#osbv2:repositories) に含まれるファイルからワークスペースをシードすることもできます。このようなワークスペースは、次の 2 つの方法でリポジトリから作成できます。

- OSBv2 ホームページから [リポジトリからのワークスペース] ボタンを選択します。
- [ここ](/external/opensourcebrain/documentation/source/OSBv2/Repositories.html#osbv2:repositories:viewing) で説明されているように、リポジトリ情報ページから。

メインページの「リポジトリからワークスペース」ボタンをクリックすると、「新しいワークスペースの作成」ダイアログボックスが開きます。
ここで、新しいワークスペースにファイルを含めるのに使用するリポジトリを選択できます。

![新しいワークスペースを作成するためのリポジトリ選択ダイアログ ボックスを示す図。](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/osbv2-workspaces-from-repo-dialog.png)

*リストからリポジトリを選択します。*
これにより、ファイル選択パネルが表示されます。
含めたいファイルを選択し、「続行」をクリックして続行します。

![新しいワークスペースを作成するためのファイル選択ダイアログ ボックスを示す図。](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/osbv2-workspaces-from-repo-file-select-dialog.png)

*ワークスペースに含めるファイルをリストから選択します。*

最後の画面では、ワークスペースを設定できます。
ここで、ワークスペースの名前、タグ、説明、サムネイルを追加できます。

![新しいワークスペースを作成するためのリポジトリ選択ダイアログ ボックスを示す図。](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/osbv2-workspaces-create-dialog.png)

*ワークスペースの名前、タグ、説明、サムネイルを追加します。*


ワークスペースがワークスペースのリストに追加され、使用できるようになります。
デフォルトでは、新しいワークスペースはプライベートです。
各ワークスペースのメニューから「公開」を選択すると公開することができます。


<a id="osbv2:workspaces:addingmore"></a>
<a id="adding-files-to-existing-workspaces"></a>
## 既存のワークスペースへのファイルの追加

<div class="note-box" markdown="1">
<strong>ワークスペース内のユーザー ストレージ</strong>

ワークスペース内の保存されたユーザー ファイルについては、さまざまな場所にある情報 [ここ](/external/opensourcebrain/documentation/source/OSBv2/User_Accounts.html#osbv2:useraccounts:storage) を参照してください。
</div>

既存のワークスペースにさらにファイルを追加することもできます。これを行う簡単な方法の 1 つは、[ジュピターラボ](/external/opensourcebrain/documentation/source/OSBv2/JupyterLab.html#osbv2:applications:jupyterlab) アプリケーションを使用してワークスペースを開き、**ファイルのアップロード アイコン**をクリックすることです。

![JupyterLab からファイルをアップロードします。](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/osbv2-upload.png)

*JupyterLab からファイルをアップロードします。*

JupyterLab ファイル ブラウザでファイルを右クリックして、個々のファイルを**ダウンロード**することもできます。

あるいは、アップロードしたいファイルがリポジトリ内にある場合は、[ここ](/external/opensourcebrain/documentation/source/OSBv2/Repositories.html#osbv2:repositories:viewing) に記載されているようにリポジトリ ページから追加するファイルを選択することも、ワークスペース情報ページに移動してそこからファイルを追加することもできます。

![ワークスペース情報ページの「新しいリソースの追加」ボタンを示す図。](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/osbv2-workspaces-add-new-resources-with-text.png)

*さらに多くのファイル/リソースをワークスペースに追加できます。*

これにより、[新しいリソースの追加] ダイアログ ボックスが表示され、URL または OSBv2 リポジトリからファイルを追加できます。

![「新しいリソースの追加」ダイアログボックスを示す図。](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/osbv2-workspaces-add-new-resources-dialog.png)

*[新しいリソースの追加] ダイアログ ボックスを使用すると、場所またはリポジトリからファイルを追加できます。*

現在、リソース サイド バーを使用してファイル/リソースをダウンロードすることはできません。
</section>

</article>
</main>
