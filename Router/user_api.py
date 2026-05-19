from fastapi import Depends , APIRouter, FastAPI , HTTPException , status

from requests import session
from sqlalchemy.orm import Session
from Database.db_connect import get_db

from Schemas.user_schm import UserCreate

from Model.fuel_table import Fuel
from Schemas.user_schm import UserCreate , UserResponse , UserUpdate

from Repository.user_repo import get_user_by_id , delete_user
from utils.jwt_token_work import role_based_token
from Model.user_table import User

owner_admin_only = Depends(role_based_token(["admin" , "owner"]))

#* ROOM 4 Work for user
router = APIRouter()


#! GET ROUTE
@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db), _ = owner_admin_only):

    user = get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user



@router.get("/", response_model=list[UserResponse])
def fecth_all_user(db : session = Depends(get_db), _ = owner_admin_only):
    return db.query(User).all()


  

#! UPDATE ROUTE
@router.patch("/{user_id}", response_model=UserResponse)
def change_user_detials(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db) , _ = owner_admin_only):
    
    #* GET user IN DATABASE
    user = db.query(User).filter(User.id == user_id).first()
    
    
    #* VALIDATION FURL
    if not user:
        raise HTTPException(status.HTTP_204_NO_CONTENT , detail="User Not Found")
    
    
    #* CONVERT PYDANTIC OBJECT IN DICT
    update_user = user_data.model_dump(exclude_unset=True)
    
    
    #* KEY VALUE PARIS
    for key , value  in update_user.items():
        
        #* SET KEY VALUE
         setattr(user , key , value)
         
         
         
    #* SAVE IN DATABASE
    db.commit()
    db.refresh(user)
    
    return user


    
#! DELETE ROUTE
@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: int, db: Session = Depends(get_db),_ = owner_admin_only):
    
    user = get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sorry User not found"
        )

    delete_user(db, user_id)

    return user

