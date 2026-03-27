from emotion_detector import detect_emotion

tests = [
    "I just got promoted! This is the best day ever!",
    "This is absolutely horrible and I am very frustrated.",
    "The meeting is scheduled for tomorrow.",
    "I am so happy today!",
    "I feel terrible and sad.",
]

for text in tests:
    r = detect_emotion(text)
    print(f"Text    : {text}")
    print(f"Emotion : {r['label']}  |  Rate: {r['rate']} wpm  |  Volume: {r['volume']}  |  Compound: {r['compound']:.4f}")
    print()
