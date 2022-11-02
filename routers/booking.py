from fastapi import APIRouter, Depends, status, HTTPException
from schemas.booking import BookFlight, ShowBookedFlight
from database import get_db
from sqlalchemy.orm import Session
from crud_func.booking_fun import book_new_flight, get_booking, delete_booking_by_id
from models.booking import Booking
from typing import List

router = APIRouter(tags = ['booking'])


@router.post(
    "/booking", response_model=ShowBookedFlight, status_code=status.HTTP_201_CREATED
)
def book_flight(obj: BookFlight, db: Session = Depends(get_db)):
    ref = book_new_flight(obj = obj, db=db)
    return ref


@router.get("/booking/{id}", response_model=ShowBookedFlight, status_code=status.HTTP_200_OK)
def get_booking_by_id(id:int , db: Session = Depends(get_db)):
    ref = get_booking(id = id, db=db)
    if not ref:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Booking with this id {id} does not exist")
    return ref


@router.delete("/booking/{id}" , response_model=ShowBookedFlight, status_code=status.HTTP_200_OK)
def delete_booking(id:int , db:Session= Depends(get_db)):
    obj = delete_booking_by_id(id=id, db=db)
    return obj