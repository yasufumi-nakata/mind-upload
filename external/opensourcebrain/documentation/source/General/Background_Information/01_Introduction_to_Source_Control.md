---
layout: default
title: "OpenSourceBrain Documentation: ソース管理の概要"
description: "OpenSourceBrain/Documentation: source/General/Background_Information/01_Introduction_to_Source_Control.md の日本語訳"
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
<p>原典: <a href="https://github.com/OpenSourceBrain/Documentation/blob/main/source/General/Background_Information/01_Introduction_to_Source_Control.md" target="_blank" rel="noopener noreferrer">https://github.com/OpenSourceBrain/Documentation/blob/main/source/General/Background_Information/01_Introduction_to_Source_Control.md</a></p>
<p>ライセンス: CC BY 4.0。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
<a id="bg:scm"></a>
<a id="introduction-to-source-control"></a>
# ソース管理の概要

ソースまたはバージョン管理は、特定のバージョンを後で呼び出せるように、ファイルまたはファイルのセットに対する変更を長期間にわたって記録するシステムです。また、複数の人が同時にファイルを変更することも防ぎます。

<a id="git"></a>
#Git

[Git](http://git-scm.com/) は、高速パフォーマンスとノンリニア編集に重点を置いた分散型 [バージョン管理システム](http://en.wikipedia.org/wiki/Revision_control) (DVCS) です。 Linux カーネル コードベースの開発ツールとして 2005 年に考案され、2014 年現在、最も広く採用されているバージョン管理テクノロジの 1 つとなっています。 Git は無料のオープンソースであり、小規模なプロジェクトから非常に大規模なプロジェクトまで、あらゆるプロジェクトを迅速かつ効率的に処理できるように設計されています。

<a id="github"></a>
## GitHub

[この 15 分間のブラウザ内チュートリアル](http://try.github.com/levels/1/challenges/1) を実行するのが、Git と GitHub を使い始める最も簡単な方法です。もう 1 つの良い選択肢は、この [GitHub の Hello World ガイド](https://guides.github.com/activities/hello-world/) です。 Ralf Ebert 著の [このスクリーンキャスト](http://www.ralfebert.de/blog/tools/git_screencast/) は包括的な入門書として最適です (特にバージョン管理システムにすでに精通している場合)。より体系的な扱いについては、Git の Web サイトの [公式ドキュメント](http://git-scm.com/doc) の一部として入手できる Scott Chacon 著の優れた [プロギット](http://git-scm.com/book) 書籍を参照してください。 Mark Lodato による [ビジュアル Git リファレンス](http://marklodato.github.io/visual-git-guide/index-en.html) は、より高度な概念を理解しようとする場合に非常に役立ちます。


*なぜ GitHub を使うのか?*

2008 年に誕生した [GitHub](https://github.com/) は、現在 Web 上で最大のオープン ソース コード ホスティング サービスであり、2013 年 1 月の時点で [1,000万のリポジトリ](https://github.com/blog/1724-10-million-repositories) を超えています。オープンソースのパブリック Git リポジトリの無料ホスティングに加え、プライベート リポジトリの有料ホスティング、[共同コーディング](https://github.com/features/projects) 用の一連の強力なツール、およびフィード、フォロワー、 Wiki など。Web インターフェイスまたはスタンドアロン クライアント経由で使用できます (下記を参照)。

Windows および Mac 用のグラフィカル クライアント

多くの人がコマンド ライン インターフェイスを介して Git リポジトリを操作しますが、複数のローカル リポジトリとリモート リポジトリを管理するためのグラフィカル アプリケーションの人気が高まっています。 GitHub には、[窓](http://windows.github.com/) 用にホストされているリポジトリと対話するための便利な GUI があります。

![](https://raw.githubusercontent.com/OpenSourceBrain/OSB_Documentation/master/resources/images/GuiWin.png)

および [マック](http://mac.github.com/):

![](https://raw.githubusercontent.com/OpenSourceBrain/OSB_Documentation/master/resources/images/GuiMac.png)

あるいは、より複雑で汎用的なバージョン管理 GUI は [ソースツリー](http://sourcetreeapp.com/) (Windows および Mac) です。

![](https://raw.githubusercontent.com/OpenSourceBrain/OSB_Documentation/master/resources/images/SourceTree.png)

<a id="alternative-version-control-system-vcss-and-hosting-services"></a>
# 代替バージョン管理システム (VCS) とホスティング サービス

GitHub は新規ユーザーに (強く) 推奨されるホスティング サービスですが、特定の技術要件を持つユーザーに対しては、Open Source Brain は [ビットバケット](https://bitbucket.org/) でホストされている [マーキュリアル](http://mercurial.selenic.com/) リポジトリ (project:destexhe\_jcns\_2009 などを参照) およびセルフホスト型 SVN/Git/Mercurial/Bazaar パブリック リポジトリをサポートしています。


</section>

</article>
</main>
