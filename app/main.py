from fastapi import FastAPI
from app.api.v1 import workouts
from app.api.v1 import exercises
from app.api.v1 import muscles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="rawlog API")

# Include les routers
app.include_router(workouts.router, prefix="/api/v1", tags=["workouts"])
app.include_router(exercises.router, prefix="/api/v1", tags=["exercises"])
app.include_router(muscles.router, prefix="/api/v1", tags=["muscles"])
app.add_middleware(
    CORSMiddleware,  #  type: ignore[arg-type]
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "rawlog API", "status": "running"}
