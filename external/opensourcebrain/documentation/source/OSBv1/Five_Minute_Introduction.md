---
layout: default
title: "OpenSourceBrain Documentation: 5 分間の紹介"
description: "OpenSourceBrain/Documentation: source/OSBv1/Five_Minute_Introduction.md の日本語訳"
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
<p>原典: <a href="https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv1/Five_Minute_Introduction.md" target="_blank" rel="noopener noreferrer">https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv1/Five_Minute_Introduction.md</a></p>
<p>ライセンス: CC BY 4.0。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
<a id="v1:five_min_intro"></a>
<a id="five-minute-introduction"></a>
# 5 分間の紹介

こんにちは！ Open Source Brain (OSB) の基本を見てみましょう。**これを読むのに必要な時間はわずか 5 分です!** (はい、とても簡単です)。

<div class="note-box" markdown="1">
<strong>**注:** この情報は OSBv1.</strong> に固有のものです。

このガイドでは、[OSBv1](https://v1.opensourcebrain.org) の機能について説明します。 [OSBv2](https://v2.opensourcebrain.org) のガイド付きツアーについては、[ここ](/external/opensourcebrain/documentation/source/OSBv2/Guided_tour.html#osbv2:guidedtour) を参照してください。
</div>

これはホーム画面のヘルプ セクションです。道に迷ったときは、いつでもここに戻ってきてください。必要な答えのほとんどがここにあります。ホーム画面から、OSB で利用可能な任意のプロジェクトやモデルを操作したり、独自のプロジェクトやモデルを作成したりできます。利用可能なプロジェクトを検索するには、上部バーの「Explore OSB」リンクをクリックするか、検索ボックスを使用します。

<a id="v1:five_min_intro:what"></a>
<a id="what-is-an-osb-project"></a>
## OSB プロジェクトとは何ですか?

まず最初に、**OSB プロジェクト** とは何ですか?

OSB プロジェクトは計算ニューロン モデルのコンテナであり、通常、これらのモデルは出版物に直接リンクされているか、特定のテクノロジによってすべてがプロジェクトにグループ化されている場合があります。 OSB プロジェクトは常に、特定のプロジェクトで利用可能なすべてのモデルを保存する GitHub リポジトリにリンクされているため、GitHub にすでに慣れている場合は問題ありませんが、そうでない場合は [ここ](https://guides.github.com/activities/hello-world/#what) で知る必要があるすべてが見つかります。 OSB プロジェクト内には多くのモデルが存在する可能性がありますが、**特定のモデルを使用するにはどうすればよいですか**? OSB 内には、モデルの探索、シミュレーション、作業の両方に役立つオンライン環境があります。はい、そのとおりです。特定のモデルを探索したりシミュレーションしたりするためにブラウザを離れる必要はありません。すべてのプロジェクトには、エントリ ポイントとしてメイン モデルがあります。これは、特定のプロジェクトのメイン ネットワークやセルなどです。このモデルを探索するには、プロジェクト内で **右上隅にある緑色のボタン「モデルの探索」をクリック**するだけです。利用可能な他のすべてのモデルを調べるには、その横にある「詳細」ボタンをクリックしてください。

![探索モデル.png](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/exploreModel.png)

モデルは OSB 内にロードされます。モデルのサイズに応じて、これには数秒から最大 1 分かかる場合があります。脳がどれほど複雑であるかご存知ですか?あなたは今モデルを見ていますが、読み取りモードになっています。つまり、モデルの内容を調べて見ることはできますが、シミュレーションを実行することはできません...まだ (読み続けてください!)。それで、何ができるでしょうか？

<a id="v1:five_min_intro:pan"></a>
<a id="pan-and-zoom"></a>
## パンとズーム

最も簡単な機能の 1 つは、シンプルな 3 次元のパン、ズーム、回転機能です。これは、マウスと、左側のパネルのナビゲーション ボタンを使用したより正確な制御の両方で機能します。

![図-1-パンズーム.gif](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/Fig-1-Pan-Zoom.gif)

<a id="v1:five_min_intro:explorer"></a>
<a id="explore-the-models"></a>
## モデルを探索する
OpenSourceBrain のモデルには、それに関連付けられた説明があります。 OSB ツールバーの「モデルの説明」ボタンをクリックすると、これらの説明にアクセスできます。

![ExploreModel.gif](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/ExploreModel.gif)

ビュー内の個々のセルをクリックすると、入力やイオン チャネルなど、それらのセルの詳細な説明を調べることができます。モデル チャネルをさらにクリックすると、それらのチャネルの活性化変数プロットを表示できます。

![ExploreChannels.gif](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/ExploreChannels.gif)

セルの説明をクリックしながら、情報ウィンドウの左上隅にある履歴アイコンを使用していつでも前のシートに戻ることができます。

![ExploreHistory.gif](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/ExploreHistory.gif)

<a id="v1:five_min_intro:explorer_connections"></a>
<a id="explore-the-network-connections"></a>
## ネットワーク接続を探索する
OSB には、モデルの探索に役立つさまざまなウィジェットが組み込まれています。このようなモデルには、かなりの数の接続があります。 [接続] ボタンをクリックすると、さまざまなグラフィカル ツールを使用してモデルの接続パターンを調べることができます。

![図-2-接続性.gif](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/Fig-2-Connectivity.gif)

**シミュレーションを実行**したい場合はどうすればよいですか?まず最初に、モデルを永続化する必要があります。この操作により、モデルのスナップショット (GitHub 上の最新のもののコピー) が作成されます。これはすべてあなたのものであり、書き込みアクセス権が与えられます。モデルの永続化は非常に簡単で、画面上部の星アイコンをクリックして数秒待つだけです (これを行うには、Open Source Brain の登録ユーザーとしてログインする必要があります)。

![持続.png](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/persist.png)

モデルが永続化されたので、それを操作できるようになりました。**実験を見てみましょう**。実験はモデルの特定の構成を表します。実験ごとに、どの状態変数を記録するか、モデルのパラメーターにどの値を与えるか、さらにはどのシミュレーターを使用するかを決定できます (私たちはサンディエゴ スーパー コンピューター センターにも接続していることをご存知ですか?)。

![図-3-紹介.gif](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/Fig-3-Intro.gif)

ログインしてプロジェクトが永続化されると、モデルの操作を開始できます。 「クローン」ボタンをクリックすると、モデルの新しい実験を作成できます。これにより、クローンを作成したものとまったく同様の新しい実験が作成されます。任意の実験のパラメータを変更できます。

![図-4-クローン.gif](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/Fig-4-Clone.gif)

<a id="v1:five_min_intro:recording"></a>
<a id="recording-variables"></a>
## 変数の記録
モデル内に存在する状態変数は、シミュレーションを実行する前に記録できます。つまり、シミュレーションが完了したら、後でその値をプロットすることが可能になります。変数を記録するには、検索バーで変数を検索し (画面左側にある小さな <i class="fas fa-search"></i> アイコンを使用するか、Ctrl+Space を押して開きます)、記録アイコン <i class="fas fa-circle-blank"></i> をクリックします。記録できる状態変数を示すアイコンは <i class="fas fa-superscript"></i> です。

![レコード変数.gif](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/RecordVariable.gif)

<a id="v1:five_min_intro:params"></a>
<a id="setting-parameters"></a>
## パラメータの設定

モデル内の任意のパラメーターを動的に変更して、さまざまな値の影響を確認できます。実験を実行する前に、検索バーでパラメータ名を検索し、入力ボックスの値を変更することで値を変更できます。パラメータ名を示すアイコンは <i class="fas fa-signin"></i> です

![SetParameters.gif](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/SetParameters.gif)

<a id="v1:five_min_intro:run_exp"></a>
<a id="run-an-experiment"></a>
## 実験を実行する

記録する変数と実験パラメーターに満足したら、実験を実行できます。上部バーの「実行」ボタンが使用できるようになります。クリックすると、実験のステータスが変更され、実験が実行キューに入っていることと、実験が完了したことが表示されます。完了した実験の結果を再生する

![図-5-Run.gif](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/Fig-5-Run.gif)

実験が終了したら、[再生] ボタンを使用して、シミュレーションされたすべての記録された変数をプロットできます。

![図-6-再生.gif](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/Fig-6-Playback.gif)

記録した特定の変数をプロットしたい場合は、検索バーを使用してその変数を検索し、「プロット」アイコンを使用してプロットすることができます。特定の実験で記録されたすべての変数のリストは、実験テーブルの「記録された変数」リンクをクリックすると表示されます。

![録音.png](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/Recorded.png)

画面上部の「結果」ボタンをクリックすると、膜電位スパイクを記録した細胞を確認する機能など、いくつかのデフォルトのアクションにすぐにアクセスできます。

![結果.png](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/Results.png)

おめでとうございます。これで、OSB でモデルの探索を開始し、独自のシミュレーションを実行する準備が整いました。
[さあ、独自のプロジェクトを作成しましょう。](/external/opensourcebrain/documentation/source/OSBv1/Creating_Your_Own_Project.html#v1:create_project)
</section>

</article>
</main>
