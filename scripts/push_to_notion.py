#!/usr/bin/env python3
# coding=utf-8
"""
将 finradar Markdown 报告写入 Notion 父页面的子页面。

用法示例:
  python scripts/push_to_notion.py --date 20260209 --type morning
  NOTION_API_TOKEN=... NOTION_PARENT_PAGE_ID=... python scripts/push_to_notion.py --type evening
"""

import argparse
import json
import os
import re
import time
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import requests

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_REPORT = PROJECT_ROOT / "output" / "report"
NOTION_API_BASE = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"
BEIJING_TZ = ZoneInfo("Asia/Shanghai")
INLINE_MD_PATTERN = re.compile(
    r"\[([^\]]+)\]\((https?://[^)\s]+)\)|\*\*([^*]+)\*\*|__([^_]+)__|`([^`]+)`|\*([^*]+)\*|_([^_]+)_|~~([^~]+)~~"
)


def now_beijing() -> datetime:
    return datetime.now(BEIJING_TZ)


def resolve_report_type(raw_type: str) -> str:
    if raw_type != "auto":
        return raw_type
    hour = now_beijing().hour
    if 5 <= hour < 14:
        return "morning"
    if 14 <= hour < 24:
        return "evening"
    return "morning"


def extract_page_id(raw: str) -> str:
    if not raw:
        raise ValueError("Notion 父页面不能为空")
    cleaned = re.sub(r"[^0-9a-fA-F]", "", raw)
    m = re.search(r"[0-9a-fA-F]{32}", cleaned)
    if not m:
        raise ValueError(f"无法从输入中解析 Notion page id: {raw}")
    return m.group(0).lower()


def split_text_chunks(text: str, max_len: int = 1900) -> list[str]:
    text = text or ""
    if not text:
        return ["\u200b"]
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start + max_len])
        start += max_len
    return chunks


def text_object(content: str, bold: bool = False, italic: bool = False,
                code: bool = False, strikethrough: bool = False,
                href: str | None = None) -> dict:
    text_payload = {"content": content}
    if href:
        text_payload["link"] = {"url": href}
    return {
        "type": "text",
        "text": text_payload,
        "annotations": {
            "bold": bold,
            "italic": italic,
            "strikethrough": strikethrough,
            "underline": False,
            "code": code,
            "color": "default",
        },
    }


def chunk_rich_text_items(items: list[dict], max_len: int = 1800) -> list[dict]:
    """确保每个 rich_text 片段不超过 Notion 限制。"""
    chunks: list[dict] = []
    for item in items:
        text_payload = item.get("text", {})
        content = str(text_payload.get("content", "") or "")
        if not content:
            continue
        link = text_payload.get("link", None)
        ann = item.get("annotations", {})
        while content:
            piece = content[:max_len]
            payload = {"content": piece}
            if link:
                payload["link"] = link
            chunks.append({
                "type": "text",
                "text": payload,
                "annotations": ann,
            })
            content = content[max_len:]
    return chunks or [text_object("\u200b")]


def parse_inline_markdown(text: str) -> list[dict]:
    """将行内 Markdown 转为 Notion rich_text（支持粗体/斜体/行内代码/删除线/链接）。"""
    text = str(text or "")
    if not text:
        return [text_object("\u200b")]

    result: list[dict] = []
    pos = 0
    for m in INLINE_MD_PATTERN.finditer(text):
        if m.start() > pos:
            result.append(text_object(text[pos:m.start()]))

        if m.group(1) is not None and m.group(2) is not None:  # [text](url)
            result.append(text_object(m.group(1), href=m.group(2)))
        elif m.group(3) is not None or m.group(4) is not None:  # **bold** / __bold__
            result.append(text_object(m.group(3) or m.group(4), bold=True))
        elif m.group(5) is not None:  # `code`
            result.append(text_object(m.group(5), code=True))
        elif m.group(6) is not None or m.group(7) is not None:  # *italic* / _italic_
            result.append(text_object(m.group(6) or m.group(7), italic=True))
        elif m.group(8) is not None:  # ~~strike~~
            result.append(text_object(m.group(8), strikethrough=True))

        pos = m.end()

    if pos < len(text):
        result.append(text_object(text[pos:]))

    return chunk_rich_text_items(result)


def text_block(block_type: str, rich_text: list[dict]) -> dict:
    return {
        "object": "block",
        "type": block_type,
        block_type: {"rich_text": rich_text},
    }


def code_block(content: str, language: str = "plain text") -> dict:
    return {
        "object": "block",
        "type": "code",
        "code": {
            "rich_text": [text_object(content)],
            "language": language if language else "plain text",
        },
    }


def append_text_blocks(blocks: list[dict], block_type: str, text: str) -> None:
    rich_text = parse_inline_markdown(text)
    for i in range(0, len(rich_text), 90):
        blocks.append(text_block(block_type, rich_text[i:i + 90]))


def append_code_blocks(blocks: list[dict], code_text: str, language: str) -> None:
    for piece in split_text_chunks(code_text, max_len=1800):
        blocks.append(code_block(piece, language=language))


def markdown_to_notion_blocks(markdown_text: str) -> list[dict]:
    blocks: list[dict] = []
    lines = markdown_text.splitlines()
    in_code = False
    code_lang = "plain text"
    code_lines: list[str] = []

    def flush_code() -> None:
        nonlocal code_lines, code_lang
        if code_lines:
            append_code_blocks(blocks, "\n".join(code_lines), code_lang)
        code_lines = []
        code_lang = "plain text"

    for raw_line in lines:
        line = raw_line.rstrip("\n")
        stripped = line.strip()

        if stripped.startswith("```"):
            if not in_code:
                in_code = True
                code_lang = (stripped[3:].strip() or "plain text").lower()
                code_lines = []
            else:
                flush_code()
                in_code = False
            continue

        if in_code:
            code_lines.append(line)
            continue

        if stripped in ("---", "***", "___"):
            blocks.append({"object": "block", "type": "divider", "divider": {}})
            continue

        if "<summary>" in stripped and "</summary>" in stripped:
            summary = re.sub(r".*<summary>(.*?)</summary>.*", r"\1", stripped)
            summary = re.sub(r"<[^>]+>", "", summary).strip()
            if summary:
                append_text_blocks(blocks, "heading_2", summary)
            continue
        if stripped.startswith("<details") or stripped.startswith("</details>"):
            continue

        if not stripped:
            blocks.append(text_block("paragraph", [text_object("\u200b")]))
            continue

        if stripped.startswith("### "):
            append_text_blocks(blocks, "heading_3", stripped[4:].strip())
            continue
        if stripped.startswith("## "):
            append_text_blocks(blocks, "heading_2", stripped[3:].strip())
            continue
        if stripped.startswith("# "):
            append_text_blocks(blocks, "heading_1", stripped[2:].strip())
            continue
        if stripped.startswith("> "):
            append_text_blocks(blocks, "quote", stripped[2:].strip())
            continue
        if stripped.startswith("- "):
            append_text_blocks(blocks, "bulleted_list_item", stripped[2:].strip())
            continue
        if re.match(r"^\d+\.\s+", stripped):
            content = re.sub(r"^\d+\.\s+", "", stripped, count=1)
            append_text_blocks(blocks, "numbered_list_item", content.strip())
            continue

        append_text_blocks(blocks, "paragraph", stripped)

    if in_code:
        flush_code()
    return blocks


def notion_headers(token: str) -> dict:
    return {
        "Authorization": f"Bearer {token}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


def notion_request(method: str, path: str, token: str,
                   payload: dict | None = None,
                   params: dict | None = None,
                   retries: int = 5) -> dict:
    url = f"{NOTION_API_BASE}{path}"
    headers = notion_headers(token)
    for attempt in range(1, retries + 1):
        resp = requests.request(method, url, headers=headers, json=payload, params=params, timeout=60)
        if resp.status_code == 429 and attempt < retries:
            retry_after = float(resp.headers.get("Retry-After", "1"))
            time.sleep(max(1.0, retry_after))
            continue
        if 500 <= resp.status_code < 600 and attempt < retries:
            time.sleep(1.0 * attempt)
            continue
        if resp.ok:
            if resp.text:
                return resp.json()
            return {}
        try:
            err = resp.json()
        except json.JSONDecodeError:
            err = {"message": resp.text}
        msg = err.get("message", "unknown error")
        code = err.get("code", "unknown_code")
        raise RuntimeError(f"Notion API 失败 ({resp.status_code}, {code}): {msg}")
    raise RuntimeError("Notion API 重试后仍失败")


def build_page_title(date_str: str, report_type: str, custom_title: str | None) -> str:
    if custom_title:
        return custom_title
    iso_date = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
    label = "早报" if report_type == "morning" else "晚报"
    return f"finradar {iso_date} {label}"


def resolve_report_path(date_str: str, report_type: str, file_arg: str | None) -> Path:
    if file_arg:
        return Path(file_arg).expanduser().resolve()
    return (OUTPUT_REPORT / f"daily_{date_str}_{report_type}.md").resolve()


def append_blocks_to_page(token: str, page_id: str, blocks: list[dict]) -> None:
    for i in range(0, len(blocks), 100):
        notion_request(
            "PATCH",
            f"/blocks/{page_id}/children",
            token,
            {"children": blocks[i:i + 100]},
        )


def create_subpage(token: str, parent_page_id: str, title: str, blocks: list[dict]) -> tuple[str, str]:
    first_batch = blocks[:100]
    payload = {
        "parent": {"page_id": parent_page_id},
        "properties": {
            "title": {
                "title": [
                    {"type": "text", "text": {"content": title[:200]}}
                ]
            }
        },
    }
    if first_batch:
        payload["children"] = first_batch

    page = notion_request("POST", "/pages", token, payload)
    page_id = page["id"]
    page_url = page.get("url", "")

    append_blocks_to_page(token, page_id, blocks[100:])
    return page_id, page_url


def list_child_pages(token: str, parent_page_id: str) -> list[dict]:
    """读取父页面下所有 child_page。"""
    pages: list[dict] = []
    next_cursor = None
    while True:
        query = {"page_size": 100}
        if next_cursor:
            query["start_cursor"] = next_cursor
        data = notion_request("GET", f"/blocks/{parent_page_id}/children", token, params=query)
        for item in data.get("results", []):
            if item.get("type") == "child_page":
                pages.append({
                    "id": item.get("id"),
                    "title": item.get("child_page", {}).get("title", ""),
                })
        if not data.get("has_more"):
            break
        next_cursor = data.get("next_cursor")
    return pages


def create_or_replace_subpage(token: str, parent_page_id: str, title: str, blocks: list[dict]) -> tuple[str, str, str]:
    """
    若同标题子页面已存在，则归档旧页面后重建，避免重复与旧格式残留。
    """
    mode = "created"
    for page in list_child_pages(token, parent_page_id):
        if str(page.get("title", "")).strip() == title.strip():
            notion_request("PATCH", f"/pages/{page['id']}", token, {"archived": True})
            mode = "replaced"
            break

    page_id, page_url = create_subpage(token, parent_page_id, title, blocks)
    return page_id, page_url, mode


def main() -> int:
    now_bj = now_beijing()
    parser = argparse.ArgumentParser(description="将 finradar 报告写入 Notion 子页面")
    parser.add_argument("--date", default=now_bj.strftime("%Y%m%d"), help="日期 YYYYMMDD")
    parser.add_argument("--type", choices=["morning", "evening", "auto"], default="auto", help="报告类型")
    parser.add_argument("--file", default=None, help="Markdown 文件路径（默认按日期+类型推导）")
    parser.add_argument("--title", default=None, help="Notion 子页面标题（可选）")
    parser.add_argument("--token", default=None, help="Notion API Token（可选，默认读环境变量）")
    parser.add_argument("--parent", default=None, help="Notion 父页面 ID 或 URL（可选，默认读环境变量）")
    args = parser.parse_args()

    report_type = resolve_report_type(args.type)
    date_str = args.date

    token = (
        args.token
        or os.environ.get("NOTION_API_TOKEN")
        or os.environ.get("NOTION_TOKEN")
        or ""
    ).strip()
    parent_raw = (
        args.parent
        or os.environ.get("NOTION_PARENT_PAGE_ID")
        or os.environ.get("NOTION_PARENT_PAGE_URL")
        or os.environ.get("NOTION_PARENT_PAGE")
        or ""
    ).strip()

    if not token:
        raise SystemExit("❌ 未提供 NOTION_API_TOKEN")
    if not parent_raw:
        raise SystemExit("❌ 未提供 NOTION_PARENT_PAGE_ID/URL")

    parent_page_id = extract_page_id(parent_raw)
    report_path = resolve_report_path(date_str, report_type, args.file)
    if not report_path.exists():
        raise SystemExit(f"❌ 报告文件不存在: {report_path}")

    notion_request("GET", f"/pages/{parent_page_id}", token)
    markdown_text = report_path.read_text(encoding="utf-8")
    blocks = markdown_to_notion_blocks(markdown_text)
    title = build_page_title(date_str, report_type, args.title)
    page_id, page_url, mode = create_or_replace_subpage(token, parent_page_id, title, blocks)

    print("✅ Notion 写入成功")
    print(f"   mode: {mode}")
    print(f"   标题: {title}")
    print(f"   page_id: {page_id}")
    if page_url:
        print(f"   url: {page_url}")
    print(f"   blocks: {len(blocks)}")
    print(f"   source: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
