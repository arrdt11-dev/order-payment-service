
Реализовано:
- FastAPI
- HTTP взаимодействие между сервисами
- Event-driven взаимодействие через RabbitMQ
- Poetry для управления зависимостями
- хранение заказов в памяти

---

# Установка

Установить Poetry:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Установить зависимости:

```bash
poetry install
```

---

# Запуск RabbitMQ

Ubuntu:

```bash
sudo apt install rabbitmq-server -y
sudo systemctl start rabbitmq-server
```

проверка:

```bash
sudo systemctl status rabbitmq-server
```

---

# Запуск Payment Service consumer

```bash
poetry run python payment_service/mq_consumer.py
```

---

# Запуск Payment Service HTTP

в новом терминале:

```bash
poetry run uvicorn payment_service.http_app:app --host 0.0.0.0 --port 8001
```

---

# Запуск Order Service

в новом терминале:

```bash
poetry run uvicorn order_service.http_app:app --host 0.0.0.0 --port 8000
```

---

# Использование

Swagger Order Service:

```
http://localhost:8000/docs
```

создание заказа:

POST /orders

пример:

```json
{
  "user_id": 1,
  "amount": 100
}
```

если amount > 0 → status = paid  
если amount = 0 → status = failed  

---

# Event-driven flow

Order Service:
- создаёт заказ
- публикует событие order_created

Payment Service:
- читает событие
- обрабатывает оплату
- выводит результат

---

# Стек

- Python
- FastAPI
- RabbitMQ
- Poetry
