from sqlalchemy import Column, Integer, String, Date, Text, JSON
from app.database import Base

class Workout(Base):
    __tablename__ = 'workouts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date)
    notes = Column(Text)

class Exercise(Base):
    __tablename__ = 'exercises'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    target_muscles = Column(JSON)