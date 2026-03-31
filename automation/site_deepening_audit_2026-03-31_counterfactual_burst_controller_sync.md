# 2026-03-31 site deepening audit: counterfactual page burst-controller sync

## 対象として選んだ箇所

- `wiki/counterfactual-and-perturbation-verification.md`
- 併せて確認・補正した公開箇所:
  - `faq.md`
  - `verification.md`

## 今回ここを優先した理由

- 2026-03-31 時点の site は、`wiki/closed-loop-latency-jitter-and-safety-stops.md` と `verification.md` ではすでに
  - `biomarker family`
  - `controller family / timescale`
  - `sensing compatibility`
  - `programming / eligibility burden`
  をかなり明示できておりました。
- しかし `wiki/counterfactual-and-perturbation-verification.md` は、因果検証の中核 wiki であるにもかかわらず、aDBS / burst-driven neuromodulation をまだ
  - `state-dependent intervention`
  - `deployment burden`
  のやや粗い箱で読める余地を残しておりました。
- このままでは、読者が
  - `adaptive DBS = one controller class`
  - `state-triggered symptom gain = generic causal control`
  - `home-life feasibility = deployable controller family`
  と再圧縮しやすくなります。

## web で確認した主な一次文献

- [Mathiopoulou et al. (2024)](https://pubmed.ncbi.nlm.nih.gov/38580641/)
- [Stanslaski et al. (2024)](https://pubmed.ncbi.nlm.nih.gov/39289373/)
- [Oehrn et al. (2024)](https://doi.org/10.1038/s41591-024-03196-z)
- [Olaru et al. (2024)](https://doi.org/10.1093/brain/awae004)
- [Busch et al. (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12397205/)
- [Mathiopoulou et al. (2025)](https://doi.org/10.1038/s41467-025-58132-7)
- [Wilkins et al. (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12268161/)
- [Dixon et al. (2026)](https://doi.org/10.1038/s41551-025-01438-0)
- [Cascino et al. (2026)](https://pubmed.ncbi.nlm.nih.gov/41741462/)

## 根拠付き批判

### 1. `state-dependent intervention` は一つの controller object ではありません

- [Little et al. (2013)](https://doi.org/10.1002/ana.23951) と [Tinkhauser et al. (2017)](https://doi.org/10.1093/brain/awx010) は beta-guided antikinetic route を押し上げました。
- [Olaru et al. (2024)](https://doi.org/10.1093/brain/awae004) は dyskinesia-linked narrowband gamma を押し上げました。
- [Mathiopoulou et al. (2025)](https://doi.org/10.1038/s41467-025-58132-7) は DBS-entrained gamma を prokinetic biomarker candidate として位置づけました。
- [Dixon et al. (2026)](https://doi.org/10.1038/s41551-025-01438-0) は remotely optimized neural-decoder route を押し上げました。

批判:

- したがって `adaptive DBS` や `state-dependent neuromodulation` を一語で読むと、
  - beta-guided bradykinesia control
  - dyskinesia-linked gamma
  - prokinetic entrained gamma
  - decoder-based movement-responsive control
  が同じ inferential object に潰れます。
- これは 2026-03-31 時点の一次文献に照らして粗すぎます。

### 2. biomarker の可制御性は movement / medication / stimulation state に依存します

- [Mathiopoulou et al. (2024)](https://pubmed.ncbi.nlm.nih.gov/38580641/) は、subthalamic beta が movement, dopaminergic medication, and DBS で異なる形に変調されることを示しました。
- [Busch et al. (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12397205/) は、chronic aDBS programming で repeated threshold adjustment と movement-rich state dependence が残ることを示しました。

批判:

- `beta was used as feedback` だけでは、どの state slice で controllable だったのかが固定されません。
- rest で調整された threshold を movement-rich / medication-cycling regime にそのまま持ち込めるとは限りません。

### 3. controller mode / timescale は implementation detail ではありません

- [Stanslaski et al. (2024)](https://pubmed.ncbi.nlm.nih.gov/39289373/) は ADAPT-PD の setup と sensing workflow を整理し、controller law / onset-duration policy が object の一部であることを示しました。
- [Wilkins et al. (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12268161/) は gait / FOG 向け burst-driven controller を別 route として扱いました。

批判:

- `adaptive` とだけ書くと、single-threshold / dual-threshold / burst-duration / decoder-based policy が同じ class に圧縮されます。
- これは因果検証ページとして不適切でございます。

### 4. sensing compatibility と programming burden は補助条件ではなく主要な ceiling です

- [Stanslaski et al. (2024)](https://pubmed.ncbi.nlm.nih.gov/39289373/) は enrolled cohort の signal availability を明示しました。
- [Busch et al. (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12397205/) は artifact-related maladaptation, unilateral sensing, repeated programming visits を報告しました。
- [Cascino et al. (2026)](https://pubmed.ncbi.nlm.nih.gov/41741462/) は `20` consecutive patients のうち `9` が eligible であり、除外理由が artifact, absent beta peak, incompatible settings であったことを示しました。

批判:

- よって `state-dependent control worked` と `controller family is broadly feasible` は別の命題です。
- counterfactual / perturbation page 側でも、controller-feasibility screening を visible にしておく必要がありました。

### 5. 公開 references の DOI も 1 件ずれていました

- `verification.md` では Dixon et al. (2026) の DOI が `10.1038/s41551-025-01592-5` になっておりました。
- web で確認した一次ソースと、同 repo 内の他ページは `10.1038/s41551-025-01438-0` で一致しておりました。

批判:

- これは内容面だけでなく reference integrity の問題であり、公開サイトとして放置すべきではありません。

## 今回実行した変更

### `wiki/counterfactual-and-perturbation-verification.md`

- `last_updated` を `2026-03-31` に更新しました。
- front matter の `description` / `page_intro` / `accuracy_note` / `page_highlights` / `known_points` / `unknown_points` を、`Burst-Controller Log` と controller-family split を含む形へ更新しました。
- note-box `2026-03-31 deepening: burst-driven neuromodulation is controller-limited, not one state-dependent intervention` を追加しました。
- six-level table の
  - `4. State-dependent intervention`
  - `5. Temporal durability / deployment`
  を改稿し、`biomarker family / controller family / signal-availability exclusions` を明示的に要求するようにしました。
- `Recent literature forces four extra stop lines` を `five extra stop lines` に改め、新規 row `Burst-Controller Log` を追加しました。
- boundary-case table に、aDBS を `deployment burden` だけでなく `controller-family / controller-feasibility` として読む row を追加しました。
- 新規 section `State-dependent neuromodulation is controller-limited, not just state-triggered` を追加しました。
- `What this site calls a counterfactual test` に `Controller family is disclosed for state-dependent neuromodulation` を追加しました。
- `Minimum log bundle now required` に `Burst-controller disclosure` row を追加しました。
- `Six questions` を `Eight questions` に拡張し、
  - `which biomarker/controller law`
  - `which comparator`
  を独立質問として追加しました。
- references に aDBS / burst-controller split を支える文献を追加しました。

### `faq.md`

- Q5b に短い追記を行い、front door でも
  - beta-guided
  - gamma-linked
  - decoder-based
  の controller family が別であること
  - movement / medication / sensing / comparator / programming burden が意味を変えること
  を止めるようにしました。

### `verification.md`

- Dixon et al. (2026) の DOI を `10.1038/s41551-025-01438-0` に修正しました。

## 今回止めた誤読

- `adaptive DBS` は一つの state-dependent intervention class である
- `state-triggered` と書いてあれば biomarker family の違いは大きくない
- `symptom improvement` が出たので controller family も broadly feasible である
- `home-life adaptive DBS` が成立したので programming / eligibility burden は補助問題である
- `verification.md` の Dixon DOI は細部なので多少ずれていてもよい

## 検証

- `ruby scripts/export_github_wiki.rb`
- `env GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT=1 ruby scripts/check_github_wiki_export.rb`
- `git diff --check`
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`

## external dependency tasks

- なし
  - 今回の主作業は、web 上の一次文献確認、公開本文修正、wiki export 同期、ローカル検証、commit、push までこのセッションで完結可能でございます。

## 参考文献

1. Little S, Pogosyan A, Neal S, et al. Adaptive deep brain stimulation in advanced Parkinson disease. *Ann Neurol*. 2013. https://doi.org/10.1002/ana.23951
2. Tinkhauser G, Pogosyan A, Little S, et al. The modulatory effect of adaptive deep brain stimulation on beta bursts in Parkinson's disease. *Brain*. 2017. https://doi.org/10.1093/brain/awx010
3. Mathiopoulou V, Lofredi R, Feldmann LK, et al. Modulation of subthalamic beta oscillations by movement, dopamine, and deep brain stimulation in Parkinson's disease. *npj Parkinsons Dis*. 2024. https://doi.org/10.1038/s41531-024-00693-3
4. Stanslaski S, Summers RLS, Tonder L, et al. Sensing data and methodology from the Adaptive DBS Algorithm for Personalized Therapy in Parkinson's Disease (ADAPT-PD) clinical trial. *npj Parkinsons Dis*. 2024. https://doi.org/10.1038/s41531-024-00772-5
5. Oehrn CR, Roediger J, Diehl A, et al. Chronic adaptive deep brain stimulation versus conventional stimulation in Parkinson's disease: a blinded randomized feasibility trial. *Nat Med*. 2024. https://doi.org/10.1038/s41591-024-03196-z
6. Olaru M, Cernera S, Hahn A, et al. Motor network gamma oscillations in chronic home recordings predict dyskinesia in Parkinson's disease. *Brain*. 2024. https://doi.org/10.1093/brain/awae004
7. Busch JL, Kaplan J, Behnke JK, et al. Chronic adaptive deep brain stimulation for Parkinson's disease: clinical outcomes and programming strategies. *npj Parkinsons Dis*. 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC12397205/
8. Mathiopoulou V, Habets J, Feldmann LK, et al. Gamma entrainment induced by deep brain stimulation as a biomarker for motor improvement with neuromodulation. *Nat Commun*. 2025. https://doi.org/10.1038/s41467-025-58132-7
9. Wilkins KB, Melbourne JA, Akella P, et al. Beta burst-driven adaptive deep brain stimulation for gait impairment and freezing of gait in Parkinson's disease. *Brain Commun*. 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC12268161/
10. Dixon TC, Strandquist G, Zeng A, et al. Movement-responsive deep brain stimulation for Parkinson's disease using a remotely optimized neural decoder. *Nat Biomed Eng*. 2026. https://doi.org/10.1038/s41551-025-01438-0
11. Cascino S, Luiso F, Caffi L, et al. Chronic adaptive deep brain stimulation in Parkinson's disease: ADAPT-START findings and programming principles. *npj Parkinsons Dis*. 2026. https://doi.org/10.1038/s41531-026-01269-z
