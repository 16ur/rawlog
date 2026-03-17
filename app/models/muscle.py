from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base


class Muscle(Base):
    __tablename__ = "muscles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)

    exercises = relationship(
        "Exercise", secondary="exercise_muscles", back_populates="muscles"
    )
