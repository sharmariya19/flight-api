from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Flight(Base):
    __tablename__ = "flight"
    
    id = Column(Integer, primary_key=True, index=True)
    start_loc = Column(String, nullable=False)
    end_loc = Column(String, nullable=False)
    flight_name = Column(String, nullable=False)
    coupon_id = Column(Integer, ForeignKey("coupon.id"), default= None)

