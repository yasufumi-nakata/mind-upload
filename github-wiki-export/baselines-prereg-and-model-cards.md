# Wiki: Baseline/Pre-registration/Model Card

> Thinking about 'what to compare, how to fix, and what to keep'
>
> This learning page is generated for GitHub Wiki. The public portal is managed on [mind-upload.com](https://mind-upload.com).

- Updated: 2026-03-15 / Role: Learning guide

## Role Of This Page
This page is a wiki that organizes from the beginning the differences in the roles of ``baseline,'' ``benchmark,'' ``pre-registration,'' ``model card,'' and ``failure example,'' which appear repeatedly in Mind-Upload. Use it as a scaffold to understand the difference between getting a high score and making comparable progress.

## Accuracy Notes
Here we will explain the differences in operational roles in an easy-to-understand manner. Please check the actual template and specifications on the public page.

## Back To Public Pages
- [Verification base](https://mind-upload.com/verification.html)
- [Hands-on](https://mind-upload.com/datasets.html#l0-practice)
- [Casework](https://mind-upload.com/verification.html#casework)

## Related Wiki Pages
- [Wiki: Basics of verification infrastructure](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - First, let's go back to the big picture of Verification Commons.
- [Wiki: Data partitioning and leaks](https://github.com/yasufumi-nakata/mind-upload/wiki/dataset-splits-and-leakage) - Compensate for particularly dangerous leaks in benchmark operations.
- [Wiki Home](https://github.com/yasufumi-nakata/mind-upload/wiki) - You can return to other basic pages.

## What Is Currently Known
- Comparable progress requires a starting point, scoring criteria, a priori rules, and a record of results.
- Without a baseline, it's harder to claim improvement.
- Lack of pre-registration and model cards makes it easier to conveniently interpret later.

## What Is Still Unknown
- Which templates will be standardized across WBE is still in the operational design stage.
- The extent to which failure cases and negative results will be required to be disclosed is subject to future development.

---

<h2>The shortest map</h2>
<p>
A baseline is a starting point, a benchmark is a ``scoring standard,'' pre-registration is a ``promise made before starting,'' a model card is a ``results report'', and failure examples are a ``record of where things went wrong.'' Any one alone is not comparable progress.
</p>

<strong>2026-03 Addendum</strong>
<p>
For L1 and higher results, in addition to the usual model card, we have attached an <a href="https://mind-upload.com/verification.html#observability-budget">Observability Budget</a> to make it operationally clear the measurement stack, direct observables, remaining latent state, claim ceiling, and abstention conditions.
</p>

<h2>First, separate roles</h2>
<table>
<thead>
<tr>
<th>Term</th>
<th>Role</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Baseline</strong></td>
<td>This is the minimum comparison partner. This will be the starting point for making improvements. </td>
</tr>
<tr>
<td><strong>Benchmark</strong></td>
<td>Fix what, which data, and which indicators to compare. </td>
</tr>
<tr>
<td><strong>Pre-registration</strong></td>
<td>Before proceeding, fix the indicators, stopping conditions, and analysis policy. </td>
</tr>
<tr>
<td><strong>Model card</strong></td>
<td>Scores, weaknesses, leak countermeasures, failure examples, calculation conditions, and Observability Budget for L1 and above. </td>
</tr>
<tr>
<td><strong>Failure examples/negative results</strong></td>
<td>Leave what didn't work and where it broke. </td>
</tr>
</tbody>
</table>

<h2>Why do we need them all</h2>
<table>
<thead>
<tr>
<th>What is missing</th>
<th>Common problems</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>No baseline</strong></td>
<td>It becomes difficult to judge whether the numbers are good or bad, an improvement or a coincidence. </td>
</tr>
<tr>
<td><strong>No benchmark</strong></td>
<td>Each person will score differently, which will break the comparison. </td>
</tr>
<tr>
<td><strong>No pre-registration</strong></td>
<td>It will be easier to select only convenient conditions later. </td>
</tr>
<tr>
<td><strong>No model card</strong></td>
<td>Only the points remain, and weaknesses and reproduction steps are no longer visible. </td>
</tr>
<tr>
<td><strong>No failure cases</strong></td>
<td>It is easy to repeat the same mistakes because the failure point is not shared. </td>
</tr>
</tbody>
</table>

<h2>View with minimal flow</h2>

01

<h4>Put a baseline</h4>
<p>First of all, it may be simple, so let's use one as a starting point for comparison. </p>

02

<h4>Fix the benchmark</h4>
<p>Align data, divisions, indicators, and prohibitions. </p>

03

<h4>Pre-register</h4>
<p>Decide first which conditions will be considered success/failure. </p>

04

<h4>Leave model cards and failure examples</h4>
<p>Not only the score, but also the weaknesses and ways of collapse will be disclosed. </p>

<h2>Why are failure examples important?</h2>
<p>
If you collect only successful cases, only the conditions that happened to be successful will remain. In a field as big as Mind-Upload, keeping track of<strong>under what conditions it failed</strong> is just as important as keeping track of success stories.
</p>

<strong>Minimum requirements for failure examples</strong>
<p>
Under what conditions, which indicators collapsed, and by how much? It is necessary to isolate whether it was a leak or partition problem, whether it collapsed due to OOD, or whether there was insufficient computational resources.
</p>

<h2>Minimum checks when reading public pages</h2>

<h4>Checklist</h4>
<ul>
<li><strong>Is there a baseline?</strong>Is it clear what it is compared to? </li>
<li><strong>Are the benchmarks fixed:</strong>Are the data, splits, and metrics written? </li>
<li><strong>Are there any pre-registrations?</strong>Have the conditions been changed afterwards? </li>
<li><strong>Are there model cards or examples of failure?</strong>In addition to weaknesses and ways of collapse, is the Observability Budget visible at L1 and above? </li>
</ul>

<h2>Where to go back next</h2>
<p>
If you want to go back to the drawing board, use <a href="https://mind-upload.com/verification.html">Verification platform</a>, if you want to go back to practice, use <a href="https://mind-upload.com/datasets.html#l0-practice">Hands-on</a>, and if you want to go back to precedents in other fields, use <a href="https://mind-upload.com/verification.html#casework">Casework</a>.
</p>
