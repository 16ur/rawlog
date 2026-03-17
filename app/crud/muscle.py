from sqlalchemy.orm import Session
from app.schemas.muscle import MuscleCreate, Muscle
from app.models.muscle import Muscle as MuscleModel


def create_muscle(db: Session, muscle: MuscleCreate) -> Muscle:
    db_muscle = MuscleModel(name=muscle.name)
    try:
        db.add(db_muscle)
        db.commit()
        db.refresh(db_muscle)
    except Exception:
        db.rollback()
        raise
    return db_muscle


def get_all_muscles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(MuscleModel).offset(skip).limit(limit).all()
