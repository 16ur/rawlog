from sqlalchemy.orm import Session
from app.models.exercise import Exercise as ExerciseModel
from app.models.muscle import Muscle as MuscleModel
from app.schemas.exercise import ExerciseCreate
from sqlalchemy.orm import joinedload


def create_exercise(db: Session, exercise: ExerciseCreate):
    db_exercise = ExerciseModel(
        name=exercise.name,
        description=exercise.description,
    )

    muscles = (
        db.query(MuscleModel).filter(MuscleModel.id.in_(exercise.muscle_ids)).all()
    )
    db_exercise.muscles = muscles
    try:
        db.add(db_exercise)
        db.commit()
        db.refresh(db_exercise)
    except Exception:
        db.rollback()
        raise
    return db_exercise


def get_exercise(db: Session, exercise_id: int):
    return (
        db.query(ExerciseModel)
        .options(joinedload(ExerciseModel.muscles))
        .filter(ExerciseModel.id == exercise_id)
        .first()
    )


def get_all_exercises(db: Session):
    return db.query(ExerciseModel).options(joinedload(ExerciseModel.muscles)).all()
