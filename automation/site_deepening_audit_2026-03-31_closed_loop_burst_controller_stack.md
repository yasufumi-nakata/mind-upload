# 2026-03-31 site deepening audit: closed-loop burst-controller stack

## 対象として選んだ箇所

- `wiki/closed-loop-latency-jitter-and-safety-stops.md`
- `verification.md`

## 今回ここを優先した理由

- 2026-03-31 時点で site はすでに、
  - latency / jitter
  - body / environment boundary
  - co-adaptation / credit assignment
  - phase-targeting の estimability / effect / stability split
  - aDBS の eligibility / continuation / programming burden
  をかなり明確に分けておりました。
- しかしなお `burst/state-triggered neuromodulation` だけは、本文上まだ
  - `burst timing`
  - `beta-trigger latency`
  - `false positive / false negative`
  を主軸に読める余地が残っておりました。
- これは技術・自然科学の観点で不十分でございます。一次文献が示しているのは、aDBS の主要な分岐点がすでに
  - `どの biomarker family を使うか`
  - `どの controller mode / timescale を使うか`
  - `movement / medication / stimulation state で controllable か`
  - `sense-compatible / artifact-tolerant か`
  - `biomarker-linked comparator を越えて symptom benefit を示せたか`
  の方へ移っているからでございます。

## web で確認した主な一次文献

- [Mathiopoulou et al. (2024)](https://doi.org/10.1038/s41531-024-00693-3)
- [Stanslaski et al. (2024)](https://doi.org/10.1038/s41531-024-00772-5)
- [Oehrn et al. (2024)](https://doi.org/10.1038/s41591-024-03196-z)
- [Olaru et al. (2024)](https://doi.org/10.1093/brain/awae004)
- [Mathiopoulou et al. (2025)](https://doi.org/10.1038/s41467-025-58132-7)
- [Busch et al. (2025)](https://doi.org/10.1038/s41531-025-01124-7)
- [Wilkins et al. (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12268161/)
- [Cascino et al. (2026)](https://doi.org/10.1038/s41531-026-01269-z)
- [Dixon et al. (2026)](https://doi.org/10.1038/s41551-025-01438-0)

## 根拠付き批判

### 1. `adaptive DBS` は一つの biomarker object ではございません

- [Little et al. (2013)](https://doi.org/10.1002/ana.23951) と [Tinkhauser et al. (2017)](https://doi.org/10.1093/brain/awx010) は beta / beta-burst 系の antikinetic route を押し上げました。
- 一方で [Olaru et al. (2024)](https://doi.org/10.1093/brain/awae004) は chronic home recording で narrowband gamma が dyskinesia と相関することを示しました。
- [Oehrn et al. (2024)](https://doi.org/10.1038/s41591-024-03196-z) は entrained gamma を含む personalized marker で high / low dopaminergic state を分けました。
- [Mathiopoulou et al. (2025)](https://doi.org/10.1038/s41467-025-58132-7) は DBS-induced gamma entrainment を prokinetic biomarker candidate として位置づけました。

批判:

- したがって `adaptive DBS` や `burst-driven loop` を一語で読むと、
  - antikinetic beta
  - gait-linked burst-duration
  - dyskinesia-linked narrowband gamma
  - prokinetic entrained gamma
  - personalized dopaminergic-state marker
  が同じ inferential object に潰れます。
- これは科学的に粗いでございます。

### 2. beta feedback 自体が movement / medication / stimulation state により動きます

- [Mathiopoulou et al. (2024)](https://doi.org/10.1038/s41531-024-00693-3) は、subthalamic beta が movement, dopaminergic medication, and DBS により異なる仕方で変調されることを示しました。
- [Busch et al. (2025)](https://doi.org/10.1038/s41531-025-01124-7) は、clinic で設定した threshold が chronic state を十分に代表せず、follow-up で高すぎた事例を示しました。

批判:

- `beta was used as feedback` だけでは、どの state slice で controllable だったのかが固定されません。
- rest で作った threshold を movement-rich / medication-cycling regime にそのまま持ち込めるとは限りません。

### 3. controller mode は単なる implementation detail ではございません

- [Stanslaski et al. (2024)](https://doi.org/10.1038/s41531-024-00772-5) は、ADAPT-PD で
  - single-threshold: `250 ms`
  - dual-threshold: `2.5 min up / 5 min down`
  - programmable onset: `1.2–2 s`
  を明示し、異なる therapeutic goal に応じて mode を使い分けています。
- [Wilkins et al. (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12268161/) は、beta burst-duration を input にしつつ、`I_min / I_max` と slow ramp を含む controller を gait / FOG 向けに較正しました。

批判:

- これは `adaptive` という label の内部で controller law と timescale がすでに大きく分岐していることを意味します。
- よって `burst-triggered` を timing family としてだけ読むのは不十分でございます。

### 4. sensing compatibility と artifact burden は補助問題ではございません

- [Stanslaski et al. (2024)](https://doi.org/10.1038/s41531-024-00772-5) は、artifact や inadequate signal により exit する participants を明記しました。
- [Busch et al. (2025)](https://doi.org/10.1038/s41531-025-01124-7) は、`3/16 hemispheres` で beta peak 不可視、`4/8 patients` で unilateral sensing が必要であったことを報告しました。
- [Cascino et al. (2026)](https://doi.org/10.1038/s41531-026-01269-z) は、`20` consecutive chronic cDBS patients のうち `9` しか適格でなく、除外理由に artifact や peak 欠如や incompatible settings が含まれることを示しました。

批判:

- したがって `signal was available` は binary な前提ではなく、それ自体が major bottleneck でございます。
- ここを本文と log rule で visible にしないと、controller feasibility を過大評価します。

### 5. biomarker-linked control と symptom superiority は別 object でございます

- [Oehrn et al. (2024)](https://doi.org/10.1038/s41591-024-03196-z) は personalized signal selection で symptom / quality-of-life 改善を示しました。
- しかし [Wilkins et al. (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12268161/) は、therapeutic window と TEED を揃えた randomly adapting DBS でも group-level で cDBS / aDBS に近い成績を示しました。

批判:

- これは `biomarker-linked adaptation` と `clinical superiority` を同一視できないことを意味します。
- comparator policy を出さずに `aDBS improved` と書くのは弱いでございます。

## 今回実行した変更

### `wiki/closed-loop-latency-jitter-and-safety-stops.md`

- `last_updated` を `2026-03-31` に更新しました。
- front matter の `description` / `page_intro` / `accuracy_note` / `page_highlights` / `known_points` / `unknown_points` を、burst-driven loop の `biomarker family + controller policy` が必要である形へ更新しました。
- `2026-03-31 re-audit: burst-driven neuromodulation needs a controller wall too` note-box を追加しました。
- loop-class table の `burst/state-triggered neuromodulation` row を改稿し、timing-only ではなく biomarker / controller / sensing viability を前面化しました。
- 新規 section `Burst-driven neuromodulation is controller-limited, not just burst-timed` を追加し、
  - biomarker family / symptom target
  - state dependence / controllability
  - controller mode / timescale
  - sensing compatibility / artifact burden
  - biomarker-linked control versus clinical effect
  - deployability / programming burden
  の 6 層で読むよう固定しました。
- `Additional metrics for burst systems` を全面改稿し、controller mode, state slice, comparator, TEED / duty-cycle matching まで要求するようにしました。
- `14 questions` を `16 questions` に更新し、
  - biomarker family / symptom target
  - controller mode / state dependence / comparator
  を独立質問として追加しました。
- references に
  - Mathiopoulou 2024
  - Stanslaski 2024
  - Olaru 2024
  - Mathiopoulou 2025
  - Wilkins 2025
  を追加しました。

### `verification.md`

- `Additional audit logs` に `Burst-Controller Log` を追加しました。
- これにより site-wide rule としても、
  - biomarker family
  - sensing compatibility
  - controller family
  - regime dependence
  - comparator / TEED rule
  - programming burden
  を disclosure しない限り、validated symptom-linked control へ昇格させない方針を明文化しました。

## 今回止めた誤読

- `adaptive DBS` は一つの controller family である
- `beta-trigger latency` を見れば aDBS の主要 burden はほぼ読める
- `beta feedback` は movement / medication / DBS の影響をほぼ受けない安定 signal である
- `adaptive` と書いてあれば single-threshold / dual-threshold / burst-duration / decoder-based policy はだいたい同じ
- `biomarker-linked controller` が成立 = symptom superiority も示された
- `proof-of-principle` が成立 = sense-compatibility / eligibility / programming burden も大きくは残らない

## 検証

- `ruby scripts/export_github_wiki.rb`
- `env GITHUB_WIKI_EXPORT_SKIP_GIT_DRIFT=1 ruby scripts/check_github_wiki_export.rb`
- `git diff --check`
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`

## external dependency tasks

- なし
  - 今回の主作業は、一次文献確認、公開本文修正、export 同期、ローカル検証、commit、push までこのセッションで完結可能でございます。

## 参考文献

1. Little S, Pogosyan A, Neal S, et al. Adaptive deep brain stimulation in advanced Parkinson disease. *Annals of Neurology*. 2013;74(3):449-457. https://doi.org/10.1002/ana.23951
2. Tinkhauser G, Pogosyan A, Little S, et al. The modulatory effect of adaptive deep brain stimulation on beta bursts in Parkinson's disease. *Brain*. 2017;140(4):1053-1067. https://doi.org/10.1093/brain/awx010
3. Mathiopoulou V, Lofredi R, Feldmann LK, et al. Modulation of subthalamic beta oscillations by movement, dopamine, and deep brain stimulation in Parkinson’s disease. *npj Parkinson's Disease*. 2024;10:77. https://doi.org/10.1038/s41531-024-00693-3
4. Stanslaski S, Summers RLS, Tonder L, et al. Sensing data and methodology from the Adaptive DBS Algorithm for Personalized Therapy in Parkinson’s Disease (ADAPT-PD) clinical trial. *npj Parkinson's Disease*. 2024;10:174. https://doi.org/10.1038/s41531-024-00772-5
5. Oehrn CR, Cernera S, Hammer LH, et al. Chronic adaptive deep brain stimulation versus conventional stimulation in Parkinson’s disease: a blinded randomized feasibility trial. *Nature Medicine*. 2024;30:3345-3356. https://doi.org/10.1038/s41591-024-03196-z
6. Olaru M, et al. Motor network gamma oscillations in chronic home recordings predict dyskinesia in Parkinson’s disease. *Brain*. 2024;147:2038-2052. https://doi.org/10.1093/brain/awae004
7. Busch JL, Kaplan J, Behnke JK, et al. Chronic adaptive deep brain stimulation for Parkinson’s disease: clinical outcomes and programming strategies. *npj Parkinson's Disease*. 2025;11:264. https://doi.org/10.1038/s41531-025-01124-7
8. Mathiopoulou V, Habets J, Feldmann LK, et al. Gamma entrainment induced by deep brain stimulation as a biomarker for motor improvement with neuromodulation. *Nature Communications*. 2025;16:2956. https://doi.org/10.1038/s41467-025-58132-7
9. Wilkins KB, Melbourne JA, Akella P, et al. Beta burst-driven adaptive deep brain stimulation for gait impairment and freezing of gait in Parkinson’s disease. *Brain Communications*. 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC12268161/
10. Cascino S, Roediger J, Oehrn C, et al. Chronic adaptive deep brain stimulation in Parkinson’s disease: ADAPT-START findings and programming principles. *npj Parkinson's Disease*. 2026. https://doi.org/10.1038/s41531-026-01269-z
11. Dixon TC, Strandquist G, Zeng A, et al. Movement-responsive deep brain stimulation for Parkinson’s disease using a remotely optimized neural decoder. *Nature Biomedical Engineering*. 2026;10:110-124. https://doi.org/10.1038/s41551-025-01438-0
