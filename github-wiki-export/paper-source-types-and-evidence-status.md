# Wiki: How to read source types, status labels, and evidence classes

> Auxiliary page to avoid confusing badge, source, status, and what a paper directly strengthens
>
> このページは GitHub Wiki 用に生成した学習ページです。公開ポータルは [mind-upload.com](https://mind-upload.com) 側で管理しています。

- 更新日: 2026-03-26 / 位置づけ: Reading guide

## このページの役割
This page is an auxiliary page that organizes labels such as ``Scopus,'' ``arXiv,'' ``Review,'' ``Media,'' ``source_logged,'' ``curated,'' and evidence classes that appear in collections and bibliographic maps for beginners. The important thing here is to read these labels separately and understand what information each one represents.

## 正確さの前提
Labels are a reading aid and do not automatically guarantee the correctness of the article content. When using them as evidence, always refer back to the DOI, main text, and primary research.

## 公開ページへ戻る
- [Collection of papers](https://mind-upload.com/mind_uploading_papers.html)
- [Literature map](https://mind-upload.com/research_harvest_50.html)
- [Casework](https://mind-upload.com/verification.html#casework)

## 関連 Wiki
- [Wiki: How to read the literature and evidence page](https://github.com/yasufumi-nakata/mind-upload/wiki/literature-and-evidence-reading) - First, we will clarify the differences in the roles of collections of papers, bibliographic maps, and proposal pages.
- [Wiki: How to read claims and evidence](https://github.com/yasufumi-nakata/mind-upload/wiki/claims-and-evidence) - It helps you understand how to read the 'strength of claim' on the label.
- [Wiki: U number guide](https://github.com/yasufumi-nakata/mind-upload/wiki/u-number-guide) - This is an auxiliary page to see which open questions are related to the bibliographic map.

## いま分かっていること
- Even for the same document, publication source, document type, site status, and evidence class must be viewed separately.
- Scopus is an index, arXiv is a preprint storage, and Review is a document type, and they do not have the same meaning.
- source_logged and curated are labels that indicate how organized this site is.
- A human PET/MRS/MRI paper can strengthen observability without closing hidden state or proving causal sufficiency.
- A language demo can strengthen semantic reconstruction, fixed-segment retrieval, known-onset decoding, prompt-conditioned generation, or communication performance without becoming unrestricted thought reading.

## まだ分かっていないこと
- The extent to which individual papers ultimately remain central evidence will depend on subsequent scrutiny.
- Top stories traced from reviews and news may weaken when returned to primary research.

---

<h2>First divide into four parts</h2>
<p>
What can be confusing on literature pages is that <strong>where</strong> a paper is listed, <strong>what type of literature</strong> it is, <strong>its current status on this site</strong>, and <strong>what it directly strengthens</strong> can all appear to be the same thing. By separating these four things first, you can significantly reduce misreadings.
</p>

<h2>Labels have four axes</h2>
<table>
<thead>
<tr>
<th>axis</th>
<th>What does it represent</th>
<th>Example</th>
<th>That's not all I can say</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Publisher/Badge</strong></td>
<td>It's about where you can trace the document and which entrance you picked it up from. </td>
<td>Scopus / arXiv / Academic journal page / DOI</td>
<td>It is not determined that the content is strong, correct, or central. </td>
</tr>
<tr>
<td><strong>Document type</strong></td>
<td>Whether the document is primary research, a review, or news. </td>
<td>Primary / Review / Media</td>
<td>It is necessary to separately confirm whether there is new data or whether it is strong enough to be used directly for verification. </td>
</tr>
<tr>
<td><strong>Site status</strong></td>
<td>Indicates whether input has been accepted, organized, or excluded on this site. </td>
<td>source_logged / curated / noise_excluded</td>
<td>It does not necessarily mean that the content of the paper is true or of low value. </td>
</tr>
<tr>
<td><strong>Evidence class</strong></td>
<td>Indicates what the paper directly strengthens in the technical reading flow. </td>
<td>Direct validator / system demo / observability-class advance / benchmark / hidden-state boundary</td>
<td>It is still not a claim that the whole problem is solved. It only fixes <strong>which evidential axis moved</strong>.</td>
</tr>
</tbody>
</table>

<strong>Multiple attributes overlap in the same document</strong>
<p>
For example, a document may be a <strong>review article on Scopus</strong>, a <strong>preprint of primary research on arXiv</strong>, or a <strong>curated human-MRI paper that belongs to the observability-class-advance bin</strong>. Do not rely on only one label.
</p>

<h2>How to read publication source and type</h2>
<table>
<thead>
<tr>
<th>Display</th>
<th>In everyday language</th>
<th>Useful points</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Scopus</strong></td>
<td>These are documents found via the academic literature index database. </td>
<td>It is easy to organize bibliographic information and becomes an entry point for picking up a wide range of academic literature. </td>
<td>Scopus is an index and does not automatically guarantee the strength of peer review or the degree of direct connection to the issue. </td>
</tr>
<tr>
<td><strong>arXiv</strong></td>
<td>This is a public storage area for preprints. </td>
<td>You can find new research quickly. </td>
<td>Many papers have not yet been peer-reviewed at the time of submission, so you need to confirm the methods and limitations yourself. </td>
</tr>
<tr>
<td><strong>Review</strong></td>
<td>This is a review article that summarizes multiple studies. </td>
<td>It is suitable for grasping the map of the entire field and the main points of discussion. </td>
<td>Since our own new experiments are not always the main character, we return to primary research when using it as strong evidence. </td>
</tr>
<tr>
<td><strong>Media</strong></td>
<td>News articles, explanatory articles, and general introductions. </td>
<td>It can be used as an entry point to a topic or as a clue for searching for primary literature. </td>
<td>It is weak as an academic basis as it is, and it is necessary to trace it back to the original paper or presentation. </td>
</tr>
<tr>
<td><strong>Primary</strong></td>
<td>Primary research that directly produces new data, experiments, and analyses. </td>
<td>The evidence can be traced most directly by reviewing the method, evaluation, and limitations. </td>
<td>Even primary research can have weak sample conditions, statistics, and reproducibility, so it cannot be used unconditionally. </td>
</tr>
</tbody>
</table>

<h2>How to read evidence class</h2>
<table>
<thead>
<tr>
<th>Evidence class</th>
<th>What it directly strengthens</th>
<th>Typical examples</th>
<th>What it still does not justify</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>direct validator / causal calibration</strong></td>
<td>Error sources, calibration limits, and local ground-truth checks.</td>
<td>Mikulan (2020), Unnwongse (2023), Hao (2025)</td>
<td>Whole-brain uniqueness recovery or full hidden-state closure.</td>
</tr>
<tr>
<td><strong>task-limited system demonstration</strong></td>
<td>Task-conditioned language decode, prompt-conditioned generation, phoneme-sequence decoding, or closed-loop communication performance on a specific scaffold and interface.</td>
<td>Tang (2023), D&eacute;fossez (2023), d'Ascoli (2025), Ye (2025), Willett (2023), Littlejohn (2025), Wairagkar (2025), Singh (2025)</td>
<td>Whole-brain emulation, unrestricted thought reading, identity continuity, or hidden-state completeness.</td>
</tr>
<tr>
<td><strong>dataset / benchmark / standard / toolchain</strong></td>
<td>Comparability, synchronization, governance, and reproducibility.</td>
<td>EEG-BIDS, Motion-BIDS, LSL, MOABB</td>
<td>Biological sufficiency or mechanistic truth.</td>
</tr>
<tr>
<td><strong>observability-class advance / human proxy ladder</strong></td>
<td>What humans can directly observe or approximate at a specific measurement class.</td>
<td>Shapson-Coe (2024), Johansen (2024), Lucchetti (2025), Baadsvik (2024), Rzechorzek (2022), Hirschler (2025)</td>
<td>State-complete measurement. Each proxy or atlas still has a claim ceiling.</td>
</tr>
<tr>
<td><strong>mechanistic boundary / hidden-state evidence</strong></td>
<td>What still remains latent or omitted even after connectome, cell type, or a strong demo.</td>
<td>Gouwens (2021), Hengen (2016), Xu (2024), Looser (2024), Cahill (2024)</td>
<td>Direct validation or a finished implementation.</td>
</tr>
<tr>
<td><strong>review / synthesis</strong></td>
<td>Field map, terminology, and issue clustering.</td>
<td>Review articles and benchmark syntheses</td>
<td>Strong conclusions without returning to primary research.</td>
</tr>
<tr>
<td><strong>context / philosophy / law / culture</strong></td>
<td>Context around the topic and its surrounding debates.</td>
<td>Ethics, legal analysis, metaphysics, cultural studies</td>
<td>The technical or natural-science frontier by itself.</td>
</tr>
</tbody>
</table>

<strong>Language-facing demos need one more split</strong>
<p>
On this site, `task-limited system demonstration` is still too broad if readers treat every language-facing result as one `brain-to-text` category. <a href="https://doi.org/10.1038/s41593-023-01304-9" target="_blank">Tang et al. (2023)</a> constrain <strong>within-subject semantic reconstruction</strong>, <a href="https://doi.org/10.1038/s42256-023-00714-5" target="_blank">D&eacute;fossez et al. (2023)</a> constrain <strong>fixed-segment speech retrieval</strong>, <a href="https://doi.org/10.1038/s41467-025-65499-0" target="_blank">d'Ascoli et al. (2025)</a> constrain <strong>known-onset word decoding</strong>, <a href="https://doi.org/10.1038/s42003-025-07731-7" target="_blank">Ye et al. (2025)</a> constrain <strong>prompt-conditioned generation</strong>, and <a href="https://doi.org/10.1038/s41467-025-63825-0" target="_blank">Singh et al. (2025)</a>, <a href="https://doi.org/10.1038/s41586-023-06377-x" target="_blank">Willett et al. (2023)</a>, <a href="https://doi.org/10.1038/s41593-025-01905-6" target="_blank">Littlejohn et al. (2025)</a>, and <a href="https://doi.org/10.1038/s41586-025-09127-3" target="_blank">Wairagkar et al. (2025)</a> constrain different invasive speech-decoding or communication-subsystem routes. Therefore, when a paper emits fluent text or speech, this site asks for the <a href="https://mind-upload.com/verification.html#neural-contribution-card">Neural Contribution Card</a> before it is promoted beyond task-conditioned evidence.
</p>

<h2>How to read site status labels</h2>
<table>
<thead>
<tr>
<th>Label</th>
<th>In everyday language</th>
<th>What you need next</th>
<th>Easy to misread</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>source_logged</strong></td>
<td>This is the stage where we accept URLs and DOIs as entry points and include them in our tracking targets. </td>
<td>Relevance confirmation, primary literature tracking, U number assignment, and abstract scrutiny are required. </td>
<td>It does not mean "recruitment confirmed" or "high quality confirmed". </td>
</tr>
<tr>
<td><strong>curated</strong></td>
<td>This site has been organized and arranged according to the points of discussion. </td>
<td>It will continue to be necessary to eliminate duplicates, replace with strong evidence, and track updates. </td>
<td>It is not a label that guarantees that the content is true. </td>
</tr>
<tr>
<td><strong>noise_excluded</strong></td>
<td>We are at the stage where we have determined that the relationship is weak, the contamination is large, and we will not use it at this time. </td>
<td>It is important to leave the reason for exclusion and prevent contamination of the same species. </td>
<td>This does not mean that the paper itself has no value, but it may be out of sync with the main points of this site. </td>
</tr>
</tbody>
</table>

<h2>Where to stop and return to the original text</h2>
<table>
<thead>
<tr>
<th>Current purpose</th>
<th>You can stop here</th>
<th>Return to original text</th>
</tr>
</thead>
<tbody>
<tr>
<td>I want to pick up a wide range of topics</td>
<td>Once you know whether you are interested by Badge, summary, or 5-point arrangement. </td>
<td>When you want to support a strong argument by citing the paper. </td>
</tr>
<tr>
<td>Looking at source_logged items</td>
<td>When you understand that you are still at the entrance stage. </td>
<td>When you want to judge whether you can pursue primary research or whether it will be included in the U number. </td>
</tr>
<tr>
<td>Looking at Reviews and Media</td>
<td>When you have a map of the issues and related keywords. </td>
<td>When you want to use evaluations, methods, and numerical values as evidence. </td>
</tr>
<tr>
<td>Comparing documents from Scopus and arXiv</td>
<td>When you can figure out which entrance it was picked up from. </td>
<td>When you want to check the peer review status, experimental conditions, limitations, and possibility of follow-up testing. </td>
</tr>
</tbody>
</table>

<h2>Common misreadings</h2>

<h4>Misread</h4>
<ul>
<li><strong>“Scopus is strong”:</strong> Scopus is an index. Check the text and method to see how it applies to the issue. </li>
<li><strong>“It's all weak because it's arXiv”:</strong> There are important entry points even before peer review. Check the content to see if it's weak or not. </li>
<li><strong>“Review is enough”:</strong> Review articles are useful as maps, but for direct evidence you need to go back to primary research. </li>
<li><strong>“Source_logged, so accepted”:</strong> This is still an acceptance log, and the decision to integrate or exclude is a follow-up work. </li>
<li><strong>“curated so it is true”:</strong> Being organized and ultimately correct are two different things. </li>
<li><strong>“A human proxy paper solved hidden state”:</strong> A human PET/MRS/MRI advance often raises an observability class, not a full state-complete readout.</li>
</ul>

<h2>Where to return next</h2>
<p>
If you want to have a broad view of the papers, go back to <a href="https://mind-upload.com/mind_uploading_papers.html">Collection of Papers</a>, if you want to see how they correspond to unresolved issues, go to <a href="https://mind-upload.com/research_harvest_50.html">Literature Map</a>, and if you want to organize them based on the differences in their roles, go back to <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/literature-and-evidence-reading">How to read the literature and evidence page</a>.
</p>
