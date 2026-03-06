from sqlalchemy.orm import Session
from app.models.workout import Workout as WorkoutModel
from app.schemas.workout import WorkoutCreate


def create_workout(db: Session, workout: WorkoutCreate):
    db_workout = WorkoutModel(date=workout.date, notes=workout.notes)

    try:
        db.add(db_workout)
        db.commit()
        db.refresh(db_workout)
    except Exception as e:
        db.rollback()
        raise e
    return db_workout


def get_workout(db: Session, workout_id: int):
    return db.query(WorkoutModel).filter(WorkoutModel.id == workout_id).first()


def get_all_workouts(db: Session):
    return db.query(WorkoutModel).all()


def update_workout(db: Session, workout_id: int, workout: WorkoutCreate):
    db_workout = db.query(WorkoutModel).filter(WorkoutModel.id == workout_id).first()
    if db_workout is None:
        return None

    db_workout.date = workout.date
    db_workout.notes = workout.notes

    try:
        db.commit()
        db.refresh(db_workout)
    except Exception as e:
        db.rollback()
        raise e
    return db_workout


def delete_workout(db: Session, workout_id: int):
    db_workout = db.query(WorkoutModel).filter(WorkoutModel.id == workout_id).first()
    if db_workout is None:
        return None
    try:
        db.delete(db_workout)
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    return db_workout
