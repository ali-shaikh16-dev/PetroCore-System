from Repository.user_repo import get_user_by_username
from fastapi import HTTPException
from utils.pass_hash import verify_password 
from utils.jwt_token_work import create_token


#* { LOGIN PROCESS WORK - RETURN TOKEN ENOUGH }

def login_access(db, user_login):

    user_check = get_user_by_username(
        db,
        user_login.username
    )

    if not user_check:
        raise HTTPException(
            status_code=400,
            detail="Username not right"
        )

    password_check = verify_password(
        user_login.password,
        user_check.password
    )

    if not password_check:
        raise HTTPException(
            status_code=400,
            detail="Password wrong"
        )

    return create_token(user_check)










        
    