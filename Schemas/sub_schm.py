from pydantic import BaseModel , Field , ConfigDict , field_validator
from datetime import datetime

class SubscriptionCreate(BaseModel):
    plan_price : float = Field(..., gt=0)
    start_date : datetime
    end_date : datetime
    status : str
    
    @field_validator("status")
    @classmethod()
    def status_valida(cls , value : str):
        return value.strip().lower()

class SubscriptionResponse(BaseModel):
    plan_price : float
    start_date : datetime
    end_date : datetime
    status : str

    model_config = ConfigDict(from_attributes=True)