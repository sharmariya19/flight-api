from fastapi import HTTPException, status
from schemas.user import CreateUser
from sqlalchemy.orm import Session
from models.user import User
from hashing import Hasher


def create_new_user(user: CreateUser, db: Session):
    # obj = db.query(User).filter(User.email==user.email)
    # if obj:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with this email already exist")
    new_user = User(
        name = user.name,
        email = user.email,
        hash_password = Hasher.get_password_hash(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_users(db: Session):
    obj = db.query(User).all()
    return obj
