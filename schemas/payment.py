from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CreatePayment(BaseModel):
    bank_name:str
    booking_id:int
    payment_mode:str
    coupon_id : Optional[int] = None

class ShowPayment(CreatePayment):
    id:int
    transaction_id:str
    paid_amount:int
    coupon_status:str
    class Config:
        orm_mode=True