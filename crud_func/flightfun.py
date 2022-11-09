from fastapi import HTTPException, status
from schemas.flights import FlightCreate
from sqlalchemy.orm import Session
from models.flights import Flight


def create_new_flight(flight: FlightCreate, db: Session):
    new_flight = Flight(**flight.dict())
    db.add(new_flight)
    db.commit()
    db.refresh(new_flight)
    return new_flight


def get_all_flights(db: Session):
    obj = db.query(Flight).all()
    return obj

def delete_flight_by_id(id:int, db:Session):
    ref = db.query(Flight).get(id)
    if not ref:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Flight with id {id} not found"
        )
    else:
        db.delete(ref)
    db.commit()

    return ref
