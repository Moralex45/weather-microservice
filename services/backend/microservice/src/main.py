import fastapi
import uvicorn
from aioredis import Redis
import aioredis
from fastapi.responses import ORJSONResponse

from db import cache
from core.config import get_settings_instance
from db.cache.redis import AsyncRedisCacheService
from api.v1 import weather

app = fastapi.FastAPI(
    title='',
    description='',
    version=1,
    default_response_class=ORJSONResponse,
)

@app.on_event('startup')
async def startup_event():
    redis_pool: Redis = await aioredis.create_redis_pool(
        (get_settings_instance().REDIS_HOST, get_settings_instance().REDIS_PORT),
        minsize=10,
        maxsize=20)
    cache.cache_service = AsyncRedisCacheService(redis_pool)

@app.on_event('shutdown')
async def shutdown_event():
    await cache.cache_service.close()

app.include_router(weather.router, prefix='/api/v1/weather', tags=['weather'])

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
        reload=True
    )
