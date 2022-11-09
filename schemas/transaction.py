from pydantic import BaseModel

class CreateTransaction(BaseModel):
    passenger_id:int
    flight_route_id:int
    payment_mode:str
    

class ShowTransaction(CreateTransaction):
    id:int
    transaction_id:int
    paid_amount:int
    coupon_status:str
    status:str
    class Config:
        orm_mode=True