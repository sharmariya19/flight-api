from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models.user import User
from crud_func.userfun import create_new_user
from hashing import Hasher

router = APIRouter(tags= ['loogin'])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

@router.post("/token")
def retrieve_token(form_data:OAuth2PasswordRequestForm = Depends(), db:Session=Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username")

    if not Hasher.verify_password(form_data.password, user.hash_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid pssword")
    