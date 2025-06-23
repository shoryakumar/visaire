#!/bin/bash

# Start the Visaire application
echo "🚀 Starting Visaire - AI Manim Animation Generator"
echo "📝 Make sure your GEMINI_API_KEY is set in .env file"
echo ""

# Create directories if they don't exist
mkdir -p videos static templates media

echo "🌐 Starting server on http://127.0.0.1:8000"
echo "📚 API Documentation: http://127.0.0.1:8000/docs"
echo "💻 Web Interface: http://127.0.0.1:8000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start the FastAPI server
uv run uvicorn main:app --reload --host 127.0.0.1 --port 8000
