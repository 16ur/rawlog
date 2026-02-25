from fastapi import FastAPI

app = FastAPI(title="rawlog")


@app.get("/")
def read_root():
    return {"message": "Workout Tracker API", "status": "running"}

