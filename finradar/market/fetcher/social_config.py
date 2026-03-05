#!/usr/bin/env python3
"""
finradar 社交源配置管理器

支持从 config/config.yaml 读取 Twitter 和微信公众号配置
"""

import os
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field


@dataclass
class TwitterConfig:
    """Twitter/Nitter RSS 配置"""
    enabled: bool = True
    nitter_instance: str = "http://localhost:8080"
    accounts: Dict[str, List[str]] = field(default_factory=dict)
    max_tweets_per_user: int = 0  # 0=不限制
    max_age_hours: int = 12  # 最大推文年龄（小时），配合12小时抓取周期，0=不限制
    timeout: int = 15
    follow_concurrency: int = 1
    follow_request_delay: float = 1.0
    
    # 关注账号滚动缓存（用于实时低频抓取 + 12h 汇总）
    follow_cache_enabled: bool = True
    follow_cache_file: str = "output/twitter/follow_cache.json"
    follow_cache_retention_hours: int = 48
    follow_cache_max_items: int = 30000
    follow_cache_cleanup_interval_hours: int = 6
    
    # 热门推文配置
    fetch_follow_accounts: bool = True
    fetch_trending: bool = True
    trending_mode: str = "keyword"  # keyword | global | hybrid
    trending_keywords: List[str] = field(default_factory=list)
    trending_global_queries: List[str] = field(default_factory=list)
    trending_realtime_sampling: bool = False
    trending_queries_per_run: int = 0
    trending_min_retweets: int = 0
    trending_pages_per_query: int = 3
    search_delay: float = 0.5
    search_page_delay: float = 0.5
    trending_cache_hours: int = 24
    trending_cache_max_items: int = 2000
    trending_cache_file: str = "output/twitter/trending_cache.json"
    trending_state_file: str = "output/twitter/trending_state.json"
    trending_max_results: int = 30
    kol_min_results: int = 8
    keyword_trending_min_results: int = 8
    priority_accounts: List[str] = field(default_factory=list)
    relevance_filter_enabled: bool = True
    relevance_min_score: int = 2
    relevance_positive_keywords: List[str] = field(default_factory=list)
    relevance_negative_keywords: List[str] = field(default_factory=list)
    trending_engagement_threshold: int = 10
    
    def get_all_accounts(self) -> List[str]:
        """获取所有账号列表（去重，并做别名归一化）。"""
        alias_map = {
            "samaltman": "sama",
            "haigao1": "haigao",
            "marcoslopezdeprado": "lopezdeprado",
            "shaynecoplan": "shayne_coplan",
            "nassimtaleb": "nntaleb",
            "tradethenews": "trade_the_news",
            "alexwang_": "alexandr_wang",
            "emad_mostaque": "emostaque",
        }
        all_accounts: List[str] = []
        seen = set()
        for _, accounts in self.accounts.items():
            for raw in (accounts or []):
                account = str(raw or "").strip().lstrip("@")
                if not account:
                    continue
                account = alias_map.get(account.lower(), account)
                key = account.lower()
                if key in seen:
                    continue
                seen.add(key)
                all_accounts.append(account)
        return all_accounts

    def get_accounts_by_category(self, category: str) -> List[str]:
        """按分类获取账号"""
        return self.accounts.get(category, [])


@dataclass
class WechatConfig:
    """微信公众号配置"""
    enabled: bool = True
    service_url: str = "http://localhost:3001"
    timeout: int = 30
    auth_key: str = ""  # API 认证密钥
    accounts: Dict[str, List[str]] = field(default_factory=dict)
    max_articles_per_account: int = 0  # 0=不限制（按时间窗口分页抓取）
    max_age_hours: int = 12  # 最大文章年龄（小时），配合12小时抓取周期，0=不限制
    fetch_content: bool = False  # 是否抓取文章全文内容
    content_delay: float = 0.5  # 抓取全文之间的延迟（秒）
    
    # 热门文章配置
    fetch_hot_articles: bool = True
    hot_max_results: int = 0  # 0=不限制
    hot_hours_ago: int = 48
    hot_categories: List[str] = field(default_factory=list)
    login_reminder_days: int = 4  # 登录提醒阈值（天）
    
    def get_all_accounts(self) -> List[str]:
        """获取所有公众号列表"""
        all_accounts = []
        for category, accounts in self.accounts.items():
            all_accounts.extend(accounts)
        return all_accounts
    
    def get_accounts_by_category(self, category: str) -> List[str]:
        """按分类获取公众号"""
        return self.accounts.get(category, [])


class SocialSourceConfig:
    """
    社交源配置管理器
    
    从 config/config.yaml 读取 Twitter 和微信公众号配置
    
    使用示例:
        config = SocialSourceConfig()
        
        # 获取 Twitter 配置
        twitter_accounts = config.twitter.get_all_accounts()
        
        # 获取微信公众号配置
        wechat_accounts = config.wechat.get_all_accounts()
    """
    
    # 配置文件默认路径 (项目根目录/config/config.yaml)
    DEFAULT_CONFIG_PATH = Path(__file__).parent.parent.parent.parent / "config" / "config.yaml"
    
    def __init__(self, config_path: Optional[str] = None):
        """
        初始化配置管理器
        
        Args:
            config_path: 配置文件路径，默认为 config/config.yaml
        """
        self.config_path = Path(config_path) if config_path else self.DEFAULT_CONFIG_PATH
        self._raw_config: Dict = {}
        self._twitter: Optional[TwitterConfig] = None
        self._wechat: Optional[WechatConfig] = None
        
        self._load_config()
    
    def _load_config(self):
        """加载配置文件"""
        if not self.config_path.exists():
            print(f"⚠️ 配置文件不存在: {self.config_path}")
            return
        
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self._raw_config = yaml.safe_load(f) or {}
        except Exception as e:
            print(f"❌ 读取配置文件失败: {e}")

    @staticmethod
    def _env_bool(name: str, default: bool) -> bool:
        value = os.environ.get(name)
        if value is None:
            return default
        return str(value).strip().lower() in ("1", "true", "yes", "on")
    
    @property
    def twitter(self) -> TwitterConfig:
        """获取 Twitter/Nitter RSS 配置"""
        if self._twitter is None:
            twitter_config = self._raw_config.get("twitter", {})
            config_enabled = twitter_config.get("enabled", True)
            config_instance = twitter_config.get("nitter_instance", "http://localhost:8080")
            self._twitter = TwitterConfig(
                enabled=self._env_bool("ENABLE_TWITTER", config_enabled),
                nitter_instance=os.environ.get("NITTER_INSTANCE", config_instance),
                accounts=twitter_config.get("accounts", {}),
                max_tweets_per_user=twitter_config.get("max_tweets_per_user", 0),
                max_age_hours=twitter_config.get("max_age_hours", 12),
                timeout=twitter_config.get("timeout", 15),
                follow_concurrency=twitter_config.get("follow_concurrency", 1),
                follow_request_delay=twitter_config.get("follow_request_delay", 1.0),
                follow_cache_enabled=twitter_config.get("follow_cache_enabled", True),
                follow_cache_file=twitter_config.get("follow_cache_file", "output/twitter/follow_cache.json"),
                follow_cache_retention_hours=twitter_config.get("follow_cache_retention_hours", 48),
                follow_cache_max_items=twitter_config.get("follow_cache_max_items", 30000),
                follow_cache_cleanup_interval_hours=twitter_config.get("follow_cache_cleanup_interval_hours", 6),
                fetch_follow_accounts=twitter_config.get("fetch_follow_accounts", True),
                fetch_trending=twitter_config.get("fetch_trending", True),
                trending_mode=twitter_config.get("trending_mode", "keyword"),
                trending_keywords=twitter_config.get("trending_keywords", []),
                trending_global_queries=twitter_config.get("trending_global_queries", []),
                trending_realtime_sampling=twitter_config.get("trending_realtime_sampling", False),
                trending_queries_per_run=twitter_config.get("trending_queries_per_run", 0),
                trending_min_retweets=twitter_config.get("trending_min_retweets", 0),
                trending_pages_per_query=twitter_config.get("trending_pages_per_query", 3),
                search_delay=twitter_config.get("search_delay", 0.5),
                search_page_delay=twitter_config.get("search_page_delay", 0.5),
                trending_cache_hours=twitter_config.get("trending_cache_hours", 24),
                trending_cache_max_items=twitter_config.get("trending_cache_max_items", 2000),
                trending_cache_file=twitter_config.get("trending_cache_file", "output/twitter/trending_cache.json"),
                trending_state_file=twitter_config.get("trending_state_file", "output/twitter/trending_state.json"),
                trending_max_results=twitter_config.get("trending_max_results", 30),
                kol_min_results=twitter_config.get("kol_min_results", 8),
                keyword_trending_min_results=twitter_config.get("keyword_trending_min_results", 8),
                priority_accounts=twitter_config.get("priority_accounts", []),
                relevance_filter_enabled=twitter_config.get("relevance_filter_enabled", True),
                relevance_min_score=twitter_config.get("relevance_min_score", 2),
                relevance_positive_keywords=twitter_config.get("relevance_positive_keywords", []),
                relevance_negative_keywords=twitter_config.get("relevance_negative_keywords", []),
                trending_engagement_threshold=twitter_config.get("trending_engagement_threshold", 10)
            )
        return self._twitter
    
    @property
    def wechat(self) -> WechatConfig:
        """获取微信公众号配置"""
        if self._wechat is None:
            wechat_config = self._raw_config.get("wechat", {})
            config_enabled = wechat_config.get("enabled", True)
            config_service_url = wechat_config.get("service_url", "http://localhost:3001")
            config_auth_key = wechat_config.get("auth_key", "")
            try:
                reminder_days = int(
                    os.environ.get(
                        "WECHAT_LOGIN_REMINDER_DAYS",
                        wechat_config.get("login_reminder_days", 4),
                    )
                )
            except (TypeError, ValueError):
                reminder_days = 4
            reminder_days = max(1, reminder_days)
            self._wechat = WechatConfig(
                enabled=self._env_bool("ENABLE_WECHAT", config_enabled),
                service_url=os.environ.get("WECHAT_SERVICE_URL", config_service_url),
                timeout=wechat_config.get("timeout", 30),
                auth_key=os.environ.get("WECHAT_AUTH_KEY", config_auth_key),
                accounts=wechat_config.get("accounts", {}),
                max_articles_per_account=wechat_config.get("max_articles_per_account", 0),
                max_age_hours=wechat_config.get("max_age_hours", 24),
                fetch_content=wechat_config.get("fetch_content", False),
                content_delay=wechat_config.get("content_delay", 0.5),
                fetch_hot_articles=wechat_config.get("fetch_hot_articles", True),
                hot_max_results=wechat_config.get("hot_max_results", 0),
                hot_hours_ago=wechat_config.get("hot_hours_ago", 48),
                hot_categories=wechat_config.get("hot_categories", []),
                login_reminder_days=reminder_days,
            )
        return self._wechat
    
    def reload(self):
        """重新加载配置"""
        self._twitter = None
        self._wechat = None
        self._load_config()
    
    def get_raw_config(self) -> Dict:
        """获取原始配置字典"""
        return self._raw_config


# ==================== 便捷函数 ====================

def get_twitter_accounts() -> List[str]:
    """
    获取所有 Twitter 账号
    
    Returns:
        Twitter 账号用户名列表
    """
    config = SocialSourceConfig()
    return config.twitter.get_all_accounts()


def get_wechat_accounts() -> List[str]:
    """
    获取所有微信公众号
    
    Returns:
        微信公众号名称列表
    """
    config = SocialSourceConfig()
    return config.wechat.get_all_accounts()


def print_config_summary():
    """打印配置摘要"""
    config = SocialSourceConfig()
    
    print("=" * 60)
    print("📋 finradar 社交源配置摘要")
    print("=" * 60)
    
    # Twitter 配置
    print("\n🐦 Twitter/Nitter RSS 配置:")
    print(f"   启用状态: {'✅ 已启用' if config.twitter.enabled else '❌ 已禁用'}")
    print(f"   Nitter 实例: {config.twitter.nitter_instance}")
    print(f"   超时时间: {config.twitter.timeout}s")
    print(f"   每用户推文数: {config.twitter.max_tweets_per_user}")
    print(f"   抓取节奏: 并发 {config.twitter.follow_concurrency} | 间隔 {config.twitter.follow_request_delay}s")
    print(f"   关注缓存: {'✅' if config.twitter.follow_cache_enabled else '❌'} | 保留 {config.twitter.follow_cache_retention_hours}h")
    print(f"   热门TopN: {config.twitter.trending_max_results} | KOL保底: {config.twitter.kol_min_results} | 关键词保底: {config.twitter.keyword_trending_min_results}")
    print(f"   KOL优先名单: {len(config.twitter.priority_accounts)} 个")
    
    print("\n   📌 关注账号:")
    for category, accounts in config.twitter.accounts.items():
        print(f"      [{category}] ({len(accounts)}人): {', '.join(accounts[:3])}{'...' if len(accounts) > 3 else ''}")
    
    total_twitter = len(config.twitter.get_all_accounts())
    print(f"   合计: {total_twitter} 个账号")
    
    # 微信公众号配置
    print("\n📱 微信公众号配置:")
    print(f"   启用状态: {'✅ 已启用' if config.wechat.enabled else '❌ 已禁用'}")
    print(f"   服务地址: {config.wechat.service_url}")
    print(f"   超时时间: {config.wechat.timeout}s")
    print(f"   每账号文章数: {config.wechat.max_articles_per_account}")
    print(f"   最大文章时间: {config.wechat.max_age_hours} 小时")
    
    print("\n   📌 关注公众号:")
    for category, accounts in config.wechat.accounts.items():
        print(f"      [{category}] ({len(accounts)}个): {', '.join(accounts[:3])}{'...' if len(accounts) > 3 else ''}")
    
    total_wechat = len(config.wechat.get_all_accounts())
    print(f"   合计: {total_wechat} 个公众号")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    print_config_summary()
