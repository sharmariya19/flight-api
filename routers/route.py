from fastapi import APIRouter, Depends, status, HTTPException
from schemas.routes import RouteCreate, ShowRoute
from database import get_db
from sqlalchemy.orm import Session
from crud_func.route_fun import create_new_route, get_all_routes, delete_route_by_id
from typing import List
from models.routes import Route

router = APIRouter(tags = ['route'])


@router.post(
    "/route", status_code=status.HTTP_201_CREATED
)
def create_route(route: RouteCreate, db: Session = Depends(get_db)):
    new_route = create_new_route(route = route, db=db)
    return f"Successfully created route from {new_route.source} to {new_route.destination}"



@router.get("/route", response_model=List[ShowRoute], status_code=status.HTTP_200_OK)
def get_routes(db: Session = Depends(get_db)):
    ref = get_all_routes(db=db)
    return ref


@router.delete("/route/{id}" , response_model=ShowRoute, status_code=status.HTTP_200_OK)
def delete_route(id:int , db:Session= Depends(get_db)):
    obj = delete_route_by_id(id=id, db=db)
    return f"successfully deleted route from {obj.source} to {obj.destination}"
