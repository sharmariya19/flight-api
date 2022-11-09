from pydantic import BaseModel


class CouponCreate(BaseModel):
    discount_type:str
    discount:int

class ShowCoupon(CouponCreate):
    id:int
    class Config:
        orm_mode = True
