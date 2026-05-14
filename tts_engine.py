"""
TTS Engine using espeak (offline, no internet needed).
Works on Linux servers including PythonAnywhere free tier.
"""

import os
import subprocess


def speak_and_save(text: str, rate: int, volume: float, output_path: str) -> str:
    """
    Synthesize text using espeak and save to output_path (.wav).

    Parameters
    ----------
    text        : The string to be spoken.
    rate        : Speaking rate in words-per-minute.
    volume      : Volume level between 0.0 and 1.0.
    output_path : Destination file path (.wav).

    Returns the absolute path of the saved audio file.
    """
    # espeak amplitude range is 0-200
    amplitude = int(volume * 200)

    subprocess.run(
        ["espeak", "-s", str(rate), "-a", str(amplitude), text, "-w", output_path],
        check=True,
    )
    return os.path.abspath(output_path)
