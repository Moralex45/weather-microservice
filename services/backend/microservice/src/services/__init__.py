from functools import lru_cache

from db.cache.base import AsyncCacheService

class WeatherService:
    def __init__(self, cache_service: AsyncCacheService):
        self.cache_service: AsyncCacheService = cache_service