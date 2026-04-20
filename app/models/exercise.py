from sqlalchemy import Column, Integer, String, Table, ForeignKey
from app.core.database import Base
from sqlalchemy.orm import relationship


exercise_muscles = Table(
    "exercise_muscles",
    Base.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("exercise_id", Integer, ForeignKey("exercises.id", ondelete="CASCADE")),
    Column("muscle_id", Integer, ForeignKey("muscles.id", ondelete="CASCADE")),
)


class Exercise(Base):
    __tablename__ = "exercises"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)

    muscles = relationship(
        "Muscle", secondary=exercise_muscles, back_populates="exercises"
    )
