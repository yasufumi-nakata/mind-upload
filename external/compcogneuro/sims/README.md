---
layout: default
title: "compcogneuro/sims: 計算による認知神経科学シミュレーション"
description: "compcogneuro/sims: README.md の日本語訳"
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
<p>原典: <a href="https://github.com/compcogneuro/sims/blob/main/README.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/sims/blob/main/README.md</a></p>
<p>ライセンス: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
# 計算による認知神経科学シミュレーション

このリポジトリには、[CCN教科書](https://compcogneuro.org) のニューラル ネットワーク シミュレーション モデルが含まれています。詳細については、[シミュレーションウェブサイト](https://compcogneuro.org/simulations) を参照してください。

＃＃ 状態

* **2024 年 8 月**: Web サイトに記載されているように、SIM は Web 上で実行できるように更新されています。

* **2023 年 2 月 15 日**: バージョン 1.3.3 リリース: 最新の GoGi での Vulkan ドライバーの選択が改善されました。

* **2022 年 9 月 15 日**: バージョン 1.3.2 リリース: ラスター ビューと個別の重量記録を備えた新しい NetView に更新されました。

* **2021 年 9 月 9 日**: バージョン 1.3.1 リリース: バグ修正、sg のディープ leabra バージョン、Python が Windows で動作します。

* **2020 年 11 月 23 日**: バージョン 1.2.2 リリース: Python バージョンと pvlv モデルのフルセット。

* 詳細な履歴については、https://github.com/compcogneuro/sims/releases を参照してください。

## 開発者向けメモ

*これは通常のユーザーには関係ありません*

Makefile には、すべての sims プログラムをビルドし、結果の実行可能ファイルを統合ディレクトリ `~/ccnsimpkg/` にコピーするターゲットが含まれています。このディレクトリは、配布目的で .zip / .tar ファイルを作成するために使用できます。  ターゲットは、`mac`、`linux`、`windows` です。

Windows 上で Makefile を使用してすべての `windows` ターゲット (つまり、`make windows`) をビルドするには、ネイティブの make がインストールされた cygwin を使用する必要があります。PowerShell で動作するように make を再帰的に呼び出すことができませんでした。  また、`TDM-GCC-64` バージョンを使用するように `mv /usr/bin/gcc.exe /usr/bin/gcc-cyg.exe` にする必要があります。そうしないとビルドされません。
</section>

</article>
</main>
