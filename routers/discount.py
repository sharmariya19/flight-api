from fastapi import APIRouter, Depends, status, HTTPException
from schemas.discount import DiscountCreate, ShowDiscount
from database import get_db
from sqlalchemy.orm import Session
from crud_func.discount_fun import create_new_discount,get_all_discount,delete_discount_by_id
from models.discount import Discount
from typing import List

router = APIRouter(tags = ['discount'])


@router.post(
    "/discount", response_model=ShowDiscount, status_code=status.HTTP_201_CREATED
)
def create_discount(obj:DiscountCreate, db: Session = Depends(get_db)):
    ref = create_new_discount(obj = obj, db=db)
    return ref


@router.get("/discount", response_model=List[ShowDiscount], status_code=status.HTTP_200_OK)
def get_discount(db: Session = Depends(get_db)):
    ref = get_all_discount(db=db)
    return ref


@router.delete("/discount/{id}" , response_model=ShowDiscount, status_code=status.HTTP_200_OK)
def delete_discount(id:int , db:Session= Depends(get_db)):
    obj = delete_discount_by_id(id=id, db=db)
    return obj