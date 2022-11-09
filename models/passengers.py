from database import Base
from sqlalchemy import Column, Integer, String


class Passenger(Base):
    __tablename__ = "passenger"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    gender = Column(String)
    age = Column(Integer)
    contact = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    hash_password = Column(String, nullable=False)
    nationality = Column(String, nullable=False)

