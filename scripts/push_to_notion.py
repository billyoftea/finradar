#!/usr/bin/env python3
# coding=utf-8
"""
将 finradar Markdown 报告写入 Notion：
- 页面模式：写入父页面的子页面
- 数据库模式：写入 Notion Database 的一条页面记录（推荐）

用法示例:
  python scripts/push_to_notion.py --date 20260209 --type morning
  NOTION_API_TOKEN=... NOTION_PARENT_PAGE_ID=... python scripts/push_to_notion.py --type evening
  NOTION_API_TOKEN=... NOTION_DATABASE_ID=... python scripts/push_to_notion.py --type evening
"""

import argparse
import json
import os
import re
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urlsplit
from zoneinfo import ZoneInfo

import requests
from requests.utils import requote_uri

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_REPORT = PROJECT_ROOT / "output" / "report"
NOTION_API_BASE = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"
BEIJING_TZ = ZoneInfo("Asia/Shanghai")
INLINE_MD_PATTERN = re.compile(
    r"\[([^\]]+)\]\((https?://[^)\s]+)\)|\*\*([^*]+)\*\*|__([^_]+)__|`([^`]+)`|\*([^*]+)\*|_([^_]+)_|~~([^~]+)~~|(https?://[^\s<]+)"
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


def parse_bool(value: str | None, default: bool = False) -> bool:
    if value is None:
        return default
    text = str(value).strip().lower()
    if text in {"1", "true", "yes", "on", "y"}:
        return True
    if text in {"0", "false", "no", "off", "n"}:
        return False
    return default


def extract_notion_id(raw: str) -> str:
    if not raw:
        raise ValueError("Notion 页面/数据库 ID 不能为空")
    cleaned = re.sub(r"[^0-9a-fA-F]", "", raw)
    m = re.search(r"[0-9a-fA-F]{32}", cleaned)
    if not m:
        raise ValueError(f"无法从输入中解析 Notion id: {raw}")
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
    def normalize_notion_url(raw_url: str | None) -> str | None:
        url = str(raw_url or "").strip()
        if not url:
            return None
        try:
            url = requote_uri(url)
        except Exception:
            return None
        try:
            parsed = urlsplit(url)
        except Exception:
            return None
        if parsed.scheme not in ("http", "https") or not parsed.netloc:
            return None
        return url

    text_payload = {"content": content}
    if href:
        safe_url = normalize_notion_url(href)
        if safe_url:
            text_payload["link"] = {"url": safe_url}
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

    def split_url_trailing_punct(url: str) -> tuple[str, str]:
        trailing = ""
        while url and url[-1] in ".,;:!?)]}":
            trailing = url[-1] + trailing
            url = url[:-1]
        return url, trailing

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
        elif m.group(9) is not None:  # bare URL
            clean_url, trailing = split_url_trailing_punct(m.group(9))
            if clean_url:
                result.append(text_object(clean_url, href=clean_url))
            if trailing:
                result.append(text_object(trailing))

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


def build_page_title(date_str: str, report_type: str, custom_title: str | None, merge_daily: bool = False) -> str:
    if custom_title:
        return custom_title
    iso_date = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
    if merge_daily:
        return f"finradar {iso_date} 日报"
    label = "早报" if report_type == "morning" else "晚报"
    return f"finradar {iso_date} {label}"


def resolve_report_path(date_str: str, report_type: str, file_arg: str | None) -> Path:
    if file_arg:
        return Path(file_arg).expanduser().resolve()
    return (OUTPUT_REPORT / f"daily_{date_str}_{report_type}.md").resolve()


def load_markdown_content(
    date_str: str,
    report_type: str,
    file_arg: str | None,
    merge_daily: bool,
) -> tuple[str, str]:
    """读取要推送的 Markdown 文本，支持同日早晚合并。"""
    if file_arg:
        report_path = resolve_report_path(date_str, report_type, file_arg)
        if not report_path.exists():
            raise SystemExit(f"❌ 报告文件不存在: {report_path}")
        return report_path.read_text(encoding="utf-8"), str(report_path)

    if not merge_daily:
        report_path = resolve_report_path(date_str, report_type, None)
        if not report_path.exists():
            raise SystemExit(f"❌ 报告文件不存在: {report_path}")
        return report_path.read_text(encoding="utf-8"), str(report_path)

    morning_path = OUTPUT_REPORT / f"daily_{date_str}_morning.md"
    evening_path = OUTPUT_REPORT / f"daily_{date_str}_evening.md"
    morning_text = morning_path.read_text(encoding="utf-8") if morning_path.exists() else ""
    evening_text = evening_path.read_text(encoding="utf-8") if evening_path.exists() else ""

    if not morning_text and not evening_text:
        raise SystemExit(f"❌ 日报合并失败：未找到 {date_str} 的早/晚报文件")

    iso_date = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
    parts = [f"# 🧾 finradar {iso_date} 日报（时间线合并）\n"]
    parts.append(
        "> 说明：此页面按时间线合并同一天早报与晚报，便于连续阅读；原始链接索引仍保留在各分段内。\n"
    )
    parts.append("---\n")

    parts.append("## 🌅 早报\n")
    if morning_text:
        parts.append(morning_text.strip())
    else:
        parts.append("> 当日早报尚未生成。")
    parts.append("\n---\n")

    parts.append("## 🌇 晚报\n")
    if evening_text:
        parts.append(evening_text.strip())
    else:
        parts.append("> 当日晚报尚未生成。")
    parts.append("")

    source = f"merged:{morning_path if morning_path.exists() else 'missing'} + {evening_path if evening_path.exists() else 'missing'}"
    return "\n".join(parts), source


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


def get_database_title_property(token: str, database_id: str) -> str:
    """获取数据库中的 title 属性名。"""
    db = notion_request("GET", f"/databases/{database_id}", token)
    props = db.get("properties", {}) if isinstance(db, dict) else {}
    for prop_name, prop_meta in props.items():
        if isinstance(prop_meta, dict) and prop_meta.get("type") == "title":
            return prop_name
    raise RuntimeError("Notion 数据库未找到 title 属性")


def list_database_pages_by_title(token: str, database_id: str, title_property: str, title: str) -> list[dict]:
    """按标题查询数据库中同名页面。"""
    payload = {
        "page_size": 100,
        "filter": {
            "property": title_property,
            "title": {"equals": title},
        },
    }
    pages: list[dict] = []
    next_cursor = None
    while True:
        query = dict(payload)
        if next_cursor:
            query["start_cursor"] = next_cursor
        data = notion_request("POST", f"/databases/{database_id}/query", token, payload=query)
        pages.extend(data.get("results", []) if isinstance(data, dict) else [])
        if not isinstance(data, dict) or not data.get("has_more"):
            break
        next_cursor = data.get("next_cursor")
    return pages


def create_database_page(
    token: str,
    database_id: str,
    title_property: str,
    title: str,
    blocks: list[dict],
) -> tuple[str, str]:
    """在 Notion Database 中创建一条页面记录，并写入正文 blocks。"""
    first_batch = blocks[:100]
    payload = {
        "parent": {"database_id": database_id},
        "properties": {
            title_property: {
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


def create_or_replace_database_page(
    token: str,
    database_id: str,
    title: str,
    blocks: list[dict],
) -> tuple[str, str, str]:
    """
    数据库模式：若同标题记录存在，则归档旧记录后重建。
    """
    title_property = get_database_title_property(token, database_id)
    mode = "created"
    for row in list_database_pages_by_title(token, database_id, title_property, title):
        page_id = str(row.get("id", "")).strip()
        if not page_id:
            continue
        notion_request("PATCH", f"/pages/{page_id}", token, {"archived": True})
        mode = "replaced"
    new_page_id, new_page_url = create_database_page(token, database_id, title_property, title, blocks)
    return new_page_id, new_page_url, mode


def main() -> int:
    now_bj = now_beijing()
    parser = argparse.ArgumentParser(description="将 finradar 报告写入 Notion（子页面或数据库）")
    parser.add_argument("--date", default=now_bj.strftime("%Y%m%d"), help="日期 YYYYMMDD")
    parser.add_argument("--type", choices=["morning", "evening", "auto"], default="auto", help="报告类型")
    parser.add_argument("--file", default=None, help="Markdown 文件路径（默认按日期+类型推导）")
    parser.add_argument("--title", default=None, help="Notion 页面标题（可选）")
    parser.add_argument("--merge-daily", action="store_true", help="同一天早晚报合并后推送同一页面")
    parser.add_argument("--no-merge-daily", action="store_true", help="禁用同日早晚报合并")
    parser.add_argument("--token", default=None, help="Notion API Token（可选，默认读环境变量）")
    parser.add_argument("--parent", default=None, help="Notion 父页面 ID 或 URL（页面模式）")
    parser.add_argument("--database", default=None, help="Notion Database ID 或 URL（数据库模式，优先）")
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
    database_raw = (
        args.database
        or os.environ.get("NOTION_DATABASE_ID")
        or os.environ.get("NOTION_DATABASE")
        or ""
    ).strip()

    if not token:
        raise SystemExit("❌ 未提供 NOTION_API_TOKEN")
    if not parent_raw and not database_raw:
        raise SystemExit("❌ 未提供 NOTION_DATABASE_ID 或 NOTION_PARENT_PAGE_ID/URL")

    parent_page_id = extract_notion_id(parent_raw) if parent_raw else ""
    database_id = extract_notion_id(database_raw) if database_raw else ""
    # 默认早报/晚报分开推送到不同页面；只有显式开启时才合并
    merge_daily = parse_bool(os.environ.get("NOTION_MERGE_DAILY"), False)
    if args.merge_daily:
        merge_daily = True
    if args.no_merge_daily:
        merge_daily = False

    target_mode = "database" if database_id else "page"
    if target_mode == "database":
        notion_request("GET", f"/databases/{database_id}", token)
    else:
        notion_request("GET", f"/pages/{parent_page_id}", token)

    markdown_text, source_label = load_markdown_content(
        date_str=date_str,
        report_type=report_type,
        file_arg=args.file,
        merge_daily=merge_daily,
    )
    blocks = markdown_to_notion_blocks(markdown_text)
    title = build_page_title(date_str, report_type, args.title, merge_daily=merge_daily)
    if target_mode == "database":
        page_id, page_url, mode = create_or_replace_database_page(token, database_id, title, blocks)
    else:
        page_id, page_url, mode = create_or_replace_subpage(token, parent_page_id, title, blocks)

    print("✅ Notion 写入成功")
    print(f"   target: {target_mode}")
    print(f"   mode: {mode}")
    print(f"   标题: {title}")
    print(f"   page_id: {page_id}")
    if page_url:
        print(f"   url: {page_url}")
    print(f"   blocks: {len(blocks)}")
    print(f"   source: {source_label}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
