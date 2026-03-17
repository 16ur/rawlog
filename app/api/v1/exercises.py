from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.exercise import ExerciseCreate, Exercise
from app.crud.exercise import create_exercise, get_exercise, get_all_exercises

router = APIRouter()


@router.post("/exercises", response_model=Exercise)
def create_exercise_handler(exercise: ExerciseCreate, db: Session = Depends(get_db)):
    return create_exercise(db, exercise)


@router.get("/exercises/{exercise_id}", response_model=Exercise)
def get_exercise_handler(exercise_id: int, db: Session = Depends(get_db)):
    return get_exercise(db, exercise_id)


@router.get("/exercises/", response_model=list[Exercise])
def get_all_exercises_handler(db: Session = Depends(get_db)):
    return get_all_exercises(db)
