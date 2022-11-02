from database import Base
from sqlalchemy import Column, Integer, ForeignKey, String


class Booking(Base):
    __tablename__ = "booking"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("passenger.id"))
    route_id = Column(Integer, ForeignKey("route.id"))
    price = Column(Integer)
    flight_name = Column(String)
