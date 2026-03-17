from pydantic import BaseModel


class MuscleCreate(BaseModel):
    name: str


class Muscle(MuscleCreate):
    id: int

    class Config:
        from_attributes = True
