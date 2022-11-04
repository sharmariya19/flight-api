from fastapi import Depends
from schemas.payment import ShowPayment, CreatePayment
from sqlalchemy.orm import Session
from models.payment import Payment
from models.discount import Discount
from models.routes import Route
import string, random
from crud_func.booking_fun import booking_done
from database import get_db


def create_new_payment(payment: CreatePayment, db: Session):
    status = "Not Applied"
    discount = 0
    ref = db.query(Route).get(payment.booking_id)
    amount = ref.fare
    if payment.coupon_id:
        status = "Applied"
        obj = db.query(Discount).get(payment.coupon_id)
        discount = obj.discount
    
    new_payment = Payment(
        bank_name = payment.bank_name,
        booking_id = payment.booking_id,
        payment_mode = payment.payment_mode,
        coupon_id = payment.coupon_id,
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

