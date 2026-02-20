from fastapi import FastAPI
from pydantic import BaseModel
import httpx

app = FastAPI()

orders = {}
order_counter = 1

PAYMENT_SERVICE_URL = "http://localhost:8001/pay"

class OrderRequest(BaseModel):
    user_id: int
    amount: float

@app.post("/orders")
async def create_order(request: OrderRequest):
    global order_counter
    
    order_id = order_counter
    order_counter += 1
    
    new_order = {
        "id": order_id,
        "user_id": request.user_id,
        "amount": request.amount,
        "status": "created"
    }
    
    orders[order_id] = new_order
    print(f"Заказ {order_id} создан. Статус: created")
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                PAYMENT_SERVICE_URL,
                json={
                    "order_id": order_id, 
                    "amount": request.amount
                },
                timeout=5.0
            )
            if response.status_code == 200:
                result = response.json()
                new_order["status"] = result["status"]
            else:
                new_order["status"] = "failed"
        except Exception:
            new_order["status"] = "failed"
    
    orders[order_id] = new_order
    return new_order
