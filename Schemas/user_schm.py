from pydantic import BaseModel , Field , ConfigDict , field_validator
from typing import Literal , Optional
from datetime import datetime

class UserCreate(BaseModel):
    username : str = Field(... , min_length=2 , max_length=45)
    phone_number : str = Field(..., min_length=10 , max_length=10)
    password : str = Field(... , min_length=6 , max_length=45)
    
    #! NEW LEARN
    @field_validator("username")
    @classmethod
    def clean_username(cls, value : str):
        return value.strip().lower()

    @field_validator("phone_number")
    @classmethod
    def clean_phone(cls, value : str):
        return value.strip()
    
    @field_validator("password")
    @classmethod
    def clean_password(cls, value : str):
        return value.strip()
    
    
    
class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=2, max_length=45)
    phone_number: Optional[str] = Field(None, min_length=10, max_length=10)
    password: Optional[str] = Field(None, min_length=6, max_length=45)
    role: Optional[Literal["owner", "admin", "worker"]] = None
    
    
    
class UserRoles(BaseModel):
    username : str = Field(... , min_length=2 , max_length=45)
    phone_number : str = Field(..., min_length=10 , max_length=10)
    password : str = Field(... , min_length=6 , max_length=45)
    role : Literal["owner", "admin", "worker"]
    
    
    
class UserResponse(BaseModel):
    username : str
    phone_number : str
    role : str
    created_at : datetime
    
    
    model_config = ConfigDict(from_attributes=True)
        

    