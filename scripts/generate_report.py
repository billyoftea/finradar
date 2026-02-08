#!/usr/bin/env python3
# coding=utf-8
"""
FinRadar 每日综合报告生成器

汇总市场数据、Twitter、微信公众号、NewsNow热榜，
调用 DeepSeek API 生成 AI 分析摘要，输出为 Markdown 格式。

用法:
    python scripts/generate_report.py                    # 今天
    python scripts/generate_report.py --date 20260207    # 指定日期
    python scripts/generate_report.py --type morning     # 只生成早报
    python scripts/generate_report.py --type evening     # 只生成晚报
"""

import argparse
import json
import os
import sqlite3
import sys
import logging
from datetime import datetime
from pathlib import Path

import requests
import yaml

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# ── 路径 ──────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_FILE = PROJECT_ROOT / "config" / "config.yaml"
OUTPUT_MARKET = PROJECT_ROOT / "output" / "market"
OUTPUT_NEWS = PROJECT_ROOT / "output" / "news"
OUTPUT_REPORT = PROJECT_ROOT / "output" / "report"


# ══════════════════════════════════════════════════════
#  1. 数据读取
# ══════════════════════════════════════════════════════

def load_config():
    """读取 config.yaml"""
    with open(CONFIG_FILE, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_market_data(date_str: str) -> dict:
    """读取最新市场数据 (每30分钟更新的那个)"""
    path = OUTPUT_MARKET / f"market_data_{date_str}.json"
    if path.exists():
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return {}


def load_social_data(date_str: str, report_type: str = None) -> dict:
    """
    读取社交媒体数据 (早报/晚报)
    report_type: "morning" / "evening" / None(自动选最新)
    """
    if report_type:
        path = OUTPUT_MARKET / f"market_data_{date_str}_{report_type}.json"
        if path.exists():
            with open(path, encoding="utf-8") as f:
                return json.load(f)
    
    # 自动选最大的 social 文件
    candidates = sorted(OUTPUT_MARKET.glob(f"market_data_{date_str}_*.json"), key=lambda p: p.stat().st_size, reverse=True)
    for c in candidates:
        with open(c, encoding="utf-8") as f:
            d = json.load(f)
        if d.get("mode") == "social":
            return d
    return {}


def is_weekend(date_str: str) -> tuple:
    """检测是否为周末及休市情况
    
    Returns:
        (is_weekend: bool, market_status: str)
        market_status 可能是: '正常交易', 'A股休市', '全市场休市'
    """
    iso_date = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
    dt = datetime.strptime(iso_date, "%Y-%m-%d")
    weekday = dt.weekday()  # 0=周一, 6=周日
    
    if weekday >= 5:  # 周六(5)或周日(6)
        return True, 'A股休市'
    return False, '正常交易'


def load_news_data(date_str: str) -> list:
    """读取 NewsNow 热榜数据"""
    iso_date = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
    db_path = OUTPUT_NEWS / f"{iso_date}.db"
    if not db_path.exists():
        return []
    
    conn = sqlite3.connect(str(db_path))
    rows = conn.execute("""
        SELECT n.title, p.name as platform, n.rank, n.url, n.first_crawl_time, n.last_crawl_time
        FROM news_items n
        JOIN platforms p ON n.platform_id = p.id
        WHERE n.rank <= 15
        ORDER BY n.last_crawl_time DESC, n.rank ASC
    """).fetchall()
    conn.close()
    
    # 去重（同标题可能多个平台）
    seen = set()
    result = []
    for title, platform, rank, url, first_time, last_time in rows:
        if title not in seen:
            seen.add(title)
            result.append({
                "title": title,
                "platform": platform,
                "rank": rank,
                "url": url,
                "first_time": first_time,
                "last_time": last_time,
            })
    return result[:100]  # 最多100条


# ══════════════════════════════════════════════════════
#  2. 数据格式化（给 AI 的全量版）
# ══════════════════════════════════════════════════════

def format_market_for_ai(market: dict) -> str:
    """格式化市场数据给 AI 分析（含板块指数）"""
    data = market.get("data", {})
    lines = []
    
    # A股主要指数
    stock = data.get("stock_cn", {})
    if stock and stock.get("indices"):
        lines.append("【A股主要指数】")
        for idx in stock["indices"]:
            if isinstance(idx, dict):
                lines.append(f"  {idx.get('name','')}: {idx.get('price',0):.2f} ({idx.get('change_pct',0):+.2f}%)")
    
    # A股板块指数
    sectors = stock.get("sectors", []) if stock else []
    if sectors:
        # 按涨跌幅排序
        sorted_sectors = sorted(
            [s for s in sectors if isinstance(s, dict) and s.get("change_pct") is not None],
            key=lambda x: x.get("change_pct", 0),
            reverse=True
        )
        if sorted_sectors:
            lines.append("【A股板块涨幅前15】")
            for s in sorted_sectors[:15]:
                leader = f" (领涨: {s['leading_stock']})" if s.get("leading_stock") else ""
                lines.append(f"  {s.get('name','')}: {s.get('change_pct',0):+.2f}%{leader}")
            lines.append("【A股板块跌幅前15】")
            for s in sorted_sectors[-15:]:
                leader = f" (领跌: {s['leading_stock']})" if s.get("leading_stock") else ""
                lines.append(f"  {s.get('name','')}: {s.get('change_pct',0):+.2f}%{leader}")
    
    # 北向资金
    north = stock.get("north_flow", {}) if stock else {}
    if north:
        lines.append("【北向资金】")
        for k, v in north.items():
            if isinstance(v, (int, float)):
                lines.append(f"  {k}: {v:.2f}亿")
    
    # 市场统计
    mstats = stock.get("market_stats", {}) if stock else {}
    if mstats:
        lines.append("【市场统计】")
        for k, v in mstats.items():
            lines.append(f"  {k}: {v}")
    
    # 贵金属
    pm = data.get("precious_metal", {})
    if pm and pm.get("metals"):
        lines.append("【贵金属】")
        for metal in pm["metals"]:
            if isinstance(metal, dict):
                lines.append(f"  {metal.get('name','')}: ${metal.get('price',0):.2f} ({metal.get('change_pct',0):+.2f}%)")
    
    # 加密货币
    crypto = data.get("crypto", {})
    if crypto and crypto.get("coins"):
        lines.append("【加密货币】")
        for coin in crypto["coins"]:
            if isinstance(coin, dict):
                lines.append(f"  {coin.get('symbol','').upper()}: ${coin.get('price',0):,.2f} ({coin.get('change_24h',0):+.2f}%)")
    
    # 期货
    futures = data.get("futures", {})
    if futures:
        cat_names = {"commodity": "国内商品期货", "index_futures": "股指期货", "international": "国际期货"}
        for cat_key, cat_name in cat_names.items():
            items = futures.get(cat_key, [])
            if items:
                lines.append(f"【{cat_name}】")
                for item in items:
                    if isinstance(item, dict):
                        lines.append(f"  {item.get('name','')}: {item.get('price',0)} ({item.get('change_pct',0):+.2f}%)")
    
    return "\n".join(lines) if lines else "暂无市场数据"


def format_twitter_for_ai(social: dict) -> str:
    """格式化 Twitter 推文给 AI 分析（全量）"""
    tweets = social.get("data", {}).get("twitter", {}).get("tweets", [])
    if not tweets:
        return "暂无 Twitter 数据"
    
    lines = [f"共 {len(tweets)} 条推文，全部内容如下："]
    for t in tweets:
        username = t.get("username", "")
        text = t.get("text", "").replace("\n", " ")
        created = t.get("created_at", "")[:16]
        lines.append(f"  @{username} [{created}]: {text}")
    
    return "\n".join(lines)


def format_wechat_for_ai(social: dict) -> str:
    """格式化微信公众号文章给 AI 分析（全量含正文）"""
    articles = social.get("data", {}).get("wechat", {}).get("articles", [])
    if not articles:
        return "暂无微信公众号文章"
    
    lines = [f"共 {len(articles)} 篇公众号文章，全部内容如下："]
    for a in articles:
        account = a.get("account_name", "")
        title = a.get("title", "")
        digest = a.get("digest", "")
        content = a.get("content", "") or ""
        read_count = a.get("read_count", 0)
        like_count = a.get("like_count", 0)
        
        # 优先使用digest（摘要），如果没有则使用正文前1000字
        if digest:
            article_summary = digest
        else:
            # 清理HTML标签，提取纯文本
            import re
            content_text = re.sub(r'<[^>]+>', ' ', content)
            article_summary = content_text[:1000].replace('\n', ' ')
        
        lines.append(f"\n  【{account}】{title}")
        if article_summary:
            lines.append(f"  摘要: {article_summary}")
        if read_count or like_count:
            lines.append(f"  阅读: {read_count} | 点赞: {like_count}")
    
    return "\n".join(lines)


def format_news_for_ai(news: list) -> str:
    """格式化 NewsNow 热榜给 AI 分析（全量）"""
    if not news:
        return "暂无热榜数据"
    
    lines = [f"共 {len(news)} 条热榜新闻，全部内容如下："]
    for n in news:
        lines.append(f"  [{n['platform']}] #{n['rank']} {n['title']}")
    
    return "\n".join(lines)


# ══════════════════════════════════════════════════════
#  3. DeepSeek AI 分析（分批调用）
# ══════════════════════════════════════════════════════

def call_deepseek(system_prompt: str, user_prompt: str, api_key: str,
                  max_tokens: int = 4000, temperature: float = 0.7) -> str:
    """调用 DeepSeek API"""
    url = "https://api.deepseek.com/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "max_tokens": max_tokens,
        "temperature": temperature,
    }
    
    logger.info(f"📤 DeepSeek API (prompt: {len(user_prompt)} 字符)...")
    
    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=180)
        resp.raise_for_status()
        result = resp.json()
        content = result["choices"][0]["message"]["content"]
        usage = result.get("usage", {})
        logger.info(f"✅ 完成 (prompt_tokens={usage.get('prompt_tokens',0)}, completion_tokens={usage.get('completion_tokens',0)})")
        return content
    except requests.exceptions.HTTPError as e:
        logger.error(f"❌ DeepSeek API 错误: {e}")
        try:
            logger.error(f"   响应: {resp.text[:500]}")
        except Exception:
            pass
        return f"AI 分析失败: {e}"
    except Exception as e:
        logger.error(f"❌ DeepSeek API 调用异常: {e}")
        return f"AI 分析失败: {e}"


def run_ai_analysis(market: dict, social: dict, news: list,
                    api_key: str, iso_date: str, report_label: str, time_range: str) -> str:
    """
    分批调用 DeepSeek，每个数据源独立分析，最后综合汇总。
    
    步骤:
      1. 市场+板块数据 → 市场分析
      2. Twitter 全量  → 推文分析
      3. 微信全量      → 公众号分析
      4. 热榜全量      → 热榜分析
      5. 汇总以上4份分析 → 最终综合报告
    """
    date_context = f"{iso_date} {report_label}（覆盖时段: {time_range}）"
    section_summaries = {}
    
    # ─── 第1步: 市场数据分析 ────────────────────────
    logger.info("🔍 [1/5] 分析市场数据...")
    market_text = format_market_for_ai(market)
    if market_text != "暂无市场数据":
        summary = call_deepseek(
            system_prompt=(
                "你是资深金融市场分析师。请对以下市场数据进行专业分析，包括：\n"
                "1. 主要指数走势判断\n"
                "2. 板块轮动分析：哪些板块在领涨/领跌，反映什么资金偏好\n"
                "3. 加密货币和商品期货的关键变化\n"
                "4. 北向资金流向暗示\n\n"
                "用中文，Markdown格式，重要数据**加粗**，500-800字。"
            ),
            user_prompt=f"以下是 {date_context} 的金融市场数据：\n\n{market_text}",
            api_key=api_key,
            max_tokens=2000
        )
        section_summaries["market"] = summary
    
    # ─── 第2步: Twitter 分析 ────────────────────────
    logger.info("🔍 [2/5] 分析 Twitter 推文...")
    twitter_text = format_twitter_for_ai(social)
    if twitter_text != "暂无 Twitter 数据":
        summary = call_deepseek(
            system_prompt=(
                "你是资深金融科技分析师。请对以下 Twitter 推文进行分析总结，提取：\n"
                "1. 最重要的5-8条信息/事件\n"
                "2. 市场情绪判断（恐慌/乐观/中性）\n"
                "3. 值得关注的交易信号或行业动向\n"
                "4. 地缘政治相关推文要点\n\n"
                "注意：按重要性排序，忽略广告和无关内容。\n"
                "用中文，Markdown格式，重要信息**加粗**，500-800字。"
            ),
            user_prompt=f"以下是 {date_context} 收集的 Twitter 推文：\n\n{twitter_text}",
            api_key=api_key,
            max_tokens=2000
        )
        section_summaries["twitter"] = summary
    
    # ─── 第3步: 微信公众号分析 ────────────────────────
    logger.info("🔍 [3/5] 分析微信公众号文章...")
    wechat_text = format_wechat_for_ai(social)
    if wechat_text != "暂无微信公众号文章":
        summary = call_deepseek(
            system_prompt=(
                "你是资深财经媒体分析师。请对以下微信公众号文章进行深度分析：\n\n"
                "第一部分：重要文章详细摘要（请为每篇重要文章生成100-200字的详细摘要。判断标准如下）：\n"
                "1. **深度分析类**：原文有深度思考、独特见解、数据支撑的研究型文章\n"
                "2. **政策解读类**：涉及重要政策、监管、法规的权威解读\n"
                "3. **行业趋势类**：预测未来趋势、产业变革的前瞻性分析\n"
                "4. **重要公司动态**：上市公司重大事件、业绩预告、并购重组\n"
                "5. **用户可能感兴趣**：与投资者关注领域（AI、芯片、新能源、金融等）相关的高质量内容\n\n"
                "第二部分：整体分析总结\n"
                "1. 核心观点汇总\n"
                "2. 政策监管动向\n"
                "3. 行业投资机会和风险提示\n"
                "4. 与市场走势相关的关键信息\n\n"
                "注意：合并重复报道，按重要性排序。\n"
                "用中文，Markdown格式，重要信息**加粗**，800-1200字。"
            ),
            user_prompt=f"以下是 {date_context} 收集的微信公众号文章：\n\n{wechat_text}",
            api_key=api_key,
            max_tokens=3000
        )
        section_summaries["wechat"] = summary
    
    # ─── 第4步: 热榜分析 ────────────────────────
    logger.info("🔍 [4/5] 分析热榜新闻...")
    news_text = format_news_for_ai(news)
    if news_text != "暂无热榜数据":
        summary = call_deepseek(
            system_prompt=(
                "你是资深新闻分析师。请对以下各平台热榜进行分析，提取：\n"
                "1. 跨平台共同关注的3-5个热点事件\n"
                "2. 与金融市场相关的重要新闻\n"
                "3. 科技/AI 相关热点\n"
                "4. 社会舆论焦点\n\n"
                "用中文，Markdown格式，300-500字。"
            ),
            user_prompt=f"以下是 {date_context} 各平台热榜新闻：\n\n{news_text}",
            api_key=api_key,
            max_tokens=1500
        )
        section_summaries["news"] = summary
    
    # ─── 第5步: 综合汇总 ────────────────────────
    logger.info("🔍 [5/5] 生成综合分析报告...")
    
    # 检查是否为周末
    is_weekend_flag, market_status = is_weekend(date_str)
    weekend_note = "【注意：今日为周末，A股休市，部分市场数据可能缺失】" if is_weekend_flag else ""
    
    synthesis_input = f"以下是 {date_context} 各数据源的分析结果，请进行最终综合汇总：{weekend_note}\n\n"
    
    if "market" in section_summaries:
        synthesis_input += f"## 市场数据分析\n{section_summaries['market']}\n\n"
    if "twitter" in section_summaries:
        synthesis_input += f"## Twitter 推文分析\n{section_summaries['twitter']}\n\n"
    if "wechat" in section_summaries:
        synthesis_input += f"## 微信公众号分析\n{section_summaries['wechat']}\n\n"
    if "news" in section_summaries:
        synthesis_input += f"## 热榜新闻分析\n{section_summaries['news']}\n\n"
    
    final_summary = call_deepseek(
        system_prompt=(
            "你是资深金融市场首席分析师，正在编写今日市场综合研报。\n"
            "用户会提供来自市场数据、Twitter、微信公众号、新闻热榜的分析结果。\n"
            "请将它们融合为一份结构清晰的综合报告，包括：\n\n"
            "## 📊 市场总览\n"
            "综合A股（含板块轮动）、加密货币、贵金属、期货的走势判断\n\n"
            "## 🔥 热点事件\n"
            "当天最重要的3-5个事件，结合多个信息源交叉验证\n\n"
            "## 🤖 科技动态\n"
            "AI、科技行业重要进展\n\n"
            "## 🌍 地缘政治\n"
            "影响市场的国际事件\n\n"
            "## � 重要微信文章\n"
            "从微信公众号分析中提取最重要、最值得关注的3-5篇文章，包括原文标题、公众号、简要分析（100字内）和推荐理由\n\n"
            "## 💡 投资启示\n"
            "基于以上信息的前瞻性投资建议\n\n"
            "要求：\n"
            "- 用中文，语言精炼专业\n"
            "- Markdown 格式，每个版块用 ## 标题\n"
            "- 重要数据用 **加粗**，关键判断要明确\n"
            "- 去除重复信息，交叉引用不同来源\n"
            "- 总字数 1500-3000 字"
        ),
        user_prompt=synthesis_input,
        api_key=api_key,
        max_tokens=6000,
        temperature=0.5
    )
    
    # 组装完整 AI 分析输出
    result_parts = [final_summary]
    
    # 附上各板块详细分析（折叠展示）
    result_parts.append("\n\n---\n")
    result_parts.append("<details><summary>📑 点击展开各板块详细分析</summary>\n")
    
    if "market" in section_summaries:
        result_parts.append(f"### 📊 市场数据详细分析\n\n{section_summaries['market']}\n")
    if "twitter" in section_summaries:
        result_parts.append(f"### 🐦 Twitter 详细分析\n\n{section_summaries['twitter']}\n")
    if "wechat" in section_summaries:
        result_parts.append(f"### 📱 微信公众号详细分析\n\n{section_summaries['wechat']}\n")
    if "news" in section_summaries:
        result_parts.append(f"### 📰 热榜详细分析\n\n{section_summaries['news']}\n")
    
    result_parts.append("</details>\n")
    
    return "\n".join(result_parts)


# ══════════════════════════════════════════════════════
#  4. Markdown 报告生成
# ══════════════════════════════════════════════════════

def generate_raw_market_section(market: dict) -> str:
    """生成市场数据原文 Markdown（含板块指数）"""
    data = market.get("data", {})
    lines = ["## 📊 金融市场数据\n"]
    
    # A股主要指数
    stock = data.get("stock_cn", {})
    if stock and stock.get("indices"):
        lines.append("### 🇨🇳 A股主要指数\n")
        lines.append("| 指数 | 价格 | 涨跌幅 |")
        lines.append("|------|------|--------|")
        for idx in stock["indices"]:
            if isinstance(idx, dict):
                icon = "🟢" if idx.get("change_pct", 0) >= 0 else "🔴"
                lines.append(f"| {idx.get('name','')} | {idx.get('price',0):.2f} | {icon} {idx.get('change_pct',0):+.2f}% |")
        lines.append("")
    
    # A股板块指数
    sectors = stock.get("sectors", []) if stock else []
    if sectors:
        sorted_sectors = sorted(
            [s for s in sectors if isinstance(s, dict) and s.get("change_pct") is not None],
            key=lambda x: x.get("change_pct", 0),
            reverse=True
        )
        if sorted_sectors:
            lines.append("### 📈 A股板块涨幅 TOP 15\n")
            lines.append("| 板块 | 涨跌幅 | 换手率 | 领涨股 |")
            lines.append("|------|--------|--------|--------|")
            for s in sorted_sectors[:15]:
                icon = "🟢" if s.get("change_pct", 0) >= 0 else "🔴"
                turnover = f"{s.get('turnover', 0):.2f}%" if s.get('turnover') else "-"
                lines.append(f"| {s.get('name','')} | {icon} {s.get('change_pct',0):+.2f}% | {turnover} | {s.get('leading_stock','')} |")
            lines.append("")
            
            lines.append("### 📉 A股板块跌幅 TOP 15\n")
            lines.append("| 板块 | 涨跌幅 | 换手率 | 领跌股 |")
            lines.append("|------|--------|--------|--------|")
            for s in sorted_sectors[-15:]:
                icon = "🟢" if s.get("change_pct", 0) >= 0 else "🔴"
                turnover = f"{s.get('turnover', 0):.2f}%" if s.get('turnover') else "-"
                lines.append(f"| {s.get('name','')} | {icon} {s.get('change_pct',0):+.2f}% | {turnover} | {s.get('leading_stock','')} |")
            lines.append("")
    
    # 北向资金
    north = stock.get("north_flow", {}) if stock else {}
    if north:
        lines.append("### 💰 北向资金\n")
        lines.append("| 项目 | 金额(亿元) |")
        lines.append("|------|------------|")
        for k, v in north.items():
            if isinstance(v, (int, float)):
                icon = "🟢" if v >= 0 else "🔴"
                lines.append(f"| {k} | {icon} {v:.2f} |")
        lines.append("")
    
    # 贵金属
    pm = data.get("precious_metal", {})
    if pm and pm.get("metals"):
        lines.append("### 🥇 贵金属\n")
        lines.append("| 品种 | 价格 | 涨跌幅 |")
        lines.append("|------|------|--------|")
        for metal in pm["metals"]:
            if isinstance(metal, dict):
                icon = "🟢" if metal.get("change_pct", 0) >= 0 else "🔴"
                lines.append(f"| {metal.get('name','')} | ${metal.get('price',0):.2f} | {icon} {metal.get('change_pct',0):+.2f}% |")
        lines.append("")
    
    # 加密货币
    crypto = data.get("crypto", {})
    if crypto and crypto.get("coins"):
        lines.append("### ₿ 加密货币\n")
        lines.append("| 币种 | 价格 | 24h涨跌 |")
        lines.append("|------|------|---------|")
        for coin in crypto["coins"]:
            if isinstance(coin, dict):
                icon = "🟢" if coin.get("change_24h", 0) >= 0 else "🔴"
                lines.append(f"| {coin.get('symbol','').upper()} | ${coin.get('price',0):,.2f} | {icon} {coin.get('change_24h',0):+.2f}% |")
        lines.append("")
    
    # 期货
    futures = data.get("futures", {})
    if futures:
        cat_names = {"commodity": "商品期货", "index_futures": "股指期货", "international": "国际期货"}
        for cat_key, cat_name in cat_names.items():
            items = futures.get(cat_key, [])
            if items:
                lines.append(f"### 📈 {cat_name}\n")
                lines.append("| 品种 | 价格 | 涨跌幅 |")
                lines.append("|------|------|--------|")
                for item in items[:10]:
                    if isinstance(item, dict):
                        icon = "🟢" if item.get("change_pct", 0) >= 0 else "🔴"
                        lines.append(f"| {item.get('name','')} | {item.get('price','')} | {icon} {item.get('change_pct',0):+.2f}% |")
                lines.append("")
    
    # GitHub
    github = data.get("github", {})
    if github and github.get("trending"):
        lines.append("### 💻 GitHub 趋势\n")
        for repo in github["trending"][:5]:
            if isinstance(repo, dict):
                lines.append(f"- ⭐ **{repo.get('name','')}** ({repo.get('stars',0)} stars)")
                desc = repo.get("description", "")[:80]
                if desc:
                    lines.append(f"  - {desc}")
        lines.append("")
    
    return "\n".join(lines)


def generate_raw_twitter_section(social: dict) -> str:
    """生成 Twitter 原文 Markdown"""
    tweets = social.get("data", {}).get("twitter", {}).get("tweets", [])
    if not tweets:
        return "## 🐦 Twitter 热点\n\n暂无数据\n"
    
    lines = [f"## 🐦 Twitter 热点 ({len(tweets)} 条)\n"]
    
    # 按账号分组
    by_user = {}
    for t in tweets:
        u = t.get("username", "unknown")
        by_user.setdefault(u, []).append(t)
    
    for username, user_tweets in by_user.items():
        lines.append(f"### @{username} ({len(user_tweets)} 条)\n")
        for t in user_tweets[:5]:  # 每个账号最多5条
            text = t.get("text", "")[:300].replace("\n", " ").replace("|", "\\|")
            created = t.get("created_at", "")[:16]
            url = t.get("url", "")
            lines.append(f"- `{created}` {text}")
            if url:
                lines.append(f"  - [原文链接]({url})")
        if len(user_tweets) > 5:
            lines.append(f"- *... 及其他 {len(user_tweets) - 5} 条*")
        lines.append("")
    
    return "\n".join(lines)


def generate_raw_wechat_section(social: dict) -> str:
    """生成微信公众号原文 Markdown"""
    articles = social.get("data", {}).get("wechat", {}).get("articles", [])
    if not articles:
        return "## 📱 微信公众号\n\n暂无数据\n"
    
    lines = [f"## 📱 微信公众号 ({len(articles)} 篇)\n"]
    
    for a in articles:
        title = a.get("title", "")
        account = a.get("account_name", "")
        url = a.get("url", "")
        digest = a.get("digest", "")[:150]
        pub_time = a.get("publish_time", "")[:16]
        
        if url:
            lines.append(f"### [{title}]({url})")
        else:
            lines.append(f"### {title}")
        lines.append(f"**{account}** | {pub_time}\n")
        if digest:
            lines.append(f"> {digest}\n")
    
    return "\n".join(lines)


def generate_raw_news_section(news: list) -> str:
    """生成 NewsNow 热榜原文 Markdown"""
    if not news:
        return "## 🔥 NewsNow 热榜\n\n暂无数据\n"
    
    lines = [f"## 🔥 NewsNow 热榜 ({len(news)} 条)\n"]
    
    # 按平台分组
    by_platform = {}
    for n in news:
        p = n["platform"]
        by_platform.setdefault(p, []).append(n)
    
    for platform, items in by_platform.items():
        lines.append(f"### {platform}\n")
        lines.append("| 排名 | 标题 |")
        lines.append("|------|------|")
        for item in items[:10]:
            title = item["title"].replace("|", "\\|")
            url = item.get("url", "")
            if url:
                lines.append(f"| #{item['rank']} | [{title}]({url}) |")
            else:
                lines.append(f"| #{item['rank']} | {title} |")
        lines.append("")
    
    return "\n".join(lines)


# ══════════════════════════════════════════════════════
#  5. 主流程
# ══════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="FinRadar 每日综合报告")
    parser.add_argument("--date", default=datetime.now().strftime("%Y%m%d"),
                        help="日期 YYYYMMDD (默认今天)")
    parser.add_argument("--type", choices=["morning", "evening", "auto"], default="auto",
                        help="报告类型: morning/evening/auto")
    parser.add_argument("--api-key", default=None,
                        help="DeepSeek API Key (也可通过环境变量 DEEPSEEK_API_KEY)")
    parser.add_argument("--no-ai", action="store_true",
                        help="跳过 AI 分析，只汇总原始数据")
    parser.add_argument("--output", default=None,
                        help="输出文件路径 (默认 output/report/daily_YYYYMMDD.md)")
    args = parser.parse_args()
    
    date_str = args.date
    iso_date = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
    
    # 获取 API Key
    api_key = args.api_key or os.environ.get("DEEPSEEK_API_KEY", "")
    if not api_key:
        cfg = load_config()
        api_key = cfg.get("ai", {}).get("api_key", "")
    
    # ── 判断早报/晚报 ──────────────────────────────
    if args.type == "auto":
        hour = datetime.now().hour
        if 5 <= hour < 12:
            report_type = "morning"
        elif 17 <= hour < 24:
            report_type = "evening"
        else:
            report_type = "morning" if hour < 5 else "evening"
    else:
        report_type = args.type
    
    report_label = "🌅 早报" if report_type == "morning" else "🌇 晚报"
    time_range = "昨日19:00 → 今日07:00" if report_type == "morning" else "今日07:00 → 19:00"
    
    logger.info(f"📅 生成 {iso_date} {report_label}")
    
    # ── 读取数据 ──────────────────────────────────
    logger.info("📥 读取市场数据...")
    market = load_market_data(date_str)
    
    logger.info(f"📥 读取社交媒体数据 ({report_type})...")
    social = load_social_data(date_str, report_type)
    
    logger.info("📥 读取热榜数据...")
    news = load_news_data(date_str)
    
    logger.info(f"   市场: {'✅' if market else '❌'}")
    logger.info(f"   社交: {'✅' if social else '❌'} (mode={social.get('mode','N/A')}, type={social.get('report_type','N/A')})")
    logger.info(f"   热榜: {'✅' if news else '❌'} ({len(news)} 条)")
    
    # ── AI 分析 ──────────────────────────────────
    ai_summary = ""
    if not args.no_ai:
        if not api_key:
            logger.warning("⚠️ 未配置 DeepSeek API Key，跳过 AI 分析")
            ai_summary = "> ⚠️ AI 分析未启用（未配置 API Key）\n"
        else:
            ai_summary = run_ai_analysis(
                market=market,
                social=social,
                news=news,
                api_key=api_key,
                iso_date=iso_date,
                report_label=report_label,
                time_range=time_range
            )
    
    # ── 生成完整 Markdown ──────────────────────
    report_parts = []
    
    # 检查休市状态
    is_weekend_flag, market_status = is_weekend(date_str)
    market_status_badge = "⚠️ A股休市" if is_weekend_flag else "✅ 正常交易"
    
    # 标题
    report_parts.append(f"# 📰 FinRadar {report_label}")
    report_parts.append(f"**{iso_date}** | {report_label} | 覆盖时段: {time_range} | 市场状态: {market_status_badge}")
    report_parts.append(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    if is_weekend_flag:
        report_parts.append(f"**⚠️ 注意：今日为周末，A股休市，部分市场数据可能缺失或未更新**\n")
    report_parts.append("---\n")
    
    # AI 分析摘要
    report_parts.append("# 🤖 AI 分析摘要\n")
    report_parts.append(ai_summary)
    report_parts.append("\n---\n")
    
    # 原始数据
    report_parts.append("# 📋 原始数据\n")
    report_parts.append(generate_raw_market_section(market))
    report_parts.append(generate_raw_twitter_section(social))
    report_parts.append(generate_raw_wechat_section(social))
    report_parts.append(generate_raw_news_section(news))
    
    # 页脚
    report_parts.append("---\n")
    report_parts.append(f"*报告由 FinRadar 自动生成 | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n")
    
    full_report = "\n".join(report_parts)
    
    # ── 保存 ──────────────────────────────────
    OUTPUT_REPORT.mkdir(parents=True, exist_ok=True)
    
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = OUTPUT_REPORT / f"daily_{date_str}_{report_type}.md"
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_report)
    
    logger.info(f"✅ 报告已保存: {output_path}")
    logger.info(f"   文件大小: {output_path.stat().st_size / 1024:.1f} KB")
    
    return str(output_path)


if __name__ == "__main__":
    main()
