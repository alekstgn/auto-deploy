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
