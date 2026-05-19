---
layout: default
title: "OpenSourceBrain Documentation: よくある質問 (FAQ)"
description: "OpenSourceBrain/Documentation: source/General/FAQ.md の日本語訳"
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
<p>原典: <a href="https://github.com/OpenSourceBrain/Documentation/blob/main/source/General/FAQ.md" target="_blank" rel="noopener noreferrer">https://github.com/OpenSourceBrain/Documentation/blob/main/source/General/FAQ.md</a></p>
<p>ライセンス: CC BY 4.0。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
<a id="faq"></a>
<a id="frequently-asked-questions-faq"></a>
# よくある質問 (FAQ)

<a id="faq:motivation"></a>
<a id="what-is-the-motivation-behind-the-open-source-brain-repository"></a>
## オープンソース Brain リポジトリの背後にある動機は何ですか?

調査対象のシステム (例: [モデルDB](http://senselab.med.yale.edu/ModelDB/default.asp*)) の解剖学的および電気生理学的特性に関する最新データをカプセル化した、さまざまな脳領域からの詳細な単一ニューロンおよびネットワーク モデルの数が増えています。これらの複雑なモデルは開発に長い時間がかかり、通常は多くの互換性のないシミュレータ固有の形式のうちの 1 つでしか利用できません。

Open Source Brain リポジトリ (OSB) は、標準化された形式の詳細なニューロン モデルの公開リポジトリであり、新しい実験結果、最新のモデリング パラダイム、シミュレータ テクノロジの開発に合わせて進化する厳選された安定リリースが含まれます。バグの修正、新機能の追加、公開モデルのドキュメントの改善を通じて、誰でも OSB 上のモデルに貢献できます。

モデルは任意のシミュレータ形式で共同開発できますが、最終的な目的は、モジュール性、アクセシビリティ、シミュレータ間での移植性を確保し、ブラウザ内での視覚化、分析、シミュレーションを可能にするために、可能な限り多くのモデルを [ニューロML](http://www.neuroml.org) や [ぴんん](http://neuralensemble.org/PyNN) などのシミュレータに依存しない形式に変換することです。

![NeuroML ロゴ](https://docs.neuroml.org/_static/logo.png)


<a id="which-version-of-osb-should-i-use"></a>
## OSB のどのバージョンを使用すればよいですか?

私たちは OSB プラットフォームのバージョン 2 を積極的に開発しています。さまざまなバージョンの機能については、[ここ](/external/opensourcebrain/documentation/source/General/GettingStarted.html#getting_started_osb) を参照してください。


<a id="faq:funding"></a>
<a id="whos-behind-osb"></a>
## OSB の背後にいるのは誰ですか?

このプロジェクトは、計算神経科学におけるモデルの共同開発を促進するために、[ようこそ](http://www.wellcome.ac.uk) 資金提供プロジェクトの一環として、UCL の [シルバーラボ](http://silverlab.org) で開始されました。

![ようこそ](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/wtlogo.png)

OSB プロジェクトの主任研究者は [アンガス・シルバー](https://www.opensourcebrain.org/users/6) です。
UCL のコア チームは現在、[パドレイグ・グリーソン](https://www.opensourcebrain.org/users/4) (プロジェクト マネージャー) と [アンクール・シンハ](https://www.opensourcebrain.org/users/434) で構成されています。
UCL 在籍中に OSB に多大な貢献をしてくれた [マッテオ・カンタレッリ](https://www.opensourcebrain.org/users/43)、[エイドリアン・キンタン](https://www.opensourcebrain.org/users311)、[マット・アーンショー](https://www.opensourcebrain.orgusers/751)、[ボリス・マリン](https://www.opensourcebrain.org/users/67)、[エウジェニオ・ピアジーニ](https://www.opensourcebrain.org/users/3)、および [メタセル](https://www.metacell.us/) のチームに感謝します。

私たちは、Open Source Brain プラットフォームで利用可能なモデルとデータを開発、保守、提供してくださっている科学コミュニティに感謝しています。
個々のリポジトリで個々のプロジェクトの貢献者を確認できます。

多くの国際的な研究グループや組織が Open Source Brain Initiative に積極的に参加しています。
詳細については、[ここ](https://www.opensourcebrain.org/about) を参照してください。


<a id="faq:neuroinformatics"></a>
<a id="how-is-this-related-to-other-neuroinformatics-initiatives"></a>
## これは他の神経情報学の取り組みとどのように関連していますか?

私たちは、神経情報学および計算神経科学に関する他のデータベースやリポジトリと緊密に連携することに非常に熱心です。
これらの多くは、[NeuroMorpho.org](http://neuromorpho.org/neuroMorpho/index.jsp) や他の多くのツールやリソースで使用されているような NeuroML の共通使用を通じて有効になります。
[ニューラルアンサンブル](http://neuralensemble.org) は、OSB 内のモデルのシミュレーションと分析において重要な役割を果たす多数のソフトウェア ツールをホストします。

また、オリジナルのモデル スクリプト用の [モデルDB](http://senselab.med.yale.edu/modeldb) やモデル コンポーネントの定義用の [NIF/ニューロレックス](https://www.opensourcebrain.org/projects/nifshowcase) などのデータベースへのディープ リンクも計画しています。

他のニューロインフォマティクス リソースとの対話の詳細については、[ここ](http://www.opensourcebrain.org/projects/neuroinformatics/wiki/Wiki) を参照してください。

この取り組みへの貢献者の多くは、[INCF](http://www.incf.org) のさまざまな国内ノードに関与しています。

![INCF](https://raw.githubusercontent.com/OpenSourceBrain/Documentation/main/source/images/incf.png)

<a id="faq:modeltypes"></a>
<a id="what-types-of-models-can-be-developed"></a>
## どのようなタイプのモデルを開発できますか?

神経系における情報処理のモデルは、認知プロセスと意識の高レベル モデルからシナプスでの信号伝達の低レベル モデルに至るまで、さまざまなレベルで作成されます。
短期から中期的には、**OSB はスパイク ニューロン モデル**、つまり、標的細胞上のシナプスにイベントを送信することで通信する個々のニューロンのネットワークに焦点を当てます。
OSB で現在開発中のモデルのコア セットは、(多くの場合マルチコンパートメントの) ニューロンのコンダクタンス ベースのモデルです。
このクラスのニューロン モデルは、チャネルとシナプスのモデル、または細胞全体のモデルが研究間で再利用されることが多く、モデル自体が複雑なソフトウェア エンティティであるため、共同開発に特に適しています。
[NeuroML v1.x](http://www.neuroml.org/introduction.php) はこのタイプのモデルに焦点を当てていましたが、[バージョン2.0](http://www.neuroml.org/neuroml2.php) では、サポートがより抽象的なニューロン モデル (リーキー積分と発火、適応閾値モデルなど) に拡張されました。

モデル コンポーネントを NeuroML に変換することは、モデルの透明性とアクセシビリティを高め、複数のシミュレーターで使用できるようにするための重要なステップですが、モデルの移植性を支援するために他のクロスプラットフォーム テクノロジが使用されます。
Python は計算神経科学で一般的に使用されるスクリプト言語であり、OSB モデルの多くのターゲット シミュレーターで採用されています。
[ぴんん](http://neuralensemble.org/PyNN) は、ニューロン ネットワーク モデルをシミュレータに依存せずに仕様化するための Python パッケージであり、複雑なネットワーク構造の手続き型仕様に役立ちます。
シミュレーション実験記述マークアップ言語 ([SED-ML](http://sed-ml.org/)) は、モデルのシミュレーションを実行するための設定を指定するために使用されます。
OSB のモデル コンポーネントから計算生物学の他の構造化言語へのマッピング ([SBML](http://www.sbml.org)、[CellML](http://www.cellml.org/)、[ナインML](http://software.incf.org/software/nineml) など) も必要に応じてサポートされます。

<a id="faq:simulatorX"></a>
<a id="my-models-only-available-in-simulator-x-not-neuromlpynn-can-i-still-share-it-on-osb"></a>
## 私のモデルはシミュレーター X でのみ利用可能であり、NeuroML/PyNN では利用できません。 OSB で共有できますか?

はい！
**モデルが既に公開されている場合は、まず [モデルDB](http://senselab.med.yale.edu/modeldb) に送信してください**。
OSB では、任意の形式のコードの最新バージョンを含むパブリック リポジトリを喜んで参照し、ModelDB 上のバージョンへのリンクを用意しています。
ただし、OSB の高度な機能の一部は、モデル (の一部) が NeuroML に変換された場合にのみ利用可能になります。

あなたのモデルがまだ公開されていないものの、まだ公開されている場合 (よろしくお願いします。あなたは [未来](http://www.openworm.org) です)、私たちはそれを喜んで入手しますが、公開で使用されているバージョンが ModelDB にアーカイブされていることを確認するようお願いします。


<a id="faq:registration"></a>
<a id="do-i-have-to-be-registered-for-accessing-osb-projects-and-tools"></a>
## OSB プロジェクトやツールにアクセスするには登録する必要がありますか?

いいえ。
OSB プロジェクトを参照し、ほとんどの OSB ツールを使用できます。
ただし、独自のプロジェクトを作成したい場合は、サインアップする必要があります。
また、OSB インターフェイスを介して独自のシミュレーションを実行および再生するための新機能は、ログインしたユーザーのみが利用できます。

<a id="faq:license"></a>
<a id="what-is-the-licenceterms-of-use-for-models-on-osb"></a>
## OSB 上のモデルのライセンス/使用条件は何ですか?

OSB 上のモデルのすべてのスクリプトは自律リポジトリ (GitHub など) に存在するため、各リポジトリには独自のライセンス情報を含めることができます (また、含めるべきです)。
残念ながら、これは OSB 上のほとんどのリポジトリには当てはまりません (これは科学ソフトウェア開発においてより広範な問題です)。
それにもかかわらず、ヒントはタイトルにあります...**オープンソース** Brain にモデルを配置するユーザーは、おそらくそれを広く使用して再利用してもらいたいと考えています。
ただし、疑問があり、確実に確認したい場合は、問題のリポジトリで問題をオープンし (または [info@opensourcebrain.org](mailto:info@opensourcebrain.org) にメールで)、リポジトリにライセンス情報を追加するようリクエストしてください。

ただし、黄金律を忘れないでください (科学者にとってソフトウェア ライセンスよりも重要です...): **モデルを使用する場合は、そのモデルについて説明している元の出版物を参照してください**。
OSB リポジトリに引用したい元のモデルからの大幅な変更がある場合、モデルの特定のバージョンの DOI/リファレンスを生成できます (例: [ここ](https://zenodo.org/communities/opensourcebrain/?page=1&size=20))。

<a id="faq:contribute"></a>
<a id="how-can-i-contribute"></a>
## どうすれば貢献できるでしょうか?

この取り組みにご協力いただける方からのご連絡をお待ちしております。
私たちは特に、計算神経科学のモデラーやソフトウェア開発者に参加してもらいたいと考えています。

**OSB (および関連する NeuroML ツール) には、ボランティアの助けを必要とするプロジェクトの中心的なリストがあります。 [詳細はこのページ](#contribute) を参照してください。**

プロジェクトまたは [連絡する](/external/opensourcebrain/documentation/source/General/Contacts.html#contact) をフォローするすべての方法を確認してください。
</section>

</article>
</main>
