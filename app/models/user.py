from sqlalchemy import Column,Integer,String,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True, index = True)
    username = Column(String(50),unique=True,nullable=False,index=True)
    password = Column(String(255),nullable=False)
    tasks = relationship("Task", back_populates="owner")
    created_at = Column(DateTime, default=datetime.now)