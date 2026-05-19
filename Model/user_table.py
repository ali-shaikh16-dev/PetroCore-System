from sqlalchemy import String , Column , DateTime , Integer
from sqlalchemy.orm import relationship
from datetime import datetime
from Database.db_connect import Base 


class User(Base):
    __tablename__ = "users"
    id = Column(Integer , primary_key=True)
    username = Column(String , nullable=False)
    password = Column(String , nullable=False)
    phone_number = Column(String , nullable=False , unique=True)
    role = Column(String, nullable=False) # customer , admin
    created_at = Column(DateTime , default=datetime.utcnow)
    
    sales = relationship("Sales", back_populates="user")
    subscriptions = relationship("Subscription", back_populates="user")
    
    detail = relationship("Profile", back_populates="user", uselist=False)
