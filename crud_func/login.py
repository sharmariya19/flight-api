from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from jose import jwt



def get_authorize(token:str, db:Session):
    payload = jwt.decode(token, "riya", "HS256")
    username = payload.get("sub")
    if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="unable to verify credentials")
    else:
        if username == "riya@gkm.com":
            return True
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not authorized")