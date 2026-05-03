#!/usr/bin/env python3
"""GitHub Issues の全件インベントリを日本語 Wiki ページとして生成する。"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from translate_content_to_ja import Translator  # noqa: E402


FIELDS = [
    "number",
    "title",
    "state",
    "createdAt",
    "updatedAt",
    "closedAt",
    "labels",
    "body",
    "url",
    "comments",
]

OUTPUT_PATH = ROOT / "wiki" / "github-issues-inventory.md"
STATE_LABEL = {"OPEN": "未完了", "CLOSED": "クローズ済み"}
LABEL_MAP = {
    "bug": "バグ",
    "documentation": "文書",
    "duplicate": "重複",
    "enhancement": "改善",
    "good first issue": "初回向け",
    "help wanted": "協力歓迎",
    "invalid": "無効",
    "question": "質問",
    "wontfix": "対応しない",
}
PATH_RE = re.compile(r"\b(?:[A-Za-z0-9_.-]+/)*[A-Za-z0-9_.-]+\.(?:md|html|py|rb|sh|json|csv|yml|yaml)\b")
HTML_TAG_RE = re.compile(r"<[^>]+>")
MARKDOWN_LINK_RE = re.compile(r"!?\[([^\]]+)\]\(([^)]+)\)")
MARKDOWN_MARK_RE = re.compile(r"[*_>#`]")
WHITESPACE_RE = re.compile(r"\s+")
JAPANESE_RE = re.compile(r"[\u3040-\u30ff\u3400-\u9fff]")
ASCII_WORD_RE = re.compile(r"[A-Za-z][A-Za-z0-9_-]{2,}")


def run_gh() -> list[dict[str, Any]]:
    command = [
        "gh",
        "issue",
        "list",
        "--state",
        "all",
        "--limit",
        "1000",
        "--json",
        ",".join(FIELDS),
    ]
    result = subprocess.run(command, cwd=ROOT, check=True, text=True, capture_output=True)
    issues = json.loads(result.stdout)
    issues.sort(key=lambda issue: int(issue["number"]), reverse=True)
    return issues


def load_issues(path: Path | None) -> list[dict[str, Any]]:
    if path is None:
        return run_gh()
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict) and "issues" in data:
        issues = data["issues"]
    else:
        issues = data
    issues.sort(key=lambda issue: int(issue["number"]), reverse=True)
    return issues


def should_translate(text: str) -> bool:
    if not ASCII_WORD_RE.search(text):
        return False
    japanese_chars = len(JAPANESE_RE.findall(text))
    ascii_words = len(ASCII_WORD_RE.findall(text))
    return japanese_chars < 8 or ascii_words > 8


def translate_text(translator: Translator, text: str) -> str:
    text = clean_inline(text)
    if not should_translate(text):
        return text
    try:
        translated = translator.translate_segment(text)
    except Exception:
        return text
    return clean_inline(translated)


def clean_inline(text: str) -> str:
    text = HTML_TAG_RE.sub("", text)
    text = MARKDOWN_LINK_RE.sub(r"\1", text)
    text = MARKDOWN_MARK_RE.sub("", text)
    text = text.replace("|", "／")
    return WHITESPACE_RE.sub(" ", text).strip()


def issue_summary(issue: dict[str, Any], translator: Translator) -> str:
    body = issue.get("body") or ""
    lines = []
    for raw_line in body.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith(("<!--", "```")):
            continue
        if set(line) <= {"-", "="}:
            continue
        line = re.sub(r"^#{1,6}\s*", "", line)
        line = re.sub(r"^[-*]\s+\[[ xX]\]\s*", "", line)
        line = re.sub(r"^[-*]\s+", "", line)
        line = clean_inline(line)
        if not line:
            continue
        if len(line) < 8 and not JAPANESE_RE.search(line):
            continue
        lines.append(line)
        if len(" ".join(lines)) >= 160:
            break
    if not lines:
        return "本文なし。"
    summary = " ".join(lines)
    summary = translate_text(translator, summary)
    if len(summary) > 180:
        summary = summary[:177].rstrip() + "..."
    return summary


def issue_targets(issue: dict[str, Any]) -> str:
    text = " ".join([issue.get("title") or "", issue.get("body") or ""])
    paths = []
    for match in PATH_RE.finditer(text):
        path = match.group(0)
        if path not in paths:
            paths.append(path)
        if len(paths) >= 4:
            break
    return " / ".join(paths) if paths else "全体方針または未分類"


def issue_labels(issue: dict[str, Any]) -> str:
    labels = []
    for label in issue.get("labels") or []:
        name = label.get("name", "")
        labels.append(LABEL_MAP.get(name, name))
    return "、".join(labels) if labels else "なし"


def iso_date(value: str | None) -> str:
    if not value:
        return "-"
    return value[:10]


def missing_numbers(issues: list[dict[str, Any]]) -> list[int]:
    numbers = {int(issue["number"]) for issue in issues}
    if not numbers:
        return []
    return [number for number in range(min(numbers), max(numbers) + 1) if number not in numbers]


def render(issues: list[dict[str, Any]], translator: Translator) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    count = len(issues)
    open_count = sum(1 for issue in issues if issue["state"] == "OPEN")
    closed_count = sum(1 for issue in issues if issue["state"] == "CLOSED")
    comment_count = sum(len(issue.get("comments") or []) for issue in issues)
    numbers = [int(issue["number"]) for issue in issues]
    missing = missing_numbers(issues)
    min_number = min(numbers) if numbers else "-"
    max_number = max(numbers) if numbers else "-"
    missing_text = "、".join(f"#{number}" for number in missing) if missing else "なし"

    lines = [
        "---",
        "layout: default",
        "title: 'Wiki: GitHub Issues 全件インベントリ'",
        "description: GitHub Issues の全件を日本語要約で確認するための取り込みページ。",
        "article_type: ウィキ",
        "subtitle: GitHub Issues の状態、要旨、反映先を全件で追跡します。",
        "author: マインドアップロード研究プロジェクト",
        "last_updated: '2026-05-03'",
        "note: GitHub Issues 全件取り込み",
        "audience: Issue の反映状況、未完了項目、クローズ済み論点をまとめて確認したい人。",
        "reading_time: 30～60分",
        "---",
        "# GitHub Issues 全件インベントリ",
        "",
        "このページは、GitHub Issues を公開 Wiki 側で漏れなく追跡するための生成インベントリです。本文そのものを完成済みの主張として扱わず、各 issue の番号、状態、要旨、反映先、GitHub URL を確認するために使います。",
        "",
        "## 取り込み範囲",
        "",
        f"- 取得コマンド: `gh issue list --state all --limit 1000 --json {','.join(FIELDS)}`",
        f"- 取得日時: {now}",
        f"- 取り込み件数: {count} 件",
        f"- open: {open_count} 件",
        f"- closed: {closed_count} 件",
        f"- issue 番号範囲: #{min_number}～#{max_number}",
        f"- GitHub issue ではない番号または欠番: {missing_text}",
        f"- 取得したコメント数: {comment_count} 件",
        "",
        "## 未完了 issue",
        "",
    ]

    open_issues = [issue for issue in issues if issue["state"] == "OPEN"]
    if open_issues:
        for issue in open_issues:
            title = translate_text(translator, issue["title"])
            lines.append(f"- [#{issue['number']} {title}]({issue['url']})（更新日: {iso_date(issue.get('updatedAt'))}）")
    else:
        lines.append("- 現在、未完了 issue はありません。")

    lines.extend(
        [
            "",
            "## 全件一覧",
            "",
            "| 番号 | 状態 | 日本語タイトル | 要旨 | 主な反映先 | ラベル | コメント | 更新日 |",
            "|---:|---|---|---|---|---|---:|---|",
        ]
    )

    for issue in issues:
        title = translate_text(translator, issue["title"])
        summary = issue_summary(issue, translator)
        labels = issue_labels(issue)
        targets = issue_targets(issue)
        comments = len(issue.get("comments") or [])
        lines.append(
            "| "
            f"[#{issue['number']}]({issue['url']}) | "
            f"{STATE_LABEL.get(issue['state'], issue['state'])} | "
            f"{title} | "
            f"{summary} | "
            f"{targets} | "
            f"{labels} | "
            f"{comments} | "
            f"{iso_date(issue.get('updatedAt'))} |"
        )

    lines.extend(
        [
            "",
            "## 運用メモ",
            "",
            "- このページは issue の存在と内容を取り込むための索引です。クローズ済み issue は、解決済みの科学的主張を意味しません。",
            "- 本文に出てくる外部依存タスクは、このリポジトリ内で実行できる変更とは分けて扱います。",
            "- issue の本文やコメントに更新が入った場合は、`python3 scripts/sync_github_issues_inventory.py` を再実行して、このページと GitHub Wiki export を更新します。",
        ]
    )

    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=None, help="gh issue list と同じ JSON を読む場合のパス")
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    args = parser.parse_args()

    issues = load_issues(args.input)
    translator = Translator(ROOT / "ignore" / "translation_cache_ja.json")
    output = render(issues, translator)
    args.output.write_text(output, encoding="utf-8")
    translator.save()
    print(f"{len(issues)} 件の GitHub Issues を {args.output} に取り込みました")


if __name__ == "__main__":
    main()
