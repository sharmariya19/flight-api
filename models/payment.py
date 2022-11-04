from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class Payment(Base):
    __tablename__ = "payment"
    
    id = Column(Integer, primary_key=True, index=True)
    bank_name = Column(String, nullable  = False)
    booking_id = Column(Integer, ForeignKey("booking.id"))
    transaction_id = Column(String)
    payment_mode = Column(String, nullable = False)
    coupon_id = Column(Integer, ForeignKey("discount.id"), nullable=True)
    paid_amount = Column(Integer)
    coupon_status = Column(String, nullable = False, default = "not applied")
