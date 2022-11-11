from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Payment(Base):
    __tablename__ = "payment"
    
    id = Column(Integer, primary_key=True, index=True)
    bank_name = Column(String, nullable  = False)
    booking_id = Column(Integer, ForeignKey("booking.id"), unique = True)
    transaction_id = Column(String, default= None)
    payment_mode = Column(String, nullable = False)
    paid_amount = Column(Integer, nullable = False, default=0)
    coupon_status = Column(String, default = "Not Applied")
