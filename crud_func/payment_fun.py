from fastapi import Depends
from schemas.payment import ShowPayment, CreatePayment
from sqlalchemy.orm import Session
from models.payment import Payment
from models.coupon import Coupon
from models.flight_route import FlightRoute
from models.flights import Flight
from models.booking import Booking
import string, random
from crud_func.booking_fun import booking_done
from database import get_db


def create_new_payment(payment: CreatePayment, db: Session):
    status = "Not Applied"
    discount = 0
    booking = db.query(Booking).get(payment.booking_id)
    flight_route = db.query(FlightRoute).get(booking.flight_route_id)
    flight = db.query(Flight).get(flight_route.flight_id)

    amount = flight_route.fare

    if flight.coupon_id:
        status = "Applied"
        obj = db.query(Coupon).get(flight.coupon_id)
        discount = obj.discount
    
    new_payment = Payment(
        bank_name = payment.bank_name,
        booking_id = payment.booking_id,
        payment_mode = payment.payment_mode,
        paid_amount = amount - discount,
        coupon_status = status,
        transaction_id = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=10))
        )

    booking_done (payment.booking_id, db)

    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return new_payment


def get_payment_by_id(id:int ,db: Session):
    obj = db.query(Payment).get(id)
    return obj
