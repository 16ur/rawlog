from pydantic import BaseModel


class ExerciseCreate(BaseModel):
    name: str
    description: str
    target_muscles: list[str]


class Exercise(ExerciseCreate):
    id: int

    class Config:
        from_attributes = True
