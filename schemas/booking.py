from pydantic import BaseModel


class BookFlight(BaseModel):
    passenger_id:int
    route_id:int

class ShowBookedFlight(BookFlight):
    id:int
    flight_name:str
    status:str
    class Config:
        orm_mode = True
