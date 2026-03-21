# Site Deepening Audit (2026-03-21, Maintenance Proxy Calibrator Matrix)

## 対象

- 主対象: `wiki/homeostatic-plasticity-and-maintenance-state.md`
- 副対象: `verification.md`
- 副対象: `wbe_101.md`
- 副対象: `index.md`

## 今回の選定理由

- 2026-03-21 時点で，サイトは human maintenance evidence を `proxy class` として整理し，さらに一部ページでは `operational maturity` まで整理していました。
- しかし，なお欠けていたのは `その proxy が何を較正できるのか` という第三軸でした。
- とくに `wiki/homeostatic-plasticity-and-maintenance-state.md` では，route card 群の整備が進んだ後も front matter の `unknown_points` に古い未整備項目が残っており，本文との内部整合性が崩れていました。
- さらに，astrocyte PET の代表文献 `Villemagne et al. (2022)` の DOI が複数ページで誤記されており，reference integrity 自体に欠陥がありました。

## 主要な批判点

### 1. `unknown_points` が本文の実装状態に追いついていませんでした

- 問題:
  - サイト本文では ECM / post-transcriptional / proteostasis / ionic / cargo / astrocyte / myelin / clearance について個別 route card がすでに導入されていました。
  - それにもかかわらず front matter 側には `どの route-card field を mandatory にするか未固定` という古い unknown が残っていました。
- 根拠:
  - `wiki/homeostatic-plasticity-and-maintenance-state.md` 本文には，各論点ごとの route card table がすでに存在します。
  - したがって，残る unknown は `route card があるかどうか` ではなく，`それらを human proxy calibration にどう接続するか` です。
- 今回実行した変更:
  - stale な unknown を削除し，未解決点を `human-compatible external calibrator` と `same-subject calibration stack` に絞り直しました。

### 2. `proxy class` と `operational maturity` だけでは human observability の限界を十分に表現できませんでした

- 問題:
  - 既存サイトは `regional synaptic-density proxy` や `macro support-state proxy` のような class label を持っていました。
  - しかし，class label だけでは `その measurement がどの latent maintenance-state family を安全に拘束するか` が見えませんでした。
- 根拠:
  - Johansen et al. (2024) は SV2A PET の regional synaptic-density atlas です。
  - Lucchetti et al. (2025) は five-metabolite parcel-similarity graph です。
  - Li et al. (2025) は dynamic deuterium MRSI による kinetic energetic-rate route です。
  - Baadsvik et al. (2024) と Genc et al. (2025) は macro myelin / oligodendrocyte-linked microstructure route です。
  - Villemagne et al. (2022) は reactive astrogliosis route です。
  - Hirschler et al. (2025) と Dagum et al. (2026) は macro support-state / clearance route です。
- 批判:
  - これらはすべて human proxy ですが，同じ latent variable を較正しているわけではありません。
  - したがって `human proxy が増えた` ことと `maintenance-state identification が近づいた` ことを同一視するのは不適切です。
- 今回実行した変更:
  - `wiki/homeostatic-plasticity-and-maintenance-state.md` に `#human-proxy-calibrator-matrix` を追加しました。
  - 各 route について `safe calibrator role` と `what it still does not calibrate` を表で固定しました。
  - `verification.md` と `wbe_101.md` と `index.md` にも，proxy class / operational maturity / calibrator role を分離して読むルールを追記しました。

### 3. 参考文献の DOI 誤記は public technical site として許容できませんでした

- 問題:
  - `Villemagne et al. (2022)` の DOI が `10.2967/jnumed.121.263254` として複数ページに記載されていました。
- 根拠:
  - Journal of Nuclear Medicine / PubMed 系の公開情報では，当該 first-in-human `18F-SMBT-1` 論文の DOI は `10.2967/jnumed.121.263255` です。
- 今回実行した変更:
  - `index.md`
  - `wbe_101.md`
  - `verification.md`
  - `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - 上記すべてで DOI を `10.2967/jnumed.121.263255` に修正しました。

## 今回実行した変更

- `wiki/homeostatic-plasticity-and-maintenance-state.md`
  - `page_highlights` に `proxy class / operational maturity / calibrator role` の三軸分離を追加
  - `known_points` に current human routes がすでに示している calibrator-role matrix を追加
  - stale な `unknown_points` を削除し，未解決点を calibration / standard submission 側へ再定義
  - `#human-proxy-calibrator-matrix` note と table を追加
  - `Villemagne et al. (2022)` DOI を修正
- `verification.md`
  - `page_highlights` に calibrator role rule を追加
  - maintenance-state budget の `Human evidence class / observability ceiling` 行に calibrator role と operational maturity を追加
  - human maintenance evidence note に calibrator role の明示を追加
  - `Villemagne et al. (2022)` DOI を修正
- `wbe_101.md`
  - entry-level note として `Human proxy class, route maturity, and calibrator role are three different questions` を追加
  - `Villemagne et al. (2022)` DOI を修正
- `index.md`
  - landing-page highlights に calibrator role の注意を追加
  - `Villemagne et al. (2022)` DOI を修正

## 検証方針

- `ruby scripts/export_github_wiki.rb`
- `git diff --check`
- `BUNDLE_PATH=vendor/bundle bundle exec jekyll build`

## 外部依存で保留

- same-subject external calibration benchmark for proxy bundles
  - 担当者: 外部の multimodal benchmark 設計者 / 計測系研究者
  - 前提条件: same-subject / same-session / same-perturbation で複数 proxy row を取得し，外部 calibration target を用意すること
  - 完了条件: サイトが `proxy bundle agreement` ではなく `validated calibrator role` を引用できる公開 benchmark が出ること

## 参考文献

1. Johansen A, Beliveau V, Colliander E, et al. An in vivo high-resolution human brain atlas of synaptic density. *Journal of Neuroscience*. 2024;44(33):e1750232024.
   - https://doi.org/10.1523/JNEUROSCI.1750-23.2024
2. Villemagne VL, Harada R, Dore V, et al. First-in-Humans Evaluation of ^18F-SMBT-1, a Novel ^18F-Labeled Monoamine Oxidase-B PET Tracer for Imaging Reactive Astrogliosis. *Journal of Nuclear Medicine*. 2022;63(10):1551-1559.
   - https://doi.org/10.2967/jnumed.121.263255
3. Lucchetti J, Hiba B, Mériaux S, et al. A human brain metabolic connectome. *Nature Communications*. 2025;16:7663.
   - https://doi.org/10.1038/s41467-025-66124-w
4. Li H, Zhu X-H, Chen W. Mapping glucose transport and metabolism in the human brain in vivo using dynamic deuterium metabolic imaging at 7 T. *PNAS Nexus*. 2025;4(4):pgaf072.
   - https://doi.org/10.1093/pnasnexus/pgaf072
5. Baadsvik EL, Weiger M, Froidevaux R, Schildknecht CM, Ineichen BV, Pruessmann KP. Myelin bilayer mapping in the human brain in vivo. *Magnetic Resonance in Medicine*. 2024;91(6):2332-2344.
   - https://doi.org/10.1002/mrm.29998
6. Genc S, Ball G, Chamberland M, et al. MRI signatures of cortical microstructure in human development align with oligodendrocyte cell-type expression. *Nature Communications*. 2025;16:3317.
   - https://doi.org/10.1038/s41467-025-58604-w
7. Hirschler L, Jann K, Van Cauter S, et al. Brainwide mapping of human cerebrospinal fluid mobility and its drivers. *Nature Neuroscience*. 2025;28:1307-1318.
   - https://doi.org/10.1038/s41593-025-02073-3
8. Dagum AB, Tian R, Korley A, et al. The glymphatic system supports transport of amyloid beta and tau from the brain to blood in humans. *Nature Communications*. 2026;17:1114.
   - https://doi.org/10.1038/s41467-026-68374-8
