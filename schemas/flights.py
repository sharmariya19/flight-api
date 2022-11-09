from pydantic import BaseModel
from typing import Optional


class FlightCreate(BaseModel):
    start_loc:str
    end_loc:str
    flight_name:str
    coupon_id: Optional[int] = None

class ShowFlight(FlightCreate):
    id:int
    class Config:
        orm_mode = True
