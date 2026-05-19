---
layout: default
title: "NetPyNE docs: NetPyNE<a href=\"#about-netpyne\" class=\"headerlink\" title=\"Link to this heading\"></a> について"
description: "NetPyNE docs: about.md の日本語訳"
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
<p>原典: <a href="http://doc.netpyne.org/about.html" target="_blank" rel="noopener noreferrer">http://doc.netpyne.org/about.html</a></p>
<p>ライセンス: MIT License for NetPyNE repository documentation/code。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
<div class="document" role="main" itemscope="itemscope" itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="about-netpyne" class="section">

# NetPyNE<a href="#about-netpyne" class="headerlink" title="Link to this heading"></a> について

NetPyNE (**Net**works using **Py**thon and **NE**URON) は、NEURON シミュレーターを使用した生物学的ニューロン ネットワークの開発、シミュレーション、並列化、分析、最適化を容易にする Python パッケージです。

NEURON はすでに分子レベルからネットワーク レベルに至るマルチスケール シミュレーションを可能にしていますが、ネットワーク シミュレーションに NEURON を使用するには大幅なプログラミングが必要で、多くの場合、並列シミュレーションが必要になります。 NetPyNE は、学生や実験者にとって、NEURON での生物学的ニューロン ネットワークの開発と並列シミュレーションを大幅に容易にします。 NetPyNE は経験豊富なモデラーも対象としており、複雑な解剖学的および生理学的データをモデルに組み込むための強力な機能を提供します。

NetPyNE の詳細な概要については、以下を参照してください。

- ジャーナル <a href="https://elifesciences.org/" class="reference external">eLife</a> の <a href="https://elifesciences.org/articles/44494" class="reference external">NetPyNE 記事</a>

- <a href="http://dura-bernal.org/netpyne-online-tutorial-2022" class="reference external">NetPyNE チュートリアル<a href="https://www.cnsorg.org/cns-2022" class="reference external">CNS*2022</a> からの </a>

<div class="line">

\

</div>

<a href="_images/schematic.png" class="reference internal image-reference"><img src="_images/schematic.png" class="align-center" style="width: 95%;" alt="_images/schematic.png" /></a>

<div class="line">

\

</div>

<div id="major-features" class="section">

## 主な特長<a href="#major-features" class="headerlink" title="Link to this heading"></a>

- **一連の高レベルの仕様を NEURON ネットワーク モデルに変換します**

- **仕様は、シンプルで標準化された宣言型の Python ベースの形式で提供されます**

- **簡単に定義できます:**

> <div>
  >
  > - *集団*: 細胞の種類とモデル、ニューロンの数または密度、空間範囲など
  >
  > - *細胞の特性*: 形態、生物物理学、実装など
  >
  > - *シナプスのメカニズム*: 時定数、逆転の可能性、実装など
  >
  > - *刺激*: スパイク ジェネレーター、電流クランプ、時空間特性など
  >
  > - *接続ルール*: シナプス前細胞とシナプス後細胞の状態、異なる機能、…
  >
  > - *シミュレーション構成*: 期間、保存と分析、グラフィック出力など
  >
  > - *反応拡散 (RxD)*: 種、領域、反応など
  >
  > </div>

- **セルのプロパティのハイライト:**

> <div>
  >
  > - 既存の HOC および Python で定義されたセル モデルを NetPyNE 形式にインポートします
  >
  > - モデルの実装を *例* ホジキン・ハクスリー マルチコンパートメントからイジケビッチ ポイント ニューロンに簡単に変更
  >
  > - 複数のセル モデルをハイブリッド ネットワークに結合して効率的な大規模ネットワークを実現
  >
  > </div>

- **接続ルールのハイライト:**

> <div>
  >
  > - シナプス前およびシナプス後の細胞特性 (*例* 細胞の種類や位置) に基づいた柔軟な接続ルール
  >
  > - 利用可能な接続関数: 全対全、確率的、収束的、発散的、および明示的なリスト
  >
  > - シナプス前後の空間特性の関数としてパラメーター (*例* 重み、確率、遅延) を指定できます。*例* 細胞間の距離や皮質深さに依存する遅延や確率など
  >
  > - 樹状突起に沿ったシナプスの細胞内分布を指定でき、各モデル ニューロンの形態に自動的に適応されます。
  >
  > - STDP や強化学習などの学習メカニズムをシナプスに簡単に追加できる
  >
  > </div>

- **MPI 並列シミュレーションの準備が整った NEURON ネットワーク インスタンスを生成します**

> <div>
  >
  > - セルの分布を管理します
  >
  > - データの収集を処理します
  >
  > </div>

- **ネットワークとシミュレーション出力の分析とプロット:**

> <div>
  >
  > - すべての細胞または集団のラスター プロット
  >
  > - すべての細胞、集団、または単一細胞のスパイク ヒストグラム
  >
  > - 固有のセル変数プロット (電圧、電流、コンダクタンス)
  >
  > - ローカルフィールドポテンシャル（LFP）の計算とプロット（時間分解スペクトルとパワースペクトル）
  >
  > - 細胞または集団レベルでの接続性行列 (重み、接続数、効率、確率など)
  >
  > - ネットワークセルの位置と接続の 2D 表現
  >
  > - 色分けされた変数 (シナプスの数など) を含めるオプションを備えた 3D 形状プロット
  >
  > - 正規化された伝達エントロピーとスペクトル グレンジャーの因果関係
  >
  > </div>

- **データ共有を容易にする:**

> <div>
  >
  > - 高レベルの仕様、ネットワーク インスタンス、シミュレーション構成、シミュレーション結果を保存/ロードできます。
  >
  > - 複数の形式をサポート: pickle、Matlab、JSON、CSV、HDF5
  >
  > - ニューラル モデルの標準化形式である NeuroML および SONATA へのエクスポート/インポートが可能
  >
  > </div>

- **バッチ シミュレーション:**

> <div>
  >
  > - バッチ シミュレーションで探索するパラメータと値の範囲を簡単に指定
  >
  > - マルチコア マシン (掲示板) またはスーパーコンピューター (SLURM または PBS Torque) でジョブを自動的に送信するための事前定義された構成可能なセットアップ
  >
  > - 多次元バッチシミュレーション結果の分析と視覚化
  >
  > </div>

- **現在の使用状況:**

> <div>
  >
  > - さまざまな脳領域および現象のモデルを開発するために使用されます。 \[モデルの完全なリスト\](www.netpyne.org/models) を参照
  >
  > - <a href="https://hnn.brown.edu/" class="reference external">Human Neocortical Neurosolver</a> と統合して、皮質モデルに柔軟性を追加
  >
  > - NeuroML ベースの NEURON モデルの並列シミュレーションを実行するために <a href="www.opensourcebrain.org" class="reference external">Open Source Brain</a> によって使用されます
  >
  > - <a href="www.nsgportal.org" class="reference external">Neuroscience Gateway</a> を介して XSEDE スーパーコンピューターでシミュレーションを実行できます
  >
  > </div>

</div>

<div id="questions-suggestions-and-contributions" class="section">

## 質問、提案、貢献<a href="#questions-suggestions-and-contributions" class="headerlink" title="Link to this heading"></a>

2 種類の貢献が求められます。 1. 以下に説明する NetPyNE コードへの直接の貢献。 2. <a href="contrib.html" class="reference external">補助コードの貢献</a>。

NetPyNE はオープンソースであり、<a href="https://github.com/Neurosim-lab/netpyne" class="reference external">github.com/Neurosim-lab/netpyne</a> から入手できます。

質問や提案がある場合は、<a href="https://groups.google.com/forum/#!forum/netpyne-forum" class="reference external">NetPyNE フォーラム</a> 、<a href="https://www.neuron.yale.edu/phpBB/viewforum.php?f=45" class="reference external">NEURON+NetPyNE フォーラム</a> または <a href="https://github.com/Neurosim-lab/netpyne/issues" class="reference external">GitHub</a> に問題を送信してください。

貢献は大歓迎です!リポジトリをフォークし、変更を加えてプル リクエストを作成してください。詳細については、<a href="https://github.com/Neurosim-lab/netpyne/blob/development/CONTRIBUTING.md" class="reference external">寄稿者ガイド</a>を参照してください。

詳細については、<a href="mailto:salvadordura%40gmail.com" class="reference external">salvadordura<span>@</span>gmail<span>.</span>com</a> までお問い合わせください。

</div>

<div id="code-of-conduct" class="section">

<span id="id1"></span>

## 行動規範<a href="#code-of-conduct" class="headerlink" title="Link to this heading"></a>

このプロジェクトは、貢献者の行動規範とともにリリースされています。このプロジェクトに参加すると、その規約に従うことに同意したことになります。

私たちはメンバー、貢献者、リーダーとして、年齢、体の大きさ、目に見える障害の有無、民族性、性的特徴、性自認と性表現、経験のレベル、教育、社会経済的地位、国籍、外見、人種、宗教、または性的自認と性的指向に関係なく、すべての人にとってハラスメントのないコミュニティへの参加を実現することを誓約します。

私たちは、オープンで、歓迎的で、多様性があり、包括的で健全なコミュニティに貢献する方法で行動し、交流することを誓います。

<a href="https://github.com/Neurosim-lab/netpyne/blob/development/CODE_OF_CONDUCT.md" class="reference external">行動規範</a> の全文をお読みください。

</div>

<div id="publications" class="section">

## 出版物<a href="#publications" class="headerlink" title="Link to this heading"></a>

<div id="id3" class="section">

### NetPyNE<a href="#id3" class="headerlink" title="Link to this heading"></a> について

- デュラ・ベルナル S、スーター B、グリーソン P、カンタレッリ M、キンタナ A、ロドリゲス F、ケジオラ DJ、チャダードン GL、カー CC、ネイモティン SA、マクドゥガル R、ハインズ M、シェパード GMG、リットン WW。 **NetPyNE: 脳回路のデータ駆動型マルチスケール モデリングのためのツール。** <a href="https://elifesciences.org/articles/44494" class="reference external">eLife 2019;8:e44494</a> 、 *2019.*

- リットン WW、ザイデンシュタイン AH、デュラ ベルナル S、マクドゥガル RA、シュールマン F、ハインズ ML。 **脳研究を前進させるためのシミュレーション ニューロテクノロジー: NEURON での大規模ネットワークの並列化。** *ニューラル コンピューティング、2016 年。*

- デュラ・ベルナル S、スーター BA、キンタナ A、カンタレッリ M、グリーソン P、ロドリゲス F、ネイモティン SA、ハインズ M、シェパード GMG、リットン WW。 **NetPyNE: 大規模なデータ駆動型ネットワーク モデルを並行して構築、シミュレーション、分析するための GUI ベースのツール NEURON。** *Society for Neuroscience (SfN)、2018*。

- デュラ・ベルナル S、スーター BA、ネイモティン SA、シェパード GMG、リットン WW。 **皮質微小回路におけるシナプス接続の細胞内分布のモデル化。** *神経科学協会 (SFN)、2016*。

- デュラ・ベルナル S、スーター BA、ネイモティン SA、カー CC、キンタナ A、グリーソン P、シェパード GMG、リットン WW。 **NetPyNE: 生物学的ニューロン ネットワークの開発と並列シミュレーションを容易にする NEURON 用の Python パッケージ** *計算神経科学 (CNS)、2016 年*

- グリーソン P、マリン B、サデー S、キンタナ A、カンタレッリ M、デュラ ベルナル S、リットン WW、デイヴィソン A、シルバー RA。 **オープンソース脳上の複数のスケールで厳選された皮質モデルのセット。** *計算神経科学 (CNS)、2016*。

- デュラ・ベルナル S、スーター BA、ネイモティン SA、キンタナ AJ、グリーソン P、シェパード GMG、リットン WW。 **皮質における細胞接続性の一次座標系としての正規化皮質深さ (NCD): 実験とモデル。** *神経科学協会 (SFN)、2015。*

</div>

<div id="make-use-of-netpyne" class="section">

### NetPyNE<a href="#make-use-of-netpyne" class="headerlink" title="Link to this heading"></a> を利用する

- テラ、H.d.C.B.、ボルヘス、F.d.S.、モラエス、MF.D.、コタ、V.R. **NEURON シミュレータ用の細胞内および細胞外の非周期的スケールフリー刺激のコンピュータでの実装。**Communications in Computer and Information Science、vol 1519。Springer、Cham。 *2021年*。ドイ:<a href="https://doi.org/10.1007/978-3-031-08443-0_8" class="reference external">https://doi.org/10.1007/978-3-031-08443-0_8</a>

- Ying Y、Yubo F、Songan H、Qingyun W. **一次運動野の光遺伝学的刺激は大脳基底核のベータ振動を調節する: 計算による研究** 非線形科学と数値シミュレーションにおけるコミュニケーション、第 117 巻。*2023*。ドイ:<a href="https://doi.org/10.1016/j.cnsns.2022.106918" class="reference external">https://doi.org/10.1016/j.cnsns.2022.106918</a>

- ハセガン D、デイブル M、アール C、ドノフリオ D、ハザン H、アンワル H、ネイモティン SA。 **マルチタイムスケールの生物学的学習アルゴリズムは、スパイキング ニューロン ネットワークの運動制御をトレーニングします** bioRxiv 2021.11.20.469405、*2021*。土井: <a href="https://doi.org/10.1101/2021.11.20.469405" class="reference external">https://doi.org/10.1101/2021.11.20.469405</a>.

- ブライソン A、バーコビッチ SF、ペトルー S、グレイデン DB。 **皮質ネットワーク モデルにおける抑制性介在ニューロンを介した状態遷移。** PLoS Comput Biol 17(10): e1009521、*2021*。土井: <a href="https://doi.org/10.1371/journal.pcbi.1009521" class="reference external">https://doi.org/10.1371/journal.pcbi.1009521</a>.

- ピメンテル1 JM、モイオリRC、デ・アラウホMFP、ラニエリCM、ロメロRAF、ブロズF、バルガスPA。 **Neuro4PD: パーキンソン病の初期ニューロボティクス モデル。** 正面。ニューロロボット。 15:640449、*2021*。土井：<a href="10.3389/fnbot.2021.640449" class="reference external">10.3389/fnbot.2021.640449</a>。

- ヴォルク、V.L.、ハミルトン、LD、ヒューム、DR他。 **神経筋骨格モデリングを改善するための有限要素フレームワーク内での神経アーキテクチャの統合。** Scientific Reports 11、22983、*2021*。土井: <a href="https://doi.org/10.1038/s41598-021-02298-9" class="reference external">https://doi.org/10.1038/s41598-021-02298-9</a>.

- ラニエリ CM、モイオリ RC、バルガス P、ロメロ RAF、**人間活動認識に基づく行動選択へのニューロロボティクス アプローチ**、arXiv:2107.12540 \[cs.RO\]、*2021*。 <a href="https://arxiv.org/abs/2107.12536" class="reference external">https://arxiv.org/abs/2107.12536</a>.

- Ranieri CM、Pimentel JM、Romano MR、Elias LA、Romero RAF、Lones MA、Araujo MFP、Vargas PA、Moioli RC、**マーモセット サルに基づくパーキンソン病のデータ駆動型生物物理計算モデル**、IEEE Access、vol. 9、122548-122567ページ、*2021*。土井: <a href="https://doi.org/10.1109/ACCESS.2021.3108682" class="reference external">https://doi.org/10.1109/ACCESS.2021.3108682</a>.

- Metzner C、Mäki-Marttunen T、Karni G、McMahon-Cole H、Steuber V. **ガンマ帯振動に対する統合失調症関連遺伝子の変化の影響**、bioRxiv 2020.09.28.316737、*2020*。土井: <a href="https://doi.org/10.1101/2020.09.28.316737" class="reference external">https://doi.org/10.1101/2020.09.28.316737</a>.

- Gao P、Graham J、Zhou W、Jang J、Angulo S、Dura-Bernal S、Hines ML、Lytton WW、Antic S **局所グルタミン酸媒介樹状プラトー電位は皮質錐体ニューロンの状態を変化させる**、Journal of Neurophysiology (出版中)。 *2020年*。

- Sivagnanam S、Gorman W、Doherty D、Neymotin S、Hovhannisyan H、Fang S、Lytton W、Dura-Bernal S **Google Cloud Platform を使用した脳神経回路の大規模モデルのシミュレーション**、先端研究コンピューティングの実践と経験、PEARC2020、*2020*。

- Neymotin, S.A.、Daniels, D.S.、Caldwell, B.、McDougal, R.A.、Carnevale, N.T.、Jas, M.、Moore, C.I.、Hines, M.L.、Hamalainen, M.、および Jones, S.R.、 **Human Neocortical Neurosolver (HNN)、ヒト MEG/EEG の細胞およびネットワーク起源を解釈するための新しいソフトウェア ツールデータ**、eLife、9、p.e51214、*2020*。ドイ: <a href="https://elifesciences.org/articles/51214" class="reference external">https://elifesciences.org/articles/51214</a> 。

- Lytton WW、Sherif MA、Dura-Bernal S、Neymotin S. **「精神」疾患のマルチスケール モデリング**、仮想生理学的人間カンファレンス、VHP2020、*2020*。

- デュラベルナル S、ネイモティン SA、スーター BA、シェパード GMG、リットン WW。 **一次運動野微小回路のデータ駆動型モデルにおけるマルチスケールのダイナミクスと情報の流れ**、bioRxiv 201707、*2019*。土井: <a href="https://www.biorxiv.org/content/10.1101/201707v3" class="reference external">https://www.biorxiv.org/content/10.1101/201707v3</a>.

- Gerkin, R.C.、Birgiolas, J.、Jarvis, R.J.、Omar, C.、Crook, S.M.. **NeuronUnit: SciUnit を使用したニューロン モデルのデータ駆動型検証用パッケージ**、bioRxiv、p.665331、*2019*。

- グリーソン P、カンタレッリ M、キンタナ A、アーンサー M、ピアジーニ E、ビルジオラス J、キャノン RC、ケイコ-ガジック A、クルック S、デイヴィソン AP、デュラ-ベルナル S、他。 **Open Source Brain: ニューロンと回路の標準化モデルを視覚化、分析、シミュレーション、開発するための共同リソース**、Neuron、10.1016/j.neuron.2019.05.019、*2019*。ドイ: <a href="https://www.cell.com/neuron/fulltext/S0896-6273(19)30444-1" class="reference external">https://www.cell.com/neuron/fulltext/S0896-6273(19)30444-1</a>。

- Dai K、Hernando J、Billeh JN、Gratiy SL、Planas J、Davison AP、Dura-Bernal S、Gleeson P、Devesse A、Gevaert M、King JG、Van Geit WAH、Povolotsky AV、Muller E、Courcol J-D、Arkhipov A 。 **大規模ネットワーク モデルの効率的な記述のための SONATA データ形式**、bioRxiv、625491 \[Preprint\] doi: <a href="https://www.biorxiv.org/content/10.1101/625491v2" class="reference external">https://www.biorxiv.org/content/10.1101/625491v2</a>. *PLoS Computational Biology で検討中。 2019年*

- Dura-Bernal S、Neymotin SA、Suter BA、Shepherd GMG、Lytton WW **長距離入力と H 電流は、マウス M1 微細回路のマルチスケール モデルにおけるさまざまな動作モードを制御します**、bioRxiv 201707、*2018*。土井: <a href="https://www.biorxiv.org/content/10.1101/201707v3" class="reference external">https://www.biorxiv.org/content/10.1101/201707v3</a>.

学位論文:

- Volk, V. **神経変性状態のメカニズムと治療を調査するための有限要素フレームワーク内の統合神経筋骨格モデリング**、*ボイシ州立大学、2022*。

カンファレンスの要約:

- デュラ・バーナル S、グリフィス EY、バルザック A、オコネル ミネソタ、マクギニス T、アンワー H、リットン WW、ラカトス P、ネイモティン SA。 **マカクの聴覚視床皮質回路の生物物理学的に詳細なマルチスケール モデルは生理学的振動を再現します。** *Computational Neurosience (CNS)、2020*。

- グリフィス EY、デュラ バーナル S、バルザック A、オコネル ミネソタ、マクギニス TM、リットン WW、ラカトス P、ネイモティン SA。 **聴覚視床皮質系リズムのデータ駆動型モデル。** *神経科学学会 (SfN)、2019*。

- ドハーティ DW、デュラ・バーナル S、リットン WW。 **マウス領域 M1 のコンピューター モデルは、層または細胞の種類によって定義された完全なモデルとサブサーキットの雪崩を示しています。** *神経科学協会 (SfN)、2019*。

- デュラ・ベルナル S、メンジーズ RS、マクロークラン C、ファン アルバダ SJ、ケジオラ DJ、ネイモティン SA、リットン WW、カー CC。 **計算能力に対するネットワーク サイズの影響。** *計算神経科学 (CNS)、2016*。

- ロマロ C、アラウホ ナジマン F、デュラ ベルナル S、ロケ AC。 **再スケーリング オプションを備えた NetPyNE/NEURON への Potjans-Diesmann 皮質微小回路モデルの実装。** *Computational Neuroscience (CNS)、2018*。

- ロドリゲス F. **歯状回ネットワーク モデル** *計算神経科学 (CNS)、2018*。

</div>

<div id="cite-netpyne" class="section">

### NetPyNE<a href="#cite-netpyne" class="headerlink" title="Link to this heading"></a> を引用します

- Spreizer S、Senk J、Rotter S、Diesmann M、Weyers、**NEST デスクトップ、神経科学のための教育アプリケーション** eNeuro 2021 年 11 月 11 日、8 (6) ENEURO.0274-21.2021、*2021*。土井: <a href="http://doi.org/10.1523/ENEURO.0274-21.2021" class="reference external">http://doi.org/10.1523/ENEURO.0274-21.2021</a>.

- Amsalem, O.、Eyal, G.、Rogozinski, N.、Gevaert, M.、Kumbhar, P.、Schürmann, F.、および Segev, I.、**詳細な非線形ニューロン モデルの効率的な分析的削減** Nature Communications、11(1)、pp.1-13、*2020*。土井: <a href="https://www.nature.com/articles/s41467-019-13932-6" class="reference external">https://www.nature.com/articles/s41467-019-13932-6</a>.

- Billeh、Y.N.、Cai、B.、Gratiy、S.L.、Dai、K.、Iyer、R.、Gouwens、N.W.、Abbasi-Asl、R.、Jia、X.、Siegle、J.H.、Olsen、S.R.そしてコッホ、C.、 **マウス一次視覚野のマルチスケールモデルへの構造データと機能データの体系的な統合。** Neuron (プレス中) NEURON-D-19-01027、*2020*。土井: <a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3416643" class="reference external">https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3416643</a>.

- Tran, H.、Ranta, R.、Le Cam, S.、および Louis-Dorr, V.、**形態学的フィルタリング近似に基づく細胞外活動電位シグネチャの高速シミュレーション** Journal of Computational Neuroscience、pp.1-20、*2020*。土井: <a href="https://doi.org/10.1007/s10827-019-00735-3" class="reference external">https://doi.org/10.1007/s10827-019-00735-3</a>.

- Gast, R.、Rose, D.、Salomon, C.、Möller, H.E.、Weiskopf, N.、および Knösche, T.R.. **PyRates—レートベースのニューラル シミュレーション用の Python フレームワーク。** PLoS ONE、14(12)、*2019*。土井: <a href="https://doi.org/10.1371/journal.pone.0225900" class="reference external">https://doi.org/10.1371/journal.pone.0225900</a>.

- Tejada J、Roque AC、**コンダクタンスベースのモデルと断片化問題: 海馬 CA1 錐体細胞モデルとてんかんに基づくケーススタディ** Epilepsy & Behavior、106841、*2019*。土井: <a href="https://doi.org/10.1016/j.yebeh.2019.106841" class="reference external">https://doi.org/10.1016/j.yebeh.2019.106841</a>.

- Kuhl E、Alber M、Tepole BA、Cannon WR、De S、Dura-Bernal S、Garikipati K、Karniadakis GE、Lytton WW、Perdicaris P、Petzold L. **マルチスケール モデリングと機械学習の出会い: 何が学べるでしょうか?** arXiv:1911.11958。ドイ: <a href="https://doi.org/10.1007/s11831-020-09405-5" class="reference external">https://doi.org/10.1007/s11831-020-09405-5</a>. \[プレプリント\]。 *応用力学および工学におけるコンピュータ手法で検討中。 2019年*

- Alber M、Buganza A、Cannon W、De S、Dura-Bernal S、Garikipati K、Karmaadakis G、Lytton W、Perdicaris P、Petzold L、Kuhl E. **機械学習とマルチスケール モデリングの統合: 生物学、生物医学、および行動科学における展望、課題、機会。** Nature Partner Journals (npj) Digital Medicine、2、 115、*2019*。土井: <a href="https://www.nature.com/articles/s41746-019-0193-y" class="reference external">https://www.nature.com/articles/s41746-019-0193-y</a>.

ここでは、Google Scholar</a> の <a href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=17032431079400790910&amp;as_sdt=5" class="reference external">更新されたリストを参照してください。

</div>

</div>

<div id="courses" class="section">

## コース<a href="#courses" class="headerlink" title="Link to this heading"></a>

<div id="future" class="section">

### 将来<a href="#future" class="headerlink" title="Link to this heading"></a>

- 2022 年 6 月: Google Cloud、Google Office、ニューヨークでの脳回路モデルの構築とシミュレーション (遅延)

</div>

<div id="past" class="section">

### 過去<a href="#past" class="headerlink" title="Link to this heading"></a>

- 2020 年 12 月 1: Minicurso - Modelagem Computacional em NetPyNE usand Google Cloud Platform - Simpósio do PPGNCG (ポルトガル語のブラジル語コース)

- 2021 年 7 月: CNS’21 NEURON と NetPyNE を使用して、分子からネットワークまで生物物理学的に詳細なニューロン モデルを構築します。

- 2021 年 5 月: オンライン 2 週間コース: NetPyNE を使用した脳回路のマルチスケール モデリング。

- 2020 年 7 月: <a href="https://www.cnsorg.org/cns-2020" class="reference external">CNS*2020</a> 機構マルチスケール モデルの構築: NEURON と NetPyNE を使用した分子からネットワークまで、オンライン カンファレンス

- 2020 年 1 月: VIII Latin American School on Computational Neuroscience (LASCON)、サンパウロ大学数学統計研究所、ブラジル

- 2019 年 7 月: CNS\*2019 チュートリアルの主催者および講師、生物物理学的に詳細なニューロン モデルの構築: 分子からネットワークまで、バルセロナ。

- 2019 年 5 月: マルチスケール ネットワーク モデリングに関するワークショップ、ブラウン大学。

- 2019 年 5 月: 計算神経科学の原理、サルデーニャのサッサリ大学。

- 2018 年 6 月: NEURON 夏期コース、アトランタのエモリー大学。

- 2018 年 7 月: CNS/[<span id="id6" class="problematic">\*</span>](#id5)2018 分子レベルから大規模ネットワーク レベルまでのマルチスケール モデリング、CNS/[<span id="id8" class="problematic">\*</span>](#id7)2018、シアトル。

- 2018 年 1 月: VII Latin American School on Computational Neuroscience (LASCON)、サンパウロ大学数学統計研究所、ブラジル

- 2017 年 7 月: バーンスタイン計算神経科学カンファレンス、マルチスケール モデリングとシミュレーション、ゲッティンゲン。

</div>

</div>

<div id="current-funding" class="section">

## 現在の資金<a href="#current-funding" class="headerlink" title="Link to this heading"></a>

- 国立衛生研究所 (NIH)、国立生物医用画像生物工学研究所 (NIBIB) U24 EB028998: 「脳回路のデータ駆動型マルチスケール モデリングのためのツールの普及」、期間: 2019 ～ 2024 年。金額: \$1,171,482; PI: サルバドール・デュラ・ベルナル

</div>

<div id="governance-structure" class="section">

## ガバナンス体制<a href="#governance-structure" class="headerlink" title="Link to this heading"></a>

NetPyNE に関する主要な決定は、<a href="#project-roadmap" class="reference internal"><span class="std std-ref">プロジェクト ロードマップ</span></a> および <a href="#code-of-conduct" class="reference internal"><span class="std std-ref">行動規範</span></a> に従って運営委員会によって行われます。委員会には、さまざまな機関、立場、背景を持つメンバーが含まれています。

現在の運営委員会は次のメンバーで構成されています (アルファベット順)。

- Salvador Dura-Bernal (ニューヨーク州立大学ダウンステート大学助教授、ネイサン クライン精神医学研究所研究員)

- パドレイグ・グリーソン (ユニバーシティ・カレッジ・ロンドン主席研究員)

- ジョー W. グラハム (ニューヨーク州立大学ダウンステート研究員)

- エリカ Y. グリフィス (ニューヨーク州立大学ダウンステート大学院生)

- Michael Hines (イェール大学上級研究員)

- クリフ C. カー (疾病モデリング研究所上級研究員)

- ウィリアム・W・リットン (ニューヨーク州立大学ダウンステート大学、キングス郡病院特別教授)

- ロバート・A・マクドゥーガル (イェール大学助教授)

- サミュエル・A・ネイモティン (ネイサン・クライン精神医学研究所研究員)

- Benjamin A. Suter (オーストリア科学技術研究所博士研究員)

- Subbashini Sivagnanam (サンディエゴ スーパーコンピューティング センター、主席計算およびデータ サイエンス研究スペシャリスト)

運営委員会のメンバーシップは個人メンバーシップです。所属は識別目的のみにリストされています。運営委員会のメンバーは雇用主や学術機関を代表するものではありません。

</div>

<div id="project-roadmap" class="section">

<span id="id9"></span>

## プロジェクト ロードマップ<a href="#project-roadmap" class="headerlink" title="Link to this heading"></a>

5 年間のプロジェクト ロードマップ (2019 ～ 2023 年) には、品質管理、新機能の開発、GUI 拡張、普及とコミュニティへの参加という 4 つの大きなカテゴリが含まれています。各カテゴリーの主な対象と想定期間

- **品質管理**: 堅牢性、信頼性、再現性

> <div>
  >
  > - *2019-2021: 信頼性* - 既存の機能、特に最近追加された機能 (RxD、細胞内接続、分散保存、パラメーターの最適化) をテストして、すべての有効な条件と入力の下で意図した機能を実行するようにします。
  >
  > - *2020-2022: 堅牢性とエラー処理* - ツールが実行中の誤った入力やエラーに対処できることを確認します。ツールの堅牢性の向上には、入力検証、例外処理、情報メッセージが含まれます。
  >
  > - *2022-2023: 再現性* - オペレーティング システム、Python、NEURON、MPI ライブラリのさまざまなバージョンを含む、最も一般的なプラットフォームでシミュレーション結果が再現可能であることを確認します。 HPC プラットフォームのセットアップ (XSEDE/NSG、Google Cloud Platform など)。
  >
  > </div>

- **新機能の開発**:

> <div>
  >
  > - *2020-2021: 巨視的スケールモデリング* - マクロスケールのデータ (例: MRI、EEG、MEG) およびモデル (例: 平均場モデル) をサポートするようにフレームワークを拡張し、このスケールを基礎となる回路、細胞および分子メカニズムに関連付けます。
  >
  > - *2021-2022: 機械学習分析手法* - ML 手法 (クラスタリング、次元削減、深層学習など) を組み込んで、大規模なパラメーター空間を探索および最適化し、ニューラル データを分析します。
  >
  > - *2022-2023: ネットワークのリバース エンジニアリング* - 統計 (ベイズ推論など) とグラフ理論分析を使用して、生物学的ネットワーク モデルの完全な接続情報から高レベルのコンパクトなネットワーク接続ルール (生成モデル) を推測します。
  >
  > </div>

- **GUI 拡張機能**: グラフィカル ユーザー インターフェイス (GUI) の拡張機能。新しいユーザーを関与させ、実験者、臨床医、学生がツールにアクセスできるようにするために不可欠です。

> <div>
  >
  > - *2019 ～ 2020 年: Web ベースのマルチユーザー展開* - ユーザーは、インターネット上の Web ブラウザーを介してモデルを構築し、シミュレーションを実行できるようになり、このツールが世界の研究コミュニティに公開されるようになります。
  >
  > - *2019-2022: 不足しているコンポーネントの組み込み* - 現在、プログラムからのみアクセス可能: RxD、細胞内接続、複雑な刺激、およびパラメーターの最適化 (グリッド検索のみ)。
  >
  > - *2021-2022: 動的インタラクティブ プロット* - 現在の静的画像を、複雑で大規模なデータセットの理解を容易にする最新のインタラクティブで動的プロットに置き換えることにより、プロットを改善します。
  >
  > - *2022-2023: 大規模ネットワークの可視化* - 詳細なニューロンの大規模ネットワーク (現在は数百ニューロンに制限されている) の 3D 可視化と操作を可能にするパフォーマンスの向上。
  >
  > </div>

- **普及とコミュニティへの関与**: ユーザーと開発者を訓練し、引き付けるために、補完的な普及と関与戦略を実装します。

> <div>
  >
  > - *2019-2020: オンライン ドキュメント* - すべてのツール コンポーネント、オプション、使用方法を例とともに網羅する更新された包括的なオンライン ドキュメント。これにより、初心者と上級ユーザーの両方がツールを最大限に活用できるようになります。
  >
  > - *2019 ～ 2023 年: ワークショップ/チュートリアル* - ツールの機能と利点の概要を提供することで、潜在的なユーザーを引き付けるために神経科学会議で開催されます。
  >
  > - *2020-2022: オンライン インタラクティブ チュートリアル* - インタラクティブに実行できるマルチメディアが豊富なステップバイステップの指示を通じて、新規ユーザーが自分のペースでトレーニングを受けることができます (例: GUI または Jupyter Notebook 経由)。
  >
  > - *2020 ～ 2023 年: 年次 3 日間の対面コース* - 研究者/臨床医に詳細なトレーニングを提供し、研究室や施設でツールの使用法を教えることができます。
  >
  > - *2020 ～ 2023 年: 年次ハッカソン* - 開発者をトレーニングして参加させ、長期的で持続可能な共同開発を促進します。
  >
  > </div>

</div>

</div>

</div>

</div>
</section>

</article>
</main>
