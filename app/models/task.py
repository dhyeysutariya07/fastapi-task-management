from app.db.base import Base
from sqlalchemy import Column,Integer,String,DateTime,Float
from datetime import datetime

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(100),index=True)
    priority = Column(String(25),nullable=False)
    estimated_hours = Column(Float,nullable=False)
    actual_hours = Column(Float,nullable=True)
    created_at = Column(DateTime,default=datetime.now)
    updated_at = Column(DateTime,default=datetime.now,onupdate=datetime.now)

