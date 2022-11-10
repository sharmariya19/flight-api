from pydantic import BaseModel
from typing import Optional


class FlightCreate(BaseModel):
    airline_name:str
    serial_no:int
    type:str
    seats:int

class ShowFlight(FlightCreate):
    id:int
    class Config:
        orm_mode = True
