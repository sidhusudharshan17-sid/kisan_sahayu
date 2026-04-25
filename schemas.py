from pydantic import BaseModel
from typing import Optional

class ChatRequest(BaseModel):
    message: str
    language: Optional[str] = "auto"
    district: Optional[str] = None
    crop: Optional[str] = None

class ChatResponse(BaseModel):
    reply: str
    language: str
    status: str