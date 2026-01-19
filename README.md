# Time Server API

Простое FastAPI приложение, возвращающее текущее время сервера.

## Установка

1. Активируйте виртуальное окружение:
   ```bash
   # Windows PowerShell
   .\venv\Scripts\Activate.ps1
   
   # Windows CMD
   venv\Scripts\activate.bat
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## Запуск

Запустите сервер с помощью uvicorn:

```bash
uvicorn main:app --reload
```

Сервер будет доступен по адресу: `http://127.0.0.1:8000`

## Эндпоинты

- `GET /` - Информация о API
- `GET /time` - Получить текущее время сервера
- `GET /docs` - Интерактивная документация Swagger UI
- `GET /redoc` - Альтернативная документация ReDoc

## Пример использования

```bash
curl http://127.0.0.1:8000/time
```

Ответ:
```json
{
  "server_time": "2024-01-15T14:30:45.123456",
  "timestamp": "2024-01-15 14:30:45",
  "timezone": "UTC+03:00"
}
```
