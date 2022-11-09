from pydantic import BaseModel


class BookFlight(BaseModel):
    passenger_id:int
    flight_route_id:int

class ShowBookedFlight(BaseModel):
    passenger:str
    flight_name:str
    source:str
    destination:str
    status:str
    transaction_id:str
    amount:int
    class Config:
        orm_mode = True
