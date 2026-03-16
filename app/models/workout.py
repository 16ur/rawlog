from sqlalchemy import Column, Integer, Date, Text
from app.core.database import Base
from sqlalchemy.orm import relationship


class Workout(Base):
    __tablename__ = "workouts"
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date)
    notes = Column(Text)
    exercises = relationship("WorkoutExercise", back_populates="workout")
