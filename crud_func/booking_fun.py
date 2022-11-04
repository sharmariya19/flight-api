from fastapi import HTTPException, status
from schemas.booking import BookFlight
from sqlalchemy.orm import Session
from models.booking import Booking
from models.routes import Route
from models.flights import Flight


def book_new_flight(obj: BookFlight, db: Session):
    ref = db.query(Route).get(obj.route_id)
    flight = db.query(Flight).get(ref.flight_id)
    flightname = flight.flight_name
    new_booking = Booking(
        passenger_id = obj.passenger_id,
        route_id = obj.route_id,
        flight_name = flightname
    )
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

def booking_done(id:int, db:Session):
    ref = db.query(Booking).get(id)
    ref.status = "Booked"

    db.commit()
    db.refresh(ref)
    return ref