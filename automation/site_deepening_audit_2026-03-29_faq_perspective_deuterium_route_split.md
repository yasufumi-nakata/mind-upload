# Site Deepening Audit (2026-03-29, FAQ / Perspective deuterium route split)

## 対象

- 主対象:
  - `faq.md`
  - `perspective.md`
- 調査範囲: 技術 / 自然科学のみ
- 明示的に除外した論点: 哲学、法学、制度論

## 今回この箇所を選んだ理由

- `index.md` と `verification.md` では、2026-03-29 時点ですでに deuterium route が
  - `metabolite-mapping / absolute quantification`
  - `kinetic-rate imaging`
  に分かれておりました。
- しかし front door に近い `faq.md` と `perspective.md` では、なお `dynamic deuterium metabolite / rate imaging` の一段圧縮が残っておりました。
- この圧縮を残すと、読者が
  - absolute metabolite distribution
  - blood-input / kinetic-model rate map
  - dose dependence
  - route-local repeatability
  を一続きの `deuterium route` と誤読しやすくなります。
- それは site-wide rule と不整合でございます。現在のサイトは、route name ではなく quantity type と operating condition まで分けて claim ceiling を決める方針だからです。

## web確認対象

- `https://doi.org/10.1002/mrm.70308`
- `https://doi.org/10.1093/pnasnexus/pgaf072`
- `https://doi.org/10.1002/jmri.29532`
- `https://doi.org/10.1186/s41747-024-00426-4`
- 補助確認:
  - `https://doi.org/10.1002/nbm.70169`

## 主要結論

- deuterium は一つの inferential object ではございません。
- [Karkouri et al. (2026)](https://doi.org/10.1002/mrm.70308) は、7 T の named absolute-quantification pipeline を通じて HDO / Glc / Glx / Lac を map する route を強めております。
- [Li et al. (2025)](https://doi.org/10.1093/pnasnexus/pgaf072) は、blood-input と kinetic model によって glucose transport / metabolic-rate map を作る route を強めております。
- [Ahmadian et al. (2025)](https://doi.org/10.1002/jmri.29532) は、[6,6'-²H₂]glucose dose が human brain-side metabolite visibility に影響することを示しており、route の operating point が可変であることを示します。
- [Bøgh et al. (2024)](https://doi.org/10.1186/s41747-024-00426-4) は、repeatability が named 3 T protocol に依存することを示しており、`deuterium result exists` を `portable stable meter exists` に変換してはいけません。
- したがって、front door では少なくとも
  - `deuterium metabolite-mapping / absolute quantification`
  - `deuterium kinetic-rate imaging`
  を別 row に分け、
  - `dose`
  - `repeatability`
  を operating condition として別に書く必要がございました。

## 根拠付き批判

### 1. absolute map と kinetic-rate map は同じ量ではございません

- [Karkouri et al. (2026)](https://doi.org/10.1002/mrm.70308) は absolute quantification pipeline を前面に置いています。
- [Li et al. (2025)](https://doi.org/10.1093/pnasnexus/pgaf072) は blood-input / kinetic-model route を前面に置いています。

批判:

- 旧 `faq.md` と `perspective.md` は deuterium を `metabolite / rate imaging` と一行で置いていたため、absolute distribution と model-conditioned rate map が同一 object に見えやすい状態でした。
- しかし quantity type と model burden が違うため、この圧縮は不正確でございます。

### 2. deuterium route の読み方は dose-free ではございません

- [Ahmadian et al. (2025)](https://doi.org/10.1002/jmri.29532) は、different [6,6'-²H₂]glucose doses が deuterated metabolite visibility を変えることを示しました。

批判:

- したがって `deuterium route exists` を `one invariant energetic meter exists` と読むことはできません。
- dose は implementation detail ではなく operating-point condition でございます。

### 3. repeatability も route-free guarantee ではございません

- [Bøgh et al. (2024)](https://doi.org/10.1186/s41747-024-00426-4) は、3 T healthy-volunteer DMI における repeatability を named protocol の下で示しました。

批判:

- これは deuterium route が無意味という意味ではございません。
- むしろ、repeatability は protocol-specific に議論すべきであり、modality label のみで持ち運べる保証ではない、という意味でございます。

### 4. front door が coarse だと site-wide stop rule が戻ってしまいます

- `index.md`, `verification.md`, `mind_uploading_papers.md`, `research_harvest_50.md` は既に deuterium family split を導入済みでございました。

批判:

- それにもかかわらず `faq.md` と `perspective.md` が粗いままだと、読者は入口で再び `deuterium imaging improved` という一語へ戻ります。
- front door こそ quantity type と operating condition を最初に固定すべきでございました。

## 今回実行した変更

- `faq.md`
  - front matter の `known_points` を更新し、deuterium を `absolute metabolite mapping / quantification` と `kinetic-rate imaging` に分離しました。
  - Q2 本文を更新し、Karkouri 2026, Li 2025, Ahmadian 2025, Bøgh 2024 を用いて deuterium の quantity split と operating-point burden を明記しました。
  - human-route table を `deuterium metabolite-mapping / absolute quantification` と `dynamic deuterium kinetic-rate imaging` の 2 行に分割しました。
  - `Route name alone is too coarse` と `Eight quick checks` を更新し、absolute distribution / kinetic rate / repeatability の区別が front door で読めるようにしました。
  - 参考文献リストへ Karkouri 2026, Ahmadian 2025, Bøgh 2024 を追加しました。

- `perspective.md`
  - front matter の `note` と `page_highlights` を更新し、deuterium route split をページ冒頭で見えるようにしました。
  - human-route table を `absolute quantification` と `kinetic-rate imaging` に分割しました。
  - `31P route names need their own quantity split` note を `31P and deuterium route names need their own quantity split` に改稿し、Ahmadian 2025 / Bøgh 2024 まで含めて operating condition を追加しました。
  - `Proxy class, operational maturity, and calibrator role are different axes` と `Operational-maturity collapse` を更新し、dose dependence と protocol-specific repeatability も maturity burden として読ませるようにしました。
  - `Key Technical Challenges` の human-evidence paragraph も、`energetic-balance / rate imaging` という粗い表現をやめ、deuterium absolute-quantification と kinetic-rate route を別に書くよう修正しました。

## 今回止めた誤読

- `deuterium imaging exists` = `one generic energetic meter exists`
- `absolute metabolite map` = `kinetic-rate map`
- `deuterium route worked` = `dose no longer matters`
- `repeatability was reported somewhere` = `repeatability is route-free and portable`
- `31P / deuterium / energetic imaging` を一つの近い進歩量としてまとめてよい

## 外部依存タスク

- なし
  - 今回の作業は web 上の一次文献確認、repo 内公開ページ改稿、監査メモ作成、生成物確認、commit、push までこのセッションで完結可能でございます。

## 参考文献

1. Karkouri J, Novoselova M, Rodgers CT, et al. Absolute Quantification of Brain Deuterium Metabolic Imaging in Healthy Volunteers and Glioblastoma Patients at 7T. *Magnetic Resonance in Medicine*. 2026.
   - https://doi.org/10.1002/mrm.70308
2. Li X, Zhu X-H, Li Y, et al. Quantitative mapping of key glucose metabolic rates in the human brain using dynamic deuterium magnetic resonance spectroscopic imaging. *PNAS Nexus*. 2025.
   - https://doi.org/10.1093/pnasnexus/pgaf072
3. Ahmadian N, Karkouri J, Deelchand DK, et al. Human Brain Deuterium Metabolic Imaging at 7 T: Impact of Different [6,6'-2H2]Glucose Doses. *Journal of Magnetic Resonance Imaging*. 2025.
   - https://doi.org/10.1002/jmri.29532
4. Bøgh N, Vaeggemose M, Schulte RF, et al. Repeatability of deuterium metabolic imaging of healthy volunteers at 3 T. *European Radiology Experimental*. 2024.
   - https://doi.org/10.1186/s41747-024-00426-4
5. Cocking DJ, Damion RA, Simpson EJ, Auer DPA, Bowtell R. Advancing Deuterium MRI to Track Human Cerebral Glucose Metabolism at 7 T: A Comparison of Glucose-d2 and Glucose-d7 Ingestion. *NMR in Biomedicine*. 2025.
   - https://doi.org/10.1002/nbm.70169
