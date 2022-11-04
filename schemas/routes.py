from pydantic import BaseModel, EmailStr


class RouteCreate(BaseModel):
    source:str
    destination:str
    flight_id:int
    fare:int
    takeoff_time:str
    landing_time:str

class ShowRoute(RouteCreate):
    flight_name:str
    id:int
    class Config:
        orm_mode = True
