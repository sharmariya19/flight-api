from fastapi import APIRouter, Depends, status, HTTPException
from schemas.payment import CreatePayment, ShowPayment
from database import get_db
from sqlalchemy.orm import Session
from crud_func.paymentfun import create_new_payment, get_payment_by_id
from typing import List

router = APIRouter(tags = ['payment'])


@router.post("/payment", status_code=status.HTTP_201_CREATED)
def create_paymenet(payment: CreatePayment, db: Session = Depends(get_db)):
    new_payment = create_new_payment(payment = payment, db=db)
    return "Payment is done... Check the booking status."



@router.get("/payment/{id}", response_model=ShowPayment, status_code=status.HTTP_200_OK)
def get_payment(id:int ,db: Session = Depends(get_db)):
    ref = get_payment_by_id(id=id,db=db)
    return ref

