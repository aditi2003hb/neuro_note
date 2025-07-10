from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.services.ai_engine import generate_study_material

router = APIRouter()

# Schema for input request
class ContentRequest(BaseModel):
    topic: str
    content: str

# Route for generating study material
@router.post("/generate")
async def generate_material(request: ContentRequest):
    try:
        output = generate_study_material(request.topic, request.content)
        return output
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
