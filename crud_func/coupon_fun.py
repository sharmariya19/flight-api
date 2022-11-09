from fastapi import HTTPException, status
from schemas.coupon import CouponCreate
from sqlalchemy.orm import Session
from models.coupon import Coupon


def create_new_coupon(obj: CouponCreate, db: Session):
    new_coupon = Coupon(**obj.dict())
    db.add(new_coupon)
    db.commit()
    db.refresh(new_coupon)
    return new_coupon


def get_all_coupon(db: Session):
    obj = db.query(Coupon).all()
    return obj

def delete_coupon_by_id(id:int, db:Session):
    ref = db.query(Coupon).get(id)
    if not ref:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Coupon with id {id} not found"
        )
    else:
        db.delete(ref)
    db.commit()

    return ref