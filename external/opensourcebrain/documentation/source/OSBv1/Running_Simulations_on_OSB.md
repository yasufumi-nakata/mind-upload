---
layout: default
title: "OpenSourceBrain Documentation: OSBv1 でシミュレーションを実行する"
description: "OpenSourceBrain/Documentation: source/OSBv1/Running_Simulations_on_OSB.md の日本語訳"
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
<p>原典: <a href="https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv1/Running_Simulations_on_OSB.md" target="_blank" rel="noopener noreferrer">https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv1/Running_Simulations_on_OSB.md</a></p>
<p>ライセンス: CC BY 4.0。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
<a id="v1:runsims"></a>
<a id="running-simulations-on-osbv1"></a>
# OSBv1 でシミュレーションを実行する

追加のソフトウェアをインストールしなくても、ブラウザから直接 OSBv1 でシミュレーションを実行できます。

<a id="introduction"></a>
## はじめに

モデルを使用してシミュレーションを実行するには、ログインする必要があり、まずローカル コピーを OSB ワークスペースに保存する (「モデルを永続化する」) 必要があります。これを行うには、星のアイコンをクリックします。

<img src="http://www.opensourcebrain.org/images/help/persist.png" class="img-help">

次に、画面の下部にある「実験」タブを開きます。テンプレート実験はデフォルトで存在し、+ ボタンを使用して追加の実験を追加できます。実験をクリックすると展開され、詳細が表示されます。

すべての膜電位、体細胞の膜電位、または Ca2+ 濃度を記録したいだけの場合は、画面上部の Run メニューをクリックし、Run Active Experiment を選択します。

パラメーターを設定した後 (シミュレーターに関するアドバイスについては以下を参照)、「送信」をクリックします。変数が選択されていない場合は、ショートカット オプションが表示されます。

<img src="https://raw.githubusercontent.com/OpenSourceBrain/OSB_Documentation/master/resources/images/run-shortcuts.png" class="img-help">

オプションを選択すると、実験のステータスがキュー中 (青い円) に変わり、次に実行中 (黄色の円) に変わります。ブラウザを閉じても実験は続行されます。

最後に、実験ステータスが完了 (緑色の円) に変更されます。その後、[結果] メニューを使用して、記録された状態変数をプロットしたり、色付きの形態でシミュレーションを再生したりすることができます。

状態変数の記録、パラメータの変化、結果のプロットをより細かく制御するには、コントロール パネルが役立ちます。コントロール パネルは、左側のコントロール パネルにある <i class="fas fa-list"></i> ボタンで開くことができます。ビジュアル オブジェクト、状態変数、パラメータという 3 つの主要なビューがあります。シミュレーションでは、後者の 2 つに興味があります。

[状態変数] ビューと [パラメーター] ビューには、3 つの基本的なフィルター レベルがあります。右から左に、結果 (状態変数) を表示およびプロットしたり、プロジェクトの実験 (<i class="fas fa-globe"></i>) または現在のプロジェクトの実験 (<i class="fas fa-flask"></i>) のパラメーターを表示したり、記録したい変数を設定したり、現在の実験のパラメーターを変更したりできます。 (<i class="gpt-activeExp"></i>)。後者のフィルターでは、<i class="fas fa-dot-circle"></i> を使用してどの変数が選択されているかを確認することもできます。 注意: 状態変数を設定したり、実験のパラメーターを変更できるのは、実験が DESIGN モード (オレンジ色の円) の場合のみです。完了した実験 (緑色の円) は変更できませんが、[実験] タブの <i class="fas fa-clone"></i> ボタンを使用してクローンを作成できます。

詳細については、[ゼペットのドキュメント](http://docs.geppetto.org/en/latest/userdocs.html) も参照してください。

<a id="protocols"></a>
## プロトコル

[パルスジェネレーター](https://www.neuroml.org/NeuroML2CoreTypes/Inputs.html#pulseGenerator) を持つモデルの場合、[Run] メニューの [Add & Run Protocol] オプションを使用して、一定範囲の振幅に対する実験のバッチを生成できます。

<a id="supported-simulators"></a>
## サポートされているシミュレーター

OSB 上の Neuron、OSB 上の jNeuroML、および OSB 上の NetPyNE シミュレーション オプションは、OSB プラットフォーム独自のサーバー上で実行されます。シミュレーションのサイズと期間には制限が適用されます。

NSG 上の Neuron および NSG 上の NetPyNE は、Neuroscience Gateway Portal 上で実行されます。 NetPyNE on NSG シミュレーションは、最大 256 プロセッサ上で実行できます。

<a id="connect-to-dropbox"></a>
## Dropbox に接続する

シミュレーション結果は、HDF5 形式で Dropbox アプリ フォルダーに自動的に送信できます。

これを有効にするには、[実験の実行] ダイアログの [Dropbox をリンク…] ボタンをクリックします。

Geppetto に Dropbox 内の独自のフォルダーへのアクセスを許可するように求められます。コードをコピーして、OSB のダイアログに貼り付けます。

![](https://raw.githubusercontent.com/OpenSourceBrain/OSB_Documentation/master/resources/images/dropbox-auth.png)

![](https://raw.githubusercontent.com/OpenSourceBrain/OSB_Documentation/master/resources/images/dropbox-auth2.png)

この設定を完了すると、実行ダイアログの [完了時に結果を Dropbox にアップロードする] オプションがデフォルトでオンになり、結果ファイルが Apps/Geppetto フォルダに自動的に表示されます。
</section>

</article>
</main>
