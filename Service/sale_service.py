from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from decimal import Decimal
from Model.fuel_table import Fuel
from Model.user_table import User
from Model.sale_table import Sales
from Schemas.sale_schm import SaleCreate
from Repository.sale_repo import create_sale


def create_sale_service(db: Session, sale: SaleCreate, current_user: User):
    
    #* 1. Fuel fetch karo
    fuel = db.query(Fuel).filter(Fuel.id == sale.fuel_id).first()

    if not fuel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Fuel not found"
        )

    #* 2. Price lo
    price_per_litter = Decimal(fuel.price_per_litter)
    
    amount = Decimal(sale.amount)
    

    #* 3. Liters calculate karo
    liters = amount / price_per_litter
    

    #* 4. Stock check karo
    if fuel.current_stock < liters:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insufficient fuel stock"
        )
        

    #* 5. Stock deduct karo
    fuel.current_stock -= liters
    

    #* 6. Temporary object banao jo repo ko diya jayega
    sale_data = Sales(
        fuel_id=sale.fuel_id,
        user_id=current_user["user_id"],
        liters=liters,
        price_per_litter=price_per_litter,
        amount=sale.amount,
        payment_method=sale.payment_method
    )
    

    #* 7. Repository save karega
    created_sale = create_sale(db, sale_data)

    return created_sale