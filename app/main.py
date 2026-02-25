from fastapi import FastAPI
from app.api.v1 import workouts

app = FastAPI(title="rawlog API")

# Include les routers
app.include_router(workouts.router, prefix="/api/v1", tags=["workouts"])

@app.get("/")
def read_root():
    return {"message": "rawlog API", "status": "running"}