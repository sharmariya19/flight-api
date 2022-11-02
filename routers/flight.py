from fastapi import APIRouter, Depends, status, HTTPException
from schemas.flights import FlightCreate, ShowFlight
from database import get_db
from sqlalchemy.orm import Session
from crud_func.flight_fun import create_new_flight, get_all_flights, delete_flight_by_id
from typing import List
from models.flights import Flight

router = APIRouter( tags= ['flight'])


@router.post(
    "/flight", response_model=ShowFlight, status_code=status.HTTP_201_CREATED
)
def create_flight(flight: FlightCreate, db: Session = Depends(get_db)):
    new_flight = create_new_flight(flight=flight, db=db)
    return new_flight



@router.get( "/flight",response_model=List[ShowFlight],status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    ref = get_all_flights(db=db)
    return ref


@router.delete("/flight/{id}" , response_model=ShowFlight,status_code=status.HTTP_200_OK)
def delete_passenger(id:int , db:Session= Depends(get_db)):
    obj = delete_flight_by_id(id=id, db=db)
    # return {"msg": "Successfully deleted."}
    return obj

