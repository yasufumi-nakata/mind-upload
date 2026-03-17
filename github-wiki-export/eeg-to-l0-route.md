# Wiki: Straight path from EEG to L0

> From an introduction to EEG to reproducible analysis, a practical route to avoid getting lost
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-14 / 位置づけ: Practical route

## このページの役割
This page is a practical guide that, after reading the basics of EEG, organizes in a straight line which public data to start with, what to keep as a set, and where to check the victory conditions. Use it as an auxiliary line to make it easier to go back and forth between EEG 101, Datasets, Hands-on, and Verification.

## 正確さの前提
What we will deal with here is the entrance to reproducible analysis of L0. Arguments after L1 and discussions of identity will not be dealt with only through this route.

## 公開ページへ戻る
- [Introduction to EEG](https://mind-upload.com/eeg_101.html)
- [Data & Bench](https://mind-upload.com/datasets.html)
- [Hands-on](https://mind-upload.com/datasets.html#l0-practice)

## 関連 Wiki
- [Wiki: Basics of EEG](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-basics) - For those who want to go back to the basics of EEG signals and noise.
- [Wiki: Guide to reading practical pages](https://github.com/yasufumi-nakata/mind-upload/wiki/practical-pages-reading-guide) - You can first sort out the role differences between Datasets, Hands-on, and Verification.
- [Wiki: Minimum artifact pack for L0](https://github.com/yasufumi-nakata/mind-upload/wiki/l0-minimum-artifact-pack) - See in one piece what you'll end up with.
- [Wiki: Data partitioning and data leaks](https://github.com/yasufumi-nakata/mind-upload/wiki/dataset-splits-and-leakage) - It's for people who don't want to redo it in split units or in case of a leak accident.
- [Wiki: Event synchronization and observation log](https://github.com/yasufumi-nakata/mind-upload/wiki/event-sync-and-measurement-logs) - Complete what's left of raw EEG.

## いま分かっていること
- After understanding the basics of EEG, the flow of creating L0 with public data is relatively clear.
- In L0, it is more important to have reproducible input, QC, processing, output, and auditing cycles than high accuracy.
- Datasets, Hands-on, and Verification have different roles even in the same practice.

## まだ分かっていないこと
- We have not yet determined which starter data will most lead to future L2 and L3.
- After L0, which task is the shortest way to proceed to generation/intervention prediction is task dependent.

---

<h2>Proceed in one direction</h2>
<p>
After learning EEG, it's easy to get confused about <strong>whether to select data next</strong>,<strong>to move your hand suddenly</strong>, or<strong>to check the victory conditions</strong> first. In this route, the order is fixed to one path.
</p>

<h2>6 steps from EEG to L0</h2>
<table>
<thead>
<tr>
<th>Order</th>
<th>Page to open</th>
<th>What to decide here</th>
<th>Conditions for proceeding to the next</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1</strong></td>
<td><a href="https://mind-upload.com/eeg_101.html">EEG 101</a></td>
<td>Understand what EEG can measure and what it cannot say on its own. </td>
<td>Once you have established the premise that EEG is not to be read as a magical mind-reading technique, proceed to the next step. </td>
</tr>
<tr>
<td><strong>2</strong></td>
<td><a href="https://mind-upload.com/datasets.html">Datasets</a></td>
<td>First decide which public data to start L0 with. </td>
<td>Once you have narrowed down the starter data to one piece, proceed to the next step. </td>
</tr>
<tr>
<td><strong>3</strong></td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/dataset-splits-and-leakage">Data splits and data leaks</a></td>
<td>Fix the unit of train/test and the boundaries of test that should not be touched. </td>
<td>If you can write the division rule in text, proceed to the next step. </td>
</tr>
<tr>
<td><strong>4</strong></td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/event-sync-and-measurement-logs">Event synchronization and observation logs</a></td>
<td>In addition to raw EEG, decide what events, stimulation logs, synchronization, and bad segments should be saved as. </td>
<td> Once you have enumerated the minimum items in the observation log, proceed to the next step. </td>
</tr>
<tr>
<td><strong>5</strong></td>
<td><a href="https://mind-upload.com/datasets.html#l0-practice">Hands-on</a></td>
<td>Go through the steps of connecting BIDS, QC, pre-processing, baseline, and failure cases. </td>
<td>Once you have all the L0 deliverables, proceed to the next step. </td>
</tr>
<tr>
<td><strong>6</strong></td>
<td><a href="https://mind-upload.com/verification.html">Verification</a></td>
<td>Check what assertion level and what the L0 you just created satisfies. </td>
<td>It will be a break if we can explain without confusing L0 and L1 and beyond. </td>
</tr>
</tbody>
</table>

<h2>The last thing I want to leave behind on this one straight road</h2>

<h4>Artifact Pack</h4>
<ul>
<li><strong>Input:</strong>Data in BIDS format, metadata, events, synchronization information. </li>
<li><strong>Quality:</strong> Recording of QC logs, exclusion criteria, bad channels/bad segments. </li>
<li><strong>Processing:</strong>Pre-processing conditions, random numbers, version used, execution steps. </li>
<li><strong>Output:</strong>At least one baseline metric and its recurrence log. </li>
<li><strong>Audit:</strong>Examples of failures, conditions that went wrong, and known weaknesses. </li>
</ul>

<p>
If you would like to check only the form of the submission in one page, <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/l0-minimum-artifact-pack">L0 Minimum Artifact Pack</a> is the corresponding auxiliary page.
</p>

<h2>Where to return to on the way</h2>
<table>
<thead>
<tr>
<th>Place to stop</th>
<th>Page you should return to</th>
</tr>
</thead>
<tbody>
<tr>
<td>Stops in the sense of EEG itself</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-basics">EEG Basics</a> / <a href="https://mind-upload.com/eeg_101.html">EEG 101</a></td>
</tr>
<tr>
<td>Stops due to difference between Datasets and Hands-on</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/practical-pages-reading-guide">Reading guide for practical pages</a></td>
</tr>
<tr>
<td>Stops due to role difference between BIDS and Validator</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/standards-repositories-validators-and-benchmarks">Standards/Repositories/Validators/Benchmarks</a></td>
</tr>
<tr>
<td>Stops at baseline or pre-registration role</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/baselines-prereg-and-model-cards">Baselines/preregistration/model cards</a></td>
</tr>
<tr>
<td>Stops wherever you go after L0</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/claim-level-reading-routes">How to read each L0 to L5</a></td>
</tr>
</tbody>
</table>

<h2>Accidents that are likely to occur on this route</h2>

<h4>Mistake</h4>
<ul>
<li><strong>Create a model immediately after EEG 101:</strong> If you don't fix the data selection and segmentation rules first, the numbers will be distorted later. </li>
<li><strong>I think raw EEG is sufficient:</strong> Without events or synchronized logs, there is no comparable input. </li>
<li><strong>Completion of Hands-on can be read as success in L1 or L2:</strong> Let's start with the reproducible analysis of L0. </li>
<li><strong>Finishing without reading Verification at the end:</strong> If you do not clearly state what has been and is not yet satisfied, the level of the claim will be off. </li>
</ul>

<h2>Where to return next</h2>
<p>
If you want to go back to the entrance to EEG, go back to <a href="https://mind-upload.com/eeg_101.html">Introduction to EEG</a>. If you go back to the role differences in practical pages, go to <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/practical-pages-reading-guide">Reading Guide for Practical Pages</a>. If you want to see how to proceed after L0, go to <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/claim-level-reading-routes">How to read from L0 to L5</a> Please use.
</p>
