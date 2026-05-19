from fastapi import Depends , APIRouter , HTTPException , status

from sqlalchemy.orm import Session
from Database.db_connect import get_db

from Schemas.user_schm import UserCreate

from Service.login_service import login_access

from fastapi import Response

from Schemas.user_schm import UserCreate , UserResponse , UserRoles

from Repository.user_repo import user_create
from utils.jwt_token_work import role_based_token

#* ROOM 1 work for AUTH - login and signup
router = APIRouter()


signup_owner_admin = Depends(role_based_token(["admin" , "owner"]))


#*signup ROUTE
@router.post("/signup" , response_model=UserResponse)
def create_new_account(user : UserRoles , db: Session = Depends(get_db) , _ = signup_owner_admin):
    return user_create(db , user) 
    
        
 
#*login ROUTE    
@router.post("/login") 
def login_account(user_login : UserCreate , response : Response , db:Session = Depends(get_db)):
    
    result = login_access(db , user_login)
    
    token = result["access_token"]
    

    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True
    )
    
    return {"message" : "Login Successfully"}


