from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Route(Base):
    __tablename__ = "route"
    
    id = Column(Integer, primary_key=True, index=True)
    source = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    flight_id = Column(Integer,ForeignKey("flight.id"))
    flight_name = Column(String, nullable=False)
    fare = Column(Integer, nullable=False)
    takeoff_time =  Column(String, nullable=False)
    landing_time = Column(String, nullable=False)
