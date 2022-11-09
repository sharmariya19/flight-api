from fastapi import APIRouter, Depends, status, HTTPException
from schemas.coupon import CouponCreate, ShowCoupon
from database import get_db
from sqlalchemy.orm import Session
from crud_func.couponfun import create_new_coupon, delete_coupon_by_id, get_all_coupon
from models.coupon import Coupon
from typing import List

router = APIRouter(tags = ['coupon'])


@router.post("/coupon", status_code=status.HTTP_201_CREATED)
def create_coupon(obj:CouponCreate, db: Session = Depends(get_db)):
    ref = create_new_coupon(obj = obj, db=db)
    return "new coupon created"


@router.get("/coupon", response_model=List[ShowCoupon], status_code=status.HTTP_200_OK)
def get_coupon(db: Session = Depends(get_db)):
    ref = get_all_coupon(db=db)
    return ref


@router.delete("/coupon/{id}", status_code=status.HTTP_200_OK)
def delete_coupon(id:int , db:Session= Depends(get_db)):
    obj = delete_coupon_by_id(id=id, db=db)
    return f"coupon with id:{id} successfully deleted"