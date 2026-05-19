---
layout: default
title: "OpenSourceBrain Documentation: OSBv1 に関するチュートリアルの作成"
description: "OpenSourceBrain/Documentation: source/OSBv1/Creating_Tutorials.md の日本語訳"
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
<p>原典: <a href="https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv1/Creating_Tutorials.md" target="_blank" rel="noopener noreferrer">https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv1/Creating_Tutorials.md</a></p>
<p>ライセンス: CC BY 4.0。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
<a id="v1:tutorials"></a>
<a id="creating-tutorials-on-osbv1"></a>
# OSBv1 に関するチュートリアルの作成

ユーザーには、OSB プロジェクトを新しいチュートリアルに変えることをお勧めします。

チュートリアル リポジトリの例は [ここ](https://github.com/mattearnshaw/tutorials) にあります。以下でこの例を参照します。

まず、チュートリアルに使用するモデルを開きます。チュートリアルを構築するには、デフォルト セッションの構成とメインのステップバイステップ ガイドの作成という 2 つの主要なコンポーネントがあります。

<a id="configuring-the-default-session"></a>
## デフォルトセッションの構成

ウィジェットを開いたり、人口の再着色、ズームやモデルの位置など、プロジェクトの状態に加えた変更はすべて保存して、チュートリアルのデフォルトの作業環境として再利用できます。
たとえば、[Blue Brain Project ショーケースセッション](http://opensourcebrain.org/projects/blue-brain-project-showcase/models?explorer=https%3A%2F%2Fraw.githubusercontent.com%2FOpenSourceBrain%2FBlueBrainProjectShowcase%2Fsample%2FosbSessions%2Fsample%2FSample_Session.json) を見てください。すぐに、モデルの説明、チュートリアル、情報ボックスという 3 つのポップアップ ウィジェットが表示されます。これは、元のプロジェクトでこれらのウィンドウを作成するだけで実現できます (つまり、[モデルの説明] をクリックし、コンソールを使用して [ポップアップウィジェットを追加する](http://docs.geppetto.org/en/latest/usingwidgets.html) を実行し、右上のツールバーの ![](https://raw.githubusercontent.com/OpenSourceBrain/OSB_Documentation/master/resources/images/download-project-button.png) ボタンを使用してプロジェクトをダウンロードします)。

project.zip ファイルには、xmi ファイル、json ファイル、js ファイル、および実行した実験の結果が含まれています。 zip の内容を [リポジトリのサブディレクトリ](https://github.com/OpenSourceBrain/BlueBrainProjectShowcase/tree/sample/osbSessions/sample) に配置します。その後、OSB 上のプロジェクトのモデル ページに json ファイルへのリンクが表示されます。

![](https://raw.githubusercontent.com/OpenSourceBrain/OSB_Documentation/master/resources/images/curated.png)

ステップバイステップのチュートリアル コンポーネントを含める場合は、デフォルトのセッション状態の一部としてチュートリアル ウィジェットが開いていることを確認してください。左側のツールバーにある本のアイコンを押すと、チュートリアル ウィジェットを開くことができます。

<a id="writing-a-step-by-step-guide"></a>
## ステップバイステップのガイドを作成する

チュートリアルの主なコンポーネントは、ステップごとに 1 つのプレーン HTML ファイルと、それらを結び付ける json ファイルです。例については、[ここ](https://github.com/mattearnshaw/tutorials/tree/master/1_hh_practical) を参照してください。
インタラクティブな側面を作成するには、`quickExperiment` JavaScript 関数を使用して、受講者が設定したパラメーターを使用して実験を追加できます。例については、[ここ](https://github.com/mattearnshaw/tutorials/blob/master/1_hh_practical/2.html) を参照してください。 json ファイルでは、`name` (チュートリアル タイトル)、チュートリアル ウィジェットのデフォルトの `height` および `width`、各ステップの HTML ファイルのパスのリストを指定する必要があります。例については、[ここ](https://github.com/mattearnshaw/tutorials/blob/master/1_hh_practical/hh_practical.json) を参照してください。

最後に、上記の手順 (デフォルト セッションの構成) でダウンロードした json ファイルを編集して、チュートリアル ウィジェットにチュートリアルを追加する必要があります。編集する前に、[フォーマッタ](https://jsonformatter.org/json-pretty-print) を通じてこのファイルを実行すると役立つ場合があります。チュートリアル ウィジェットのデータ フィールドに、上で作成した json ファイルを指す URL を追加します (例については、[ここ](https://github.com/mattearnshaw/tutorials/blob/master/models/hodgkinHuxley/GEPPETTO.json) を参照)。 `componentSpecific` の下の `activeTutorial` フィールドを、最初に表示したいチュートリアルのタイトルに変更することもできます。受講者は、チュートリアル ウィジェットの左上隅にある本のアイコンを使用してチュートリアルを切り替えることができます。

<a id="existing-tutorials"></a>
## 既存のチュートリアル

既存のチュートリアル [ここ](http://www.opensourcebrain.org/tutorials) をご覧ください。シナプス統合チュートリアルはまだ開発中です。

<a id="support"></a>
## サポート

チュートリアルの準備のどの段階でも、<b><a href="http://www.opensourcebrain.org/docs#How_To_Contact_Us" onclick="javascript:(function(event){ enableDocSection($(this).attr('href')); if(window.history.pushState) {window.history.pushState(null, null, $(this).attr('href'));} event.preventDefault(); })">ご連絡ください</a></b>。
</section>

</article>
</main>
