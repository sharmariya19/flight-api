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
from models.passenger_coupon import PassengerCoupon
import datetime

def get_amount(booking:Booking , db: Session):
    ref = db.query(PassengerCoupon).filter(booking.passenger_id == PassengerCoupon.passenger_id, booking.coupon_id == PassengerCoupon.coupon_id).first()
    if ref:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail="You have already used this coupon")
    
    couponstatus = "Not Applied"
    discount = 0
    flight_route = db.query(FlightRoute).get(booking.flight_route_id)
    amount = flight_route.fare

      
    if booking.coupon_id:
        obj = db.query(Coupon).get(booking.coupon_id)
        if not obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Coupon does not exist")
        if amount < obj.min_cart_value:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = f"Coupon can be applied only at min value of {obj.min_cart_value}")
      
        if obj.type == "PERCENT":
            discount = amount*(obj.value/100)
        else:
            discount = obj.value

        discount = min(discount, obj.max_discount)

        couponstatus = "Applied"

    return amount - discount, couponstatus


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
        airline_name = flight.airline_name, 
        source = route.source ,
        destination = route.destination,
        ticket_issue_date=obj.ticket_issue_date,
        status = obj.status, 
        transaction_id = transaction_id,
        amount = amount,
        coupon_status = coupon_status
    )
    return ref




def book_new_flight(obj: BookFlight, db: Session):
    amount , status = get_amount(obj, db)
    new_booking = Booking(**obj.dict())
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking, amount



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
    ref.ticket_issue_date = datetime.date.today()
    obj = db.query(FlightRoute).get(ref.flight_route_id)
    obj.available_seats -= 1
    if ref.coupon_id:

        new_obj = PassengerCoupon(
            coupon_id = ref.coupon_id,
            passenger_id = ref.passenger_id
        )
        db.add(new_obj)
    db.commit()
    db.refresh(ref)
    db.refresh(obj)