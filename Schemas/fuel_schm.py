from pydantic import BaseModel, ConfigDict , Field , field_validator
from typing import Literal , Optional

class FuelCreate(BaseModel):
    fuel_type : Literal["petrol" , "diesel" , "cng"]
    price_per_litter : float
    current_stock : float
    
    @field_validator("fuel_type", mode="before")
    @classmethod
    def clean_type(cls, value):
        if not isinstance(value, str):
            raise ValueError("type must be a string")
        return value.strip().lower()
    
    
class FuelUpdate(BaseModel):
    fuel_type: Optional[Literal["petrol", "diesel", "cng"]] = None
    price_per_litter: Optional[float] = None
    current_stock: Optional[float] = None
    
    
class FuelResponse(BaseModel):
    fuel_type : str
    price_per_litter : float
    current_stock : float
        
    model_config = ConfigDict(from_attributes=True)
            
            