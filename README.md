# 🎙 The Empathy Engine

> **Challenge 1 Submission** – Emotionally Expressive AI Voice Synthesizer

## Overview

The Empathy Engine is a Python service that **dynamically modulates synthesized speech** based on the detected emotion of the input text. It bridges the gap between plain text-based sentiment and expressive, human-like audio output — moving beyond robotic, monotonic TTS delivery.

---

## Features

- **3-Class Emotion Detection** – Positive, Negative, Neutral (using VADER)
- **Intensity Scaling** – Mild / Moderate / Strong, based on sentiment score magnitude
- **2 Vocal Parameters Modulated** – Speaking Rate (wpm) & Volume
- **Offline & No API Keys Required** – Uses `pyttsx3` (local SAPI5 on Windows)
- **Audio File Output** – Saves a playable `.wav` file for every input
- **Interactive CLI Mode** – Process multiple texts in one session

---

## Emotion → Voice Mapping

| Emotion           | Rate (wpm) | Volume |
|-------------------|-----------|--------|
| Positive (Mild)   | 165       | 0.80   |
| Positive (Moderate)| 185      | 0.87   |
| Positive (Strong) | 205       | 0.95   |
| Neutral           | 155       | 0.78   |
| Negative (Mild)   | 140       | 0.72   |
| Negative (Moderate)| 120      | 0.65   |
| Negative (Strong) | 100       | 0.55   |

**Logic:** VADER's compound score determines emotion class (`>= 0.05` = Positive, `<= -0.05` = Negative, else Neutral). The magnitude of the compound score determines intensity (`< 0.3` = mild, `0.3–0.6` = moderate, `> 0.6` = strong), which then scales the vocal parameters accordingly.

---

## Project Structure

```
EmpathyEngine/
├── main.py              # CLI entry point
├── emotion_detector.py  # VADER-based emotion & intensity detection
├── tts_engine.py        # pyttsx3 TTS with vocal parameter modulation
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

---

## Setup & Installation

### Prerequisites
- Python 3.8 or higher
- Windows (SAPI5 voices built-in) / macOS / Linux

### Step 1 – Clone or download the project

```bash
cd EmpathyEngine
```

### Step 2 – Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3 – (Automatic) Download VADER lexicon

The VADER lexicon downloads automatically on first run. No manual step needed.

---

## Running the Application

### Interactive Mode (recommended for demo)

```bash
python main.py
```

You will be prompted to enter text. Type anything and press Enter. A `.wav` file is saved for each input. Type `quit` to exit.

### Single Text via CLI flag

```bash
python main.py --text "I just got promoted today!"
```

Saves output to `output.wav` by default.

### Custom Output File

```bash
python main.py --text "This is terrible news." --output angry_speech.wav
```

### List Available System Voices

```bash
python main.py --voices
```

---

## Example Outputs

| Input Text | Detected Emotion | Rate | Volume |
|---|---|---|---|
| `"I just got promoted! This is the best day ever!"` | Positive (Strong) | 205 wpm | 0.95 |
| `"I'm okay I guess."` | Neutral | 155 wpm | 0.78 |
| `"This is absolutely horrible and frustrating."` | Negative (Strong) | 100 wpm | 0.55 |

---

## Design Choices

- **VADER over TextBlob** – VADER is specifically designed for social-media and short texts, making it more accurate for conversational input without needing a trained model.
- **pyttsx3 for TTS** – Fully offline, no API keys, works on all platforms. Uses Windows SAPI5 on Windows.
- **Rate + Volume modulation** – Rate (speed) naturally conveys excitement vs. sadness; volume reinforces confidence/energy vs. subdued emotion.
- **Intensity scaling** – A single positive/negative/neutral label is too coarse. Scaling by compound score magnitude gives a much more natural and nuanced voice response.

---

## Dependencies

| Package | Purpose |
|---|---|
| `pyttsx3` | Offline Text-to-Speech engine |
| `nltk` | Natural Language Toolkit (VADER sentiment analyser) |
