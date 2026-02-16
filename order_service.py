# ========== order_service.py ==========

from fastapi import FastAPI
from pydantic import BaseModel
import httpx  
import uvicorn
from datetime import datetime  


app = FastAPI()


orders = {}


order_counter = 1


PAYMENT_SERVICE_URL = "http://localhost:8001/pay"


class OrderRequest(BaseModel):
    user_id: int
    amount: float


class OrderResponse(BaseModel):
    id: int
    user_id: int
    amount: float
    status: str
    created_at: datetime

@app.post("/orders")
async def create_order(request: OrderRequest):
    global order_counter  # говорим, что будем менять глобальную переменную
    
   
    order_id = order_counter
    order_counter += 1
    
    
    now = datetime.now()
    
    
    new_order = {
        "id": order_id,
        "user_id": request.user_id,
        "amount": request.amount,
        "status": "created",
        "created_at": now
    }
    
  
    orders[order_id] = new_order
    print(f" Заказ {order_id} создан. Статус: created")
    
  
    print(f" Идем в Payment Service за оплатой заказа {order_id}...")
    
    
    async with httpx.AsyncClient() as client:
        try:
            
            response = await client.post(
                PAYMENT_SERVICE_URL,
                json={
                    "order_id": order_id, 
                    "amount": request.amount
                },
                timeout=5.0  # ждем ответ максимум 5 секунд
            )
            
            
            if response.status_code == 200:
                result = response.json()
                new_order["status"] = result["status"]
                print(f" Payment Service ответил: {result['status']} для заказа {order_id}")
            else:
                print(f" Payment Service вернул ошибку {response.status_code}")
                new_order["status"] = "failed"
                
        except Exception as e:
            print(f" Ошибка соединения с Payment Service: {e}")
            new_order["status"] = "failed"
    
    
    orders[order_id] = new_order
    
   
    return new_order

@app.get("/orders/{order_id}")
async def get_order(order_id: int):
    """Посмотреть, что там с заказом"""
    if order_id in orders:
        return orders[order_id]
    else:
        return {"error": "Заказ не найден"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)