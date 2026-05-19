from pydantic import BaseModel, ConfigDict , Field , field_validator
from typing import Literal
from datetime import datetime

class SaleCreate(BaseModel):
    fuel_id : int = Field(... , gt=0)
    amount : float = Field(... , gt=0)
    payment_method : Literal["cash" , "card" , "upi"]
    
    @field_validator("payment_method", mode="before")
    @classmethod
    def clean_payment(cls, value):
     if isinstance(value, str): #! NEW LEARN
        return value.strip().lower()
     return value
    
class SaleResponse(BaseModel):
    fuel_id : int
    user_id : int
    liters : float
    price_per_litter : float
    amount : float
    payment_method : str
    created_at : datetime
    
    model_config = ConfigDict(from_attributes=True)