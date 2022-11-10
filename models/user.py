from database import Base
from sqlalchemy import Column, Integer, String, Boolean


class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    hash_password = Column(String, nullable=False)
    is_admin = Column(Boolean, default = False)

