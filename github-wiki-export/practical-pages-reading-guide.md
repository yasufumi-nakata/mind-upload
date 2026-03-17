# Wiki: Guide to reading practical pages

> Map to avoid mixing victory conditions, entrance data, work procedures, reference examples, and proposal organization
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-14 / 位置づけ: Reading guide

## このページの役割
This page is an auxiliary guide to help you distinguish between Mind-Upload's practice-oriented public pages. Verification is a victory condition, Datasets is entry data, L0 practice section in Datasets is a minimum loop procedure, casework section in Verification is a reference example, and proposal integration section in Issue is a proposal organization. Although they may look similar, they have different roles.

## 正確さの前提
What we are dealing with here is the difference in the roles of pages. Please check the details of the actual verification conditions and procedures on each main page.

## 公開ページへ戻る
- [Verification base](https://mind-upload.com/verification.html)
- [Data & Bench](https://mind-upload.com/datasets.html)
- [L0 practice](https://mind-upload.com/datasets.html#l0-practice)

## 関連 Wiki
- [Wiki: Guide to reading public pages](https://github.com/yasufumi-nakata/mind-upload/wiki/public-page-reading-guide) - This is for people who want to see the role differences across public pages.
- [Wiki: Minimum artifact pack for L0](https://github.com/yasufumi-nakata/mind-upload/wiki/l0-minimum-artifact-pack) - This is for people who want to check their L0 practice section submissions in one page.
- [Wiki: Standards/Location/Validator/Benchmark](https://github.com/yasufumi-nakata/mind-upload/wiki/standards-repositories-validators-and-benchmarks) - Compensates for differences in casework clauses in Verification and operational words that appear in Verification.
- [Wiki: Baseline/Pre-registration/Model Card](https://github.com/yasufumi-nakata/mind-upload/wiki/baselines-prereg-and-model-cards) - Organize what should remain on the practice page by role.

## いま分かっていること
- Verification, Datasets, L0 practice section within Datasets, casework section within Verification, and proposal integration section within Issues are all practical-oriented, but their roles are different.
- Verification is the definition of progress, Datasets is the entry selection, the L0 practice section in Datasets is the procedure, the casework section in Verification is the design reference, and the proposal integration section in Issue is the proposal organization.
- If you separate the roles of pages first, it will be difficult to misread the practical guidance.

## まだ分かっていないこと
- We have not yet determined which practical route will be most effective for future L2 and L3.
- Which practice pages will be expanded independently in the future will change depending on the accumulation of operations.

---

<h2>First divide into 5 parts</h2>
<p>
All of the practical pages are ``pages that are useful for work,'' but the difference is in what pages you decide on. If you first divide it into <strong>victory conditions</strong>, <strong>entry data</strong>, <strong>work procedures</strong>, <strong>reference examples</strong>, and <strong>proposal organization</strong>, the practical guidance will become much more stable.
</p>

<strong>When you want to see only the order from EEG to L0 in a straight line</strong>
<p>
If you would like to follow the sequence from EEG introduction to Datasets, L0 practice section, and Verification rather than looking at the role differences on the practical page, please see <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-to-l0-route">One ​​straight path from EEG to L0</a>.
</p>

<strong>When you just want to decide what to see after Verification</strong>
<p>
After understanding the differences in the roles of practical pages, if you want to see in one page just which route to take next from Verification, please see <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/verification-next-routes">Four paths to take after Verification</a>.
</p>

<h2>Differences in the roles of practical pages</h2>
<table>
<thead>
<tr>
<th>Page</th>
<th>Main role</th>
<th>First question</th>
<th>What is not enough here</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong><a href="https://mind-upload.com/verification.html">Verification</a></strong></td>
<td>This is a blueprint that determines victory conditions and counter-conditions. </td>
<td>This is when you want to fix "what needs to be met to move forward" first. </td>
<td>Actual entry data and work procedures must be supplemented with Datasets and L0 practice sections. </td>
</tr>
<tr>
<td><strong><a href="https://mind-upload.com/datasets.html">Datasets</a></strong></td>
<td>This is the page for selecting entrance data. </td>
<td>The first thing you want to do is decide which public data to start L0 with. </td>
<td>What to leave behind as a deliverable must be supplemented with L0 practice section and Verification. </td>
</tr>
<tr>
<td><strong><a href="https://mind-upload.com/datasets.html#l0-practice">L0 Practice Section</a></strong></td>
<td>This is a procedure manual for creating a minimum loop. </td>
<td>Now is the time to connect analyzes that can be reproduced right here and now. </td>
<td>The design reason why the step is necessary should be supplemented with Verification. </td>
</tr>
<tr>
<td><strong><a href="https://mind-upload.com/verification.html#casework">Casework section</a></strong></td>
<td>A reference collection for learning design patterns from successful examples in other fields. </td>
<td>Now is the time to see an example of why Standard, Storage, Bench, and Pre-registration worked. </td>
<td>This example alone cannot prove that WBE holds true. </td>
</tr>
<tr>
<td><strong><a href="https://mind-upload.com/issue.html#proposal-integration">Proposal integration section</a></strong></td>
<td>This is a summary table that summarizes the status and basis of the proposal group. </td>
<td>This is the time to track which proposals were aimed at and to what extent they were reflected. </td>
<td>It is not possible to say that the implementation is complete just by looking at the summary; it is necessary to return to the issue and the original text. </td>
</tr>
</tbody>
</table>

<h2>If you have this question, please check this page</h2>
<table>
<thead>
<tr>
<th>What I want to know now</th>
<th>First page to open</th>
<th>Next page</th>
</tr>
</thead>
<tbody>
<tr>
<td>I want to know what needs to be met to call progress</td>
<td><a href="https://mind-upload.com/verification.html">Verification</a></td>
View dependencies in <td><a href="https://mind-upload.com/tech_roadmap.html">Roadmap</a>. </td>
</tr>
<tr>
<td>I want to decide which public data to use first</td>
<td><a href="https://mind-upload.com/datasets.html">Datasets</a></td>
<td><a href="https://mind-upload.com/datasets.html#l0-practice">L0 practice section</a> Proceed to work on L0. </td>
</tr>
<tr>
<td>I want to know what to actually keep as a set</td>
<td><a href="https://mind-upload.com/datasets.html#l0-practice">L0 practice section</a></td>
Complements <td><a href="https://mind-upload.com/verification.html">Verification</a> and <a href="https://mind-upload.com/datasets.html">Datasets</a>. </td>
</tr>
<tr>
<td>I would like to see historical examples of why standards and benches are necessary</td>
<td><a href="https://mind-upload.com/verification.html#casework">Casework section</a></td>
Go back to <td><a href="https://mind-upload.com/verification.html">Verification</a> and check against the current design. </td>
</tr>
<tr>
<td>I want to distinguish between proposed and implemented ones</td>
<td><a href="https://mind-upload.com/issue.html#proposal-integration">Proposal integration section</a></td>
Return to <td><a href="https://mind-upload.com/issue.html">Issue</a> and the original clause. </td>
</tr>
<tr>
<td>I want to decide where to add/update</td>
<td><a href="https://mind-upload.com/content_hub.html">Content Hub</a></td>
<td><a href="https://mind-upload.com/issue.html">Issue</a> down to executable tasks. </td>
</tr>
</tbody>
</table>

<h2>Differences between pages that look similar</h2>
<table>
<thead>
<tr>
<th>Groups that look alike</th>
<th>The difference in one word</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Verification / L0 practice section</strong></td>
<td>Verification is the passing condition, and L0 practice clause is the working order of the minimum loop. </td>
</tr>
<tr>
<td><strong>Datasets / L0 Practice Section</strong></td>
<td>What to start with Datasets, and how to go around it in the L0 practice section. </td>
</tr>
<tr>
<td><strong>Verification / Casework Section</strong></td>
<td>Verification is the current design, Casework section is a type borrowed from other fields. </td>
</tr>
<tr>
<td><strong>Proposal integration section / Issue</strong></td>
<td>The proposal integration section organizes the main text of the proposal, and the issue section deals with cutting tasks here and now and managing external dependencies. </td>
</tr>
</tbody>
</table>

<h2>Common ways to get lost</h2>

<h4>Mistake</h4>
<ul>
<li><strong>I feel like I've progressed just by looking at Datasets:</strong> What to leave as a deliverable must be fixed in the L0 practice section and Verification. </li>
<li><strong>Misreading the L0 practice section as the definition of victory conditions:</strong> The procedure manual alone does not determine what is called progress. </li>
<li><strong>Read the casework section as direct evidence:</strong> This is a design reference, not a proof that WBE holds. </li>
<li><strong>Read the proposal integration section as a list of implementation completion:</strong> Proposal acceptance and document reflection are different from implementation completion and external agreement. </li>
</ul>

<h2>Where to return next</h2>
<p>
If you want to go back to the practical entry point, please use <a href="https://mind-upload.com/verification.html">Verification Platform</a>. If you want to go back to the actual L0 work, please use <a href="https://mind-upload.com/datasets.html#l0-practice">L0 Practice</a>. If you want to decide where to update, please use <a href="https://mind-upload.com/content_hub.html">Public Content Integration Hub</a>.
</p>
