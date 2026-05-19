# Router/sale_api.py

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from Database.db_connect import get_db
from Schemas.sale_schm import SaleCreate, SaleResponse
from Service.sale_service import create_sale_service
from utils.jwt_token_work import role_based_token
from Repository.sale_repo import get_all_sales


#* ROOM 3 Work for sale
router = APIRouter()

#* Worker aur Owner dono sale create kar sakte hain
employee_only = Depends(role_based_token(["worker", "owner" , "admin"]))

#! CREATE
@router.post("/", response_model=SaleResponse, status_code=status.HTTP_201_CREATED)
def create_sale(sale: SaleCreate, db: Session = Depends(get_db), current_user = employee_only):
    
    sale_new = create_sale_service(db, sale , current_user)
    return sale_new


#! GET BY ID
@router.get("/", response_model=list[SaleResponse])
def check_sales(db: Session = Depends(get_db), _ = Depends(role_based_token(["owner" , "admin"]))):
    
    return get_all_sales(db)




