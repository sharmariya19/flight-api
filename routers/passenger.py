from fastapi import APIRouter, Depends, status, HTTPException
from schemas.passengers import PassengerCreate, ShowPassenger
from database import get_db
from sqlalchemy.orm import Session
from crud_func.passengerfun import create_new_passenger, get_all_passengers, delete_passenger_by_id
from typing import List
from routers.login import oauth2_scheme
from crud_func.login import get_authorize

router = APIRouter(tags = ['passenger'])


@router.post("/passenger", status_code=status.HTTP_201_CREATED)
def create_passenger(passenger: PassengerCreate, db: Session = Depends(get_db)):
    new_passenger = create_new_passenger(passenger=passenger, db=db)
    return "passenger registered successfully"


@router.get("/passenger",response_model=List[ShowPassenger],status_code=status.HTTP_200_OK)
def get_passengers(db: Session = Depends(get_db), token:str=Depends(oauth2_scheme)):
    if get_authorize(token, db):
        ref = get_all_passengers(db=db)
        return ref
    
@router.delete("/passenger/{id}", status_code=status.HTTP_200_OK)
def delete_passenger(id:int , db:Session= Depends(get_db)):
    obj = delete_passenger_by_id(id=id, db=db)
    return f"passenger with id:{id} deleted successfully"