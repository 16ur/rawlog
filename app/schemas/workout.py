from pydantic import BaseModel
from datetime import date
from app.schemas.workout_exercise import WorkoutExerciseCreate, WorkoutExercise


# Pour créer un workout avec des exercices
class WorkoutCreateFull(BaseModel):
    date: date
    notes: str
    exercises: list[WorkoutExerciseCreate]


# Pour créer un workout sans exercice (temporaire)
class WorkoutCreate(BaseModel):
    date: date
    notes: str


# Pour lire un workout sans exercices
class Workout(BaseModel):
    id: int
    date: date
    notes: str

    class Config:
        from_attributes = True


class WorkoutWithExercises(Workout):
    exercises: list[WorkoutExercise]
