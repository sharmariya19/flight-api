from database import Base
from sqlalchemy import Column, Integer, ForeignKey, String


class Booking(Base):
    __tablename__ = "booking"
    
    id = Column(Integer, primary_key=True, index=True)
    passenger_id = Column(Integer, ForeignKey("passenger.id"))
    flight_route_id = Column(Integer, ForeignKey("flight_route.id"))
    status = Column(String, default = "Not Booked")
    
