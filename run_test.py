"""Quick end-to-end test — runs without CLI args."""
from emotion_detector import detect_emotion
from tts_engine import speak_and_save

samples = [
    ("I just got promoted! This is the best day ever!", "happy.wav"),
    ("This is absolutely horrible and frustrating.",    "sad.wav"),
    ("The meeting is scheduled for tomorrow.",          "neutral.wav"),
]

for text, filename in samples:
    result = detect_emotion(text)
    print(f"\nText    : {text}")
    print(f"Emotion : {result['label']}")
    print(f"Rate    : {result['rate']} wpm  |  Volume: {result['volume']}")
    saved = speak_and_save(text, result["rate"], result["volume"], filename)
    print(f"Saved   : {saved}")

print("\nAll 3 audio files generated successfully!")
