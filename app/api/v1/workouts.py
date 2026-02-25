from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.workout import WorkoutCreate, Workout
from app.crud.workout import create_workout

router = APIRouter()

@router.post("/workouts", response_model=Workout)
def create_workout_handler(workout: WorkoutCreate, db: Session = Depends(get_db)):
    return create_workout(db, workout)

