from pydantic import BaseModel
from datetime import date


# Représente UNE série d'un exercice -> "reps":12, "weight":10
class SetDetails(BaseModel):
    reps: int
    weight: int


# Curl Biceps avec les séries et reps
class WorkoutExerciseCreate(BaseModel):
    exercise_id: int
    sets: list[SetDetails]


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


class WorkoutExercise(WorkoutExerciseCreate):
    id: int
