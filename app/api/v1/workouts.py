from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.workout import WorkoutCreate, Workout
from app.crud.workout import create_workout, get_workout, get_all_workouts

router = APIRouter()

@router.post("/workouts", response_model=Workout)
def create_workout_handler(workout: WorkoutCreate, db: Session = Depends(get_db)):
    return create_workout(db, workout)

@router.get("/workouts/{workout_id}", response_model=Workout)
def get_workout_handler(workout_id: int, db:Session = Depends(get_db)):
    return get_workout(db, workout_id)

@router.get("/workouts/", response_model=list[Workout])
def get_all_workouts_handler(db:Session = Depends(get_db)):
    return get_all_workouts(db)
