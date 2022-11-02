from pydantic import BaseModel


class BookFlight(BaseModel):
    user_id:int
    route_id:int
    price:int
    flight_name:str

class ShowBookedFlight(BookFlight):
    flight_name:str
    id:int
    class Config:
        orm_mode = True
