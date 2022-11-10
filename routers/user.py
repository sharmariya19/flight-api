from fastapi import APIRouter, Depends, status, HTTPException
from schemas.user import CreateUser, ShowUser
from database import get_db
from sqlalchemy.orm import Session
from crud_func.userfun import create_new_user, get_all_users
from typing import List
from routers.login import oauth2_scheme

router = APIRouter(tags = ['user'])


@router.post("/user", status_code=status.HTTP_201_CREATED)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    new_user = create_new_user(user=user, db=db)
    return "user created successfully"



@router.get("/user",response_model=List[ShowUser],status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db), token:str=Depends(oauth2_scheme)):
    ref = get_all_users(db=db)
    return ref
