from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Flight(Base):
    __tablename__ = "flight"
    
    id = Column(Integer, primary_key=True, index=True)
    airline_name = Column(String, nullable=False)
    serial_no = Column(Integer, nullable=False)
    type = Column(String, nullable=False)
    seats = Column(Integer, nullable=False)