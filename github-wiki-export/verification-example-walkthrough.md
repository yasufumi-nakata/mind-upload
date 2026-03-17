# Wiki: Verification example walkthrough

> Read the blueprint by reducing it to one small example
>
> This learning page is generated for GitHub Wiki. The public portal is managed on [mind-upload.com](https://mind-upload.com).

- Updated: 2026-03-14 / Role: Worked example

## Role Of This Page
This page is a wiki where you can read the Verification Commons blueprint in order by converting it into a "small example of state classification using EEG". Rather than increasing the number of abstract words, visualize how input, procedure, evaluation, and falsification are connected.

## Accuracy Notes
This is a minimal example for understanding. This alone does not support WBE's strong claims; it is a supplementary course that embodies the entrance to L0-L2.

## Back To Public Pages
- [Verification platform](https://mind-upload.com/verification.html)
- [hands-on](https://mind-upload.com/datasets.html#l0-practice)
- [Data & Bench](https://mind-upload.com/datasets.html)

## Related Wiki Pages
- [Wiki: Basics of verification infrastructure](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - This is for people who want to get an overview of the role first.
- [Wiki: Data partitioning and leaks](https://github.com/yasufumi-nakata/mind-upload/wiki/dataset-splits-and-leakage) - This complements the train/test bounds assumed in this example.
- [Wiki Home](https://github.com/yasufumi-nakata/mind-upload/wiki) - You can return to other auxiliary pages.

## What Is Currently Known
- You can also practice creating a minimal form of Verification Commons with public EEG data.
- Simply keeping inputs, procedures, evaluations, and counterevidence separate greatly increases comparability.
- Even in small cases, leak prevention and failure recording are essential.

## What Is Still Unknown
- Small examples like this alone do not allow us to proceed to the examination of identity or phenomenal consciousness.
- Which tasks have the strongest connections to future L3 and beyond is still being explored.

---

<h2>This small example</h2>
<p>
Here, we will use a small model that uses public EEG data to classify two states as an example. The goal is not to achieve high accuracy, but to understand<strong>the smallest set that others can check under the same conditions</strong>.
</p>

<h2>Arrange the four parts first</h2>
<table>
<thead>
<tr>
<th>Parts</th>
<th>What to put in this example</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Data Standard</strong></td>
<td>EEG data in BIDS format, subject information, event definitions, and QC logs. </td>
</tr>
<tr>
<td><strong>Benchmark</strong></td>
<td>What to predict, which division to compare, and which index to score. </td>
</tr>
<tr>
<td><strong>Registry</strong></td>
<td>This is a record in which preprocessing conditions, division rules, stopping conditions, and baselines are fixed in advance. </td>
</tr>
<tr>
<td><strong>Model Card</strong></td>
<td>Summary of final scores, failure examples, leak tests, weaknesses, and calculation conditions. </td>
</tr>
</tbody>
</table>

<h2>Step 1: First, fix the input shape</h2>
<p>
Even with the same EEG data, missing event definitions and electrode information will prevent others from reproducing the same analysis. The first thing you need isn't an "amazing model"; you need <strong>a clear idea of ​​what you're passing as input</strong>.
</p>

<h4>What you want at least</h4>
<ul>
<li><strong>BIDS format:</strong> Matches file placement and metadata format. </li>
<li><strong>QC Log:</strong>Leaves missing, noisy, and exclusion reasons. </li>
<li><strong>Division unit:</strong>Specify whether it is by subject or session. </li>
</ul>

<h2>Step 2: Fix the comparison method</h2>
<p>
Next, put Benchmark. This is the part where you decide what to consider as the correct answer and what to compare it with. If this is vague, you will be able to escape to a more convenient indicator later.
</p>
<table>
<thead>
<tr>
<th>Item</th>
<th>Fixed content in this example</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Assignment</strong></td>
<td>2 Do the state classification and fix it first. </td>
</tr>
<tr>
<td><strong>Split</strong></td>
<td>Separate train/validation/test for each subject. </td>
</tr>
<tr>
<td><strong>Indicators</strong></td>
<td>In addition to accuracy, it also records confusion matrices and failure examples. </td>
</tr>
<tr>
<td><strong>Baseline</strong></td>
<td>Place one simple classifier and check the improvement. </td>
</tr>
</tbody>
</table>

<h2>Step 3: Leave a promise before doing it</h2>
<p>
Registry is a component that prevents you from changing the conditions later and assuming you won. For example, first write down which preprocessing to use, when to stop it, and where to not use test.
</p>

<strong>What I would like to write here first</strong>
<p>
These are preprocessing candidates, division rules, baselines, scoring indicators, conditions for failure, and what to keep as differences when updating. Being able to read and audit later is more important than fancy formatting.
</p>

<h2>Step 4: Finally, publish with Model Card</h2>
<p>
In the end, what we need to do is not just announce the scores, but also record ``where we won and where we collapsed.'' This is the role of the Model Card.
</p>

<h4>Minimum items you want to include</h4>
<ul>
<li><strong>Results:</strong>Key metrics, differences from baseline, rerun conditions. </li>
<li><strong>Leak check:</strong>Is test information mixed in during splitting or preprocessing? </li>
<li><strong>Example of failure:</strong>For which subjects and under what conditions does it tend to collapse? </li>
<li><strong>Weaknesses:</strong>OOD, noise, computational cost, known limitations. </li>
</ul>

<h2>What you can learn/don't understand from this example</h2>
<table>
<thead>
<tr>
<th>What you can learn from this example</th>
<th>Things you can't understand from this example only</th>
</tr>
</thead>
<tbody>
<tr>
<td>How to create a reproducible minimum loop between L0 and L1. </td>
<td>Individuality, phenomenal consciousness, conditions for L4 and beyond. </td>
</tr>
<tr>
<td>A form of comparable evaluation that avoids leaks. </td>
<td>Strong causal claims that include interventions and closed loops. </td>
</tr>
<tr>
<td>What should I record to make it easier for others to try again? </td>
<td>Which theory is ultimately correct as an explanation of consciousness? </td>
</tr>
</tbody>
</table>

<h2>Where to go back next</h2>
<p>
If you want to go back to the blueprint itself, read <a href="https://mind-upload.com/verification.html">Verification Foundation</a>, if you want to actually run the minimal loop, read <a href="https://mind-upload.com/datasets.html#l0-practice">Hands-on</a>, and if you want to review the input data, read <a href="https://mind-upload.com/datasets.html">Data & Bench</a>.
</p>
