# Time Server API

Простое FastAPI приложение, возвращающее текущее время сервера.

## GitHub Actions CI/CD

Проект включает автоматизированный workflow для сборки Docker образа и деплоя на сервер.

### Настройка секретов

Для работы workflow необходимо настроить следующие секреты в GitHub репозитории (Settings → Secrets and variables → Actions):

- `SSH_PRIVATE_KEY` - Приватный SSH ключ для подключения к серверу
- `SSH_HOST` - IP адрес или доменное имя сервера
- `SSH_USER` - Имя пользователя для SSH подключения
- `SSH_PORT` - Порт SSH (опционально, по умолчанию 22)

### Workflow

Workflow состоит из двух джоб:

1. **build-and-push** - Собирает Docker образ и пушит его в GitHub Container Registry (GHCR)
2. **deploy** - Подключается к серверу по SSH, скачивает образ из GHCR и развертывает контейнер

Workflow запускается автоматически при пуше в ветки `main` или `master`, а также может быть запущен вручную через `workflow_dispatch`.

### Docker

Образ будет доступен в GitHub Container Registry по адресу:
`ghcr.io/<ваш-username>/<название-репозитория>:latest`

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
- `GET /date` - Получить текущую дату сервера
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

```bash
curl http://127.0.0.1:8000/date
```

Ответ:
```json
{
  "server_date": "2024-01-15",
  "year": "2024",
  "month": "01",
  "day": "15"
}
```
