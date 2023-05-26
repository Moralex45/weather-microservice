from abc import ABC, abstractmethod
from typing import Any, Type

class AsyncCache(ABC):
    
    async def get(self, key: str) -> Any | None:
        raise NotImplementedError()
    
    async def set(self, key: str, expire: int):
        raise NotImplementedError()
    
class AsyncCacheService(AsyncCache):

    @abstractmethod
    async def set_single(self, key: str, data, expire: int):
        raise NotImplementedError()
    
    @abstractmethod
    async def close(self):
        raise NotImplementedError()