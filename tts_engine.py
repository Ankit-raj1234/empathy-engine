"""
TTS Engine using pyttsx3.
Applies emotion-driven vocal parameter modulation and saves audio to a file.
"""

import os
import pyttsx3


def speak_and_save(text: str, rate: int, volume: float, output_path: str) -> str:
    """
    Synthesize `text` with the given vocal parameters and save to `output_path`.

    Parameters
    ----------
    text        : The string to be spoken.
    rate        : Speaking rate in words-per-minute (e.g. 100–220).
    volume      : Volume level between 0.0 (silent) and 1.0 (loudest).
    output_path : Destination file path (should end with .wav).

    Returns the absolute path of the saved audio file.
    """
    engine = pyttsx3.init()

    # Apply vocal parameters
    engine.setProperty("rate",   rate)
    engine.setProperty("volume", volume)

    # Save to file
    engine.save_to_file(text, output_path)
    engine.runAndWait()

    return os.path.abspath(output_path)


def list_voices() -> list[dict]:
    """Return available TTS voices on this system."""
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    return [{"id": v.id, "name": v.name} for v in voices]
