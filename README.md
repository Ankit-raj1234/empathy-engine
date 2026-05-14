# The Empathy Engine

> **Challenge 1 Submission** - Emotionally Expressive AI Voice Synthesizer

## Overview

The Empathy Engine is a Python web application that **dynamically modulates synthesized speech** based on the detected emotion of the input text. It bridges the gap between plain text-based sentiment and expressive, human-like audio output — moving beyond robotic, monotonic TTS delivery.

---

## Features

- **3-Class Emotion Detection** - Positive, Negative, Neutral (using VADER)
- **Intensity Scaling** - Mild / Moderate / Strong, based on sentiment score magnitude
- **2 Vocal Parameters Modulated** - Speaking Rate (wpm) & Volume
- **Offline & No API Keys Required** - Uses `pyttsx3` (local SAPI5 on Windows)
- **Audio File Output** - Saves a playable `.wav` file for every input
- **Web Interface** - Beautiful dark UI with live audio player (Flask)
- **CLI Mode** - Also works fully from the command line

---

## Project Structure

```
EmpathyEngine/
├── app.py                  # Flask web application (backend)
├── main.py                 # CLI entry point
├── emotion_detector.py     # VADER-based emotion & intensity detection
├── tts_engine.py           # pyttsx3 TTS with vocal parameter modulation
├── requirements.txt        # Python dependencies
├── README.md               # This file
├── templates/
│   └── index.html          # Web UI (dark gradient, audio player)
└── static/
    └── audio/              # Generated .wav files stored here
```

---

## Setup & Installation

### Prerequisites
- Python 3.8 or higher
- Windows / macOS / Linux

### Step 1 - Clone the repository

```bash
git clone https://github.com/Ankit-raj1234/empathy-engine.git
cd empathy-engine
```

### Step 2 - Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3 - VADER lexicon downloads automatically on first run. No extra step needed.

---

## Running the Web App (Recommended)

```bash
python app.py
```

Then open your browser and visit:

```
http://127.0.0.1:5000
```

**How to use:**
1. Type any text in the input box
2. Click **Generate Voice**
3. The detected emotion, sentiment score, rate and volume are displayed
4. The audio player appears and **auto-plays** the generated voice

You can also press `Ctrl + Enter` to generate quickly.

---

## Running via CLI

### Interactive Mode

```bash
python main.py
```

Type text, press Enter, a `.wav` file is saved. Type `quit` to exit.

### Single Text

```bash
python main.py --text "I just got promoted today!"
```

### Custom Output File

```bash
python main.py --text "This is terrible news." --output sad_voice.wav
```

### List Available Voices

```bash
python main.py --voices
```

---

## Emotion to Voice Mapping

| Emotion            | Rate (wpm) | Volume |
|--------------------|-----------|--------|
| Positive (Mild)    | 165       | 0.80   |
| Positive (Moderate)| 185       | 0.87   |
| Positive (Strong)  | 205       | 0.95   |
| Neutral            | 155       | 0.78   |
| Negative (Mild)    | 140       | 0.72   |
| Negative (Moderate)| 120       | 0.65   |
| Negative (Strong)  | 100       | 0.55   |

**Logic:** VADER's compound score determines emotion class (`>= 0.05` = Positive, `<= -0.05` = Negative, else Neutral). The magnitude of the compound score determines intensity (`< 0.3` = mild, `0.3-0.6` = moderate, `> 0.6` = strong), which scales the vocal parameters accordingly.

---

## Example Outputs

| Input Text | Detected Emotion | Rate | Volume |
|---|---|---|---|
| `"I just got promoted! This is the best day ever!"` | Positive (Strong) | 205 wpm | 0.95 |
| `"I'm okay I guess."` | Neutral | 155 wpm | 0.78 |
| `"This is absolutely horrible and frustrating."` | Negative (Strong) | 100 wpm | 0.55 |

---

## Design Choices

- **VADER over TextBlob** - VADER is specifically designed for short conversational texts, giving more accurate results without needing a trained ML model.
- **pyttsx3 for TTS** - Fully offline, no API keys, works on all platforms using Windows SAPI5.
- **Rate + Volume modulation** - Rate (speed) naturally conveys excitement vs. sadness; volume reinforces energy vs. subdued emotion.
- **Intensity scaling** - A single positive/negative/neutral label is too coarse. Scaling by compound score magnitude gives a much more natural voice response.
- **Flask Web UI** - Makes the project easy to demo with a live audio player instead of manually opening `.wav` files.

---

## Dependencies

| Package   | Purpose                              |
|-----------|--------------------------------------|
| `pyttsx3` | Offline Text-to-Speech engine        |
| `nltk`    | VADER sentiment analyser             |
| `flask`   | Web framework for the UI             |
