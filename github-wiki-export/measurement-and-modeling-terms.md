# Wiki: Terminology guide from measurement to modeling

> Don't memorize words by dots, connect them by flow.
>
> This learning page is generated for GitHub Wiki. The public portal is managed on [mind-upload.com](https://mind-upload.com).

- Updated: 2026-03-14 / Role: Learning guide

## Role Of This Page
This page is a wiki for understanding measurement terms such as EEG, model terms such as ESI and DCM, and operational terms such as BIDS and QC by connecting them in the flow of ``observation → organization → estimation → verification.'' Rather than memorizing individual words, the aim is to first distinguish which words to use and where to stop making an argument.

## Accuracy Notes
The flow shown here is organized for understanding. Although there are back-and-forths and exceptions in actual research, it is important not to confuse observation and estimation, and estimation and verification.

## Back To Public Pages
- [Glossary](https://mind-upload.com/glossary.html)
- [Introduction to EEG](https://mind-upload.com/eeg_101.html)
- [Verification platform](https://mind-upload.com/verification.html)

## Related Wiki Pages
- [Wiki: Basics of EEG](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-basics) - As an entry point to measurements, you can see what EEG measures.
- [Wiki: EEG pretreatment and QC](https://github.com/yasufumi-nakata/mind-upload/wiki/eeg-preprocessing-and-qc) - Compensate on what changes the outcome during the organizing stage.
- [Wiki: Basics of verification infrastructure](https://github.com/yasufumi-nakata/mind-upload/wiki/verification-basics) - Make up for what to fix in the final validation step.

## What Is Currently Known
- Measurement, preprocessing, estimation, and verification have different roles and different words are used for each.
- The observed signal is not the brain state as it is, and estimation involves uncertainty and candidate model dependence.
- BIDS and QC are not an added bonus; they are the backbone of comparability.

## What Is Still Unknown
- The extent to which non-invasive measurements alone can restore sufficient internal state for WBE remains an open question.
- Which modeling combinations will ultimately be most effective is still being studied.
- The extent to which causality can be identified using observational data alone varies greatly depending on the intervention design.

---

<h2>The shortest map</h2>
<p>
The words on this site can be roughly divided into four levels. These are to <strong>observe</strong>, <strong>arrange</strong>, <strong>estimate</strong>, and <strong>confirm</strong>. Even if the words seem difficult, confusion will be reduced if you first explain what stage the story is in.
</p>

<h2>View in 4 levels</h2>
<table>
<thead>
<tr>
<th>stage</th>
<th>Words that are easy to appear here</th>
<th>What are you doing</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1. Observation</strong></td>
<td>EEG, MEG, fMRI, ECoG</td>
<td>We first measure the signals coming out from the brain and body. </td>
</tr>
<tr>
<td><strong>2. Organize</strong></td>
<td>QC, pretreatment, BIDS</td>
<td>Check for noise and defects and arrange it into a shape that others can follow. </td>
</tr>
<tr>
<td><strong>3. Estimation</strong></td>
<td>Inverse problem, ESI, DCM, SCM</td>
<td>Think about how far you can estimate the state and causal structure in the brain from observations. </td>
</tr>
<tr>
<td><strong>4. Verification</strong></td>
<td>Benchmark, baseline, pre-registration, model card</td>
<td>Check whether the estimation or model really holds true in a comparable manner. </td>
</tr>
</tbody>
</table>

<h2>1. Observation: First get the signal</h2>
<p>
EEG and MEG do not directly look inside the brain, but rather measure signals that can be observed from outside. The important point here is that<strong>what you observe is not the same as what is really happening in</strong>the brain.
</p>
<table>
<thead>
<tr>
<th>Term</th>
<th>In one word</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>EEG</strong></td>
<td>This is a method to quickly measure the potential difference on the scalp. While it is resistant to changes over time, it is easily blurred spatially. </td>
</tr>
<tr>
<td><strong>MEG</strong></td>
<td>This is a method of measuring magnetic fields. Although it is complementary to EEG, it is expensive and has significant equipment limitations. </td>
</tr>
<tr>
<td><strong>fMRI</strong></td>
<td>This is a method to measure changes in blood flow. It is strong in position, but slow in time resolution. </td>
</tr>
<tr>
<td><strong>ECoG</strong></td>
<td>This is an invasive measurement that measures near the brain surface. Although it is highly accurate, there are strong restrictions on the applicable range. </td>
</tr>
</tbody>
</table>

<h2>2. Organize: Don't believe the signal as it is</h2>
<p>
The observed signals include blinks, myoelectricity, body movements, equipment noise, etc. Therefore, the next step is QC and pre-treatment. This is not a matter of improving the appearance, but of <strong>recording what information has been kept and what has been removed</strong>.
</p>

<h4>Words used here</h4>
<ul>
<li><strong>QC:</strong>Leave missing, noise, artifact, and exclusion reasons in numerical form. </li>
<li><strong>Preprocessing:</strong> Set up reference methods, filters, artifact removal, etc. </li>
<li><strong>BIDS:</strong>A standard for aligning data and metadata in a way that others can track them. </li>
</ul>

<p>
If you skip this step, even if a high-performance model comes out later, it will not provide comparable evidence.
</p>

<h2>3. Estimation: How much can we tell from observations</h2>
<p>
We want to estimate brain activity and causal structure based on the organized signals. This is where inverse problems, ESI, DCM, and SCM come into play. However, it must be remembered at this stage that<strong>the estimate is an estimate, and uncertainty and candidate model dependence remain</strong>.
</p>
<table>
<thead>
<tr>
<th>Term</th>
<th>Role</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Inverse problem</strong></td>
<td>This is a problem of estimating the cause inside from the signal seen from outside. There is generally no one choice. </td>
</tr>
<tr>
<td><strong>ESI</strong></td>
<td>A framework for estimating brain sources from EEG. Not only the point estimate but also the uncertainty must be reported. </td>
</tr>
<tr>
<td><strong>DCM</strong></td>
<td>Assuming the connections and movement of neural circuits, we estimate which connections are likely to explain the observation. </td>
</tr>
<tr>
<td><strong>SCM</strong></td>
<td>This is a model that makes it easier to handle interventions and counterfactuals by clarifying causal relationships. </td>
</tr>
</tbody>
</table>

<strong>Changes that are likely to occur here</strong>
<p>
Observing an EEG is not the same as uniquely reconstructing brain states. Furthermore, being correct in a correlational prediction is not the same as knowing the causal structure.
</p>

<strong>Supplementary information for 2026-03</strong>
<p>
DCM is a comparison of candidate generative models, and SCM is a language that facilitates describing interventions and counterfactuals. Causal equivalence classes often remain from observational data alone, so it is necessary to read the candidate model space, family comparison, external validation, and the presence or absence of intervention data separately. For more information, see <a href="https://github.com/yasufumi-nakata/mind-upload/wiki/observation-to-estimation">Wiki: From observation to estimation</a>.
</p>

<h2>4. Verification: How to trust estimates</h2>
<p>
The final question is, "Can other people confirm this estimation or model under the same conditions?" This is where words like Benchmark, Baseline, Preregistration, and Model Card come into play.
</p>
<table>
<thead>
<tr>
<th>Term</th>
<th>What is it needed for</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Benchmark</strong></td>
<td>Fix what will be compared and what indicators will be used to score. </td>
</tr>
<tr>
<td><strong>Baseline</strong></td>
<td>Places a starting point for advocating for improvements. </td>
</tr>
<tr>
<td><strong>Pre-registration</strong></td>
<td>Avoid changing the conditions later. </td>
</tr>
<tr>
<td><strong>Model card</strong></td>
<td>In addition to the score, we will also publish weaknesses, failure examples, leak countermeasures, and calculation conditions. </td>
</tr>
</tbody>
</table>

<h2>What has been learned from this process and what is still unknown</h2>
<table>
<thead>
<tr>
<th>What we know</th>
<th>What we still don't know</th>
</tr>
</thead>
<tbody>
<tr>
<td>Which stage of work does the term belong to? </td>
<td>Which model ultimately adequately explains consciousness and identity? </td>
</tr>
<tr>
<td>How to read without confusing observation, estimation, and verification. </td>
<td>Is it possible to obtain sufficient information for WBE with non-invasive measurements alone? </td>
</tr>
<tr>
<td>Why are BIDS and QC part of the technology rather than the outside? </td>
<td>Which multimodal integration is ultimately best? </td>
</tr>
</tbody>
</table>

<h2>Where to go back next</h2>
<p>
Please use <a href="https://mind-upload.com/glossary.html">Glossary</a> to return to a short definition, <a href="https://mind-upload.com/eeg_101.html">Introduction to EEG</a> to read the role of EEG again, and <a href="https://mind-upload.com/verification.html">Verification infrastructure</a> to proceed to comparable verification.
</p>
