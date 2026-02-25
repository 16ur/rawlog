from pydantic import BaseModel
from datetime import date

# Ex: Curl Biceps - Muscle ciblé ["Biceps", "Avant-bras"]
class ExerciseCreate(BaseModel):
    name: str
    description: str
    target_muscles: list[str]

# Représente UNE série d'un exercice -> "reps":12, "weight":10
class SetDetails(BaseModel):
    reps: int
    weight: int

# Curl Biceps avec les séries et reps
class WorkoutExerciseCreate(BaseModel):
    exercise_id: int
    sets: list[SetDetails]

# Séance avec pleins d'exercice et les series etc
class WorkoutCreate(BaseModel):
    date: date
    notes: str
    exercises: list[WorkoutExerciseCreate]
    
    
class Exercise(ExerciseCreate):
    id: int

class Workout(WorkoutCreate):
    id: int

class WorkoutExersice(WorkoutExerciseCreate):
    id: int