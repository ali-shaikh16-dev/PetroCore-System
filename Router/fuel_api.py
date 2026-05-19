from fastapi import Depends , FastAPI , Security , APIRouter , HTTPException ,status
from sqlalchemy.orm import Session
from Database.db_connect import get_db
from Model.fuel_table import Fuel
from utils.jwt_token_work import role_based_token

from Schemas.fuel_schm import FuelCreate , FuelResponse , FuelUpdate
from Repository.fuel_repo import fuels_create , get_fuel_by_id , fuel_update , fuel_delete 

from sqlalchemy.exc import IntegrityError


#*ROOM 2 WORK FOR Fuel
router = APIRouter()


#* OWNER and ADMIN ONLY ACCESS

owner_admin_only = Depends(role_based_token(["admin" , "owner"]))


#! CREATE FUEL
@router.post("/", response_model=FuelResponse, status_code=status.HTTP_201_CREATED)
def create_fuel(fuel: FuelCreate, db: Session = Depends(get_db) , _ = owner_admin_only):
    
    try:
        return fuels_create(db, fuel)

    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400,detail="Fuel type already exists")
    



#! GET FUEL BY ID
@router.get("/{fuel_id}", response_model=FuelResponse)
def get_fuel(fuel_id: int, db: Session = Depends(get_db) , _ = owner_admin_only):
    
    get_fuel = get_fuel_by_id(db, fuel_id)

    if not get_fuel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Fuel not found")

    return get_fuel



@router.get("/", response_model=list[FuelResponse])
def fetch_all_fuel(db:Session = Depends(get_db) , _ = owner_admin_only):
    return db.query(Fuel).all()





#! UPDATE FUEL
@router.patch("/{fuel_id}", response_model=FuelResponse)
def update_fuel(fuel_id: int, fuel_data: FuelUpdate, db: Session = Depends(get_db) ,  _ = owner_admin_only):
    
    db_fuel = db.query(Fuel).filter(Fuel.id == fuel_id).first()
    
    if not db_fuel:
        raise HTTPException(status.HTTP_404_NOT_FOUND , detail="Fuel Not Found")
    
    fuel_upd = fuel_data.model_dump(exclude_unset=True)
    
    for key , value in fuel_upd.items():
        setattr(db_fuel , key , value)
        
    db.commit()
    db.refresh(db_fuel)
    
    return db_fuel




#! DELETE FUEL
@router.delete("/{fuel_id}")
def delete_fuel(fuel_id: int, db: Session = Depends(get_db) , _ = owner_admin_only):
    
    is_deleted = fuel_delete(db, fuel_id)

    if not is_deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Fuel not found")

    return {"message": "Fuel deleted successfully"}