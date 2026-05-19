---
layout: default
title: "OpenSourceBrain Documentation: 独自の OSBv1 プロジェクトの作成"
description: "OpenSourceBrain/Documentation: source/OSBv1/Creating_Your_Own_Project.md の日本語訳"
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
<p>原典: <a href="https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv1/Creating_Your_Own_Project.md" target="_blank" rel="noopener noreferrer">https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv1/Creating_Your_Own_Project.md</a></p>
<p>ライセンス: CC BY 4.0。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
<a id="v1:create_project"></a>
<a id="creating-your-own-osbv1-project"></a>
# 独自の OSBv1 プロジェクトの作成

<a id="is-your-model-on-modeldb"></a>
## あなたのモデルは ModelDB にありますか?

まず、モデルが公開されている場合は、**オリジナルのスクリプトを [モデルDB](http://senselab.med.yale.edu/ModelDB/default.asp)** に提出してください。これは、出版時にモデルをデポジットするための正しい場所であり、計算神経科学の出版物に関連するオリジナルのスクリプトを探している人にとって最初の窓口となるはずです。

ModelDB への送信後にモデルを OSB に配置することは、オープン ソースの共同環境で自分の (または他のモデラーの公開共有された) モデルを開発し、モデルのデバッグや改善の支援を得て、シミュレーターに依存しない形式に変換し、一般に広範な再利用を奨励したいことを示しています。

<a id="sign-up-to-osb"></a>
## OSB にサインアップする

OSBv1 [ここ](http://www.opensourcebrain.org/account/register) のユーザーとして登録します。 [GitHub](https://github.com/) ユーザー名と [ORCID ID](https://orcid.org/) (持っている場合) を追加します。

プロジェクト、ソフトウェア、またはラボの URL も追加する必要があります。
後者の場合、PI が同意すれば、そのグループを [OSBイニシアチブに参加している研究室](http://www.opensourcebrain.org/about#who_about) のリストに追加できます。
ご興味がございましたら、info@opensourcebrain.org までメールをお送りください。

<a id="share-your-code"></a>
## コードを共有する

GitHub 上にコード用の新しいリポジトリを作成します (ソース コード テクノロジと Git/GitHub について詳しく知りたい場合は、[ここ](/external/opensourcebrain/documentation/source/General/Background_Information/01_Introduction_to_Source_Control.html#bg:scm) を参照してください)。
[GitHub ヘルプ](https://help.github.com/articles/create-a-repo) で新しいリポジトリの作成の概要を参照してください。

リポジトリは [OpenSourceBrain GitHub 組織](https://github.com/OpenSourceBrain) でホストできますが、個人アカウントで保持しても問題ありません。リポジトリのホストを希望される場合は、<a href="mailto:info@opensourcebrain.org"></a> お知らせください。リポジトリを追加し、GitHub ユーザーにリポジトリへのフル アクセスを付与します。

<a id="create-a-new-osb-project"></a>
## 新しい OSB プロジェクトを作成する

ログインしたら、http://www.opensourcebrain.org に移動します。右上に新しいプロジェクトを追加するための緑色のボタンがあるはずです。

![](https://raw.githubusercontent.com/OpenSourceBrain/OSB_Documentation/master/resources/images/NewProject.png)

プロジェクトの長い名前 (これは後で編集できます)、短い ID (これは変更できません)、プロジェクトの説明、および GitHub リポジトリへのパスを入力します。

元のモデル コードが存在する場合は、**[モデルDB](http://senselab.med.yale.edu/ModelDB/default.asp) エントリへのリンク**を忘れずに追加してください。詳細については、[次のページ](/external/opensourcebrain/documentation/source/OSBv1/Write_Your_Project_Documentation.html#v1:document_project) を参照してください。

<a id="add-some-documentation"></a>
## ドキュメントを追加

OSB プロジェクトにさらにドキュメントを追加するための情報 [ここ](/external/opensourcebrain/documentation/source/OSBv1/Write_Your_Project_Documentation.html#v1:document_project) があります。 README ファイルまたはその他のメタデータから取得した説明。

<a id="say-hello"></a>
## こんにちは…

今がこの機会に info@opensourcebrain.org までご連絡いただき、OSB から何を実現したいかについての計画をお知らせください。新しいユーザーからのご意見をお待ちしております。
</section>

</article>
</main>
