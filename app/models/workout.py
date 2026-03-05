from sqlalchemy import Column, Integer, Date, Text
from app.core.database import Base


class Workout(Base):
    __tablename__ = "workouts"
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date)
    notes = Column(Text)
