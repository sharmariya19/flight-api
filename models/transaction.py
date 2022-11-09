from database import Base
from sqlalchemy import Column, Integer, ForeignKey, String


class Transaction(Base):
    __tablename__ = "transaction"
    
    id = Column(Integer, primary_key=True, index=True)
    passenger_id = Column(Integer, ForeignKey("passenger.id"))
    flight_route_id = Column(Integer, ForeignKey("flight_route.id"))
    transaction_id = Column(Integer, default = None)
    payment_mode = Column(String, nullable = False)
    coupon_status = Column(String, default = "Not Applied")
    paid_amount = Column(Integer, nullable = False, default=0)
    status = Column(String, default = "Not Booked")
