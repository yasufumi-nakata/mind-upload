# Wiki: How to read claims and evidence

> Don't let flashy wording lead to strong conclusions.
>
> This learning page is generated for GitHub Wiki. The public portal is managed on [mind-upload.com](https://mind-upload.com).

- Updated: 2026-03-06 / Role: Reading guide

## Role Of This Page
This page is a guide to help you read the strong language that comes up in the talk of neuroscience and Mind-Upload by bringing it back to the strength of the necessary evidence. Practice differentiating between ``It looks amazing'' and ``What has been proven?''

## Accuracy Notes
The organization here is not to weaken the argument, but to prevent both overestimation and underestimation.

## Back To Public Pages
- [Introduction to WBE](https://mind-upload.com/wbe_101.html)
- [Verification platform](https://mind-upload.com/verification.html)
- [FAQ](https://mind-upload.com/faq.html)

## Related Wiki Pages
- [Wiki: Basics of WBE](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-basics) - This is the overall picture that is the premise of this reading.
- [Wiki: Basics of verification infrastructure](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - I will explain why the placement of evidence itself is important.
- [Wiki Home](https://github.com/yasufumi-nakata/mind-upload/wiki) - You can return to other basic pages.

## What Is Currently Known
- Reproducible analysis and claims of identity differ greatly in the strength of evidence required.
- There is a difference between the output being correct and the internal mechanism being correct.
- It is safe to read strong claims without conditions to disprove them or steps to reproduce them.

## What Is Still Unknown
- It has not yet been decided at what stage L4 will proceed to assert its identity.
- We are not yet at the stage where we can completely integrate the differences between theories into one evaluation axis.

---

<h2>Basic rules</h2>
<p>
The language in research publications often appears stronger than the actual evidence. Therefore, first, think about where to place ``What did this result do?'' from L0 to L5. The higher the level, the more evidence you need.
</p>

<h2>Rephrasing L0-L5 in everyday language</h2>
<table>
<thead>
<tr>
<th>Level</th>
<th>Roughly speaking</th>
<th>Minimum evidence you want</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>L0</strong></td>
<td>Get the same result again</td>
<td>The data, code, environment, and logs are complete and can be reproduced by a third party. </td>
</tr>
<tr>
<td><strong>L1</strong></td>
<td>You can guess something from the signal</td>
<td>Reproducibility accuracy with baseline comparison, leak inspection, and matching conditions. </td>
</tr>
<tr>
<td><strong>L2</strong></td>
<td>Can be predicted even if conditions are changed</td>
<td>Predictive matching for unlearning conditions, counterfactuals, and interventions. </td>
</tr>
<tr>
<td><strong>L3</strong></td>
<td>Stable operation in closed loop</td>
<td>Real-time operation, delay management, safe stop conditions. </td>
</tr>
<tr>
<td><strong>L4</strong></td>
<td>Discussing identity</td>
<td>Pre-registered continuity test, branch verification of memory, values, and learning. </td>
</tr>
<tr>
<td><strong>L5</strong></td>
<td>Can be used in society</td>
<td>System design including rights, consent, suspension criteria, and audit structure. </td>
</tr>
</tbody>
</table>

<h2>Translating common phrases</h2>
<table>
<thead>
<tr>
<th>How to write headings</th>
<th>What is most likely actually being said</th>
<th>Additional things to check</th>
</tr>
</thead>
<tbody>
<tr>
<td>"Recovered sentences from the brain"</td>
<td>Mostly L1 decoding. </td>
<td>We will see if it holds true even under unlearning conditions, and if it is different from LLM completion. </td>
</tr>
<tr>
<td>"Reproduced the brain state with high precision"</td>
<td>L1, at best, may be the entrance to L2. </td>
<td>Check whether you are looking at predictions for condition changes and interventions. </td>
</tr>
<tr>
<td>"Behaved just like a human"</td>
<td>There is a possibility that the story remains that the behavior is similar in appearance. </td>
<td>Check whether the internal state, memory continuity, and failure conditions are exposed. </td>
</tr>
<tr>
<td>“Now you can save your identity”</td>
<td>This is a very strong argument for L4. </td>
<td>It is necessary to have a pre-registered identity test or to eliminate alternative explanations. </td>
</tr>
</tbody>
</table>

<h2>Three points to check when reading</h2>

<h4>Checklist</h4>
<ul>
<li><strong>This is somewhere between L0 and L5:</strong>First, put the strength of your argument. </li>
<li><strong>What was measured:</strong>Look at whether it is just output matching or whether it includes condition changes and interventions. </li>
<li><strong>What's a failure?</strong> Check if there are counter-conditions and steps to reproduce. </li>
</ul>

<h2>What is missing to advance to the next level of argument</h2>
<p>
Even if you have the results for L1, you can't jump straight to L4. Normally, we first solidify the reproducibility of L0, then test changing the conditions of L2, and proceed by separating out any remaining points. In other words,<strong>a higher level cannot jump over a lower level</strong>.
</p>

<h4>Next</h4>
<p>Here is the concept of "standards, benches, registration, and audits" that supports this reading. </p>
<a href="https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics">To the basics of verification infrastructure →</a>
