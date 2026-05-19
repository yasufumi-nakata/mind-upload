---
layout: default
title: "NetPyNE docs: インストール<a href=\"#installation\" class=\"headerlink\" title=\"Link to this heading\"></a>"
description: "NetPyNE docs: install.md の日本語訳"
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
<p>原典: <a href="http://doc.netpyne.org/install.html" target="_blank" rel="noopener noreferrer">http://doc.netpyne.org/install.html</a></p>
<p>ライセンス: MIT License for NetPyNE repository documentation/code。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
<div class="document" role="main" itemscope="itemscope" itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="installation" class="section">

<span id="install"></span>

# インストール<a href="#installation" class="headerlink" title="Link to this heading"></a>

<div id="requirements" class="section">

## 要件<a href="#requirements" class="headerlink" title="Link to this heading"></a>

NetPyNE をインストールする前に、以下がインストールされていることを確認してください。

1. Python 2 または 3 (2.7 およびバージョン \> 3.6 がサポートされています)。 Python と多くの必要なパッケージが既にインストールされているパッケージ/環境マネージャー <a href="https://www.anaconda.com/distribution/" class="reference external">Anaconda</a> をお勧めします。あるいは、Python のインストールは、<a href="https://www.python.org/" class="reference external">Python の公式 Web サイト</a> から行うこともできます。 Windows を使用している場合は、<a href="https://jchen6727.github.io/portal/windows/wsl/neuron/netpyne/python/2022/10/31/A-Neurosim-Build-Using-Windows-Subsystem-Linux!.html" class="reference external">Windows サブシステム Linux</a> (推奨) を使用するか、Windows 上の <a href="https://jchen6727.github.io/portal/windows/neuron/netpyne/python/2023/04/11/A-Neurosim-Build-On-Windows.html" class="reference external">Anaconda ディストリビューションを通じて Python を使用するためのクイックスタート ガイドを参照してください。

2. Python パッケージをインストールするための <span class="pre">`pip`</span> ツール。 <a href="https://pip.pypa.io/en/stable/installing/" class="reference external">pip のインストールはこちら</a> を参照してください。

3. NEURON シミュレーター。 NEURON の <a href="http://www.neuron.yale.edu/neuron/download/" class="reference external"> インストール手順</a> を参照してください。並列シミュレーションを実行したい場合は、必ず MPI サポートを備えた NEURON をインストールしてください (<a href="https://neuron.yale.edu/ftp/neuron/2019umn/neuron-quickstart.pdf" class="reference external">クイック スタート ガイド</a> も参照)。 Linux または Mac の場合の注意: Linux または Mac 上の最新の NEURON バージョンは、<span class="pre">`pip`</span>` `<span class="pre">`install`</span>` `<span class="pre">`neuron`</span> から簡単にインストールできます。

注： Windows ユーザーは、<a href="https://learn.microsoft.com/en-us/windows/wsl/install" class="reference external">Windows サブシステム Linux</a> を利用して、Linux 環境を再作成できます。

よくある質問。これまで、パス定義により、Python、NEURON、または NetPyNE の実行に問題が発生していました。パス マネージャーを使用すると、これを解決できます (Anaconda、Miniconda など)。インストールするときは、すべての *推奨* パス定義がインストールに含まれるように注意してください。

</div>

<div id="install-the-latest-released-version-of-netpyne-via-pip-recommended" class="section">

## pip 経由で NetPyNE の最新リリース バージョンをインストールします (推奨)<a href="#install-the-latest-released-version-of-netpyne-via-pip-recommended" class="headerlink" title="Link to this heading"></a>

Linux (または WSL を介した Windows) または Mac OS:

端末から:

<span class="pre">`pip`</span>` `<span class="pre">`install`</span>` `<span class="pre">`netpyne`</span>

窓

Anaconda PowerShell またはユーザーが事前に構成した端末から:

<span class="pre">`pip`</span>` `<span class="pre">`install`</span>` `<span class="pre">`netpyne`</span>

</div>

<div id="upgrade-to-the-latest-released-version-of-netpyne-via-pip" class="section">

## pip<a href="#upgrade-to-the-latest-released-version-of-netpyne-via-pip" class="headerlink" title="Link to this heading"></a> 経由で NetPyNE の最新リリース バージョンにアップグレードします。

NetPyNE がすでにインストールされており、最新バージョンに更新したい場合は、このオプションを使用します。

Linux (または WSL を介した Windows) または Mac OS:

端末から:

<span class="pre">`pip`</span>` `<span class="pre">`install`</span>` `<span class="pre">`netpyne`</span>` `<span class="pre">`-U`</span>

Windows:

Anaconda PowerShell またはユーザーが事前に構成した端末から:

<span class="pre">`pip`</span>` `<span class="pre">`install`</span>` `<span class="pre">`-U`</span>` `<span class="pre">`netpyne`</span>

</div>

<div id="install-the-development-version-of-netpyne-via-github-and-pip" class="section">

## GitHub および pip<a href="#install-the-development-version-of-netpyne-via-github-and-pip" class="headerlink" title="Link to this heading"></a> 経由で NetPyNE の開発バージョンをインストールします

NetPyNE パッケージのソース ファイルとサンプル モデルは、GitHub 経由で次の場所から入手できます: <a href="https://github.com/Neurosim-lab/netpyne" class="reference external">https://github.com/Neurosim-lab/netpyne</a>. 次の手順では、GitHub の「開発」ブランチにバージョンをインストールします。これには、最新の機能強化とバグ修正の一部が含まれますが、一時的なバグも含まれる可能性があります。

1. <span class="pre">`git`</span>` `<span class="pre">`clone`</span>` `<span class="pre">`https://github.com/suny-downstate-medical-center/netpyne.git`</span>

2. <span class="pre">`cd`</span>` `<span class="pre">`netpyne`</span>

3. <span class="pre">`git`</span>` `<span class="pre">`checkout`</span>` `<span class="pre">`development`</span>

4. <span class="pre">`pip`</span>` `<span class="pre">`install`</span>` `<span class="pre">`-e`</span>` `<span class="pre">`.`</span>

pip は、デフォルトの Python パッケージ ディレクトリ内のシンボリック リンクをクローンされた NetPyNE ディレクトリに追加します (そのため、PYTHONPATH を変更する必要はありません)。新しい変更が利用可能な場合は、クローンされた NetPyNE ディレクトリから <span class="pre">`git`</span>` `<span class="pre">`pull`</span> を実行するだけです。

このバージョンは、パッケージの拡張に関心のある開発者も使用できます。

</div>

<div id="use-a-browser-based-online-version-of-netpyne-gui-beta-version" class="section">

<span id="install-gui"></span>

## NetPyNE GUI のブラウザベースのオンライン バージョンを使用します (ベータ版)<a href="#use-a-browser-based-online-version-of-netpyne-gui-beta-version" class="headerlink" title="Link to this heading"></a>

NetPyNE GUI は、<a href="http://v2.opensourcebrain.org" class="reference external">v2.opensourcebrain.org</a> からオンラインで入手できます。このオンライン版には最大同時ユーザー数があるため、ログインできない場合は、しばらくしてからもう一度お試しください。

注: GUI には、NetPyNE コード/モデルを直接実行するために使用できる (つまり、実際のグラフィカル インターフェイスを使用せずに) インタラクティブな Python Jupyter Notebook (左下の「Python」アイコンをクリック) も含まれています。

</div>

<div id="installation-troubleshooting" class="section">

## インストールのトラブルシューティング<a href="#installation-troubleshooting" class="headerlink" title="Link to this heading"></a>

インストール中に問題が発生した場合は、詳細を記載したメッセージを <a href="http://www.netpyne.org/forum" class="reference external">NetPyNE フォーラム</a> または <a href="https://github.com/Neurosim-lab/netpyne/issues" class="reference external">NetPyNE GitHub issues</a> に投稿してください。

</div>

</div>

</div>

</div>
</section>

</article>
</main>
