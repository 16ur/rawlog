from sqlalchemy import Column, Integer, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.core.database import Base


class WorkoutExercise(Base):
    __tablename__ = "workout_exercises"

    id = Column(Integer, primary_key=True)
    workout_id = Column(Integer, ForeignKey("workouts.id", ondelete="CASCADE"))
    exercise_id = Column(Integer, ForeignKey("exercises.id", ondelete="RESTRICT"))
    sets = Column(JSON)

    workout = relationship("Workout", back_populates="exercises")
    exercise = relationship("Exercise")
