"""
Empathy Engine - Flask Web Application
"""

import os
import uuid
from flask import Flask, render_template, request, jsonify, send_from_directory
from emotion_detector import detect_emotion
from tts_engine import speak_and_save

app = Flask(__name__)

AUDIO_FOLDER = os.path.join("static", "audio")
os.makedirs(AUDIO_FOLDER, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    text = data.get("text", "").strip()

    if not text:
        return jsonify({"error": "Please enter some text."}), 400

    if len(text) > 500:
        return jsonify({"error": "Text must be 500 characters or less."}), 400

    # Detect emotion
    result = detect_emotion(text)

    # Generate a unique audio filename to avoid browser caching
    filename = f"output_{uuid.uuid4().hex[:8]}.mp3"
    filepath = os.path.join(AUDIO_FOLDER, filename)

    # Generate audio
    speak_and_save(text, result["rate"], result["volume"], filepath)

    # Clean up old audio files (keep only last 5)
    _cleanup_old_files(AUDIO_FOLDER, keep=5, ext=".mp3")

    return jsonify({
        "emotion":    result["label"],
        "compound":   round(result["compound"], 4),
        "rate":       result["rate"],
        "volume":     result["volume"],
        "audio_url":  f"/static/audio/{filename}",
        "intensity":  result["intensity"],
        "category":   result["emotion"],
    })


@app.route("/static/audio/<filename>")
def serve_audio(filename):
    return send_from_directory(AUDIO_FOLDER, filename)


def _cleanup_old_files(folder: str, keep: int = 5, ext: str = ".mp3"):
    """Delete oldest audio files, keeping only the most recent `keep` files."""
    files = sorted(
        [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(ext)],
        key=os.path.getmtime,
    )
    for old_file in files[:-keep]:
        try:
            os.remove(old_file)
        except OSError:
            pass


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"\n  Empathy Engine Web App running at: http://127.0.0.1:{port}\n")
    app.run(host="0.0.0.0", port=port, debug=False)
