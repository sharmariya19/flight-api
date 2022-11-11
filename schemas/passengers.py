from pydantic import BaseModel, EmailStr


class Passenger(BaseModel):
    name:str
    email:EmailStr
    gender:str
    age:int
    contact:str
    nationality:str

class PassengerCreate(Passenger):
    password:str

class ShowPassenger(Passenger):
    id:int
    class Config:
        orm_mode = True
