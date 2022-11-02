from fastapi import APIRouter, Depends, status, HTTPException
from schemas.passengers import PassengerCreate, ShowPassenger
from database import get_db
from sqlalchemy.orm import Session
from crud_func.passenger_fun import create_new_passenger, get_all_passengers, delete_passenger_by_id
from typing import List
from models.passengers import Passenger

router = APIRouter(tags = ['passenger'])


@router.post(
    "/passenger", response_model=ShowPassenger, status_code=status.HTTP_201_CREATED
)
def create_passenger(passenger: PassengerCreate, db: Session = Depends(get_db)):
    new_passenger = create_new_passenger(passenger=passenger, db=db)
    return new_passenger



@router.get(
    "/passenger",
    response_model=List[ShowPassenger],
    status_code=status.HTTP_200_OK,
)
def get_passengers(db: Session = Depends(get_db)):
    ref = get_all_passengers(db=db)
    return ref


@router.delete("/passenger/{id}" , response_model=ShowPassenger,status_code=status.HTTP_200_OK)
def delete_passenger(id:int , db:Session= Depends(get_db)):
    obj = delete_passenger_by_id(id=id, db=db)
    return obj