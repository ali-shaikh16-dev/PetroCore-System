from sqlalchemy.orm import Session
from Model.sale_table import Sales
from Schemas.sale_schm import SaleCreate

def create_sale(db:Session , sale:SaleCreate):
    new_sale = Sales(**sale.model_dump())
    
    db.add(new_sale)
    db.commit()
    db.refresh(new_sale)
    return new_sale


def get_sales(db:Session , sale_id:int):
    return db.query(Sales).filter(Sales.id == sale_id).first()


def get_all_sales(db: Session):
    return db.query(Sales).all()


def update_sale(db:Session , sale_id:int , sale:SaleCreate):
    sale_update = db.query(Sales).filter(Sales.id == sale_id).first()
    if sale_update:
        sale_update.fuel_id = sale.fuel_id
        sale_update.user_id = sale.user_id
        
        sale_update.liters = sale.liters
        sale_update.price_per_litter = sale.price_per_litter
        
        sale_update.amount = sale.amount
        sale_update.payment_method = sale.payment_method
        db.commit()
        db.refresh(sale_update)
        return sale_update is True


def delete_sale(db:Session , sale_id:int):
    sale_delete = db.query(Sales).filter(Sales.id == sale_id).first()
    if sale_delete:
        db.delete(sale_delete)
        db.commit()
        db.refresh(sale_delete)
        return sale_delete is True
    
    