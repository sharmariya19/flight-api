from fastapi import APIRouter, Depends, status, HTTPException
from schemas.flightroute import CreateFlightRoute, ShowFlightRoute
from database import get_db
from sqlalchemy.orm import Session
from crud_func.flightroutefun import get_flight_route, new_flight_route, delete_flight_route, get_all_flight_route
from typing import List
from routers.login import oauth2_scheme
from crud_func.login import get_authorize

router = APIRouter( tags= ['flightroute'])


@router.post("/flightroute", status_code=status.HTTP_201_CREATED)
def create_flightroute(flight: CreateFlightRoute, db: Session = Depends(get_db), token:str=Depends(oauth2_scheme)):
    if get_authorize(token, db):
        new_flight = new_flight_route(flight=flight, db=db)
        return "flight route created"



@router.get( "/flightroute",response_model=List[ShowFlightRoute],status_code=status.HTTP_200_OK)
def get_flightroute(db: Session = Depends(get_db)):
    ref = get_all_flight_route(db=db)
    return ref


@router.delete("/flightroute/{id}",status_code=status.HTTP_200_OK)
def delete_flightroute(id:int , db:Session= Depends(get_db), token:str=Depends(oauth2_scheme)):
    if get_authorize(token, db):
        obj = delete_flight_route(id=id, db=db)
        return "Successfully deleted"



@router.get("/route/{source}/{destination}",response_model = List[ShowFlightRoute],  status_code=status.HTTP_200_OK)
def get_flights(source:str, destination:str, db:Session = Depends(get_db)):
    obj = get_flight_route(source, destination, db)
    return obj