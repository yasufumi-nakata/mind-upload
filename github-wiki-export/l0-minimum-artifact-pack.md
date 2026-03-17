# Wiki: Minimum artifact pack for L0

> Auxiliary page for checking 'Minimal Loop' in the form of submissions
>
> This learning page is generated for GitHub Wiki. The public portal is managed on [mind-upload.com](https://mind-upload.com).

- Updated: 2026-03-14 / Role: Operational guide

## Role Of This Page
This page is an auxiliary page that organizes what should be finalized as a set when creating a reproducible analysis of L0. Rather than a procedure manual, it is used to focus on the form of the submission and check ``what is necessary for a third party to rerun?''

## Accuracy Notes
What we are dealing with here is the bare minimum of L0. Although this alone will not allow us to proceed to a discussion of causal claims or identity, it is important as a starting point for comparison.

## Back To Public Pages
- [Hands-on](https://mind-upload.com/datasets.html#l0-practice)
- [Data & Bench](https://mind-upload.com/datasets.html)
- [Verification base](https://mind-upload.com/verification.html)

## Related Wiki Pages
- [Wiki: Basics of verification infrastructure](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - You can see from the beginning why artifacts are fixed first.
- [Wiki: Data partitioning and leaks](https://github.com/yasufumi-nakata/mind-upload/wiki/dataset-splits-and-leakage) - Supplements the reason why splitting rules go into artifacts.
- [Wiki: Baseline/Pre-registration/Model Card](https://github.com/yasufumi-nakata/mind-upload/wiki/baselines-prereg-and-model-cards) - Compensates for the role differences between baseline and failure examples.

## What Is Currently Known
- For L0, it is more important than high accuracy that a third party can rerun under the same conditions.
- Comparability is greatly improved just by having the BIDS format, QC logs, splitting rules, and baselines in place.
- Even if the dataset name is the same, if the snapshot or version is different, it will not be reproduced.
- Examples of failures and known stumbling blocks should be included as part of the deliverables.

## What Is Still Unknown
- Which baselines and QC metrics ultimately work best will vary from challenge to challenge.
- Beyond L0, the extent to which it will be extended to L1/L2 standard deliverables will depend on future development.

---

<h2>First, think in terms of one pack</h2>
<p>
The L0 artifact is not a single file or a single score. Only when the <strong>version of the input</strong>, <strong>form of the input</strong>, <strong>quality trail</strong>, <strong>evaluation rules</strong>, and <strong>re-execution steps</strong> are in place can a third party track the results.
</p>

<h2>Minimum 8 points you want to have in L0</h2>
<table>
<thead>
<tr>
<th>Deliverables</th>
<th>Minimum desired contents</th>
<th>What is the problem if it is missing</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. Data version</strong></td>
<td>OpenNeuro snapshot, PhysioNet version, DOI, acquisition date, or persistent URL. </td>
<td>Even with the same dataset name, different versions are mixed, making it impossible to reproduce. </td>
</tr>
<tr>
<td><strong>2. Data skeleton</strong></td>
<td>BIDS skeleton, minimum metadata, task name, electrode information. </td>
<td>Different people cannot have the same input, and the starting points for comparison will not be the same. </td>
</tr>
<tr>
<td><strong>3. Standards confirmation results</strong></td>
<td>The reason for the warning left by the BIDS Validator. </td>
<td>It is easier to overlook non-shareable standard violations. </td>
</tr>
<tr>
<td><strong>4. QC log</strong></td>
<td>Numerical record of missingness, noise, artifacts, and reasons for exclusion. </td>
<td>Which data is bad will depend on the person, and reproducibility will be broken. </td>
</tr>
<tr>
<td><strong>5. Split rule</strong></td>
<td>Within-session / cross-session / cross-subject, train/test unit, leak prevention rules, promise not to touch test. </td>
<td>Unable to see the upward swing in the numbers, the entire evaluation collapses. </td>
</tr>
<tr>
<td><strong>6. Baseline results</strong></td>
<td>One simple indicator, settings and results table. </td>
<td>There will be no starting point for claiming improvements. </td>
</tr>
<tr>
<td><strong>7. Execution steps</strong></td>
<td>Commands, environments, random numbers, preprocessing conditions, known stumbling blocks. </td>
<td>Other people cannot rerun the same flow. </td>
</tr>
<tr>
<td><strong>8. Failure example</strong></td>
<td>Excluded conditions, settings that did not work, and points to note. </td>
<td>Only successes remain, and the next person repeats the same failure. </td>
</tr>
</tbody>
</table>

<h2>In short,</h2>

<h4>Pack</h4>
<ul>
<li><strong>Input:</strong> Fixed version + BIDS shape</li>
<li><strong>Quality:</strong> QC and Validator</li>
<li><strong>Evaluation:</strong> Split rules and baselines</li>
<li><strong>Replay:</strong> Execution steps and failure examples</li>
</ul>

<h2>Common omissions</h2>
<table>
<thead>
<tr>
<th>Common conditions</th>
<th>What is still missing</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>dataset name exists</strong></td>
<td>Snapshot, version, DOI, and acquisition date may not remain. </td>
</tr>
<tr>
<td><strong>Waveform file is available</strong></td>
<td>Events, synchronization, bad segments, and issue definitions may be missing. </td>
</tr>
<tr>
<td><strong>Accuracy is there</strong></td>
<td>There may be no difference from the splitting rule, leak check, or baseline. </td>
</tr>
<tr>
<td><strong>There is a code</strong></td>
<td>Environment, random numbers, execution order, and known failure conditions may not be written. </td>
</tr>
<tr>
<td><strong>I thought I did QC</strong></td>
<td>Numeric logs and exclusion reasons may not remain. </td>
</tr>
</tbody>
</table>

<h2>Simple judgment of L0 completion</h2>
<table>
<thead>
<tr>
<th>Question</th>
<th>If yes, move forward</th>
<th>If no, what to do next</th>
</tr>
</thead>
<tbody>
<tr>
<td>Can other people have the same version of input</td>
<td>Snapshot / version / DOI and BIDS skeleton are complete. </td>
<td>Fix the data version and skeleton first. </td>
</tr>
<tr>
<td>Do you know what data was excluded?</td>
<td>QC logs and exclusion reasons remain. </td>
<td>Download to numerical log. </td>
</tr>
<tr>
<td>Can you explain how to make numbers</td>
<td>Split rules and baselines are fixed. </td>
<td>Fix train/test and comparison partner first. </td>
</tr>
<tr>
<td>Can someone else run it again</td>
<td>Command, environment, and known failure conditions remain. </td>
<td>Create a short runbook. </td>
</tr>
</tbody>
</table>

<strong>What this page doesn't do</strong>
<p>
Here we do not decide which model is the strongest or which indicators are ultimately correct. The first objective of L0 is to create a comparable starting point.
</p>

<h2>Where to return next</h2>
<p>
Return to <a href="https://mind-upload.com/datasets.html#l0-practice">Hands-On</a> if you want to follow the actual steps, <a href="https://mind-upload.com/datasets.html">Data & Bench</a> if you want to reselect the input data, or return to <a href="https://mind-upload.com/verification.html">Verification Infrastructure</a> if you want to see how this product stacks up as a public good.
</p>
