from pydantic import BaseModel
from app.schemas.muscle import Muscle


class ExerciseCreate(BaseModel):
    name: str
    description: str
    muscle_ids: list[int]


class Exercise(BaseModel):
    id: int
    name: str
    description: str
    muscles: list[Muscle]

    class Config:
        from_attributes = True
