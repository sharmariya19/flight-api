from fastapi import HTTPException, status
from schemas.payment import ShowPayment, CreatePayment
from sqlalchemy.orm import Session
from models.payment import Payment
from models.discount import Discount
from models.booking import Booking


def create_new_payment(payment: CreatePayment, db: Session):
    discount = 0
    ref = db.query(Booking).get(payment.booking_id)
    amount = ref.price
    if payment.coupon_id:
        obj = db.query(Discount).get(payment.coupon_id)
        discount = obj.discount
    # payment.paid_amount = discount
    new_payment = Payment(
        booking_id = payment.booking_id,
        payment_mode = payment.payment_mode,
        coupon_id = payment.coupon_id,
        paid_amount = amount - discount)
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return new_payment


def get_payment_by_id(id:int ,db: Session):
    obj = db.query(Payment).get(id)
    return obj

