# Wiki: How to read partial solution/exploration stage/undeveloped

> Auxiliary page to accurately read 'What's still missing?'
>
> This learning page is generated for GitHub Wiki. The public portal is managed on [mind-upload.com](https://mind-upload.com).

- Updated: 2026-03-06 / Role: Reading guide

## Role Of This Page
This is a supplementary page that organizes words such as 'partial solution', 'exploratory stage', 'unstandardized', 'undeveloped', and 'insufficient' that appear in literature maps, technology roadmaps, verification platforms, and research notes for beginners. The purpose here is not to be optimistic or pessimistic, but to specifically read 'what is still missing'.

## Accuracy Notes
Progress labels are not meant to praise or devalue the value of a topic. Read them as management labels that indicate what is in place and what is not yet.

## Back To Public Pages
- [Literature map](https://mind-upload.com/research_harvest_50.html)
- [Technology Roadmap](https://mind-upload.com/tech_roadmap.html)
- [Verification base](https://mind-upload.com/verification.html)

## Related Wiki Pages
- [Wiki: U number guide](https://github.com/yasufumi-nakata/mind-upload/wiki/u-number-guide) - First, organize the objects that are currently labeled.
- [Wiki: How to read the roadmap](https://github.com/yasufumi-nakata/mind-upload/wiki/roadmap-reading-guide) - This is a supplementary page to read along with P/M/R/I/V/D dependencies.
- [Wiki: Basics of verification infrastructure](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - We'll help you understand from the beginning what it takes to make comparable progress.

## What Is Currently Known
- Even the same word 'unresolved' has different meanings depending on whether there is no standard, there is weak evidence, or the threshold has not been determined.
- Partial resolution is not 'all parts were solved', but a state in which at least part of the problem is progressing.
- The exploratory stage does not mean that the question itself is meaningless; it is a state in which the type of comparison and verification is still weak.

## What Is Still Unknown
- There is still room for future updates regarding which quantitative standards should be used to unify the boundaries of each label.
- Even in the same area, the current label may change due to the appearance of new benches or standards.

---

<h2>First, fix your mindset</h2>
<p>
Progress labels are not words that judge a research theme as ``pass/fail.'' Its role is to briefly show<strong>what you already have</strong> and <strong>what is still missing</strong>.
</p>

<h2>Meanings of frequently used labels</h2>
<table>
<thead>
<tr>
<th>Label</th>
<th>In everyday language</th>
<th>At least what you can say</th>
<th>Things I can't say yet</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Partial solution</strong></td>
<td>While progress has been made in some core areas, all conditions are not yet in place. </td>
<td>At least some of the methods, measurements, and comparison axes are working. </td>
<td>It cannot be said that the final victory condition has been reached. </td>
</tr>
<tr>
<td><strong>Exploration stage</strong></td>
<td>This is an important question, but evaluation methods and public benches are still weak. </td>
<td>It is worth addressing as an issue, and there are initial evidence and hypotheses. </td>
<td>It cannot be said that stable comparison, reproduction, and standardization have been achieved. </td>
</tr>
<tr>
<td><strong>Unstandardized</strong></td>
<td>Measurement methods and formats vary depending on the person and team. </td>
<td>Although individual studies exist, the common yardstick is still weak. </td>
<td>It is not possible to make fair comparisons between different studies. </td>
</tr>
<tr>
<td><strong>Undeveloped</strong></td>
<td>Operational rules, audit procedures, division of responsibility, disclosure format, etc. have not yet been finalized. </td>
<td>Practical conditions other than technology remain. </td>
<td>We cannot say that it will cover long-term operation or third-party audits. </td>
</tr>
<tr>
<td><strong>Lack</strong></td>
<td>We still lack the necessary data, benches, error bounds, comparison tests, etc. </td>
<td>I can see what needs to be added. </td>
<td>It cannot be said that the current materials are sufficient. </td>
</tr>
<tr>
<td><strong>Undefined</strong></td>
<td>How to determine thresholds, boundaries, and sufficient conditions has not yet been determined. </td>
<td>The problem setting is visible, but the line drawing is not fixed. </td>
<td>It cannot be said that everyone will get the same judgment. </td>
</tr>
<tr>
<td><strong>Insufficient</strong></td>
<td>Although there is a minimum, it is still not enough for third-party comparisons or strong claims. </td>
<td>There is some foundation. </td>
<td>It cannot be said that the strict verification conditions have been met. </td>
</tr>
</tbody>
</table>

<h2>There are different types of "not enough"</h2>
<table>
<thead>
<tr>
<th>Expression</th>
<th>What's missing</th>
<th>Example</th>
<th>What you need next</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Not enough benches</strong></td>
<td>There is no place to compare the same issues and the same indicators. </td>
<td>``Lack of unified bench''</td>
<td>Public data, fixed indicators, baseline, and failure examples. </td>
</tr>
<tr>
<td><strong>Standards not yet developed</strong></td>
<td>Format, logging, naming, and auditing procedures are not consistent. </td>
<td>“Common audit regulations are insufficient”</td>
<td>Standards, Validators, Templates, and Checklists. </td>
</tr>
<tr>
<td><strong>Insufficient error bounds</strong></td>
<td>We do not know how far it can be generalized and the uncertainty. </td>
<td>"Insufficient generalized error bound"</td>
<td>Confidence interval, subject difference evaluation, OOD evaluation. </td>
</tr>
<tr>
<td><strong>Threshold not determined</strong></td>
<td>It has not been decided where to start calling things ``same'', ``sufficient'', and ``safe''. </td>
<td>"Threshold value not determined"</td>
<td>This is a comparison test with pre-registered judgment rules. </td>
</tr>
<tr>
<td><strong>Undeveloped public operation</strong></td>
<td>There is no way to go beyond third-party supplementary examinations, responsibility sharing, and suspension criteria. </td>
<td>“Operating regulations not yet in place”</td>
<td>Registry, audit log, suspension rules, and publishing procedures. </td>
</tr>
</tbody>
</table>

<h2>Read with examples</h2>
<table>
<thead>
<tr>
<th>Example</th>
<th>What you want to read in this way</th>
<th>Questions that remain</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>U0: Partial resolution/identity evaluation bench unstandardized</strong></td>
<td>There are attempts to measure identity, and there are also partial evaluation axes. </td>
<td>A common bench and thresholds that include interventions are not yet available. </td>
</tr>
<tr>
<td><strong>U10: Exploration stage / limited actual measurement research</strong></td>
<td>Thermodynamic grounding exists as an issue and there are candidate indicators. </td>
<td>The comparison between the actual measured pipeline and the published pipeline is still weak, and its generalization is still uncertain. </td>
</tr>
<tr>
<td><strong>U15: Exploration stage / lack of implementation standards</strong></td>
<td>The need for system integration is clear, and the problem set is clear. </td>
<td>There is still no specific standard that connects technical KPIs and stopping criteria. </td>
</tr>
</tbody>
</table>

<strong>Labels are not just about hierarchical relationships</strong>
<p>
It is not a simple matter that "partial solution" is always better than "exploration stage". Partial solution indicates that there is some foundation, and the exploration stage indicates that the comparative basis for the whole question is still weak. You need to read up to the types of what is missing.
</p>

<h2>Common misreadings</h2>

<h4>Misread</h4>
<ul>
<li><strong>"It's only a partial solution, so it's almost finished":</strong> Depending on the remaining conditions, rather heavy work remains behind. </li>
<li><strong>"It's only in the exploratory stage so it's meaningless":</strong> There are things that are important, but the basis for comparison is still weak. </li>
<li><strong>“It says “deficiency, so don’t do everything”:</strong> If you don’t read what’s missing separately, you’ll miss the progress. </li>
<li><strong>“There is no research because it is not standardized”:</strong> Even if there is research, there may be no common format or common bench. </li>
<li><strong>“Underdeveloped means only a lack of technology”:</strong> It is often a lack of systems, audits, and open operations. </li>
</ul>

<h2>Where to return next</h2>
<p>
If you want to read the current status of each U, please go back to <a href="https://mind-upload.com/research_harvest_50.html">Literature Map</a>. If you want to see the progress with dependencies, go back to <a href="https://mind-upload.com/tech_roadmap.html">Technology Roadmap</a>. If you want to distinguish between designed and unimplemented projects, go back to <a href="https://mind-upload.com/verification.html">Verification Platform</a>.
</p>
