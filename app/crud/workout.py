from sqlalchemy.orm import Session, joinedload
from app.models.workout import Workout as WorkoutModel
from app.models.workout_exercise import WorkoutExercise as WorkoutExerciseModel
from app.schemas.workout import WorkoutCreateFull, WorkoutCreate


def create_workout(db: Session, workout: WorkoutCreateFull):
    db_workout = WorkoutModel(date=workout.date, notes=workout.notes)

    try:
        db.add(db_workout)
        db.commit()
        db.refresh(db_workout)

        for exercise in workout.exercises:
            db_workout_exercise = WorkoutExerciseModel(
                workout_id=db_workout.id,
                exercise_id=exercise.exercise_id,
                sets=[set.model_dump() for set in exercise.sets],
            )
            db.add(db_workout_exercise)
        db.commit()
        db.refresh(db_workout)
    except Exception:
        db.rollback()
        raise
    return db_workout


def get_workout(db: Session, workout_id: int):
    return (
        db.query(WorkoutModel)
        .options(joinedload(WorkoutModel.exercises))
        .filter(WorkoutModel.id == workout_id)
        .first()
    )


def get_all_workouts(db: Session):
    return db.query(WorkoutModel).options(joinedload(WorkoutModel.exercises)).all()


def update_workout(db: Session, workout_id: int, workout: WorkoutCreate):
    db_workout = db.query(WorkoutModel).filter(WorkoutModel.id == workout_id).first()
    if db_workout is None:
        return None

    db_workout.date = workout.date
    db_workout.notes = workout.notes

    try:
        db.commit()
        db.refresh(db_workout)
    except Exception:
        db.rollback()
        raise
    return db_workout


def delete_workout(db: Session, workout_id: int):
    db_workout = db.query(WorkoutModel).filter(WorkoutModel.id == workout_id).first()
    if db_workout is None:
        return None
    try:
        db.delete(db_workout)
        db.commit()
    except Exception:
        db.rollback()
        raise
    return db_workout
