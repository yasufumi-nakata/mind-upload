#!/usr/bin/env python3
"""公開向け Markdown / JSON 文書を日本語化する補助スクリプト。

このスクリプトは文書構造を保つため、YAML front matter のキー、URL、
コードフェンス、インラインコードを翻訳対象から外し、自然文だけを
日本語へ変換する。既に日本語中心の断片は再翻訳しない。
"""

from __future__ import annotations

import argparse
import json
import os
import re
import signal
import sys
import time
import warnings
from pathlib import Path
from typing import Any

import yaml

warnings.filterwarnings("ignore", message="urllib3 v2 only supports OpenSSL")

try:
    from deep_translator import GoogleTranslator
except Exception:  # pragma: no cover - 実行環境差分のフォールバック
    GoogleTranslator = None

try:
    from argostranslate import translate as argos_translate
except Exception:  # pragma: no cover - 実行環境差分のフォールバック
    argos_translate = None


ROOT = Path(__file__).resolve().parents[1]
CACHE_PATH = ROOT / "ignore" / "translation_cache_ja.json"
MAX_CHARS = 2600
GOOGLE_TIMEOUT_SECONDS = 25

CODE_FENCE_RE = re.compile(r"(^```.*?^```)", re.M | re.S)
FRONT_MATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[([^\]\n]+)\]\(([^)\n]+)\)")
HTML_TAG_RE = re.compile(r"<!--.*?-->|</?[^>\n]+>", re.S)
URL_RE = re.compile(r"https?://[^\s<>\"')]+")
EMAIL_RE = re.compile(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}")
ASCII_WORD_RE = re.compile(r"[A-Za-z][A-Za-z0-9_-]{2,}")
JAPANESE_RE = re.compile(r"[\u3040-\u30ff\u3400-\u9fff]")
FRONT_MATTER_KEEP_KEYS = {"layout", "body_class", "url", "last_updated"}


class Translator:
    def __init__(self, cache_path: Path, prefer: str = "google") -> None:
        self.cache_path = cache_path
        self.cache_path.parent.mkdir(parents=True, exist_ok=True)
        if cache_path.exists():
            self.cache: dict[str, str] = json.loads(cache_path.read_text(encoding="utf-8"))
        else:
            self.cache = {}
        self.prefer = prefer
        self.google = GoogleTranslator(source="en", target="ja") if GoogleTranslator else None

    def save(self) -> None:
        self.cache_path.write_text(
            json.dumps(self.cache, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    def should_translate(self, text: str) -> bool:
        if not text or not ASCII_WORD_RE.search(text):
            return False
        # 日本語が多い断片は、残った専門語や固有名詞を無理に再翻訳しない。
        japanese_chars = len(JAPANESE_RE.findall(text))
        ascii_words = len(ASCII_WORD_RE.findall(text))
        return not (japanese_chars >= 12 and ascii_words <= 4)

    def translate_raw(self, text: str) -> str:
        key = text.strip()
        if not key:
            return text
        if key in self.cache:
            translated = self.cache[key]
            return text.replace(key, translated, 1)

        translated = None
        if self.prefer == "google" and self.google is not None:
            for attempt in range(3):
                try:
                    translated = self.translate_google_with_timeout(key)
                    break
                except Exception as exc:
                    if attempt == 2:
                        print(f"[warn] Google translation failed, fallback to Argos: {exc}", file=sys.stderr)
                    time.sleep(1.5 * (attempt + 1))

        if translated is None:
            if argos_translate is None:
                raise RuntimeError("No translator is available")
            translated = argos_translate.translate(key, "en", "ja")

        self.cache[key] = translated
        return text.replace(key, translated, 1)

    def translate_google_with_timeout(self, text: str) -> str:
        def handle_timeout(_signum: int, _frame: Any) -> None:
            raise TimeoutError("Google translation timed out")

        previous = signal.signal(signal.SIGALRM, handle_timeout)
        signal.alarm(GOOGLE_TIMEOUT_SECONDS)
        try:
            return self.google.translate(text)
        finally:
            signal.alarm(0)
            signal.signal(signal.SIGALRM, previous)

    def translate_segment(self, text: str) -> str:
        if not self.should_translate(text):
            return text

        placeholders: dict[str, str] = {}

        def stash(value: str) -> str:
            token = f"PH{len(placeholders)}X"
            placeholders[token] = value
            return token

        protected = HTML_TAG_RE.sub(lambda m: stash(m.group(0)), text)
        protected = INLINE_CODE_RE.sub(lambda m: stash(m.group(0)), protected)
        protected = URL_RE.sub(lambda m: stash(m.group(0)), protected)
        protected = EMAIL_RE.sub(lambda m: stash(m.group(0)), protected)

        translated = self.translate_protected(protected)
        for token, value in placeholders.items():
            translated = translated.replace(token, value)
        return translated

    def translate_protected(self, text: str) -> str:
        if len(text) <= MAX_CHARS:
            return self.translate_raw(text)
        return "".join(self.translate_raw(chunk) for chunk in self.split_long_text(text))

    def split_long_text(self, text: str) -> list[str]:
        parts = re.split(r"(\s+)", text)
        chunks: list[str] = []
        current = ""
        for part in parts:
            if len(current) + len(part) > MAX_CHARS and current:
                chunks.append(current)
                current = ""
            current += part
        if current:
            chunks.append(current)
        return chunks

    def translate_markdown_body(self, body: str) -> str:
        parts = CODE_FENCE_RE.split(body)
        translated_parts = []
        for part in parts:
            if not part:
                continue
            if part.startswith("```"):
                translated_parts.append(part)
            else:
                translated_parts.append(self.translate_text_blocks(part))
        return "".join(translated_parts)

    def translate_text_blocks(self, text: str) -> str:
        paragraphs = re.split(r"(\n\s*\n)", text)
        out: list[str] = []
        for para in paragraphs:
            if not para.strip():
                out.append(para)
                continue
            if self.has_markdown_structure(para):
                out.append("".join(self.translate_structural_line(line) for line in para.splitlines(keepends=True)))
                continue
            out.extend(self.translate_paragraph(para))
        return "".join(out)

    def has_markdown_structure(self, text: str) -> bool:
        return any(
            re.match(r"\s*(#{1,6}\s+|[-*+]\s+|\d+\.\s+|>\s+|\|)", line)
            for line in text.splitlines()
        )

    def translate_structural_line(self, line: str) -> str:
        newline = "\n" if line.endswith("\n") else ""
        body = line[:-1] if newline else line
        if not body.strip():
            return line

        if re.match(r"\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$", body):
            return line

        if body.lstrip().startswith("|"):
            return self.translate_table_line(body) + newline

        match = re.match(r"^(\s*#{1,6}\s+)(.*)$", body)
        if match:
            return f"{match.group(1)}{self.translate_segment(match.group(2))}{newline}"

        match = re.match(r"^(\s*[-*+]\s+)(.*)$", body)
        if match:
            return f"{match.group(1)}{self.translate_segment(match.group(2))}{newline}"

        match = re.match(r"^(\s*\d+\.\s+)(.*)$", body)
        if match:
            return f"{match.group(1)}{self.translate_segment(match.group(2))}{newline}"

        match = re.match(r"^(\s*>\s+)(.*)$", body)
        if match:
            return f"{match.group(1)}{self.translate_segment(match.group(2))}{newline}"

        return self.translate_segment(body) + newline

    def translate_table_line(self, line: str) -> str:
        cells = line.split("|")
        translated = []
        for index, cell in enumerate(cells):
            if index == 0 or index == len(cells) - 1:
                translated.append(cell)
            else:
                leading = re.match(r"^\s*", cell).group(0)
                trailing = re.search(r"\s*$", cell).group(0)
                content = cell.strip()
                translated.append(f"{leading}{self.translate_segment(content)}{trailing}")
        return "|".join(translated)

    def translate_paragraph(self, para: str) -> list[str]:
        if len(para) <= MAX_CHARS:
            return [self.translate_segment(para)]

        out: list[str] = []
        current = ""
        for line in para.splitlines(keepends=True):
            if len(current) + len(line) > MAX_CHARS and current:
                out.append(self.translate_segment(current))
                current = ""
            current += line
        if current:
            out.append(self.translate_segment(current))
        return out

    def translate_value(self, value: Any, key: str | None = None) -> Any:
        if key in FRONT_MATTER_KEEP_KEYS:
            return value
        if isinstance(value, str):
            if value.startswith(("http://", "https://", "/", "#")):
                return value
            return self.translate_segment(value)
        if isinstance(value, list):
            return [self.translate_value(item, key=key) for item in value]
        if isinstance(value, dict):
            return {child_key: self.translate_value(item, key=child_key) for child_key, item in value.items()}
        return value


def split_front_matter(text: str) -> tuple[dict[str, Any] | None, str]:
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return None, text
    data = yaml.safe_load(match.group(1)) or {}
    return data, text[match.end() :]


def dump_front_matter(data: dict[str, Any]) -> str:
    dumped = yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=120)
    return f"---\n{dumped}---\n"


def translate_markdown_file(path: Path, translator: Translator, dry_run: bool) -> bool:
    original = path.read_text(encoding="utf-8")
    front_matter, body = split_front_matter(original)
    if front_matter is None:
        updated = translator.translate_markdown_body(original)
    else:
        translated_front = translator.translate_value(front_matter)
        updated = dump_front_matter(translated_front) + translator.translate_markdown_body(body)

    if updated == original:
        return False
    if not dry_run:
        path.write_text(updated, encoding="utf-8")
    return True


def translate_json_file(path: Path, translator: Translator, dry_run: bool) -> bool:
    original = path.read_text(encoding="utf-8")
    data = json.loads(original)
    updated_data = translator.translate_value(data)
    updated = json.dumps(updated_data, ensure_ascii=False, indent=2) + "\n"
    if updated == original:
        return False
    if not dry_run:
        path.write_text(updated, encoding="utf-8")
    return True


def default_targets() -> list[Path]:
    targets: list[Path] = []
    targets.extend(sorted(ROOT.glob("*.md")))
    targets.extend(sorted((ROOT / "wiki").glob("*.md")))
    targets.extend(
        [
            ROOT / "automation" / "README.md",
            ROOT / "dataset_description.json",
        ]
    )
    return [path for path in targets if path.exists()]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="公開コンテンツを日本語化する")
    parser.add_argument("paths", nargs="*", help="対象ファイル。未指定なら公開 Markdown と Wiki ソースを処理する。")
    parser.add_argument("--dry-run", action="store_true", help="ファイルを書き換えず変更有無だけ確認する。")
    parser.add_argument("--prefer", choices=["google", "argos"], default=os.environ.get("TRANSLATE_PREFER", "google"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    translator = Translator(CACHE_PATH, prefer=args.prefer)
    targets = [ROOT / p for p in args.paths] if args.paths else default_targets()
    changed: list[str] = []
    try:
        for index, path in enumerate(targets, 1):
            rel = path.relative_to(ROOT)
            print(f"[{index}/{len(targets)}] {rel}", flush=True)
            if path.suffix == ".json":
                did_change = translate_json_file(path, translator, args.dry_run)
            elif path.suffix in {".md", ".html"}:
                did_change = translate_markdown_file(path, translator, args.dry_run)
            else:
                continue
            if did_change:
                changed.append(str(rel))
            if index % 5 == 0:
                translator.save()
    finally:
        translator.save()

    print("changed files:")
    for rel in changed:
        print(f"- {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
