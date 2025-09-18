import os, time
from langsmith import Client as LangSmithClient
from dotenv import load_dotenv

load_dotenv()
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")

langsmith = None
if LANGSMITH_API_KEY:
    langsmith = LangSmithClient(api_key=LANGSMITH_API_KEY)

def log_to_langsmith(name: str, meta: dict, duration: float = None):
    if not langsmith:
        return None
    run = langsmith.create_run(name=name, metadata=meta)
    if duration:
        langsmith.log_run(run.id, {"duration": duration})
    return run.id
