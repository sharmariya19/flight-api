from fastapi import Depends, HTTPException, status
from schemas.payment import ShowPayment, CreatePayment
from sqlalchemy.orm import Session
from models.payment import Payment
from models.booking import Booking
import string, random
from crud_func.bookingfun import booking_done, get_amount



def create_new_payment(payment: CreatePayment, db: Session):
    booking = db.query(Booking).get(payment.booking_id)
    

    if booking.status == "Booked":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Payment already done for this booking")

    paid_amount,couponstatus = get_amount(booking, db)

    new_payment = Payment(
        bank_name = payment.bank_name,
        booking_id = payment.booking_id,
        payment_mode = payment.payment_mode,
        paid_amount = paid_amount,
        coupon_status = couponstatus,
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
