from fastapi import HTTPException, status
from schemas.booking import BookFlight
from sqlalchemy.orm import Session
from models.booking import Booking


def book_new_flight(obj: BookFlight, db: Session):
    new_booking = Booking(**obj.dict())
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking


def get_booking(id:int ,db: Session):
    obj = db.query(Booking).get(id)
    return obj

def delete_booking_by_id(id:int, db:Session):
    ref = db.query(Booking).get(id)
    if not ref:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Booking with id {id} not found"
        )
    else:
        db.delete(ref)
    db.commit()

    return ref