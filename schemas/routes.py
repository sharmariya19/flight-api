from pydantic import BaseModel, EmailStr


class RouteCreate(BaseModel):
    source:str
    destination:str
    flight_id:int

class ShowRoute(RouteCreate):
    id:int
    class Config:
        orm_mode = True
