import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from order_service.storage import orders
from order_service.mq_producer import publish_order_created

app = FastAPI()


class OrderRequest(BaseModel):
    user_id: int
    amount: float


@app.post("/orders")
def create_order(order_request: OrderRequest):

    order_id = len(orders) + 1

    orders[order_id] = {
        "id": order_id,
        "user_id": order_request.user_id,
        "amount": order_request.amount,
        "status": "created"
    }

    # отправляем событие в RabbitMQ
    publish_order_created(orders[order_id])

    # HTTP вызов Payment Service (можно оставить)
    response = requests.post(
        "http://127.0.0.1:8001/pay",
        json={
            "order_id": order_id,
            "amount": order_request.amount
        }
    )

    result = response.json()

    orders[order_id]["status"] = result["status"]

    return orders[order_id]


@app.get("/orders/{order_id}")
def get_order(order_id: int):

    order = orders.get(order_id)

    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    return order
