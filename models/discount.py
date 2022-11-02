from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Discount(Base):
    __tablename__ = "discount"
    
    id = Column(Integer, primary_key=True, index=True)
    discount_type = Column(String)
    discount = Column(Integer)

