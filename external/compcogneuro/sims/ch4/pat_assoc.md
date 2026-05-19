---
layout: default
title: "compcogneuro/sims: 簡単なタスク"
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
<p>原典: <a href="https://github.com/compcogneuro/sims/blob/main/ch4/pat_assoc/README.md" target="_blank" rel="noopener noreferrer">https://github.com/compcogneuro/sims/blob/main/ch4/pat_assoc/README.md</a></p>
<p>ライセンス: BSD 3-Clause。このページは日本語翻訳であり、変更点は翻訳とサイト内整形です。</p>
</div>

<section class="section translated-source" markdown="1">
*[シミュレーションに戻る](https://compcogneuro.org/simulations)*

＃ 導入

このシミュレーションは、エラー駆動型学習とヘビアン学習が、隠れ層のない単純なタスク駆動型学習コンテキスト内でどのように機能するかを示しています。この状況は、4 つの入力ユニットのセットが 2 つの出力ユニットに投影されるという最も単純なケースに帰着します。 「タスク」は、入力ユニットの活性化パターンと、対応する出力ユニットの望ましい値または**ターゲット**値の間の関係の観点から指定されます。このタイプのネットワークは、入力のアクティビティのパターンと出力のアクティビティのパターンを関連付けることが目的であるため、**パターン アソシエータ**と呼ばれることがよくあります。

# 簡単なタスク

ネットワークには、一連のフィードフォワード重みを介して 4 つの入力ユニットから入力を受信する 2 つの出力ユニットがあることがわかります。

* [[[sim:Easy/Easy]]] ボタンをクリックすると、ネットワークが関連付けを学習する最初のパターン セットが表示されます。

ご覧のとおり、この「タスク」で学習する入出力関係は、左端の 2 つの入力ユニットが左の出力ユニットをアクティブにし、右端のユニットが右の出力ユニットをアクティブにするだけです。これは、最初の 2 つの入力を左の出力ユニットの「左」として分類し、次の 2 つの入力を右の出力ユニットの「右」として分類すると考えることができます。

これは、左側の出力ユニットが左端の入力ユニットに強い重みを付けて右側の入力ユニットを無視するだけでよいのに対し、右側の出力ユニットはその逆であるため、学習するのは比較的簡単なタスクです。 FFFB 禁止を使用していることに注意してください。これにより、(厳密ではありませんが) アクティブな出力ユニットが 1 つになる傾向があります。

ネットワークは、入力ユニットと出力ユニットの両方を環境内のイベントからの対応する値に単純にクランプし、純粋な BCM 学習を実行することによって、このタスクでトレーニングされます。

* ネットワークを監視しているときに、[[sim:Init]] を押してから、[[sim:Step]] トライアルを 4 回押します。

環境からの 4 つのイベントがすべてランダムな順序で表示されるはずです。  シナプスの重みは、各項目の後に BCM ヘビアン学習ルールに従って更新されます。

* 次に、実行モード (左上) を `Train` ではなく `Test` に設定し、次に [[sim:Init]] と [[sim:Step]] を 4 回試行して、各入力に対するネットワークの応答をテストします。

今回は、出力ユニットのアクティベーションが異なることがわかります。これは、出力アクティベーションが正解に固定されず、入力ユニットからの現在の重みのみに従って更新されるためです。  したがって、テストでは、「コーチング」されていないときの、このタスクに関するネットワークの現在の *実際の* パフォーマンスが記録されます (これがテストである理由です)。  これはトレーニング中の *マイナス フェーズ アクティベーション* に相当し、ネットワーク内の [[sim:Phase]]/`ActM` 変数を使用して表示できます。

* [[[sim:Test Trial]]] タブをクリックすると、すべてのテスト トライアルの記録が表示されます。

実行したテストトライアルの結果が表示されます。各行は 4 つのイベントのうちの 1 つを表し、右側に入力パターンと実際の出力アクティベーションが表示されます。 `SSE` 列は、**二乗合計誤差** (SSE) をレポートします。これは、テスト中の実際の出力アクティブ化 (`o`) と、トレーニング中にクランプされた *ターゲット* 値 (`t`) の間の差を単純に合計したものです。

```
   SSE = Sum (t - o)^2
```

where the sum is over the 2 output units. We are actually computing the *thresholded* SSE, where absolute differences of less than 0.5 are treated as zero, so the unit just has to get the activation on the correct side of 0.5 to get zero error. We thus treat the units as representing underlying binary quantities (i.e., whether the pattern that the unit detects is present or not), with the graded activation value expressing something like the likelihood of the underlying binary hypothesis being true. All of our tasks specify binary input/output patterns.

With only a single training epoch (one *epoch* is one pass through all the training patterns), the output unit is likely making some errors.

* Click on the [[sim:Train Epoch Plot]] tab to see a plot of SSE (summed also over all 4 training patterns) as the network trains. Change back to Train mode, then set the step level (to the right of [[sim:Step]]) to `Run` and [[sim:Step]] that to see the network iterate over training patterns.

Now you will see a summary plot across epochs of the sum of the thresholded SSE measure across all the events in the epoch. This shows what is often referred to as the **learning curve** for the network, and it should have decreased steadily down to zero, indicating that the network has learned the task.  Training will stop automatically after the network has exhibited 5 correct epochs in a row (determined by the `Config` settings, `NZero` = 5) just to make sure it has really learned the problem), or it stops after 100 epochs (`NEpochs`) if it fails to learn.

Let's see what the network has learned.

* Click back on the [[sim:Network]] and then select `Test` mode in the top left, then [[sim:Init]] (needed to restart the testing) and then set the step level to `Trial` and [[sim:Step]] to see each of the different input patterns and the network's response.

You should see that it is producing the correct output units for each input pattern. You can also look at the tab to see the behavior of the network across all four trials, all at once. You should see that the network has learned this easy task, turning on the left output for the first two patterns, and the right one for the next two. Now, let's take a look at the weights for the output unit to see exactly how this happened.

* In the [[sim:Network]], click on [[sim:Wts]]/r.Wt and then select the left `Output` unit to see its weights from the `Input`, then do the same for the right.

> **Question 4.3:** Describe the pattern of weights in qualitative terms for each of the two output units (e.g., left output has strong weights from the ?? input units, and weaker weights from the ?? input units).

<sim-question id="4.3">

> **Question 4.4:** Why would a Hebbian-style learning mechanism, which increases weights for units that are active together at the same time, produce the pattern of weights you just observed?  This should be simple qualitative answer, referring to the specific patterns of activity in the input and output of the Easy patterns.

<sim-question id="4.4">

# The Hard Task

Now, let's try a more difficult task.

* Click the [[sim:Hard/Hard]] button in the left panel to pull up a view of the Hard patterns.

In this harder environment, there is overlap among the input patterns for cases where the left output should be on, and where it should be off (and the right output on). This overlap makes the task hard because the unit has to somehow figure out what the most distinguishing or *task relevant* input units are, and set its weights accordingly.

This task reveals a problem with Hebbian learning: it is only driven by the correlation between the output and input units, so it cannot learn to be sensitive to which inputs are more task relevant than others (unless this happens to be the same as the input-output correlations, as in the easy task). This hard task has a complicated pattern of overlap among the different input patterns. For the two cases where the left output should be on, the middle two input units are very strongly correlated with the output activity, while the outside two inputs are half-correlated. The two cases where the left output should be off (and the right one on) overlap considerably with those where it should be on, with the last event containing both of the highly correlated inputs. Thus, if the network just pays attention to correlations, it will tend to respond incorrectly to this last case.

Let's see what happens when we run the network on this task.

* After making sure you are still viewing the [[sim:Wts]]/`r.Wt` receiving weights of the left output unit in the [[sim:Network]], switch back to `Train` mode (in the top left), press [[sim:Init]] and [[sim:Step]] with the step level set to `Run`. After training (or even during), click back and forth between the left and right output units. Try multiple Runs to see what generally tends to happen.

You should see that the weights into the left output unit increase, often with the two middle ones being more strongly increasing due to the higher correlation. The right output tends to have a strong weight from the 2nd input unit, and then somewhat weaker weights to the right two inputs, again reflecting the input correlations. Note that in contrast to a purely Hebbian learning mechanism, the BCM learning does not strictly follow the input correlations, as it depends significantly on the output unit activations over time as well, which determine the floating threshold for weight increase vs. decrease.

* Return to viewing the [[sim:Act]]/`Act` variable, and do `Test` mode (in the top left), [[sim:Init]], then [[sim:Step]] with step level set to `Trial` to see the network's response to the inputs.

You should see that the network is not getting all the right answers (you can also look at the `Test Trial` tab to see all events at once.)  This is also evident in the training SSE shown in the network view.

* Do several more `Train` `Step`s (with step level set to `Run`) on this Hard task. You can try increasing the [[sim:Config]]/`NEpochs` to 200, or even 500, to give it more time to learn -- press [[sim:Init]] after changing these parameters to get them to take.

> **Question 4.5:** Does the network ever solve the task? Run the network several times. Report the final SSE at the end of training for each run (hover on the last point in the [[sim:Train Epoch Plot]] to see the value).

<sim-question id="4.5">

Hebbian learning does not seem to be able to solve tasks where the correlations do not provide the appropriate weight values. In the broad space of tasks that people learn (e.g., naming objects, reading words, etc) it seems unlikely that there will always be a coincidence between correlational structure and the task solution. Thus, we must conclude that Hebbian learning by itself is of limited use for task learning. In contrast, we will see in the next section that error-driven learning, which specifically adapts the weights precisely to solve input/output mappings, can handle this Hard task without much difficulty.

# Exploration of Error-Driven Task Learning

* Select `Error Driven` instead of `Hebbian` for the Learn value in the left control panel, go back to `Easy` for the `Patterns`, and then press [[sim:Init]] in `Train` mode to have it take effect.

This will switch weight updating from the purely Hebbian (BCM) form of learning, to the form that is purely error driven, in terms of the contrast between plus (short term average) and minus (medium term) phases of activation. In this simple two-layer network, this form of learning is effectively equivalent to the Delta rule error-driven learning algorithm.   This sets the `Learn` params on the connections between Input and Output to have 0 amount of learning driven by the long-term running average activation (which corresponds to BCM Hebbian learning) and 100% of the learning driven by the medium-term floating threshold (which corresponds to error-driven learning).

Before training the network, we will explore how the minus-plus activation phases work in the simulator.

* Make sure that you are viewing activations in the network by selecting the [[sim:Act]]/Act button in the [[sim:Network]], and do [[sim:Step]] in `Trial` mode to present a Hard training pattern.

The activity will flicker over 4 **quarters** of time, where each quarter represents 25 msec (aka the `Gamma cycle`), and the first 75 msec (3 quarters) of a 100 msec trial period constitutes the *expectation* or *minus phase*, followed by the final 25 msec which is the *outcome* or *plus phase*.

* To see the activation at each of these time points, you can use the VCR-like buttons at the bottom-right of the Network, by the `Time` label -- step back and you'll see the cycle counter going back through each quarter increment.  Step forward to see it unfold in the proper order.  You can also click on the [[sim:Phase]] category of variables and select `ActQ1`, `ActQ2`, `ActM` and `ActP` to see the activity at the end of each quarter as well.

Learning occurs after the plus phase of activation.  You can recognize targets, like all external inputs, because their activations are exactly .95 or 0 -- note that we are clamping activations to .95 (not 1.0) because units cannot easily produce activations above .95 with typical net input values due to the saturating nonlinearity of the rate code activation function. You can also switch to viewing the `Act / Targ` value, which will show you the target inputs prior to the activation clamping. In addition, the minus phase activation is always viewable as `ActM` and the plus phase as `ActP`.

The critical difference between error-driven learning and Hebbian is that error-driven learning is based directly on this difference between the expectation or guess produced in the minus phase, and the correct target activation in the plus phase.

* If your network did not make the wrong guess during the minus phase, keep doing [[sim:Step]] in `Trial` mode until it does, then click on the [[sim:Wts]]/`r.DWt` variable to see the delta-weights (weight changes, i.e., learning) that occurred for incorrectly activated unit, versus the correctly activated one.  You should see that the weights go down for the erroneously activated unit, and up for the one that *should* have been activated -- this is the essence of error correction and occurs because learning is proportional to the change in activity over time for each output unit.

* Go ahead and [[sim:Step]] with the step mode set to `Run` the network to complete the training on the Easy task.

The network should have no trouble learning this task, as you can see in the `Train Epoch Plot`. You can do more `Step Run`s to see how reliably and rapidly it learns this problem. Compared to Hebbian, it learns this Easy task more slowly.

But the real challenge is whether it can learn the Hard task, which Hebbian  could not learn at all.

* Set `Patterns` to `Hard`, press [[sim:Init]] and [[sim:Step]] with the step mode set to `Run`. Do multiple repeated Runs, to see how reliably and quickly it learns overall (monitor [[sim:Train Epoch Plot]] to make it run faster).

You should see that the network learns this task without much difficulty, because error-driven learning is directly a function of how well the network is actually doing, driving the weights specifically to solve the task, instead of doing something else like encoding correlational structure. Now we'll push the limits of even this powerful error-driven learning.

* Set `Patterns` to `Impossible`, and click on the [[sim:Impossible/Impossible]] button to view the patterns.

Notice that each input unit in this environment is active equally often when the output is active as when it is inactive. That is, there is complete overlap among the patterns that activate the different output units. These kinds of problems are called *ambiguous cue* problems, or *nonlinear discrimination* problems (e.g., Sutherland & Rudy, 1989).  This kind of problem might prove difficult, because every input unit will end up being equivocal about what the output should do. Nevertheless, the input patterns are not all the same -- people could learn to solve this task fairly trivially by just paying attention to the overall patterns of activation. Let's see if the network can do this.

* Press [[sim:Init]] and [[sim:Step]] `Run`. Do it again, and again.. Increase the [[sim:Config]] / `NEpochs` higher than 100.

> **Question 4.6:** Does the network ever learn to solve this "Impossible" problem? Report the final SSE values for your runs.

<sim-question id="4.6">

Because error-driven learning cannot learn what appears to be a relatively simple task, we conclude that something is missing.  Unfortunately, that is not the conclusion that Minsky & Papert reached in their highly influential book, *Perceptrons*. Instead, they concluded that neural networks were hopelessly inadequate because they could not solve problems like the one we just explored. This conclusion played a large role in the waning of the early interest in neural network models of the 1960s. As we'll see, all that was required was the addition of a hidden layer interposed between the input and output layers (and the necessary math to make learning work with this hidden layer, which is really just an extension of the chain rule used to derive the delta rule for two layers in the first place).



</section>

</article>
</main>
