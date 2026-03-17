from pydantic import BaseModel


class SetDetails(BaseModel):
    reps: int
    weight: int


class WorkoutExerciseCreate(BaseModel):
    exercise_id: int
    sets: list[SetDetails]


class WorkoutExercise(WorkoutExerciseCreate):
    id: int
    workout_id: int

    class Config:
        from_attributes = True
