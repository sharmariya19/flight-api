from pydantic import BaseModel
from typing import Optional
from datetime import date

class BookFlight(BaseModel):
    passenger_id:int
    flight_route_id:int
    coupon_id:Optional[int] = None

class ShowBookedFlight(BaseModel):
    passenger:str
    airline_name:str
    source:str
    destination:str
    amount:int
    status:str
    ticket_issue_date:Optional[date] = None
    transaction_id:Optional[str] = None
    coupon_status:Optional[str] = None
    
    class Config:
        orm_mode = True
