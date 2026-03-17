from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.muscle import MuscleCreate, Muscle
from app.crud.muscle import create_muscle

router = APIRouter()


@router.post("/muscles", response_model=Muscle)
def create_muscle_handler(muscle: MuscleCreate, db: Session = Depends(get_db)):
    return create_muscle(db, muscle)


# @router.get("/muscles")
