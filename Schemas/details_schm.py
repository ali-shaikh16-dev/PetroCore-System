from pydantic import BaseModel, Field , field_validator
from typing import Optional
from datetime import datetime


#* =========================
# Create Schema
#* =========================

class ProfileCreate(BaseModel):
    user_id : int
    Fullname: str = Field(..., min_length=2, max_length=100)
    address: str = Field(..., min_length=5, max_length=255)
    pincode: int
    aadhar_id: str = Field(..., min_length=12, max_length=12)

    designation: str = Field(..., min_length=2, max_length=100)
    salary: float
    bonus: float = 0.0

    joining_date: datetime
    
    #! NEW LEARN
    @field_validator("Fullname")
    @classmethod
    def clean_name(cls, value : str):
        return value.strip().lower()

    @field_validator("address")
    @classmethod
    def clean_address(cls, value : str):
        return value.strip().lower()
    
    @field_validator("designation")
    @classmethod
    def clean_designation(cls, value : str):
        return value.strip().lower()


#* =========================
# Update Schema (PATCH)
#* =========================

class ProfileUpdate(BaseModel):
    Fullname : Optional[str] = Field(None, min_length=2, max_length=100)
    address: Optional[str] = Field(None, min_length=5, max_length=255)
    pincode: Optional[int] = None
    aadhar_id: Optional[str] = Field(None, min_length=12, max_length=12)

    designation: Optional[str] = Field(None, min_length=2, max_length=100)
    salary: Optional[float] = None
    bonus: Optional[float] = None

    joining_date: Optional[datetime] = None
    
    
    @field_validator("Fullname")
    @classmethod
    def clean_name_value(cls, value : str):
        return value.strip().lower()

    @field_validator("address")
    @classmethod
    def clean_address_value(cls, value : str):
        return value.strip().lower()
    
    @field_validator("designation")
    @classmethod
    def clean_designation_value(cls, value : str):
        return value.strip().lower()


#* =========================
# Response Schema
#* =========================
class ProfileResponse(BaseModel):
    id: int
    user_id: int

    Fullname: str
    address: str
    pincode: int
    aadhar_id: str

    designation: str
    salary: float
    bonus: float

    joining_date: datetime

    class Config:
        from_attributes = True