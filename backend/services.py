from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

class GroqService:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("GROQ_API_KEY")
        self.llm = ChatGroq(api_key=self.api_key, model="gemma2-9b-it")

    def build_prompt(self, title, tone, keywords, length, humanize):
        length_map = {"short": 200, "medium": 400, "long": 800}
        tokens = length_map.get(length, 400)
        prompt = f"""
        Write a Medium-style blog draft.

        Title: {title}
        Tone: {tone}
        Keywords: {keywords}
        Approx tokens: {tokens}
        """
        if humanize:
            prompt = (
            "You are a Humanizer AI. Your job is to rewrite robotic or AI-generated text "            
            "u have to be  imperfect like a human u can make some  error. "
            "Make it more expressive, personal, varied, and emotionally rich.\n"
            + prompt
        )
        return prompt

    def generate_draft(self, request):
        # Generate draft
        prompt = self.build_prompt(
            request.title, request.tone, request.keywords, request.length, request.humanize
        )
        draft = self.llm.invoke(prompt).content

        # Optional translation
        if request.target_language:
            translation_prompt = f"Translate the following blog into {request.target_language}:\n{draft}"
            draft = self.llm.invoke(translation_prompt).content

        return {"draft": draft}
