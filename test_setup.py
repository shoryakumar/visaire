#!/usr/bin/env python3
"""
Simple test script to verify the Manim animation generation works
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def test_imports():
    """Test that all imports work correctly"""
    try:
        import google.generativeai as genai
        import manim
        from manim_runner import generate_animation, clean_code

        print("✅ All imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False


def test_api_key():
    """Test that API key is configured"""
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        print("✅ GEMINI_API_KEY is configured")
        return True
    else:
        print("❌ GEMINI_API_KEY not found in .env")
        return False


def test_manim_runner():
    """Test the manim_runner functions"""
    try:
        from manim_runner import clean_code

        # Test with sample Manim code
        sample_code = """
```python
from manim import *

class TestScene(Scene):
    def construct(self):
        circle = Circle()
        self.play(Create(circle))
```
"""
        cleaned = clean_code(sample_code)
        print("✅ Code cleaning works")
        print(f"Cleaned code preview:\n{cleaned[:100]}...")
        return True
    except Exception as e:
        print(f"❌ Code cleaning error: {e}")
        return False


def test_directories():
    """Test that required directories can be created"""
    try:
        os.makedirs("videos", exist_ok=True)
        os.makedirs("media", exist_ok=True)
        print("✅ Directory creation works")
        return True
    except Exception as e:
        print(f"❌ Directory creation error: {e}")
        return False


def main():
    print("🔍 Running diagnostic tests for visaire...\n")

    tests = [
        ("Imports", test_imports),
        ("API Key", test_api_key),
        ("Manim Runner", test_manim_runner),
        ("Directories", test_directories),
    ]

    passed = 0
    total = len(tests)

    for test_name, test_func in tests:
        print(f"\n📋 Testing {test_name}:")
        if test_func():
            passed += 1

    print(f"\n📊 Results: {passed}/{total} tests passed")

    if passed == total:
        print("🎉 All tests passed! Your app should work correctly.")
        print("\n🚀 To run your app:")
        print("   uv run uvicorn main:app --reload")
        print("\n🌐 Then visit: http://127.0.0.1:8000/docs")
    else:
        print(
            "⚠️  Some tests failed. Please fix the issues above before running the app."
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
