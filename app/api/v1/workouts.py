from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.workout import WorkoutCreate, Workout
from app.crud.workout import (
    create_workout,
    get_workout,
    get_all_workouts,
    update_workout,
    delete_workout,
)

router = APIRouter()


@router.post("/workouts", response_model=Workout, status_code=201)
def create_workout_handler(workout: WorkoutCreate, db: Session = Depends(get_db)):
    return create_workout(db, workout)


@router.get("/workouts/{workout_id}", response_model=Workout)
def get_workout_handler(workout_id: int, db: Session = Depends(get_db)):
    result = get_workout(db, workout_id)

    if result is None:
        raise HTTPException(status_code=404, detail="Workout not found")

    return result


@router.get("/workouts/", response_model=list[Workout])
def get_all_workouts_handler(db: Session = Depends(get_db)):
    return get_all_workouts(db)


@router.put("/workouts/{workout_id}", response_model=Workout)
def update_workout_handler(
    workout_id: int, workout: WorkoutCreate, db: Session = Depends(get_db)
):
    result = update_workout(db, workout_id, workout)

    if result is None:
        raise HTTPException(status_code=404, detail="Workout not found")

    return result


@router.delete("/workouts/{workout_id}", status_code=204)
def delete_workout_handler(workout_id: int, db: Session = Depends(get_db)):
    result = delete_workout(db, workout_id)

    if result is None:
        raise HTTPException(status_code=404, detail="Workout not found")

    return None
