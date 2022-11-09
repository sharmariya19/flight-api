from pydantic import BaseModel


class BookFlight(BaseModel):
    passenger_id:int
    flight_route_id:int

class ShowBookedFlight(BookFlight):
    id:int
    status:str
    class Config:
        orm_mode = True
