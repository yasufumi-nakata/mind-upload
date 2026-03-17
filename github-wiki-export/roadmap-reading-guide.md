# Wiki: How to read the roadmap

> Read your technology roadmap as a dependency map rather than a long list
>
> This learning page is generated for GitHub Wiki. The public portal is managed on [mind-upload.com](https://mind-upload.com).

- Updated: 2026-03-06 / Role: Reading guide

## Role Of This Page
This page is a supplementary page that explains what P/M/R/I/V/D in the technology roadmap means and where to start to read them to avoid getting lost. Rather than resummarizing the main text of the roadmap, we will organize the ``how to read the map'' itself.

## Accuracy Notes
This page is a reading aid. Please be sure to return to the main text of the technology roadmap for the official list of issues and current arrangement.

## Back To Public Pages
- [technology roadmap](https://mind-upload.com/tech_roadmap.html)
- [Introduction to WBE](https://mind-upload.com/wbe_101.html)
- [Verification platform](https://mind-upload.com/verification.html)

## Related Wiki Pages
- [Wiki: Basics of WBE](https://github.com/yasufumi-nakata/mind-upload/wiki/mind-upload-basics) - This is for people who want to see the overall picture of why this map is needed.
- [Wiki: Basics of verification infrastructure](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - Complement what you want to fix in the V series.
- [Wiki Home](https://github.com/yasufumi-nakata/mind-upload/wiki) - You can return to other basic pages.

## What Is Currently Known
- P is the definition of progress, M is measurement, R is reconstruction, I is implementation, V is verification, and D is social implementation.
- The stronger the argument, the further back it is, and the more unorganized the previous layer is, the more difficult it is to move forward.
- It's best to read a roadmap as a map of dependencies rather than a collection of conclusions.

## What Is Still Unknown
- Which route is the shortest and most effective may change as data benches are developed in the future.
- The final conditions for V and D still have many unresolved issues.

---

<h2>First of all, in a nutshell</h2>
<p>
A technology roadmap is a map that shows what needs to be solved first before the future story will collapse. Although it may seem like a long list, it actually represents the dependency relationship of ``Assumption → Measurement → Estimation → Implementation → Verification → Social Implementation''.
</p>

<strong>After deciding how to read, you also want to decide on the next page</strong>
<p>
If you want to see not only the meaning of the symbols on the roadmap, but also where to go in measurement, reconfiguration, implementation, verification, and social implementation after reading it, please see <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/roadmap-next-routes">Five paths to follow after the roadmap</a>.
</p>

<h2>P/M/R/I/V/D in everyday language</h2>
<table>
<thead>
<tr>
<th>Symbol</th>
<th>What question is it?</th>
<th>What will be the problem if this goes out</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>P</strong></td>
<td>What we call success</td>
<td>The goal is not set, and the victory conditions can be changed later. </td>
</tr>
<tr>
<td><strong>M</strong></td>
<td>What can be measured and with what precision</td>
<td>In the first place, I don't know what is in the input. </td>
</tr>
<tr>
<td><strong>R</strong></td>
<td>What can we infer from observations</td>
<td>The measured signal is interpreted to have a stronger meaning than necessary. </td>
</tr>
<tr>
<td><strong>I</strong></td>
<td>How to move the model</td>
<td>Even if it looks good on paper, it may not turn in reality. </td>
</tr>
<tr>
<td><strong>V</strong></td>
<td>What and how to check</td>
<td>I can't tell if I've moved forward or if it's just an appearance. </td>
</tr>
<tr>
<td><strong>D</strong></td>
<td>How to be treated in society</td>
<td>Even if the technology works, it cannot be used due to rights and safety concerns. </td>
</tr>
</tbody>
</table>

<h2>Reading order by interest</h2>
<table>
<thead>
<tr>
<th>What I'm curious about now</th>
<th>Symbol to read first</th>
<th>Next symbol</th>
</tr>
</thead>
<tbody>
<tr>
<td>I want to know what I need to accomplish to move forward</td>
<td><strong>P</strong></td>
<td><strong>V</strong></td>
</tr>
<tr>
<td>I want to get into the limitations of EEG and fMRI</td>
<td><strong>M</strong></td>
<td><strong>R</strong></td>
</tr>
<tr>
<td>I want to know how the model works</td>
<td><strong>R</strong></td>
<td><strong>I</strong></td>
</tr>
<tr>
<td>I want to see the identity and social system</td>
<td><strong>V</strong></td>
<td><strong>D</strong></td>
</tr>
</tbody>
</table>

<h2>This is a dependency, not a chronology</h2>
<p>
Even if the numbers are arranged in the order P → M → R → I → V → D, it does not mean that they will definitely go this far in this year. The important thing is that the later arguments are more vulnerable to the failures of the earlier layers. For example, if we proceed to a strong identity claim in V while M and R are ambiguous, input limitations and estimation uncertainties remain.
</p>

<h4>Next</h4>
<p>Please check the official issue list and index in the technology roadmap text. </p>
<a href="https://mind-upload.com/tech_roadmap.html">Go to technology roadmap →</a>
