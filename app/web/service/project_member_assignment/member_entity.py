from pydantic import BaseModel, Field

class Member(BaseModel):
    id: str
    role: str
    processing_skill: int = Field(..., ge=0, le=100)
    english_skill: int = Field(..., ge=0, le=100)
