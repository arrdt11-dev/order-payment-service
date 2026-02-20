# ========== payment_service.py ==========


from fastapi import FastAPI  
from pydantic import BaseModel  
import uvicorn  


app = FastAPI()


class PaymentRequest(BaseModel):
    order_id: int    
    amount: float    

class PaymentResponse(BaseModel):
    status: str      

 

@app.post("/pay")
async def process_payment(request: PaymentRequest):
    print(f"  Payment Service получил запрос: заказ {request.order_id} на сумму {request.amount}")
    
    
    if request.amount > 0:
        print(f" Оплата заказа {request.order_id} успешна")
        return PaymentResponse(status="paid")
    else:
        print(f" Оплата заказа {request.order_id} отклонена")
        return PaymentResponse(status="failed")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)