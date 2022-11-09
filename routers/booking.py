from fastapi import APIRouter, Depends, status, HTTPException
from schemas.booking import BookFlight, ShowBookedFlight
from database import get_db
from sqlalchemy.orm import Session
from crud_func.bookingfun import book_new_flight, get_booking, delete_booking_by_id, get_all_booking
from models.booking import Booking
from typing import List

router = APIRouter(tags = ['booking'])



@router.post("/booking", status_code=status.HTTP_201_CREATED)
def book_flight(obj: BookFlight, db: Session = Depends(get_db)):
    ref = book_new_flight(obj = obj, db=db)
    return "booking is not done yet... complete the payment first."


@router.get("/booking/{id}", response_model=ShowBookedFlight, status_code=status.HTTP_200_OK)
def get_booking_by_id(id:int , db: Session = Depends(get_db)):
    ref = get_booking(id = id, db=db)
    return ref

@router.get("/booking", response_model=List[ShowBookedFlight], status_code=status.HTTP_200_OK)
def get__all_booking(db: Session = Depends(get_db)):
    ref = get_all_booking(db=db)
    return ref


@router.delete("/booking/{id}" , response_model=ShowBookedFlight, status_code=status.HTTP_200_OK)
def delete_booking(id:int , db:Session= Depends(get_db)):
    obj = delete_booking_by_id(id=id, db=db)
    return obj