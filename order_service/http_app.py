from fastapi import FastAPI
from pydantic import BaseModel
import requests
from order_service.storage import orders

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
    response = requests.post("http://127.0.0.1:8001/pay", json={
        "order_id": order_id,
        "amount": order_request.amount
    })
    result = response.json()
    orders[order_id]["status"] = result["status"]
    return orders[order_id]
