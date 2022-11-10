from pydantic import BaseModel, EmailStr


class CreateUser(BaseModel):
    name:str
    email:EmailStr
    password:str
    is_admin:bool
    

class ShowUser(BaseModel):
    id:int
    name:str
    email:EmailStr
    class Config:
        orm_mode = True
