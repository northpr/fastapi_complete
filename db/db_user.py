from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser
from db.hash import Hash

def create_user(db: Session, request: UserBase): # create functionality to write to database
    new_user = DbUser(
        username = request.username,
        email = request.email,
        password = Hash.bcrpyt(request.password) # need to hash so we will create a new file (check hash.py)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db: Session):
    return db.query(DbUser).all()

def get_user(db: Session, id:int):
    return db.query(DbUser).filter(DbUser.id == id).first() # return id that we get and show the first one
