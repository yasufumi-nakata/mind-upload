# Wiki: Basics of verification infrastructure

> Before making flashy claims, create a yardstick and a place for records.
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-14 / 位置づけ: Beginner guide

## このページの役割
This page is a wiki that explains from the beginning why Mind-Upload focuses on "standards, benches, registration, and audits." The purpose is to learn not only the technical content but also the operational side to make comparable progress.

## 正確さの前提
The analogy used here is to aid understanding. Don't think you understand it by analogy; please go back to the specifications on the public page and check the actual design.

## 公開ページへ戻る
- [Verification platform](https://mind-upload.com/verification.html)
- [case work](https://mind-upload.com/verification.html#casework)
- [Data & Bench](https://mind-upload.com/datasets.html)

## 関連 Wiki
- [Wiki: How to read claims and evidence](https://github.com/yasufumi-nakata/mind-upload/wiki/claims-and-evidence) - I will explain why this foundation is necessary to distinguish between claims.
- [Wiki: Basics of WBE](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-basics) - This is for people who want to go back and read the big picture.
- [Wiki: Baseline/Pre-registration/Model card](https://github.com/yasufumi-nakata/mind-upload/wiki/baselines-prereg-and-model-cards) - We will organize the differences in the roles of operational words from the beginning.
- [Wiki Home](https://github.com/yasufumi-nakata/mind-upload/wiki) - You can return to other basic pages.

## いま分かっていること
- Comparable progress requires four things: input, evaluation, rules, and records.
- Without pre-registration and auditing, success conditions can be changed at a later date.
- Progress has been accelerated in the development of public goods in other areas, such as PDB and BIDS.

## まだ分かっていないこと
- A final benchmark dedicated to WBE does not yet exist in complete form.
- Which additional requirements are sufficient for L4 or L5 is still a matter of research and societal debate.

---

<h2>Why “ruler” comes first</h2>
<p>
If you take a school test and compare the answer sheets and grading standards, saying ``this one is smarter,'' the results will be difficult to trust. It's the same with WBE: if you don't have data, evaluations, failure conditions, and a place to store your records, you won't be able to compare them even if you say you've made progress.
</p>

<h2>Comparing the four parts to a school test</h2>
<table>
<thead>
<tr>
<th>Parts</th>
<th>Role</th>
<th>Parable</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Data Standard</strong></td>
<td>Align input form</td>
<td>It is the same answer sheet. </td>
</tr>
<tr>
<td><strong>Benchmark</strong></td>
<td>Align issues and indicators for comparison</td>
<td>Same scoring criteria. </td>
</tr>
<tr>
<td><strong>Registry / Prereg</strong></td>
<td>Fix the rules before doing it</td>
<td>These are the implementation guidelines distributed before the exam. </td>
</tr>
<tr>
<td><strong>Audit (Audit / Model Card)</strong></td>
<td>Leave examples of failures and weaknesses</td>
<td>This is a report card that shows not only your score, but also mistakes and reexamination requirements. </td>
</tr>
</tbody>
</table>

<h2>What happens if one is missing</h2>
<table>
<thead>
<tr>
<th>What is missing</th>
<th>Problems that occur</th>
</tr>
</thead>
<tbody>
<tr>
<td>Standard</td>
<td>You won't know if you are looking at the same input. </td>
</tr>
<tr>
<td>Benchmark</td>
<td>Everyone can say they won using a different yardstick. </td>
</tr>
<tr>
<td>Pre-registration</td>
<td>It will be easier to select only convenient conditions later and treat it as a success. </td>
</tr>
<tr>
<td>Audit</td>
<td>Scores take on a life of their own, and weaknesses and leaks become invisible. </td>
</tr>
</tbody>
</table>

<h2>Why is it especially important for WBE</h2>
<p>
WBE is a field where level changes can easily occur due to the large scale of the story. Accidents such as talking about L1 results as if they were L4, making correlation seem like cause and effect, and treating partial successes as if they were the whole are easy to happen. That's why you need to fix<strong>how you evaluated</strong>not just the results.
</p>

<h2>How this site is used</h2>
<p>
In Mind-Upload, the Verification page is the blueprint, Hands-on is the minimum implementation, Datasets are the entry data, and Casework is the precedent for other fields. The wiki is there to supplement that prerequisite knowledge.
</p>
<p>If you would like to organize the role differences between baseline, preregistration, model cards, and failure examples in more detail, <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/baselines-prereg-and-model-cards">Wiki: Baselines, preregistration, and model cards</a> is a supplementary lecture. </p>

<h4>Next</h4>
<p>If you want to see the actual blueprint after reading this basics, click here. </p>
<a href="https://mind-upload.com/verification.html">Go to verification infrastructure page →</a>
