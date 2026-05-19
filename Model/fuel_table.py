from sqlalchemy import Column, Integer , String , Float , Numeric
from sqlalchemy.orm import relationship
from Database.db_connect import Base

class Fuel(Base):
    __tablename__ = "fuels"
    id = Column(Integer , primary_key=True)
    fuel_type = Column(String ,nullable=False , unique=True) #petrol , diesel , cng
    price_per_litter = Column(Numeric(10, 2))
    current_stock = Column(Numeric(10, 3)) 
    
    sales = relationship("Sales", back_populates="fuel")