from pydantic import BaseModel
from typing import Optional

class GenerateRequest(BaseModel):
    title: str
    tone: str
    keywords: str
    length: str
    humanize: bool = True
    target_language: Optional[str] = None  # Optional translation

class GenerateResponse(BaseModel):
    draft: str
