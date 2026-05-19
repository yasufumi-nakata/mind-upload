---
layout: default
title: "OpenSourceBrain Documentation: 計算神経科学"
description: "OpenSourceBrain/Documentation: source/General/Background_Information/02_Introduction_to_Computational_Neuroscience.md の日本語訳"
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
<p>原典: <a href="https://github.com/OpenSourceBrain/Documentation/blob/main/source/General/Background_Information/02_Introduction_to_Computational_Neuroscience.md" target="_blank" rel="noopener noreferrer">https://github.com/OpenSourceBrain/Documentation/blob/main/source/General/Background_Information/02_Introduction_to_Computational_Neuroscience.md</a></p>
<p>ライセンス: CC BY 4.0。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
<a id="bg:compneuro"></a>
<a id="computational-neuroscience"></a>
# 計算神経科学

この文書は、初心者が計算神経科学に入門できるよう支援することを目的としています。
これは生きたドキュメントであり、定期的に更新されることに注意してください。
[援助の申し出](https://github.com/OpenSourceBrain/Contribute/issues/3) を完了することは大歓迎です!

<a id="books"></a>
## 本

1. 神経科学
   - [認知神経科学][b_1.1]、マイケル S. ガザニガ、リチャード B. アイヴリー、ジョージ R. マングン
   - [神経科学の原理][b_1.2]、エリック カンデル

2. 計算モデリング/理論神経科学
   - [理論的神経科学: 神経システムの計算および数学的モデリング][b_2.1]、Peter Dayan および LF Abbott
   - [ニューロン モデリングの方法: イオンからネットワークまで][kochsegev]、C. Koch および I. Segev (編)
   - [神経科学における計算モデリングの原理][willshaw]、David sterratt、Bruce Graham、Andrew Gillies、David Willshaw (編)
   - [ニューロンダイナミクス - 単一ニューロンからネットワークおよび認知モデルまで][ガースナー]、ウルフラム ガースナー、ヴェルナー M. キスラー、リチャード ノー、リアム パニンスキー (**[オンラインで無料で入手可能!][ガースナー]**)
   - [計算神経科学: 実験家のための現実的なモデリング][deschutter]。 E.デ・シュッター (編)
   - [ニューラル計算理論入門][b_2.2]、ジョン A. ハーツ、アンダース S. クロー、リチャード G. パーマー
   - [ビジョン: 人間の表現と視覚情報の処理に関する計算による調査][b_2.3]、デビッド マー
   - [脳理論とニューラル ネットワークのハンドブック][b_2.4]、マイケル A. アービブ (編)

3. プログラミング
   - [神経科学者のための Matlab][b_3.1]
   - [SciPy と NumPy][b_3.2]
   - [データ分析のためのPython][b_3.3]
   - [統計を考える][b_3.4]
   - [Python を詳しく見る][b_3.5]

4. 機械学習
   - [パターン認識と機械学習][b_4.1]、クリストファー M ビショップ
   - [機械学習、確率的観点][b_4.2]、ケビン P. マーフィー

[b_1.1]: http://www.amazon.com/Cognitive-Neuroscience-Biology-Mind-4th/dp/0393913481/ref=sr_1_1?s=books&ie=UTF8&qid=1457248826&sr=1-1&keywords=cognitive+neuroscience+gazzaniga
[b_1.2]: http://www.amazon.com/Principles-Neural-Science-Eric-Kandel/dp/0838577016
[b_2.1]: http://www.gatsby.ucl.ac.uk/~dayan/book/
[b_2.2]: http://www.amazon.com/Introduction-Theory-Neural-Computation-Institute/dp/0201515601
[b_2.3]: http://www.amazon.com/Vision-Computational-Investigation-Representation-Information/dp/0262514621
[b_2.4]: http://www.amazon.com/Handbook-Brain-Theory-Neural-Networks/dp/0262011972
[コチセゲフ]: https://mitpress.mit.edu/books/methods-neuronal-modeling
[ウィルショー]: http://www.compneuroprinciples.org/
[ガースナー]: http://neuronaldynamics.epfl.ch/
[シャッター解除]: http://www.amazon.co.uk/Computational-Neuroscience-Realistic-Experimentalists-Frontiers/dp/0849320682
[b_3.1]: http://www.amazon.com/MATLAB-Neuroscientists-Introduction-Scientific-Computing/dp/0123745519
[b_3.2]: http://shop.oreilly.com/product/0636920020219.do
[b_3.3]: http://shop.oreilly.com/product/0636920023784.do
[b_3.4]: http://greenteapress.com/thinkstats/
[b_3.5]: http://www.diveintopython.net/
[b_4.1]: http://www.amazon.com/Pattern-Recognition-Machine-Learning-Christopher/dp/8132209060/ref=pd_sim_14_4?ie=UTF8&dpID=51qDRMnf9LL&dpSrc=sims&preST=_AC_UL160_SR118%2C160_&refRID=1N99QG8VBWEBCHJ893BR
[b_4.2]: https://mitpress.mit.edu/books/machine-learning-0

<a id="publications"></a>
## 出版物

1. 記事をレビューする
   - Atick、J.J.、1992年。[情報理論は感覚処理の生態学的理論を提供できるでしょうか?][p_1.1] ネットワーク: ニューラル システムの計算、3(2)、213-251 ページ。
   - Oztop, E.、Kawato, M.、Arbib, M.、2006 年。[ミラー ニューロンと模倣: 計算によるガイド付きレビュー。][p_1.5] Neural Networks、19(3)、pp.254-271。
   - Bower、J.M.、2013。[20 年間の計算神経科学。][p_1.3] ニューヨーク: Springer。
   - ブレット、R.、ルドルフ、M.、カーネヴァーレ、T.、ハインズ、M.、ビーマン、D.、バウワー、J.M.、ディーズマン、M.、モリソン、A.、グッドマン、P.H.、ハリス Jr、F.C. [スパイキング ニューロンのネットワークのシミュレーション: ツールと戦略のレビュー][p_1.4] Journal of computational Nuclearscience、23(3)、349-398 ページ。

2. 古典的な論文
   - Hodgkin, A.L. および Huxley, A.F.、1952 年。[膜電流の定量的説明と、神経の伝導と興奮へのその応用][p_2.1] The Journal of physiology、117(4)、p.500。
   - マカロック、W.S. [神経活動に内在する概念の論理的計算。][p_2.2] 数理生物物理学紀要、5(4)、115-133 ページ。
   - Donald O.Hebb、[The Organization of Behavior][p_2.3] ニューヨーク: Wiley、序論と第 4 章、「認識の第一段階: 集会の成長」、pp. xi-xix、60-78。
   - ラシュリー、K.S.、1950年。 [エングラムを探して][p_2.4]
   - Von Neumann, J. および Kurzweil, R.、2012 年。[コンピューターと脳。][p_2.5] エール大学出版局。
   - Rosenblatt, F.、1958. [パーセプトロン: 脳内の情報の保存と組織化のための確率的モデル。][p_2.6] Psychological review、65(6)、p.386
   - Marr, D. および Poggio, T.、1976 年。[ステレオ視差の共同計算][p_2.7] Science、194(4262)、283-287 ページ。
   - Grossberg, S.、1982. [脳はどのようにして認知コードを構築するのですか?][p_2.8] 心と脳の研究 (1-52 ページ)。オランダのシュプリンガー社。
   - アクリー、D.H.、ヒントン、G.E. [ボルツマン マシンの学習アルゴリズム][p_2.9] 認知科学、9(1)、147-169 ページ。

[p_1.1]: http://invibe.net/biblio_database_dyva/woda/data/att/0b79.file.pdf
[p_1.2]: ftp://134.76.12.4/pub/misc2/neuron/papers/nsimenv.pdf
[p_1.3]: http://link.springer.com/book/10.1007/978-1-4614-1424-7
[p_1.4]: http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2638500/
[p_1.5]: http://www.sciencedirect.com/science/article/pii/S0893608006000268
[p_2.1]: http://www.ncbi.nlm.nih.gov/pmc/articles/PMC1392413/
[p_2.2]: http://www.minicomplexity.org/pubs/1943-mcculloch-pitts-bmb.pdf
[p_2.3]: http://www.cs.cmu.edu/~bhiksha/courses/deeplearning/Fall.2013/slides.2014/3.Srivaths.Hebb.pdf
[p_2.4]: http://gureckislab.org/courses/fall13/learnmem/papers/Lashley1950.pdf
[p_2.5]: https://books.google.co.in/books/about/The_Computer_and_the_Brain.html?id=Q30MqJjRv1gC&redir_esc=y
[p_2.6]: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.335.3398
[p_2.7]: http://www.dtic.mil/dtic/tr/fulltext/u2/a030748.pdf
[p_2.8]: http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.228.3623&rep=rep1&type=pdf
[p_2.9]: http://onlinelibrary.wiley.com/doi/10.1207/s15516709cog0901_7/pdf

<a id="open-source-brain-projects"></a>
## オープンソース Brain プロジェクト

計算神経科学のチュートリアル、演習などを含む OSB プロジェクトのリストについては、[ここ](http://www.opensourcebrain.org/search_custom_field?f[]=43&op[43]=~&v[43][]=Tutorial) を参照してください。

<a id="software"></a>
## ソフトウェア

1. モデリング

Open Source Brain のモデルの主なターゲット シミュレーターの概要については、[ここ](https://github.com/OpenSourceBrain/OSB_Documentation/blob/master/contents/Help/08_Simulators.md) を参照してください。

2. マークアップ言語
   - 計算論的神経科学のためのモデル記述言語 [(NeuroML)][s_1.2.1]
   - システム生物学マークアップ言語 [(SBML)][s_1.2.2]
   - [CellML][s_1.2.3]

[s_1.2.1]: http://www.neuroml.org/home
[s_1.2.2]: http://sbml.org/Main_Page
[s_1.2.3]: http://www.cellml.org/

3. ライブラリ: データ分析と科学計算
   - [パンダ、Python][s_2.1]
   - [NumPy、Python][s_2.2]
   - [SciPy、Python][s_2.3]

4. ライブラリ: データの視覚化
    - [matplotlib、python][s_3.1]
    - [prettyplotlib、Python][s_3.2]
    - [ボケ味、パイソン][s_3.3]
    - [ggplot、R][s_3.4]

3. ライブラリ: 機械学習
   - [PyBrain、Python][s_4.1]
   - [SciKit、Python][s_4.2]
   - [Pylearn2、Python][s_4.3]
   - [テアノ、パイソン][s_4.4]
   - [ナイルラーン、Python][s_4.5]

[s_2.1]: http://pandas.pydata.org
[s_2.2]: http://www.numpy.org
[s_2.3]: http://scipy.org/index.html
[s_3.1]: http://matplotlib.org/
[s_3.2]: http://blog.olgabotvinnik.com/prettyplotlib/
[s_3.3]: http://bokeh.pydata.org/en/latest/
[s_3.4]: http://ggplot2.org/
[s_4.1]: http://pybrain.org
[s_4.2]: http://scikit-learn.org/stable/
[s_4.3]: http://deeplearning.net/software/pylearn2/
[s_4.4]: http://deeplearning.net/software/theano/
[s_4.5]: http://nilearn.github.io/

<a id="databases"></a>
## データベース

- ModelDB: 計算神経科学用モデルデータベース [(ModelDB)][d_1]
- オープンソース ブレイン [(OSB)][d_2]
- デジタル再構成ニューロンデータベース[(ニューロモルフォ)][d_3]
- 神経科学情報フレームワーク [(NIF)][d_4]
- 脳操作データベースシステム[(BODB)][d_5]
- BioModels データベース [(BioModels)][d_6]

[d_1]: https://senselab.med.yale.edu/ModelDB/
[d_2]: http://opensourcebrain.org/
[d_3]: http://neuromorpho.org/neuroMorpho/index.jsp
[d_4]: http://www.neuinfo.org/about/index.shtm
[d_5]: http://bodb.usc.edu/bodb/
[d_6]: http://www.ebi.ac.uk/biomodels-main/

<a id="organisations"></a>
## 組織

- 計算神経科学機構 [(OCNS)][o_1]
- 国際神経情報学調整施設 [(INCF)][o_2]

[o_1]: http://www.cnsorg.org/
[o_2]: http://www.incf.org/

<a id="institutions-laboratories-and-research-groups"></a>
## 機関、研究所、研究グループ

1. アジア
   - [計算神経科学研究所、ATR][larg_1.1]
   - [理化学研究所脳科学総合研究センター(BSI)][larg_1.2]
   - [神経計算ユニット、OIST][larg_1.3]
   - [OIST 計算神経科学ユニット][larg_1.4]
   - [イスラエル、エルサレムのヘブライ大学神経物理学研究室][larg_1.5]
   - [教授。 Upinder S. Bhalla、NCBS、インド][larg_1.6]

2. ヨーロッパ
   - [国立バーンスタイン ネットワーク計算神経科学][larg_2.1]
   - [ギャツビー計算神経科学ユニット][larg_2.2]
   - [計算神経科学および認知ロボット工学センター (CNCR)][larg_2.3]
   - [教授。 Wolfgang Maass、理論計算機科学研究所、グラーツ工科大学][larg_2.4]

3. アメリカ
   - [アレン脳科学研究所][larg_3.1]
   - [スワーツ計算神経科学センター、UCSD、カリフォルニア州][larg_3.2]
   - [認知の神経基盤センター][larg_3.3]
   - [スン研究所、ニューヨーク州プライストン][larg_3.4]
   - [ニューラルダイナミクスおよび計算研究所、カリフォルニア州スタンフォード][larg_3.5]
   - [ニューヨーク州コロンビア大学理論神経科学センター][larg_3.6]
   - [カリフォルニア州カリフォルニア州カリフォルニア州カリフォルニア州セジノウスキー研究所][larg_3.7]

研究室、センター、研究者のより包括的なリストは、[ここ](https://compneuroweb.com/labs.html) でご覧いただけます。

[larg_1.1]: http://www.cns.atr.jp/en/home-3/cns/
[larg_1.2]: http://www.brain.riken.jp/en/
[larg_1.3]: https://groups.oist.jp/ncu/research
[larg_1.4]: https://groups.oist.jp/cnu/
[larg_1.5]: http://neurophysics.huji.ac.il/
[larg_1.6]: https://www.ncbs.res.in/faculty/bhalla-research
[larg_2.1]: http://www.nncn.de/en
[larg_2.2]: http://www.gatsby.ucl.ac.uk/
[larg_2.3]: http://www.birmingham.ac.uk/research/activity/cncr/index.aspx
[larg_2.4]: http://www.igi.tugraz.at/maass/#Research
[larg_3.1]: http://www.alleninstitute.org/our-science/brain-science/research/open-science-resources/
[larg_3.2]: http://sccn.ucsd.edu/
[larg_3.3]: http://www.cnbc.cmu.edu/computational-neuroscience
[larg_3.4]: http://seunglab.org/
[larg_3.5]: http://ganguli-gang.stanford.edu/
[larg_3.6]: http://www.neurotheory.columbia.edu/index.html
[larg_3.7]: http://cnl.salk.edu/

<a id="mailing-lists-blogs-and-news"></a>
## メーリングリスト、ブログ、ニュース

1. メーリングリスト
   - 計算神経科学 [(Comp-neuro)][mlbn_1.1]
   - 計算およびシステム神経科学 [(Cosyne)][mlbn_1.2]
   - コネクショニスト メーリング リスト [(コネクショニスト)][mlbn_1.3]

2. ブログ
   - [神経懐疑論者][mlbn_2.1]
   - [振動する思考][mlbn_2.2]
   - [真面目な脳][mlbn_2.3]
   - [xcorr : コンプニューロ][mlbn_2.4]
   - [PLoS ニューロ][mlbn_2.5]
   - [ブレインボックス][mlbn_2.6]

3. ニュース
   - [サイエンスデイリー][mlbn_3.1]
   - [神経科学ニュース][mlbn_3.2]

[mlbn_1.1]: http://www.neuroinf.org/mailman/listinfo/comp-neuro
[mlbn_1.2]: https://groups.google.com/forum/#!forum/cosyne-announce
[mlbn_1.3]: http://www.cnbc.cmu.edu/connectionists
[mlbn_2.1]: http://blogs.discovermagazine.com/neuroskeptic/#.Vt59D5x9600
[mlbn_2.2]: http://blog.ketyov.com/
[mlbn_2.3]: http://blogs.scientificamerican.com/scicurious-brain/
[mlbn_2.4]: https://xcorr.net/
[mlbn_2.5]: http://blogs.plos.org/neuro/
[mlbn_2.6]: http://the-brain-box.blogspot.in/
[mlbn_3.1]: http://www.sciencedaily.com/articles/c/computational_neuroscience.htm
[mlbn_3.2]: http://neurosciencenews.com/neuroscience-terms/computational-neuroscience/

<a id="online-courses"></a>
## オンラインコース

1.コーセラ
   - [計算神経科学][oc_1.1]
   - [機械学習][oc_1.3]
   - [シナプス、ニューロン、脳][oc_1.4]

2.edX
   - [神経科学の基礎、パート I][oc_2.1]
   - [神経科学の基礎、パート II][oc_2.2]

3. ウルフラム・ガースナー
   - [ニューロンダイナミクス - 単一ニューロンの計算神経科学][oc_3.1]
   - [生物学的ニューロンとニューラルネットワークのモデリング][oc_3.2]

4. OCW MIT
   - [計算神経科学の概要][oc_4.1]
   - [計算認知科学][oc_4.2]

[oc_1.1]: https://www.coursera.org/course/compneuro
[oc_1.2]: https://www.coursera.org/course/neuraldata
[oc_1.3]: https://www.coursera.org/learn/machine-learning
[oc_1.4]: https://www.coursera.org/course/bluebrain
[oc_2.1]: https://www.edx.org/course/fundamentals-neuroscience-part-i-harvardx-mcb80-1x#.VRv8q8svD0o
[oc_2.2]: https://www.edx.org/course/fundamentals-neuroscience-part-2-neurons-harvardx-mcb80-2x#.VRv9qMsvD0o
[oc_3.1]: http://lcn.epfl.ch/~gerstner/NeuronalDynamics-MOOC1.html
[oc_3.2]: http://lcn.epfl.ch/~gerstner/VideoLecturesGerstner.html
[oc_4.1]: http://ocw.mit.edu/courses/brain-and-cognitive-sciences/9-29j-introduction-to-computational-neuroscience-spring-2004
[oc_4.2]: http://ocw.mit.edu/courses/brain-and-cognitive-sciences/9-66j-computational-cognitive-science-fall-2004/

<a id="other-resources"></a>
## その他のリソース

- [ウェブ上の計算論的神経科学][or_1]
- [興味深い (計算) 神経科学論文 ][or_2]
- [理論的な神経科学の書籍に関するコメント][or_3]
- [計算神経科学の入門講義][or_4]

[or_1]: https://compneuroweb.com
[or_2]: http://compneuropapers.tumblr.com/
[or_3]: http://compneuro.uwaterloo.ca/research/theoretical-neuroscience/comments-on-theoretical-neuroscience-books.html
[or_4]: http://www.genesis-sim.org/cnslecs/cnslecs.html
</section>

</article>
</main>
