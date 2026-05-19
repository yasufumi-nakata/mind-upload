---
layout: default
title: "OpenSourceBrain Documentation: 投稿ガイドライン"
description: "OpenSourceBrain/Documentation: CONTRIBUTING.md の日本語訳"
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
<p>原典: <a href="https://github.com/OpenSourceBrain/Documentation/blob/main/CONTRIBUTING.md" target="_blank" rel="noopener noreferrer">https://github.com/OpenSourceBrain/Documentation/blob/main/CONTRIBUTING.md</a></p>
<p>ライセンス: CC BY 4.0。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
<a id="contribution-guidelines"></a>
# 投稿ガイドライン

- Jupyter-book は [複数のコンテンツタイプ](https://jupyterbook.org/file-types/index.html) をサポートします。 Markdown のフレーバーが好まれます。
- ドキュメント内の各文は新しい行で始めてください。これにより、
  より良い差分とプルリクエストを実現します。


<a id="building-docs-locally"></a>
## ローカルでドキュメントを構築する

現在、ドキュメントでは [ジュピターブック](https://jupyterbook.org/) が使用されています。
ドキュメントをローカルで構築したり、プル リクエストを開く前にテストしたりするには、仮想環境を使用できます。

{% raw %}
```

  # Create a new virtual environment
  $ python3 -m venv ./.venv
  # Activate the virtual environment
  $ source .venv/bin/activate
  # Install the necessary Python packages
  $ pip install -r requirements-book.txt
  # Build the docs
  $ jupyter-book build ./source
  # This will create the HTML files in ./source/_build/html
```
{% endraw %}


仮想環境を非アクティブ化するには:

{% raw %}
```

  $ deactivate
```
{% endraw %}

Python 仮想環境の詳細については、Python ドキュメント [ここ](https://docs.python.org/3.9/library/venv.html) を参照してください。

<a id="publishing-the-book"></a>
## 本を出版する

この本は、`ghp-import` ツールを使用して GitHub ページで公開されています。

{% raw %}
```

  # Use ghp-import
  $ ghp-import -n -p -f ./source/_build/html
```
{% endraw %}

これにより、`jupyter-book` によってビルドされた HTML ファイルが `gh-pages` ブランチにインポートされます。
詳細については、[公式ドキュメント](https://jupyterbook.org/publish/gh-pages.html) を参照してください。

これらの手順を支援するヘルパー スクリプト `./build-helper.sh` がリポジトリに存在します。
</section>

</article>
</main>
