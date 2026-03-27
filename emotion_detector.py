"""
Emotion Detector using VADER Sentiment Analysis.
Classifies text into emotions with intensity levels.
"""

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon on first run
nltk.download("vader_lexicon", quiet=True)


EMOTION_MAP = {
    "positive": {
        "mild":     {"label": "Positive (Mild)",    "rate": 165, "volume": 0.80},
        "moderate": {"label": "Positive (Moderate)","rate": 185, "volume": 0.87},
        "strong":   {"label": "Positive (Strong)",  "rate": 205, "volume": 0.95},
    },
    "negative": {
        "mild":     {"label": "Negative (Mild)",    "rate": 140, "volume": 0.72},
        "moderate": {"label": "Negative (Moderate)","rate": 120, "volume": 0.65},
        "strong":   {"label": "Negative (Strong)",  "rate": 100, "volume": 0.55},
    },
    "neutral": {
        "mild":     {"label": "Neutral",            "rate": 155, "volume": 0.78},
        "moderate": {"label": "Neutral",            "rate": 155, "volume": 0.78},
        "strong":   {"label": "Neutral",            "rate": 155, "volume": 0.78},
    },
}


def _get_intensity(compound: float) -> str:
    """Map compound score magnitude to an intensity level."""
    magnitude = abs(compound)
    if magnitude >= 0.6:
        return "strong"
    elif magnitude >= 0.3:
        return "moderate"
    else:
        return "mild"


def detect_emotion(text: str) -> dict:
    """
    Analyse text and return emotion category, intensity, and voice parameters.

    Returns a dict with keys:
        - emotion   : 'positive' | 'negative' | 'neutral'
        - intensity : 'mild' | 'moderate' | 'strong'
        - label     : human-readable label
        - rate      : TTS speaking rate (words per minute)
        - volume    : TTS volume  (0.0 – 1.0)
        - compound  : raw VADER compound score
    """
    analyser = SentimentIntensityAnalyzer()
    scores = analyser.polarity_scores(text)
    compound = scores["compound"]

    if compound >= 0.05:
        emotion = "positive"
    elif compound <= -0.05:
        emotion = "negative"
    else:
        emotion = "neutral"

    intensity = _get_intensity(compound)
    params = EMOTION_MAP[emotion][intensity]

    return {
        "emotion":   emotion,
        "intensity": intensity,
        "label":     params["label"],
        "rate":      params["rate"],
        "volume":    params["volume"],
        "compound":  compound,
    }
