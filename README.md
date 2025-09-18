# AI Blog App with Groq LLM

This project allows users to generate Medium-style blog drafts and optionally translate them into another language using a **Groq LLM**.  
It uses **FastAPI** for the backend and **Streamlit** for the frontend.

## Features
- Generate AI-written blogs with optional humanization
- Optional translation into user-selected languages
- Modular architecture with multi-agent capabilities (Writer + Translation)
- Streamlit interactive frontend


1️⃣ Clone the repository
    git clone https://github.com/rarihant14/AI_Blog_App.git
    cd AI_Blog_App

2️⃣ Install dependencies
    pip install -r requirements.txt

3️⃣    Copy .env.example to .env:
    (add real api)


4️⃣ Run the backend (FastAPI)    
    uvicorn backend.main:app --reload

5️⃣ Run the frontend (Streamlit)
    streamlit run frontend/app.py


