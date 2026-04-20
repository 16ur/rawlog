from pydantic import BaseModel, Field


class SetDetails(BaseModel):
    reps: int = Field(gt=0, le=100)
    weight: int = Field(ge=0, le=500)


class WorkoutExerciseCreate(BaseModel):
    exercise_id: int
    sets: list[SetDetails]


class WorkoutExercise(WorkoutExerciseCreate):
    id: int
    workout_id: int

    class Config:
        from_attributes = True
