from app.core.database import Base, engine
from app.models.workout import Workout
from app.models.exercise import Exercise

Base.metadata.create_all(bind=engine)
print("Tables créées avec succès !")



