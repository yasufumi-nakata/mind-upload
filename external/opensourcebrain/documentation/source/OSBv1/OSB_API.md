---
layout: default
title: "OpenSourceBrain Documentation: OSBv1 用の API"
description: "OpenSourceBrain/Documentation: source/OSBv1/OSB_API.md の日本語訳"
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
<p>原典: <a href="https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv1/OSB_API.md" target="_blank" rel="noopener noreferrer">https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv1/OSB_API.md</a></p>
<p>ライセンス: CC BY 4.0。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
<a id="v1:API"></a>
<a id="api-for-osbv1"></a>
# OSBv1 用の API

OSB プロジェクトに含まれる情報にアクセスするための API が開発されました。

https://github.com/OpenSourceBrain/OSB_API. を参照

<a id="rest-api"></a>
## REST API

これは、OSB のベースとなるフレームワークである [レッドマイン](http://www.redmine.org) 用に開発された [REST API](http://www.redmine.org/projects/redmine/wiki/Rest_api) に基づいています。

OSB 上の各プロジェクトに対してこの REST API によって返されるデータの例は、ここで参照できます: http://www.opensourcebrain.org/projects/thalamocortical.xml.

<a id="python-api"></a>
## Python API

この REST API を使用する Python モジュール (osb) が開発されており、OSB プロジェクトに関して取得した情報を使用するスクリプトを開発できます。

簡単な使用例を以下に示します。

    import osb

    for project in osb.get_projects(min_curation_level="Low"):

        print "Project: %s has tags: %s" % (project.name, project.tags)

その他の例は [ここ](https://github.com/OpenSourceBrain/OSB_API/tree/master/python/examples) にあります。



</section>

</article>
</main>
