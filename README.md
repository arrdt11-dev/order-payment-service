# Order Payment Service

Микросервисное приложение, состоящее из двух сервисов:

- Order Service — создаёт и хранит заказы
- Payment Service — обрабатывает оплату

Взаимодействие реализовано через HTTP и RabbitMQ.  
Проект использует FastAPI и Poetry.

---

# Установка

Клонировать репозиторий:

git clone https://github.com/arrdt11-dev/order-payment-service.git
cd order-payment-service

Установить зависимости через Poetry:

poetry install

Запуск команд через Poetry:

poetry run <command>

---

# Запуск сервисов (HTTP)

## Запуск Payment Service

poetry run uvicorn payment_service.http_app:app --port 8001 --reload

## Запуск Order Service

в новом терминале:

poetry run uvicorn order_service.http_app:app --port 8000 --reload

---

# Использование API

Документация доступна после запуска:

http://127.0.0.1:8000/docs

---

## Создать заказ

POST /orders

пример body:

{
  "user_id": 1,
  "amount": 100
}

---

## Получить заказ

GET /orders/{id}

пример:

http://127.0.0.1:8000/orders/1

---

# RabbitMQ (event-driven)

Запуск RabbitMQ через Docker:

docker run -d -p 5672:5672 -p 15672:15672 rabbitmq:3-management

Запуск consumer:

poetry run python payment_service/mq_consumer.py

---

# Технологии

Python  
FastAPI  
RabbitMQ  
Poetry  
Docker  

---

#
https://github.com/arrdt11-dev/order-payment-service
