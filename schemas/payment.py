from pydantic import BaseModel

class CreatePayment(BaseModel):
    bank_name:str
    booking_id:int
    payment_mode:str

class ShowPayment(CreatePayment):
    id:int
    transaction_id:str
    paid_amount:int
    coupon_status:str
    class Config:
        orm_mode=True