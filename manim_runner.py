import uuid
import os
import re
import subprocess

def clean_code(code: str) -> str:
    """
    Clean Gemini-generated code and ensure it's Manim-compatible.
    Removes markdown syntax and explanations.
    """
    lines = code.strip().splitlines()

    # Remove markdown formatting like ```python and ```
    lines = [line for line in lines if not line.strip().startswith("```")]

    # Filter out explanation lines after class definition
    code_lines = []
    inside_class = False

    for line in lines:
        if not inside_class and line.strip().startswith("class") and "Scene" in line:
            inside_class = True
            code_lines.append(line)
        elif inside_class:
            if re.match(r"^\s*\w+[\s\w]*[:\-]", line.strip()):
                # probably explanation or new section
                break
            code_lines.append(line)
        elif not inside_class:
            code_lines.append(line)

    # Ensure the necessary import is included
    return "from manim import *\n\n" + "\n".join(code_lines)

def generate_animation(code: str) -> str:
    """
    Generates a Manim animation from provided code.
    Returns the path to the output video file.
    """
    # Ensure videos directory exists
    os.makedirs("videos", exist_ok=True)

    # Unique ID for this animation
    unique_id = str(uuid.uuid4())
    python_file = f"anim_{unique_id}.py"
    video_file = f"video_{unique_id}.mp4"
    video_path = os.path.join("videos", video_file)

    # Clean and write the Manim code to a Python file
    cleaned_code = clean_code(code)
    with open(python_file, "w") as f:
        f.write(cleaned_code)

    # Try to extract the class name from the code
    class_match = re.search(r"class\s+(\w+)$begin:math:text$Scene$end:math:text$:", cleaned_code)
    scene_name = class_match.group(1) if class_match else "Scene"

    # Run the Manim command to generate the video
    try:
        subprocess.run([
            "manim",
            python_file,
            scene_name,
            "-o", video_file,
            "-qk"  # qk = quick render
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Manim failed: {e}")
        raise e
    finally:
        if os.path.exists(python_file):
            os.remove(python_file)

    return video_path