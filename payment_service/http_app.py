from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PaymentRequest(BaseModel):
    order_id: int
    amount: float

@app.post("/pay")
def pay(request: PaymentRequest):
    if request.amount > 0:
        return {"status": "paid"}
    return {"status": "failed"}
