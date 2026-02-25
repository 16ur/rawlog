from app.database import Base, engine
from app.models import Workout, Exercise

Base.metadata.create_all(bind=engine)
print("Tables créées avec succès !")



