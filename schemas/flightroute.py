from pydantic import BaseModel

class FlightRoute(BaseModel):
    fare:int
    takeoff_time:str
    landing_time:str
    available_seats : int

class CreateFlightRoute(FlightRoute):
    flight_id:int
    route_id:int

class ShowFlightRoute(FlightRoute):
    id:int
    flight_name:str
    source:str
    destination:str
    class Config:
        orm_mode = True
