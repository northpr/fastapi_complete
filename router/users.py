from typing import List
from schemas import UserBase, UserDisplay
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user


router = APIRouter(
    prefix ='/user',
    tags = ['user']
)

# Crate User
@router.post('/', response_model=UserDisplay) # Create API Operation - allows us to call this from docus and allows user to use the function
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


# Read All User
@router.get('/', response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)

# Read One User
@router.get('/{id}', response_model=UserDisplay) # return only one user, don't need a list
def get_user(id: int, db: Session = Depends(get_db)):
    return db_user.get_user(db, id)

# Update User


# Delete User

