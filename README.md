# 🎬 Visaire - AI Manim Animation Generator

Visaire is a web application that generates mathematical animations using AI. Simply describe what you want to animate, and Visaire will create beautiful mathematical visualizations using Manim and Google's Gemini AI.

![Visaire Demo](https://img.shields.io/badge/Status-Ready-brightgreen) ![Python](https://img.shields.io/badge/Python-3.13+-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green) ![Manim](https://img.shields.io/badge/Manim-0.19.0-orange)

## ✨ Features

- 🤖 **AI-Powered**: Uses Google Gemini to generate Manim code from natural language descriptions
- 🎨 **Beautiful Web UI**: Modern, responsive interface built with Bootstrap 5
- 📱 **Mobile Friendly**: Works seamlessly on desktop and mobile devices
- 🎥 **Video Generation**: Creates high-quality mathematical animation videos
- 📚 **Animation History**: Automatically saves your generated animations locally
- ⚡ **Fast Rendering**: Optimized for quick preview generation
- 🔄 **Real-time Status**: Live API status monitoring
- 📤 **Export & Share**: Download or share your generated animations

## 🚀 Quick Start

### Prerequisites

- Python 3.13 or higher
- A Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))
- Git (for cloning the repository)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd visaire
   ```

2. **Install uv package manager**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
   
   Or if you prefer pip:
   ```bash
   pip install uv
   ```

3. **Initialize the project**
   ```bash
   uv init --app
   ```

4. **Install dependencies**
   ```bash
   uv add fastapi pydantic google-generativeai python-dotenv manim uvicorn jinja2
   ```

5. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your GEMINI_API_KEY
   ```
   
   Create a `.env` file with:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

6. **Create required directories**
   ```bash
   mkdir -p videos static templates media
   ```

### Running the Application

**Option 1: Use the run script (recommended)**
```bash
./run.sh
```

**Option 2: Manual start**
```bash
uv run uvicorn main:app --reload
```

**Option 3: Using virtual environment**
```bash
source .venv/bin/activate
uvicorn main:app --reload
```

## 🌐 Usage

### Web Interface

1. **Start the server** using one of the methods above
2. **Open your browser** and go to `http://127.0.0.1:8000`
3. **Enter your animation prompt** in the text area
4. **Click "Generate Animation"** and wait for the magic!
5. **Watch, download, or share** your generated video

### Example Prompts

Try these example prompts to get started:

- "A red circle moves in a figure-8 pattern"
- "A square transforms into a triangle with a rotation"
- "Mathematical equation 2x + 3 = 7 being solved step by step"
- "A graph of sine and cosine waves appearing and oscillating"
- "A blue dot tracing a spiral path while growing larger"
- "Two circles colliding and bouncing off each other"

### API Endpoints

#### Generate Animation
```bash
POST /generate
Content-Type: application/json

{
  "user_prompt": "A circle transforms into a square"
}
```

#### Health Check
```bash
GET /health
```

#### API Documentation
Visit `http://127.0.0.1:8000/docs` for interactive API documentation.

## 📁 Project Structure

```
visaire/
├── main.py                 # FastAPI application
├── manim_runner.py         # Manim code execution module
├── pyproject.toml          # Project dependencies
├── run.sh                  # Easy start script
├── test_setup.py           # Diagnostic tests
├── .env                    # Environment variables
├── .gitignore              # Git ignore rules
├── README.md               # This file
├── static/                 # Web assets
│   ├── app.js             # Frontend JavaScript
│   └── style.css          # Custom styling
├── templates/              # HTML templates
│   └── index.html         # Main web interface
├── videos/                 # Generated animations
├── media/                  # Manim output directory
└── .venv/                  # Virtual environment (created by uv)
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# Required: Google Gemini API Key
GEMINI_API_KEY=your_api_key_here

# Optional: Server configuration
HOST=127.0.0.1
PORT=8000
DEBUG=True
```

### Manim Settings

The application uses these Manim settings by default:
- **Quality**: Low quality (`-ql`) for faster rendering
- **Output**: Direct to videos folder
- **Format**: MP4 video files

You can modify these settings in `manim_runner.py`.

## 🛠️ Development

### Running Tests

Test your setup with the diagnostic script:
```bash
uv run python test_setup.py
```

### Adding New Features

1. **Backend changes**: Edit `main.py` for new API endpoints
2. **Frontend changes**: Edit files in `static/` and `templates/`
3. **Manim processing**: Modify `manim_runner.py`

### Code Quality

The project follows these practices:
- Type hints for Python functions
- Error handling with informative messages
- Responsive web design
- Clean separation of concerns

## 🐛 Troubleshooting

### Common Issues

**1. "GEMINI_API_KEY not configured"**
- Make sure you have a `.env` file with a valid API key
- Check that the API key is active and has proper permissions

**2. "Manim command failed"**
- Ensure Manim is properly installed: `uv run python -c "import manim; print('OK')"`
- Check that system dependencies for Manim are installed

**3. "Videos not appearing"**
- Check that the `videos/` directory exists and is writable
- Verify that the generated video files are not corrupted

**4. Web interface not loading**
- Ensure all static files are in place (`static/` and `templates/` directories)
- Check browser console for JavaScript errors

### Debug Mode

Run with debug output:
```bash
uv run uvicorn main:app --reload --log-level debug
```

### Checking Dependencies

Verify all packages are installed:
```bash
uv run python -c "
import fastapi, manim, google.generativeai
print('✅ All dependencies installed correctly')
"
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [Manim](https://github.com/ManimCommunity/manim) - Mathematical animation engine
- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework
- [Google Gemini](https://ai.google.dev/) - AI code generation
- [Bootstrap](https://getbootstrap.com/) - UI framework

## 📞 Support

- 🐛 **Bug Reports**: Open an issue on GitHub
- 💡 **Feature Requests**: Open an issue with the "enhancement" label
- 📧 **Questions**: Check the discussions section

---

**Made with ❤️ and AI magic** ✨