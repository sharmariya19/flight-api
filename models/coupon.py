from database import Base
from sqlalchemy import Column, Integer, String, Date


class Coupon(Base):
    __tablename__ = "coupon"
    
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, nullable = False)
    value = Column(Integer, nullable = False)
    type = Column(String, nullable = False)
    min_cart_value = Column(Integer, nullable = False)
    max_discount = Column(Integer, nullable=False)
    issue_date = Column(Date, nullable= False)
    expiry_date = Column(Date, nullable=False)

