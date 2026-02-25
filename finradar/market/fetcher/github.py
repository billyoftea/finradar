"""
GitHub 趋势数据抓取器

可选实现方案：
1. PyGithub - GitHub 官方 Python SDK
   GitHub: https://github.com/PyGithub/PyGithub
   安装: pip install PyGithub

2. 直接使用 requests 调用 GitHub REST API
   API文档: https://docs.github.com/en/rest

3. 第三方 github-trending-api (非官方)
   GitHub: https://github.com/huchenme/github-trending-api

GitHub API 限制:
- 无认证: 60 requests/hour
- 有认证: 5000 requests/hour (使用 Personal Access Token)

支持获取:
- Trending 仓库（按 star 增长）
- 热门语言项目
- 最新创建的热门项目
"""

import asyncio
import math
from datetime import datetime, timedelta
from typing import Dict, Any, Optional, List
import logging

try:
    from github import Github
    PYGITHUB_AVAILABLE = True
except ImportError:
    PYGITHUB_AVAILABLE = False
    Github = None

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False

from . import BaseFetcher
from ..models.market_data import GitHubTrendingRepo

logger = logging.getLogger(__name__)


class GitHubFetcher(BaseFetcher):
    """
    GitHub 趋势数据抓取器
    
    支持获取:
    - 今日/本周热门仓库（按 star 排序）
    - 指定语言的热门项目
    - 最近创建的爆款项目
    - AI/ML 相关热门项目
    """
    
    GITHUB_API_BASE = "https://api.github.com"
    
    # 热门编程语言
    POPULAR_LANGUAGES = [
        "python", "javascript", "typescript", "rust", "go", 
        "java", "cpp", "c", "swift", "kotlin"
    ]
    
    # AI/ML 相关关键词
    AI_KEYWORDS = [
        "llm", "gpt", "ai", "machine-learning", "deep-learning",
        "transformer", "langchain", "chatgpt", "openai", "anthropic"
    ]
    FINTECH_KEYWORDS = [
        "fintech", "quant", "trading", "portfolio", "risk", "payment",
        "banking", "broker", "orderbook", "market-data"
    ]
    QUANT_KEYWORDS = [
        "quant", "quantitative", "backtest", "backtesting", "factor",
        "alpha", "portfolio", "risk-model", "timeseries", "orderbook"
    ]
    WEB3_KEYWORDS = [
        "web3", "blockchain", "defi", "wallet", "ethereum", "bitcoin",
        "solidity", "token", "nft", "zk"
    ]
    INTERESTING_KEYWORDS = [
        "agent", "automation", "mcp", "search", "observability",
        "benchmark", "simulator", "database", "compiler", "inference"
    ]
    
    def __init__(self, config: Optional[Dict] = None):
        super().__init__(config)
        
        # GitHub Token（可选，用于提高 API 限额）
        self.token = self.config.get("token", "")
        self.authenticated = bool(str(self.token).strip())
        
        # 初始化客户端
        if PYGITHUB_AVAILABLE and self.token:
            self.gh = Github(self.token)
        elif PYGITHUB_AVAILABLE:
            self.gh = Github()  # 无认证模式
        else:
            self.gh = None
            if not REQUESTS_AVAILABLE:
                logger.warning("Neither PyGithub nor requests available. Install one of them.")
                self.enabled = False
        
        # 配置
        self.languages = self.config.get("languages", ["python", "javascript", "rust"])
        self.fetch_count = max(1, int(self.config.get("fetch_count", 10) or 10))
        self.search_candidates_multiplier = max(
            1, int(self.config.get("search_candidates_multiplier", 3) or 3)
        )
        self.max_candidates_per_query = max(
            self.fetch_count, int(self.config.get("max_candidates_per_query", 40) or 40)
        )
        # 多样性约束，避免“固定几个项目”反复出现
        self.max_per_owner = max(1, int(self.config.get("max_per_owner", 1) or 1))
        self.max_per_language = max(1, int(self.config.get("max_per_language", 4) or 4))
        self.max_language_boost_queries = max(
            0, int(self.config.get("max_language_boost_queries", 4) or 4)
        )

        # 无 token 场景自动降载，避免触发 Search API 速率限制
        if not self.authenticated:
            self.fetch_count = min(self.fetch_count, 10)
            self.search_candidates_multiplier = min(self.search_candidates_multiplier, 2)
            self.max_candidates_per_query = min(self.max_candidates_per_query, 24)
            self.max_language_boost_queries = min(self.max_language_boost_queries, 1)
    
    async def fetch(self) -> Dict[str, Any]:
        """
        抓取 GitHub 趋势数据
        
        Returns:
            包含热门仓库数据的字典
        """
        loop = asyncio.get_event_loop()
        
        # 并行获取不同类型的趋势数据
        tasks = [
            loop.run_in_executor(None, self._fetch_trending_repos),
            loop.run_in_executor(None, self._fetch_ai_repos),
            loop.run_in_executor(None, self._fetch_fintech_repos),
            loop.run_in_executor(None, self._fetch_quant_repos),
            loop.run_in_executor(None, self._fetch_web3_repos),
            loop.run_in_executor(None, self._fetch_interesting_repos),
        ]
        trending, ai_repos, fintech_repos, quant_repos, web3_repos, interesting_repos = await asyncio.gather(
            *tasks,
            return_exceptions=True
        )
        
        return {
            "trending": trending if not isinstance(trending, Exception) else [],
            "ai_trending": ai_repos if not isinstance(ai_repos, Exception) else [],
            "fintech_trending": fintech_repos if not isinstance(fintech_repos, Exception) else [],
            "quant_trending": quant_repos if not isinstance(quant_repos, Exception) else [],
            "web3_trending": web3_repos if not isinstance(web3_repos, Exception) else [],
            "interesting_trending": interesting_repos if not isinstance(interesting_repos, Exception) else [],
            "timestamp": datetime.now()
        }
    
    def _fetch_trending_repos(self) -> List[Dict]:
        """
        获取今日热门仓库
        
        通过搜索最近创建且 star 数增长快的仓库来模拟 trending
        """
        candidate_count = self._candidate_count()
        # 维持“新建爆款”和“近期活跃爆款”两条线，扩大覆盖
        created_from = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
        pushed_from = (datetime.now() - timedelta(days=21)).strftime("%Y-%m-%d")

        pools: List[Dict[str, Any]] = []
        pools.extend(
            self._search_repos(
                f"created:>{created_from} stars:>80",
                sort="stars",
                per_page=candidate_count,
            )
        )
        if self.authenticated:
            pools.extend(
                self._search_repos(
                    f"pushed:>{pushed_from} stars:>120",
                    sort="updated",
                    per_page=candidate_count,
                )
            )
            pools.extend(self._fetch_language_boost_repos(candidate_count))
        return self._finalize_repo_pool(pools, limit=self.fetch_count)
    
    def _fetch_ai_repos(self) -> List[Dict]:
        """获取 AI/ML 相关热门仓库"""
        candidate_count = self._candidate_count()
        date_from = (datetime.now() - timedelta(days=45)).strftime("%Y-%m-%d")

        pools: List[Dict[str, Any]] = []
        # 两组关键词，减少固定词组导致的重复
        q1 = " OR ".join(self.AI_KEYWORDS[:6])
        q2 = " OR ".join(self.AI_KEYWORDS[2:8])
        pools.extend(
            self._search_repos(
                f"({q1}) pushed:>{date_from} stars:>30",
                sort="stars",
                per_page=candidate_count,
            )
        )
        if self.authenticated:
            pools.extend(
                self._search_repos(
                    f"({q2}) pushed:>{date_from} stars:>30",
                    sort="updated",
                    per_page=candidate_count,
                )
            )
        return self._finalize_repo_pool(pools, limit=self.fetch_count)

    def _fetch_fintech_repos(self) -> List[Dict]:
        """获取金融科技相关热门仓库。"""
        candidate_count = self._candidate_count()
        date_from = (datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d")
        q1 = " OR ".join(self.FINTECH_KEYWORDS[:6])
        q2 = " OR ".join(self.FINTECH_KEYWORDS[2:8])
        pools: List[Dict[str, Any]] = []
        pools.extend(
            self._search_repos(
                f"({q1}) pushed:>{date_from} stars:>15",
                sort="updated",
                per_page=candidate_count,
            )
        )
        if self.authenticated:
            pools.extend(
                self._search_repos(
                    f"({q2}) pushed:>{date_from} stars:>15",
                    sort="stars",
                    per_page=candidate_count,
                )
            )
        return self._finalize_repo_pool(pools, limit=self.fetch_count)

    def _fetch_quant_repos(self) -> List[Dict]:
        """获取量化交易/研究相关热门仓库。"""
        candidate_count = self._candidate_count()
        date_from = (datetime.now() - timedelta(days=120)).strftime("%Y-%m-%d")
        q1 = " OR ".join(self.QUANT_KEYWORDS[:6])
        q2 = " OR ".join(self.QUANT_KEYWORDS[2:8])
        pools: List[Dict[str, Any]] = []
        pools.extend(
            self._search_repos(
                f"({q1}) pushed:>{date_from} stars:>10",
                sort="updated",
                per_page=candidate_count,
            )
        )
        if self.authenticated:
            pools.extend(
                self._search_repos(
                    f"({q2}) pushed:>{date_from} stars:>10",
                    sort="stars",
                    per_page=candidate_count,
                )
            )
        return self._finalize_repo_pool(pools, limit=self.fetch_count)

    def _fetch_web3_repos(self) -> List[Dict]:
        """获取 Web3 相关热门仓库。"""
        candidate_count = self._candidate_count()
        date_from = (datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d")
        q1 = " OR ".join(self.WEB3_KEYWORDS[:6])
        q2 = " OR ".join(self.WEB3_KEYWORDS[2:8])
        pools: List[Dict[str, Any]] = []
        pools.extend(
            self._search_repos(
                f"({q1}) pushed:>{date_from} stars:>15",
                sort="updated",
                per_page=candidate_count,
            )
        )
        if self.authenticated:
            pools.extend(
                self._search_repos(
                    f"({q2}) pushed:>{date_from} stars:>15",
                    sort="stars",
                    per_page=candidate_count,
                )
            )
        return self._finalize_repo_pool(pools, limit=self.fetch_count)

    def _fetch_interesting_repos(self) -> List[Dict]:
        """获取“有意思”的通用项目（跨赛道探索池）。"""
        candidate_count = self._candidate_count()
        date_from = (datetime.now() - timedelta(days=35)).strftime("%Y-%m-%d")
        q1 = " OR ".join(self.INTERESTING_KEYWORDS[:6])
        q2 = " OR ".join(self.INTERESTING_KEYWORDS[2:8])
        pools: List[Dict[str, Any]] = []
        pools.extend(
            self._search_repos(
                f"({q1}) pushed:>{date_from} stars:>80",
                sort="stars",
                per_page=candidate_count,
            )
        )
        if self.authenticated:
            pools.extend(
                self._search_repos(
                    f"({q2}) pushed:>{date_from} stars:>80",
                    sort="updated",
                    per_page=candidate_count,
                )
            )
        return self._finalize_repo_pool(pools, limit=self.fetch_count)

    def _candidate_count(self) -> int:
        """每条查询抓取候选数。"""
        return min(self.max_candidates_per_query, max(self.fetch_count, self.fetch_count * self.search_candidates_multiplier))

    def _fetch_language_boost_repos(self, candidate_count: int) -> List[Dict]:
        """
        按语言做补充搜索，提升覆盖面，避免总是同一批仓库。
        只取前 4 个语言，控制 API 请求量。
        """
        if not self.languages:
            return []
        date_from = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
        per_language = max(4, math.ceil(candidate_count / 4))
        pools: List[Dict] = []
        if self.max_language_boost_queries <= 0:
            return pools
        for language in self.languages[: self.max_language_boost_queries]:
            query = f"language:{language} pushed:>{date_from} stars:>50"
            pools.extend(self._search_repos(query, sort="stars", per_page=per_language))
        return pools

    def _finalize_repo_pool(self, repos: List[Dict], limit: int) -> List[Dict]:
        """候选仓库去重+多样性重排后截断。"""
        deduped: List[Dict] = []
        seen = set()
        for repo in repos:
            if not isinstance(repo, dict):
                continue
            key = repo.get("full_name") or repo.get("url") or repo.get("name")
            if not key or key in seen:
                continue
            seen.add(key)
            deduped.append(repo)

        # 先按热度排序
        deduped.sort(
            key=lambda r: (
                int(r.get("stars", 0) or 0),
                int(r.get("forks", 0) or 0),
                str(r.get("updated_at", "")),
            ),
            reverse=True,
        )

        # 再做多样性采样（owner/language 上限）
        selected: List[Dict] = []
        owner_count: Dict[str, int] = {}
        language_count: Dict[str, int] = {}
        for repo in deduped:
            owner = str(repo.get("owner", "") or "").lower()
            language = str(repo.get("language", "Unknown") or "Unknown").lower()
            if owner and owner_count.get(owner, 0) >= self.max_per_owner:
                continue
            if language_count.get(language, 0) >= self.max_per_language:
                continue

            selected.append(repo)
            if owner:
                owner_count[owner] = owner_count.get(owner, 0) + 1
            language_count[language] = language_count.get(language, 0) + 1
            if len(selected) >= limit:
                break

        if len(selected) >= limit:
            return selected[:limit]

        # 不足时补齐（放宽多样性约束）
        used = {r.get("full_name") or r.get("url") or r.get("name") for r in selected}
        for repo in deduped:
            key = repo.get("full_name") or repo.get("url") or repo.get("name")
            if key in used:
                continue
            selected.append(repo)
            if len(selected) >= limit:
                break
        return selected[:limit]
    
    def _fetch_repos_by_language(self, language: str) -> List[Dict]:
        """获取指定语言的热门仓库"""
        date_from = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
        query = f"language:{language} created:>{date_from} stars:>50"
        
        return self._search_repos(query, sort="stars", per_page=5)
    
    def _search_repos(self, query: str, sort: str = "stars", per_page: int = 10) -> List[Dict]:
        """
        执行仓库搜索
        
        Args:
            query: GitHub 搜索查询语句
            sort: 排序方式 (stars, forks, updated)
            per_page: 返回数量
        """
        try:
            if self.gh and PYGITHUB_AVAILABLE:
                return self._search_with_pygithub(query, sort, per_page)
            else:
                return self._search_with_requests(query, sort, per_page)
        except Exception as e:
            logger.error(f"Error searching repos: {e}")
            return []
    
    def _search_with_pygithub(self, query: str, sort: str, per_page: int) -> List[Dict]:
        """使用 PyGithub 搜索"""
        repos = self.gh.search_repositories(query=query, sort=sort, order="desc")
        
        results = []
        for i, repo in enumerate(repos):
            if i >= per_page:
                break
            
            results.append({
                "name": repo.name,
                "full_name": repo.full_name,
                "description": repo.description or "",
                "url": repo.html_url,
                "stars": repo.stargazers_count,
                "forks": repo.forks_count,
                "language": repo.language or "Unknown",
                "topics": repo.topics if hasattr(repo, 'topics') else [],
                "created_at": repo.created_at.isoformat() if repo.created_at else "",
                "updated_at": repo.updated_at.isoformat() if repo.updated_at else "",
                "owner": repo.owner.login if repo.owner else "",
                "owner_avatar": repo.owner.avatar_url if repo.owner else "",
            })
        
        return results
    
    def _search_with_requests(self, query: str, sort: str, per_page: int) -> List[Dict]:
        """使用 requests 直接调用 API"""
        url = f"{self.GITHUB_API_BASE}/search/repositories"
        
        headers = {}
        if self.token:
            headers["Authorization"] = f"token {self.token}"
        
        params = {
            "q": query,
            "sort": sort,
            "order": "desc",
            "per_page": per_page
        }
        
        response = requests.get(url, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        results = []
        for repo in data.get("items", []):
            results.append({
                "name": repo.get("name", ""),
                "full_name": repo.get("full_name", ""),
                "description": repo.get("description", "") or "",
                "url": repo.get("html_url", ""),
                "stars": repo.get("stargazers_count", 0),
                "forks": repo.get("forks_count", 0),
                "language": repo.get("language", "Unknown") or "Unknown",
                "topics": repo.get("topics", []),
                "created_at": repo.get("created_at", ""),
                "updated_at": repo.get("updated_at", ""),
                "owner": repo.get("owner", {}).get("login", ""),
                "owner_avatar": repo.get("owner", {}).get("avatar_url", ""),
            })
        
        return results
    
    def parse(self, raw_data: Dict[str, Any]) -> Dict[str, List[GitHubTrendingRepo]]:
        """
        解析原始数据为标准格式
        
        Args:
            raw_data: fetch() 返回的原始数据
            
        Returns:
            按类别组织的 GitHubTrendingRepo 字典
        """
        timestamp = raw_data.get("timestamp", datetime.now())
        
        def convert_repos(repos: List[Dict]) -> List[GitHubTrendingRepo]:
            return [
                GitHubTrendingRepo(
                    name=repo.get("name", ""),
                    full_name=repo.get("full_name", ""),
                    description=repo.get("description", ""),
                    url=repo.get("url", ""),
                    stars=repo.get("stars", 0),
                    forks=repo.get("forks", 0),
                    language=repo.get("language", ""),
                    topics=repo.get("topics", []),
                    timestamp=timestamp
                )
                for repo in repos
            ]
        
        return {
            "trending": convert_repos(raw_data.get("trending", [])),
            "ai_trending": convert_repos(raw_data.get("ai_trending", [])),
            "fintech_trending": convert_repos(raw_data.get("fintech_trending", [])),
            "quant_trending": convert_repos(raw_data.get("quant_trending", [])),
            "web3_trending": convert_repos(raw_data.get("web3_trending", [])),
            "interesting_trending": convert_repos(raw_data.get("interesting_trending", [])),
        }
    
    # ==================== 便捷方法 ====================
    
    def get_daily_trending(self, limit: int = 10) -> List[Dict]:
        """获取今日热门仓库"""
        return self._fetch_trending_repos()[:limit]
    
    def get_language_trending(self, language: str, limit: int = 5) -> List[Dict]:
        """获取指定语言的热门仓库"""
        return self._fetch_repos_by_language(language)[:limit]
    
    def get_ai_ml_trending(self, limit: int = 10) -> List[Dict]:
        """获取 AI/ML 相关热门仓库"""
        return self._fetch_ai_repos()[:limit]
