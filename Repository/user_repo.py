from requests import session
from sqlalchemy.orm import Session
from Model.user_table import User 
from Schemas.user_schm import UserCreate
from utils.pass_hash import hash_password
from fastapi import HTTPException , status


def user_create(db:Session, user : UserCreate , role = "worker"):
    create_user = User(**user.model_dump() , role=role)
    
    db.add(create_user)
    db.commit()
    db.refresh(create_user)
    return create_user


def get_user_by_username(db:Session , username:str):
    return db.query(User).filter(User.username == username).first()


def get_user_by_id(db:Session, id: int):
    return db.query(User).filter(User.id == id).first()


def get_phone_no(db:Session , phone : int):
    return db.query(User).filter(User.phone_number == phone).first()


def get_password(db:Session , password : str):
    return db.query(User).filter(User.password == password)


def update_user(db:Session, user_id: int, user: UserCreate):
    upd_user = db.query(User).filter(User.id == user_id).first()
    
    if not upd_user:
        raise HTTPException

    upd_user.username = user.username
    upd_user.phone_number = user.phone_number
    upd_user.password = hash_password(user.password)
    upd_user.role = user.role

    db.commit()
    db.refresh(upd_user)
    
    return upd_user
    

def delete_user(db:Session, user_id: int):
    delt_user = db.query(User).filter(User.id == user_id).first()
    if not delt_user:
        return False

    db.delete(delt_user)
    db.commit()
    return delt_user
    
       
        