from pydantic import BaseModel, Field

class Project(BaseModel):
    id: str
    scale: int = Field(..., gt=0)
    english_required: bool
