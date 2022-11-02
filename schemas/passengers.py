from pydantic import BaseModel, EmailStr


class Passenger(BaseModel):
    name:str
    contact:str
    email:EmailStr
    nationality:str

class PassengerCreate(Passenger):
    password:str


class ShowPassenger(Passenger):
    id:int
    class Config:
        orm_mode = True
