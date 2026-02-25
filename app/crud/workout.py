from sqlalchemy.orm import Session
from app.models.workout import Workout as WorkoutModel
from app.schemas.workout import WorkoutCreate

# TODO :
#  create_workout(db, workout_data) -> crée une séance en base
#  get_workout(db, workout_id) -> récupère une séance par id
#  get_workouts(db) -> liste toutes les séances

def create_workout(db: Session, workout: WorkoutCreate):
    db_workout = WorkoutModel(
        date = workout.date,
        notes = workout.notes
    )
    
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

def get_all_workouts(db:Session):
    return db.query(WorkoutModel).all()