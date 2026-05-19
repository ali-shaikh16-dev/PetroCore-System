import jwt
from fastapi import HTTPException , Request
    
from datetime import datetime , timezone , timedelta
from config import (
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES
)


#* ---------------------------------------------------------------------------------------------------

#* 1️⃣ SCOPE BASED MAPPING TOKEN 

SCOPE_MAPPING = {
    "owner" : ["read" , "write" , "delete" , "update"],
    "admin" : ["read" , "write" , "delete" , "update"],
    "worker" : ["read" , "write"]
}


def create_token(user):
    
    scope = SCOPE_MAPPING.get(user.role , [])
    
    # Token expiry time (.env se aayega)
    expire_time = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    # JWT payload
    payload = {
        "user_id": user.id,
        "user": user.username,
        "scope": scope,
        "role": user.role,
        "expire": int(expire_time.timestamp())
    }

    # Token generate
    token_gen = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
        
        
    return {"access_token" : token_gen}


#* ---------------------------------------------------------------------------------------------------


# def verify_token(security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)):
    
#     secret_key = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

#     payload = jwt.decode(token, secret_key , algorithms=["HS256"])

#     token_scopes = payload.get("scope", [])

#     for scope in security_scopes.scopes:
#         if scope not in token_scopes:
#             raise HTTPException(
#                 status_code=status.HTTP_401_UNAUTHORIZED,
#                 detail="SORRY YOU NOT ACCESS THIS"
#             )

#     return payload


#* ---------------------------------------------------------------------------------------------------


#* 2️⃣ ROLE BASED MAPPING TOKEN

def role_based_token(allowed_roles):

    def verify_role(request : Request): #* oauth2_scheme ki jagah Request use karenge
        
        
        #* Cookie se token nikaalo
        token  = request.cookies.get("access_token") 
        
        
        if not token:
            raise HTTPException(status_code=401,detail="Token not found")
        
        
        try:
            #* Token decode karo
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            
            
        #* Token validation 
        except jwt.PyJWTError:
            raise HTTPException(status_code=401, detail="Invalid token")
            

        #* Role check
        if payload["role"] not in allowed_roles:
            raise HTTPException(status_code=403, detail="Access Denied Sorry Your Worker")
        

        #* User data return karo
        return payload
    
    return verify_role

    
    
    