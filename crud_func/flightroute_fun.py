from fastapi import HTTPException, status
from schemas.flight_route import CreateFlightRoute
from sqlalchemy.orm import Session
from models.flight_route import FlightRoute


def new_flight_route(flight: CreateFlightRoute, db: Session):
    new_flight = FlightRoute(**flight.dict())
    db.add(new_flight)
    db.commit()
    db.refresh(new_flight)
    return new_flight


def get_flight_route(db: Session):
    obj = db.query(FlightRoute).all()
    return obj

def delete_flight_route(id:int, db:Session):
    ref = db.query(FlightRoute).get(id)
    if not ref:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Flight with id {id} not found"
        )
    else:
        db.delete(ref)
    db.commit()

    return ref
