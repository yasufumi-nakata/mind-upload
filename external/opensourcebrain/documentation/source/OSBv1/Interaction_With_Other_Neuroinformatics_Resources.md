---
layout: default
title: "OpenSourceBrain Documentation: 他のニューロインフォマティクス リソースとの対話"
description: "OpenSourceBrain/Documentation: source/OSBv1/Interaction_With_Other_Neuroinformatics_Resources.md の日本語訳"
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
<p>原典: <a href="https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv1/Interaction_With_Other_Neuroinformatics_Resources.md" target="_blank" rel="noopener noreferrer">https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv1/Interaction_With_Other_Neuroinformatics_Resources.md</a></p>
<p>ライセンス: CC BY 4.0。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
<a id="v1:neuroinformatics_resources"></a>
<a id="interaction-with-other-neuroinformatics-resources"></a>
# 他のニューロインフォマティクス リソースとの対話

以下は、神経情報学、計算神経科学、システム生物学の分野におけるいくつかの重要なリソースのリストと、オープンソース ブライアン リポジトリがそれらとどのように連携するかを計画しているものです。

<a id="modeldb"></a>
## モデルDB

[モデルDB](http://senselab.med.yale.edu/ModelDB/) は、計算神経科学で公開されているモデルを厳選したデータベースです。これは、OSB のモデルのベースとなるオリジナルのシミュレーター スクリプトのほとんどの主要なソースです。必要に応じて、OSB モデルは ModelDB 上の元の公開モデルにリンクされます。

将来的には、これらのリソース間のリンクの強化が計画されており、オリジナルのモデル スクリプト (シミュレーター固有の形式) や、他のモデリング スタディで拡張/改善/使用されている更新バージョン (標準化された形式) を見つけやすくなります。

<a id="neuralensemble"></a>
## ニューラルアンサンブル

![](http://www.opensourcebrain.org/images/neuralensemble.png)

[ニューラルアンサンブル](http://neuralensemble.org/) は、計算神経科学用のソフトウェアを開発する多数のプロジェクトを調整し、神経機能に関する複雑な問題に対処するための相互運用可能なツールのセットを作成する取り組みです。

NeuralEnsemble イニシアチブの一環として開発されたツールの多くは、OSB で開発されたモデルのターゲット アプリケーションになります。

<a id="neurolex-nif"></a>
## NeuroLex と NIF

![](http://www.opensourcebrain.org/attachments/download/85/nifneurolex.png)

[ニューロレックス](http://neurolex.org/wiki/Main_Page) は神経科学の辞書です。 OSB モデルの多くの重要な要素 (細胞、イオン チャネル、脳領域) には NeuroLex 辞書内に固有のエントリがあり、この識別子を使用して OSB 内の要素を識別できます。

これらの参照は現在、多くのテーマ Wiki ページ ([ここ](http://www.opensourcebrain.org/projects/cerebellarmodelling/wiki) など) で使用されており、**neuroLexId** は NeuroML v2.0 モデル要素の新しい属性であるため、セル、セルラー要素、チャネルなどの識別にさらに広く使用されるようになるでしょう ([ここ](http://sourceforge.net/apps/trac/neuroml/browser/NeuroML2/examples/NML2_FullCell.nml#L65) の例を参照)。

詳細については、[NIF と NeuroLex ショーケース プロジェクト](http://www.opensourcebrain.org/projects/nifshowcase) を参照してください。

<a id="biomodels"></a>
## バイオモデル

[バイオモデル](http://www.ebi.ac.uk/biomodels-main/) データベースは、査読済み、公開済みの計算モデルのリポジトリです。私たちはこのデータベースの開発者と協力して、これらのリポジトリ内のモデル間のリンクを強化できるように取り組んでいます。

この作業は主に [結合ネットワーク](http://co.mbine.org) の枠組みで行われています。

<a id="neuroelectro"></a>
## ニューロエレクトロ

![](http://www.opensourcebrain.org/images/neuroelectro_logo.png)

[ニューロエレクトロ](http://neuroelectro.org/) は、ニューロンの電気生理学的特性に関する情報の構造化データベースです。このタイプの情報は、モデル ニューロンの電気的特性を実際の実験データと比較するのに非常に役立ちます。

NeuroElectro データベースへの API を使用すると、このデータを取得でき、[科学ユニット](https://github.com/cyrus-/sciunit) パッケージを使用して、これらのプロパティに対するモデルのテストを作成できます。

詳細については、[NeuroElectro & SciUnit ショーケース プロジェクト](http://www.opensourcebrain.org/projects/neuroelectrosciunit) を参照してください。
</section>

</article>
</main>
