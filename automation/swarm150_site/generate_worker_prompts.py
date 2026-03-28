#!/usr/bin/env python3
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parent
PROMPTS = ROOT / 'prompts'
PROMPTS.mkdir(parents=True, exist_ok=True)
REPO_ROOT = ROOT.parent.parent

pages = [
    'index.md',
    'verification.md',
    'datasets.md',
    'hands_on.md',
    'faq.md',
    'issue.md',
    'wbe_101.md',
    'eeg_101.md',
    'glossary.md',
    'casework.md',
    'idea.md',
    'proposals.md',
    'technical_proposal_46.md',
    'technical_proposal_48.md',
    'technical_proposal_61.md',
]

lenses = [
    'Improve the introduction for first-time readers',
    'Clarify testable claims and pass/fail conditions',
    'Reduce ambiguity and define terms more clearly',
    'Cut redundancy and improve readability',
    'Strengthen guidance to the next page to read',
    'Make the next practical action more concrete',
    'Separate external dependencies more clearly',
    'Preempt likely misunderstandings',
    'Tighten paragraph structure (one message per paragraph)',
    'Unify tone (polite, without overclaiming)',
]

assert len(pages) * len(lenses) == 150

meta_rows = []
worker_id = 1
for page in pages:
    for lens in lenses:
        prompt = f'''You are web-content improvement worker {worker_id}/150.

Target repository: {REPO_ROOT}
Target file: {page}
Improvement lens: {lens}

Task:
1. Read the target file and choose exactly one place with clear room for improvement.
2. Produce exactly one short replacement-ready text improvement.

Required output format (JSON only; no extra explanation before or after):
{{
  "worker_id": {worker_id},
  "file": "{page}",
  "lens": "{lens}",
  "section_hint": "Short section label",
  "problem": "One-sentence description of the problem",
  "before_excerpt": "Short excerpt of the target text (40-160 characters)",
  "after_text": "Replacement draft (80-220 characters)",
  "reason": "1-2 sentence reason for the change",
  "priority": "high"
}}

Constraints:
- Do not add new factual claims if the facts are uncertain.
- Preserve the existing page policy, especially its focus on testability and reproducibility.
- Do not write HTML tags; propose plain body text only.
- Output JSON only.
'''
        (PROMPTS / f'worker{worker_id}.txt').write_text(prompt, encoding='utf-8')
        meta_rows.append((worker_id, page, lens))
        worker_id += 1

merge_prompt = '''You are the merge worker.
Merge the worker output JSON items below and summarize the top three adoption candidates for each page.

Output format (Markdown):
# Swarm Summary
## by page
### <page>
- Top candidate 1: ...
- Top candidate 2: ...
- Top candidate 3: ...

## global priorities
- 10 highest-priority improvements overall
'''
(PROMPTS / 'merge.txt').write_text(merge_prompt, encoding='utf-8')

with (ROOT / 'worker_matrix.csv').open('w', encoding='utf-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(['worker_id', 'file', 'lens'])
    w.writerows(meta_rows)

print('generated', len(meta_rows), 'worker prompts')
