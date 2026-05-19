from sqlalchemy import String , Column , DateTime , Integer , ForeignKey , Float
from sqlalchemy.orm import relationship
from datetime import datetime
from Database.db_connect import Base 

class Subscription(Base):
    __tablename__ = "subscriptions"
    id = Column(Integer , primary_key=True)
    
    user_id = Column(Integer , ForeignKey("users.id"))
    
    plan_price = Column(Float) # $ per month
    start_date = Column(DateTime , default=datetime.utcnow)
    end_date = Column(DateTime)
    
    status = Column(String) # active , expired 
    user = relationship("User", back_populates="subscriptions")
    

