from fastapi import FastAPI
from app.api.v1 import workouts
from app.api.v1 import exercises
from app.api.v1 import muscles

app = FastAPI(title="rawlog API")

# Include les routers
app.include_router(workouts.router, prefix="/api/v1", tags=["workouts"])
app.include_router(exercises.router, prefix="/api/v1", tags=["exercises"])
app.include_router(muscles.router, prefix="/api/v1", tags=["muscles"])


@app.get("/")
def read_root():
    return {"message": "rawlog API", "status": "running"}
