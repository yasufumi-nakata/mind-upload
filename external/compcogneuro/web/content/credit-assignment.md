---
layout: default
title: "compcogneuro/web: credit-assignment"
description: "compcogneuro/web: credit-assignment.md の日本語訳"
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
<p>原典: <a href="https://github.com/compcogneuro/web/blob/main/content/credit-assignment.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/web/blob/main/content/credit-assignment.md</a></p>
<p>ライセンス: Text: CC BY 4.0; code: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
+++
Categories = ["Learning", "Computation"]
bibfile = "ccnlab.json"
+++
**単位の割り当て** は、あらゆる種類の [[learning]] メカニズムで最も重要なプロセスであり、現在の学習イベントに対して差分単位/責任を [[neuron]] に割り当てます。多くの場合、[[Hebbian learning]] 学習と [[error backpropagation]] 学習の両方のように、送信ニューロンの [[activation]] 値を乗算することで実現されます。数学的な詳細については、エラー逆伝播の [[error backpropagation#credit assignment]] を参照してください。

## 時間単位の割り当て

標準誤差逆伝播コンテキストでは、ニューロンの現在の活性化状態を使用して、クレジット割り当てプロセスが効果的に並行して行われます。しかし、現実世界の連続時間のコンテキストでは、行動的または動機的に関連する結果に対する信用や責任の真の源泉は通常、過去にあります。たとえば、エージェントが以前にとった行動などです。これにより、クレジット割り当て問題の「一時的」バージョンが作成されます。これは、エラー逆伝播で利用できる即時クレジット割り当てプロセスよりもはるかに困難です。

[[Reinforcement learning]] (RL) アルゴリズムは、この一時的なクレジット割り当ての問題を何らかの方法で解決する必要があります。たとえば、TD (時間的差分) アルゴリズムは、報酬予測誤差 (RPE) を時間の経過とともに逆方向にカスケードすることによって、時間的クレジットの割り当てを実行します。

対照的に、RL 用の生物学に基づく [[PVLV]] アルゴリズムは、[[amygdala]]、腹側 [[basal ganglia]] (BG)、および [[orbitofrontal cortex]] (OFC) を含む生物学的メカニズムの調整されたセットを介して時間的クレジット割り当てを実行します。扁桃体は結果に関連する刺激を認識することを学習し、OFC は時間の経過とともにこれらの将来の結果に対する期待を積極的に維持し、一時的な信用の割り当てを提供するために時間的なギャップを埋めることができます。 BG は、扁桃体や他の領域からの入力を使用して、OFC 活動状態の更新をトリガーすることを学習します。これは、より広範な [[Rubicon]] フレームワークの主要コンポーネントです。

[[transformer]] アーキテクチャを使用する [[large language models]] では、時間的クレジットの割り当ては、関連するすべての時間的コンテキストをネットワークへの直接入力として提供することにより、標準的な並列誤差逆伝播を介して達成されます。これは生態学的にも、神経学的にも、認知的にも妥当ではありません。人々のテキストの記憶容量は 7 単語程度です。したがって、さまざまなメカニズムが必要になります。


</section>

</article>
</main>
