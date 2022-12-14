from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models.passengers import Passenger
from hashing import Hasher
from jose import jwt

router = APIRouter(tags= ['login'])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

@router.post("/token")
def retrieve_token(form_data:OAuth2PasswordRequestForm = Depends(), db:Session=Depends(get_db)):
    user = db.query(Passenger).filter(Passenger.email == form_data.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username")

    if not Hasher.verify_password(form_data.password, user.hash_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")


    data = {"sub":form_data.username}
    jwt_token = jwt.encode(data,"riya", algorithm="HS256")

    return {"access_token":jwt_token, "token_type":"bearer"}



