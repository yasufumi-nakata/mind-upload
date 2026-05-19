---
layout: default
title: "OpenSourceBrain Documentation: OSBv2 のガイド付きツアー"
description: "OpenSourceBrain/Documentation: source/OSBv2/Guided_tour.md の日本語訳"
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
<p>原典: <a href="https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv2/Guided_tour.md" target="_blank" rel="noopener noreferrer">https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv2/Guided_tour.md</a></p>
<p>ライセンス: CC BY 4.0。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
<a id="osbv2:guidedtour"></a>
<a id="guided-tour-of-osbv2"></a>
# OSBv2 のガイド付きツアー

このガイドでは、[OSBv2 ショーケース リポジトリ](https://www.v2.opensourcebrain.org/repositories/38) の内容を使用して、OSBv2 プラットフォームの主な機能を簡単に説明します。

<table>
<tr>
<td style="padding: 10px"><a href="#create-a-new-workspace"><img src="https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/GT1.png" height=170 title="ワークスペースを作成する"/></a>&nbsp;&nbsp;</td>
<td style="padding: 10px"><a href="#explore-nwb-datasets"><img src="https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/GT20.png" height=170 title="NWB エクスプローラー"/></a></td>
</tr>
<tr>
<td style="padding: 10px"><p align="centre"><a href="#create-a-network-simulation-using-netpyne"><img src="https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/GT34.png" height=180 title="NetPyNE"/></a></p></td>
<td style="padding: 10px"><p align="centre"><a href="#open-notebooks-in-jupyterlab"><img src="https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/GT41a.png" height=180 title="ジュピターラボ"/></a></p></td>
</tr>
</table>

<a id="osbv2:guidedtour:register"></a>
<a id="1-register-sign-in-to-osbv2"></a>
<a id="register-sign-in-to-osbv2"></a>
## 1) OSBv2 に登録してサインインする

以下で説明するワークスペースを作成して開くには、OSBv2 アカウントが必要です (OSBv1 のユーザー名/パスワードは機能しません)。無料の OSBv2 ユーザー アカウントに登録するには、[ここ](https://www.v2.opensourcebrain.org/register) または [OSBv2に向かう](https://v2.opensourcebrain.org) をクリックし、右上隅にある [サインイン] をクリックします。

![ガイド付きツアー...](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/GT0.png)

*OSBv2 に登録*

OSBv2 ユーザー アカウント (ファイル ストレージ、クォータなど) の詳細については、[ここ](/external/opensourcebrain/documentation/source/OSBv2/User_Accounts.html#osbv2:useraccounts) を参照してください。


<a id="osbv2:guidedtour:createworkspace"></a>
<a id="2-create-a-new-workspace"></a>
<a id="create-a-new-workspace"></a>
## 2) 新しいワークスペースを作成する

ここで、OSBv2 [アプリケーション](/external/opensourcebrain/documentation/source/OSBv2/Applications.html#osbv2:applications) で表示および分析できるファイルを保持する [ワークスペース](/external/opensourcebrain/documentation/source/OSBv2/Workspaces.html#osbv2:workspaces) を作成します。

このワークスペースは、OSBv2 でサポートされる多数のファイル タイプを含む [リポジトリ](/external/opensourcebrain/documentation/source/OSBv2/Repositories.html#osbv2:repositories)、**OSBv2 ショーケース** のコピーになります。

このリポジトリの現在の内容を確認するには、https://www.v2.opensourcebrain.org/repositories/38 のリポジトリ ページに移動します。

![ガイド付きツアー...](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/GT1.png)

*[OSBv2 ショーケース](https://www.v2.opensourcebrain.org/repositories/38) リポジトリから新しいワークスペースを作成します*

ご覧のとおり、GitHub 上のファイルのソースへのリンク、https://github.com/OpenSourceBrain/OSBv2_Showcase. があります。GitHub への追加/変更は、OSB リポジトリ ページのビューに反映されます。

新しいワークスペースを作成するには、青いボタン「**CREATE NEW WORKSPACE**」をクリックします。表示されるダイアログでは、ワークスペースに関連付けるタイトルやタグなどを設定して、見つけやすくします。

![ガイド付きツアー...](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/GT2.png)

*ワークスペース作成ダイアログ*

作成後、**ワークスペースに移動**するオプションが表示されます。ここに移動すると、ワークスペースのビューが表示され、右上隅に続行方法に関する多くのオプションが表示されます。

![ガイド付きツアー...](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/GT3.png)

*ワークスペースを開くためのオプションは右上隅にあります*

<a id="osbv2:guidedtour:nwbe"></a>
<a id="3-explore-nwb-datasets"></a>
<a id="explore-nwb-datasets"></a>
## 3) NWB データセットを探索する

ドロップダウン メニューで **NWB Explorer で開く** を選択し、青いボタンをクリックします。 [NWB エクスプローラー](/external/opensourcebrain/documentation/source/OSBv2/NWBE.html#osbv2:applications:nwbe) インターフェイスが開きます。

![ガイド付きツアー...](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/GT20.png)

*NWB Explorer のメイン インターフェイス。左側の **リソース パネル** (NWB ファイルのリストなど) は、パネルの下部にある矢印 (**>**、**<**) で開閉できることに注意してください。
左側の列には、既知のタイプのファイル (NWB ファイル、Python ノートブックなど) がリストされています。この列で **LanoreEtAl2019.nwb** を選択すると、その NWB ファイルが NWB Explorer インターフェイスにロードされます。

この [データセット](https://www.biorxiv.org/content/10.1101/567172v1) には、小脳からのゴルジ細胞の電気生理学的記録が含まれています。以下の左側の列には、NWB ファイルのメタデータから抽出されたデータ セットに関する一般情報が表示されます。この研究では、さまざまな条件下でのスパイク挙動を調べた: 1) 薬物ノルエピネフリンの適用前、2) 薬物の適用後、3) 脳スライスから薬物を洗い流した後。右上のパネル **取得** は、これらの条件下で取得されたデータ、膜電位トレースを示します。右上のテキスト ボックスに *Prior* と入力すると、薬剤を適用する前のトレースのみが選択されます。個々のトレースの 1 つの横にある目 (&#x1F441;) を押すと、そのトレースがプロットされ、下部にある「41 件の一致結果」のアイコンを押すと、これらすべてが 1 つの図にプロットされます。これらのトライアル中に注入された電流の同様のトレースは、**刺激**で見つけることができます。

![ガイド付きツアー...](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/GT21.png)

*Lanore らの NWB Explorer ビュー。 2019 年のデータセット。*

<a id="osbv2:guidedtour:netpyne"></a>
<a id="4-create-a-network-simulation-using-netpyne"></a>
<a id="create-a-network-simulation-using-netpyne"></a>
## 4) NetPyNE を使用してネットワーク シミュレーションを作成する

次に、NetPyNE で同じワークスペースを開きます。これを行うには、ホームページに戻って (左上隅の OSB ロゴをクリックするなど) ワークスペース ページへのリンクを見つけるか、別のアプリケーションで開いているワークスペースから、左側の [リソース] パネルの上部にある 3 つの点 (**...**) をクリックし、[NetPyNE で開く] を選択します。

NetPyNE が開いた後、以下のインターフェイスが表示されるはずです。

![ガイド付きツアー...](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/GT31.png)

*モデルがロード/作成される前の NetPyNE インターフェイス。*

OSBv2 リポジトリには、簡単なネットワークの例が含まれています。これを開くには、メニュー項目 *[ファイル] -> [開く...] を選択し、`/home/jovyan/netpyne/workspace/OSBv2 Showcase/main/NetPyNE/HHTut/HHTut_data.json` にある JSON ファイルを見つけます (または、このパスをダイアログの上部のテキスト フィールドに貼り付けます)。


![ガイド付きツアー...](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/GT32.png)

*JSON ファイルを読み込みます。*

モデルがロードされた後、設定を調べることができます。 **Populations** タブをクリックし、次に **PYR** をクリックすると、これが 20 個のセルの母集団であることがわかります。


![ガイド付きツアー...](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/GT33.png)

*現在の人口を表示します。*

次に、3D で表示してみます (右上の **CREATE NETWORK** をクリック)。下の左側のビューが表示されます。

ネットワークを実行することもできます (右上の **SIMULATE** をクリックします)。記録された膜トレースの 1 つを表示するには、左側の **細胞トレース** のアイコンを押すと、右側のプロットが表示されます。


![ガイド付きツアー...](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/GT34.png)

*モデルの作成とシミュレーション後。*


<a id="osbv2:guidedtour:jupyter"></a>
<a id="5-open-notebooks-in-jupyterlab"></a>
<a id="open-notebooks-in-jupyterlab"></a>
## 5) JupyterLab でノートブックを開く

<a id="5a-nwb-data-loading"></a>
<a id="nwb-data-loading"></a>
### 5a) NWB データのロード

次に、[ジュピターラボ](/external/opensourcebrain/documentation/source/OSBv2/JupyterLab.html#osbv2:applications:jupyterlab) で同じワークスペースを開きます (もう一度 3 つの点 (**...**) をクリックするか、ホームページに移動します)。

以下に示すように、左側には **ファイル ブラウザ** があり、[OSBv2 ショーケース GitHub リポジトリ](https://github.com/OpenSourceBrain/OSBv2_Showcase) からコピーされたすべてのファイルが含まれています。右側には **ランチャー** があり、さまざまなタイプの新しいファイルを作成したり、**ターミナル**を開いてシェル コマンドを入力したりできます。 **+** の付いた大きな青いボタンを押すと、いつでも新しいランチャーを作成できます。


![ガイド付きツアー...](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/GT41.png)

*[ジュピターラボ](/external/opensourcebrain/documentation/source/OSBv2/JupyterLab.html#osbv2:applications:jupyterlab)のメインインターフェイス*

以下の画像は、JupyterLab でサポートされているインターフェイスとファイルの種類の一部を示しています。 4 つのパネルの左上はコマンドとスクリプトを実行するためのコマンド ライン **ターミナル**、右上は **Markdown ファイル** (テキスト エディターで変更することもできます) のプレビュー、左下は **Python スクリプト**、右下は **JSON ファイル**です。また、JupyterLab インターフェイスの軽量バージョンも示しています。メニューからアクセスできます: *設定 -> テーマ -> JupyterLab Light*。



![ガイド付きツアー...](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/GT41a.png)

*[ジュピターラボ](/external/opensourcebrain/documentation/source/OSBv2/JupyterLab.html#osbv2:applications:jupyterlab) (ライト テーマ) のインターフェイス。ターミナルを表示し、Markdown ファイルと JSON ファイル、および Python スクリプトを表示します。*

`OSBv2 Showcase/main/notebooks` に移動し、`LoadNWBData.ipynb` をダブルクリックします。これにより、NWB エクスプローラーで以前に視覚化された NWB ファイル **LanoreEtAl2019.nwb** の内容をプログラムで読み取るために使用されるノートブックが開きます。 [pyNWB](https://pynwb.readthedocs.io/en/stable/) を使用してファイルをロードし、「コントロール」に一致する `nwbfile.acquisition` 内のエントリ、つまり薬物を適用する前の記録を選択し、これらをプロットします。

ノートブックを再実行するには、ノートブック パネルのアイコン バーにある二重矢印 (&#x25B6;&#x25B6;) (**コード** の左側) を押します。

![ガイド付きツアー...](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/GT42.png)

*NWBデータをロードするためのノート*

<a id="5b-netpyne-simulation-results-loading"></a>
<a id="netpyne-simulation-results-loading"></a>
### 5b) NetPyNE シミュレーション結果の読み込み

再度、ディレクトリ `OSBv2 Showcase/main/notebooks` で `LoadNetPyNEData.ipynb` を開きます。これにより、上記の NetPyNE シミュレーションの実行時に生成されたファイル (ディレクトリ `../NetPyNE/HHTut/HHTut_data.json` 内) が検索され、そこから保存された膜電位トレースが抽出されます。

![ガイド付きツアー...](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/GT44.png)

*NetPyNE データをロードするためのノートブック*

<a id="osbv2:guidedtour:simulators"></a>
<a id="6-run-simulator-scripts-in-jupyterlab"></a>
<a id="run-simulator-scripts-in-jupyterlab"></a>
## 6) JupyterLab でシミュレーター スクリプトを実行する

<a id="6a-run-netpyne-scripts"></a>
<a id="run-netpyne-scripts"></a>
### 6a) NetPyNE スクリプトを実行する

次に、ターミナルでいくつかのシミュレーター スクリプトを実行してみます。ランチャー (**+** の付いた大きな青いボタン) からターミナルを開き、`cd` から `/opt/workspace/OSBv2 Showcase/main/NetPyNE/HHTut` を開きます。 `python HHTut_run.py` と入力して、*グラフィカル インターフェイスで実行したのと同じシミュレーション* を実行します。

![ガイド付きツアー...](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/GT61.png)

*ターミナルでの NetPyNE シミュレーションの実行*


<a id="6a-run-brian-eden-scripts"></a>
<a id="run-brian-eden-scripts"></a>
### 6a) Brian、EDEN、... スクリプトを実行します。

OSBv2 にプリインストールされている他のシミュレーター用の多数のスクリプトは、`/opt/workspace/OSBv2 Showcase/main/simulators` にあります。ターミナルのこの場所に移動し、これらを実行してみてください。 `brian2_example.py`。

![ガイド付きツアー...](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/GT63.png)

*ターミナルでの Brian シミュレーションの実行*

含まれている別の例では、Arbor で単純なネットワークを作成する方法を示しています。

![ガイド付きツアー...](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/GT64.png)

*ノートブックで Arbor シミュレーションを実行*
</section>

</article>
</main>
