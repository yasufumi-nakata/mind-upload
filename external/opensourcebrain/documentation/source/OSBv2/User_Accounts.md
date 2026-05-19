---
layout: default
title: "OpenSourceBrain Documentation: User_Accounts"
description: "OpenSourceBrain/Documentation: source/OSBv2/User_Accounts.md の日本語訳"
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
<p>原典: <a href="https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv2/User_Accounts.md" target="_blank" rel="noopener noreferrer">https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv2/User_Accounts.md</a></p>
<p>ライセンス: CC BY 4.0。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
<a id="osbv2:useraccounts"></a>
<a id="user-accounts-on-osbv2"></a>
OSBv2 のユーザー アカウント数

[アプリケーション](/external/opensourcebrain/documentation/source/OSBv2/Applications.html#osbv2:applications): [NWB エクスプローラー](/external/opensourcebrain/documentation/source/OSBv2/NWBE.html#osbv2:applications:nwbe)、[NetPyNE](/external/opensourcebrain/documentation/source/OSBv2/NetPyNE.html#osbv2:applications:netpyne)、または [ジュピターラボ](/external/opensourcebrain/documentation/source/OSBv2/JupyterLab.html#osbv2:applications:jupyterlab) のいずれかで [ワークスペース](/external/opensourcebrain/documentation/source/OSBv2/Workspaces.html#osbv2:workspaces) を開くには、ユーザーは OSBv2 に登録してログインする必要があります。

<a id="osbv2:useraccounts:register"></a>
<a id="registration"></a>
## 登録

<div class="note-box" markdown="1">
<strong>OSBv2 には OSBv1</strong> とは異なるユーザー データベースがあります

現在、[OSBv1](/external/opensourcebrain/documentation/source/OSBv1/Getting_Started.html#v1:getting_started) のユーザー データベースと OSBv2 の間に重複はありません。 OSBv2 を使用するには、新しいユーザー アカウントを作成する必要があります。
</div>

OSBv2 ユーザー アカウント [ここをクリック](https://www.v2.opensourcebrain.org/register) に登録するには。


<a id="osbv2:useraccounts:signin"></a>
<a id="signing-in"></a>
## サインイン

登録が完了すると、ユーザーはホームページの右上にあるリンクをクリックするか、[ここをクリックしてください](https://www.v2.opensourcebrain.org/login) によってサインインできます。


<a id="osbv2:useraccounts:storage"></a>
<a id="user-data-storage-inside-a-workspace"></a>
## ワークスペース内のユーザー データ ストレージ

<div class="note-box" markdown="1">
<strong>ユーザー ストレージに関する警告</strong>

注: OSB プロジェクトの存続期間中、すべてのデータを安全に保存およびバックアップするよう努めますが (プラットフォーム上でも作業を行っています!) **現時点ではいかなる保証も提供していません**。そのため、ユーザーには貴重な研究データを定期的にバックアップすることをお勧めします。
</div>

[ワークスペース](/external/opensourcebrain/documentation/source/OSBv2/Workspaces.html#osbv2:workspaces) を開いたときにデータを保存できる場所はいくつかあります。

|場所 |説明 |永続性 |
|:---|:---|:---|
| `/opt/user` |このユーザーが **開いているすべてのワークスペース** でアクセスできるプライベート ボリューム |永続的<sup>*</sup> |
| `/opt/workspace` | **このワークスペース**が開かれるたびにアクセスできるボリューム (ワークスペースが共有されて別のユーザーによって開かれている場合でも、この場合は読み取り専用になります)。永続的<sup>*</sup> |
| `/opt/workspace/my-shared` |上記の `/opt/user` へのリンク ([ジュピターラボ](/external/opensourcebrain/documentation/source/OSBv2/JupyterLab.html#osbv2:applications:jupyterlab) のファイル メニューに表示されるようにここに追加)永続的<sup>*</sup> |
| `/opt/home` |ワークスペースの使用中に使用するローカル ストレージ |一時的<sup>^</sup> |
| `/opt/conda` | Python パッケージの場所 (プレインストールされたものとこのセッション中にインストールされたもの)。注: これはワークスペースが再ロードされるたびに更新されるため、セッションごとに新しいパッケージをインストールする必要があります。一時的<sup>^</sup> |

<sup>*</sup> ユーザー ストレージに関する上記の警告を参照してください。

<sup>^</sup> 注: ワークスペースが閉じられ、その後すぐに同じアプリケーションで開かれた場合、同じ Kubernetes ポッドが同じ一時ストレージとともに使用される可能性があり、その結果、`/opt/home` および `/opt/conda` 上のデータがこれらのセッション間で永続化される可能性があります。

これらの場所を参照する最も簡単な方法は、[ジュピターラボ](/external/opensourcebrain/documentation/source/OSBv2/JupyterLab.html#osbv2:applications:jupyterlab) アプリケーションを開くことです (他のファイルは [アップロードしたり、既存のファイルをダウンロードしたりできます](/external/opensourcebrain/documentation/source/OSBv2/Workspaces.html#osbv2:workspaces:addingmore))。


<a id="osbv2:useraccounts:quotas"></a>
<a id="user-quotas"></a>
## ユーザー割り当て

現在、新規ユーザーが作成できるワークスペースの数は限られており、並行して実行できるアプリケーションの数には制限があります。

現在のクォータを表示するには、ログイン時に右上にあるユーザー名をクリックし、[**マイ アカウント**] を選択します。 **実行中のワークスペースの管理** へのリンクをクリックするか、[ここ](https://notebooks.v2.opensourcebrain.org/hub/home) をクリックすると、現在実行中のワークスペースを表示し、停止/削除できます。

<div class="note-box" markdown="1">
<strong>さらにリソースが必要ですか?</strong>

OSBv2 インフラストラクチャのテストを支援したいユーザーやグループに追加のリソースを喜んで提供します。さらに詳しく話し合うには、要件を [連絡を取る](/external/opensourcebrain/documentation/source/General/Contacts.html#contact) に記入してください。
</div>
</section>

</article>
</main>
