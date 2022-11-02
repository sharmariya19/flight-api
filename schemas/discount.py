from pydantic import BaseModel


class DiscountCreate(BaseModel):
    discount_type:str
    discount:int

class ShowDiscount(DiscountCreate):
    id:int
    class Config:
        orm_mode = True
