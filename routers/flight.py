from fastapi import APIRouter, Depends, status, HTTPException
from schemas.flights import FlightCreate, ShowFlight
from database import get_db
from sqlalchemy.orm import Session
from crud_func.flightfun import create_new_flight, get_all_flights, delete_flight_by_id
from typing import List
from routers.login import oauth2_scheme
from crud_func.login import get_authorize

router = APIRouter( tags= ['flight'])


@router.post("/flight", status_code=status.HTTP_201_CREATED)
def create_flight(flight: FlightCreate, db: Session = Depends(get_db), token:str=Depends(oauth2_scheme)):
    if get_authorize(token,db):
        new_flight = create_new_flight(flight=flight, db=db)
        return f"successfully created flight "



@router.get( "/flight",response_model=List[ShowFlight],status_code=status.HTTP_200_OK)
def get_flights(db: Session = Depends(get_db)):
    ref = get_all_flights(db=db)
    return ref


@router.delete("/flight/{id}", status_code=status.HTTP_200_OK)
def delete_flight(id:int , db:Session= Depends(get_db), token:str=Depends(oauth2_scheme)):
    if get_authorize(token, db):
        obj = delete_flight_by_id(id=id, db=db)
        return f"successfully deleted flight with id:{id}"

