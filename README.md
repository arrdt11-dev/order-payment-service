# Order & Payment Service

### Запуск сервиса оплаты (Терминал 1):
poetry run uvicorn payment_service:app --host 127.0.0.1 --port 8001

### Запуск сервиса заказов (Терминал 2):
poetry run uvicorn order_service:app --host 127.0.0.1 --port 8000

### Проверка (Терминал 3):
curl -X POST http://127.0.0.1 -H "Content-Type: application/json" -d '{"user_id": 1, "amount": 100}'
## Работа через RabbitMQ
1. Запустить брокер: `sudo systemctl start rabbitmq-server`
2. Запустить воркер: `poetry run python payment_worker.py`
3. Отправить заказ: `curl -X POST http://127.0.0.1:8000/orders_mq ...`
