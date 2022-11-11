from pydantic import BaseModel
from datetime import date


class CouponCreate(BaseModel):
    code:str
    value:int
    type:str
    min_cart_value: int
    max_discount: int
    issue_date: date
    expiry_date: date

class ShowCoupon(CouponCreate):
    id:int
    class Config:
        orm_mode = True
