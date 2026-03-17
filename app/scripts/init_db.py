from app.core.database import Base, engine

from app.models.workout import Workout  # noqa: F401
from app.models.exercise import Exercise, exercise_muscles  # noqa: F401
from app.models.workout_exercise import WorkoutExercise  # noqa: F401
from app.models.muscle import Muscle  # noqa: F401

Base.metadata.create_all(bind=engine)

print("Tables créées avec succès !")
print(f"Tables créées : {list(Base.metadata.tables.keys())}")
