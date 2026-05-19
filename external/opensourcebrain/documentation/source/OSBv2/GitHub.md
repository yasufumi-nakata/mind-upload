---
layout: default
title: "OpenSourceBrain Documentation: GitHub との対話"
description: "OpenSourceBrain/Documentation: source/OSBv2/GitHub.md の日本語訳"
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
<p>原典: <a href="https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv2/GitHub.md" target="_blank" rel="noopener noreferrer">https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv2/GitHub.md</a></p>
<p>ライセンス: CC BY 4.0。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
<a id="osbv2:github"></a>
<a id="interacting-with-github"></a>
# GitHub との対話

[GitHub](https://github.com/) は、OSBv2 のコードとデータの主要なソースの 1 つです。

任意のパブリック GitHub リポジトリを [OSBリポジトリ](/external/opensourcebrain/documentation/source/OSBv2/Repositories.html#osbv2:repositories) のソースとして使用できます。たとえば、[OSBv2 のガイド付きツアー](/external/opensourcebrain/documentation/source/OSBv2/Guided_tour.html#osbv2:guidedtour) のメイン リポジトリのソースは GitHub ([GitHub リポジトリ](https://github.com/OpenSourceBrain/OSBv2_Showcase)、[OSBv2リポジトリ](https://www.v2.opensourcebrain.org/repositories/38)) にあります。

GitHub ベースのリポジトリとワークスペースに関する注意:

- 現在、**パブリック** GitHub リポジトリのみが OSBv2 リポジトリのソースとして使用できます。
- [ワークスペース](/external/opensourcebrain/documentation/source/OSBv2/Workspaces.html#osbv2:workspaces) が GitHub リポジトリから作成されるときにコピーされるのは、リポジトリの内容の **スナップショット**、つまり、その時点で指定されたブランチにコミットされているものです。

<a id="using-git-on-workspace-contents-in-jupyterlab"></a>
## JupyterLab のワークスペースコンテンツで git を使用する

GitHub ベースの OSB リポジトリから作成されたワークスペースが [ジュピターラボ](/external/opensourcebrain/documentation/source/OSBv2/JupyterLab.html#osbv2:applications:jupyterlab) で開かれる場合 (例: [ガイド付きツアー OSBv2 ショーケース](/external/opensourcebrain/documentation/source/OSBv2/Guided_tour.html#osbv2:guidedtour) から)、`git` コマンド ライン ツールを使用して、ワークスペースの作成時のバージョンからのファイルの変更を調査し、リモート リポジトリから変更を取得できます。


![JupyterLab 上の GitHub リモート リポジトリとの対話](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/github_jlab.png)

*JupyterLab 上の GitHub リモート リポジトリとの対話*
</section>

</article>
</main>
