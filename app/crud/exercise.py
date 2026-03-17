from sqlalchemy.orm import Session
from app.models.exercise import Exercise as ExerciseModel
from app.schemas.exercise import ExerciseCreate


def create_exercise(db: Session, exercise: ExerciseCreate):
    db_exercise = ExerciseModel(
        name=exercise.name,
        description=exercise.description,
        target_muscles=exercise.target_muscles,
    )

    try:
        db.add(db_exercise)
        db.commit()
        db.refresh(db_exercise)
    except Exception:
        db.rollback()
        raise
    return db_exercise


def get_exercise(db: Session, exercise_id: int):
    return db.query(ExerciseModel).filter(ExerciseModel.id == exercise_id).first()


def get_all_exercises(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ExerciseModel).offset(skip).limit(limit).all()
