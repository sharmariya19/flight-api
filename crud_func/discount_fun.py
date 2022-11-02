from fastapi import HTTPException, status
from schemas.discount import DiscountCreate
from sqlalchemy.orm import Session
from models.discount import Discount


def create_new_discount(obj: DiscountCreate, db: Session):
    new_discount = Discount(**obj.dict())
    db.add(new_discount)
    db.commit()
    db.refresh(new_discount)
    return new_discount


def get_all_discount(db: Session):
    obj = db.query(Discount).all()
    return obj

def delete_discount_by_id(id:int, db:Session):
    ref = db.query(Discount).get(id)
    if not ref:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Discount with id {id} not found"
        )
    else:
        db.delete(ref)
    db.commit()

    return ref