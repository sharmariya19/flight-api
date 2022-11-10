from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from jose import jwt
from models.user import User



def get_authorize(token:str, db:Session):
    payload = jwt.decode(token, "riya", "HS256")
    username = payload.get("sub")
    if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="unable to verify credentials")
    else:
        user = db.query(User).filter(User.email == username).first()
        if user.is_admin:
            return True
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not authorized")