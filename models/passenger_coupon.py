from database import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.schema import PrimaryKeyConstraint


class PassengerCoupon(Base):
    __tablename__ = "passenger_coupon"
    
    coupon_id = Column(Integer, ForeignKey("coupon.id"))
    passenger_id = Column(Integer, ForeignKey("passenger.id"))
    __table_args__ = (
        PrimaryKeyConstraint(
            coupon_id,
            passenger_id),
        {})
