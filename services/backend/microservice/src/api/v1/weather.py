from http import HTTPStatus

from fastapi import APIRouter
import httpx
from scrapy.selector import Selector

from core.config import get_settings_instance

router = APIRouter()

@router.get('/{city}',
            description='Получение прогноза погоды',
            summary='Endpoint позволяет получать актуальную погоду для конкретного города',
            response_description='',
            tags=['Данные погоды'])
async def get_weather_by_city(city: str):
    pass