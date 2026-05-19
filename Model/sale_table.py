from sqlalchemy import String , Column , DateTime , Integer , Float , ForeignKey , Numeric
from sqlalchemy.orm import relationship
from Database.db_connect import Base 
from datetime import datetime

class Sales(Base):
    __tablename__ = "sale"
    id = Column(Integer , primary_key=True)
    
    fuel_id = Column(Integer , ForeignKey("fuels.id"))
    user_id = Column(Integer , ForeignKey("users.id"))
    
    liters = Column(Numeric(10, 3))
    price_per_litter = Column(Numeric(10, 2))
    amount = Column(Numeric(10, 2)) 
    payment_method = Column(String) # cash , card , upi
    created_at = Column(DateTime , default=datetime.utcnow)
    
    user = relationship("User", back_populates="sales")
    fuel = relationship("Fuel", back_populates="sales") 
    


