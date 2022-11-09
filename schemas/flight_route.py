from pydantic import BaseModel


class CreateFlightRoute(BaseModel):
    flight_id:int
    route_id:int
    fare:int
    takeoff_time:str
    landing_time:str

class ShowFlightRoute(CreateFlightRoute):
    id:int
    class Config:
        orm_mode = True
