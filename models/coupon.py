from database import Base
from sqlalchemy import Column, Integer, String


class Coupon(Base):
    __tablename__ = "coupon"
    
    id = Column(Integer, primary_key=True, index=True)
    discount_type = Column(String, nullable = False)
    discount = Column(Integer, nullable = False)

