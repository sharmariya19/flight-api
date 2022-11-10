from pydantic import BaseModel
from typing import Optional

class FlightRoute(BaseModel):
    fare:int
    takeoff_time:str
    landing_time:str
    coupon_id:Optional[int] = None

class CreateFlightRoute(FlightRoute):
    flight_id:int
    route_id:int

class ShowFlightRoute(FlightRoute):
    id:int
    airline_name:str
    source:str
    destination:str
    available_seats:int
    class Config:
        orm_mode = True
