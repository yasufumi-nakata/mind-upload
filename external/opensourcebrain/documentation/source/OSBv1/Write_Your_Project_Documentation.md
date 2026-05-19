---
layout: default
title: "OpenSourceBrain Documentation: プロジェクトを文書化する"
description: "OpenSourceBrain/Documentation: source/OSBv1/Write_Your_Project_Documentation.md の日本語訳"
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
<p>原典: <a href="https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv1/Write_Your_Project_Documentation.md" target="_blank" rel="noopener noreferrer">https://github.com/OpenSourceBrain/Documentation/blob/main/source/OSBv1/Write_Your_Project_Documentation.md</a></p>
<p>ライセンス: CC BY 4.0。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
<a id="v1:document_project"></a>
<a id="document-your-project"></a>
# プロジェクトを文書化する
OSB プロジェクトにドキュメントを追加し、注釈を付けるには、いくつかのオプションがあります。


<a id="add-a-readme-file-in-your-github-repository-and-reuse-it-on-your-osb-projects"></a>
## README ファイルを GitHub リポジトリに追加し、OSB プロジェクトで再利用します

[READMEファイル](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) は、リポジトリの内容とその使用方法の概要を簡単に説明するのに最適な方法です。 GitHub でコードを共有する場合、最上位に README を追加すると、リポジトリにアクセスした人は誰でも内容の簡単な紹介を確認できるようになります。これらは通常、編集しやすい [マークダウン形式](https://daringfireball.net/projects/markdown/basics) で作成されます。

説明をコピー/ペーストする必要性を回避し、概要が 1 か所のデータから消えてしまうのを避けるために、GitHub の README の正確な内容を OSB 上のメインの説明に再利用できます。 [設定] のメイン プロジェクトの説明のテキスト フィールドに次の内容を追加するだけです。

{% raw %}
```
github:README.md
```
{% endraw %}

![お読みください](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/README_settings.png)

たとえば、次のようになります: https://github.com/OpenSourceBrain/ACnet2/blob/master/README.md は、次の OSB プロジェクト ページでプロジェクトの説明としても使用されます: http://www.opensourcebrain.org/projects/acnet2.

<a id="set-values-for-custom-fields"></a>
## カスタムフィールドの値を設定します

OSB のプロジェクトのフィールドに多数の値を設定して、モデルを分類し、他のリソースにリンクし、OSB でのモデルの検索を容易にすることができます。これらには、[モデルDB](https://senselab.med.yale.edu/ModelDB/default) 上の元のスクリプトの場所、モデル化されている種と脳領域、モデルのキュレーションの状態が含まれます。

これらには「設定」からアクセスできます。 **注: これらの値を変更するには、<u>管理設定</u> の下にある <u>カスタム フィールド</u> タブをクリックする必要があります。**

![お読みください](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/Settings_fields.png)


<a id="add-wiki-pages-to-osb-projects"></a>
## Wiki ページを OSB プロジェクトに追加する

新しい Wiki ページを OSB プロジェクトに追加するには、プロジェクト オプション バー (ログイン時) の [Wiki] リンクをクリックし、Wiki ページの編集を開始します。

OSB ドキュメントは [マークダウン形式の構文](https://daringfireball.net/projects/markdown/basics) で書かれており、Redmine および OSB 固有の追加機能もいくつか含まれています (詳細については以下を参照してください)。
注 Markdown を使用すると、ほとんどの HTML 構文 (ビデオなど) を含めることができます。
GitHub wiki と可能な限り互換性を保つために、OSB は [GitHub 風味のマークダウン](https://help.github.com/articles/markdown-basics) を使用します。
チートシート [ここ](https:www.opensourcebrain.org/help/en/wiki_markdown_syntax.html) があります。

以下では、OSB 上の Wiki ページを強化するための OSB/Redmine の機能について簡単に説明します (これらは、[設定] のメイン プロジェクトの説明のテキスト フィールドでも使用できます)。

<a id="reference-to-a-repository-file"></a>
### リポジトリ ファイルへの参照。

GitHub または Bitbucket リポジトリ (プロジェクトで使用されるリポジトリ) 内の任意のファイル (マークダウンまたはプレーン テキスト) を指定できます。

{% raw %}
```
github:[path]
bitbucket:[path]
```
{% endraw %}

これにより、ファイルのコンテンツが取得され、OSB wiki ページに表示されます。これにより、リポジトリ内の 1 つのファイル (メインの README.md など) がプロジェクトのドキュメントのマスター コピーとなり、OSB でプロジェクトを閲覧している人がそのファイルにアクセスできるようになります。

*例：*

{% raw %}
```
github:help/readme.md
bitbucket:help.txt
```
{% endraw %}


<a id="reference-to-pubmed-publication"></a>
### [パブメッド](https://www.ncbi.nlm.nih.gov/pubmed/) 出版物への参照:

{% raw %}
```
pubmed:[publicationID]
```
{% endraw %}

*例：*

{% raw %}
```
pubmed:17442244
```
{% endraw %}

この構文は、次のような参照リンクを生成します (リンクは OSB でのみ正しく表示されます): pubmed:17442244 と、参考文献セクションがページの下部に自動的に生成されます。


<a id="create-a-formula"></a>
### 数式を作成する

LaTeX 構文を使用してドキュメントに数式を記​​述することができます。次のように数式を囲むだけです。

{% raw %}
```
{{latex(formula)}}
```
{% endraw %}

*例：*

{% raw %}
```
{{latex(x=\frac{-b\pm\sqrt{b^2-4ac}}{2a})}}
```
{% endraw %}

これにより、[GoogleチャートAPI](https://developers.google.com/chart/infographics/docs/formulas) を使用して次のイメージが自動的に生成されます。
![](https://raw.githubusercontent.com/OpenSourceBrain/OSB_Documentation/master/resources/images/formula.png)

<a id="link-to-wiki-page"></a>
### Wiki ページへのリンク

他の Wiki ページにリンクしたい場合:

{% raw %}
```
[[Wiki page]]
```
{% endraw %}

<a href="#">ウィキページ</a>

<a id="link-to-an-issue"></a>
### 問題へのリンク

プロジェクト内の課題にリンクしたい場合:

{% raw %}
```
Issue #12
```
{% endraw %}

<a href="#">#12</a> を発行します

<a id="link-to-a-commit"></a>
### コミットへのリンク

リポジトリ内のコミットにリンクしたい場合:

{% raw %}
```
commit:f30e13e43
```
{% endraw %}

<a href="#">f30e13e4</a>
</section>

</article>
</main>
