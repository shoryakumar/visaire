from fastapi import FastAPI, Request
from pydantic import BaseModel
from manim_runner import generate_animation
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class Prompt(BaseModel):
    user_prompt: str

@app.post("/generate")
async def generate_code(prompt: Prompt):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(f"Generate Manim code to animate: {prompt.user_prompt}")
    
    manim_code = response.text
    video_path = generate_animation(manim_code)
    
    return {"video_url": video_path}