from sqlalchemy import Column, ForeignKey , String , Integer , Float , Boolean , ForeignKey , DateTime
from sqlalchemy.orm import relationship
from Database.db_connect import Base

class Profile(Base):
    __tablename__ = "worker_profile"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id") , unique=True)

    Fullname = Column(String)
    address = Column(String)
    pincode = Column(Integer)
    aadhar_id = Column(String, unique=True)
    designation = Column(String)
    salary = Column(Float)
    bonus = Column(Float)
    joining_date = Column(DateTime)

    user = relationship("User", back_populates="detail")
    