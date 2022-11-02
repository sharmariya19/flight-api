from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class Payment(Base):
    __tablename__ = "payment"
    
    id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer, ForeignKey("booking.id"))
    payment_mode = Column(String)
    coupon_id = Column(Integer, ForeignKey("discount.id"), nullable=True)
    paid_amount = Column(Integer)

