---
layout: default
title: "OpenSourceBrain Documentation: Hackathon_2013"
description: "OpenSourceBrain/Documentation: source/General/Meetings/Hackathon_2013.md の日本語訳"
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
<p>原典: <a href="https://github.com/OpenSourceBrain/Documentation/blob/main/source/General/Meetings/Hackathon_2013.md" target="_blank" rel="noopener noreferrer">https://github.com/OpenSourceBrain/Documentation/blob/main/source/General/Meetings/Hackathon_2013.md</a></p>
<p>ライセンス: CC BY 4.0。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
<a id="meetings:hackathon2013"></a>
<a id="osb-hackathon-2013"></a>
#OSBハッカソン2013

![](http://www.opensourcebrain.org/attachments/download/106/OSBHackathon1.png)

（イラスト提供：[マテオ・ファリネッラ](https://www.opensourcebrain.org/users/34)））

日程: **2013年11月6日水曜日午前9時～木曜日午後5時**

場所: 英国ユニバーシティ・カレッジ・ロンドン。

地元の主催者: [マッテオ・カンタレッリ](https://www.opensourcebrain.org/users/43))、[パドレイグ・グリーソン](https://www.opensourcebrain.org/users/4)、[エウジェニオ・ピアジーニ](https://www.opensourcebrain.org/users/3)、[アンガス・シルバー](https://www.opensourcebrain.org/users/6)、[ボリス・マリン](https://www.opensourcebrain.org/users/67)

<a id="focus-of-meeting"></a>
## 会議の焦点

この会議の焦点は、**オープンソースのマルチコンパートメント、コンダクタンス ベースの皮質細胞およびネットワーク モデル**にありました。

さまざまな科学的問題に対処するために、利害関係者によって利用可能および再利用/変更される、マルチコンパートメントのコンダクタンスベースの（視床）皮質細胞モデルの数が増加しています。例としては [Traub et al 2005 視床皮質ネットワーク モデル](http://www.opensourcebrain.org/projects/thalamocortical) があり、Fortran、NEURON、MOOSE、NeuroML の各バージョンがさまざまなラボで開発されています。この会議は、複数の関係者にとって興味深い新皮質と視床からのさまざまなモデルを検討し、これらを標準化された形式 (NeuroML および潜在的に PyNN) で公開のオープンソース リポジトリに公開し、十分にテストされ、注釈が付けられ、参加者やより広範なコミュニティが研究ツールとして使用できるようにすることを目的としていました。

<a id="aims"></a>
## 目標

この会議の具体的な目的は 3 つありました。

1) Traub ネットワーク モデルのバージョンを統合します。**2005 年の論文の結果を再現することを目的としています**。これらのバージョンがどの段階にあるのか、各実装にはどのような問題があるのか​​を文書化します。

2) 最初は洗練された Traub モデルに基づいて、更新されたセルと接続を備えた**この詳細レベルの新しいネットワーク モデル**の計画を作成します。このモデルは *最初からオープンソースである必要があり*、可能な限りシミュレーターから独立している必要があります。この更新されたモデルに必要な実験データと、それらが表示する必要がある電気的特性に関する要件を収集します。データに対してこれらのモデルを最適化するためのフレームワークを作成します。

3) このプロセスからも恩恵を受ける可能性がある **他のマルチコンパートメント、コンダクタンスベースの皮質モデル** に注目してください (2 のモデルで使用するための修正の候補となる可能性もあります)

<a id="attendees"></a>
## 人の出席者

[ラズロ・ビクスケイ](https://www.opensourcebrain.org/users/229))、アンドリュー ブラウン ([サウサンプトン](http://www.ecs.soton.ac.uk/people/adb))、[マッテオ・カンタレッリ](https://www.opensourcebrain.org/users/43)、[チャイタニヤ チンタルリ](https://www.opensourcebrain.org/users/75)、[トーマス・グレッグ・コーコラン](https://www.opensourcebrain.org/users/228)、[ヘレナ・グウォブスカ](https://www.opensourcebrain.org/users/69)、[パドレイグ・グリーソン](https://www.opensourcebrain.org/users/4)、[リー・ゲッツ](https://www.opensourcebrain.org/users/188)、[ボリス・マリン](https://www.opensourcebrain.org/users/67)、 [フィリップ・メンドンカ](https://www.opensourcebrain.org/users/195)、[サイモン・オコナー](https://www.opensourcebrain.org/users/92)、[パオラ・ペリン](https://www.opensourcebrain.org/users/210)、[エウジェニオ・ピアジーニ](https://www.opensourcebrain.org/users/3)、[スバシス・レイ](https://www.opensourcebrain.org/users/39)、[マルティナ・リザ](https://www.opensourcebrain.org/users/132)、[アルンド・ロス](https://www.opensourcebrain.org/users/108)、[アンガス・シルバー](https://www.opensourcebrain.org/users/6)、[リチャード・トムセット](https://www.opensourcebrain.org/users/198)、 [マイク・ベラ](https://www.opensourcebrain.org/users/50)

<a id="agenda"></a>
## 議題

<a id="wednesday-6th-november"></a>
### 11月6日水曜日

全体的なテーマ: [視床皮質モデリング](http://www.opensourcebrain.org/projects/corticalmodelling/wiki/Wiki)、特にプロジェクト: 視床皮質

**ディスカッションのトピック**

* Traub のモデルのロジスティック上の問題と既知の修正 [FORTRAN (並列) 対 NEURON (並列) 対 NeuroML 対 MOOSE]
* Traub の論文の結果の再現性
* Traub モデルの欠点/欠陥/更新 - セルレベルとネットワークレベル
* トラウブのモデルは何を教えてくれるでしょうか?
* 直す価値はありますか?
* 詳細なコンパートメント TC 柱状ループをモデル化するための研究関心 [コンパートメント モデリングとスパイキング ニューロン]。
* 優れた TC ループ モデルに関するコンセンサス - ベンチマークの種類。 [その他の既存の代替モデル]
* (任意の) 実験と一致させることはできますか?もしそうならどの種類ですか?

| |**午前のセッション** | |
|:---|:---|:---|
|9:00| [アンガス・シルバー](https://www.opensourcebrain.org/users/6)) |ようこそ |
|9:05| [パドレイグ・グリーソン](https://www.opensourcebrain.org/users/4)) |ハッカソンの紹介と目標; Traub モデル ([スライド](http://www.opensourcebrain.org/attachments/download/117/Hackathon2013_Gleeson_IntroToHachathonAndTraub05.odp)) の紹介 |
|09:30| [マッテオ・カンタレッリ](https://www.opensourcebrain.org/users/43)) | Open Source Brain の最新機能の紹介 ([スライド](http://www.opensourcebrain.org/attachments/download/121/Hackathon2013_Cantarelli_OSBIntro.pdf)) |
|10:00| [チャイタニヤ チンタルリ](https://www.opensourcebrain.org/users/75)) & [ヘレナ・グウォブスカ](https://www.opensourcebrain.org/users/69) |並列 NEURON での Traub モデルの経験 ([ウィキ](http://www.opensourcebrain.org/projects/thalamocortical/wiki/Known_issues)、[スライド](http://www.opensourcebrain.org/attachments/download/123/Hackathon2013_Glabska_NrnTraub.pdf)) |
|10:30| [スバシス・レイ](https://www.opensourcebrain.org/users/39)) | MOOSE の Traub モデルのエクスペリエンス ([ウィキ](http://www.opensourcebrain.org/projects/thalamocortical/wiki/Known_issues)、[スライド](http://www.opensourcebrain.org/attachments/download/122/Hackathon2013_Ray_MooseTraub.pdf)) |
|11:00| | **コーヒーブレイク** |
|11:15| [パドレイグ・グリーソン](https://www.opensourcebrain.org/users/4)) | Traub モデルを NeuroML に変換した経験 ([ウィキ](http://www.opensourcebrain.org/projects/thalamocortical/wiki/Known_issues)、[スライド](http://www.opensourcebrain.org/attachments/download/117/Hackathon2013_Gleeson_IntroToHachathonAndTraub05.odp)) |
|11:45| [リチャード・トムセット](https://www.opensourcebrain.org/users/198)) |縮小細胞モデルを使用した皮質の大規模モデリング ([スライド](http://www.opensourcebrain.org/attachments/download/129/Hackathon2013_Tomsett_CortexModel.ppt)) |
|12:15| [アルンド・ロス](https://www.opensourcebrain.org/users/108)) |錐体ニューロンの縮小モデルの最適化とテスト ([紙](http://senselab.med.yale.edu/modeldb/ShowModel.asp?model=146026)、[スライド](http://www.opensourcebrain.org/attachments/download/119/Hackathon2013_Roth_OptimisingReducedModels.ppt)) |
|12:45| |皮質モデリング ([ウィキ](http://www.opensourcebrain.org/projects/corticalmodelling/wiki/Wiki)) および Traub モデルの問題点 ([ウィキ](http://www.opensourcebrain.org/projects/thalamocortical/wiki/Known_issues)) に関する一般的なディスカッション |
|13:00| | **昼食** |

| |**午後のセッション** | |
|:---|:---|:---|
|14:00| | **ハッキング セッション I**: 互いのモデルのインストール、テスト、文書化。ハイ パフォーマンス コンピューティング インフラストラクチャ上でネットワーク モデルを実行する |
|15:30| | **コーヒーブレイク** |
|15:45| |続き: 皮質モデリングに関する一般的な議論 ([ウィキ](http://www.opensourcebrain.org/projects/corticalmodelling/wiki/Wiki)) と Traub モデルの問題点 ([ウィキ](http://www.opensourcebrain.org/projects/thalamocortical/wiki/Known_issues)|)
|16:15| |優れた TC ループ モデルに関するコンセンサス ([ウィキ](http://www.opensourcebrain.org/projects/corticalmodelling/wiki/Modelling_the_thalamocortical_loop)) |
|17:30| | **今日の終わり** |
|19:30| | **ディナー** |

<a id="thursday-7th-november"></a>
### 11月7日木曜日

全体テーマ：[レイヤー5錐体細胞モデル](http://www.opensourcebrain.org/projects/l5pyramidalcellmodels/wiki)

**ディスカッションのトピック**

* 既存の L5 錐体セル モデルの不一致 - 比較。
* L5Py セルの優れたモデルに関するコンセンサス。
* 単一セルの命名規則のコンセンサス - 互換性とテストに不可欠です。
* 次回会議のマイルストーンと開発に向けた関係者の約束。
* 必須のツールと要件。 [データ共有、相互運用性、テストなど]
* 皮質の「柱状構造」に関する議論 - これが皮質についての正しい考え方なのか?
* 聴覚皮質と体性感覚皮質の比較
* 自動テストツール - 参加状況に応じて隔週テスト。

| |**午前のセッション** | |
|:---|:---|:---|
|9:00| [チャイタニヤ チンタルリ](https://www.opensourcebrain.org/users/75)) & [ヘレナ・グウォブスカ](https://www.opensourcebrain.org/users/69) |プロジェクト:l5bpyrcellhayetal2011 の生物物理特性を Traub モデルに組み込む ([スライド](http://www.opensourcebrain.org/attachments/download/128/Hackathon2013_Chintaluri_HayL5.pdf)) |
|9:30| [マイク・ベラ](https://www.opensourcebrain.org/users/50)) | L5 錐体細胞モデリングと [ニューロチューン](https://github.com/vellamike/neurotune) ([スライド](http://www.opensourcebrain.org/attachments/download/124/Hackathon2013_Vella_ShapeModulation.pdf)) |
|10:00| [サイモン・オコナー](https://www.opensourcebrain.org/users/92)) | Vanier の梨状皮質錐体細胞モデル ([OSBプロジェクト](http://www.opensourcebrain.org/projects/piriformcortexvanier)、[スライド](http://www.opensourcebrain.org/attachments/download/120/Hackathon2013_OConnor_VanierPiriformCortexModel.pptx)) |
| 10:30 | [アンガス・シルバー](https://www.opensourcebrain.org/users/6)) |バックグラウンドネットワーク活動は、L5皮質錐体細胞モデルにおける空間的および時間的統合を拡張します |
|11:00| | **コーヒーブレイク** |
|11:30| | L5 セル モデリングに関する一般的なディスカッション ([ウィキ](http://www.opensourcebrain.org/projects/l5pyramidalcellmodels/wiki)) |
|13:00| | **昼食** |

| |**午後のセッション** | |
|:---|:---|:---|
|14:00| | **ハッキング セッション II**: 錐体細胞モデルのインストール、テスト。モデル最適化のためのパッケージのテスト |
|15:00| |現実的なモデルをテストするためのパイプライン ([ウィキ](http://www.opensourcebrain.org/projects/model-tuning/wiki/Wiki)) |
|15:30| | **コーヒーブレイク** |
|15:45|次のステップ |どのように進めるべきか ([ウィキ](http://www.opensourcebrain.org/projects/corticalmodelling/wiki/Priorities)?) OSB 2014 の計画 |
|17:30| | **会議終了** |

<a id="next-steps"></a>
## 次のステップ

<a id="some-ideassuggestions-for-improving-osb-interface"></a>
### OSB インターフェースを改善するためのいくつかのアイデア/提案

ツリー ビューの横に検索ボックスを追加します ([問題](https://github.com/epiasini/redmine/issues/63))。 [これ](https://github.com/epiasini/redmine/issues/57)に関連する

テーマをより明確にする ([問題](https://github.com/epiasini/redmine/issues/64))

GitHub の問題/スター/フォークへのリンク ([問題](https://github.com/epiasini/redmine/issues/65))

Wiki へのより著名な貢献者のリスト ([問題](https://github.com/epiasini/redmine/issues/66))

<a id="thalamocortical-modelling"></a>
### 視床皮質モデリング

会議で合意された優先事項/アクション ポイントのリストは [ここ](http://www.opensourcebrain.org/projects/corticalmodelling/wiki/Priorities) です。

<a id="practicalities"></a>
## 実用性

会議は UCL のメイン キャンパスで開催されました: http://www.ucl.ac.uk/maps. 両日とも部屋は [フォスターコート 243](http://www.ucl.ac.uk/estates/roombooking/building-location/?id=040) でした。

近隣の宿泊施設のご提案:
http://www.gowerhousehotel.co.uk
http://www.jenkinshotel.demon.co.uk

<a id="enquiries"></a>
## お問い合わせ

このミーティングに関するご質問がございましたら、お気軽に [p.gleeson@ucl.ac.uk](mailto:p.gleeson@ucl.ac.uk) までご連絡ください。
</section>

</article>
</main>
