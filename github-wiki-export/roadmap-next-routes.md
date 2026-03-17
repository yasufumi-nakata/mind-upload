# Wiki: 5 paths to follow after the roadmap

> A guide to help you decide on the next page after looking at the dependency map
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-14 / 位置づけ: Roadmap route

## このページの役割
This page is an auxiliary guide that helps you organize what points to discuss next after reading the technology roadmap. The next page will change depending on whether you go back to measurement, go to reconstruction and causal estimation, go down to implementation, go back to verification conditions, or look at systems and collaboration.

## 正確さの前提
What is shown here is the entry point after reading the roadmap. Please be sure to check the official points and achievement conditions for each node in the main text of the roadmap.

## 公開ページへ戻る
- [Technology Roadmap](https://mind-upload.com/tech_roadmap.html)
- [Verification base](https://mind-upload.com/verification.html)
- [Introduction to EEG](https://mind-upload.com/eeg_101.html)

## 関連 Wiki
- [Wiki: How to read the roadmap](https://github.com/yasufumi-nakata/mind-upload/wiki/roadmap-reading-guide) - For those who want to get back to reading the Roadmap itself.
- [Wiki: How to read each L0 to L5](https://github.com/yasufumi-nakata/mind-upload/wiki/claim-level-reading-routes) - For those who want to see the lead from the assertion level.
- [Wiki: 4 paths after Verification](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-next-routes) - This is for people who want to further refine their skills after moving on to the V series.

## いま分かっていること
- The technology roadmap is an overall map, so the next page is too wide as it is.
- The page to return to is different for measurement, reconfiguration, implementation, verification, and social implementation.
- After reading the Roadmap, narrowing down to one route will make it easier to understand and proceed.

## まだ分かっていないこと
- Which route is the shortest and most effective may change based on future data and bench development.
- The final conditions for V and D still have many unresolved parts.

---

<h2>Decide the route after the map</h2>
<p>
Technology roadmaps are useful for getting the "big picture," but they are too broad in terms of where to go next. Here, we will divide it into 5 paths depending on what we want to dig into right now and pin the next page.
</p>

<h2>Five paths to follow after the roadmap</h2>
<table>
<thead>
<tr>
<th>What I want to know next</th>
<th>Next page</th>
<th>What you can find out</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>I want to reduce the measurement limit</strong></td>
<td><a href="https://mind-upload.com/eeg_101.html">EEG 101</a> / <a href="https://mind-upload.com/datasets.html">Datasets</a></td>
<td>You can check what can be measured and what cannot be measured by itself, which is the premise of the M series. </td>
</tr>
<tr>
<td><strong>I want to dig deeper into reconstruction and causal estimation</strong></td>
<td><a href="https://mind-upload.com/verification.html">Verification</a> / <a href="https://mind-upload.com/perspective.html">Perspective</a></td>
<td>You can see where the R series connects to evaluation and causal verification. </td>
</tr>
<tr>
<td><strong>I want to get down to implementation and L0 work</strong></td>
<td><a href="https://mind-upload.com/datasets.html#l0-practice">Hands-on</a> / <a href="https://mind-upload.com/datasets.html">Datasets</a></td>
<td>I You can specify the minimum loop before proceeding to the series and the selection of input data. </td>
</tr>
<tr>
<td><strong>I want to focus on verification conditions</strong></td>
<td><a href="https://mind-upload.com/verification.html">Verification</a> / <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/verification-next-routes">Four paths after Verification</a></td>
<td>You can check the assertion level of the V series and the following branches of practice, closed loop, and identity. </td>
</tr>
<tr>
<td><strong>I would like to see the system and external collaboration</strong></td>
<td><a href="https://mind-upload.com/issue.html#external-collaboration">Collaborations</a> / <a href="https://mind-upload.com/issue.html">Issue</a></td>
<td>You can check the D series and external dependencies while separating them from the preparations you can make now. </td>
</tr>
</tbody>
</table>

<h2>Why this division</h2>
<table>
<thead>
<tr>
<th>way</th>
<th>Reasons for going to that page after Roadmap</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Measurement</strong></td>
<td>Since the M series determines input limits, it is better to check the basics of measurement on a separate page to reduce misreading. </td>
</tr>
<tr>
<td><strong>Reconfiguration</strong></td>
<td>The R series is connected to evaluation and causal verification, so it needs to be supplemented with Verification and Perspective. </td>
</tr>
<tr>
<td><strong>Implementation</strong></td>
<td>This is because it is difficult to make progress in the I-series unless you organize it not only on paper, but also through Hands-on and Datasets. </td>
</tr>
<tr>
<td><strong>Verification</strong></td>
<td>Since it is necessary to look at the overall design and assertion level together in the V series, it is more natural to dig deeper into the Verification side. </td>
</tr>
<tr>
<td><strong>Social implementation</strong></td>
<td>D series has a large system and external dependence, so it is easier to put it into practice if it is concreted in issues and collaborations. </td>
</tr>
</tbody>
</table>

<h2>Assistance wiki when you stop midway</h2>
<table>
<thead>
<tr>
<th>Place to stop</th>
<th>Go back to wiki</th>
</tr>
</thead>
<tbody>
<tr>
<td>Stops at reading P/M/R/I/V/D itself</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/roadmap-reading-guide">How to read the roadmap</a></td>
</tr>
<tr>
<td>I want to look at it from the assertion level</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/claim-level-reading-routes">How to read each L0 to L5</a></td>
</tr>
<tr>
<td>Stops in order of descending to the practical side</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-to-l0-route">One straight path from EEG to L0</a> / <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/verification-next-routes">Four paths to follow after Verification</a></td>
</tr>
<tr>
<td>Stops in order of returning to theory side</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/wbe-to-theory-route">Four routes to get started with WBE and dig deeper into theory</a></td>
</tr>
<tr>
<td>Stops due to external dependence and participation path</td>
<td><a href="https://github.com/yasufumi-nakata/mind-upload/wiki/internal-prework-and-external-dependencies">In-house production and external dependencies</a></td>
</tr>
</tbody>
</table>

<h2>Common ways to get lost</h2>

<h4>Mistake</h4>
<ul>
<li><strong>Just reading the Roadmap makes you feel like you've decided what to do next:</strong> Actually, you need to narrow it down to one route. </li>
<li><strong>Skip M and R and move on to I and V:</strong> This makes it easier to move on to stronger arguments while still remaining within the limitations of input and estimation. </li>
<li><strong>Leave the D series abstract:</strong> It is more practical to cut the preparations back to Issues and Collaborations. </li>
<li><strong>If you go to Verification, you will understand everything:</strong> After the V series, there are the following branches at L0, L3, and L4. </li>
</ul>

<h2>Where to return next</h2>
<p>
Roadmap Please use <a href="https://mind-upload.com/tech_roadmap.html">Technology Roadmap</a> to return to the text, <a href="https://mind-upload.com/verification.html">Verification Platform</a> to return to the verification side, and <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/wbe-to-theory-route">4 routes from WBE introduction to deep dive into theory</a> to return to the theory side branch.
</p>
