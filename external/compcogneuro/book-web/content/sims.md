---
layout: default
title: "compcogneuro/book-web: sims"
description: "compcogneuro/book-web: sims.md の日本語訳"
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
<p>原典: <a href="https://github.com/compcogneuro/book-web/blob/main/content/sims.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/book-web/blob/main/content/sims.md</a></p>
<p>ライセンス: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
以下のシミュレーションのリストにあるリンクを使用して、この書籍に関連するシミュレーション演習を Web 上で実行することをお勧めします。

**重要:** 現在、これは macOS および Windows 上の Chrome の最新バージョンでのみ完全に動作します。そのため、Linux を使用している場合は、このページの下部にある別の手順を参照してください。

シミュレーションに関連するすべてのバグ レポートは、[問題トラッカー](https://github.com/compcogneuro/sims/issues) に提出する必要があります。

さらに詳しい背景情報と基礎となるコードが必要な場合は、[コージェントコア](https://cogentcore.org/core) を使用して、[シムズ](https://github.com/compcogneuro/sims) リポジトリ内の [緊急の](https://github.com/emer/emergent) フレームワークの Go バージョンでシミュレーションが実装されます。この Web サイトも Cogent Core で構築されています。

＃＃ 使用法

各シミュレーションには、ウィンドウの右側に完全なステップバイステップの説明があり、モデルの実行方法と、クラスの使用法について答えるための質問が含まれています (詳細については、シラバスを参照してください)。提供されたテキスト ボックスを使用して、シミュレーション内の質問に答えることができます。これらのテキスト ボックスは、作業内容の損失を防ぐためにブラウザに自動的に保存されます。すべての質問に回答したら、説明の上部にある [回答をコピー] ボタンをクリックします。次に、新しい Google ドキュメントと [マークダウンから貼り付ける](https://support.google.com/docs/answer/12014036) を作成します ([ツール] > [設定] で [マークダウンを有効にする] を選択し、右クリックして [マークダウンから貼り付け] をクリックします)。この Google ドキュメントを PDF としてダウンロードして、クラスに提出できます。

手順には、ユーザー インターフェイス内の要素を強調表示するためにクリックできる特別なリンクが含まれています。たとえば、「テスト サイクル プロット」へのリンクがある場合、それをクリックすると、「テスト サイクル プロット」のボタンが強調表示され、指示に従うのに役立ちます。

標準の `Ctrl+` および `Ctrl-` キー シーケンスを使用して、表示を希望のスケールにズームできます。また、Cogent Core 設定ウィンドウには、ライト/ダーク モードなどのその他の表示オプションがあります (これには、右クリック/2 本指のクリック/コントロール クリックしてから「設定」をクリックすることでアクセスできます)。

実行のための主なアクションは上部のツールバーにあり、モデルに最も関連するパラメータは左側のコントロール パネルにあります。ウィンドウの中央にあるタブ付きビューで、さまざまな出力表示を選択できます。

[Go Emergent Wiki](https://github.com/emer/emergent/wiki/Home) には、ネットワークを表示する `NetView` などを使用するためのさまざまなヘルプ ページが含まれています。

コントロール パネルの `Net` の右側にあるボタンをクリックすると (NetView でレイヤー名をクリックすることでも)、いつでも詳細なパラメータにアクセスでき、このモデルのカスタム パラメータは `Params` フィールドに設定されます。

## シムと演習の質問のリスト

すべてのシミュレーションとそれに関連する教科書の演習問題の完全なリストを次に示します。

## 第 2 章: ニューロン

* [ニューロン](https://sims.compcogneuro.org/ch2/neuron): 統合、スパイク、およびレート コードのアクティブ化。 (質問 **2.1 -- 2.7**)

* [検出器](https://sims.compcogneuro.org/ch2/detector): 検出器としてのニューロン -- ニューロンが何を検出するかを決定する際のシナプス重みの重要な機能を示します。 (質問 **2.8 ～ 2.10**)

## 第 3 章: ネットワーク

* [顔](https://sims.compcogneuro.org/ch3/faces): ボトムアップおよびトップダウンの処理を含む顔の分類 (ネットワークの章の複数の探索に使用) (質問 **3.1 -- 3.3**)

* [猫_犬](https://sims.compcogneuro.org/ch3/cats_dogs): Cats and Dogs モデルの制約満足度。 (質問**3.4**)

* [ネッカーキューブ](https://sims.compcogneuro.org/ch3/necker_cube): ネッカー キューブ モデルにおける制約満足度およびノイズと調整の役割。 (質問**3.5**)

* [インヒブ](https://sims.compcogneuro.org/ch3/inhib): 抑制性介在ニューロンを介した抑制性相互作用、および FFFB 近似。 (質問 **3.6 -- 3.8**)

## 第 4 章: 学習

* [自己組織](https://sims.compcogneuro.org/ch4/self_org): XCAL の BCM のようなダイナミックを使用した自己組織化学習 (質問 **4.1 -- 4.2**)。

* [pat_assoc](https://sims.compcogneuro.org/ch4/pat_assoc): ヘビアンおよびエラー駆動メカニズムを使用した単純な入出力マッピング タスク (パターン アソシエーター) を学習する基本的な 2 層ネットワーク (質問 **4.3 -- 4.6**)。

* [err_driven_hidden](https://sims.compcogneuro.org/ch4/err_driven_hidden): 隠れ層を使用した完全なエラー駆動学習は、あらゆる入出力マッピングを解決できます (質問 **4.7**)。

* [家系図](https://sims.compcogneuro.org/ch4/family_trees): 深い (多重隠れ層) ネットワークでの学習。自己組織化学習とエラー駆動型学習の組み合わせの利点を示します (質問 ** 4.8 -- 4.9**)。

* [hebberr_combo](https://sims.compcogneuro.org/ch4/hebberr_combo): ヘブビアン学習とエラー駆動を組み合わせると一般化が容易になります (質問 **4.10 -- 4.12**)。

注: チャプター 5 にはシムはありません

## 第 6 章: 知覚と注意

* [v1rf](https://sims.compcogneuro.org/ch6/v1rf): ヘビアン学習からの V1 受容野、側面トポグラフィー。 (質問 **6.1 -- 6.2**)

* [オブジェクト](https://sims.compcogneuro.org/ch6/objrec): 階層変換に対する不変オブジェクト認識。 (質問 **6.3 -- 6.5**)

* [注目](https://sims.compcogneuro.org/ch6/attn): 小規模モデルにおける物体認識経路と相互作用する空間的注意。 (質問 **6.6 ～ 6.11**)

## 第 7 章: 学習と記憶

* [アバク](https://sims.compcogneuro.org/ch7/abac): ペアになったアソシエート AB-AC 学習と壊滅的な干渉。 (質問 **7.1 -- 7.3**)

* [ヒップ](https://sims.compcogneuro.org/ch7/hip): 海馬モデルと干渉の克服。 (質問 **7.4 -- 7.6**)

* [呼び水](https://sims.compcogneuro.org/ch7/priming): 重みとアクティベーションベースのプライミング。 (質問 **7.7 -- 7.8**)

## 第 8 章: モーター制御と強化学習

* [バックグラウンド](https://sims.compcogneuro.org/ch8/bg): 大脳基底核におけるアクション選択/ゲーティングおよび強化学習。 (質問 **8.1 -- 8.3**)

* [rl](https://sims.compcogneuro.org/ch8/rl): 時間差強化学習を使用したパブロフ条件付け。 (質問 **8.4 -- 8.5**)

* `pvlv`: PVLV モデルによるパブロフ条件付け (質問 **8.6 -- 8.8**) **まだ利用できません!**

* `cereb`: 運動学習、エラーからの学習における小脳の役割。 (質問 **8.9 -- 8.10**) **まだ利用できません!**

## 第 9 章: 実行機能

* [a_not_b](https://sims.compcogneuro.org/ch9/a_not_b): PFC アクティブ保守と A-not-B タスクの開発 (質問 **9.1 ～ 9.3**)

* [ストロープ](https://sims.compcogneuro.org/ch9/stroop): ストループ効果と PFC トップダウン バイアス (質問 **9.4 -- 9.6**)

* [お客様](https://sims.compcogneuro.org/ch9/sir): タスクの保存/無視/呼び出し - より複雑な PFC モデルでの更新とメンテナンス (質問 **9.7 ～ 9.8**)

## 第 10 章: 言語

* [セム](https://sims.compcogneuro.org/ch10/sem): 世界の共起とヘビアン学習からの意味表現。 (質問 **10.1 ～ 10.3**)

* [ss](https://sims.compcogneuro.org/ch10/ss): 正書法から音韻論へのマッピングと規則性、周波数効果。 (質問 **10.4 -- 10.5**)

* [失読症](https://sims.compcogneuro.org/ch10/dyslexia): 通常の読み取りと無秩序な読み取り、および分散辞書。 (質問 **10.6 ～ 10.11**)

* [sg](https://sims.compcogneuro.org/ch10/sg): 文のゲシュタルト モデル。 (質問**10.12**)

## 別の実行方法

### ソースからビルドする

任意のプラットフォーム上のコンピューター上でローカルに SIM を実行するには、まず [Cogent Core のインストール手順](https://www.cogentcore.org/core/install) に従う必要があります。次に、SIM リポジトリのクローンを作成し、`core run` を使用して SIM を実行できます。

```sh
git clone https://github.com/compcogneuro/sims
cd sims/ch2/neuron # or any other sim
core run
```

You can also use `core run web` to run a sim on the web, which does not require running the `core setup` command in the setup instructions.

### Prebuilt executables

We will provide updated prebuilt versions of the sims soon. You can see old prebuilt versions in the [releases](https://github.com/compcogneuro/sims/releases), which are not recommended. The even older [C++ emergent (cemer)](https://github.com/emer/cemer) sims project files are available here: [cecn_8_5_2.zip](https://github.com/compcogneuro/sims/releases/download/v1.2.2/cecn_8_5_2.zip) (no longer updated or supported; recommend transitioning to new ones).


</section>

</article>
</main>
