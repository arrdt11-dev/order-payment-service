# Order & Payment Service

### Запуск сервиса оплаты (Терминал 1):
poetry run uvicorn payment_service:app --host 127.0.0.1 --port 8001

### Запуск сервиса заказов (Терминал 2):
poetry run uvicorn order_service:app --host 127.0.0.1 --port 8000

### Проверка (Терминал 3):
curl -X POST http://127.0.0.1 -H "Content-Type: application/json" -d '{"user_id": 1, "amount": 100}'
