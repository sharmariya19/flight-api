from database import Base
from sqlalchemy import Column, Integer, String


class Route(Base):
    __tablename__ = "route"
    
    id = Column(Integer, primary_key=True, index=True)
    source = Column(String, nullable=False)
    destination = Column(String, nullable=False)
