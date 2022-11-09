from pydantic import BaseModel


class RouteCreate(BaseModel):
    source:str
    destination:str

class ShowRoute(RouteCreate):
    id:int
    class Config:
        orm_mode = True
