from fastapi import HTTPException, status
from schemas.booking import BookFlight, ShowBookedFlight
from sqlalchemy.orm import Session
from models.booking import Booking
from models.routes import Route
from models.flightroute import FlightRoute
from models.passengers import Passenger
from models.flights import Flight
from models.payment import Payment
from models.coupon import Coupon

def get_amount(booking:Booking , db: Session):
    status = "Not Applied"
    discount = 0
    flight_route = db.query(FlightRoute).get(booking.flight_route_id)
    flight = db.query(Flight).get(flight_route.flight_id)

    amount = flight_route.fare

    if flight.coupon_id:
        status = "Applied"
        obj = db.query(Coupon).get(flight.coupon_id)
        discount = obj.discount

    return amount - discount, status


def get_parameters(id:int, db:Session):
    obj = db.query(Booking).get(id)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Booking with id {id} does not exist")
    
    passenger = db.query(Passenger).get(obj.passenger_id)
    flight_route = db.query(FlightRoute).get(obj.flight_route_id)
    flight = db.query(Flight).get(flight_route.flight_id)
    route = db.query(Route).get(flight_route.route_id)
    payment = db.query(Payment).filter(id == Payment.booking_id).first()

    if payment:
        transaction_id = payment.transaction_id
    else:
        transaction_id = None

    booking = db.query(Booking).get(id)
    amount, coupon_status = get_amount(booking ,db)

    ref = ShowBookedFlight( passenger = passenger.name, 
        flight_name = flight.flight_name, 
        source = route.source ,
        destination = route.destination,
        status = obj.status , 
        transaction_id = transaction_id,
        amount = amount,
        coupon_status = coupon_status
    )
    return ref




def book_new_flight(obj: BookFlight, db: Session):
    new_booking = Booking(
        passenger_id = obj.passenger_id,
        flight_route_id = obj.flight_route_id
    )
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking



def get_booking(id:int ,db: Session):
    ref = get_parameters(id,db)

    return ref


def get_all_booking(db: Session):
    obj = db.query(Booking).all()
    lst = []
    
    for booking in obj:
        ref = get_parameters(booking.id, db)
        lst.append(ref)
    return lst


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

    obj = db.query(FlightRoute).get(ref.flight_route_id)
    obj.available_seats -= 1

    db.commit()
    db.refresh(ref)
    db.refresh(obj)