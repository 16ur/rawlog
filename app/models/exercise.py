from sqlalchemy import Column, Integer, String, Date, Text, JSON
from app.core.database import Base


class Exercise(Base):
    __tablename__ = 'exercises'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    target_muscles = Column(JSON)