from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class FlightRoute(Base):
    __tablename__ = "flight_route"
    
    id = Column(Integer, primary_key=True, index=True)
    flight_id = Column(Integer,ForeignKey("flight.id"))
    route_id = Column(Integer, ForeignKey("route.id"))
    fare = Column(Integer, nullable=False)
    takeoff_time =  Column(String, nullable=False)
    landing_time = Column(String, nullable=False)
    coupon_id = Column(Integer, ForeignKey("coupon.id"), nullable= True)
    available_seats = Column(Integer, nullable= False)