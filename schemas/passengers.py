from pydantic import BaseModel


class PassengerCreate(BaseModel):
    name:str
    gender:str
    age:int
    contact:str
    nationality:str

class ShowPassenger(PassengerCreate):
    id:int
    class Config:
        orm_mode = True
