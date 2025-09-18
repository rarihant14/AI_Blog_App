from fastapi import FastAPI
from .models import GenerateRequest, GenerateResponse
from .services import GroqService

app = FastAPI()
service = GroqService()

@app.post("/generate", response_model=GenerateResponse)
def generate_blog(request: GenerateRequest):
    return service.generate_draft(request)
