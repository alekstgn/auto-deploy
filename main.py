from fastapi import FastAPI
from datetime import datetime
from typing import Dict

app = FastAPI(title="Time Server API", version="1.0.0")


@app.get("/")
async def root() -> Dict[str, str]:
    """Корневой эндпоинт с информацией о API"""
    return {
        "message": "Time Server API",
        "endpoints": {
            "/time": "Получить текущее время сервера",
            "/date": "Получить текущую дату сервера",
            "/docs": "Интерактивная документация API"
        }
    }


@app.get("/time")
async def get_server_time() -> Dict[str, str]:
    """Возвращает текущее время сервера"""
    current_time = datetime.now()
    return {
        "server_time": current_time.isoformat(),
        "timestamp": current_time.strftime("%Y-%m-%d %H:%M:%S"),
        "timezone": str(current_time.astimezone().tzinfo)
    }


@app.get("/date")
async def get_server_date() -> Dict[str, str]:
    """Возвращает текущую дату сервера"""
    today = datetime.now().date()
    return {
        "server_date": today.isoformat(),
        "year": today.strftime("%Y"),
        "month": today.strftime("%m"),
        "day": today.strftime("%d")
    }
