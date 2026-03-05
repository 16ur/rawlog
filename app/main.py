from fastapi import FastAPI
from app.api.v1 import workouts
from app.api.v1 import exercises

app = FastAPI(title="rawlog API")

# Include les routers
app.include_router(workouts.router, prefix="/api/v1", tags=["workouts"])
app.include_router(exercises.router, prefix="/api/v1", tags=["exercises"])


@app.get("/")
def read_root():
    return {"message": "rawlog API", "status": "running"}
