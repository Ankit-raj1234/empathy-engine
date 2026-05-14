"""
TTS Engine using edge-tts (Microsoft Neural TTS).
Works on all platforms including cloud servers - no system dependencies needed.
Applies emotion-driven vocal parameter modulation and saves audio to a file.
"""

import os
import asyncio
import edge_tts

BASE_RATE_WPM = 155
BASE_VOLUME = 0.78
VOICE = "en-US-AriaNeural"


def _rate_to_percent(rate_wpm: int) -> str:
    """Convert words-per-minute to edge-tts rate percentage string."""
    percent = int(((rate_wpm - BASE_RATE_WPM) / BASE_RATE_WPM) * 100)
    return f"+{percent}%" if percent >= 0 else f"{percent}%"


def _volume_to_percent(volume: float) -> str:
    """Convert 0.0-1.0 volume to edge-tts volume percentage string."""
    percent = int(((volume - BASE_VOLUME) / BASE_VOLUME) * 100)
    return f"+{percent}%" if percent >= 0 else f"{percent}%"


async def _generate_audio(text: str, rate_str: str, volume_str: str, output_path: str):
    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE,
        rate=rate_str,
        volume=volume_str,
    )
    await communicate.save(output_path)


def speak_and_save(text: str, rate: int, volume: float, output_path: str) -> str:
    """
    Synthesize text with emotion-modulated voice and save to output_path (.mp3).

    Parameters
    ----------
    text        : The string to be spoken.
    rate        : Speaking rate in words-per-minute.
    volume      : Volume level between 0.0 and 1.0.
    output_path : Destination file path (should end with .mp3).

    Returns the absolute path of the saved audio file.
    """
    rate_str = _rate_to_percent(rate)
    volume_str = _volume_to_percent(volume)
    asyncio.run(_generate_audio(text, rate_str, volume_str, output_path))
    return os.path.abspath(output_path)
