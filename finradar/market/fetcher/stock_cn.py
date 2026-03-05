"""
A股市场数据抓取器

基于 AkShare 开源库实现
GitHub: https://github.com/akfamily/akshare
文档: https://akshare.akfamily.xyz/

AkShare 功能概览:
- 股票指数数据: ak.stock_zh_index_daily()
- 北向资金: ak.stock_em_hsgt_north_net_flow_in()
- 板块数据: ak.stock_board_industry_name_em()
- 概念板块: ak.stock_board_concept_name_em()
- 涨跌统计: ak.stock_changes_em()

安装: pip install akshare>=1.12.0
"""

import asyncio
from datetime import datetime, date
from typing import List, Dict, Any, Optional
import logging

try:
    import akshare as ak
    AKSHARE_AVAILABLE = True
except ImportError:
    AKSHARE_AVAILABLE = False
    ak = None

from . import BaseFetcher
from ..models.market_data import IndexData, SectorData, MarketOverview

logger = logging.getLogger(__name__)


class StockCNFetcher(BaseFetcher):
    """
    A股数据抓取器
    
    基于 AkShare 实现，支持获取:
    - 主要指数数据（上证、沪深300、创业板等）
    - 北向资金流向
    - 行业板块涨跌
    - 概念板块涨跌
    - 涨跌家数统计
    """
    
    # 主要指数代码映射
    INDEX_MAPPING = {
        "上证指数": {"code": "000001", "market": "sh"},
        "深证成指": {"code": "399001", "market": "sz"},
        "沪深300": {"code": "000300", "market": "sh"},
        "创业板指": {"code": "399006", "market": "sz"},
        "科创50": {"code": "000688", "market": "sh"},
        "中证500": {"code": "000905", "market": "sh"},
    }
    
    # 重点关注板块分类（默认配置）
    DEFAULT_FOCUS_SECTORS = {
        "tech": ["电子", "计算机", "通信"],
        "cyclical": ["有色金属", "钢铁", "煤炭", "化工"],
        "agriculture": ["农林牧渔"],
        "consumption": ["食品饮料", "家用电器", "汽车"],
        "finance": ["银行", "非银金融", "房地产"],
    }
    
    def __init__(self, config: Optional[Dict] = None):
        super().__init__(config)
        
        if not AKSHARE_AVAILABLE:
            logger.warning("akshare not installed. Run: pip install akshare")
            self.enabled = False
        
        # 合并默认配置和用户配置
        self.focus_sectors = self.config.get("focus_sectors", self.DEFAULT_FOCUS_SECTORS)
        self._trade_day_cache: Dict[str, bool] = {}
    
    async def fetch(self) -> Dict[str, Any]:
        """
        抓取所有A股相关数据
        
        Returns:
            包含指数、板块、资金流向等数据的字典
        """
        now = datetime.now()
        if not self._is_trading_day(now.date()):
            logger.info("📅 今日A股休市，跳过A股行情抓取")
            return {
                "indices": [],
                "north_flow": {},
                "sectors": [],
                "market_stats": {},
                "market_closed": True,
                "market_status": "A股休市",
                "timestamp": now,
            }

        # 使用线程池执行同步的 akshare 调用
        loop = asyncio.get_event_loop()
        
        # 并行获取各类数据
        indices_task = loop.run_in_executor(None, self._fetch_indices)
        north_flow_task = loop.run_in_executor(None, self._fetch_north_flow)
        sectors_task = loop.run_in_executor(None, self._fetch_sectors)
        market_stats_task = loop.run_in_executor(None, self._fetch_market_stats)
        
        indices, north_flow, sectors, market_stats = await asyncio.gather(
            indices_task, north_flow_task, sectors_task, market_stats_task,
            return_exceptions=True
        )
        
        return {
            "indices": indices if not isinstance(indices, Exception) else None,
            "north_flow": north_flow if not isinstance(north_flow, Exception) else None,
            "sectors": sectors if not isinstance(sectors, Exception) else None,
            "market_stats": market_stats if not isinstance(market_stats, Exception) else None,
            "market_closed": False,
            "market_status": "正常交易",
            "timestamp": now
        }

    def _is_trading_day(self, check_day: date) -> bool:
        """
        判断是否为A股交易日。

        优先使用 AkShare 交易日历，失败时回退到“周一至周五”规则。
        """
        key = check_day.isoformat()
        if key in self._trade_day_cache:
            return self._trade_day_cache[key]

        try:
            df = ak.tool_trade_date_hist_sina()
            if df is not None and not df.empty:
                # 兼容 datetime/date/string 等类型
                trade_days = {str(v)[:10] for v in df.iloc[:, 0].tolist()}
                is_trade_day = key in trade_days
                self._trade_day_cache[key] = is_trade_day
                return is_trade_day
        except Exception as e:
            logger.warning(f"交易日历查询失败，回退周规则: {e}")

        # 回退规则：周一到周五
        is_trade_day = check_day.weekday() < 5
        self._trade_day_cache[key] = is_trade_day
        return is_trade_day

    @staticmethod
    def _parse_numeric(value: Any, default: float = 0.0) -> float:
        """解析数值字符串（兼容逗号、百分号、单位）。"""
        if isinstance(value, (int, float)):
            return float(value)
        text = str(value or "").strip().replace(",", "")
        text = text.replace("%", "").replace("亿元", "").replace("亿", "").replace("万手", "")
        if text in {"", "--", "None", "nan", "NaN"}:
            return default
        try:
            return float(text)
        except Exception:
            return default
    
    def _fetch_indices(self) -> List[Dict]:
        """获取主要指数数据"""
        results = []
        
        for name, info in self.INDEX_MAPPING.items():
            try:
                symbol = f"{info['market']}{info['code']}"
                df = ak.stock_zh_index_daily(symbol=symbol)
                
                if df.empty:
                    continue
                
                latest = df.iloc[-1]
                prev = df.iloc[-2] if len(df) > 1 else latest
                
                change = float(latest["close"]) - float(prev["close"])
                change_pct = (change / float(prev["close"])) * 100 if prev["close"] != 0 else 0
                
                results.append({
                    "name": name,
                    "code": info["code"],
                    "price": float(latest["close"]),
                    "change": change,
                    "change_pct": round(change_pct, 2),
                    "volume": float(latest["volume"]) if "volume" in latest else 0,
                    "open": float(latest["open"]),
                    "high": float(latest["high"]),
                    "low": float(latest["low"]),
                })
            except Exception as e:
                logger.error(f"Error fetching index {name}: {e}")
                continue
        
        return results
    
    def _fetch_north_flow(self) -> Dict:
        """获取北向资金数据
        
        使用 stock_hsgt_fund_flow_summary_em 接口获取当日北向资金流向
        """
        try:
            df = ak.stock_hsgt_fund_flow_summary_em()
            if df is None or df.empty:
                return {}

            def _to_float(value: Any) -> float:
                if isinstance(value, (int, float)):
                    return float(value)
                text = str(value or "").strip().replace(",", "")
                text = text.replace("亿元", "").replace("亿", "")
                if text in {"", "--", "None", "nan", "NaN"}:
                    return 0.0
                try:
                    return float(text)
                except Exception:
                    return 0.0

            direction_col = next((c for c in ("资金方向", "方向") if c in df.columns), "")
            board_col = next((c for c in ("板块", "市场", "通道") if c in df.columns), "")
            net_col = next((c for c in ("成交净买额", "资金净流入", "净买入额", "净流入") if c in df.columns), "")
            date_col = next((c for c in ("交易日", "日期") if c in df.columns), "")
            status_col = next((c for c in ("交易状态", "状态") if c in df.columns), "")

            if not direction_col or not net_col:
                logger.warning("north flow schema changed: columns=%s", list(df.columns))
                return {}

            # 筛选北向资金（沪股通 + 深股通）
            north_data = df[df[direction_col].astype(str).str.contains("北向", na=False)]
            if north_data.empty:
                return {}

            north_data = north_data.copy()
            north_data["_net_flow_num"] = north_data[net_col].apply(_to_float)

            # 计算北向资金总净流入（沪股通 + 深股通）
            total_net_flow = float(north_data["_net_flow_num"].sum())
            trade_date = north_data.iloc[0].get(date_col, "") if date_col else ""
            trade_status = str(north_data.iloc[0].get(status_col, "")) if status_col else ""

            # 获取详细数据
            if board_col:
                hu_data = north_data[north_data[board_col].astype(str).str.contains("沪股通", na=False)]
                shen_data = north_data[north_data[board_col].astype(str).str.contains("深股通", na=False)]
            else:
                hu_data = north_data.iloc[0:0]
                shen_data = north_data.iloc[0:0]

            hu_net_flow = float(hu_data["_net_flow_num"].sum()) if not hu_data.empty else 0.0
            shen_net_flow = float(shen_data["_net_flow_num"].sum()) if not shen_data.empty else 0.0
            is_zero_snapshot = abs(total_net_flow) < 1e-9 and abs(hu_net_flow) < 1e-9 and abs(shen_net_flow) < 1e-9

            return {
                "net_flow": round(float(total_net_flow), 2),  # 单位: 亿元
                "date": str(trade_date),
                "hu_net_flow": round(hu_net_flow, 2),
                "shen_net_flow": round(shen_net_flow, 2),
                "trade_status": trade_status,
                "is_zero_snapshot": bool(is_zero_snapshot),
            }
        except Exception as e:
            logger.error(f"Error fetching north flow: {e}")
            return {}
    
    def _fetch_sectors(self) -> List[Dict]:
        """获取行业板块数据"""
        try:
            df = ak.stock_board_industry_name_em()
            results = []
            
            for _, row in df.iterrows():
                sector_name = row.get("板块名称", "")
                
                # 判断板块分类
                category = "other"
                for cat, names in self.focus_sectors.items():
                    if sector_name in names:
                        category = cat
                        break
                
                results.append({
                    "name": sector_name,
                    "change_pct": float(row.get("涨跌幅", 0)),
                    "turnover": float(row.get("换手率", 0)) if "换手率" in row else 0,
                    "volume": float(row.get("总成交量", 0)) if "总成交量" in row else 0,
                    "amount": float(row.get("总成交额", 0)) if "总成交额" in row else 0,
                    "leading_stock": row.get("领涨股票", ""),
                    "category": category,
                })
            
            return results
        except Exception as e:
            logger.warning(f"stock_board_industry_name_em failed, fallback to ths focus sectors: {e}")
            return self._fetch_focus_sectors_with_ths()

    def _fetch_focus_sectors_with_ths(self) -> List[Dict]:
        """
        当东方财富板块接口不可用时，回退抓取同花顺重点板块快照。
        仅抓取配置中的重点板块，保证报告最小可用板块信息。
        """
        results: List[Dict] = []
        sector_names: List[str] = []
        for category, names in (self.focus_sectors or {}).items():
            if not isinstance(names, list):
                continue
            for name in names:
                if isinstance(name, str) and name.strip():
                    sector_names.append(name.strip())
        sector_names = list(dict.fromkeys(sector_names))
        if not sector_names:
            return results

        available_names: List[str] = []
        try:
            names_df = ak.stock_board_industry_name_ths()
            if names_df is not None and not names_df.empty and "name" in names_df.columns:
                available_names = [
                    str(v).strip() for v in names_df["name"].tolist()
                    if str(v).strip()
                ]
        except Exception as name_err:
            logger.warning("ths sector name list unavailable: %s", name_err)

        selected_names: List[str] = []
        if available_names:
            for name in sector_names:
                if name in available_names:
                    selected_names.append(name)
                    continue
                fuzzy = next(
                    (
                        item for item in available_names
                        if name in item or item in name
                    ),
                    "",
                )
                if fuzzy:
                    selected_names.append(fuzzy)
        else:
            selected_names = sector_names[:]

        selected_names = list(dict.fromkeys([x for x in selected_names if x]))
        if not selected_names:
            return results

        for sector_name in selected_names:
            try:
                info_df = ak.stock_board_industry_info_ths(symbol=sector_name)
                if info_df is None or info_df.empty:
                    continue
                info_map = {
                    str(row.get("项目", "")).strip(): row.get("值")
                    for _, row in info_df.iterrows()
                }

                change_pct = self._parse_numeric(info_map.get("板块涨幅"), 0.0)
                amount = self._parse_numeric(info_map.get("成交额(亿)"), 0.0)
                net_inflow = self._parse_numeric(info_map.get("资金净流入(亿)"), 0.0)

                category = "other"
                for cat, names in self.focus_sectors.items():
                    if sector_name in names:
                        category = cat
                        break

                results.append({
                    "name": sector_name,
                    "change_pct": round(change_pct, 2),
                    "turnover": 0.0,
                    "volume": 0.0,
                    "amount": amount,
                    "leading_stock": "",
                    "category": category,
                    "net_inflow": round(net_inflow, 2),
                    "source": "ths_fallback",
                })
            except Exception as err:
                logger.warning("ths sector detail unavailable for %s: %s", sector_name, err)
                continue
        return results
    
    def _fetch_market_stats(self) -> Dict:
        """获取市场涨跌统计
        
        使用 stock_zt_pool_em 和 stock_zt_pool_dtgc_em 接口
        获取涨停板和跌停板数量
        """
        from datetime import datetime
        today = datetime.now().strftime('%Y%m%d')
        
        result = {
            "limit_up_count": 0,
            "limit_down_count": 0,
        }
        
        try:
            # 获取涨停板数据
            df_up = ak.stock_zt_pool_em(date=today)
            result["limit_up_count"] = len(df_up) if df_up is not None and not df_up.empty else 0
        except Exception as e:
            logger.error(f"Error fetching limit up stocks: {e}")
        
        try:
            # 获取跌停板数据 (跌停观察池)
            df_down = ak.stock_zt_pool_dtgc_em(date=today)
            result["limit_down_count"] = len(df_down) if df_down is not None and not df_down.empty else 0
        except Exception as e:
            logger.error(f"Error fetching limit down stocks: {e}")
        
        return result
    
    def parse(self, raw_data: Dict[str, Any]) -> MarketOverview:
        """
        解析原始数据为标准格式
        
        Args:
            raw_data: fetch() 返回的原始数据
            
        Returns:
            MarketOverview 数据模型
        """
        indices = []
        if raw_data.get("indices"):
            for idx in raw_data["indices"]:
                indices.append(IndexData(
                    name=idx["name"],
                    code=idx["code"],
                    price=idx["price"],
                    change=idx["change"],
                    change_pct=idx["change_pct"],
                    volume=idx["volume"],
                    timestamp=raw_data.get("timestamp", datetime.now())
                ))
        
        sectors = []
        if raw_data.get("sectors"):
            for sec in raw_data["sectors"]:
                sectors.append(SectorData(
                    name=sec["name"],
                    change_pct=sec["change_pct"],
                    leading_stocks=[sec.get("leading_stock", "")] if sec.get("leading_stock") else [],
                    category=sec["category"]
                ))
        
        north_flow = raw_data.get("north_flow", {})
        market_stats = raw_data.get("market_stats", {})
        
        return MarketOverview(
            timestamp=raw_data.get("timestamp", datetime.now()),
            indices=indices,
            sectors=sectors,
            north_flow_net=north_flow.get("net_flow", 0),
            limit_up_count=market_stats.get("limit_up_count", 0),
            limit_down_count=market_stats.get("limit_down_count", 0),
        )
    
    # ==================== 便捷方法 ====================
    
    def get_top_sectors(self, n: int = 5, ascending: bool = False) -> List[SectorData]:
        """
        获取涨幅/跌幅前N的板块
        
        Args:
            n: 返回数量
            ascending: True 返回跌幅最大的，False 返回涨幅最大的
        """
        sectors = self._fetch_sectors()
        sorted_sectors = sorted(sectors, key=lambda x: x["change_pct"], reverse=not ascending)
        return sorted_sectors[:n]
    
    def get_focus_sectors_summary(self) -> Dict[str, List[Dict]]:
        """
        获取重点关注板块的汇总
        
        Returns:
            按分类组织的板块数据
        """
        sectors = self._fetch_sectors()
        result = {cat: [] for cat in self.focus_sectors.keys()}
        
        for sector in sectors:
            if sector["category"] != "other":
                result[sector["category"]].append(sector)
        
        return result
