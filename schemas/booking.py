from pydantic import BaseModel
from typing import Optional

class BookFlight(BaseModel):
    passenger_id:int
    flight_route_id:int

class ShowBookedFlight(BaseModel):
    passenger:str
    flight_name:str
    source:str
    destination:str
    status:str
    transaction_id:Optional[str] = None
    amount:int
    class Config:
        orm_mode = True
