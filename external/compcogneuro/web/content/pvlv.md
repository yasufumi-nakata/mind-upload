---
layout: default
title: "compcogneuro/web: pvlv"
description: "compcogneuro/web: pvlv.md の日本語訳"
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
<p>原典: <a href="https://github.com/compcogneuro/web/blob/main/content/pvlv.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/web/blob/main/content/pvlv.md</a></p>
<p>ライセンス: Text: CC BY 4.0; code: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
+++
Name = "PVLV"
Categories = ["Rubicon", "Neuroscience"]
bibfile = "ccnlab.json"
+++
**PVLV** (一次値、学習値) モデルは、さまざまな古典的条件付けパラダイム ([[@OReillyFrankHazyEtAl07]]; [[@HazyFrankOReilly10]]; [[@OReillyFrankHazyEtAl07]]; [[@OReillyFrankHazyEtAl07]]; [[@MollickHazyKruegerEtAl20]])。これは、[[reinforcement learning]] で詳しく説明されている TD (時間差分) アルゴリズムなどの純粋な計算アルゴリズムから、[[Rubicon]] 目標駆動フレームワークの中心となる神経基板へのブリッジを提供します。

[[PVLV simulation]] では、フレームワークの主要なメカニズムについて詳しく説明していますが、このページでは、その背後にある主要なニューラル データと、それがより大きなルビコン モデル内にどのように適合するかについて説明します。 [[Axon]] スパイキング フレームワーク内で実装されたモデルの更新バージョンは、[[@^MollickHazyKruegerEtAl20]] で最近公開されたモデルのいくつかの側面、特に、[[prefrontal cortex]] のルビコン目標関与維持ネットワークの一部として、その後の目標結果の期待を維持するために眼窩前頭皮質 (OFC) コンポーネントが活性化される方法に関して、より生物学に基づいた実装を提供します。さらに、[[lateral habenula]] および神経調節物質 [[acetylcholine]] の寄与は、US の基礎となる [[emotion|drives]] のモデルと同様に、元のモデルから拡大されました。

2つの経路と貢献の概要など


## サインとゴールトラッカーの比較

## TODO: 新しい研究

### 副社長

* [[@FujimotoHoriNagaiEtAl19]] -- VP は rmCD (NAcc) 入力よりも早いアクティビティを示します: VP 115 +/- 17ms、PAN 190 +/- 25ms! VP は報酬のサイズと満腹度をエンコードします。 VP の不活性化により中断されます。 OFC -> rmCD エンコード値:

> (インら、2005; グレメルおよびコスタ、2013; グレメルら、2016);これにより、目標指向行動を仲介するための rmCD の役割が確認されました。  まず、VP ニューロンのコーディング待ち時間は、rmCD 投影ニューロン (PAN) のコーディング待ち時間よりも大幅に短かったです。第二に、これが事実であれば、rmCD から VP への投影が GABA 作動性であることを考慮すると、応答極性は 2 つの領域間で逆になるでしょう (Haber et al., 1990)。しかし、両方の領域のニューロンの大部分は、合図に対して興奮性反応を示しました。

> 残りの疑問は次のとおりです。そのような豊富で迅速なインセンティブ価値情報はどこから得られるのでしょうか?考えられる発生源の 1 つは基底外側扁桃体 (BLA) であり、これは VP と相互接続しており (Mitrovic and Napier、1998; Root et al.、2015)、短い潜伏期間の合図のインセンティブ値を反映するニューロンを含むことが知られています (Paton et al., 2006; Belova et al., 2008; Jenison et al., 2011）。最近の研究では、扁桃体病変がサルのVS病変よりも報酬に基づく学習をより深刻に阻害することが実証されており（Averbeck et al., 2014; Costa et al., 2016）、インセンティブ価値処理におけるBLA-VP投影の寄与を裏付けている。別の候補は視床下核 (STN) からの投影です。 VP は、辺縁皮質領域からの投射を受け取る内側 STN と相互接続しており (Haynes and Haber、2013)、辺縁皮質 - 視床下 - 淡蒼球の「ハイパーダイレクト」経路を構成しています (Nambu et al.、

一般に、これは標準的なストーリーと互換性があります。早期に amyg および STN 入力を取得し、変調を開始しますが、キー Go / No 信号は依然として線条体から来ています。

* [[@AhrensMeyerFergusonEtAl16]] -- VP は、サイン トラッカーが CS 発症時に VP を強く活性化していることを示していますが、ゴール トラッカーは活性化していません。 -- ロングトライアル: 7 ～ 8 秒 -- CS の維持を気にしないための鍵。  どちらもCSの発症に対して同じ大きな反応を示します。 fig_vp_sign_track_cs_ahrens_etal_16.png

* [[@SagaRichardSgambato-FaureEtAl16]] -- サルの食欲不振に対する VP CS 活動:

> 我々は、食欲および嫌悪条件刺激（CS）によって優先的に活性化されるニューロンの2つの集団を発見しました。さらに、VP は食欲と嫌悪の結果を予測する活動を示しました。これらの活動パターンは、VP が CS によって引き起こされる嫌悪的な文脈情報の符号化と維持に関与していることを示しています。さらに、ビククリン注射による VP 活動の妨害により、嫌悪試行におけるエラー試行の数が増加しました。特に、被験者は反応バーを途中で解放したり、まったく反応を示さなかったり、嫌悪感を引き起こす結果を回避できなかったりしました。

* [[@TachibanaHikosaka12]] -- VP の意欲的な CS

* [[@FagetZellSouterEtAl18]] -- VP での対戦相手のコーディング

* [[@OttenheimerBariSutliefEtAl20]] -- VP は RPE シグネチャを示しますが、TD とあまり一致しません。スクロースはマルトデキストリン（MD）よりも有益です。 MD を取得する場合は RPE。ニューロンのサブセットは、基本的な RW RPE モデルと一致する過去の病歴に対する感受性を示します。  [[@FujimotoHoriNagaiEtAl19]] と同様に、VP と NAc の方が優れたデコードを示しますが、VP は発火率が高く、統合されています。Barter らと同様に、GPi の信号は常に優れていますが、NAc が学習の鍵となります。

タスクエンゲージメント用の VP キー。


* [[@FujimotoHoriNagaiEtAl19]] -- 副社長
</section>

</article>
</main>
