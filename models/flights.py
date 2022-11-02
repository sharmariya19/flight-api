from database import Base
from sqlalchemy import Column, Integer, String, Boolean


class Flight(Base):
    __tablename__ = "flight"
    
    id = Column(Integer, primary_key=True, index=True)
    start_loc = Column(String, nullable=False)
    end_loc = Column(String, nullable=False)
    flight_name = Column(String, nullable=False)
    no_of_seats = Column(String, nullable=False)
    day = Column(String, nullable=False)
