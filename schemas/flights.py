from pydantic import BaseModel


class FlightCreate(BaseModel):
    start_loc:str
    end_loc:str
    flight_name:str
    no_of_seats:int
    day:str

class ShowFlight(FlightCreate):
    id:int
    class Config:
        orm_mode = True
