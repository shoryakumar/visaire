from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from manim_runner import generate_animation
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/videos", StaticFiles(directory="videos"), name="videos")
templates = Jinja2Templates(directory="templates")

class Prompt(BaseModel):
    user_prompt: str

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/health")
async def health_check():
    api_key_configured = bool(os.getenv("GEMINI_API_KEY"))
    return {
        "status": "healthy",
        "api_key_configured": api_key_configured,
        "service": "manim animation generator"
    }

@app.post("/generate")
async def generate_code(prompt: Prompt):
    try:
        # Check if API key is configured
        if not os.getenv("GEMINI_API_KEY"):
            raise HTTPException(status_code=500, detail="GEMINI_API_KEY not configured")
        
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(f"Generate Manim code to animate: {prompt.user_prompt}")
        
        if not response.text:
            raise HTTPException(status_code=500, detail="Failed to generate code from AI")
        
        manim_code = response.text
        video_path = generate_animation(manim_code)
        
        return {"video_url": video_path, "status": "success"}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating animation: {str(e)}")