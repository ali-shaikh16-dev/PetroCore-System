from turtle import update

from sqlalchemy.orm import Session
from Model.fuel_table import Fuel 
from Schemas.fuel_schm import FuelCreate

def fuels_create(db:Session , fuel:FuelCreate):
    create_fuel = Fuel(**fuel.model_dump())
    
    db.add(create_fuel)
    db.commit()
    db.refresh(create_fuel)
    
    return create_fuel


def get_fuel_by_id(db:Session , id:int):
    return db.query(Fuel).filter(Fuel.id == id).first()


def fuel_update(db:Session , fuel_id:int , fuel:FuelCreate):
    update_fuel = db.query(Fuel).filter(Fuel.id == fuel_id).first()
    if update_fuel:
        update_fuel.fuel_type = fuel.fuel_type
        update_fuel.price_per_litter = fuel.price_per_litter
        update_fuel.current_stock = fuel.current_stock
        
        db.commit()
        db.refresh(update_fuel)
        return True


def fuel_delete(db:Session , fuel_id:int):
    delete_fuel = db.query(Fuel).filter(Fuel.id == fuel_id).first()
    if delete_fuel:
        db.delete(delete_fuel)
        db.commit()
        return True

 