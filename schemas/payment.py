from pydantic import BaseModel
from typing import Optional

class CreatePayment(BaseModel):
    booking_id:int
    payment_mode:str
    coupon_id : Optional[int] = None

class ShowPayment(CreatePayment):
    id:int
    paid_amount:int

    class Config:
        orm_mode=True