"""FinPay backend - simple FastAPI service"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="FinPay API")

class Payment(BaseModel):
    id: int
    sender: str
    receiver: str
    amount: float
    currency: str = "USD"

# In‑memory store (for demo purposes)
payments: List[Payment] = []

@app.get("/payments", response_model=List[Payment])
async def list_payments():
    return payments

@app.post("/payments", response_model=Payment)
async def create_payment(p: Payment):
    # Simple duplicate check
    if any(p.id == existing.id for existing in payments):
        raise HTTPException(status_code=400, detail="Payment with this ID already exists")
    payments.append(p)
    return p

@app.get("/payments/{payment_id}", response_model=Payment)
async def get_payment(payment_id: int):
    for p in payments:
        if p.id == payment_id:
            return p
    raise HTTPException(status_code=404, detail="Payment not found")

@app.delete("/payments/{payment_id}")
async def delete_payment(payment_id: int):
    global payments
    payments = [p for p in payments if p.id != payment_id]
    return {"detail": "Deleted"}
