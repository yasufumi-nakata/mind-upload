# Wiki: Identity assessment and continuity test

> Returning to philosophy and test design with reservation conditions
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-06 / 位置づけ: Learning guide

## このページの役割
This page is a wiki that organizes Mind-Upload's L4 ``Individuality Assertion'' from the perspective of ``What do you want to test and how?'' rather than introducing philosophical terms. We will explain from the beginning how to reduce memory, values, learning, longitudinal stability, and handling of divergences to pre-registered continuity tests.

## 正確さの前提
What is described here is the beginning of evaluation design. It is still unresolved under what conditions we can finally determine that the two persons are the same person, and this page does not provide that conclusion.

## 公開ページへ戻る
- [Introduction to WBE](https://mind-upload.com/wbe_101.html)
- [Verification platform](https://mind-upload.com/verification.html)
- [technology roadmap](https://mind-upload.com/tech_roadmap.html)

## 関連 Wiki
- [Wiki: Identity and copying issues](https://github.com/yasufumi-nakata/mind-upload/wiki/personhood-and-copy-problem) - First of all, it is for those who want to return to the philosophical foundations.
- [Wiki: How to read claims and evidence](https://github.com/yasufumi-nakata/mind-upload/wiki/claims-and-evidence) - It makes up for how strong a claim L4 is.
- [Wiki: Counterfactuals/Interventions/Perturbations](https://github.com/yasufumi-nakata/mind-upload/wiki/counterfactual-and-perturbation-verification) - This will explain why you want to see reactions to changes in conditions.
- [Wiki: state/trait/drift](https://github.com/yasufumi-nakata/mind-upload/wiki/state-trait-and-drift) - Supplement how to distinguish between short-term conditions and long-term characteristics in longitudinal evaluation.
- [Wiki: Update/branch/stop rules](https://github.com/yasufumi-nakata/mind-upload/wiki/update-branching-and-stop-rules) - Supplements the basics of branch logs, version management, and stop conditions.

## いま分かっていること
- The assertion of identity is stronger than L0-L3, and mere output matching is not enough.
- We need to look at memories, values, learning history, and reactions to changing conditions separately.
- Bifurcations and long-term drift make claims of identity even more difficult.

## まだ分かっていないこと
- It is still unresolved which combination of tests must be met to constitute a sufficient condition.
- It remains to be proven that continuous transitions may be sufficient to protect one's identity.

---

<h2>The shortest idea</h2>
<p>
When questioning someone's identity, it is not only necessary to ask whether they speak the same way. It is important to decide first what is going on and what will be put on hold if things break down.
</p>

<h2>Why L4 suddenly becomes difficult</h2>
<p>
In L1 and L2, you can put relatively clear metrics like accuracy and prediction match. However, in L4, questions such as ``Is this memory match enough?'' ``If a person's values ​​change slightly, are they a different person?'' and ``To what extent should we allow changes due to learning?'' come into play. In other words, not only the measurement but also the judgment rules themselves become difficult.
</p>

<h2>First of all, 5 items to consider separately</h2>
<table>
<thead>
<tr>
<th>Item</th>
<th>What do you want to see</th>
<th>Why that's not enough</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Memory</strong></td>
<td>Autobiographical memory and episodic coherence. </td>
<td>Memory replay alone does not necessarily indicate subjective continuity. </td>
</tr>
<tr>
<td><strong>Values/Preferences</strong></td>
<td>Consistency in judgment tendencies and priorities. </td>
<td>It is necessary to distinguish between short-term mood swings and long-term personality trends. </td>
</tr>
<tr>
<td><strong>Learning history</strong></td>
<td>How to incorporate new experiences and connect with previous trends. </td>
<td>It is natural for things to change as they learn, and the change itself cannot be immediately called a mismatch. </td>
</tr>
<tr>
<td><strong>Reaction to changes in conditions</strong></td>
<td>How do responses diverge under unlearning conditions and interventions? </td>
<td>Even if they are similar during normal times, there is a possibility that they will break down drastically due to branching. </td>
</tr>
<tr>
<td><strong>Longitudinal stability</strong></td>
<td>What is stable and what fluctuates within the day, between days, and over the long term? </td>
<td>It is not possible to see the persistence of identity with just one measurement. </td>
</tr>
</tbody>
</table>

<h2>What kind of continuity test do you want to consider</h2>

<h4>Tests you would like to include as examples</h4>
<ul>
<li><strong>Autobiographical memory alignment: Tracks not only the content of events, but also their associations and priorities. </li>
<li><strong>Preference stability:</strong>Looks at whether value judgments and choice trends persist beyond short-term noise. </li>
<li><strong>Learning continuity:</strong>After giving new information, see if the update method connects with the original trend. </li>
<li><strong>Branch verification:</strong>When changing conditions, record the point at which it should be treated as a separate individual. </li>
<li><strong>Long-term drift monitoring:</strong> Track characteristics that change and characteristics that don't change over days or weeks. </li>
</ul>

<p>In particular, if you want to organize only the entrance of longitudinal evaluation first, <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/state-trait-and-drift">Wiki: state/trait/drift</a> is a supplementary lecture. </p>

<h2>Why pre-registration is especially important</h2>
<p>
Evaluations of a person's personality can be interpreted in any way that suits them in hindsight. That's why it is necessary to <strong>pre-register</strong> ``what to consider as a match,'' ``to what degree of deviation to suspend,'' and ``which branches to treat as separate individuals.''
</p>

<strong>Things you should decide first</strong>
<p>
These are test items, scoring rules, observation period, failure conditions, stopping conditions, and handling of branching. In L4, if this part is ambiguous, the entire conclusion will be shaken.
</p>

<h2>What is difficult when branching occurs</h2>
<p>
If the two systems start learning separately at some point, they may start out almost the same, but over time they will have different histories. At this time, the question is ``to what point should they be treated as the same evaluation unit?'' and ``at what point should they be separated as separate entities?''
</p>
<p>
Therefore, when evaluating L4, it is important to consider not only similarity but also <strong>branch log</strong> and <strong>version control</strong>.
</p>
<p>
If you want to clarify the differences between branching points, branch IDs, stop conditions, and kill switches first, <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/update-branching-and-stop-rules">Wiki: Update/branching/stop rules</a> is a supplementary lecture.
</p>

<h2>Things you shouldn't say at this stage</h2>
<table>
<thead>
<tr>
<th>Expressions that are easy to overstate</th>
<th>Safer reading</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Identity verified</strong></td>
<td>There have been no major discrepancies so far in the pre-registered continuity test group. </td>
</tr>
<tr>
<td><strong>Same person completely saved</strong></td>
<td>Preliminary evaluation regarding memory, values, learning, and branching has been established. </td>
</tr>
<tr>
<td><strong>Same in the long run</strong></td>
<td>No significant drift was observed in the defined indicators within the observation period. </td>
</tr>
</tbody>
</table>

<h2>Minimum checks when reading L4 stories</h2>

<h4>Checklist</h4>
<ul>
<li><strong>What do you consider to be continuous:</strong>Whether you are looking at memory, values, learning, branching, or longitudinal. </li>
<li><strong>Are there pre-registrations?</strong>Are the criteria changed later? </li>
<li><strong>Are there any failure conditions?</strong>Are there any discrepancies that will cause the project to be put on hold? </li>
<li><strong>Is the observation period sufficient?</strong>Does a single match indicate long-term identity? </li>
</ul>

<h2>Where to go back next</h2>
<p>
If you want to go back to the philosophy-oriented entrance, please use <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/personhood-and-copy-problem">Identity and the copy problem</a>, if you want to go back to the L4 position, please use <a href="https://mind-upload.com/wbe_101.html">Introduction to WBE</a>, and if you want to go back to verification design, please use <a href="https://mind-upload.com/verification.html">Verification infrastructure</a>.
</p>
