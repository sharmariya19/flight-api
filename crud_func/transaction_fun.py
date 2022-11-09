from fastapi import HTTPException, status
from schemas.booking import BookFlight
from sqlalchemy.orm import Session
from models.flights import Flight
from models.flight_route import FlightRoute
from models.coupon import Coupon
from models.transaction import Transaction

import string, random


def book_new_flight(obj: BookFlight, db: Session):
    coupon_status = "Not Applied"
    discount = 0
    ref = db.query(FlightRoute).get(obj.flight_route_id)
    flight = db.query(Flight).get(ref.flight_id)
    coupon = flight.coupon_id

    amount = ref.fare


    

    if coupon :
        coupon_status = "Applied"
        discount = coupon.discount


    new_booking = Transaction(
        passenger_id = obj.passenger_id,
        flight_route_id = obj.flight_route_id,
        payment_mode = obj.payment_mode,
        transaction_id = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=10)),
        paid_amount = amount - discount,
        coupon_status = coupon_status,
        status = "Boooked"

        
    )
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking


def get_booking(id:int ,db: Session):
    obj = db.query(Transaction).get(id)
    return obj

def delete_booking_by_id(id:int, db:Session):
    ref = db.query(Transaction).get(id)
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